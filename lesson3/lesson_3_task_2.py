from smartphone import Smartphone

catalog = [
    Smartphone('Samsung', 'Galaxy S23', +79616448127),
    Smartphone('Apple', 'iPhone 16', +79609643145),
    Smartphone('Xiaomi', 'Redmi A5', +79613146952),
    Smartphone('Tecno', 'SPARK GO 1', +79053261448),
    Smartphone('Infinix', 'SMART 9', +79059846547)
]

for smartphone in catalog:
    print(f'{smartphone.company} – {smartphone.model}.{smartphone.number}')
