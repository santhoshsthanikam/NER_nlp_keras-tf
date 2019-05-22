platform_weight=0.5
middleware_weight=0.1
application_weight=0.4

Platform='Linux'
Middleware='MQ'
Application=['Java','SDK']

total_weight=0
if Platform == 'Linux':
	total_weight +=platform_weight*1
else:
	total_weight +=platform_weight*0

if Middleware == 'MQ':
	total_weight +=middleware_weight*1
else:
	total_weight +=middleware_weight*0
if 'Java' in Application:
	total_weight +=application_weight*1
else:
	total_weight +=application_weight*0

print(total_weight*100)