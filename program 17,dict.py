data = {"b":20,"a":10,"d":40,"c":30}

asending = dict(sorted(data.items()))

print("Asending orders :",asending)

desending = dict(sorted(data.items(),reverse=True))

print("Decending orders ;",desending)
