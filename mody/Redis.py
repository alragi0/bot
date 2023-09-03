from redis import StrictRedis

# تعيين المعلمات الخاصة بالاتصال
host = "containers-us-west-188.railway.app"  # عنوان خادم Redis
port = 6810  # المنفذ الذي ترغب في استخدامه
password = "p5XWFPNw4Idm5mOQAl84"  # كلمة المرور إذا كانت مطلوبة

# إنشاء اتصال Redis
db = StrictRedis(host=host, port=port, password=password, decode_responses=True)

# الآن يمكنك استخدام الاتصال db للقيام بالعمليات على خادم Redis بالمنفذ المحدد
