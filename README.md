# Nemo Feels Lonely
## -- Ursina Engine--

This is a simple 3D exploration project created to learn and try out the Ursina game engine.
The "game" itself is a basic "swimming simulator" with no complex objectives. It features a player-controlled fish (Nemo) that can swim freely in a 3D environment populated with coral, marine life, and other scenery.

### 3D Asset Credits
All 3D models and assets used in this project were acquired for free from **Sketchfab**.

---

## Key Features

* **3D Player Control**: Swim freely as Nemo in a 3D space (forward, backward, left, right, up, and down).
* **Third-Person Camera**: The camera follows the player smoothly from a fixed third-person perspective.
* **Animated Models**: The player (Nemo) has a "swim" animation, and the environment includes an animated Kraken.
* **Procedural World**: The seabed is randomly populated with coral, starfish, and reefs each time the game starts.
* **Static Scenery**: Includes various 3D models like hills, clams, and different coral types to build the world.

---

## Technologies Used

* **Language**: Python 3
* **Game Engine**: Ursina (which is built on Panda3D)
* **Animation**: The `Actor` class from Panda3D is used for character animations.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

* **Python**: (Recommended: 3.6 or newer) - Download from [python.org](https://www.python.org/)
* **pip**: The Python Package Installer (usually comes bundled with Python)

---

## Installation and Setup

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/sslythrrr/nemofeellonely.git](https://github.com/sslythrrr/nemofeellonely.git)
    cd nemofeellonely
    ```

2.  **Install dependencies**:
    This project primarily requires the `ursina` library. You can install it using pip.
    ```bash
    pip install ursina
    ```

3.  **Run the application**:
    Once the library is installed, you can run the game directly.
    ```bash
    python main.py
    ```

---

## How to Play (Controls)

* **Swim Forward**: `W`
* **Swim Backward**: `S`
* **Swim Left**: `A`
* **Swim Right**: `D`
* **Swim Up**: `Up Arrow`
* **Swim Down**: `Down Arrow`
* *Diagonal movement is also supported by combining keys (e.g., `W` + `A`).*

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1.  **Fork** the repository on GitHub.
2.  **Clone** your forked repository to your local machine.
3.  Create a new **branch** for your feature or bug fix (`git checkout -b feature/your-feature-name`).
4.  Make your changes and **commit** them (`git commit -m 'Add some feature'`).
5.  **Push** your changes to your fork on GitHub (`git push origin feature/your-feature-name`).
6.  Open a **Pull Request** from your fork to the original repository.

---

## License

This project is licensed under the **MIT License**.
