from pysocrocket import SocRocket

socrocket = SocRocket("apikey")

order=create_order(120, "https://vk.com/durov", 1000)

print(order.get_order_status(order["id"]))
