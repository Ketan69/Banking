from django.shortcuts import render
from django.http import HttpResponse 
from .models import cust,trans
from datetime import date
from random import *

def home(req):
 return render(req,'home.html',{})

def login(req):
 if 'login' in req.POST:
  try:
   a=cust.objects.filter(custid=req.POST['id'])
   a=list(a.values())
   if a[0]['passwd']!=req.POST['passwd'] or a[0]['name']=='admin':
    raise KeyError 
   else:
     if a[0]['status']==0:  
      return HttpResponse('Account is Blocked..')
     else:
      d=date.today()
      d=d.strftime('%d/%m/%y')
      return render(req,'detail.html',{'a':a[0],'d':d}) 
  except:
   html='''<body bgcolor=white>invalid Id or Password <a href='/'>try again</a></body>'''
  return HttpResponse(html) 
 else:
  try:
   a=cust.objects.filter(custid=req.POST['id'])
   a=list(a.values())
   if a[0]['name']!='admin':
    return HttpResponse("invalid Id or Password..<a href='/'>try again</a>") 
  except:
   return HttpResponse("invalid Id or Password..<a href='/'>try again</a>")   
  if req.POST['id']==str(a[0]['custid']) and req.POST['passwd']==a[0]['passwd']:
   z=req.POST['id']
   w=req.POST['passwd']
   return render(req,'admin.html',{'z':z,'w':w})
  else:
   html='''<body bgcolor=white>invalid Id or Password <a href='/'>try again</a></body>'''
  return HttpResponse(html)

#def unblock(req):
 

def delete(req):    
 a=req.POST['id']
 b=req.POST['passwd']  
 return render(req,'delete.html',{'a':a,'b':b})

def _delete(req):
 try:
  a=cust.objects.filter(custid=req.POST['iid'])
  a=a.values()
  if a[0]['status']==0:
   return HttpResponse('Account already deleted before..')
  p=req.POST['id'] 
  k=req.POST['passwd']
  return render(req,'_delete.html',{'p':p,'k':k})
 except:
  html='''<body bgcolor=white>invalid credentials <a href='/delete'>try again</a></body>'''
  return HttpResponse(html)   


def new(req): 
 a=req.POST['id']
 b=req.POST['passwd'] 
 return render(req,'new.html',{'a':a,'b':b})

def _new(req):
 if req.POST['ipasswd']==req.POST['rpasswd']:
  d=date.today()
  cust(req.POST['iid'],req.POST['ipasswd'],req.POST['name'],req.POST['balance'],d.strftime('%Y-%m-%d'),1).save()
  a=req.POST['id']
  b=req.POST['passwd']
  return HttpRespose(req,'_new.html',{'a':a,'b':b})
 else:
  html='''<body bgcolor=white>Password doesn't match <a href='/new'>try again</a</body>'''
  return HttpResponse(html) 


def update(req):
 a=req.POST['id']
 b=req.POST['passwd'] 
 return render(req,'update.html',{'a':a,'b':b})


def block(req):
 a=req.POST['id'] 
 b=req.POST['passwd']  
 return render(req,'block.html',{'a':a,'b':b})

def _block(req):
 try:
  a=cust.objects.filter(custid=req.POST['iid'])
  a=list(a.values())
  if req.POST['ipasswd']==a[0]['passwd']:
   cust(a[0]['custid'],a[0]['passwd'],a[0]['name'],a[0]['balance'],a[0]['opendate'],0).save()
   p=req.POST['id']
   k=req.POST['passwd']
  return render(req,'_block.html',{'p':p,'k':k})
 except:
  html='''<body bgcolor=white>invalid credentials <a href='/block'>try again</a></body>'''
  return HttpResponse(html) 

def revert(req):
 a=req.POST['id']
 b=req.POST['passwd'] 
 return render(req,'revert.html',{'a':a,'b':b})

def _revert(req):
 try:
  a=cust.objects.filter(custid=req.POST['iid'])
 except:
  return HttpResponse('invalid Id..')
 a=list(a.values())
 b=list(trans.objects.filter(receiver=a[0]['custid'],status='credited').values())
 y=req.POST['iid']
 if req.POST['ipasswd']==a[0]['passwd']:
  p=req.POST['iid']
  k=req.POST['ipasswd']
  return render(req,'rrevert.html',{'b':b,'y':y,'p':p,'k':k})
 else:
  return HttpResponse('invalid Password..')

