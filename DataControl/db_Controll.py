import tkinter.messagebox as msgbox
import DataControl.crypto as crypto
import pymysql

def db_conn() :
    return pymysql.connect(host='127.0.0.1', user='root', password='wjdqhqhdks', db='idm', charset='utf8') # DB 연결 객체 반환
'''
    db(data).insert()
    db(data).delete()
    db(data).search()
    db(data).update()
    위 방식으로 사용하며, data중 비밀번호부분의 암호화가 필요하므로 init함수를 통해서 생성자 단위에서 암호화 진행 후
    해당 결과값을 반환하는 것이 가장 매끄럽고 깔끔함 동작 순서로 보임.
    [프로토타입 제작 후 반영 여부 검토]
'''

# Search Account
def search(keyword) :
    con = db_conn()
    cur = con.cursor()
    if keyword == '' : sql = 'select * from info;'
    else : sql =  "select * from info where site_name like '%%%s%%'" % (keyword)
    cur.execute(sql)
    res = list(cur.fetchall())
    con.close()
    for i in range(len(res)) :
        res[i] = list(res[i])
        res[i][3] = crypto.decrypto(res[i][3]).decode()
    return res

# Insert Account
def insert(data) :
    con = db_conn()
    cur = con.cursor()

    # Duplicate Prevention
    sql = "select * from info where site_name = '%s' and id = '%s'" % (data[0],data[2])
    chk_dp = cur.execute(sql)

    if chk_dp :
        msgbox.showwarning('Error', 'Account Duplicate !')
    else :
        data = list(data)
        data[3] = crypto.encrypto(data[3])
        data[4] = str(data[4]).replace('\n','\\n')
        sql = "insert into info value(%s,%s,%s,%s,%s,0);"
        res = cur.execute(sql,data)
        if res :
            con.commit()
            con.close()
            msgbox.showinfo('Success', 'Success Insert Account Information!')
        else :
            msgbox.showwarning('Error','Data Insert Error!')

# Update Account
def update(data) :
    con = db_conn()
    cur = con.cursor()
    data[3] = crypto.encrypto(data[3])
    data[4] = str(data[4]).replace('\n', '\\n')
    sql = "update info set site_name=%s, site_url=%s, id=%s, pw=%s, note=%s where id_num=%s;"
    res = cur.execute(sql, data)
    if res:
        con.commit()
        con.close()
        msgbox.showinfo('Success', 'Success Update !')
    else :
        con.close()
        msgbox.showinfo('Fail', 'Fail Update !')

# Delete Account
def delete(target) : # (site_name,id) 의 양식으로 넘겨줌
    print('Delete Target : ',target)
    con = db_conn()
    cur = con.cursor()
    sql = "delete from info where site_name = %s and id = %s"

    # Init Auto Increment
    cur.execute(sql,target)
    cur.execute('set @cnt = 0;')
    cur.execute('update info set info.id_num = @cnt := @cnt+1;')
    cur.execute('select count(*) from info;')
    res = cur.fetchone()[0]+1
    sql = 'alter table info auto_increment=%s'%(res)

    cur.execute(sql)
    con.commit()
    print(' -> Delete Success !')

def get_link(site) :
    con = db_conn()
    cur = con.cursor()
    sql = "select site_url from info where site_name=%s"
    cur.execute(sql, site)
    return cur.fetchone()[0]