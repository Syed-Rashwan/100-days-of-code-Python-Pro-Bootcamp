import turtle
# import matplotlib.pyplot as plt

# Function to draw a Sierpinski Triangle using recursion
def drawsierpinski_triangle(t, length, depth, levels):
    if depth == 0:
        
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
       
        levels[depth] += 1
        drawsierpinski_triangle(t, length / 2, depth - 1, levels)
        t.forward(length / 2)
        drawsierpinski_triangle(t, length / 2, depth - 1, levels)
        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        drawsierpinski_triangle(t, length / 2, depth - 1, levels)
        t.left(60)
        t.backward(length / 2)
        t.right(60)


def draw_fractal():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Sierpinski Triangle")

    # Create Turtle object
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, -150)
    t.pendown()

    # Parameters
    depth = 4
    levels = [0] * (depth + 1)
    length = 400

    # Draw the fractal
    drawsierpinski_triangle(t, length, depth, levels)
    turtle.done()
    
    # Return the recursion depth levels
    return levels


# Function to create a pie chart visualization
def plot_pie_chart(levels):
    depths = [f"Depth {i}" for i in range(len(levels))]
    plt.figure(figsize=(8, 8))
    plt.pie(levels, labels=depths, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    plt.title("Recursion Depth Distribution")
    plt.show()

# Main Execution
if __name__ == "__main__":
    # Draw the fractal and get recursion depth data
    recursion_levels = draw_fractal()
    
    # Visualize the recursion depth distribution with a pie chart
   # plot_pie_chart(recursion_levels)