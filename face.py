import requests
from uuid import uuid4

idf = "alhrrani80@gmail.com"
pas = "paoakakkajsjsjsj"

url = "https://b-graph.facebook.com/auth/login"
payload = f"adid=00000000-0000-0000-0000-000000000000&format=json&device_id={str(uuid4())}&email={idf}&password=%23PWD_MSGR%3A1%3A&%3A{pas}&generate_analytics_claim=1&community_id=&cpl=true&try_num=1&family_device_id={str(uuid4())}&secure_family_device_id=&credentials_type=password&enroll_misauth=false&generate_session_cookies=1&source=login&generate_machine_id=1&jazoest=22353&meta_inf_fbmeta=NO_FILE&advertiser_id=00000000-0000-0000-0000-000000000000&currently_logged_in_userid=0&locale=ar_AR&client_country_code=YE&fb_api_req_friendly_name=authenticate&fb_api_caller_class=AuthOperations%24PasswordAuthOperation&api_key=256002347743983&sig=1f7929ef23bdb20f98f0695be6cceac3&access_token=256002347743983%7C374e60f8b9bb6b8cbb30f78030438895"
headers = {
  'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) [FBAN/Orca-Android;FBAV/391.2.0.20.404;FBPN/com.facebook.orca;FBLC/ar_EG;FBBV/437533713;FBCR/Yemen Mobile;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;]",
  'Accept-Encoding': "gzip, deflate",
  'Content-Type': "application/x-www-form-urlencoded",
  }

response = requests.post(url, data=payload, headers=headers)
print(response.json())
