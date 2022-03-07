import logging
from time import sleep
import pytest
from Pages.cyber_attack_page import CyberAttackPage


@pytest.mark.usefixtures("setup")
class TestValidation:

    def test_case1(self):

        cyber_attack_page=CyberAttackPage()
        logging.info("navigating to cyber attack page")

        #sorting name
        filter_names=['Xss','phishing','session','injection','attack']
        for name in filter_names:
            cyber_attack_page.filter_data.set_text(name)
            list=cyber_attack_page.names.get_all_elements()
            logging.info("finding text {}".format(str(list)))
            names=[i.text for i in list]
            logging.info("names text {}".format(str(names)))
            assert name.lower() in str(names).lower(),'{} not present'.format(name)
            sleep(1)

        #sorting data
        all_data = []
        sleep(2)
        list = cyber_attack_page.rows.get_all_elements()
        comp={'low':1,'medium':2,'high':3}
        for li in range(len(list)):
            temp={}
            temp['Name']=cyber_attack_page.get_name(li+1).text

            t=cyber_attack_page.get_no_of_cases(li+1).text
            temp['Number of cases']=cyber_attack_page.convert_value(t)
            temp['Impact score']=float(cyber_attack_page.get_avg_impact_score(li+1).text)

            temp['Complexity']=comp[cyber_attack_page.get_complexity(li+1).text]
            logging.info("name {}".format(str(temp)))
            all_data.append(temp)
        logging.info("all_data {}".format(str(all_data)))

        def get_name(all_data):
            return all_data.get('Name')
        def get_cases(all_data):
            return all_data.get('Number of cases')
        def get_score(all_data):
            return all_data.get('Impact score')
        def get_complex(all_data):
            return all_data.get('Complexity')
        name_sort=all_data.copy()
        name_sort.sort(key=get_name)
        logging.info("get_name all_data {}".format(str(name_sort)))

        all_data.sort(key=get_complex)
        logging.info("get_complex all_data {}".format(str(all_data)))

        all_data.sort(key=get_score)
        logging.info("get_score all_data {}".format(str(all_data)))

        all_data.sort(key=get_cases)
        logging.info("get_cases all_data {}".format(str(all_data)))
        # end of sorting


        sort_data = ['Name','Number of cases', 'Impact score','Complexity']
        for name in sort_data:
            sleep(2)
            list = cyber_attack_page.names.get_all_elements()
            beforesort = [i.text for i in list]
            logging.info("sorted name {}".format(str(beforesort)))
            cyber_attack_page.get_sort_data(name)
            sleep(2)
            if 'Name' == name:
                list = cyber_attack_page.names.get_all_elements()
                names = [i.text for i in list]
                logging.info("finding text {}".format(str(names)))
                name_sort.sort(key=get_name)
                name_sorted = [x[name] for x in name_sort]

            if 'Number of cases' == name:
                list = cyber_attack_page.no_of_cases.get_all_elements()
                names = [i.text for i in list]
                names=[cyber_attack_page.convert_value(case) for case in names]
                logging.info("finding text {}".format(str(names)))
                name_sort.sort(key=get_cases)
                name_sorted = [x[name] for x in name_sort]

            if 'Impact score' == name:
                list = cyber_attack_page.imapact.get_all_elements()
                names = [float(i.text) for i in list]
                logging.info("finding text {}".format(str(names)))
                name_sort.sort(key=get_score)
                name_sorted = [x[name] for x in name_sort]

            if 'Complexity' == name:
                list = cyber_attack_page.complexity.get_all_elements()
                names = [comp[i.text] for i in list]
                logging.info("finding text {}".format(str(names)))
                name_sort.sort(key=get_complex)
                name_sorted = [x[name] for x in name_sort]

            logging.info("get_name all_data {}".format(str(name_sorted)))
            logging.info("names text {}".format(str(names)))
            assert name_sorted==names, '{} not sorted'.format(name)
            sleep(1)

    def test_case2(self):

        cyber_attack_page=CyberAttackPage()
        logging.info("navigating to cyber attack page")

        #sorting data
        all_data = []
        sleep(5)
        list = cyber_attack_page.rows.get_all_elements()
        comp={'low':1,'medium':2,'high':3}
        for li in range(len(list)):
            temp={}
            temp['Name']=cyber_attack_page.get_name(li+1).text

            t=cyber_attack_page.get_no_of_cases(li+1).text
            temp['Number of cases']=cyber_attack_page.convert_value(t)
            temp['Impact score']=float(cyber_attack_page.get_avg_impact_score(li+1).text)

            temp['Complexity']=comp[cyber_attack_page.get_complexity(li+1).text]
            logging.info("name {}".format(str(temp)))
            all_data.append(temp)
        logging.info("all_data {}".format(str(all_data)))

        def get_name(all_data):
            return all_data.get('Name')
        def get_cases(all_data):
            return all_data.get('Number of cases')
        def get_score(all_data):
            return all_data.get('Impact score')
        def get_complex(all_data):
            return all_data.get('Complexity')
        name_sort=all_data.copy()
        name_sort.sort(key=get_name)
        logging.info("get_name all_data {}".format(str(name_sort)))
        all_data.sort(key=get_complex)
        logging.info("get_complex all_data {}".format(str(all_data)))
        all_data.sort(key=get_score)
        logging.info("get_score all_data {}".format(str(all_data)))
        all_data.sort(key=get_cases)
        logging.info("get_cases all_data {}".format(str(all_data)))

        # end of sorting
        sort_data = ['Name','Number of cases', 'Impact score','Complexity']
        for name in sort_data:
            sleep(2)
            list = cyber_attack_page.names.get_all_elements()
            beforesort = [i.text for i in list]
            logging.info("sorted name {}".format(str(beforesort)))
            cyber_attack_page.get_sort_data(name)
            sleep(2)
            if 'Name' == name:
                list = cyber_attack_page.names.get_all_elements()
                names = [i.text for i in list]
                logging.info("finding text {}".format(str(names)))
                name_sort.sort(key=get_name)
                name_sorted = [x[name] for x in name_sort]
            if 'Number of cases' == name:
                list = cyber_attack_page.no_of_cases.get_all_elements()
                names = [i.text for i in list]

                names=[cyber_attack_page.convert_value(case) for case in names]

                logging.info("finding text {}".format(str(names)))
                name_sort.sort(key=get_cases)
                name_sorted = [x[name] for x in name_sort]
            if 'Impact score' == name:
                list = cyber_attack_page.imapact.get_all_elements()
                names = [float(i.text) for i in list]
                logging.info("finding text {}".format(str(names)))
                name_sort.sort(key=get_score)
                name_sorted = [x[name] for x in name_sort]
            if 'Complexity' == name:
                list = cyber_attack_page.complexity.get_all_elements()
                names = [comp[i.text] for i in list]
                logging.info("finding text {}".format(str(names)))
                name_sort.sort(key=get_complex)
                name_sorted = [x[name] for x in name_sort]

            logging.info("get_name all_data {}".format(str(name_sorted)))
            logging.info("names text {}".format(str(names)))

            assert name_sorted==names, '{} not sorted'.format(name)
            sleep(1)
