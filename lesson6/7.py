"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

from pprint import pprint
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'  # вместо pt вставляете свой язык (ru)
owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d', config_dict)
mgr = owm.weather_manager()

place = input ("город: ")
obs = mgr.weather_at_place(place)
w = obs.to_dict()



# pprint(w)
print(f"""
Погода в городе {w['location']['name']}:
- общее состояние: {w['weather']['detailed_status']}
- температура фактическая: {round((w['weather']['temperature']['temp'] - 273),0)}
- температура по ощущениям: {round((w['weather']['temperature']['feels_like'] - 273),0)}
- дождь: {w['weather']['rain']}
""")