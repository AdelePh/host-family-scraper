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
                   if 'début de travail' in info.text.lower():
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
                task_description = task_description.replace('Description des tâches','')
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
                requirements_sumary = requirements_sumary.replace('Tâches requises','')
#                requirements_sumary =  re.sub('\t+','',requirements_sumary)
                
            except:
                soup = '' 
            if soup != '':
                for info in soup.find_all('p'):
                    if 'heures de travail' in info.text.lower():
                        work_hour = info.span.text
                    if 'argent de poche' in info.text.lower():
                        salary = info.span.text
                
                    if 'durée du séjour souhaité' in info.text.lower():
                        time_stay = info.span.text
                    if 'date de début (au plus tôt)' in info.text.lower():
                        earliest_start_date = info.span.text
                    if 'date de début (au plus tard)' in info.text.lower():
                        lates_start_date = info.span.text
                    if 'âge des enfants' in info.text.lower():
                        age_enfant = info.span.text
                    if "nombre d'enfants" in info.text.lower():
                        number_enfant = info.span.text
                    if 'expérience minimale en garde' in info.text.lower():
                        required_experience = info.span.text
                    if 'niveau de langue souhaité' in info.text.lower():
                        language_level = info.span.text
                    if 'âge souhaité' in info.text.lower():
                        age_wish = info.span.text
                        
                    if 'soins aux enfants/personnes handicapées' in info.text.lower():
                        care_personnes_handi = info.span.text
                    if 'soins des animaux' in info.text.lower():
                        care_animal = info.span.text
                    if 'doit pouvoir nager' in info.text.lower():
                        swim = info.span.text
                    if 'doit pouvoir faire du vélo' in info.text.lower():
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
                    if 'je suis un parent celibataire' in info.text.lower(): #'La personne âgée vit-elle seule ?'
                        mariage_situation = info.span.text
                    if "l'âge des parents" in info.text.lower():
                        parent_age = info.span.text
                    if 'nationalité' in info.text.lower():
                        nationality = info.span.text
                    if 'langues parlées' in info.text.lower():
                        speaking_language = info.span.text
                    if 'profession' in info.text.lower():
                        profession = info.span.text
                    if 'personnes qui vivent dans la maison' in info.text.lower():
                        people_in_house = info.span.text
                    if 'âge et sexe des enfants' in info.text.lower():
                        age_enfant_2 = info.span.text
        dictionary_data =  {'liên kết' : link_to_family, 'lời giới thiệu':family_description,'id':ID, 'enfants' :enfant, 'thành phố sống': ville, 'thời gian làm việc' : start_date, 'thời gian cần aupair' : duration, 
                      'mô tả công việc':task_description,
                      'thời gian làm việc hàng tuần': work_hour, 'lương' : salary, 'thời gian ở' : time_stay, 'ngày bắt đầu sớm nhất' : earliest_start_date, 'ngày bắt đầu muộn nhất' : lates_start_date,
                      'tuổi của trẻ em' : age_enfant , 'số lượng trẻ em' : number_enfant, 
                      'mô tả chung về gia đình chủ nhà' : family_sumary, 'nơi ở (thành phố/làng)' : place_live_in, 'tình trạng hôn nhân của chủ nhà' : mariage_situation,
                      'tuổi của chủ nhà': parent_age, 'quốc tịch của chủ nhà' : nationality, 'ngôn ngữ dùng ở nhà': speaking_language, 'nghề nghiệp của chủ nhà' : profession,
                      'số lượng người sống trong nhà' : people_in_house, 'tuổi của trẻ em cần chăm sóc' : age_enfant_2 , 
                      'mô tả chung về yêu cầu với aupair' : requirements_sumary ,
                      'yêu cầu về kinh nghiệm giữ trẻ' : required_experience,
                      'yêu cầu về ngôn ngữ của aupair' : language_level, 'chăm sóc người khuyết tật' : care_personnes_handi, 'chăm sóc vật nuôi' : care_animal,
                      'tuổi của aupair' : age_wish , 'yêu cầu biết bơi' : swim, 'yêu cầu biết đi xe đạp': bike_cycle, 'quyền lợi tham gia khóa học tiếng' : take_language_course,
                      'yêu cầu chứng chỉ sơ cứu' : first_aid_certificate, 'yêu cầu biết lái xe ô tô' : driver_license      }
        
        yield dictionary_data
