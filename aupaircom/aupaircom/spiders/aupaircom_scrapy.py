import scrapy
import pandas as pd
from bs4 import BeautifulSoup
import re

class AupaircomScrapySpider(scrapy.Spider):
    name = 'aupaircom_scrapy'
    allowed_domains = ['aupair.com']
    start_urls = list(pd.read_excel('link_to_all_families.xlsx')['families'])

    def parse(self, response):
        ID=''
        enfant = ''
        ville=''
        family_description =''
        start_date = ''
        duration = ''
        task_description=''
        work_hour =''
        salary = ''
        time_stay = ''
        earliest_start_date =''
        lates_start_date = ''
        age_enfant = ''
        number_enfant = ''
        requirements_sumary =''
        family_sumary =''
        place_live_in = ''
        mariage_situation = ''
        parent_age = ''
        nationality = ''
        speaking_language = ''
        profession = ''
        people_in_house = ''
        age_enfant_2 = ''
        required_experience = '' 
        language_level =''
        age_wish =''
        care_personnes_handi = ''
        care_animal = ''
        swim=''
        bike_cycle =''
        take_language_course = ''
        first_aid_certificate = ''
        driver_license = ''
        
        link_to_family = response.request.url
        
        family_description = response.xpath("//div[@class='profileBannerRight']/span/text()").extract_first() + '\n' + response.xpath("//div[@class='profileBannerRight']/h1/text()").extract_first()
        
        family_description = re.sub(' +',' ',family_description)
        family_description =  re.sub('\s+',' ',family_description)
        
        sumary_box = response.xpath("//div[@class='summary_box']").extract()
        if len(sumary_box) != 0:
            try: 
                soup = BeautifulSoup(sumary_box[0],'html.parser')
            except:
                soup = '' 
            if soup != '':
               for info in soup.find_all('p'):
                   if'enfants'in info.text.lower():
                       enfant = info.span.text
                   if 'ville' in info.text.lower():
                       ville = info.span.text
                   if 'id' in info.text.lower():
                       ID = info.span.text
                   if 'd??but de travail' in info.text.lower():
                       start_date = info.span.text
                       start_date = re.sub('\n+',' ',start_date)
                   if "besoin d'au pair pour" in info.text.lower():
                       duration = info.span.text
                       
        tag_task_description = response.xpath("//div[@class='jobDesc']").extract()
        if len(tag_task_description) !=0:
            try: 
                soup = BeautifulSoup(tag_task_description[0],'html.parser').text
                task_description = re.sub(' +',' ',soup)
                task_description =  re.sub('\n\n\n+','\n\n',task_description)
                task_description = task_description.replace('Description des t??ches','')
#                task_description =  re.sub('\t+','',task_description)
            except:
                pass
        requirements = response.xpath("//div[@id='jobDescHeight']").extract()
        if len(requirements) != 0:
            try: 
                soup = BeautifulSoup(requirements[0],'html.parser')
                requirements_sumary = soup.text
                requirements_sumary = re.sub(' +',' ',requirements_sumary)
                requirements_sumary =  re.sub('\n\n\n+','\n\n',requirements_sumary)
                requirements_sumary = requirements_sumary.replace('T??ches requises','')
#                requirements_sumary =  re.sub('\t+','',requirements_sumary)
                
            except:
                soup = '' 
            if soup != '':
                for info in soup.find_all('p'):
                    if 'heures de travail' in info.text.lower():
                        work_hour = info.span.text
                    if 'argent de poche' in info.text.lower():
                        salary = info.span.text
                
                    if 'dur??e du s??jour souhait??' in info.text.lower():
                        time_stay = info.span.text
                    if 'date de d??but (au plus t??t)' in info.text.lower():
                        earliest_start_date = info.span.text
                    if 'date de d??but (au plus tard)' in info.text.lower():
                        lates_start_date = info.span.text
                    if '??ge des enfants' in info.text.lower():
                        age_enfant = info.span.text
                    if "nombre d'enfants" in info.text.lower():
                        number_enfant = info.span.text
                    if 'exp??rience minimale en garde' in info.text.lower():
                        required_experience = info.span.text
                    if 'niveau de langue souhait??' in info.text.lower():
                        language_level = info.span.text
                    if '??ge souhait??' in info.text.lower():
                        age_wish = info.span.text
                        
                    if 'soins aux enfants/personnes handicap??es' in info.text.lower():
                        care_personnes_handi = info.span.text
                    if 'soins des animaux' in info.text.lower():
                        care_animal = info.span.text
                    if 'doit pouvoir nager' in info.text.lower():
                        swim = info.span.text
                    if 'doit pouvoir faire du v??lo' in info.text.lower():
                        bike_cycle = info.span.text
                    if 'peut suivre un cours de langue' in info.text.lower():
                        take_language_course = info.span.text
                    if 'doit avoir le brevet de secourisme' in info.text.lower():
                        first_aid_certificate = info.span.text
                    if 'doit avoir le permis de conduire' in info.text.lower():
                        driver_license = info.span.text
                        
                        
        info_family = response.xpath('//div[@id="familyInfoHeight"]').extract()
        if len(info_family) != 0:
            try: 
                soup = BeautifulSoup(info_family[0],'html.parser')
                family_sumary = soup.text
                family_sumary = re.sub(' +',' ',family_sumary)
                family_sumary =  re.sub('\n+','\n',family_sumary)
                family_sumary = family_sumary.replace('Informations sur la famille','')
