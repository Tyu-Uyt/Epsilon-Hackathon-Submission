import logic

# Initalization
player = 1
player1 = [10, 300, 300, 0, 20, 30, 20, 30, 20, 0, 0, 0, 0, 0, 0, 0, 0, 200]
# list order: 0:people ,1:Food available ,2:water available ,3:Sick ,4: Stability ,5:Opinion ,6:Coins ,7:wood ,8:Stone ,9:Houses ,10:TownHalls ,11: Walls,12:Lumber Mill ,13:Farm ,14:Water Mill,15:Quarries ,16:Hospitals 17:coins
player2 = [15, 300, 300, 0, 50, 30, 50, 23, 20, 0, 0, 0, 0, 0, 0, 0, 0]

logic.TitleScreen()
logic.WriteCommand(player, player1, player2)   


 

