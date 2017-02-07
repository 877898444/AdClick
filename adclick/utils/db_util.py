# coding=utf-8
import MySQLdb


class DB(object):
    def __init__(self):
        self.conn = self.__db_connect()
        self.cur = self.conn.cursor()
        self.conn.select_db('campaign')

    def __db_connect(self):
        conn = MySQLdb.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='a877898444',
            charset='utf8')
        return conn

    def inserttoreprote(self, data_content):
        expr = "insert into reports(fdow,campaigns,time,websites,mode,countries,groups,orders,`generated`,rows)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        campaignlist = data_content['campaigns']
        time = data_content['time']
        ti = str(time)
        websites = data_content['websites']
        countries = data_content['countries']
        groups = data_content['groups']
        orders = data_content['orders']
        rows = data_content['rows']
        rowslist = ''
        for row in range(0, len(rows)):
            rowslist = ''.join(str(row))
        print rowslist

        ins = (data_content['fdow'], str(campaignlist), str(time), str(websites), data_content['mode'], str(countries),
               str(groups), str(orders), data_content['generated'], rowslist)

        self.cur.execute(expr, ins)
        self.conn.commit()

    def insertdata(self, data_content, apiname):
        # sql = "INSERT INTO popads_report (fdow,mode,generated) VALUES (%s,%s,%s)"
        # ins = (data_content['fdow'], data_content['mode'], data_content['generated'])
        # self.cur.execute(sql, ins)
        # self.conn.commit()

        ##expr =  "insert into campaigns_test(campaignId,status,aux_status,group_id,name,budget,url,created) values('%s','%s','%s','%s','%s','%s','%s','%s')"% (data_content['id'], data_content['status'],data_content['aux_status'],data_content['group_id'],data_content['name'],data_content['budget'],str(data_content['url'][0]),data_content['created'])
        # print data_content['fdow'], data_content['mode'], data_content['generated']
        # insert into popads_report(fdow,mode,`generated`) values ('','%s','')

        expr = "insert into popads_report(fdow,mode,`generated`,apiname) values (%s,%s,%s,%s)"  # "generater"在MySQL中是特殊字
        self.cur.execute(expr, (data_content['fdow'], data_content['mode'], data_content['generated'], apiname))

        last_id = self.cur.lastrowid

        for campaign in data_content['campaigns']:
            exp_campaigns = "insert into popads_report_campaigns(campaigns_id,report_id) values ('%s','%s')" % (
                campaign, last_id)
            self.cur.execute(exp_campaigns)

        time = data_content['time']
        exp_time = "insert into popads_report_time(start,end,start_nice,end_nice,offset,quick_name,zone,travel,travel_origin,valid_zone,report_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            time['start'], time['end'], time['start_nice'], time['end_nice'], time['offset'], time['quick_name'],
            time['zone'], time['travel'], time['travel_origin'], time['valid_zone'], last_id)

        self.cur.execute(exp_time)

        for row in data_content['rows']:
            expr = "insert into popads_report_rows(campaign,campaign_id,conversion_count,conversion_profit,conversion_roi,conversion_value,cost,datetime,impressions,website_id,report_id)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            ins = (row['campaign'], row['campaign_id'], row['conversion_count'], row['conversion_profit'],
                   row['conversion_roi'], row['conversion_value'], row['cost'], row['datetime'], row['impressions'],
                   row['website_id'], last_id)
            self.cur.execute(expr, ins)

        self.conn.commit()

    def close(self):
        self.cur.close()
        # self.conn.commit()
        self.conn.close()


db = DB()
if __name__ == '__main__':
    db = DB()
    # data_content = {
    #     "campaignId": "3933746",
    #     "status": "out_of_money",
    #     "aux_status": "approved",
    #     "group_id": None,
    #     "name": "Fonemasti-Weekly-IN-Voda- popads",
    #     "budget": "0",
    #     "url": [
    #         "http://im.jetmobo.com/click.php?c=5&key=9v21efqyfuaer8kn96qcqcgv&c1=[IMPRESSIONID]&c2=[WEBSITEID]&c3=[DEVICENAME]"
    #     ],
    #     "created": "2016-09-22 08:56:58"
    # }
    # db.insertdata(data_content)
    # db.close()