#                family_sumary =  re.sub('\t+','',family_sumary)
            except:
                soup = '' 
            if soup != '':
                for info in soup.find_all('p'):
                    if 'la famille vit dans' in info.text.lower():
                        place_live_in = info.span.text
                    if 'je suis un parent celibataire' in info.text.lower(): #'La personne ??g??e vit-elle seule ?'
                        mariage_situation = info.span.text
                    if "l'??ge des parents" in info.text.lower():
                        parent_age = info.span.text
                    if 'nationalit??' in info.text.lower():
                        nationality = info.span.text
                    if 'langues parl??es' in info.text.lower():
                        speaking_language = info.span.text
                    if 'profession' in info.text.lower():
                        profession = info.span.text
                    if 'personnes qui vivent dans la maison' in info.text.lower():
                        people_in_house = info.span.text
                    if '??ge et sexe des enfants' in info.text.lower():
                        age_enfant_2 = info.span.text
        dictionary_data =  {'li??n k???t' : link_to_family, 'l???i gi???i thi???u':family_description,'id':ID, 'enfants' :enfant, 'th??nh ph??? s???ng': ville, 'th???i gian l??m vi???c' : start_date, 'th???i gian c???n aupair' : duration, 
                      'm?? t??? c??ng vi???c':task_description,
                      'th???i gian l??m vi???c h??ng tu???n': work_hour, 'l????ng' : salary, 'th???i gian ???' : time_stay, 'ng??y b???t ?????u s???m nh???t' : earliest_start_date, 'ng??y b???t ?????u mu???n nh???t' : lates_start_date,
                      'tu???i c???a tr??? em' : age_enfant , 's??? l?????ng tr??? em' : number_enfant, 
                      'm?? t??? chung v??? gia ????nh ch??? nh??' : family_sumary, 'n??i ??? (th??nh ph???/l??ng)' : place_live_in, 't??nh tr???ng h??n nh??n c???a ch??? nh??' : mariage_situation,
                      'tu???i c???a ch??? nh??': parent_age, 'qu???c t???ch c???a ch??? nh??' : nationality, 'ng??n ng??? d??ng ??? nh??': speaking_language, 'ngh??? nghi???p c???a ch??? nh??' : profession,
                      's??? l?????ng ng?????i s???ng trong nh??' : people_in_house, 'tu???i c???a tr??? em c???n ch??m s??c' : age_enfant_2 , 
                      'm?? t??? chung v??? y??u c???u v???i aupair' : requirements_sumary ,
                      'y??u c???u v??? kinh nghi???m gi??? tr???' : required_experience,
                      'y??u c???u v??? ng??n ng??? c???a aupair' : language_level, 'ch??m s??c ng?????i khuy???t t???t' : care_personnes_handi, 'ch??m s??c v???t nu??i' : care_animal,
                      'tu???i c???a aupair' : age_wish , 'y??u c???u bi???t b??i' : swim, 'y??u c???u bi???t ??i xe ?????p': bike_cycle, 'quy???n l???i tham gia kh??a h???c ti???ng' : take_language_course,
                      'y??u c???u ch???ng ch??? s?? c???u' : first_aid_certificate, 'y??u c???u bi???t l??i xe ?? t??' : driver_license      }
        
        yield dictionary_data
