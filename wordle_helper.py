import json

with open("words.json", 'r') as f:
    data = json.load(f)

words = data['words']

# init
fault = ""  # gray spot
pos_wrong = ["", "", "", "", ""]    # yellow spot
right = ["", "", "", "", ""]    # green spot

# hint
print(40*"-")
print("The Best Starting Word in WORDLE may is 'SOARE'")
print("for result, gray:0 yellow:1 green:2")
print(40*"-")


for i in range(5):

    # handle input
    guess = input("{0}：".format(i+1))
    results = input("result:")
    for n in range(len(results)):
        if results[n] == "0":
            fault = fault + guess[n]
        elif results[n] == "1":
            pos_wrong[n] = pos_wrong[n] + guess[n]
        elif results[n] == "2":
            right[n] = guess[n]
        else:
            print("bad input")

    # suggest
    temp_list = []
    for word in words:
        # check gray (fault case)
        flag = True
        for f in fault:
            if f in word:
                flag = False
                break

        if not flag:
            continue

        for n in range(5):

            # check green (right case)
            if right[n] != "" and right[n] != word[n]:
                flag = False
                break

            # check yellow (pos wrong)
            if pos_wrong[n] != "":
                for ps in pos_wrong[n]:
                    # skip if have yellow spot letter or not
                    if ps not in word:
                        flag = False
                        break
                    else:
                        # check if still in wrong position
                        if word.index(ps) == n:
                            flag = False
                            break

        if not flag:
            continue

        temp_list.append(word)
    print("suggest:", temp_list)
    word = temp_list.copy()
    print(40*"-")
