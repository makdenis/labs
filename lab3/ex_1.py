#!/usr/bin/env python3
from librip.gen import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]


#print([x for x in field(goods, 'title', 'price')])
#print([x for x in field(goods, 'title')])
print([x for x in gen_random(1, 5, 5)])
