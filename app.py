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
        100,                    # Level 1 (Root)
        100, 84,              # Level 2
        100, 92, 84, 76,    # Level 3
        100, 96, 92, 88, 84, 80, 76, 72,  # Level 4
        100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70,  # Level 5
        100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 87, 86, 85, 
        84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69  # Level 6
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
    72, 76, 80, 84, 88, 92, 96, 100, # Level 4
    70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, # Level 5
    69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
    85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100 # Level 6
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
        97,                    # Level 1 (Root)
        97, 77,              # Level 2
        97, 85, 77, 69,    # Level 3
        97, 89, 85, 81, 77, 73, 69, 65,  # Level 4
        97, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 65, 63,  # Level 5
        97, 94, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 80, 79, 78, 
        77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62  # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/6')
def index6():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        96,                    # Level 1 (Root)
        96, 78,              # Level 2
        96, 86, 78, 70,    # Level 3
        96, 90, 86, 82, 78, 74, 70, 66,  # Level 4
        96, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64,  # Level 5
        96, 94, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 81, 80, 79, 
        78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63  # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/7')
def index7():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        99,                    # Level 1 (Root)
        99, 96,              # Level 2
        99, 87, 96, 71,    # Level 3
        99, 91, 87, 83, 96, 75, 71, 67,  # Level 4
        99, 93, 91, 89, 87, 85, 83, 81, 96, 77, 75, 73, 71, 69, 67, 65,  # Level 5
        99, 98, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 82, 81, 80, 
        96, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64  # Level 9
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
    100, 86, 98, 70, # Level 3
    100, 90, 86, 82, 98, 74, 70, 66, # Level 4
    100, 92, 90, 88, 86, 84, 82, 80, 98, 76, 74, 72, 70, 68, 66, 64, # Level 5
    100, 99, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79,
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
    100, 99, # Level 2
    100, 88, 80, 99, # Level 3
    100, 92, 88, 84, 80, 76, 72, 99, # Level 4
    100, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 99, # Level 5
    100, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81,
    80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 99, 65 # Level 6
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
        88,                    # Level 1 (Root)
        88, 53,              # Level 2
        88, 61, 53, 45,    # Level 3
        88, 65, 61, 57, 53, 49, 45, 41,  # Level 4
        88, 67, 65, 63, 61, 59, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39,  # Level 5
        88, 81, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 56, 55, 54, 
        53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38  # Level 6
    ]
    
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/16')
def index16():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        100,                    # Level 1 (Root)
        100, 81,              # Level 2
        100, 89, 81, 73,    # Level 3
        100, 93, 89, 85, 81, 77, 73, 69,  # Level 4
        100, 95, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67,  # Level 5
        100, 98, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 84, 83, 82, 
        81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66  # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

@app.route('/tree/17')
def index17():
    # Define your 63 numbers here (arranged by levels)
    tree_data = [
        98,                    # Level 1 (Root)
        98, 80,              # Level 2
        98, 88, 80, 72,    # Level 3
        98, 92, 88, 84, 80, 76, 72, 68,  # Level 4
        98, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66,  # Level 5
        98, 97, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 83, 82, 81, 
        80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65  # Level 6
    ]
    tree_data = level_to_preorder(tree_data)
    return render_template('index.html', tree_data=tree_data)

if __name__ == '__main__':
    app.run(debug=True)