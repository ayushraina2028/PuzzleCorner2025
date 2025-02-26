from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def level_to_preorder(level_order):
    def get_preorder(index):
        if index >= len(level_order):
            return []
        # Current node
        current = [level_order[index]]

        # Left child index: 2*i + 1
        # Right child index: 2*i + 2
        left = get_preorder(2 * index + 1)
        right = get_preorder(2 * index + 2)

        return current + left + right
    return get_preorder(0)

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
    
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/4')
def index4():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        99,                    # Level 1 (Root)
        83, 99,              # Level 2
        75, 83, 91, 99,    # Level 3
        71, 75, 79, 83, 87, 91, 95, 99,  # Level 4
        69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99,  # Level 5
        68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 
        84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99  # Level 6
    ]
    
    preorder = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=preorder)

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
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
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
    
    tree_data = level_to_preorder(tree_data)
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
    
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/15')
def index15():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        300,                    # Level 1 (Root)
        250, 750,              # Level 2
        125, 375, 625, 875,    # Level 3
        62, 187, 312, 437, 562, 687, 812, 937,  # Level 4
        31, 93, 156, 218, 281, 343, 406, 468, 531, 593, 656, 718, 781, 843, 906, 968,  # Level 5
        15, 46, 77, 108, 139, 170, 201, 232, 263, 294, 325, 356, 387, 418, 449, 480, 
        511, 542, 573, 604, 635, 666, 697, 728, 759, 790, 821, 852, 883, 914, 945, 976  # Level 6
    ]
    
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
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
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

if __name__ == '__main__':
    app.run(debug=True)