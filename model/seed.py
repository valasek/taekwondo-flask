# -*- coding: utf-8 -*-
# app/seed.py
import datetime
from models import Matsogi, Tull, Wirok, Tki, Levels, Sex
from models import db, MemberCompetition, TeamMembers, Teams, Competitions, Users
from itf import app

app.logger.info('Entering seed.py')
db.drop_all()
db.create_all()

# Users
db.session.add(Users(u'AdminF', u'AdminL', u'admin', u'admin', 1, 1))
db.session.add(Users(u'UserF', u'UserL', u'user', u'user', 2, 0))
db.session.add(Users(u'Robert', u'Pokorný', u'administrator@taekwondocz.com', u'robert', 1, 1))

# member_competition
db.session.add(MemberCompetition(1, 1, 3, 4, 5, 6, 1, 1))
db.session.add(MemberCompetition(2, 1, 3, 4, 5, 6, 1, 1))
db.session.add(MemberCompetition(13, 1, 3, 4, 5, 6, 0, 0))
db.session.add(MemberCompetition(14, 1, 3, 4, 5, 6, 0, 0))
db.session.add(MemberCompetition(12, 1, 3, 4, 5, 6, 0, 0))

# Competitions
db.session.add(Competitions(u'Světový pohár 2016', u'Budapešť',
                            u'12. října - 16. října 2016',
                            u'30. srpna 2016',
                            '200',
                            'http://taekwondocz.com/files/PROPOZICE%20MR%202016.pdf',
                            '50.289,14.830'))

# Teams
db.session.add(Teams(u'Sparring'))
db.session.add(Teams(u'Stránčice'))

# Sex
db.session.add(Sex(u'Muž'))
db.session.add(Sex(u'Žena'))

# Levels
db.session.add(Levels(u'9. DAN'))
db.session.add(Levels(u'8. DAN'))
db.session.add(Levels(u'7. DAN'))
db.session.add(Levels(u'6. DAN'))
db.session.add(Levels(u'5. DAN'))
db.session.add(Levels(u'4. DAN'))
db.session.add(Levels(u'3. DAN'))
db.session.add(Levels(u'2. DAN'))
db.session.add(Levels(u'1. DAN'))
db.session.add(Levels(u'9. KUP'))
db.session.add(Levels(u'8. KUP'))
db.session.add(Levels(u'7. KUP'))
db.session.add(Levels(u'6. KUP'))
db.session.add(Levels(u'5. KUP'))
db.session.add(Levels(u'4. KUP'))
db.session.add(Levels(u'3. KUP'))
db.session.add(Levels(u'2. KUP'))
db.session.add(Levels(u'1. KUP'))

# TeamMembers
db.session.add(TeamMembers(510317, 1, u'Jiří', u'Beneš', 1, datetime.date(2013, 3, 25), 50, 5))
db.session.add(TeamMembers(507192, 1, u'Lucie', u'Bohatá', 2, datetime.date(2001, 2, 14), 55, 10))
db.session.add(TeamMembers(510313, 1, u'Mikuláš', u'Hupcej', 1, datetime.date(2013, 9, 9), 60, 7))
db.session.add(TeamMembers(509634, 1, u'Eliška', u'Hupcejová', 2, datetime.date(2001, 9, 1), 40, 4))
db.session.add(TeamMembers(510314, 1, u'Jakub', u'Kalous', 1, datetime.date(2002, 10, 24), 42, 4))
db.session.add(TeamMembers(510387, 1, u'Erik', u'Kudrjavcev', 1, datetime.date(2013, 3, 21), 32, 8))
db.session.add(TeamMembers(510394, 1, u'Zdeněk', u'Lhotka', 1, datetime.date(2003, 9, 28), 38, 1))
db.session.add(TeamMembers(510391, 1, u'Patricia', u'Oginčuková', 2, datetime.date(2005, 9, 5), 35, 8))
db.session.add(TeamMembers(507195, 1, u'Natáli', u'Podskalníková', 2, datetime.date(2003, 5, 19), 52, 1))
db.session.add(TeamMembers(507191, 1, u'Sára', u'Podskalníková', 2, datetime.date(2000, 6, 13), 57, 10))
db.session.add(TeamMembers(507196, 2, u'Patricie', u'Pokorná', 2, datetime.date(2002, 12, 2), 48, 1))
db.session.add(TeamMembers(510380, 2, u'Antonín', u'Pokorný', 1, datetime.date(2006, 12, 14), 62, 6))
db.session.add(TeamMembers(509636, 2, u'Daniela', u'Richterová', 2, datetime.date(2004, 4, 2), 60, 3))
db.session.add(TeamMembers(510384, 2, u'Davil', u'Roubal', 1, datetime.date(1998, 7, 17), 68, 4))
db.session.add(TeamMembers(500822, 2, u'Jakub', u'Roubal', 1, datetime.date(2000, 1, 11), 63, 7))

