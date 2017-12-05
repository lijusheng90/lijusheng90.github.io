# coding:utf-8
import psycopg2

class MyPostgre():
    def __init__(self,host="127.0.0.1",user="odoo_ljs",password="odoo_ljs",database="CW_cp",port='5432'):
        self.myconn = psycopg2.connect(host=host,user=user,password=password,database=database,port=port)


    def exe_sql(self,sql):
        cur = self.myconn.cursor()
        cur.execute(sql)

        self.myconn.commit() # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
        rets = cur.fetchall()
        return rets

    def exe_run(self,sql):
        cur = self.myconn.cursor()
        cur.execute(sql)

        self.myconn.commit()  # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
        # rets = cur.fetchall()
        # return rets


    def __del__(self):
        self.myconn.close()




