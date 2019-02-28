try:
    from xmlrpc import client as xmlrpclib
except ImportError:
    import xmlrpclib

DATABASE = 'andy_5_10'
USERNAME = 'admin'
PASSWORD = 'admin'

common = xmlrpclib.ServerProxy('http://emipro:8998/xmlrpc/2/common')
user_id = common.login(DATABASE, USERNAME, PASSWORD)
print("========user_id", user_id)

server = xmlrpclib.ServerProxy('http://emipro:8998/xmlrpc/2/object')

aws_iot = server.execute_kw(DATABASE, user_id, PASSWORD, 'aws.iot.log.ept', 'check_iot', ['G030JF0524415HFV','DOUBLE'])

print("********", aws_iot)
