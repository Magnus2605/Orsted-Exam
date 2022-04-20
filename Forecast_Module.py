import pandas as pd                                             #Importering af pandas bibliotek (Beregning)
import matplotlib.pyplot as plt                                 #Importering af matplotlib.pyplot bibliotek (Plotting)
import csv                                                      #Importering af csv modul (Behandling)

print('Hej, og velkommen til vejrudsigtsmodulet, før du kan få indsigt skal du logge ind.\n')

class Login():                                          #Definerer en class som indeholer en række funktioner.

    def __init__(self):                                 #Definerer opstarts funktionen. Denne funktion kører når Login() kører.

        self.brugernavn = input('Arbejdsmail : ')       #Definerer brugernavn som et input fra bruger
        self.adgangskode = input('Adgangskode : ')      #Definerer adgangskode som et input fra bruger

    def login_check(self):                              #login_check funktion. " By using the “self” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments. " (https://www.geeksforgeeks.org/self-in-python-class/)

        file = open("Login.txt","r")                    #Åbner Login.txt fil i read mode "r". Der kan kun læses i filen i dette mode.

        if '@' not in self.brugernavn:                  #If statement. Hvis @ ikke er en del af brugernavnet gør dette:
            print('Arbejdsmail skal indeholde @')
            print('Log venligst ind igen')
            login = Login()                             #Kører Login() class på ny
            login.login_check()                         #Kører login_check class efter __init__ class.

        elif self.brugernavn and self.adgangskode in file:      #Elif statement. Elif bruges, da der er flere "if". Hvis brugernavn og adgangskode er i fil gør dette:
            print('\nVelkommen', self.brugernavn)

        else:                                                   #else statement. Hvis brugernavn og adgangskode ikke er i fil gør dette:
            question = input("\nArbejdsmail eller Adgangskode er forkert. \nHar du godkendt dine login oplysninger? ja/nej : ")

            if question == 'ja':                                #if statement. Hvis input = "ja" gør dette:
                print('Prøv venligst at logge ind igen')
                login = Login()                                 #Kører Login() class på ny
                login.login_check()                             #Kører login_check class efter __init__ class.

            elif question == "nej":                             #elif statement. Hvis input = "nej" gør dette:
                print('Du skal skrive din arbejdsmail og adgangskode første gang du logger ind.')
                print('Dette skal du gøre for at godkende dine oplysingner i vores system.')
                self.approve_login()                            #Kører funktionen approve_login()

            else:                                               #else start på ny.
                login = Login()
                login.login_check()

    def approve_login(self):                                                            #approve_login funktion. Godkender login.

        file = open("Login.txt", "a")                                                   #Åbner .txt fil i append mode "a". I dette mode er det kun muligt at tilføje noget til filen.

        file.write("\n" + input('Arbejdsmail : '))                                      #.write gør at man kan skrive noget der bliver tilføjet til filen. Her er det brugerens input der bliver tilføjet.
        file.write("\n" + input('Adgangskode : '))
        print("Login godkendes")
        print('Login er godkendt i vores system. Prøv venligst at logge ind igen.')

        file.close()                                                                    #Lukker filen Login.txt der er blevet navngivet "file" i 46.

        login = Login()                                                                 #Starter på ny.
        login.login_check()

login = Login()                     #Kører Login() class og dermed __init__
login.login_check()                 #Kører login_check class efter __init__ class.

