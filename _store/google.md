---
aid: google
url: https://raw.githubusercontent.com/api-search/cloud/main/_apis/google/apis.md
apis:
  - aid: google:google-cloud-api-gateway
    name: Google Cloud API Gateway
    tags:
      - API Gateway
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
    description: |-
      API Gateway enables you to provide secure access to your backend services
      through a well-defined REST API that is consistent across all of your
      services, regardless of the service implementation. Clients consume your
      REST APIS to implement standalone apps for a mobile device or tablet,
      through apps running in a browser, or through any other type of app that
      can make a request to an HTTP endpoint. 
  - aid: google:books-api
    name: Books API
    tags:
      - Books
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    contact:
      - FN: Google Help
        url: https://support.google.com/
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
    description: |-
      This document is intended for developers who want to write applications
      that can interact with the Google Books API. Google Books has a vision to
      digitize the world's books. You can use the Google Books API to search
      content, organize an authenticated user's personal library and modify it
      as well.
  - aid: google:google-drive-api
    name: Google Drive API
    tags:
      - Documents
      - Storage
    humanURL: https://workspace.google.com/products/drive/
    properties:
      - url: https://developers.google.com/workspace/drive/api/guides/about-sdk
        type: Documentation
    description: >-
      Google Drive is a cloud-based storage service that lets users store,
      access, and share files from any device with an internet connection.
  - aid: google:google-drive-activity-api
    name: Introduction to Google Drive Activity API
    tags:
      - Documents
      - Activity
    humanURL: https://workspace.google.com/products/drive/
    properties:
      - url: https://developers.google.com/workspace/drive/activity/v2
        type: Documentation
    description: >-
      The Google Drive Activity API consists of the DriveActivity resource,
      which represents changes made to objects within a user's Google Drive, and
      the activity.query method, which allows you to retrieve information about
      those changes.
  - aid: google:google-drive-labels-api
    name: Drive Labels API
    tags:
      - Documents
      - Labels
    humanURL: https://workspace.google.com/products/drive/
    properties:
      - url: https://developers.google.com/workspace/drive
        type: Documentation
    description: >-
      Labels are metadata that you define to help users organize, find, and
      apply policy to files in Google Drive. The Drive Labels API is a RESTful
      API that supports business processes by attaching metadata to your Drive
      files.  
name: Google
tags:
  - Search
  - Advertising
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
modified: '2025-07-18'
description: |-

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