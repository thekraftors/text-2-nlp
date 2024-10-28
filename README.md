
# Text-2-NLP

## Overview

Text-2-NLP is a Natural Language Processing (NLP) project that leverages the `transformers` library and pre-trained BERT models to handle advanced text processing tasks. This project demonstrates how to use tokenization, model loading, and tensor output using a BERT model.

## Installation

This project requires Python 3.10+ and the `transformers` library.

1. **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd text-2-nlp
    ```

2. **Install Dependencies:**

    Use `pip` to install the necessary packages:

    ```bash
    pip install transformers torch
    ```

3. **Optional**: Install the latest development version of `transformers` (if needed):

    ```bash
    pip install git+https://github.com/huggingface/transformers.git
    ```

## Using the Docker Images

The `text-2-nlp` project can also be run using Docker images for reproducibility. These images come in two flavors:

- **Alpine**: Smaller image size, best for lightweight environments.
- **Debian (slim)**: Useful for CI jobs or environments requiring additional tooling.

### Docker Image Tags:

The images are available on the GitLab registry:

- **Alpine (default)**:
  
    ```bash
    docker pull registry.gitlab.com/your-namespace/text-2-nlp:latest
    ```

- **Debian (slim-bullseye)**:
  
    ```bash
    docker pull registry.gitlab.com/your-namespace/text-2-nlp:slim-bullseye
    ```

### Running the Docker Container

To start the container:

```bash
docker run -it --rm registry.gitlab.com/your-namespace/text-2-nlp:latest python3 main.py
```

## Usage

After installing dependencies, run the main script to start processing text with the BERT model:

```bash
python3 main.py
```

### Example Output

Upon successful execution, you should see model outputs in tensor format. Warnings about `clean_up_tokenization_spaces` can be ignored or fixed as described in the Troubleshooting section.

## Troubleshooting

- **No module named 'transformers'**  
  Make sure `transformers` is installed with:
  
    ```bash
    pip install transformers
    ```

- **No module named 'torch'**  
  Install PyTorch:

    ```bash
    pip install torch
    ```

- **Unrecognized Keyword Argument**  
  If you see an unrecognized argument (`clean_up_tokenization_spaces`), edit `main.py` to remove or update this argument.

---

## License

This project is licensed under the MIT License.
