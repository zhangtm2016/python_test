#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

if __name__ == '__main__':

    print(datetime.date.today().strftime('%d/%m/%Y'))

    miyazakBirthDate = datetime.date(1941,1,5)

    print(miyazakBirthDate.strftime('%d/%m/%Y'))

    miyazakBirthNextDate = miyazakBirthDate + datetime.timedelta(days=1)

    print(miyazakBirthNextDate.strftime('%d/%m/%Y'))

    miyazakiFirstBirthday = miyazakBirthDate.replace(year=miyazakBirthDate.year + 1)

    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))


