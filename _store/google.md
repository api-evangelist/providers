---
aid: google
url: https://raw.githubusercontent.com/api-search/cloud/main/_apis/google/apis.md
apis:
  - aid: google:google-cloud-api-gateway
    name: Google Cloud API Gateway
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    contact:
      - FN: Cloud Gateway Support
        url: https://cloud.google.com/api-gateway/docs/support
        email: ''
    humanURL: https://cloud.google.com/api-gateway/docs
    overlays:
      - url: >-
          overlays/https://api.apis.guru/v2/specs/googleapis.com/apigateway/v1alpha2/openapi.json-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://cloud.google.com/api-gateway/docs/reference/rest
        type: Documentation
      - url: >-
          https://api.apis.guru/v2/specs/googleapis.com/apigateway/v1alpha2/openapi.json
        type: OpenAPI
    description: >-
      API Gateway enables you to provide secure access to your backend services
      through a well-defined REST API that is consistent across all of your
      services, regardless of the service implementation. Clients consume your
      REST APIS to implement standalone apps for a mobile device or tablet,
      through apps running in a browser, or through any other type of app that
      can make a request to an HTTP endpoint. 
  - aid: google:books-api
    name: Books API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    contact:
      - FN: Google Help
        url: https://support.google.com/
        email: ''
    humanURL: https://developers.google.com/books
    overlays:
      - url: >-
          overlays/https://api.apis.guru/v2/specs/googleapis.com/books/v1/openapi.json-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.google.com/books/docs/v1/using
        type: Documentation
      - url: https://api.apis.guru/v2/specs/googleapis.com/books/v1/openapi.json
        type: OpenAPI
      - url: https://developers.google.com/books/docs/v1/getting_started
        type: Getting Started
    description: >-
      This document is intended for developers who want to write applications
      that can interact with the Google Books API. Google Books has a vision to
      digitize the world's books. You can use the Google Books API to search
      content, organize an authenticated user's personal library and modify it
      as well.
name: Google
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://cloud.google.com
    type: Google Cloud
  - url: https://developers.google.com/
    type: Developer Portal
  - url: https://googledevelopers.blogspot.com/
    type: Blog
  - url: >-
      https://console.cloud.google.com/apis/dashboard?project=api-project-111046942866
    type: Console
  - url: https://www.linkedin.com/showcase/googledevelopers/
    type: LinkedIn
  - url: https://developers.google.com/events
    type: Events
  - url: https://developers.google.com/community
    type: Community
created: 2023/11/8
modified: 2023/11/8
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: overlays/apis-io-search.yml
    type: API Evangelist Ratings
description: >-
  Google Cloud APIs are programmatic interfaces to Google Cloud Platform
  services. They are a key part of Google Cloud Platform, allowing you to easily
  add the power of everything from computing to networking to storage to
  machine-learning-based data analysis to your applications.
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
---