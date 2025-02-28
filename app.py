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
        99,                    # Level 1 (Root)
        83, 99,              # Level 2
        75, 83, 91, 99,    # Level 3
        71, 75, 79, 83, 87, 91, 95, 99,  # Level 4
        69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99,  # Level 5
        68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 
        84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99  # Level 6
    ]
    
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/2')
def index2():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [ 
        100, # Level 1 (Root)
    84, 100, # Level 2
    76, 84, 92, 100, # Level 3
    72, 76, 80, 84, 88, 92, 98, 100, # Level 4
    70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 98, 99, 100, # Level 5
    69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
    85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 98, 33, 99, 97, 100 # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/3')
def index3():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        100, # Level 1 (Root)
    84, 100, # Level 2
    76, 84, 92, 100, # Level 3
    72, 76, 80, 84, 88, 92, 100, 98, # Level 4
    70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 100, 96, 98, 94, # Level 5
    69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
    85, 86, 87, 88, 89, 90, 91, 92, 100, 99, 95, 96, 97, 98, 94, 93 # Level 6
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
        300,                    # Level 1 (Root)
        269, 300,              # Level 2
        75, 269, 91, 300,    # Level 3
        71, 75, 79, 269, 87, 91, 95, 300,  # Level 4
        69, 71, 73, 75, 77, 79, 81, 269, 85, 87, 89, 91, 93, 95, 278, 300,  # Level 5
        68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 269, 
        84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 278, 98, 300  # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/6')
def index6():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        300,                    # Level 1 (Root)
        250, 300,              # Level 2
        75, 250, 91, 300,    # Level 3
        71, 75, 79, 250, 87, 91, 300, 98,  # Level 4
        69, 71, 73, 75, 77, 79, 81, 250, 85, 87, 89, 91, 300, 95, 96, 98,  # Level 5
        68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 250, 
        84, 85, 86, 87, 88, 89, 90, 91, 300, 279, 94, 95, 96, 93, 98, 92  # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/7')
def index7():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        301,                    # Level 1 (Root)
        301, 269,              # Level 2
        75, 301, 91, 269,    # Level 3
        71, 75, 79, 301, 87, 91, 95, 269,  # Level 4
        69, 71, 73, 75, 77, 79, 81, 301, 85, 87, 89, 91, 93, 95, 258, 269,  # Level 5
        68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 298, 301, 
        84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 258, 98, 269  # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/8')
def index8():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        169, # Level 1
    169, 167, # Level 2
    169, 85, 167, 69, # Level 3
    169, 89, 85, 81, 167, 73, 69, 65, # Level 4
    169, 91, 89, 87, 85, 83, 81, 79, 167, 75, 73, 71, 69, 67, 65, 63, # Level 5
    169, 168, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78,
    167, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62 # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/9')
def index9():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        100, # Level 1
    100, 98, # Level 2
    96, 100, 98, 70, # Level 3
    96, 90, 86, 100, 98, 74, 70, 66, # Level 4
    96, 92, 90, 88, 86, 84, 82, 100, 98, 76, 74, 72, 70, 68, 66, 64, # Level 5
    96, 56, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 100, 99,
    98, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63 # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/10')
def index10():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        99, # Level 1
    99, 97, # Level 2
    99, 86, 97, 70, # Level 3
    99, 90, 86, 82, 97, 74, 70, 66, # Level 4
    99, 92, 90, 88, 86, 84, 82, 80, 97, 76, 74, 72, 70, 68, 66, 64, # Level 5
    99, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79,
    97, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63 # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/11')
def index11():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        200, # Level 1
    200, 79, # Level 2
    200, 87, 79, 71, # Level 3
    200, 91, 87, 83, 79, 75, 71, 67, # Level 4
    200, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 65, # Level 5
    200, 101, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80,
    79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64 # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/12')
def index12():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        98, # Level 1
    98, 96, # Level 2
    98, 87, 79, 96, # Level 3
    98, 91, 87, 83, 79, 75, 71, 96, # Level 4
    98, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 96, # Level 5
    98, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80,
    79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 96 # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/13')
def index13():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        100, # Level 1
    100, 98, # Level 2
    100, 88, 80, 98, # Level 3
    100, 99, 88, 84, 80, 76, 72, 98, # Level 4
    100, 94, 99, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 98, # Level 5
    100, 95, 94, 93, 99, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81,
    80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 98, 65 # Level 6
    ]
    
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/14')
def index14():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        99, # Level 1
    99, 98, # Level 2
    99, 89, 81, 98, # Level 3
    99, 93, 89, 85, 81, 77, 73, 98, # Level 4
    99, 95, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 98, # Level 5
    99, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82,
    81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 98 # Level 6
    ]
    
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/15')
def index15():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        99,                    # Level 1 (Root)
        95, 99,              # Level 2
        75, 95, 91, 99,    # Level 3
        71, 75, 79, 95, 87, 91, 95, 99,  # Level 4
        69, 71, 73, 75, 77, 79, 81, 95, 85, 87, 89, 91, 93, 95, 97, 99,  # Level 5
        68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 95, 
        84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99  # Level 6
    ]
    
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/16')
def index16():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        99,                    # Level 1 (Root)
        83, 99,              # Level 2
        75, 83, 91, 99,    # Level 3
        71, 75, 79, 83, 87, 91, 95, 99,  # Level 4
        69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 98, 99,  # Level 5
        68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 
        84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 97, 99  # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/17')
def index17():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        100, # Level 1
    100, 98, # Level 2
    100, 88, 80, 98, # Level 3
    100, 92, 88, 84, 80, 76, 72, 98, # Level 4
    100, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 98, # Level 5
    100, 99, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81,
    80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 98, 65 # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

if __name__ == '__main__':
    app.run(debug=True)