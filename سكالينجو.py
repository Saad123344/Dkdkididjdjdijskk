{
    "name": "westrthon - سورس جمثون",
    "description": "تنصيب سورس جمثون مجانا على منصة سكالينجو",
    "addons": ["scalingo-postgresql"],
    "keywords": ["jmthon", "userbot","scalingo"],
    "repository": "https://github.com/thejmthon/sbb_b0",
  "stack": "container",
    "env": {
        "APP_ID": {
            "description": "ضع هنا الايبي ايدي الخاص بك",
            "required": true,
            "value":""
        },
        "API_HASH": {
            "description": "ضع هنا الايبي هاش الخاص بك",
            "required": true,
            "value":""
        },
        "STRING_SESSION": {
            "description": "هنا ضع كود سيشن بايروجرام او سيشن تيليثون",
            "required": true
        },
        "TG_BOT_TOKEN": {
            "description": "ضع توكن البوت المساعد الخاص بك",
            "required": true,
            "value":""
        },
        "TZ": {
            "description": "ضع هنا المنطقة الزمنيه الخاصه بك القارة وعاصمه بلدك",
            "required": true,
            "value": "Asia/Baghdad"
        },
        "ENV": {
            "description": "لا تغيره نهائيا!",
            "required": true,
            "value": "ANYTHING"
        }

    }
  }
