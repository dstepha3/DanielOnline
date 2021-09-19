from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#img_src's must be direct links for some reason,
#chose imgur as image host
Plants = [
    {
        'name': 'Algaonema',
        'img_src': 'https://i.imgur.com/VYlR2xC.jpg', 
        'modal_id': '#aglaModal',
        'active': False,
    },
    {
        'name': 'Dracaena',
        'img_src': 'https://i.imgur.com/BAAcnBa.jpg', 
        'modal_id': '#dracaenaModal',
        'active': False,
    },
    {
        'name': 'Epipremnum',
        'img_src': 'https://i.imgur.com/GkMG42V.jpg', 
        'modal_id': '#epipremnumModal',
        'active': False,
    },  
    {
        'name': 'Ficus',
        'img_src': 'https://i.imgur.com/UlpMVYC.jpg', 
        'modal_id': '#ficusModal',
        'active': False,
    },
    {
        'name': 'Garden',
        'img_src': 'https://i.imgur.com/SQHHpAh.jpg', 
        'modal_id': '#gardenModal',
        'active': False,
    },
    {
        'name': 'Miscellaneous',
        'img_src': 'https://i.imgur.com/QGAckPl.jpg', 
        'modal_id': '#miscModal',
        'active': False,
    },  
    {
        'name': 'Palms',
        'img_src': 'https://i.imgur.com/g6K5yWX.jpg', 
        'modal_id': '#palmsModal',
        'active': False,
    }, 
    {
        'name': 'Philodenderon',
        'img_src': 'https://i.imgur.com/oibHCCL.jpg', 
        'modal_id': '#philoModal',
        'active': False,
    },
    {
        'name': 'Rhapidophora',
        'img_src': 'https://i.imgur.com/xgipV3i.jpg', 
        'modal_id': '#rhaphModal',
        'active': False,
    },
    {
        'name': 'Sanseveria',
        'img_src': 'https://i.imgur.com/mFNFLKQ.jpg', 
        'modal_id': '#snakeModal',
        'active': False,
    },
    {
        'name': 'Scindapsus',
        'img_src': 'https://i.imgur.com/M9cuNAp.jpg', 
        'modal_id': '#scindapsusModal',
        'active': False,
    },
    {
        'name': 'Succulents',
        'img_src': 'https://i.imgur.com/ZUJ6z6A.jpg', 
        'modal_id': '#succulentsModal',
        'active': False,
    },
    {
        'name': 'Syngonium',
        'img_src': 'https://i.imgur.com/3EIGCWD.jpg', 
        'modal_id': '#syngoniumModal',
        'active': False,
    },
    {
        'name': 'ZZ',
        'img_src': 'https://i.imgur.com/Z1j8zPC.jpg', 
        'modal_id': '#zzModal',
        'active': False,
    }    
]

KentCoreCourses = [
    {
        'course': 'US 10097',
        'title': 'Destination Kent State: First Year Experience', 
        'grade': 'B',
        'credits': '1',
        'term': 'Fall 2013'
    },
    {
        'course': 'ENG 11011',
        'title': 'College Writing I', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2018'
    },
    {
        'course': 'ENG 21011',
        'title': 'College Writing II', 
        'grade': 'A-',
        'credits': '3',
        'term': 'Spring 2019'
    },
    {
        'course': 'CS 10051',
        'title': 'Intro to Computer Science', 
        'grade': 'A',
        'credits': '4',
        'term': 'Spring 2018'
    },
    {
        'course': 'HIST 11051',
        'title': 'Modern World History', 
        'grade': 'B',
        'credits': '3',
        'term': 'Spring 2018'
    },
    {
        'course': 'HIST 12071',
        'title': 'Modern America', 
        'grade': 'C',
        'credits': '3',
        'term': 'Fall 2018'
    },
    {
        'course': 'THEA 11000',
        'title': 'The Art of Theatre', 
        'grade': 'C',
        'credits': '3',
        'term': 'Spring 2014'
    },
    {
        'course': 'PSYC 11761',
        'title': 'General Psychology', 
        'grade': 'C',
        'credits': '3',
        'term': 'Fall 2013'
    },
    {
        'course': 'SOC 12050',
        'title': 'Introduction to Sociology', 
        'grade': 'D',
        'credits': '3',
        'term': 'Spring 2014'
    },
    {
        'course': 'BSCI 20020',
        'title': 'Biological Structure and Function', 
        'grade': 'B',
        'credits': '5',
        'term': 'Fall 2013'
    },
    {
        'course': 'BSCI 20021',
        'title': 'Basic Microbiology', 
        'grade': 'B-',
        'credits': '3',
        'term': 'Fall 2014'
    },
    {
        'course': 'CHEM 10050',
        'title': 'Fundamentals of Chemistry', 
        'grade': 'C-',
        'credits': '3',
        'term': 'Fall 2013'
    },
    {
        'course': 'NURS 10050',
        'title': 'Intro to Professional Nursing', 
        'grade': 'A',
        'credits': '1',
        'term': 'Spring 2014'
    },
    {
        'course': 'MATH 11009',
        'title': 'Modeling Algebra', 
        'grade': 'D+',
        'credits': '4',
        'term': 'Fall 2013'
    },
    {
        'course': 'MATH 11010',
        'title': 'Algebra For Calculus', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2018'
    },
    {
        'course': 'MATH 11022',
        'title': 'Trigonometry', 
        'grade': 'C+',
        'credits': '3',
        'term': 'Spring 2019'
    },
    {
        'course': 'SPAN 18201',
        'title': 'Elementary Spanish I', 
        'grade': 'C',
        'credits': '4',
        'term': 'Spring 2018'
    },
    {
        'course': 'SPAN 18202',
        'title': 'Elementary Spanish II', 
        'grade': 'B+',
        'credits': '4',
        'term': 'Fall 2018'
    }
]

