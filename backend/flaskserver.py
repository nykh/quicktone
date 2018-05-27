from flask import Flask, render_template, request, jsonify
import json
import os
import jinja2
import csv

# suppose level 1 is tone 2, level 2 is tone 3, level 3 is tone 1
# test use only Json data
#  text = '{"data": [[5, 1, 3, 5, 4], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]}'

app = Flask(__name__)
app.jinja_loader = jinja2.FileSystemLoader('.')

@app.route('/howmany', methods=['GET'])
def number():
   num = os.popen('wc -l result.csv').read().split(' ')[0]
   return render_template('number.html', num=num)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_data()
        j_data =  json.loads(data.decode('utf-8'))
        #print (j_data['data'])
        #print(j_data)
        print(j_data['questionaire'])
        # 8 tones is the final version
        level = len(j_data['data'])
        toneCount = len(j_data['data'][0])
        print(level)
        print(toneCount)
        csvfile = open('result.csv', 'r')
        reader = csv.reader(csvfile)
        all_lines = list(reader)
        #print(all_lines)
        data = [[[0 for k in range(toneCount)] for j in range(3)] for i in range(level)]
        linesLength = 0;
        if(len(all_lines) >= 3):
            linesLength = 3
        else:
            linesLength = len(all_lines)
        for y in range(0, level):
            # last_line is a new 4*8 line
            # 3 lines for result
            # every lines should be 4 * 8 array
            for x in range(0, linesLength):
                last_line = all_lines[-1 - x]
                # print(last_line)
                for i in range(0, toneCount):
                    data[y][x][i] = last_line[y * toneCount + i] 
        csvfile.close()
        #print(data)
        f = open('result.csv', 'a')
        for level in j_data['data']:
            for point in level:
                f.write(str(point))
                f.write(',')
        # every line is a result for a request
        f.write(str(j_data['questionaire']['learner']))
        f.write(',')
        f.write(str(j_data['questionaire']['englishspeaker']))
        f.write(',')
        f.write(str(j_data['questionaire']['drawtone']))
        f.write(',')
        f.write(j_data['questionaire']['language'])
        f.write(',')
        f.write(str(j_data['questionaire']['years']))
        f.write('\n')
        f.close()       

        datadict = {}
        datadict['data'] = data
        #print(datadict)
        json_data = json.dumps(datadict)
        print(json_data)
        return jsonify(data=data)
    else:
        return render_template('index.html')



if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

