import random
from faker import Faker
import arrow
fake = Faker()

class Guest:
    pass

class DashboardService:
    @staticmethod
    def get_start_and_end_time():
        end_time = arrow.utcnow()
        start_time = end_time.shift(days=-30)
        return start_time, end_time

class DashboardDummyDataService:
    statuses_list = ['success', 'in_process', 'refunded', 'error']
    package_names = ['1 Day 1 Device', '1 Day 4 Devices', '1 Week 1 Device', '1 Week 4 Devices', '15 Mins Free']

    @staticmethod
    def dummy_get_avg_dwell_time_for_site(*args, **kwargs):
        return 25

    @staticmethod
    def dummy_get_total_num_guests(*args,**kwargs):
        return 3678


    @staticmethod
    def dummy_get_total_new_guests(*args,**kwargs):
        return 345

    @staticmethod
    def dummy_get_currently_online_guests(*args,**kwargs):
        return 25

    @staticmethod
    def dummy_get_site_bounce_rate(*args,**kwargs):
        return 90

    @staticmethod
    def dummy_get_site_login_graph(*args,**kwargs):
        start_time, end_time= DashboardService.get_start_and_end_time()

        stats_list = []

        num_days        = (end_time - start_time).days
        for x in range(num_days):
            day = start_time.shift(days=x)
            stat = {
                'num_new_guests':random.randint(20,50),
                'num_repeat_guests':random.randint(10,30),
                'day':day.floor('day').isoformat()
            }
            stats_list.append(stat)
        return stats_list


    @staticmethod
    def dummy_get_site_activity_graph(*args,**kwargs):
        return {"02:00":32,"04:00":3,"12:00":25,"14:00":80,"16:00":100,"18:00":87,"20:00":83,"22:00":35,"24:00":22}


    @staticmethod
    def dummy_get_site_latest_guests(*args,**kwargs):
        fake_guests = []

        for i in range(5):
            profile = fake.profile()
            g = Guest()
            g.firstname = profile['name'].split()[0]
            g.firstname = profile['name'].split()[1]
            g.email = profile['mail']
            g.dob = profile['birthdate']
            g.phonenumber = fake.phone_number()
            g.gender = fake.phone_number()
            g.siteid = kwargs.get('siteid')
            g.first_seen = arrow.utcnow().replace(hours=-(random.randint(1,10))).naive
            g.last_seen_at = arrow.utcnow().replace(minutes=-(random.randint(1,10))).naive
            fake_guests.append(g)

        return fake_guests

    @staticmethod
    def dummy_get_site_gender_segments(*args,**kwargs):
        return {
            'male': 40,
            'female': 40,
            'unknown': 20
        }

    @staticmethod
    def dummy_get_site_visits_segment(*args,**kwargs):
        return {"1 to 1":53,"1 to 2":37, '3+': 10}

    @staticmethod
    def dummy_get_successful_payments(*args,**kwargs):
        return '3500$'
    @staticmethod
    def dummy_get_recurring_payments(*args,**kwargs):
        return '550$'

    @staticmethod
    def dummy_get_daily_transactions(*args,**kwargs):
        start_time, end_time= DashboardService.get_start_and_end_time()

        stats_list = []

        num_days        = (end_time - start_time).days
        for x in range(num_days):
            day = start_time.shift(days=x)
            stat = {
                "num_paid_transactions": random.randint(3,10),
                "num_free_transactions": random.randint(5,20),
                "num_failed_transactions": random.randint(0,5),
                'day':day.floor('day').format('DD/MM/YYYY')
            }
            stats_list.append(stat)
        return stats_list

    @staticmethod
    def dummy_get_only_once_guests(*args,**kwargs):
        return 5

    @staticmethod
    def dummy_get_last_n_transactions(*args,**kwargs):
        count = 5
        stats_list = []

        for i in range(count):
            profile = fake.profile()
            stats_list.append(
                {
                    'email': profile['mail'],
                    'package_name': DashboardDummyDataService.package_names[random.randint(0,4)],
                    'status': DashboardDummyDataService.statuses_list[random.randint(0,3)],
                    'created_at': arrow.utcnow().shift(minutes=-(random.randint(20,300))).humanize()
                }
            )

        return stats_list

    @staticmethod
    def dummy_get_most_transactions_package(*args,**kwargs):
        packages_list = [{
            'package_name': name,
            'transaction_count': random.randint(1,20) } for name in DashboardDummyDataService.package_names
        ]
        return sorted(packages_list, key=lambda d: d['transaction_count'],reverse=True)

    @staticmethod
    def dummy_get_active_vouchers(*args,**kwargs):
        return {'data':30}

    @staticmethod
    def dummy_get_unused_vouchers(*args,**kwargs):
        return {'data':20}

    @staticmethod
    def dummy_get_vouchers_near_expiry(*args,**kwargs):
        return {'data':10}