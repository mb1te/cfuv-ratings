from ratings.models import Abiturient, FieldOfStudy
from bs4 import BeautifulSoup


def process(f):
    soup = BeautifulSoup(f.read(), features='lxml')
    tbl = soup.find_all("tbody")
#    print(len(tbl))
    lst = []
    lst2 = []
    for tr in tbl[26].find_all("tr"):
        newab = Abiturient()
        cur = tr.find_all("td")
#        print(cur)
        newab.fio = cur[2].get_text()
        splitted = cur[3].get_text().split(", ")
        cur_str = splitted[1].split()
#        print(cur_str)
        newab.field = " ".join(cur_str[1:])
        newab.form = splitted[2] + " " + splitted[5]
        code = int(cur_str[0][4])
        newab.type = [0, 0, 0, 'бакалавриат', 'магистратура', 'специалитет', 'аспирантура', 0, 'ординатура'][code]
        if "СОГЛАСИЕ" in newab.form:
            newab.is_accepted = True
        newab.form = " ".join(newab.form.split()[:2])
        newab.res_sum = int(cur[5].get_text())
        newab.min_ball = int(cur[6].get_text())
        newab.cnt_of_places = int(cur[7].get_text())
        newab.cur_place = int(cur[8].get_text())
        newab.__str__()
        lst.append(newab)
        lst2.append(newab.field + " " + newab.type)
#        break
    Abiturient.objects.bulk_create(lst)
    lst3 = []
    for i in set(lst2):
        cur = i.split()
        lst3.append(FieldOfStudy(name=" ".join(cur[:len(cur) - 1]), type=cur[len(cur) - 1]))
    FieldOfStudy.objects.bulk_create(lst3)


Abiturient.objects.all().delete()
FieldOfStudy.objects.all().delete()
process(open("ratings/last/out.txt", "rb"))
process(open("ratings/last/bak1.txt", "rb"))
process(open("ratings/last/bak2.txt", "rb"))