class Menu():                       #Definerer Menu() som en class

    #Menu der viser valgmuligheder
    def __init__(self):
        print("----------------------------------------------------------------------------------")
        print("MENU")
        print("1. Se datointerval og antal af målinger.")
        print("2. Se den maksimale vindhastighed for hver enkel dag og samlet for alle dage.")
        print("3. Se graf der viser hyppigheden for vindretningerne.")
        print("4. Se graf der viser middelhastighed for hver vindretning.")
        print("5. Se graf der viser vindretningen for hver enkel dato.")
        print("6. Afslut")
        print("----------------------------------------------------------------------------------")

    #Funktion hvor der vælges hvilket menupunkt man ønsker at tilgå. Består af "if", "elif" og "else" statements.
    def choice(self):

        choice = input("\n" + "Venligst vælg hvilket menupunkt du ønsker at tilgå." + "\n" + "Du vælger menupunkt ved at taste det nummer der står ud for det menupunkt du ønsker at vælge. (1, 2, 3, 4, 5, 6)" + "\n")

        if choice == "1":
            choice1 = choice_1()
            choice1.date_interval()
            choice1.row_count()

        elif choice == "2":
            choice2 = choice_2()
            choice2.max_windspeed_per_day()
            choice2.max_windspeed_period()
            choice2.plot_max_windspeed_per_day()

        elif choice == "3":
            choice3 = choice_3()
            choice3.filter_windspeed()
            choice3.wind_direction_frequency()
            choice3.plot_wind_direction_frequency()

        elif choice == "4":
            choice4 = choice_4()
            choice4.filter_windspeed()
            choice4.mean_windspeed()
            choice4.plot_mean_windspeed()

        elif choice == "5":
            choice5 = choice_5()
            choice5.filter_windspeed()
            choice5.plot_wind_direction_per_day()

        elif choice == "6":                             #Afslutter programmet
            exit()
        else:
            self.choice()                               #Hvis nummeret der indtastes ikke stemmer overens med nummeret i menuen, sendes brugeren tilbage til valg af menupunkt(choice(self)).

    def return_or_leave(self):

        print("----------------------------------------------------------------------------------")
        print("1. Gå tilbage til menu")
        print("2. Afslut")
        print("----------------------------------------------------------------------------------")

        return_or_leave = input("Vælg venligst ved at taste 1 eller 2\n")

        if return_or_leave == "1":
            menu = Menu()           #Kører Menu class på ny med __init__ først
            menu.choice()           #Kører choice() funktion efter __init__ funktion.

        elif return_or_leave == "2":
            exit()                  #Afslutter programmet/script

        else:
            self.return_or_leave()  #Kører return_or_leave funktion på ny.


#Class hvor der vises datointerval og antal af målinger.
class choice_1():

    def date_interval(self):

        fh = open('WindData.csv', 'r')                  #Åbner og læser hvad der står i .csv filen
        csvreader = csv.reader(fh, delimiter = ';')     #Laver hver linje i csv filen til en liste. Denne liste opstår af strings sepereret af kommaer. En ny liste skabes efter hvert linjeskift. I WindData.csv er delimiteren (;). Delimiter er der hvor kolonner i csv filen skifter.
        next(csvreader)                                  #Springer den øverste linje over (header). Bruges for at undgå at overskrifterne tælles med i beregninger.

        TimestampList = []                               #Fortæller at der er tale om en liste
        WindDirectionList = []
        WindSpeedList = []

        for row in csvreader:                                               #For linjer i .csv filen gør dette.
            if any(row):                                                    #Tjekker om der eksisterer linjer med data.
                TimestampList.append(row[0])                                #laver en liste ud fra tidspunkter opgivet i csv filen. Listen indeholder al data der står på kolonne med index 0 i .csv filen (csvreader).
                WindDirectionList.append(row[1])                            #Kolonne index 1 til liste.
                WindSpeedList.append(row[2])                                ##Kolonne index 2 til liste.

        Date_interval = [TimestampList[-1] + " til " + TimestampList[0]]      #Printer det sidste og det første i listen over tidspunkter. Printer index [-1] og [0] i listen "TimestampList".

        print ("\nDatointervallet for samtlige målinger er:\n",Date_interval)
        fh.close()                                      #Lukker fil

    def row_count(self):

        fh = open('WindData.csv', 'r')                  #Åbner og læser hvad der står i .csv filen
        csvreader = csv.reader(fh, delimiter = ';')     #Laver hver linje i csv filen til en liste. Denne liste opstår af strings sepereret af kommaer. En ny liste skabes efter hvert linjeskift. I WindData.csv er delimiteren (;)
        next(csvreader)                                 #Springer den øverste linje over (header)
        rows = len(list(csvreader))                    #Finder hvor mange lister der er i listerne baseret på .csv filen. Mængden af lister må blive det samme som mængden af linjer, da listen laves efter linjeskift.

        print("\nAntal af målinger ialt =", rows, "\n")           #Printer antallet af linjer
        fh.close()                                      #Lukker fil
        menu.return_or_leave()                          #Kører return_or_leave() funktion i Menu() class

