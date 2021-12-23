from bs4 import BeautifulSoup
import requests
import pandas as pd 

url = 'https://www.alodokter.com/komunitas/topic-tag/'
list_penyakit = ['depresi','skizofrenia','bipolar','kecemasan','insomnia','transgender']
halaman = 30

for penyakit in list_penyakit:
    isi = []
    for x in range(1,halaman):
        html2 = requests.get(url+penyakit+'/page/'+str(x)).text
        soup2 = BeautifulSoup(html2, 'lxml')

        link = soup2.find_all(attrs={"notification":True})
        total = len(link)
        for i in range(0,total):
            linknya = link[i]['href']
            print(linknya)

            html = requests.get('https://www.alodokter.com'+linknya).text
            soup = BeautifulSoup(html, 'lxml')

            a = soup.find(attrs={"member-topic-title":True})

            content = a['member-topic-content']
            split_content = content.split()
            content2 = ""
            for s in split_content:
                if s.find('\\') == -1:
                    content2 = content2+s+" "
            #print(content2)
            isi.append([content2,penyakit])

    df = pd.DataFrame(isi,columns=['kalimat', 'tag'])
    df.to_csv("dataset alodokter "+penyakit+".csv",sep=';',index=False)