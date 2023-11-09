# [Postalized](https://github.com/ErcinDedeoglu/Postalized)

Postalized is an open source project that provides a simple and efficient way to parse and expand addresses using the power of `libpostal`. This project wraps `libpostal` functionalities in a Flask-based web API, making it easy to integrate address parsing and expansion into web applications.

## Features

- **Address Parsing**: Break down addresses into components with high accuracy.
- **Address Expansion**: Generate normalized variations of a given address.
- Dockerized application for easy deployment and scaling.

## Quick Start

### Prerequisites

- Docker

## Installation

Postalized is available as a Docker image on Docker Hub. You can easily pull and run the Postalized service without manually building it.

### Pulling the Docker Image

You can pull the latest version of Postalized from Docker Hub using the following command:

```bash
docker pull dublok/postalized:latest
```

This command retrieves the latest image of Postalized, ensuring you have the most up-to-date version.

### Running the Docker Image

After pulling the image, you can run it using:

```bash
docker run -p 8080:8080 dublok/postalized
```

This will start a container running Postalized and bind port 8080 on your host machine to port 8080 in the Docker container, making the API accessible via `http://localhost:8080`.


Alternatively, you can build the Docker image manually:

```bash
git clone https://github.com/ErcinDedeoglu/Postalized.git
cd Postalized
docker build -t postalized .
```

### Running the Application

To start the application, run:

```bash
docker run -p 8080:8080 postalized
```

The API should now be available at `http://localhost:8080`.

## Usage

Postalized exposes two endpoints: `/parse` for parsing addresses and `/expand` for expanding addresses.

### Parsing an Address

Send a POST request with a JSON body containing the address:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"address":"123 Main St"}' http://localhost:8080/parse
```

Example response:

```json
[
    {
        "label": "house_number",
        "value": "123"
    },
    {
        "label": "road",
        "value": "Main St"
    }
]
```

### Expanding an Address

Send a POST request with a JSON body containing the address:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"address":"123 Main Street"}' http://localhost:8080/expand
```

Example response:

```json
[
    "123 main street",
    "123 main st"
]
```

These examples demonstrate successful responses from the API. The parsing endpoint breaks down the input address into its components, and the expansion endpoint provides normalized variations of the input address.

---

## Development

For developing and contributing to Postalized, please follow the steps below:

1. Fork and clone the repository.
2. Make changes and test your code.
3. Submit a pull request with a clear list of what you've done.

## Support

If you are having issues, please let us know by creating an issue in the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
