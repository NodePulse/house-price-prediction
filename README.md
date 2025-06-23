# House Price Prediction App

A simple web application for predicting house prices using a trained Linear Regression model, built with Flask and deployed on Render. This project demonstrates a basic machine learning model deployment, allowing users to get house price predictions via a web form or an API endpoint.

---

## 🔗 Live Demo (Coming Soon!)

Once your application is deployed on Render, you can replace this placeholder with a direct link to your live app.

<p>
  <a href="https://house-price-prediction-sx3z.onrender.com/" target="_blank">
    <img src="https://img.shields.io/badge/🚀%20Live%20App-House%20Price%20Predictor-blueviolet?style=for-the-badge&logo=render&logoColor=white" alt="Live App Badge" />
  </a>
</p>

---

## 🖼️ UI Preview (Example - You can add a screenshot later)

*(Once your `index.html` is ready and the app is running, you can take a screenshot of your web form and place it here. For now, this is a placeholder.)*

![UI Preview Placeholder](./public/ui-preview-placeholder.png)

---

## 🚀 Features

-   **Web Interface**: A user-friendly form to input house features and receive price predictions.
-   **Prediction API**: A RESTful API endpoint for programmatic access to the prediction model via JSON input.
-   **Pre-trained Model**: Utilizes a pre-trained Scikit-learn Linear Regression model for predictions.
-   **Data Scaling**: Incorporates a pre-fitted `StandardScaler` to correctly transform input features before prediction, ensuring accuracy.
-   **Easy Deployment**: Configured for straightforward deployment on cloud platforms like Render.

---

## 🛠️ Tech Stack

-   **Backend/Web Framework**: Flask
-   **Machine Learning**: Scikit-learn (for Linear Regression and StandardScaler)
-   **Data Handling**: Pandas, NumPy
-   **Deployment**: Gunicorn (WSGI server), Render (Cloud Platform)
-   **Visualization (Local Development/Notebook)**: Matplotlib, Seaborn (used during model training and EDA, not directly in the deployed app)

---

## 📦 Installation (Local Development)

To run this project locally, follow these steps:

1.  **Clone the repository**:

    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    *(Remember to replace `your-username/your-repo-name.git` with your actual repository URL)*

2.  **Create and activate a virtual environment** (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Ensure Model and Scaler Files Exist**:
    Make sure `lr_model.pkl` (your trained Linear Regression model) and `scaler.pkl` (your fitted StandardScaler) are present in the root directory of your project. These files are generated during the model training phase (e.g., in your Jupyter notebook).

5.  **Run the Flask Development Server**:

    ```bash
    python app.py
    ```
    The application will typically run on `http://127.0.0.1:5000/`.

---

## 📤 Deployment

This project is optimized for deployment on **Render**.

1.  **Prepare Files**: Ensure all necessary files (`app.py`, `requirements.txt`, `lr_model.pkl`, `scaler.pkl`, and the `templates/` directory containing `index.html`) are committed and pushed to your Git repository.
2.  **Create a New Web Service on Render**:
    * Go to your Render dashboard and create a "New Web Service".
    * Connect your Git repository.
    * **Runtime**: Python 3
    * **Build Command**: `pip install -r requirements.txt` (Render usually infers this)
    * **Start Command**: `gunicorn --workers 4 --threads 2 --bind 0.0.0.0:$PORT app:app` (You can adjust workers and threads based on your Render plan).
    * Select your desired plan type and deploy.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1.  Fork the repository
2.  Create a new branch (`git checkout -b feature/your-feature`)
3.  Commit your changes (`git commit -m 'Add new feature'`)
4.  Push to the branch (`git push origin feature/your-feature`)
5.  Open a Pull Request

---

## 🙌 Acknowledgements

-   [Flask](https://flask.palletsprojects.com/): Python micro web framework.
-   [Scikit-learn](https://scikit-learn.org/): Machine learning library for Python.
-   [Render](https://render.com/): Cloud platform for deploying web services.
-   [Gunicorn](https://gunicorn.org/): Python WSGI HTTP Server for UNIX.
