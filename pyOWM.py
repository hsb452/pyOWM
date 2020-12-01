from pyowm import OWM

reg=input("지역 이름을 영문으로 입력해주세요: ")

owm=OWM("d0866560026dda53ae6587dbcb4721ae")
mgr=owm.weather_manager()
obs=mgr.weather_at_place(reg)
w=obs.weather

w_temp=w.temperature('celsius')
w_humi=w.humidity
w_wind=w.wind()
w_rain=w.rain
w_snow=w.snow
w_pres=w.pressure

'''
w_temp['temp'] 현재 기온 (℃)
w_temp['temp_max'] 오늘 최고 기온 (℃)
w_temp['temp_min'] 오늘 최저 기온 (℃)
w_temp['feels_like'] 체감 온도 (℃)
w_humi 습도 (%)
w_pres['press'] 기압 (Pa)
w_wind['speed'] 풍속(m/s)
w_wind['deg'] 풍향 (°)
w_rain['1h'] 최근 1시간동안 강우량 (mm)
w_rain['3h'] 최근 3시간동안 강우량 (mm)
w_snow['1h'] 최근 1시간동안 강설량 (mm)
w_snow['3h'] 최근 3시간동안 강설량 (mm)
'''

print("기온: {}℃".format(w_temp['temp']))
print("오늘 최고 기온: {}℃".format(w_temp['temp_max']))
print("오늘 최저 기온: {}℃".format(w_temp['temp_min']))
print("체감온도: {}℃".format(w_temp['feels_like']))

print("습도: {}%".format(w_humi))

print("기압: {}Pa".format(w_pres['press']))

print("풍속: {}m/s".format(w_wind['speed']))
print("풍향: {}°(방위각)".format(w_wind['deg']))

if w_rain.get('1h')!=None:
    print("최근 1시간 강우량: {}mm".format(w_rain['1h']))
if w_rain.get('3h')!=None:
    print("최근 3시간 강우량: {}mm".format(w_rain['3h']))

if w_snow.get('1h')!=None:
    print("최근 1시간 강설량: {}mm".format(w_snow['1h']))
if w_snow.get('3h')!=None:
    print("최근 3시간 강설량: {}mm".format(w_snow['3h']))