# Class hvor der vises den maksimale vindhastighed for hver enkel dag og samlet for alle dage.
class choice_2():

    def max_windspeed_per_day(self):

        winddata = pd.read_csv('WindData.csv', parse_dates=[0], dayfirst=True, sep = ';', decimal=',')  #Bruger pandas til at åbne .csv filen "pd.read_csv". parse_dates laver dataformatet om således at pandas kan forstå det. Datoen står i kolonne med index [0]. dayfirst=True fortæller pandas at i vores datoer står dagen først. sep = ';' fortæller at kolonner skifter ved semikolon. decimal = ',' fortæller at istedet for at bruge punktum bruger vi komma som decimal.

        self.max_windspeed_per_day = winddata.groupby(pd.Grouper(key='Timestamp', freq='1D')).max()          #Gruppere dataen i winddata. key='Timestamp' fortæller at det er "Timestamp" kolonnen der grupperes efter. freq='1D' fortæller at vi ønsker at se data per dag. .max() fortæller at det er den højeste værdi vi ønsker at se per dag.
        print("De maksimale opnåede vindhastighedheder for hver enkel dag:\n")
        print("--------------------------------------------------------------------------")
        print(self.max_windspeed_per_day)
        print("--------------------------------------------------------------------------")

    def max_windspeed_period(self):

        winddata = pd.read_csv('WindData.csv', parse_dates=[0], dayfirst=True, sep = ';', decimal=',')  #Bruger pandas til at åbne .csv filen "pd.read_csv". parse_dates laver dataformatet om således at pandas kan forstå det. Datoen står i kolonne med index [0]. dayfirst=True fortæller pandas at i vores datoer står dagen først. sep = ';' fortæller at kolonner skifter ved semikolon. decimal = ',' fortæller at istedet for at bruge punktum bruger vi komma som decimal.

        print("\nDen maksimale opnået vindhastighed for hele perioden:\n")
        self.max_windspeed_period = winddata['WindSpeed'].max()                                                  #finder max værdien for WindSpeed. winddata['WindSpeed'] fortæller at det er "WindSpeed" kolonnen i winddata. .max() at det er den højeste værdi i den kolonne.
        print("--------------------------------------------------------------------------")
        print(self.max_windspeed_period, "m/s")
        print("--------------------------------------------------------------------------")

    def plot_max_windspeed_per_day(self):

        answer = input("Ønsker du at se en graf over de maksimale opnåede vindhastigheder for hver enkel dag? (ja/nej)")

        if answer == "ja" or "Ja":
            #Plotter en graf over de maksimale opnåede vindhastigheder for hver enkel dag.
            plt.plot(self.max_windspeed_per_day.index, self.max_windspeed_per_day["WindSpeed"], '-o') #max_windspeed_per_day.index fortæller at det er første kolonne(Timestamp) der skal stå på x aksen. max_windspeed_per_day["WindSpeed"] fortæller at det er WindSpeed kolonnen på y aksen. '-o' fotæller at der skal være streger mellem punkterne.
            plt.xlabel("Dato")                                                              #Hvad der skal stå på x aksen
            plt.ylabel("Vindhastighed i m/s")                                               #Hvad der skal stå på y aksen
            plt.title("Maksimalt opnåede vindhastigheder for hver enkel dag")               #Hvad der skal stå som titel
            manager = plt.get_current_fig_manager()                                         #Henter funktion fra plt bibliotek.
            manager.full_screen_toggle()                                                    #Gør at grafen åbner i fuldskærm
            plt.show()                                                                      #Viser graf

            menu.return_or_leave()                          #Kører return_or_leave() funktion i Menu() class

        elif answer == "nej" or "Nej":
            menu.return_or_leave()                          #Kører return_or_leave() funktion i Menu() class


    #class der viser graf over hyppigheden for vindretningerne
