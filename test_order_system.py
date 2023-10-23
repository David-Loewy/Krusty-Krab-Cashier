from order_system import Order


class TestOrder:
    def test_orders(self):
        o = Order('Spongebob', ['Krabby Patty'])
        print('testing details: order')
        assert('Spongebob', ['Krabby Patty'], 6.25, 1) == (o.customer_name, o.item_list, o.order_total, o.order_num)

    def test_orders2(self):
        o2 = Order('Squidward', ['Kelp Shake', 'Krusty Krab Pizza'])
        print('testing details: order')
        assert('Squidward', ['Kelp Shake', 'Krusty Krab Pizza'], 11.5, 2) == (o2.customer_name, o2.item_list, o2.order_total, o2.order_num)
