# -*- coding: utf-8 -*-
# app/seed.py
from itf import db_new
from models import CompetitionCategories

db_new.drop_all()
db_new.create_all()

#matsogi
db_new.session.add(CompetitionCategories(u'matsogi', u'Žáci do 32 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Žáci 32 – 38 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Žáci 38 – 44 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Žáci 44 – 50 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Žáci nad50 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Žákyně do 32 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Žákyně 32 – 38 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Žákyně 38 – 44 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Žákyně 44 – 50 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Žákyně nad50 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Junioři do 50 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Junioři 50 – 56 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Junioři 56 – 62 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Junioři 62 – 68 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Junioři 68 - 75 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Junioři nad 75 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Juniorky do 45 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Juniorky 45 – 50 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Juniorky 50 – 55 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Juniorky 55 – 60 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Juniorky 60 – 65 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Juniorky nad 65 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Senioři do 57 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Senioři 57 – 63 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Senioři 63 – 70 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Senioři 70 – 78 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Senioři 78 – 85 kg', u'Muž'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Senioři nad 85 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Seniorky do 50 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Seniorky 50 – 56 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Seniorky 56 – 62 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Seniorky 62 – 68 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Seniorky 68 – 75 kg', u'Žena'))
db_new.session.add(CompetitionCategories(u'matsogi', u'Seniorky nad 75 kg', u'Žena'))
#Tull
db_new.session.add(CompetitionCategories(u'tull', u'Žáci 9. - 8. kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Žáci 7. - 5. Kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Žáci 4. - 3. Kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Žáci 2. - 1. kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Žáci I. Dan a výše', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Žákyně 9. - 8. kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Žákyně 7. - 5. Kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Žákyně 4. - 3. Kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Žákyně 2. - 1. kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Žákyně I. Dan a výše', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Junioři 9. - 8. kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Junioři 7. - 5. Kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Junioři 4. - 3. Kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Junioři 2. - 1. kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Junioři I. Dan a výše', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Juniorky 9. - 8. kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Juniorky 7. - 5. Kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Juniorky 4. - 3. Kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Juniorky 2. - 1. kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Juniorky I. Dan a výše', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Senioři 9. - 8.Kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Senioři 4. - 3.Kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Senioři 2. - 1. Kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Senioři I. - II. Dan', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Senioři III. Dan a výše', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Seniorky 9. - 8.Kup', u'Muž'))
db_new.session.add(CompetitionCategories(u'tull', u'Seniorky 4. - 3.Kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Seniorky 2. - 1. Kup', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Seniorky I. - II. Dan', u'Žena'))
db_new.session.add(CompetitionCategories(u'tull', u'Seniorky III. Dan a výše', u'Žena'))
#wirok
db_new.session.add(CompetitionCategories(u'wirok', u'Junioři', u'Muž'))
db_new.session.add(CompetitionCategories(u'wirok', u'Juniorky', u'Žena'))
db_new.session.add(CompetitionCategories(u'wirok', u'Senioři', u'Muž'))
db_new.session.add(CompetitionCategories(u'wirok', u'Seniorky', u'Žena'))
# T-ki
db_new.session.add(CompetitionCategories(u'T-ki', u'Žáci', u'Muž'))
db_new.session.add(CompetitionCategories(u'T-ki', u'Žákyně', u'Žena'))
db_new.session.add(CompetitionCategories(u'T-ki', u'Junioři', u'Muž'))
db_new.session.add(CompetitionCategories(u'T-ki', u'Juniorky', u'Žena'))
db_new.session.add(CompetitionCategories(u'T-ki', u'Senioři', u'Muž'))
db_new.session.add(CompetitionCategories(u'T-ki', u'Seniorky', u'Žena'))

db_new.session.commit()
