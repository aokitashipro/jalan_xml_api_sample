import urllib.request
from bs4 import BeautifulSoup
import pymysql.cursors
import requests
from tqdm import tqdm


connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='DB_name',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

#CSVから読み込む場合
f = open('APIfile.txt')
lines2 = f.readlines()

for i in lines2:

    # CSVから1行ずつ抜き出すか、直接指定するか
    #Pref = '350000'
    #l_area = '350300'
    #s_area = '350302'

    url = i

    #html = urllib.request.urlopen(url + Pref + "&l_area=" + l_area + "&xml_ptn=2&count=100")
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,"html5lib")

    #print(soup.prettify())

    #items = soup.find("hotel")


    for hotel in soup.findAll("hotel"):
        HotelID = hotel.hotelid.string
        HotelName = hotel.hotelname.string
        PostCode = hotel.postcode.string
        HotelAddress = hotel.hoteladdress.string
        Region = hotel.region.string
        Prefecture = hotel.prefecture.string
        LargeArea = hotel.largearea.string
        SmallArea = hotel.smallarea.string
        HotelType = hotel.hoteltype.string
        HotelDetailURL = hotel.hoteldetailurl.string
        SampleRateFrom = hotel.sampleratefrom.string
        NumberOfRatings = hotel.numberofratings.string
        Rating = hotel.rating.string

        if Rating is None:
            sql = "insert into `table_name` (`HotelID`, `HotelName`, `PostCode`, `HotelAddress`, `Region`, `Prefecture`, `LargeArea`, `SmallArea`, `HotelType`, `HotelDetailURL`, `SampleRateFrom`, `NumberOfRatings`) values( '" + HotelID + "','" + HotelName + "','" + PostCode + "','" + HotelAddress + "','" + Region + "','" + Prefecture + "','" + LargeArea + "','" + SmallArea + "','" + HotelType + "','" + HotelDetailURL + "','" + SampleRateFrom + "','" + NumberOfRatings + "')"

        else:
            sql = "insert into `table_name` (`HotelID`, `HotelName`, `PostCode`, `HotelAddress`, `Region`, `Prefecture`, `LargeArea`, `SmallArea`, `HotelType`, `HotelDetailURL`, `SampleRateFrom`, `NumberOfRatings`, `Rating` ) values( '" + HotelID + "','" + HotelName + "','" + PostCode + "','" + HotelAddress + "','" + Region + "','" + Prefecture + "','" + LargeArea + "','" + SmallArea + "','" + HotelType + "','" + HotelDetailURL + "','" + SampleRateFrom + "','" + NumberOfRatings + "','" + Rating + "')"


        cursor.execute(sql)
        result = cursor.fetchall()
        connection.commit()

connection.close()

f.close()
