# pi-visual

# Pi Visualization and Approximation

This project consists of two parts:
1. **Pi Approximation** using regular polygons inscribed in a circle.
2. **Pi Visualization** with real-time graphical representation of the circle and regular polygons, showing how increasing the number of sides approximates \(\pi\).

## 1. Pi Approximation (Numerical Method)

The first part of the project approximates the value of \(\pi\) by calculating the area of regular polygons inscribed in a circle. The program starts with a triangle and gradually increases the number of sides, improving the approximation of \(\pi\).

- **side_size(R, n)**: Calculates the side length of a regular polygon with \(n\) sides inscribed in a circle with radius \(R\).
- **Area(R, n)**: Calculates the area of the regular polygon.
- **get_pi(n, Area)**: Calculates the approximation of \(\pi\) based on the polygon's area.

## 2. Pi Visualization (Graphical Representation)

The second part uses Pygame to visually display the approximation of \(\pi\) by drawing a circle and a regular polygon with \(n\) sides. The user can interact with the program to change the number of sides of the polygon and see how the approximation of \(\pi\) improves as the polygon becomes closer to the circle.

- **get_angle(n)**: Calculates the angle between two vertices of the regular polygon.
- **get_vertices(cx, cy, R, n)**: Calculates the vertices of the regular polygon inscribed in the circle.

### Features:
- Displays a circle and a regular polygon with \(n\) sides.
- Updates the approximation of \(\pi\) as the number of sides increases.
- Real-time visualization of the polygon's progression toward the circle.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/x3tra/pi-visual.git
   ```

2. Navigate to the project directory:
   ```bash
   cd pi-visual
   ```

3. Install the required libraries:
   ```bash
   pip install pygame
   ```

4. Run the programs:

   **Numerical Approximation**:
   ```bash
   python pi.py
   ```

   **Graphical Visualization**:
   ```bash
   python pi_visualization.py
   ```

---

## Controls (for Pi Visualization)

- **Arrow Left**: Decrease the number of sides of the polygon.
- **Arrow Right**: Increase the number of sides of the polygon.
- **Spacebar**: Toggle auto-increment mode (the polygon’s sides will increase automatically).
- **Esc**: Exit the program.

## Dependencies

- `pygame`: For graphical visualization and interaction.
