# import requests
# from decouple import config
#
# API_KEY = config('API_KEY')
# CX_KEY = config('CX_KEY')
#
#
# def is_copied(essay):
#     # try:
#         sentences = essay.split('.')
#         result = {}
#         for sentence in sentences:
#             search_results = search(sentence)
#         #     if(search_results):
#         #         if len(search_results) > 1:
#         #             result[sentence] = True
#         #             print(True)
#         #         else:
#         #             result[sentence] = False
#         # print(result)
#     # except:
#     #     print("Something went wrong.")
#
#
# def search(query):
#     url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX_KEY}&q={query}'
#     response = requests.get(url)
#     try:
#         # results = response.json()['items']
#         print(response.json())
#         # urls = [result['link'] for result in results]
#         # return urls
#     except:
#         print("Something went wrong.")
#
# print(is_copied('''Data has been more and more influential in defining what it means for firms to be successful over the past couple of decades. It fascinates me how corporations can generate large profits by making the correct decisions at the right moment. Another fascinating aspect is how talents, technology, and processes are utilized to investigate and explore prior business performance to obtain insight and influence business strategy. Business analytics is a broad and diversified idea that may be applied to any industry, but the outcomes will never be the same. The more I attempt to grasp Business Analytics, the more I realize how broad it is; this is one of the main reasons I want to pursue a master's with this degree. I completed my bachelor's in Electronics and Communications Engineering as a major from Bhoj Reddy Engineering College for Women, Hyderabad, India (affiliated to JNTUH- Jawaharlal Nehru Technological University Hyderabad). I feel that I learn best in an atmosphere that is nurturing but which also has enough elements of competition to make it challenging. I like to understand the reasoning and logic behind everything I encounter or experience. It has also encouraged me to believe that I can do better each time. The undergraduate program not only helped me build a strong foundation in electronics engineering fundamentals but also made me conceptually sound in the vast field of both communication and computer engineering. During my under-graduation, I learnt C and C++, and MATLAB, which have given me primary exposure to computer technology. I was exposed to various computer subjects like Java, Data Structures, Information Technology, Fuzzy Logic, and Principles of Management. I gradually immersed myself in this field, thus laying a strong foundation for my skills in computer science. In my UG studies, I did numerous projects as a part of academics. I completed my projects based on Raspberry pi and Python, “Semantic Aware Real-Time Scheduling in Robotics", which uses a C++ application along with Microcontrollers. Involving designing, coding, Developing, and maintaining electronic circuit systems through computer applications has motivated my confidence in the computer technology arena. This tempted me to pursue higher studies. I supplemented my knowledge and experience by taking up various leadership responsibilities throughout my university journey. I have been the Class Representative for five semesters,many skills such as lean six sigma, Project Management, CRM, CSS, HTML, JavaScript, MySQL, and Data management. The experience I have accrued in AMAZON is invaluable. These projects inspired me to learn more about all things data and analytics in the business world. Through Google Data Analytics Professional Certification, I have expanded my skills in R language, SQL language and some visualization tools.'''))