import pickle
import class_definitions as cd

# test1 = cd.Admin("Locke", "888-777-6666", "gvlocke@locke.com", "1234", "GVLocke")
test1 = cd.User("John", "888-777-6666", "bruh@bruh.bruh", "1234", "Bruh")
with open("dealership.dat", "ab") as f:
    pickle.dump(test1, f)
f.close()