class choice_3():

    def filter_windspeed(self):

        winddata = pd.read_csv('WindData.csv', sep = ';', decimal=',')      #Åbner csv filen som winddata i read mode. sep bruges for at fortælle at der bruges semikolon mellem datakolonner og ikke ','. decimal fortæller at vi bruger ',' og ikke '.' som decimal.

        self.filter_windspeed = []                                       #Laver en liste, hvori de filtrerede værdier kommer til at være.

        for windspeed in winddata.WindSpeed:                        #Et for loop der filtrere, således at vi kun har vores ønskede værdier. De ønskede værdier gemmes i vores liste filter_windspeed.
            if ((windspeed >= 2.5) and (windspeed <= 25)):
                self.filter_windspeed.append(True)                       #Hvis dataen er indenfor værdierne tilføjes de til listen via .append. BOOLEAN
            else:
                self.filter_windspeed.append(False)                      #Hvis dataen ikke er indenfor værdierne tilføjes de ikke til listen via .append. BOOLEAN

        convert_filter_windspeed = pd.Series(self.filter_windspeed)      #Konverterer vores liste filter_windspeed[] til pandas serie. Dette gør at data bliver opstillet som et dataframe og ikke liste. Dette dataframe består af True og False statements for WindSpeed.
        self.winddata_filter = winddata[convert_filter_windspeed]        #Koverterer vores true/false dataframe til et samlet dataframe hvor alle false statements er filtreret fra. winddata[convert_filter_windspeed] winddata fortæller at det er det samlede dataframe.[convert_filter_windspeed] fortæller at linjer med WindSpeed under 2.5 eller over 25 skal filtreres fra.

    def wind_direction_frequency(self):

        East = self.winddata_filter[(self.winddata_filter['WindDirection'] > 45) & (self.winddata_filter['WindDirection'] <= 135)]     #Viser kun resultater over 45 eller under eller lig med 135 for WindDirection.
        South = self.winddata_filter[(self.winddata_filter['WindDirection'] > 135) & (self.winddata_filter['WindDirection'] <= 225)]   #Viser kun resultater over 135 eller under eller lig med 225 for WindDirection.
        West = self.winddata_filter[(self.winddata_filter['WindDirection'] > 225) & (self.winddata_filter['WindDirection'] <= 315)]    #Viser kun resultater over 225 eller under eller lig med 315 for WindDirection.
        North315 = self.winddata_filter[(self.winddata_filter['WindDirection'] > 315)]                                            #Viser kun resultater over 315 for WindDirection.
        North45 = self.winddata_filter[(self.winddata_filter['WindDirection'] <= 45)]                                             #Viser kun resultater under eller lig med 45 for WindDirection.
        North = North315.append(North45)                                            #Tilføjer North45 til North315 således at de tilsammen udgør alle resultater for vindretningen North

        self.Winddirection_East = len(East)          #giver antal målinger for "East" eller længden af data rækker for "East"
        self.Winddirection_South = len(South)
        self.Winddirection_West = len(West)
        self.Winddirection_North = len(North)

    def plot_wind_direction_frequency(self):

        wind_direction_frequency_list = [self.Winddirection_East, self.Winddirection_South, self.Winddirection_West, self.Winddirection_North]      #Liste med de forskellige længder af datarækker.
        winddirections = ["Øst", "Syd", "Vest", "Nord"]     #Liste med vindretninger.

        plt.bar(winddirections, wind_direction_frequency_list, color ='blue')       #bar fortæller at det er et søjlediagram. winddirections på x aksen. wind_direction_frequency_list på y aksen. farve blå.
        plt.xlabel("Vindretning")                                                   #Skrift på x akse
        plt.ylabel("Hyppigheden målt i antal tidspunkter")                          #Skrift på y akse
        plt.title("Hyppigheden for vindretningerne Ø, S, V og Nord")                #Skrift på titel
        manager = plt.get_current_fig_manager()                                     #Henter funktion fra plt bibliotek.
        manager.full_screen_toggle()                                                #Gør at grafen åbner i fuldskærm
        plt.show()                                                                  #Viser graf

        menu.return_or_leave()                          #Kører return_or_leave() funktion i Menu() class

