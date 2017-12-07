# Maplestory

import Character
import Field
import GameState
import Npc
import Quest
import Terminal
import time

Terminal.SetRushByLevel(False)

while True:
    time.sleep(1)
    level = Character.GetLevel()

    if not GameState.IsInGame():
        continue

    if Terminal.IsRushing():
        continue

    if level < 140:
        continue

    fieldID = Field.GetID()

    # Gets statuses on quests required
    quest1 = Quest.GetQuestState(17600)
    quest2 = Quest.GetQuestState(17601)
    quest3 = Quest.GetQuestState(17602)
    quest4 = Quest.GetQuestState(17603)
    quest5 = Quest.GetQuestState(17608)
    quest6 = Quest.GetQuestState(17610)
    quest7 = Quest.GetQuestState(17611)
    quest8 = Quest.GetQuestState(17612)
    quest9 = Quest.GetQuestState(17613)
    quest10 = Quest.GetQuestState(17614)
    quest11 = Quest.GetQuestState(17615)
	quest12 = Quest.GetQuestState(17616)
	quest13 = Quest.GetQuestState(17617)
	quest14 = Quest.GetQuestState(17618)
	quest15 = Quest.GetQuestState(17619)
	quest16 = Quest.GetQuestState(17620)
	quest17 = Quest.GetQuestState(17621)
	quest18 = Quest.GetQuestState(17622)
	quest19 = Quest.GetQuestState(17623)
	quest20 = Quest.GetQuestState(17624)
	quest21 = Quest.GetQuestState(17625)
	quest22 = Quest.GetQuestState(17626)
	quest23 = Quest.GetQuestState(17627)
	quest24 = Quest.GetQuestState(17628)
	quest25 = Quest.GetQuestState(17629)
	quest26 = Quest.GetQuestState(17630)
	quest27 = Quest.GetQuestState(17631)
	quest28 = Quest.GetQuestState(17632)
	quest29 = Quest.GetQuestState(17633)
	quest30 = Quest.GetQuestState(17634)
	quest31 = Quest.GetQuestState(17635)
	quest32 = Quest.GetQuestState(17636)
	quest33 = Quest.GetQuestState(17637)
	quest34 = Quest.GetQuestState(17638)
	quest35 = Quest.GetQuestState(17639)
	quest36 = Quest.GetQuestState(17640)
	quest37 = Quest.GetQuestState(17641)
	quest38 = Quest.GetQuestState(17642)
	quest39 = Quest.GetQuestState(17643)
	quest40 = Quest.GetQuestState(17644)
	quest41 = Quest.GetQuestState(17645)
	quest42 = Quest.GetQuestState(17678)
	quest43 = Quest.GetQuestState(17679)
	quest44 = Quest.GetQuestState(17680)
	quest45 = Quest.GetQuestState(17646)
	quest46 = Quest.GetQuestState(17647)
	quest47 = Quest.GetQuestState(17648)
	quest48 = Quest.GetQuestState(17649)
	quest49 = Quest.GetQuestState(17650)
	quest50 = Quest.GetQuestState(17651)
	quest51 = Quest.GetQuestState(17652)
	quest52 = Quest.GetQuestState(17653)
	quest53 = Quest.GetQuestState(17654)
	quest54 = Quest.GetQuestState(17655)
	quest55 = Quest.GetQuestState(17656)
	quest56 = Quest.GetQuestState(17657)
	quest57 = Quest.GetQuestState(17658)
	quest58 = Quest.GetQuestState(17659)
	quest59 = Quest.GetQuestState(17660)
	quest60 = Quest.GetQuestState(17661)
	quest61 = Quest.GetQuestState(17662)
	quest62 = Quest.GetQuestState(17663)
	quest63 = Quest.GetQuestState(17664)
	quest64 = Quest.GetQuestState(17665)
	quest65 = Quest.GetQuestState(17666)
	quest66 = Quest.GetQuestState(17667)
	quest67 = Quest.GetQuestState(17668)
	quest68 = Quest.GetQuestState(17669)
	quest69 = Quest.GetQuestState(17670)
	quest70 = Quest.GetQuestState(17671)
	quest71 = Quest.GetQuestState(17672)
	quest72 = Quest.GetQuestState(17673)
	quest73 = Quest.GetQuestState(17674)
	quest74 = Quest.GetQuestState(17675)
	quest75 = Quest.GetQuestState(17676)
	quest76 = Quest.GetQuestState(17677)
	quest77 = Quest.GetQuestState(17681)
	
	
    # Completing [Commerci Republic] Neinheart's Call
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(17600, 1101002)
        elif quest1 == 1:
            Quest.CompleteQuest(17600, 1101002)

    # Completing [Commerci Republic] In the Name of the Empress
    elif quest2 != 2:
        if quest2 == 0:
            if fieldID != 130000000:
                Terminal.Rush(130000000)
            else:
                Quest.StartQuest(17601, 1101000)
        elif quest2 == 1:
            Quest.CompleteQuest(17601, 1101000)

    # Completing [Commerci Republic] Neinheart's Request
    elif quest3 != 2:
        if quest3 == 0:
            if fieldID != 130000000:
                Terminal.Rush(130000000)
            else:
                Quest.StartQuest(17602, 1101002)
        elif quest3 == 1:
            if fieldID != 104000000:
                Terminal.Rush(104000000)
            else:
                Quest.CompleteQuest(17602, 9390200)

    # Completing [Commerci Republic] Parbell, World's 'Greatest' Explorer
    elif quest4 != 2:
        if quest4 == 0:
            if fieldID != 104000000:
                Terminal.Rush(104000000)
            else:
                Quest.StartQuest(17603, 9390200)

    # Completing [Commerci Republic] After a Pleasant Voyage
    elif quest5 != 2:
        if quest5 == 1:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.CompleteQuest(17608, 9390201)

    # Completing [Commerci Republic] Berry Concerned 1
    elif quest6 != 2:
        if quest6 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.StartQuest(17610, 9390201)
                time.sleep(1)
        elif quest6 == 1:
            if Quest.CheckCompleteDemand(17610, 9390201) == 0:
                if fieldID != 865010200:
                    Terminal.Rush(865010200)
                else:
                    Quest.CompleteQuest(17610, 9390201)
            else:
                if fieldID != 865010100:
                    Terminal.Rush(865010100)

    # Completing [Commerci Republic] Berry Concerned 2
    elif quest7 != 2:
        if quest7 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.StartQuest(17611, 9390201)
                time.sleep(1)
        elif quest7 == 1:
            if Quest.CheckCompleteDemand(17611, 9390201) == 0:
                if fieldID != 865010200:
                    Terminal.Rush(865010200)
                else:
                    Quest.CompleteQuest(17611, 9390201)
            else:
                if fieldID != 865010000:
                    Terminal.Rush(865010000)

    # Completing [Commerci Republic] The Problem with Presumptions
    elif quest8 != 2:
        if quest8 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Npc.RegisterSelection("(There's no better time to tell him the truth.)")
                Quest.StartQuest(17612, 9390201)

    # Completing [Commerci Republic] The Minister's Son
    elif quest9 != 2:
        if quest9 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.StartQuest(17613, 9390201)
        elif quest9 == 1:
            if Quest.CheckCompleteDemand(17613, 9390241) == 0:
                if fieldID not in [865010200, 865090001]:
                    Terminal.Rush(865010200)
                else:
                    Quest.CompleteQuest(17613, 9390241)
            else:
                if fieldID not in [865010200, 865090001]:
                    Terminal.Rush(865010200)
                else:
                    if fieldID == 865010200:
                        Character.AMoveX(851)

    # Completing [Commerci Republic] Ciao, Until Next Time
    elif quest10 != 2:
        if quest10 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.StartQuest(17614, 9390241)
        elif quest10 == 1:
            if fieldID != 865000000:
                Terminal.Rush(865000000)

    # Completing [Commerci Republic] The Trade Kingdom
    elif quest11 != 2:
        if quest10 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.StartQuest(17614, 9390241)
        elif quest10 == 1:
            if fieldID != 865000000:
                Terminal.Rush(865000000)

	# Completing [Commerci Republic] Stolen Items
	
	elif quest12 != 2:
        if quest12 == 0:
            if fieldID != 865000001:
                Terminal.Rush(865000001)
            else:
                Quest.StartQuest(17616, 9390217)
        elif quest12 == 1:
            if fieldID != 865000001:
                Terminal.Rush(865000001)
			else CompleteQuest(17616, 9390220)
				
	# Completing [Commerci Republic] Missing Goods
	
	elif quest13 != 2:
        if quest13 == 0:
            if fieldID != 865000001:
                Terminal.Rush(865000001)
            else:
                Quest.StartQuest(17617, 9390220)
				Sleep(10)
				Quest.StartQuest(17618, 0)
				Sleep(20)
				CompleteQuest(17618, 9390204)
	
	# Completing [Commerci Republic] Come Back Here!
	
	elif quest15 != 2:
        if quest15 == 0:
            Quest.StartQuest(17617, 9390220)
			Sleep(10)
			Quest.StartQuest(17618, 0)
			Sleep(20)
			CompleteQuest(17618, 9390204)
            else:
            Quest.StartQuest(17617, 9390220)
        elif quest15 == 1:
            if fieldID != 865000000:
                Terminal.Rush(865000000)
			else CompleteQuest(17619, 9390217)
				
	# Completing [Commerci Republic] Eye for an Eye
	
	elif quest16 != 2:
        if quest16 == 0:
            if fieldID != 865000000:
                Terminal.Rush(865000000)
            else:
                StartQuest(17620, 9390217)
        elif quest16 == 1:
            if fieldID != 865000002:
                Terminal.Rush(865000002)
			else CompleteQuest(17620, 9390203)
	
	# Completing [Commerci Republic] Gilberto Daniella
	
	elif quest17 != 2:
        if quest17 == 0:
            if fieldID != 865000002:
                Terminal.Rush(865000002)
            else:
                StartQuest(17621, 9390203)
        elif quest16 == 1:
            if fieldID != 865000002:
                Terminal.Rush(865000002)
            else:
                StartQuest(17621, 9390203)
	
	# Completing [Commerci Republic] Gilberto's Reaction
	
	elif quest18 != 2:
        if quest18 == 0:
            if fieldID != 865000002:
                Terminal.Rush(865000002)
            else:
                StartQuest(17622, 9390202)
        elif quest18 == 1:
            sleep(5)
	
	# Completing [Commerci Republic] Another Outsider
	
	elif quest19 != 2:
        if quest19 == 0:
            StartQuest(17623, 0)
			Sleep(15)
        elif quest19 == 1:
            Sleep(5)
				
	# Completing [Commerci Republic] Fish Out of Water
	
	elif quest20 != 2:
        if quest20 == 0:
            StartQuest(17624, 9390202)
			Sleep(15)
        elif quest19 == 1:
            Sleep(5)
	# Completing [Commerci Republic] Delfinos? More Like Dead Fishos.
	
	elif quest21 != 2:
        if quest21 == 0:
			if fieldID != 865000002:
                Terminal.Rush(865000002)
			else
            StartQuest(17625, 9390203)
        elif quest19 == 1:
			if fieldID != 865000002:
               Terminal.Rush(865000002)
            else CompleteQuest(17620, 9390203)
			
	# Completing [Commerci Republic] Delfino Deleter 1
	
	elif quest22 != 2:
        if quest22 == 0:
            if fieldID != 865020000:
                Terminal.Rush(865020000)
            else:
                StartQuest(17626, 9390258)
                time.sleep(1)
        elif quest22 == 1:
            if Quest.CheckCompleteDemand(17626, 9390258) == 0:
                if fieldID != 865020000:
                    Terminal.Rush(865020000)
                else:
                    Quest.CompleteQuest(17626, 9390258)
            else:
                if fieldID != 865020000:
                    Terminal.Rush(865020000)
	
	# Completing [Commerci Republic] Delfino Deleter 2
	# Completing [Commerci Republic] Delfino Deleter 3
	# Completing [Commerci Republic] Delfino Deleter 4
	# Completing [Commerci Republic] Delfino Deleter 5
	

    # We're done!
    else:
        break
