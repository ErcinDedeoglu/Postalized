# Postalized

Postalized is an open-source project that provides a RESTful API for the powerful [libpostal](https://github.com/openvenues/libpostal) library, a C library for parsing/normalizing street addresses around the world. This project allows you to make HTTP requests to parse and expand street addresses.

The libpostal library is needed to be built and installed in the docker container, which is automatically done in the Dockerfile included in this repository.

## Getting Started

These instructions will help you to run Postalized locally for development and testing purposes.

### Prerequisites

* Docker
* Docker Compose
* Git

### Installation

1. Clone the repository:
`git clone https://github.com/ErcinDedeoglu/Postalized.git`

2. Build the Docker image:
`docker build -t postalized .`

3. Start the service:
`docker run -d -p 8080:8080 postalized`

The Postalized API should now be running at "http://localhost:8080".

API Endpoints
-------------
### Parse
**Description:** Parses a given address string into components.
**Endpoint:** /parse
**Method:** POST
**Request Body:**
```
{
    "address": "The address string to parse"
}
```

**Success Response:** JSON array of parsed components

**CURL Command:**
`curl -X POST -H "Content-Type: application/json" -d '{"address": "123 Main St"}' http://localhost:8080/parse`

**Sample Response:**
```
[
    {
        "label": "house_number",
        "value": "123"
    },
    {
        "label": "road",
        "value": "main st"
    }
]
```

### Expand
**Description:** Expands a given address string into a list of possible expansions.
**Endpoint:** /expand
**Method:** POST
**Request Body:**
```
{
    "address": "The address string to expand"
}
```

**Success Response:** JSON array of possible expansions

**CURL Command:**
`curl -X POST -H "Content-Type: application/json" -d '{"address": "The address string to expand"}' http://localhost:8080/expand`

**Sample Response:**
```
[
    "the address string to expand",
    "the address string to expand",
    "the address string to expand"
]
```