#Funktion der viser graf over middelhastighed for hver vindretning.
class choice_4():

    def filter_windspeed(self):

        winddata = pd.read_csv('WindData.csv', sep = ';', decimal=',')      #Åbner csv filen som winddata i read mode. sep bruges for at fortælle at der bruges semikolon mellem datakolonner og ikke ','. decimal fortæller at vi bruger ',' og ikke '.' som decimal.

        self.filter_windspeed = []                                       #Laver en liste, hvori de filtrerede værdier kommer til at være.

        for windspeed in winddata.WindSpeed:                        #Et for loop der filtrere, således at vi kun har vores ønskede værdier. De ønskede værdier gemmes i vores liste filter_windspeed.
            if ((windspeed >= 2.5) and (windspeed <= 25)):
                self.filter_windspeed.append(True)                       #Hvis dataen er indenfor værdierne tilføjes de til listen via .append. BOOLEAN
            else:
                self.filter_windspeed.append(False)                      #Hvis dataen ikke er indenfor værdierne tilføjes de ikke til listen via .append. BOOLEAN

        convert_filter_windspeed = pd.Series(self.filter_windspeed)      #Konverterer vores liste filter_windspeed[] til pandas serie. Dette gør at data bliver opstillet som et dataframe og ikke liste. Dette dataframe består af True og False statements for WindSpeed.
        self.winddata_filter = winddata[convert_filter_windspeed]        #Koverterer vores true/false dataframe til et samlet dataframe hvor alle false statements er filtreret fra. winddata[convert_filter_windspeed] winddata fortæller at det er det samlede dataframe.[convert_filter_windspeed] fortæller at linjer med WindSpeed under 2.5 eller over 25 skal filtreres fra.

    def mean_windspeed(self):

        East = self.winddata_filter[(self.winddata_filter['WindDirection'] > 45) & (self.winddata_filter['WindDirection'] <= 135)]     #Viser kun resultater over 45 eller under eller lig med 135 for WindDirection.
        South = self.winddata_filter[(self.winddata_filter['WindDirection'] > 135) & (self.winddata_filter['WindDirection'] <= 225)]   #Viser kun resultater over 135 eller under eller lig med 225 for WindDirection.
        West = self.winddata_filter[(self.winddata_filter['WindDirection'] > 225) & (self.winddata_filter['WindDirection'] <= 315)]    #Viser kun resultater over 225 eller under eller lig med 315 for WindDirection.
        North315 = self.winddata_filter[(self.winddata_filter['WindDirection'] > 315)]                                            #Viser kun resultater over 315 for WindDirection.
        North45 = self.winddata_filter[(self.winddata_filter['WindDirection'] <= 45)]                                             #Viser kun resultater under eller lig med 45 for WindDirection.
        North = North315.append(North45)                                            #Tilføjer North45 til North315 således at de tilsammen udgør alle resultater for vindretningen North

        self.Average_windspeed_East = East['WindSpeed'].mean()       #Giver gennemsnittet for WindSpeed i dataframe East
        self.Average_windspeed_South = South['WindSpeed'].mean()
        self.Average_windspeed_West = West['WindSpeed'].mean()
        self.Average_windspeed_North = North['WindSpeed'].mean()

    def plot_mean_windspeed(self):

        average_windspeed_list = [self.Average_windspeed_East, self.Average_windspeed_South, self.Average_windspeed_West, self.Average_windspeed_North]     #Liste over gennemsnit for WindSpeed for hver vindretning.
        winddirections = ["Øst", "Syd", "Vest", "Nord"]     #Liste over vindretninger

        plt.bar(winddirections, average_windspeed_list, color ='blue')              #bar fortæller at det er et søjlediagram. winddirections på x aksen. average_windspeed_list på y aksen. farve blå.
        plt.xlabel("Vindretning")                                                   #Skrift på x akse
        plt.ylabel("Gennemsnitlig vindstyrke i m/s")                                #Skrift på y akse
        plt.title("Gennemsnitlig vindstyrke for Ø, S, V og Nord")                   #Skrift på titel
        manager = plt.get_current_fig_manager()                                     #Henter funktion fra plt bibliotek.
        manager.full_screen_toggle()                                                #Gør at grafen åbner i fuldskærm
        plt.show()                                                                  #Viser graf

        menu.return_or_leave()                          #Kører return_or_leave() funktion i Menu() class

