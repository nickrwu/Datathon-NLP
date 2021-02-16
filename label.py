import pandas as pd

# Loading Training Data csv
df = pd.read_csv("TrainingData.csv")
inputRec = 0

results = pd.DataFrame(columns = ['RecordID', 'Form'])

def search(record):
    # Printing Link
    print('\033[1m' +'\nLink:' + '\033[0m', 'https://search-proquest-com.proxy.library.nyu.edu/docview/' + str(record))
    text = df.loc[df['RecordID'] == int(record), 'text'].iloc[0]
    
    # Printing Text
    print('\033[1m' + 'Record Text:' + '\033[0m', text)

    # Defining Target Variable
    target = 0
    # Stores indices to be converted into tuples
    store = [] # Stores tuples

    while target != 'done':
        target = input("\nInput a target string. Type \033[1m'done'\033[0m to input new RecordID.\
            \nPress \033[1mEnter\033[0m to see text again. \033[1m'cl'\033[0m clear the store:\n")
        if target == 'done':
            break

        elif target == '':
            print(text)

        elif target == 'cl':
            store=[]
        
        else:
            try:
                for i in range(len(text)):
                    indices = []
                    # Storing index into indices
                    if text[i:i+len(target)] == target:
                        indices.append(i)
                        indices.append(i+len(target))

                        entity = input("\n Input Entity Type: ")
                        indices.append(entity)

                        tup = tuple(indices)
                        print('\n', tup)

                        store.append(tup)
                print('\n', store)
                continue

            except:
                print('\033[1m' + "\n Target not found" + '\033[0m')
                continue
        
        continue

    append = 0
    while append != 'y' or 'n':
        append = input("\nAppend RecordID? y/n:\n")
        global resultsDF

        if append == 'y':   
            # Appending tuples into Data Frame
            fullForm = ('(\"%s\", {\"entities\": %s }),') % (text, store)

            d = {'RecordID': record, 
                'Form': fullForm
                            }
            resultsDF = pd.DataFrame(d, index=[0])
            break
            
        elif append == 'n':

            resultsDF = pd.DataFrame(columns = ['RecordID', 'Form'], index=[0])
            break
            
        else:
            print("\nInvalid Response. Try again.")
            continue


while inputRec != '':
    inputRec = input("Input a RecordID. If you are finished, press \033[1mEnter\033[0m: \n")
    if inputRec.isnumeric():
        search(inputRec)
        
        results = pd.concat([results, resultsDF], ignore_index=True)
        results = results.dropna()
        print('\n', results, '\n')

    elif inputRec == '':
        # Storing Results into CSV
        print(results.head())

        results.to_csv('./results.csv', index=True, encoding='utf-8')

        break

    else:
        print('\033[1m' + "Invalid RecordID. Please try again.\n" + '\033[0m')
    continue
    

else:
    exit()


