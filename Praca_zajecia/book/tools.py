from datetime import datetime
# locale.setlocale(locale.LC_TIME, "pl_PL.utf8")
#
def dzis():
    return datetime.now().strftime("%Y-%m-%d")


## cos tu poszlo nie tak, a chodzi o to, zeby zdefiniowane dzis z tego pliku uzyc w model.py
