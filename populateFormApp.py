# import models form formApp.models
from faker import Faker
import random
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial5.settings')


django.setup()
fakegen = Faker()

topics = [
    # 'Search',
    # 'Social',
    # 'Marketplace',
    # 'News',
    # 'Games'
]


def populate(N=5):
    for _ in range(N):

        # # get the topic for the entry
        # top = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
        # top.save()
        # # create the fake data for entry
        # fake_url = fakegen.url()
        # fake_date = fakegen.date()
        # fake_name = fakegen.company()
        # # create the new webpage entry
        # webpg = Webpage.objects.get_or_create(
        #     topic=top, url=fake_url, name=fake_name)[0]
        # webpg.save()
        # # create fake access record
        # acc_rec = AccessRecord.objects.get_or_create(
        #     name=webpg, date=fake_date)[0]
        # acc_rec.save()
        # there is a problem in this platform
        # if __name__ == "__main__":
        #     print('Populating script running')
        #     populate(20)
        #     print('Population complete')
        # instead i will do
populate(40)


#####################################Running procedure############################
# python manage.py shell
# >>>exec(open('populateFormApp.py').read())
