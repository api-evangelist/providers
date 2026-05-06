---
aid: google
url: https://raw.githubusercontent.com/api-evangelist/google/refs/heads/main/apis.yml
parent: alphabet
type: Company
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
    properties:
      - url: https://cloud.google.com/api-gateway/docs/reference/rest
        type: Documentation
    description: API Gateway enables you to provide secure access to your backend services through a well-defined REST API that is consistent across all of your services, regardless of the service implementation. Clients consume your REST APIS to implement standalone apps for a mobile device or tablet, through apps running in a browser, or through any other type of app that can make a request to an HTTP endpoint.
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
    properties:
      - url: https://developers.google.com/books/docs/v1/using
        type: Documentation
      - url: https://developers.google.com/books/docs/v1/getting_started
        type: Getting Started
      - url: openapi/books-api-openapi.yml
        type: OpenAPI
    description: This document is intended for developers who want to write applications that can interact with the Google Books API. Google Books has a vision to digitize the world's books. You can use the Google Books API to search content, organize an authenticated user's personal library and modify it as well.
  - aid: google:google-drive-api
    name: Google Drive API
    tags:
      - Documents
      - Storage
    humanURL: https://workspace.google.com/products/drive/
    properties:
      - url: https://developers.google.com/workspace/drive/api/guides/about-sdk
        type: Documentation
      - url: https://developers.google.com/workspace/drive/api/reference/rest/v3
        type: APIReference
      - url: openapi/google-drive-api-openapi.yml
        type: OpenAPI
    description: Google Drive is a cloud-based storage service that lets users store, access, and share files from any device with an internet connection.
  - aid: google:google-drive-activity-api
    name: Google Drive Activity API
    tags:
      - Activity
      - Documents
    humanURL: https://workspace.google.com/products/drive/
    properties:
      - url: https://developers.google.com/workspace/drive/activity/v2
        type: Documentation
      - url: openapi/google-drive-activity-api-openapi.yml
        type: OpenAPI
    description: The Google Drive Activity API consists of the DriveActivity resource, which represents changes made to objects within a user's Google Drive, and the activity.query method, which allows you to retrieve information about those changes.
  - aid: google:google-drive-labels-api
    name: Google Drive Labels API
    tags:
      - Documents
      - Labels
    humanURL: https://workspace.google.com/products/drive/
    properties:
      - url: https://developers.google.com/workspace/drive
        type: Documentation
      - url: openapi/google-drive-labels-api-openapi.yml
        type: OpenAPI
    description: Labels are metadata that you define to help users organize, find, and apply policy to files in Google Drive. The Drive Labels API is a RESTful API that supports business processes by attaching metadata to your Drive files.
  - aid: google:google-calendar-api
    name: Google Calendar API
    tags:
      - Calendar
    humanURL: https://developers.google.com/workspace/calendar/api/guides/overview
    properties:
      - url: https://developers.google.com/workspace/calendar/api/guides/overview
        type: Documentation
      - url: openapi/google-calendar-api-openapi.yml
        type: OpenAPI
    description: The Google Calendar API is a RESTful API that can be accessed through explicit HTTP calls or using the Google Client Libraries. The API exposes most of the features available in the Google Calendar Web interface.
  - aid: google:google-gmail-api
    name: Google Gmail API
    tags:
      - Email
    humanURL: https://developers.google.com/workspace/gmail/api/guides
    properties:
      - url: https://developers.google.com/workspace/gmail/api/guides
        type: Documentation
      - url: openapi/google-gmail-api-openapi.yml
        type: OpenAPI
    description: The Gmail API is a RESTful API that can be used to access Gmail mailboxes and send mail. For most web applications the Gmail API is the best choice for authorized access to a user's Gmail data and is suitable for various applications.
  - aid: google:google-sheets-api
    name: Google Sheets API
    tags:
      - Spreadsheets
    humanURL: https://developers.google.com/workspace/sheets/api/guides/concepts
    properties:
      - url: https://developers.google.com/workspace/sheets/api/guides/concepts
        type: Documentation
      - url: openapi/google-sheets-api-openapi.yml
        type: OpenAPI
    description: The Google Sheets API is a RESTful interface that lets you read and modify a spreadsheet's data..
  - aid: google:google-docs-api
    name: Google Docs API
    tags:
      - Documents
    humanURL: https://developers.google.com/workspace/docs/api/reference/rest
    properties:
      - url: https://developers.google.com/workspace/docs/api/reference/rest
        type: Documentation
      - url: openapi/google-docs-api-openapi.yml
        type: OpenAPI
    description: Reads and writes Google Docs documents.
  - aid: google:google-maps-api
    name: Google Maps API
    tags:
      - Geolocation
      - Maps
    humanURL: https://developers.google.com/maps
    properties:
      - url: https://developers.google.com/maps
        type: Documentation
    description: Create real-world, real-time experiences with the latest Maps, Routes, and Places features from Google Maps Platform. Built by the Google team for developers everywhere.
  - aid: google:google-places-api
    name: Google Places API
    tags:
      - Places
    humanURL: https://developers.google.com/maps/documentation/places/web-service
    properties:
      - url: https://developers.google.com/maps/documentation/places/web-service
        type: Documentation
      - url: openapi/google-places-api-openapi.yml
        type: OpenAPI
    description: The Google Places API provides programmatic access to detailed information about millions of places, including names, addresses, reviews, photos, and geographic coordinates, enabling location-based search and discovery in applications.
  - aid: google:google-aggregate-places-api
    name: Google Aggregate Places API
    tags:
      - Maps
      - Places
    humanURL: https://developers.google.com/maps/documentation/places-aggregate
    properties:
      - url: https://developers.google.com/maps/documentation/places-aggregate
        type: Documentation
    description: The Google Places Aggregate API delivers aggregated insightssuch as the count or list of Place IDsfor places within a defined area, based on filters like type (e.g., restaurants), price level, user ratings, or operational status.
  - aid: google:google-places-insights-api
    name: Google Places Insights API
    tags:
      - Analytics
      - Maps
      - Places
    humanURL: https://developers.google.com/maps/documentation/placesinsights
    properties:
      - url: https://developers.google.com/maps/documentation/placesinsights
        type: Documentation
    description: The Google Places Insights API (now generally known as the Places Aggregate API) provides aggregated intelligencesuch as counts of matching places or lists of Place IDswithin a defined geographic area, filtered by attributes like place type, ratings, price, or operating status, to help analyze local density and distribution.
  - aid: google:google-street-view-imagery-api
    name: Google Street View Imagery API
    tags:
      - Images
      - Maps
      - Street View
    humanURL: https://developers.google.com/maps/documentation/streetview
    properties:
      - url: https://developers.google.com/maps/documentation/streetview
        type: Documentation
    description: The Google Street View Imagery API lets developers embed and display interactive 360-degree panoramic images from Google Street View in their applications, enabling users to virtually explore real-world locations.
  - aid: google:google-elevation-api
    name: Google Elevation API
    tags:
      - Elevation
      - Maps
    humanURL: https://developers.google.com/maps/documentation/elevation
    properties:
      - url: https://developers.google.com/maps/documentation/elevation
        type: Documentation
    description: The Google Elevation API provides elevation data for specific locations on the Earth's surface, including height above sea level for points, paths, or sets of coordinates.
  - aid: google:google-routes-api
    name: Google Routes API
    tags:
      - Directions
      - Maps
      - Routes
    humanURL: https://developers.google.com/maps/documentation/routes
    properties:
      - url: https://developers.google.com/maps/documentation/routes
        type: Documentation
    description: The Google Routes API calculates routes between locations, providing directions, distances, travel times, and additional data like traffic conditions, tolls, and alternative paths for various modes of transportation.
  - aid: google:google-geocoding-api
    name: Google Geocoding API
    tags:
      - Geocoding
      - Maps
    humanURL: https://developers.google.com/maps/documentation/geocoding
    properties:
      - url: https://developers.google.com/maps/documentation/geocoding
        type: Documentation
    description: The Google Geocoding API converts addresses into geographic coordinates (latitude and longitude) and vice versa, enabling applications to map locations and perform location-based queries.
  - aid: google:google-geolocation-api
    name: Google Geolocation API
    tags:
      - Geolocation
      - Maps
    humanURL: https://developers.google.com/maps/documentation/geolocation
    properties:
      - url: https://developers.google.com/maps/documentation/geolocation
        type: Documentation
    description: The Google Geolocation API determines a devices approximate location based on nearby cell towers, Wi-Fi nodes, or Bluetooth beacons, without requiring GPS.
  - aid: google:google-address-validation-api
    name: Google Address Validation API
    tags:
      - Address
      - Maps
      - Validation
    humanURL: https://developers.google.com/maps/documentation/address-validation
    properties:
      - url: https://developers.google.com/maps/documentation/address-validation
        type: Documentation
    description: The Google Address Validation API standardizes, validates, and enriches postal addresses by checking them against authoritative data sources, ensuring accuracy and deliverability for shipping, billing, and location-based services.
  - aid: google:google-time-zone-api
    name: Google Time Zone API
    tags:
      - Maps
      - Time Zone
    humanURL: https://developers.google.com/maps/documentation/timezone
    properties:
      - url: https://developers.google.com/maps/documentation/timezone
        type: Documentation
    description: The Google Time Zone API provides time zone information for a given location, including the standard time offset from UTC and daylight saving time details.
  - aid: google:google-air-quality-api
    name: Google Air Quality API
    tags:
      - Air Quality
      - Environment
      - Maps
    humanURL: https://developers.google.com/maps/documentation/air-quality
    properties:
      - url: https://developers.google.com/maps/documentation/air-quality
        type: Documentation
    description: The Google Air Quality API allows applications to access real-time, historical, and forecasted air quality dataencompassing over 70 indices, pollutant details, health recommendations, and heatmap tiles for visualizing atmospheric conditions at a high (500//500/m) resolution across more than 100 countries.
  - aid: google:google-pollen-api
    name: Google Pollen API
    tags:
      - Environment
      - Maps
      - Pollen
    humanURL: https://developers.google.com/maps/documentation/pollen
    properties:
      - url: https://developers.google.com/maps/documentation/pollen
        type: Documentation
    description: The Google Pollen API provides localized pollen informationincluding daily forecasts, pollen levels by plant type (trees, weeds, grasses), and related health recommendationshelping applications inform users about allergy risks in their area.
  - aid: google:google-solar-api
    name: Google Solar API
    tags:
      - Energy
      - Maps
      - Solar
    humanURL: https://developers.google.com/maps/documentation/solar
    properties:
      - url: https://developers.google.com/maps/documentation/weather
        type: Documentation
    description: The Google Solar API delivers solar potential data for buildings, including rooftop geometry, shading, sunlight exposure, and energy production estimates, to support solar panel planning and deployment.
  - aid: google:google-weather-api
    name: Google Weather API
    tags:
      - Environment
      - Maps
      - Weather
    humanURL: https://developers.google.com/maps/documentation/weather
    properties:
      - url: https://developers.google.com/maps/documentation/weather
        type: Documentation
    description: The Google Weather API delivers hyperlocal, real-time weather dataincluding current conditions, hourly and 10day forecasts, and the past 24 hours of historyfor any location worldwide, with information refreshed every 1530 minutes.
  - aid: google:google-gemini-api
    name: Google Gemini API
    tags:
      - AI
      - Documents
      - Machine Learning
    humanURL: https://ai.google.dev/
    properties:
      - url: https://ai.google.dev/
        type: Documentation
      - url: https://ai.google.dev/gemini-api/docs
        type: GettingStarted
      - url: openapi/google-gemini-api-openapi.yml
        type: OpenAPI
  - aid: google:youtube-data-api
    name: YouTube Data API
    tags:
      - Media
      - Video
    humanURL: https://developers.google.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
    description: The YouTube Data API lets you incorporate functions normally executed on the YouTube website into your own website or application, including searching for videos, retrieving standard feeds, and managing playlists and subscriptions.
  - aid: google:google-analytics-data-api
    name: Google Analytics Data API
    tags:
      - Analytics
      - Reporting
    humanURL: https://developers.google.com/analytics/devguides/reporting/data/v1
    properties:
      - url: https://developers.google.com/analytics/devguides/reporting/data/v1
        type: Documentation
      - url: https://developers.google.com/analytics/devguides/reporting/data/v1/rest
        type: APIReference
    description: The Google Analytics Data API provides programmatic methods to access report data in Google Analytics, enabling custom dashboards, automated reporting workflows, and integration with other business applications.
  - aid: google:google-ads-api
    name: Google Ads API
    tags:
      - Advertising
    humanURL: https://developers.google.com/google-ads/api
    properties:
      - url: https://developers.google.com/google-ads/api/docs/get-started/introduction
        type: Documentation
      - url: https://developers.google.com/google-ads/api/docs/get-started/make-first-call
        type: GettingStarted
    description: The Google Ads API is the programmatic interface to Google Ads and is used for managing large or complex Google Ads accounts and campaigns efficiently.
  - aid: google:google-custom-search-json-api
    name: Google Custom Search JSON API
    tags:
      - Search
    humanURL: https://developers.google.com/custom-search/v1/overview
    properties:
      - url: https://developers.google.com/custom-search/v1/overview
        type: Documentation
      - url: https://developers.google.com/custom-search/v1/reference/rest
        type: APIReference
    description: The Custom Search JSON API lets you develop websites and applications to retrieve and display search results from Programmable Search Engine programmatically using RESTful requests to get web search or image search results in JSON format.
  - aid: google:google-cloud-translation-api
    name: Google Cloud Translation API
    tags:
      - AI
      - Machine Learning
      - Translation
    humanURL: https://cloud.google.com/translate
    properties:
      - url: https://cloud.google.com/translate/docs
        type: Documentation
      - url: https://cloud.google.com/translate/docs/reference/rest
        type: APIReference
    description: The Cloud Translation API uses Google neural machine translation technology to let you dynamically translate text through the API using a Google pre-trained or custom model, supporting over 100 language pairs.
  - aid: google:google-cloud-vision-api
    name: Google Cloud Vision API
    tags:
      - AI
      - Machine Learning
      - Vision
    humanURL: https://cloud.google.com/vision
    properties:
      - url: https://cloud.google.com/vision/docs
        type: Documentation
    description: The Cloud Vision API allows developers to integrate vision detection features within applications, including image labeling, face and landmark detection, optical character recognition (OCR), and tagging of explicit content.
  - aid: google:google-cloud-natural-language-api
    name: Google Cloud Natural Language API
    tags:
      - AI
      - Machine Learning
      - Natural Language Processing
    humanURL: https://cloud.google.com/natural-language
    properties:
      - url: https://cloud.google.com/natural-language/docs
        type: Documentation
    description: The Cloud Natural Language API provides natural language understanding technologies including sentiment analysis, entity analysis, entity sentiment analysis, content classification, and syntax analysis.
  - aid: google:google-cloud-speech-to-text-api
    name: Google Cloud Speech-to-Text API
    tags:
      - AI
      - Machine Learning
      - Speech
    humanURL: https://cloud.google.com/speech-to-text
    properties:
      - url: https://cloud.google.com/speech-to-text/docs
        type: Documentation
    description: The Cloud Speech-to-Text API enables developers to convert audio to text using powerful neural network models, supporting over 125 languages and variants with automatic speech recognition.
  - aid: google:google-cloud-text-to-speech-api
    name: Google Cloud Text-to-Speech API
    tags:
      - AI
      - Machine Learning
      - Speech
    humanURL: https://cloud.google.com/text-to-speech
    properties:
      - url: https://cloud.google.com/text-to-speech/docs
        type: Documentation
    description: The Cloud Text-to-Speech API converts text into natural-sounding speech using an API powered by Google AI technologies, with support for multiple languages, voices, and audio formats.
  - aid: google:google-cloud-bigquery-api
    name: Google Cloud BigQuery API
    tags:
      - Analytics
      - Big Data
      - Database
    humanURL: https://cloud.google.com/bigquery
    properties:
      - url: https://cloud.google.com/bigquery/docs
        type: Documentation
      - url: https://cloud.google.com/bigquery/docs/reference/rest
        type: APIReference
    description: BigQuery is a fully managed, petabyte-scale analytics data warehouse that lets you run analytics over vast amounts of data in near real time using SQL queries.
  - aid: google:google-fonts-api
    name: Google Fonts API
    tags:
      - Design
      - Fonts
    humanURL: https://developers.google.com/fonts
    properties:
      - url: https://developers.google.com/fonts/docs/developer_api
        type: Documentation
      - url: https://developers.google.com/fonts/docs/getting_started
        type: GettingStarted
    description: The Google Fonts Developer API provides programmatic access to the metadata for all font families served by Google Fonts, allowing applications to query for available font families, styles, and subsets.
  - aid: google:google-people-api
    name: Google People API
    tags:
      - Contacts
      - People
    humanURL: https://developers.google.com/people
    properties:
      - url: https://developers.google.com/people
        type: Documentation
      - url: https://developers.google.com/people/api/rest
        type: APIReference
    description: The Google People API provides access to information about profiles and contacts, allowing applications to read and manage the authenticated user's contacts and profile data.
  - aid: google:google-blogger-api
    name: Google Blogger API
    tags:
      - Blogging
    humanURL: https://developers.google.com/blogger
    properties:
      - url: https://developers.google.com/blogger/docs/3.0/getting_started
        type: Documentation
      - url: https://developers.google.com/blogger/docs/3.0/reference/
        type: APIReference
    description: The Blogger API enables client applications to view and update Blogger content, providing programmatic access to blog posts, comments, pages, and user information.
  - aid: google:google-slides-api
    name: Google Slides API
    tags:
      - Presentations
    humanURL: https://developers.google.com/workspace/slides/api/guides/overview
    properties:
      - url: https://developers.google.com/workspace/slides/api/guides/overview
        type: Documentation
      - url: https://developers.google.com/workspace/slides/api/reference/rest
        type: APIReference
    description: The Google Slides API lets you create and modify Google Slides presentations, enabling applications to build slide decks automatically from user and system-provided data.
  - aid: google:google-tasks-api
    name: Google Tasks API
    tags:
      - Productivity
      - Tasks
    humanURL: https://developers.google.com/workspace/tasks/overview
    properties:
      - url: https://developers.google.com/workspace/tasks/overview
        type: Documentation
      - url: https://developers.google.com/workspace/tasks/reference/rest
        type: APIReference
    description: The Google Tasks API lets you search, read, and update Google Tasks content and metadata using a RESTful interface, enabling programmatic management of task lists and individual tasks.
  - aid: google:google-chat-api
    name: Google Chat API
    tags:
      - Chat
      - Messaging
    humanURL: https://developers.google.com/workspace/chat/overview
    properties:
      - url: https://developers.google.com/workspace/chat/overview
        type: Documentation
      - url: https://developers.google.com/workspace/chat/api/reference/rest
        type: APIReference
    description: The Google Chat API enables developers to build Chat apps that bring services and resources into Google Chat, letting users get information and take action without leaving the conversation.
  - aid: google:google-classroom-api
    name: Google Classroom API
    tags:
      - Classroom
      - Education
    humanURL: https://developers.google.com/classroom
    properties:
      - url: https://developers.google.com/workspace/classroom/guides/get-started
        type: Documentation
      - url: https://developers.google.com/workspace/classroom/reference/rest
        type: APIReference
    description: The Google Classroom API lets you manage courses, rosters, assignments, and grades programmatically, enabling integration with learning management systems and educational tools.
  - aid: google:google-forms-api
    name: Google Forms API
    tags:
      - Forms
      - Surveys
    humanURL: https://developers.google.com/forms
    properties:
      - url: https://developers.google.com/workspace/forms/api/guides
        type: Documentation
      - url: https://developers.google.com/workspace/forms/api/reference/rest
        type: APIReference
    description: The Google Forms API is a RESTful interface that lets you create and modify forms and quizzes, retrieve form responses and quiz grades, set up answer keys with automatic feedback, and receive push notifications.
  - aid: google:google-meet-rest-api
    name: Google Meet REST API
    tags:
      - Meetings
      - Video Conferencing
    humanURL: https://developers.google.com/workspace/meet/api/guides/overview
    properties:
      - url: https://developers.google.com/workspace/meet/api/guides/overview
        type: Documentation
      - url: https://developers.google.com/workspace/meet/api/reference/rest/v2
        type: APIReference
    description: The Google Meet REST API lets you create and manage meetings for Google Meet, retrieve meeting and participant information, and access meeting artifacts like recordings and transcripts.
  - aid: google:google-knowledge-graph-search-api
    name: Google Knowledge Graph Search API
    tags:
      - Knowledge Graph
      - Search
    humanURL: https://developers.google.com/knowledge-graph
    properties:
      - url: https://developers.google.com/knowledge-graph
        type: Documentation
    description: The Knowledge Graph Search API lets you find entities in the Google Knowledge Graph, providing access to information about people, places, and things that Google knows about.
  - aid: google:google-pagespeed-insights-api
    name: Google PageSpeed Insights API
    tags:
      - Performance
      - Web
    humanURL: https://developers.google.com/speed/docs/insights/v5/get-started
    properties:
      - url: https://developers.google.com/speed/docs/insights/v5/get-started
        type: Documentation
      - url: https://developers.google.com/speed/docs/insights/rest
        type: APIReference
    description: The PageSpeed Insights API analyzes the performance of web pages and provides suggestions for improving page speed, accessibility, and SEO.
  - aid: google:google-civic-information-api
    name: Google Civic Information API
    tags:
      - Civic
      - Government
    humanURL: https://developers.google.com/civic-information
    properties:
      - url: https://developers.google.com/civic-information
        type: Documentation
    description: The Google Civic Information API lets developers build applications that display civic information, including elected officials, polling places, and election data for US addresses.
  - aid: google:google-roads-api
    name: Google Roads API
    tags:
      - Maps
      - Roads
    humanURL: https://developers.google.com/maps/documentation/roads
    properties:
      - url: https://developers.google.com/maps/documentation/roads
        type: Documentation
    description: The Google Roads API provides snap-to-road functionality that maps GPS coordinates to road geometry, identifies nearest road segments, and returns speed limit data for road segments.
  - aid: google:google-map-tiles-api
    name: Google Map Tiles API
    tags:
      - Maps
      - Tiles
    humanURL: https://developers.google.com/maps/documentation/tile
    properties:
      - url: https://developers.google.com/maps/documentation/tile
        type: Documentation
    description: The Map Tiles API provides high-resolution Photorealistic 3D Tiles, 2D Tiles, and Street View Tiles for building immersive, customized map visualizations.
  - aid: google:google-route-optimization-api
    name: Google Route Optimization API
    tags:
      - Maps
      - Optimization
      - Routes
    humanURL: https://developers.google.com/maps/documentation/route-optimization
    properties:
      - url: https://developers.google.com/maps/documentation/route-optimization
        type: Documentation
    description: The Route Optimization API generates optimized route plans for single or multiple vehicles and their stops, assigning tasks and routes to a vehicle fleet while optimizing against supplied objectives and constraints.
  - aid: google:google-play-developer-api
    name: Google Play Developer API
    tags:
      - Android
      - App Store
    humanURL: https://developers.google.com/android-publisher
    properties:
      - url: https://developers.google.com/android-publisher
        type: Documentation
      - url: https://developers.google.com/android-publisher/api-ref/rest
        type: APIReference
    description: The Google Play Developer API allows you to perform publishing and app-management tasks, including managing in-app purchases and subscriptions, retrieving reviews, and automating app publishing workflows.
  - aid: google:firebase-api
    name: Firebase API
    tags:
      - Backend
      - Cloud
      - Mobile
    humanURL: https://firebase.google.com/
    properties:
      - url: https://firebase.google.com/docs
        type: Documentation
      - url: https://firebase.google.com/docs/reference
        type: APIReference
    description: Firebase is a comprehensive app development platform that provides backend services, including real-time databases, authentication, cloud messaging, storage, and hosting for web and mobile applications.
  - aid: google:google-picker-api
    name: Google Picker API
    tags:
      - Documents
      - File Picker
    humanURL: https://developers.google.com/workspace/drive/picker
    properties:
      - url: https://developers.google.com/workspace/drive/picker
        type: Documentation
    description: The Google Picker API is a JavaScript API that allows users to select or upload Google Drive files through a familiar dialog, providing a browser-based file picker for Drive content.
  - aid: google:google-keep-api
    name: Google Keep API
    tags:
      - Notes
      - Productivity
    humanURL: https://developers.google.com/workspace/keep/api
    properties:
      - url: https://developers.google.com/workspace/keep/api
        type: Documentation
    description: The Google Keep API enables enterprise applications to programmatically manage and access Google Keep notes and lists on behalf of users within a Google Workspace domain.
  - aid: google:google-vault-api
    name: Google Vault API
    tags:
      - Compliance
      - Legal
    humanURL: https://developers.google.com/workspace/vault
    properties:
      - url: https://developers.google.com/workspace/vault
        type: Documentation
    description: The Google Vault API provides programmatic access to Vault functionality, enabling retention management, legal hold management, and data export for compliance and eDiscovery purposes.
name: Google
tags:
  - Advertising
  - Cloud
  - Developer
  - Google
  - Platform
  - Search
  - T1
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
common:
  - url: https://cloud.google.com
    type: Google Cloud
  - url: https://developers.google.com/
    type: Developer Portal
  - url: https://developers.googleblog.com/en/
    type: Blog
  - url: https://console.cloud.google.com/apis/dashboard?project=api-project-111046942866
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
  - url: https://developers.google.com/
    name: Google for Developers - from AI and Cloud to Mobile and Web
    type: Portal
  - url: https://discord.com/invite/google-dev-community
    name: Discord
    type: Discord
  - url: https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw
    name: Videos
    type: Videos
  - url: https://console.cloud.google.com/apis/dashboard?pli=1&inv=1&invt=Ab3RcQ&project=api-project-111046942866
    name: APIs & Services  APIs & Services  API Evangelist  Google Cloud console
    type: Explorer
  - url: https://developers.google.com/terms/site-terms
    name: Google Developers Site Terms of Service \_|\_ Google for Developers
    type: TermsOfService
  - url: https://www.anthropic.com/pricing#api
    data:
      - id: gemini-2-5-pro
        name: Gemini 2.5 Pro
        tier: Free
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: Free
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: Free
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Context Caching
            price: Free
            metric: token
            timeFrame: usage
            description: Read prompt caching for model.
          - geo: US
            unit: 1M
            label: Google Search
            price: Free
            metric: token
            timeFrame: usage
            description: Grounding with Google search.
        description: Our state-of-the-art multipurpose model, which excels at coding and complex reasoning tasks.
      - id: gemini-2-5-pro
        name: Gemini 2.5 Pro
        tier: Paid
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 1.25
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Input
            price: 2.5
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 10
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 15
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Context Caching
            price: 0.31
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Context caching for up to 200K.
          - geo: US
            unit: 1M
            label: Context Caching
            price: 0.625
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Context caching for over 200K.
          - geo: US
            unit: 1M
            label: Cache Storage
            price: 0.625
            metric: token
            timeFrame: hour
            description: Caching storage.
          - geo: US
            unit: 100
            label: Google Search
            price: 35
            metric: requests
            timeFrame: usage
            description: Grounding with Google search.
        description: Our state-of-the-art multipurpose model, which excels at coding and complex reasoning tasks.
      - id: gemini-2-5-flash-free
        name: Gemini 2.5 Flash (Free)
        tier: Free
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: Free
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: Free
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Context Caching
            price: Free
            metric: token
            timeFrame: usage
            description: Read prompt caching for model.
          - geo: US
            unit: 1M
            label: Google Search
            price: Free
            metric: token
            timeFrame: usage
            description: Grounding with Google search.
          - geo: US
            unit: 1M
            label: Live API
            price: Free
            metric: token
            timeFrame: usage
            description: Access to the live API.
        description: Our first hybrid reasoning model which supports a 1M token context
      - id: gemini-2-5-flash-paid
        name: Gemini 2.5 Flash (Paid)
        tier: Paid
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input Text Image and Videos
            price: 0.3
            metric: token
            timeFrame: usage
            description: Text and Image Video
          - geo: US
            unit: 1M
            label: Input Audio
            price: 1
            metric: token
            timeFrame: usage
            description: Audio Input
          - geo: US
            unit: 1M
            label: Output
            price: 2.5
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Context Caching Text Image and Video
            price: 0.075
            metric: token
            timeFrame: usage
            description: Context caching for text, images, and video.
          - geo: US
            unit: 1M
            label: Context Caching for Audio
            price: 0.25
            metric: token
            timeFrame: usage
            description: Context caching for audio.
          - geo: US
            unit: 1M
            label: Cache Storage
            price: 1
            metric: token
            timeFrame: hour
            description: Caching storage.
          - geo: US
            unit: 100
            label: Google Search
            price: 35
            metric: requests
            timeFrame: usage
            description: Grounding with Google search.
          - geo: US
            unit: 1M
            label: Live API Text Input
            price: 0.5
            metric: requests
            timeFrame: usage
            description: Live API Text Input
          - geo: US
            unit: 1M
            label: Live API Audio Image Video Input
            price: 3
            metric: requests
            timeFrame: usage
            description: Live API Audio Image Video Input
          - geo: US
            unit: 1M
            label: Live API Text Output
            price: 2
            metric: requests
            timeFrame: usage
            description: Live API Text Output
          - geo: US
            unit: 1M
            label: Live API Audio Image Video Output
            price: 12
            metric: requests
            timeFrame: usage
            description: Live API Audio Output
        description: Our first hybrid reasoning model which supports a 1M token context
      - id: gemini-2-5-flash-lite-free
        name: Gemini 2.5 Flash-Lite (Free)
        tier: Free
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: Free
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: Free
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Context Caching
            price: Free
            metric: token
            timeFrame: usage
            description: Read prompt caching for model.
          - geo: US
            unit: 1M
            label: Google Search
            price: Free
            metric: token
            timeFrame: usage
            description: Grounding with Google search.
        description: Our smallest and most cost effective model, built for at scale usage.
      - id: gemini-2-5-flash-lite-paid
        name: Gemini 2.5 Flash-Lite (Paid)
        tier: Paid
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input Text Image and Videos
            price: 0.1
            metric: token
            timeFrame: usage
            description: Text and Image Video
          - geo: US
            unit: 1M
            label: Input Audio
            price: 0.3
            metric: token
            timeFrame: usage
            description: Audio Input
          - geo: US
            unit: 1M
            label: Output
            price: 0.4
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Context Caching Text Image and Video
            price: 0.025
            metric: token
            timeFrame: usage
            description: Context caching for text, images, and video.
          - geo: US
            unit: 1M
            label: Context Caching for Audio
            price: 0.125
            metric: token
            timeFrame: usage
            description: Context caching for audio.
          - geo: US
            unit: 1M
            label: Cache Storage
            price: 1
            metric: token
            timeFrame: hour
            description: Caching storage.
          - geo: US
            unit: 100
            label: Google Search
            price: 35
            metric: requests
            timeFrame: usage
            description: Grounding with Google search.
        description: Our smallest and most cost effective model, built for at scale usage.
      - id: gemini-2-5-flash-native-audio-free
        name: Gemini 2.5 Flash Native Audio (Free)
        tier: Free
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: Free
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: Free
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
        description: Our native audio models optimized for higher quality audio outputs with better pacing, voice naturalness, verbosity, and mood.
      - id: gemini-2-5-flash-native-audio-paid
        name: Gemini 2.5 Flash Native Audio (Paid)
        tier: Paid
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input Text
            price: 0.5
            metric: token
            timeFrame: usage
            description: Input text.
          - geo: US
            unit: 1M
            label: Input Audio
            price: 3
            metric: token
            timeFrame: usage
            description: Input audio.
          - geo: US
            unit: 1M
            label: Output Text
            price: 2
            metric: token
            timeFrame: usage
            description: Output text.
          - geo: US
            unit: 1M
            label: Output Audio
            price: 12
            metric: token
            timeFrame: usage
            description: Output audio.
        description: Our native audio models optimized for higher quality audio outputs with better pacing, voice naturalness, verbosity, and mood.
      - id: gemini-2-5-flash-preview-tts-free
        name: Gemini 2.5 Flash Preview TTS (Free)
        tier: Free
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: Free
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: Free
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
        description: Our 2.5 Flash text-to-speech audio model optimized for price-performant, low-latency, controllable speech generation.
      - id: gemini-2-5-flash-preview-tts-paid
        name: Gemini 2.5 Flash Preview TTS (Paid)
        tier: Paid
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input Text
            price: 0.5
            metric: token
            timeFrame: usage
            description: Input text.
          - geo: US
            unit: 1M
            label: Output Audio
            price: 10
            metric: token
            timeFrame: usage
            description: Output audio.
        description: Our 2.5 Flash text-to-speech audio model optimized for price-performant, low-latency, controllable speech generation.
      - id: gemini-2-5-pro-preview-tts-free
        name: Gemini 2.5 Pro Preview TTS (Free)
        tier: Free
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: Free
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: Free
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
        description: Our 2.5 Pro text-to-speech audio model optimized for powerful, low-latency speech generation for more natural outputs and easier to steer prompts.
      - id: gemini-2-5-pro-preview-tts-paid
        name: Gemini 2.5 Pro Preview TTS (Paid)
        tier: Paid
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input Text
            price: 1
            metric: token
            timeFrame: usage
            description: Input text.
          - geo: US
            unit: 1M
            label: Output Audio
            price: 20
            metric: token
            timeFrame: usage
            description: Output audio.
        description: Our 2.5 Pro text-to-speech audio model optimized for powerful, low-latency speech generation for more natural outputs and easier to steer prompts.
    name: Pricing
    type: Pricing
  - url: https://gemini.google/subscriptions/
    data:
      - id: free
        name: Free
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Usage based pricing.
        elements:
          - name: Access to 2.5 Flash
          - name: Limited access to 2.5 Pro
          - name: Image Generation with Imagen 4
          - name: Deep Research
          - name: Gemini Live
          - name: Canvas
          - name: Gems
          - name: Generate and animate images with Imagen 4 and Veo 2
          - name: Research and writing assistant
          - name: 15 GB of total storage for Photos, Drive, and Gmail
        description: Get everyday help from Google AI to tackle tasks at work, school or home.
      - id: pro
        name: Google AI Pro
        entries:
          - geo: US
            unit: 1
            label: User
            price: 19.99
            metric: user
            timeFrame: month
            description: Usage based pricing.
        elements:
          - name: Access to 2.5 Flash
          - name: Limited access to 2.5 Pro
          - name: Image Generation with Imagen 4
          - name: Deep Research
          - name: Gemini Live
          - name: Canvas
          - name: Gems
          - name: Generate and animate images with Imagen 4 and Veo 2
          - name: Research and writing assistant
          - name: 15 GB of total storage for Photos, Drive, and Gmail
          - name: Get more access to our most capable model 2.5 Pro, Deep Research on 2.5 Pro and unlock video generation with Veo 3 Fast, our video generation model that maintains high-quality while optimizing for speed
          - name: Access our AI filmmaking tool custom built with Veo 3 Fast to create cinematic scenes and stories
          - name: Higher limits for image-to-video-creation with Veo 2
          - name: Get access to Gemini 2.5 Pro model and Deep Search in AI Mode, plus expanded access to AI-powered calling for local business pricing (US only)
          - name: Higher task limits when using Jules, our asynchronous coding agent for software development
          - name: Research and writing assistant with 5x more Audio Overviews, notebooks, and more
          - name: Access Gemini directly in Google apps, Gmail, Docs, Vids, and more
          - name: our personal assistant to browse the web
          - name: early access
          - name: 2 TB of total storage for Photos, Drive, and Gmail
        description: Get more access to new and powerful features to boost your productivity and creativity.
      - id: pro
        name: Google AI Ultra
        entries:
          - geo: US
            unit: 1
            label: User
            price: 249.99
            metric: user
            timeFrame: month
            description: Usage based pricing.
        elements:
          - name: Highest level of access to Veo 3, our state-of-the-art video generation model, and access to Gemini 2.5 Deep Think, our most advanced reasoning model
          - name: Highest level of access to our AI filmmaking tool with access to Veo 3 and premium features like ingredients to video
          - name: Highest limits for image-to-video creation with Veo 2
          - name: Highest limits to Gemini 2.5 Pro model and Deep Search in AI Mode, plus AI-powered calling for local business pricing (US only)
          - name: Highest task limits when using Jules, our asynchronous coding agent for software development
          - name: Highest limits and best model capabilities (later this year)
          - name: Highest limits to Gemini directly in Google apps, Gmail, Docs, Vids, and more
          - name: Streamline tasks with an agentic research prototype
          - name: early access
          - name: YouTube ad-free, offline, and in the background
          - name: 30 TB of total storage for Photos, Drive, and Gmail
        description: Unlock the highest level of access to the best of Google AI and exclusive features.
    name: Plans
    type: Plans
  - url: https://docs.anthropic.com/en/api/service-tiers
    data:
      - name: Free
        description: Users in eligible countries.
      - name: Tier 1
        description: Billing account linked to the project.
      - name: Tier 2
        description: 'Total spend greater than $250 and at least 30 days since successful payment.  '
      - name: Tier 4
        description: 'Total spend greater than $1,000 and at least 30 days since successful payment  .  '
    name: Tiers
    type: Tiers
    description: Rate limits are tied to the project's usage tier. As your API usage and spending increase, you'll have an option to upgrade to a higher tier with increased rate limits. The qualifications for Tiers 2 and 3 are based on the total cumulative spending on Google Cloud services (including, but not limited to, the Gemini API) for the billing account linked to your project.
  - url: https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits
    data:
      - name: Gemini 2.5 Pro
        tier: Free
        type: Model
        limit: 5
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Pro
        tier: Free
        type: Model
        limit: 250,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Pro
        tier: Free
        type: Model
        limit: 100
        metric: request
        timeframe: day
        description: The requests per day (RPD).
      - name: Gemini 2.5 Flash
        tier: Free
        type: Model
        limit: 10
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Flash
        tier: Free
        type: Model
        limit: 250,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Flash
        tier: Free
        type: Model
        limit: 250
        metric: request
        timeframe: day
        description: The requests per day (RPD).
      - name: "Gemini 2.5 Flash-Lite\t15"
        tier: Free
        type: Model
        limit: 15
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: "Gemini 2.5 Flash-Lite\t15"
        tier: Free
        type: Model
        limit: 250,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: "Gemini 2.5 Flash-Lite\t15"
        tier: Free
        type: Model
        limit: 1000
        metric: request
        timeframe: day
        description: The requests per day (RPD).
      - name: Gemini 2.0 Flash
        tier: Free
        type: Model
        limit: 15
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.0 Flash
        tier: Free
        type: Model
        limit: 1,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.0 Flash
        tier: Free
        type: Model
        limit: 200
        metric: request
        timeframe: day
        description: The requests per day (RPD).
      - name: Gemini 2.0 Flash-Lite
        tier: Free
        type: Model
        limit: 30
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.0 Flash
        tier: Free
        type: Model
        limit: 1,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.0 Flash
        tier: Free
        type: Model
        limit: 200
        metric: request
        timeframe: day
        description: The requests per day (RPD).
      - name: Gemini 2.5 Pro
        tier: Tier 1
        type: Model
        limit: 150
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Pro
        tier: Tier 1
        type: Model
        limit: 2,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Pro
        tier: Tier 1
        type: Model
        limit: 10,000
        metric: request
        timeframe: day
        description: The requests per day (RPD).
      - name: Gemini 2.5 Flash
        tier: Tier 1
        type: Model
        limit: 1,000
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Flash
        tier: Tier 1
        type: Model
        limit: 1,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Flash
        tier: Tier 1
        type: Model
        limit: 10,000
        metric: request
        timeframe: day
        description: The requests per day (RPD).
      - name: Gemini 2.5 Flash-Lite
        tier: Tier 1
        type: Model
        limit: 4,000
        metric: request
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Flash-Lite
        tier: Tier 1
        type: Model
        limit: 4,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.0 Flash
        tier: Tier 1
        type: Model
        limit: 2,000
        metric: request
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.0 Flash
        tier: Tier 1
        type: Model
        limit: 4,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.0 Flash-Lite
        tier: Tier 1
        type: Model
        limit: 4,000
        metric: request
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.0 Flash
        tier: Tier 1
        type: Model
        limit: 4,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Pro
        tier: Tier 2
        type: Model
        limit: 1,000
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Pro
        tier: Tier 2
        type: Model
        limit: 5,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Pro
        tier: Tier 2
        type: Model
        limit: 50,000
        metric: request
        timeframe: day
        description: The requests per day (RPD).
      - name: Gemini 2.5 Flash
        tier: Tier 2
        type: Model
        limit: 2,000
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Flash
        tier: Tier 2
        type: Model
        limit: 3,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Flash
        tier: Tier 2
        type: Model
        limit: 100,000
        metric: request
        timeframe: day
        description: The requests per day (RPD).
      - name: Gemini 2.5 Flash-Lite
        tier: Tier 2
        type: Model
        limit: 10,000
        metric: request
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Flash-Lite
        tier: Tier 2
        type: Model
        limit: 10,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.0 Flash
        tier: Tier 2
        type: Model
        limit: 10,000
        metric: request
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.0 Flash
        tier: Tier 2
        type: Model
        limit: 10,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.0 Flash-Lite
        tier: Tier 2
        type: Model
        limit: 20,000
        metric: request
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.0 Flash-Lite
        tier: Tier 2
        type: Model
        limit: 10,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Pro
        tier: Tier 3
        type: Model
        limit: 2,000
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Pro
        tier: Tier 3
        type: Model
        limit: 8,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Flash
        tier: Tier 3
        type: Model
        limit: 10,000
        metric: token
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Flash
        tier: Tier 3
        type: Model
        limit: 8,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.5 Flash-Lite
        tier: Tier 3
        type: Model
        limit: 30,000
        metric: request
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.5 Flash-Lite
        tier: Tier 3
        type: Model
        limit: 30,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.0 Flash
        tier: Tier 3
        type: Model
        limit: 30,000
        metric: request
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.0 Flash
        tier: Tier 3
        type: Model
        limit: 30,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
      - name: Gemini 2.0 Flash-Lite
        tier: Tier 3
        type: Model
        limit: 30,000
        metric: request
        timeframe: minute
        description: The requests per minute (RPM).
      - name: Gemini 2.0 Flash-Lite
        tier: Tier 3
        type: Model
        limit: 30,000,000
        metric: token
        timeframe: minute
        description: The tokens per minute (TPM).
    name: Rate Limits
    type: RateLimits
    description: The following table lists the rate limits for all standard Gemini API calls.
  - url: https://developers.google.com/get-started
    type: Getting Started
  - url: https://developers.google.com/support
    type: Support
  - url: https://status.cloud.google.com/
    type: Status
  - url: https://developers.google.com/identity/protocols/oauth2
    type: Authentication
  - url: https://x.com/googledevs
    type: X
  - url: https://discuss.google.dev/
    type: Forum
  - url: https://github.com/google
    type: GitHub
  - url: https://console.cloud.google.com/
    type: SignUp
  - url: https://developers.google.com/apis-explorer
    type: APIExplorer
  - url: https://developers.google.com/products
    type: ProductDirectory
  - url: https://developers.google.com/terms/api-services-user-data-policy
    type: DataPolicy
  - type: Features
    data:
      - 'Google (Cloud + Ads + Workspace + Maps + YouTube): hundreds of services across Cloud + Ads + Productivity'
      - 'Detailed pricing: see https://cloud.google.com/pricing'
      - 'Service: Compute Engine'
      - 'Service: Cloud Storage'
      - 'Service: Cloud SQL'
      - 'Service: Spanner'
      - 'Service: Firestore'
      - 'Service: BigQuery'
      - 'Service: Bigtable'
      - 'Service: Cloud Functions (Gen 2)'
      - 'Service: Cloud Run'
      - 'Service: GKE (Kubernetes)'
      - 'Service: Cloud Load Balancing'
      - 'Service: Cloud CDN'
      - 'Service: Cloud DNS'
      - 'Service: VPC'
      - 'Service: IAM'
      - 'Service: Cloud KMS'
      - 'Service: Secret Manager'
      - 'Service: Cloud Monitoring'
      - 'Service: Cloud Logging'
      - 'Service: Cloud Trace'
      - 'Service: Vertex AI / Gemini API'
      - 'Service: Cloud Translation'
      - 'Service: Speech-to-Text'
      - 'Service: Text-to-Speech'
      - 'Service: Vision AI'
      - 'Service: Natural Language AI'
      - 'Service: Document AI'
      - 'Service: Maps Platform'
      - 'Service: Apigee (API management)'
      - 'Service: Pub/Sub'
      - 'Service: Dataflow'
      - 'Service: Dataproc'
      - 'Service: Composer (Airflow)'
      - 'Service: Looker (BI)'
      - 'Service: Cloud Build'
      - 'Service: Artifact Registry'
      - 'Service: Google Ads API'
      - 'Service: Google Search Console API'
      - 'Service: Google Analytics 4 API'
      - 'Service: YouTube Data API'
      - 'Service: YouTube Live Streaming API'
      - 'Service: Google Workspace API'
      - 'Service: Google Drive API'
      - 'Service: Google Calendar API'
      - 'Service: Gmail API'
      - 'Service: Google Maps Platform'
    sources:
      - https://cloud.google.com/pricing
      - https://focus.finops.org/
    updated: '2026-05-04'
created: '2023-11-08'
modified: '2026-05-04'
description: Google's public APIs and services.
maintainers:
  - FN: Kin Lane
    url: https://apievangelist.com
    email: kin@apievangelist.com
  - FN: Google
    url: https://developers.google.com
specificationVersion: '0.19'
---
