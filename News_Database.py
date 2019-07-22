import sqlite3

class News():

    def __init__(self,title,section,date,time_read,link,picture):
        self.title = title
        self.section = section
        self.date = date
        self.time_read = time_read
        self.link = link
        self.picture = picture


    def text_of_mail(self):

        section_link = ""
        color = ""

        if (self.section == "Haftanın Özeti"):
            section_link = "https://www.dunyahalleri.com/category/haftanin-ozeti/"
            color = "230,185,53"
        elif (self.section == "Genel Gündem"):
            section_link = "https://www.dunyahalleri.com/category/genel-gundem/"
            color = "3,94,214"
        elif (self.section == "Teknoloji / Bilim"):
            section_link = "https://www.dunyahalleri.com/category/teknoloji-bilim/"
            color = "254,72,29"
        elif (self.section == "İnternet / Girişimler"):
            section_link = "https://www.dunyahalleri.com/category/internet-girisimler/"
            color = "63,126,45"
        elif (self.section == "Tasarım / İnovasyon"):
            section_link = "https://www.dunyahalleri.com/category/tasarim-inovasyon/"
            color = "13,58,91"
        elif (self.section == "Kültür / Sanat"):
            section_link = "https://www.dunyahalleri.com/category/kultur-sanat/"
            color = "29,125,54"


        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title></title>
        </head>
        <body>
        
        <div style="width: 375px; border: 4px solid black; background-color: rgb(237, 237, 237);">
            
            <div style="border-bottom:3px solid black;">
                <a href='https://www.dunyahalleri.com/'><img  style="display: block; margin-left: auto; margin-right: auto; vertical-align:middle;" src='https://www.dunyahalleri.com/wp-content/uploads/2016/07/dh-logo-transparan.png' width="183px" height="90px"></a>
            </div>
            
            <div class="All Info" style="margin-top: 5px; text-decoration: none;">
                
                <div class="Image Div" style="margin-bottom: 3px;">
                    <a href='""" + self.link + """'><img style="display: block; margin-left: auto; margin-right: auto; vertical-align:middle;" src='""" + self.picture + """' width="295px" height="195px"></a>
        
                    
                    <div style="font: 18px/1.5 'Ubuntu', Arial, sans-serif;">
                        <a href='""" + section_link + """' style="text-decoration: none;"><p style="background-color: rgb(""" + color + """); margin-top: 6px; padding-left: 40px; color:white; margin-bottom: 3px;">""" + self.section + """</p></a>
                    </div>
        
                </div>
        
                <div class="Info Div" style="margin-top: 2px;">
                    <div style="text-decoration: none; margin-left: 40px; width: 300px; font-family: 'Roboto Slab';"> 
                        <a href='""" + self.link + """' style="text-decoration: none; color: black; font: 20px/20px 'Contentia Bold'"><h3>""" + self.title + """</h3></a>
                    </div>
                    
                    <div style="margin-bottom: 3px;"></div>

                    <div style="margin-top: -20px; margin-left: 40px; width: 300px; font: 14px/1.5 'Ubuntu', Arial, sans-serif;"">
                        <span>
                             """ + self.date + """&ensp; &ensp;
                        </span>
        
                        <span>
                            """ + self.time_read + """
                        </span>
        
                    </div>

                    <div style="margin-bottom: 5px;"></div>
        
                </div>
        
            </div>
        </div>
        
        </body>
        </html>
        """


class Database_Post():

    def __init__(self):

        self.connect_database()

    def connect_database(self):

        self.connection = sqlite3.connect("World News.db")
        self.cursor = self.connection.cursor()

        query = "create table if not exists " \
                "Tbl_News (" \
                "Title text," \
                "Section text," \
                "Date text," \
                "Time_Read text," \
                "Link text," \
                "Picture text)"
        self.cursor.execute(query)
        self.connection.commit()

    def check_if_post_exists(self,link):

        query = "select * from tbl_news where link = @p1"
        self.cursor.execute(query,(link,))
        posts = self.cursor.fetchall()

        if (len(posts) == 0):
            return 0

        else:
            return 1

    def add_post(self,News):

        query = "insert into tbl_news values (@p1,@p2,@p3,@p4,@p5,@p6)"
        self.cursor.execute(query,(News.title,News.section,News.date,News.time_read,News.link,News.picture))
        self.connection.commit()
