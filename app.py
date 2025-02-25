from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/get_random_number')
def get_random_number():
    number = random.randint(1, 17)
    return jsonify({'number': number})

@app.route('/tree/1')
def index():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/2')
def index2():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/3')
def index3():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/4')
def index4():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/5')
def index5():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/6')
def index6():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/7')
def index7():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/8')
def index8():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/9')
def index9():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/10')
def index10():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/11')
def index11():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/12')
def index12():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/13')
def index13():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/14')
def index14():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/15')
def index15():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/16')
def index16():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/17')
def index17():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        500,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    return render_template('index.html', tree_data=tree_data)

if __name__ == '__main__':
    app.run(debug=True)