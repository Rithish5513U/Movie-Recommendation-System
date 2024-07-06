# Movie Recommendation System

This project implements a movie recommendation system using Streamlit and cloud storage for data persistence. The system is content-based, using cosine similarity on movie tags to recommend similar movies.

## Features

- **Content-Based Recommendation**: Recommends movies based on similarity in movie tags.
- **Dynamic Poster Display**: Displays movie posters for recommended movies.
- **Data Persistence**: Utilizes cloud storage (Google Drive and Dropbox) for storing large data files.
- **Streamlit Interface**: Provides an interactive interface for users to select a movie and view recommendations.

## Setup

1. **Installation**
   - Clone the repository:
     ```
     git clone https://github.com/Rithish5513U/Movie-Recommendation-System.git
     cd <repository_name>
     ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```

2. **Running the Application**
   - Start the Streamlit application:
     ```
     streamlit run app.py
     ```
   - Open your browser and go to `http://localhost:8501` to view the application.

3. **Usage**
   - Select a movie from the dropdown menu.
   - Click on the "Show Recommendation" button to display recommended movies and their posters.

## Data Handling

- **Movies Data**: Initially downloaded from Google Drive and stored locally as `movie_list.pkl`.
- **Similarity Data**: Downloaded from Dropbox and stored locally as `similarity.pkl`.

### Handling Data Download

- The system checks for local data files (`movie_list.pkl` and `similarity.pkl`).
- If not found locally, it downloads them from cloud storage.
- Handles errors and retries during download using requests and custom exception handling.

## Credits

- **Data Sources**: 
  - Movies data: [Google Drive](https://drive.google.com/uc?export=download&id=1uBgqLmgibehSLWi6vNJ7Ydm8bo-4ZLo9)
  - Similarity data: [Dropbox](https://www.dropbox.com/scl/fi/d55bf7gj87wka9mr16ln0/similarity.pkl?rlkey=alu41tgjd89xhc0n8iic15l6j&st=r5f883im&dl=1)
- **Libraries**:
  - Streamlit
  - Pandas
  - Requests
  - NLTK
  - Scikit-learn
  - Pickle

## Troubleshooting

- **Downloading Large Files**: If encountering issues with downloading large files from cloud storage platforms like Google Drive or Dropbox, ensure the file sharing settings allow public access.

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

## Contributing

Feel free to submit issues or pull requests for new features, bug fixes, or enhancements.

## Acknowledgements

- Special thanks to the [TMDb API](https://www.themoviedb.org/documentation/api) for providing the movie data.
- [Krish Naik](https://github.com/krishnaik06) for the original inspiration and datasets.

---

Enjoy using the Movie Recommendation System! If you have any questions or feedback, feel free to reach out.