# matsogi
db.session.add(Matsogi(u'Nepřiřazeno', 1))
db.session.add(Matsogi(u'Nepřiřazeno', 2))
db.session.add(Matsogi(u'Žáci do 32 kg', 1))
db.session.add(Matsogi(u'Žáci 32 – 38 kg', 1))
db.session.add(Matsogi(u'Žáci 38 – 44 kg', 1))
db.session.add(Matsogi(u'Žáci 44 – 50 kg', 1))
db.session.add(Matsogi(u'Žáci nad50 kg', 1))
db.session.add(Matsogi(u'Žákyně do 32 kg', 2))
db.session.add(Matsogi(u'Žákyně 32 – 38 kg', 2))
db.session.add(Matsogi(u'Žákyně 38 – 44 kg', 2))
db.session.add(Matsogi(u'Žákyně 44 – 50 kg', 2))
db.session.add(Matsogi(u'Žákyně nad50 kg', 2))
db.session.add(Matsogi(u'Junioři do 50 kg', 1))
db.session.add(Matsogi(u'Junioři 50 – 56 kg', 1))
db.session.add(Matsogi(u'Junioři 56 – 62 kg', 1))
db.session.add(Matsogi(u'Junioři 62 – 68 kg', 1))
db.session.add(Matsogi(u'Junioři 68 - 75 kg', 1))
db.session.add(Matsogi(u'Junioři nad 75 kg', 1))
db.session.add(Matsogi(u'Juniorky do 45 kg', 2))
db.session.add(Matsogi(u'Juniorky 45 – 50 kg', 2))
db.session.add(Matsogi(u'Juniorky 50 – 55 kg', 2))
db.session.add(Matsogi(u'Juniorky 55 – 60 kg', 2))
db.session.add(Matsogi(u'Juniorky 60 – 65 kg', 2))
db.session.add(Matsogi(u'Juniorky nad 65 kg', 2))
db.session.add(Matsogi(u'Senioři do 57 kg', 1))
db.session.add(Matsogi(u'Senioři 57 – 63 kg', 1))
db.session.add(Matsogi(u'Senioři 63 – 70 kg', 1))
db.session.add(Matsogi(u'Senioři 70 – 78 kg', 1))
db.session.add(Matsogi(u'Senioři 78 – 85 kg', 1))
db.session.add(Matsogi(u'Senioři nad 85 kg', 1))
db.session.add(Matsogi(u'Seniorky do 50 kg', 2))
db.session.add(Matsogi(u'Seniorky 50 – 56 kg', 2))
db.session.add(Matsogi(u'Seniorky 56 – 62 kg', 2))
db.session.add(Matsogi(u'Seniorky 62 – 68 kg', 2))
db.session.add(Matsogi(u'Seniorky 68 – 75 kg', 2))
db.session.add(Matsogi(u'Seniorky nad 75 kg', 2))

# tull
db.session.add(Tull(u'Nepřiřazeno', 1))
db.session.add(Tull(u'Nepřiřazeno', 2))
db.session.add(Tull(u'Žáci 9. - 8. kup', 1))
db.session.add(Tull(u'Žáci 7. - 5. Kup', 1))
db.session.add(Tull(u'Žáci 4. - 3. Kup', 1))
db.session.add(Tull(u'Žáci 2. - 1. kup', 1))
db.session.add(Tull(u'Žáci I. Dan a výše', 1))
db.session.add(Tull(u'Žákyně 9. - 8. kup', 2))
db.session.add(Tull(u'Žákyně 7. - 5. Kup', 2))
db.session.add(Tull(u'Žákyně 4. - 3. Kup', 2))
db.session.add(Tull(u'Žákyně 2. - 1. kup', 2))
db.session.add(Tull(u'Žákyně I. Dan a výše', 2))
db.session.add(Tull(u'Junioři 9. - 8. kup', 1))
db.session.add(Tull(u'Junioři 7. - 5. Kup', 1))
db.session.add(Tull(u'Junioři 4. - 3. Kup', 1))
db.session.add(Tull(u'Junioři 2. - 1. kup', 1))
db.session.add(Tull(u'Junioři I. Dan a výše', 1))
db.session.add(Tull(u'Juniorky 9. - 8. kup', 2))
db.session.add(Tull(u'Juniorky 7. - 5. Kup', 2))
db.session.add(Tull(u'Juniorky 4. - 3. Kup', 2))
db.session.add(Tull(u'Juniorky 2. - 1. kup', 2))
db.session.add(Tull(u'Juniorky I. Dan a výše', 2))
db.session.add(Tull(u'Senioři 9. - 8.Kup', 1))
db.session.add(Tull(u'Senioři 4. - 3.Kup', 1))
db.session.add(Tull(u'Senioři 2. - 1. Kup', 1))
db.session.add(Tull(u'Senioři I. - II. Dan', 1))
db.session.add(Tull(u'Senioři III. Dan a výše', 1))
db.session.add(Tull(u'Seniorky 9. - 8.Kup', 2))
db.session.add(Tull(u'Seniorky 4. - 3.Kup', 2))
db.session.add(Tull(u'Seniorky 2. - 1. Kup', 2))
db.session.add(Tull(u'Seniorky I. - II. Dan', 2))
db.session.add(Tull(u'Seniorky III. Dan a výše', 2))

# wirok
db.session.add(Wirok(u'Nepřiřazeno', 1))
db.session.add(Wirok(u'Nepřiřazeno', 2))
db.session.add(Wirok(u'Junioři', 1))
db.session.add(Wirok(u'Juniorky', 2))
db.session.add(Wirok(u'Senioři', 1))
db.session.add(Wirok(u'Seniorky', 2))

# tki
db.session.add(Tki(u'Nepřiřazeno', 1))
db.session.add(Tki(u'Nepřiřazeno', 2))
db.session.add(Tki(u'Žáci', 1))
db.session.add(Tki(u'Žákyně', 2))
db.session.add(Tki(u'Junioři', 1))
db.session.add(Tki(u'Juniorky', 2))
db.session.add(Tki(u'Senioři', 1))
db.session.add(Tki(u'Seniorky', 2))

db.session.commit()
