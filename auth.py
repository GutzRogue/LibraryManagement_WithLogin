def register():
    db = open("Log.txt", "r");
    User = input("Create a Username : ");
    Pass1 = input("Create a Password : ");
    Pass2 = input("Confirm Password : ");
    d = [];
    f = [];
    p = 0;
    for i in db:
        a =  i.split(", ");
        for z in a :
            if p%2 != 0:
                z = z[:-1]
                f.append(z);
            else:
                d.append(z);
            p=p+1;
    if Pass1 != Pass2:
        print("Passwords don't match !");
        register();
    else:
        if User in d :
            print("Username is already taken");
            register();
        else:
            db = open("Log.txt", "a");
            db.write(User +", "+Pass1+"\n")
            print("Success !")

def connect():
    db = open("Log.txt", "r");
    User = input("Username : ");
    Pass = input("Pass : ");
    if not len(User or Pass) < 1 :
        d = [];
        f = [];
        p = 0;
        for i in db:
            a = i.split(", ");
            for z in a:
                if p % 2 != 0:
                    z = z[:-1]
                    f.append(z);
                else:
                    d.append(z);
                p = p + 1;
        data = dict(zip(d, f))
        try:
            if data[User]:
                try:
                    if Pass == data[User]:
                        print("Success");
                        print("Hi !", User);
                        library()
                    else :
                        print("username or password invalid ");
                except:
                    print("incorrect pass or user");
            else:
                print("user doesn't exist");
        except:
            print("login error");
    else:
        print("inputs are empty ")
def menu ():
    option = input("login | signup \n")
    if option == "login":
        connect();
    elif option == "signup":
        register();
    else:
        print("invalid option")

def library():
    lib=open("library.txt" ,"r+")
    Name = []
    Author= []
    Type = []
    Pages = []
    Resume = []
    for i in lib :
        (a, b, c, d, e)=i.split("||")
        Name.append(a)
        Author.append(b)
        Type.append(c)
        Pages.append(d)
        Resume.append(e)
    for (a, b, c, d, e) in zip(Name, Author, Type, Pages, Resume):
        print(a +"||"+ b+"||"+c+"||"+d+"||"+e + "\n")
    see = input("would you like adding a new book? y/n").lower()
    if see == "y":
        N = input("What is the name of the book :")
        A = input("What is the name of the author :")
        T = input("What is the type of the book:")
        P = input("How many pages / tomes :")
        R = input("Give us a small resume :")
        lib.write(N+"\t||"+A+"\t||"+T+"\t||"+P+"\t||"+R +"\n")
        lib.flush()
        library()
library();