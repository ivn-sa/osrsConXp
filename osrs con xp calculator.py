try:
    xpNeeded = float(input("Amount of XP you need: "))
    if xpNeeded > 0:
        typePlank = int(input("What type of plank are you using? \n1.Planks\n2.Oak Planks\n3.Teak Planks\n4.Mahogany "
                              "planks\n"))
        if typePlank in (1, 2, 3, 4):
            if typePlank == 1:
                plankType1 = 29
                plankType2 = 93.65
            elif typePlank == 2:
                plankType1 = 60
                plankType2 = 200
            elif typePlank == 3:
                myth = int(input("Can you make myth cape racks?\n1.Yes\n2.No\n"))
                if myth == 1:
                    plankType1 = 123.33
                elif myth == 2:
                    plankType1 = 90
                else:
                    print("Invalid answer, proceeding assuming you cant make the myth cape racks")
                    plankType1 = 90
                plankType2 = 287.85
            elif typePlank == 4:
                plankType1 = 140
                plankType2 = 346.12
            planksAmount = int(input("Amount of planks you have: "))
        if planksAmount >= 1:
            plank1 = (planksAmount - 1)
            plank2 = 1
            if (planksAmount * plankType2) < xpNeeded:
                print(f"You dont have enough planks for {round(xpNeeded):,} XP, you have {round(planksAmount * plankType2):,} XP if using "
                      f"mahogany homes, or {round(planksAmount * plankType1):,} XP if using regular construction.\nYou'll "
                      f"need at least {round(((xpNeeded/plankType2)-(planksAmount)+1)):,} more planks "
                      f"to get that xp in mahogany homes or "
                      f"{round((xpNeeded/plankType1)-(planksAmount)+1):,} more planks to do it "
                      f"through regular construction")
            elif planksAmount * plankType1 > xpNeeded:
                print(
                    f"You have enough planks to do regular construction for the xp you need, you'll need {round((xpNeeded / plankType1) + 1):,} planks.")
            else:
                print("\nYou have enough to get the xp needed if you also do some mahogany homes")
                while True:
                    plank1 -= 1
                    plank2 += 1
                    xpPlank1 = plank1 * plankType1
                    xpPlank2 = plank2 * plankType2
                    if xpPlank1 + xpPlank2 > xpNeeded:
                        print(f"\nPlanks for regular construction: {round(plank1):,} \nPlanks for Mahogany homes: {round(plank2):,}\nTotal XP: {xpPlank1 + xpPlank2:,}")
                        break
except:
    print("Invalid input")
finally:
    input("\nPress Enter to exit...")