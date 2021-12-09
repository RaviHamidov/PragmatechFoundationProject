from app import app
from flask import render_template,request,redirect
from models import User
@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/users',methods=['GET','POST'])
def admin_users():
    if request.method=='POST':
        _ad=request.form['ad']
        _soyad=request.form['soyad']
        user=User(_ad,_soyad)
        return render_template('admin/users.html',user=user)
    
    return render_template('admin/users.html',user=None)