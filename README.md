# Movie Recommendation System

This is a web-based movie recommendation system built using Streamlit. The application recommends movies based on the selected movie by the overview of the movie and content-based and displays the posters of the recommended movies.

## Features

- **Movie Recommendation**: Get movie recommendations based on a selected movie.
- **Poster Display**: Display posters of the recommended movies.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Rithish5513U/Movie-Recommendation-System.git
    cd Movie-Recommendation-System
    ```

2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the utils.py**:

    ```bash
    python -m src/utils.py
    ```
It will create a new folder Artifacts in which the models are exported as .pkl files which contains movie list with tags and similarity matrix of the movies.

4. **Run the Application**:

    ```bash
    python -m src/app.py
    ```
Ensure running utils.py and removing last two lines from it and run src/app.py to ensure smooth running of the app. The app will recommend movies based on the genres, overview of the movie and much more

## Usage

1. **Load the Application**:
    - Open your web browser and go to `http://localhost:8501` (or the URL provided by Streamlit).

2. **Select a Movie**:
    - Use the dropdown menu to select a movie.

3. **Show Recommendations**:
    - Click the 'Show Recommendation' button to get movie recommendations.
    - The recommended movie posters will be displayed.

## Project Structure

- `src/`
  - `app.py`: Main application file.
  - `components/`: Contains the components of the application.
    - `data_ingestion.py`: Importing the data for the movies
    - `data_transformation.py`: Preprocess the data
    - `model_trainer.py`: Train the model using sklearn
  - `utils.py`: Utility functions.
  - `exception.py`: Custom exception handling.
  - `logger.py`: Logging configuration.
- `Artifacts/`
  - `movie_list.pkl`: Pickle file containing the list of movies.
  - `similarity.pkl`: Pickle file containing the similarity matrix.
- `requirements.txt`: List of required packages.
- `setup.py`: Used to initiate the setup for the project.

## Dependencies

- Streamlit
- Pandas
- Requests
- NLTK
- Scikit-learn
- Pickle

## Contributing

Feel free to submit issues or pull requests for new features, bug fixes, or enhancements.

## Acknowledgements

- Special thanks to the [TMDb API](https://www.themoviedb.org/documentation/api) for providing the movie data.
- [Krish Naik](https://github.com/krishnaik06) for the original inspiration and datasets.

---

Enjoy using the Movie Recommendation System! If you have any questions or feedback, feel free to reach out.
