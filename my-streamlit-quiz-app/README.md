# My Streamlit Quiz App

This project is a simple web application built using Streamlit that presents a quiz to users. The quiz questions and options are sourced from a Markdown file (`quizz.md`), allowing for easy updates and modifications to the quiz content.

## Project Structure

```
my-streamlit-quiz-app
├── src
│   └── streamlit_app.py  # Contains the Streamlit application code
├── quizz.md              # Contains the quiz questions and options in Markdown format
├── requirements.txt       # Lists the dependencies required for the project
└── README.md              # Documentation for the project
```

## Requirements

To run this application, you need to have Python installed on your machine. The required libraries are listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-streamlit-quiz-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the Streamlit application, navigate to the `src` directory and run the following command:
```
streamlit run streamlit_app.py
```

This will launch the application in your default web browser.

## Usage

Once the application is running, you will see the quiz questions displayed. Select your responses to each question and submit your answers to see the results.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features.

## License

This project is open-source and available under the MIT License.