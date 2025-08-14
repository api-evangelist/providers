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
    name: Google Drive Activity API
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
    name: Google Drive Labels API
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
  - aid: google:google-calendar-api
    name: Google Calendar API
    tags:
      - Calendar
    humanURL: https://developers.google.com/workspace/calendar/api/guides/overview
    properties:
      - url: https://developers.google.com/workspace/calendar/api/guides/overview
        type: Documentation
      - url: properties/google-calendar-api-openapi.yml
        type: OpenAPI
    description: >-
      The Google Calendar API is a RESTful API that can be accessed through
      explicit HTTP calls or using the Google Client Libraries. The API exposes
      most of the features available in the Google Calendar Web interface.
  - aid: google:google-gmail-api
    name: Google Gmail API
    tags:
      - Email
    humanURL: https://developers.google.com/workspace/gmail/api/guides
    properties:
      - url: https://developers.google.com/workspace/gmail/api/guides
        type: Documentation
      - url: properties/google-gmail-api-openapi.yml
        type: OpenAPI
    description: >-
      The Gmail API is a RESTful API that can be used to access Gmail mailboxes
      and send mail. For most web applications the Gmail API is the best choice
      for authorized access to a user's Gmail data and is suitable for various
      applications.
  - aid: google:google-sheets-api
    name: Google Sheets API
    tags:
      - Spreadsheets
    humanURL: https://developers.google.com/workspace/sheets/api/guides/concepts
    properties:
      - url: https://developers.google.com/workspace/sheets/api/guides/concepts
        type: Documentation
      - url: properties/google-sheets-api-openapi.yml
        type: OpenAPI
    description: >-
      The Google Sheets API is a RESTful interface that lets you read and modify
      a spreadsheet's data..
  - aid: google:google-docs-api
    name: Google Docs API
    tags:
      - Documents
    humanURL: https://developers.google.com/workspace/docs/api/reference/rest
    properties:
      - url: https://developers.google.com/workspace/docs/api/reference/rest
        type: Documentation
      - url: properties/google-docs-api-openapi.yml
        type: OpenAPI
    description: Reads and writes Google Docs documents.
  - aid: undefined:google-maps-api
    name: Google Maps API
    humanURL: https://developers.google.com/maps
    properties:
      - url: https://developers.google.com/maps
        type: Documentation
    description: >-
      Create real-world, real-time experiences with the latest Maps, Routes, and
      Places features from Google Maps Platform. Built by the Google team for
      developers everywhere.
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
  - url: https://developers.googleblog.com/en/
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
  - url: https://policies.google.com/privacy
    name: Privacy Policy  Privacy & Terms  Google
    type: PrivacyPolicy
    description: 'null'
  - url: https://developers.google.com/
    name: Google for Developers - from AI and Cloud to Mobile and Web
    type: Portal
    description: 'null'
  - url: https://discord.com/invite/google-dev-community
    name: Discord
    type: Discord
    description: 'null'
  - url: https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw
    name: Videos
    type: Videos
    description: 'null'
  - url: >-
      https://console.cloud.google.com/apis/dashboard?pli=1&inv=1&invt=Ab3RcQ&project=api-project-111046942866
    name: APIs & Services  APIs & Services  API Evangelist  Google Cloud console
    type: Explorer
    description: 'null'
  - url: https://developers.google.com/terms/site-terms
    name: "Google Developers Site Terms of Service \_|\_ Google for Developers"
    type: TermsOfService
    description: 'null'
created: 2023/11/8
modified: '2025-07-29'
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