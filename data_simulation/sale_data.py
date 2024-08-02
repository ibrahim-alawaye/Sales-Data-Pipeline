import csv
import time
import uuid
import json
from faker import Faker
from kafka import KafkaProducer

fake = Faker()

producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)

def generate_sales_data():
    location = fake.local_latlng(country_code='US', coords_only=False)
    order_date = fake.date_time_this_year()
    unit_price = round(fake.random.uniform(10.0, 100.0), 2)
    quantity = fake.random_int(min=1, max=10)
    discount = round(fake.random.uniform(0.0, 10.0), 2)
    total_price = round((unit_price * quantity) - discount, 2)
    return {
        'SaleID': str(uuid.uuid4()),  
        'OrderID': str(uuid.uuid4()), 
        'OrderDate': order_date.strftime('%Y-%m-%d %H:%M:%S'),
        'CustomerName': fake.name(),
        'CustomerEmail': fake.email(),
        'ProductID': fake.random_int(min=1, max=100),
        'ProductName': fake.word(),
        'ProductCategory': fake.word(),
        'UnitsSold': quantity,
        'UnitPrice': unit_price,
        'TotalPrice': total_price,
        'Revenue': total_price,
        'Region': fake.random_element(elements=('North', 'South', 'East', 'West')),
        'Discount': discount,
        'CustomerID': fake.random_int(min=1, max=500),
        'PaymentMethod': fake.random_element(elements=('Credit Card', 'Debit Card', 'PayPal', 'Cash')),
        'PaymentStatus': fake.random_element(elements=('Paid', 'Unpaid', 'Refunded')),
        'OrderStatus': fake.random_element(elements=('Pending', 'Shipped', 'Delivered', 'Cancelled')),
        'ShippingCost': round(fake.random.uniform(5.0, 20.0), 2),
        'Carrier': fake.random_element(elements=('UPS', 'FedEx', 'DHL', 'USPS')),
        'TrackingNumber': str(uuid.uuid4()),
        'CouponCode': fake.word(),
        'CouponDiscount': discount,
        'City': location[2],
        'Country': location[3],
        'Latitude': location[0],
        'Longitude': location[1],
        'ShippingAddress': fake.address().replace('\n', ', '),
        'BillingAddress': fake.address().replace('\n', ', ')
    }

while True:
    sales_data = generate_sales_data()
    # print(sales_data)
    producer.send('sales_data', json.dumps(sales_data).encode('utf-8'))
    time.sleep(5)
    print(sales_data)
