### demo_statistic
#1-step: clone repo
#2-step: create virtualenviroment
#3-step: pip install -r  requirements.txt 
#4-step: create database postgresql db_name='demo_db', db_user='demo_user', password='12345'
#5-step: python manage.py migrate
#6-step: python manage.py createsuperuser 
#7-step: py manage.py create_employees (create default employees)
#8-step: py manage.py create_clients (create default clients)
#9-step: py manage.py create_products (create default products)
#10-step: py manage.py add (create orders and order_setails)
#11-step: python manage.py runserver
## APIs
1. /statistics/employee/{id}/?month=1&year=2023
2. /employee/statistics/?month=1&year=2023
3. /statistics/client/{id}?month=1&year=2023
   #####
4. order/list (for all orders)
5. order/details (for all order details)


 
