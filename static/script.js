document.addEventListener('DOMContentLoaded', function() {

    const treeContainer = document.getElementById('tree-container');

    const width = Math.max(1200, window.innerWidth - 40);

    const height = 800;

    

    // Create SVG element

    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");

    svg.setAttribute("width", width);

    svg.setAttribute("height", height);

    treeContainer.appendChild(svg);


    // Generate tree data

    const levels = 6;

    const nodeRadius = 20;

    let nodeId = 0;  // Start from 0 to match array indexing


    function generateTree(level, x, y, horizontalGap) {

        if (level >= levels) return null;


        const node = {

            id: nodeId,

            x: x,

            y: y,

            value: treeNumbers[nodeId]  // Use value from our array

        };

        nodeId++;


        const nextY = y + 80;

        const nextGap = horizontalGap / 2;


        node.left = generateTree(level + 1, x - horizontalGap, nextY, nextGap);

        node.right = generateTree(level + 1, x + horizontalGap, nextY, nextGap);


        return node;

    }

    // Create the tree structure
    const root = generateTree(0, width / 2, 50, width / 4);

    // Draw the tree
    function drawTree(node) {
        if (!node) return;

        // Draw connections to children
        if (node.left) {
            const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
            line.setAttribute("x1", node.x);
            line.setAttribute("y1", node.y);
            line.setAttribute("x2", node.left.x);
            line.setAttribute("y2", node.left.y);
            line.setAttribute("class", "link");
            svg.appendChild(line);
        }

        if (node.right) {
            const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
            line.setAttribute("x1", node.x);
            line.setAttribute("y1", node.y);
            line.setAttribute("x2", node.right.x);
            line.setAttribute("y2", node.right.y);
            line.setAttribute("class", "link");
            svg.appendChild(line);
        }

        // Create group for node
        const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
        svg.appendChild(g);

        // Draw node
        const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("cx", node.x);
        circle.setAttribute("cy", node.y);
        circle.setAttribute("r", nodeRadius);
        circle.setAttribute("class", "node");
        g.appendChild(circle);

        // Create text element (initially hidden)
        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("x", node.x);
        text.setAttribute("y", node.y);
        text.setAttribute("class", "node-text hidden");
        text.textContent = node.value;
        g.appendChild(text);

        // Add click event
        let isRevealed = false;
        g.addEventListener('click', function() {
            if (!isRevealed) {
                text.classList.remove('hidden');
                text.classList.add('visible');
                isRevealed = true;
            }
        });

        // Recursively draw children
        if (node.left) drawTree(node.left);
        if (node.right) drawTree(node.right);
    }

    drawTree(root);
});