def __revert(req):
 a=list(trans.objects.filter(receiver=req.POST['id']).values())
 
 for x in a:
  if req.POST['tid']==str(x['transid']):
   d=date.today()
   d=d.strftime('%Y-%m-%d')
   trans(x['transid'],x['sender'],x['receiver'],x['amt'],'reverted',x['dot']).save() 
   trans(randint(1,9999),x['receiver'],x['sender'],x['amt'],'refund',d).save()
   trans(randint(1,9999),x['receiver'],x['sender'],x['amt'],'debited',d).save()
   y=cust.objects.POST(custid=x['sender'])
   y.balance=y.balance+x['amt']
   y.save()
   z=cust.objects.POST(custid=req.POST['id'])
   z.balance=z.balance-x['amt']
   z.save()
   return HttpResponse('Transaction reverted..')
 return HttpResponse('invalid Transaction_Id..') 
  
def change(req):
 a=req.POST['id']
 b=req.POST['passwd']
 x=cust.objects.get(custid=a)
 if x.name=='admin':
  return render(req,'achange.html',{'a':a,'b':b})
 else:   
  return render(req,'change.html',{'a':a,'b':b}) 

def _change(req):
 if req.POST['id']!=req.POST['cid']:
  return HttpResponse('invalid ID..')
 if req.POST['ipasswd']!=req.POST['rpasswd']:
  return HttpResponse("Password didn't match..")
 x=list(cust.objects.filter(custid=req.POST['id']).values())
 x=x[0]
 cust(x['custid'],req.POST['ipasswd'],x['name'],x['balance'],x['opendate'],x['status']).save()
 a=req.POST['id']
 b=req.POST['passwd']  
 return render(req,'_change.html',{'a':a,'b':b}) 

def send(req):
 a=req.POST['id']
 b=req.POST['passwd'] 
 return render(req,'send.html',{'a':a,'b':b})

def _send(req):
 if req.POST['code']!='2661':
  html='''Transaction Failed,invalid Passcode'''
  return HttpResponse(html)
 try:
  a=cust.objects.filter(custid=req.POST['rid'])
 except:
  html='''invalid Customer_id'''
  return HttpResponse(html) 
 a=list(a.values())
 print(a)
 b=list(cust.objects.filter(custid=req.POST['id']).values())
 if b[0]['balance']<int(req.POST['amt']):
  html='''Not Enough Amount'''
  return HttpResponse(html)
 if b[0]['status']!=1:
  html='''account no longer exist'''
  return HttpResponse(html)
 b[0]['balance']=b[0]['balance']-int(req.POST['amt'])
 cust(b[0]['custid'],b[0]['passwd'],b[0]['name'],b[0]['balance'],b[0]['opendate'],b[0]['status']).save()
 d=date.today()
 d=d.strftime('%Y-%m-%d')
 trans(randint(1,9999),req.POST['id'],req.POST['rid'],req.POST['amt'],'debited',d).save()
 a[0]['balance']=a[0]['balance']+int(req.POST['amt']) 
 print(a)
 cust(a[0]['custid'],a[0]['passwd'],a[0]['name'],a[0]['balance'],a[0]['opendate'],a[0]['status']).save()
 trans(randint(1,9999),req.POST['id'],req.POST['rid'],req.POST['amt'],'credited',d).save()
 a=req.POST['id']
 b=req.POST['passwd'] 
 return render(req,'_send.html',{'a':a,'b':b}) 
   
def transaction(req): 
 a=trans.objects.filter(sender=req.POST['id'],status='debited').values()
 b=trans.objects.filter(receiver=req.POST['id'],status='reverted').values() 
 c=trans.objects.filter(receiver=req.POST['id'],status='credited').values()
 d=trans.objects.filter(receiver=req.POST['id'],status='refund').values() 
 p=req.POST['id']
 k=req.POST['passwd']
 return render(req,'trans.html',{'a':a,'b':b,'c':c,'d':d,'p':p,'k':k})