---
aid: requests
name: Requests
description: 'Requests is a simple and elegant HTTP library for Python, designed for human beings. Published under the Apache2 license by the Python Software Foundation (PSF), it is one of the most downloaded Python packages with approximately 300 million weekly downloads and over 4 million dependent repositories. Requests abstracts urllib3 to provide idiomatic HTTP method functions (get, post, put, patch, delete, head, options), persistent Sessions with connection pooling, automatic content decompression, TLS/SSL verification, Basic and Digest authentication, cookie persistence, streaming downloads, multipart file uploads, SOCKS proxy support, and configurable timeouts. Current stable version: 2.33.1 (March 2026). Supports Python 3.10+.'
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/apis.yml
tags:
  - Clients
  - HTTP Client
  - HTTP Library
  - Open Source
  - Python
  - Python Software Foundation
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: requests:requests
    name: Requests
    description: Requests is a simple and elegant HTTP library for Python, designed for human beings. It provides a clean, human-friendly API for all standard HTTP methods with automatic content handling, authentication, session management, and TLS verification.
    humanURL: https://requests.readthedocs.io
    tags:
      - Clients
      - HTTP Client
      - HTTP Library
      - Open Source
      - Python
    properties:
      - type: Documentation
        url: https://requests.readthedocs.io/en/latest/
      - type: APIReference
        url: https://requests.readthedocs.io/en/latest/api/
      - type: Getting Started
        url: https://requests.readthedocs.io/en/latest/user/quickstart/
      - type: AdvancedUsage
        url: https://requests.readthedocs.io/en/latest/user/advanced/
      - type: GitHub
        url: https://github.com/psf/requests
      - type: PyPI
        url: https://pypi.org/project/requests/
common:
  - type: Website
    url: https://requests.readthedocs.io
  - type: Documentation
    url: https://requests.readthedocs.io/en/latest/
  - type: GitHub Organization
    url: https://github.com/psf/requests
  - type: PyPI
    name: Requests on PyPI
    description: Python Package Index listing for the requests package.
    url: https://pypi.org/project/requests/
  - type: JSONSchema
    name: Requests Request Schema
    description: JSON Schema describing the parameters of a Requests HTTP request call.
    url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/json-schema/requests-request-schema.json
  - type: JSONSchema
    name: Requests Response Schema
    description: JSON Schema describing the attributes of a requests.Response object.
    url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/json-schema/requests-response-schema.json
  - type: JSONStructure
    name: Requests Response Structure
    description: Field-level structure documentation for the requests.Response object.
    url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/json-structure/requests-response-structure.json
  - type: JSONLDContext
    name: Requests JSON-LD Context
    description: JSON-LD context mapping Requests HTTP concepts to Hydra and schema.org.
    url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/json-ld/requests-context.jsonld
  - type: Example
    name: GET Request Example
    description: Example of a GET request to the GitHub API using requests.get().
    url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/examples/requests-get-example.json
  - type: Example
    name: POST Request Example
    description: Example of a POST request with JSON body using requests.post().
    url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/examples/requests-post-example.json
  - type: Vocabulary
    name: Requests Vocabulary
    description: Domain vocabulary for the Requests library programming model, features, and ecosystem.
    url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/vocabulary/requests-vocabulary.yml
  - type: Changelog
    name: Requests Changelog
    description: Release history and changelog for the Requests library.
    url: https://requests.readthedocs.io/en/latest/community/updates/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