#Funktion der viser graf over vindretningen for hver enkel dato.
class choice_5():

    def filter_windspeed(self):

        winddata = pd.read_csv('WindData.csv', parse_dates=[0], dayfirst=True, sep = ';', decimal=',')      #Bruger pandas til at åbne .csv filen "pd.read_csv". parse_dates laver dataformatet om således at pandas kan forstå det. Datoen står i kolonne med index [0]. dayfirst=True fortæller pandas at i vores datoer står dagen først. sep = ';' fortæller at kolonner skifter ved semikolon. decimal = ',' fortæller at istedet for at bruge punktum bruger vi komma som decimal.

        self.filter_windspeed = []                                       #Laver en liste, hvori de filtrerede værdier kommer til at være.

        for windspeed in winddata.WindSpeed:                        #Et for loop der filtrere, således at vi kun har vores ønskede værdier. De ønskede værdier gemmes i vores liste filter_windspeed.
            if ((windspeed >= 2.5) and (windspeed <= 25)):
                self.filter_windspeed.append(True)                       #Hvis dataen er indenfor værdierne tilføjes de til listen via .append. BOOLEAN
            else:
                self.filter_windspeed.append(False)                      #Hvis dataen ikke er indenfor værdierne tilføjes de ikke til listen via .append. BOOLEAN

        convert_filter_windspeed = pd.Series(self.filter_windspeed)      #Konverterer vores liste filter_windspeed[] til pandas serie. Dette gør at data bliver opstillet som et dataframe og ikke liste. Dette dataframe består af True og False statements for WindSpeed.
        self.winddata_filter = winddata[convert_filter_windspeed]        #Koverterer vores true/false dataframe til et samlet dataframe hvor alle false statements er filtreret fra. winddata[convert_filter_windspeed] winddata fortæller at det er det samlede dataframe.[convert_filter_windspeed] fortæller at linjer med WindSpeed under 2.5 eller over 25 skal filtreres fra.

    def plot_wind_direction_per_day(self):

        plt.plot(self.winddata_filter["Timestamp"], self.winddata_filter["WindDirection"], '-o')  #"Timestamp" skal stå på x aksen. "WindDirection" skal stå på y aksen. '-o' fotæller at der skal være streger mellem punkterne.
        plt.xlabel("Tidspunkter")                                                   #Skrift på x akse
        plt.ylabel("Vindretning i grader for hvert tidspunkt")                      #Skrift på y akse
        plt.title("Vindretning i grader. Øst(>45 - <=135), Syd(>135 - <=225), Vest(>225 - <=315), Nord(>315 - <=45)")  #Skrift på titel
        manager = plt.get_current_fig_manager()                                     #Henter funktion fra plt bibliotek.
        manager.full_screen_toggle()                                                #Gør at grafen åbner i fuldskærm
        plt.show()                                                                  #Viser graf

        menu.return_or_leave()                          #Kører return_or_leave() funktion i Menu() class


menu = Menu()   #Kører Menu() class
menu.choice()   #Kører choice() funktion i Menu() class