MajorCourses = [
    {
        'course': 'CS 13001',
        'title': 'Computer Science I: Programming / Problem Solving', 
        'grade': 'A',
        'credits': '4',
        'term': 'Spring 2019'
    },
    {
        'course': 'CS 23001',
        'title': 'Computer Science II: Data Structures', 
        'grade': 'A',
        'credits': '4',
        'term': 'Fall 2019'
    },
    {
        'course': 'CS 23022',
        'title': 'Discrete Structures for Computer Science', 
        'grade': 'B-',
        'credits': '3',
        'term': 'Spring 2019'
    },
    {
        'course': 'CS 33007',
        'title': 'Introduction to Database System Design', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'CS 33101',
        'title': 'Structure of Programming Languages', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'CS 33211',
        'title': 'Operating Systems', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2020'
    },
    {
        'course': 'CS 33901',
        'title': 'Software Engineering', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2020'
    },
    {
        'course': 'CS 35101',
        'title': 'Computer Architecture', 
        'grade': 'B+',
        'credits': '3',
        'term': 'Fall 2019'
    },
    {
        'course': 'CS 35201',
        'title': 'Computer Communication Networks', 
        'grade': 'A-',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'CS 44001',
        'title': 'Computer Science III: Programming Patterns', 
        'grade': 'YD',
        'credits': '4',
        'term': 'Spring 2021'
    },
    {
        'course': 'CS 46101',
        'title': 'Design and Analysis of Algorithms', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2021'
    },
    {
        'course': 'CS 44105',
        'title': 'Web Programming I', 
        'grade': 'A-',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'MATH 12002',
        'title': 'Analytic Geometry and Calculus I', 
        'grade': 'B',
        'credits': '5',
        'term': 'Fall 2019'
    },
    {
        'course': 'MATH 12003',
        'title': 'Analytic Geometry and Calculus II', 
        'grade': 'B-',
        'credits': '5',
        'term': 'Spring 2020'
    },
    {
        'course': 'MATH 22005',
        'title': 'Analytic Geometry and Calculus III', 
        'grade': 'A-',
        'credits': '4',
        'term': 'Summer 2021'
    },
    {
        'course': 'MATH 21001',
        'title': 'Linear Algebra', 
        'grade': 'TBA',
        'credits': '4',
        'term': 'Fall 2021'
    },
    {
        'course': 'CS 43203',
        'title': 'Systems Programming', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2021'
    },
    {
        'course': 'CS 47205',
        'title': 'Information Security', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2020'
    },
    {
        'course': 'CS 47207',
        'title': 'Digital Forensics', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'CS 47221',
        'title': 'Introduction to Cryptology', 
        'grade': 'TBA',
        'credits': '3',
        'term': 'Fall 2021'
    },
    {
        'course': 'CS 49999',
        'title': 'Capstone Project', 
        'grade': 'A',
        'credits': '4',
        'term': 'Spring 2021'
    },
]




# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


#########     Plant Routes      #########
@app.route('/api/plants', methods=['GET'])
def my_plants():
    return jsonify(Plants)


#########      Course Routes      #########
@app.route('/api/courses/kentcore', methods=['GET'])
def kentCore():
    return jsonify(KentCoreCourses)


@app.route('/api/courses/majorcourses', methods=['GET'])
def majorCourses():
    return jsonify(MajorCourses)


#########      Start Flask      #########
if __name__ == '__main__':
    app.run()