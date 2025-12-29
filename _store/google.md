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
    properties:
      - url: https://cloud.google.com/api-gateway/docs/reference/rest
        type: Documentation
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
    properties:
      - url: https://developers.google.com/books/docs/v1/using
        type: Documentation
      - url: https://developers.google.com/books/docs/v1/getting_started
        type: Getting Started
      - url: openapi/books-api-openapi.yml
        type: OpenAPI
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
    description: Reads and writes Google Docs documents.
  - aid: google:google-maps-api
    name: Google Maps API
    humanURL: https://developers.google.com/maps
    properties:
      - url: https://developers.google.com/maps
        type: Documentation
    description: >-
      Create real-world, real-time experiences with the latest Maps, Routes, and
      Places features from Google Maps Platform. Built by the Google team for
      developers everywhere.
  - aid: google:google-places-api
    name: Google Places API
    tags:
      - Places
    humanURL: https://developers.google.com/maps/documentation/places/web-service
    properties:
      - url: https://developers.google.com/maps/documentation/places/web-service
        type: Documentation
      - url: properties/google-places-api-openapi.yml
        type: OpenAPI
    description: >-
      The Google Places API provides programmatic access to detailed information
      about millions of places, including names, addresses, reviews, photos, and
      geographic coordinates, enabling location-based search and discovery in
      applications.      
  - aid: google:google-aggregate-places-api
    name: Google Aggregate Places API
    humanURL: https://developers.google.com/maps/documentation/places-aggregate
    properties:
      - url: https://developers.google.com/maps/documentation/places-aggregate
        type: Documentation
    description: >-
      The Google Places Aggregate API delivers aggregated insightssuch as the
      count or list of Place IDsfor places within a defined area, based on
      filters like type (e.g., restaurants), price level, user ratings, or
      operational status.  
  - aid: google:google-places-insights-api
    name: Google Places Insights API
    humanURL: https://developers.google.com/maps/documentation/placesinsights
    properties:
      - url: https://developers.google.com/maps/documentation/placesinsights
        type: Documentation
    description: >-
      The Google Places Insights API (now generally known as the Places
      Aggregate API) provides aggregated intelligencesuch as counts of matching
      places or lists of Place IDswithin a defined geographic area, filtered by
      attributes like place type, ratings, price, or operating status, to help
      analyze local density and distribution.  
  - aid: google:google-street-view-imagery-api
    name: Google Street View Imagery API
    humanURL: https://developers.google.com/maps/documentation/streetview
    properties:
      - url: https://developers.google.com/maps/documentation/streetview
        type: Documentation
    description: >-
      The Google Street View Imagery API lets developers embed and display
      interactive 360-degree panoramic images from Google Street View in their
      applications, enabling users to virtually explore real-world locations.  
  - aid: google:google-elevation-api
    name: Google Elevation API
    humanURL: https://developers.google.com/maps/documentation/elevation
    properties:
      - url: https://developers.google.com/maps/documentation/elevation
        type: Documentation
    description: >-
      The Google Elevation API provides elevation data for specific locations on
      the Earth's surface, including height above sea level for points, paths,
      or sets of coordinates. 
  - aid: google:google-routes-api
    name: Google Routes API
    humanURL: https://developers.google.com/maps/documentation/routes
    properties:
      - url: https://developers.google.com/maps/documentation/routes
        type: Documentation
    description: >-
      The Google Routes API calculates routes between locations, providing
      directions, distances, travel times, and additional data like traffic
      conditions, tolls, and alternative paths for various modes of
      transportation. 
  - aid: google:google-geocoding-api
    name: Google Geocoding API
    humanURL: https://developers.google.com/maps/documentation/geocoding
    properties:
      - url: https://developers.google.com/maps/documentation/geocoding
        type: Documentation
    description: >-
      The Google Geocoding API converts addresses into geographic coordinates
      (latitude and longitude) and vice versa, enabling applications to map
      locations and perform location-based queries. 
  - aid: google:google-geolocation-api
    name: Google Geolocation API
    humanURL: https://developers.google.com/maps/documentation/geolocation
    properties:
      - url: https://developers.google.com/maps/documentation/geolocation
        type: Documentation
    description: >-
      The Google Geolocation API determines a devices approximate location based
      on nearby cell towers, Wi-Fi nodes, or Bluetooth beacons, without
      requiring GPS. 
  - aid: google:google-address-validation-api
    name: Google Address Validation API
    humanURL: https://developers.google.com/maps/documentation/address-validation
    properties:
      - url: https://developers.google.com/maps/documentation/address-validation
        type: Documentation
    description: >-
      The Google Address Validation API standardizes, validates, and enriches
      postal addresses by checking them against authoritative data sources,
      ensuring accuracy and deliverability for shipping, billing, and
      location-based services. 
  - aid: google:google-time-zone-api
    name: Google Time Zone API
    humanURL: https://developers.google.com/maps/documentation/timezone
    properties:
      - url: https://developers.google.com/maps/documentation/timezone
        type: Documentation
    description: >-
      The Google Time Zone API provides time zone information for a given
      location, including the standard time offset from UTC and daylight saving
      time details. 
  - aid: google:google-air-quality-api
    name: Google Air Quality API
    humanURL: https://developers.google.com/maps/documentation/air-quality
    properties:
      - url: https://developers.google.com/maps/documentation/air-quality
        type: Documentation
    description: >-
      The Google Air Quality API allows applications to access real-time,
      historical, and forecasted air quality dataencompassing over 70 indices,
      pollutant details, health recommendations, and heatmap tiles for
      visualizing atmospheric conditions at a high (500//500/m) resolution
      across more than 100 countries. 
  - aid: google:google-pollen-api
    name: Google Pollen API
    humanURL: https://developers.google.com/maps/documentation/pollen
    properties:
      - url: https://developers.google.com/maps/documentation/pollen
        type: Documentation
    description: >-
      The Google Pollen API provides localized pollen informationincluding daily
      forecasts, pollen levels by plant type (trees, weeds, grasses), and
      related health recommendationshelping applications inform users about
      allergy risks in their area. 
  - aid: google:google-solar-api
    name: Google Solar API
    humanURL: https://developers.google.com/maps/documentation/solar
    properties:
      - url: https://developers.google.com/maps/documentation/weather
        type: Documentation
    description: >-
      The Google Solar API delivers solar potential data for buildings,
      including rooftop geometry, shading, sunlight exposure, and energy
      production estimates, to support solar panel planning and deployment. 
  - aid: google:google-weather-api
    name: Google Weather API
    humanURL: https://developers.google.com/maps/documentation/weather
    properties:
      - url: https://developers.google.com/maps/documentation/weather
        type: Documentation
    description: >-
      The Google Weather API delivers hyperlocal, real-time weather
      dataincluding current conditions, hourly and 10day forecasts, and the past
      24 hours of historyfor any location worldwide, with information refreshed
      every 1530 minutes. 
  - aid: google:google-gemini-api
    name: Google Gemini API
    tags:
      - Documents
    humanURL: https://ai.google.dev/
    properties:
      - url: https://ai.google.dev/
        type: Documentation
name: Google
tags:
  - Search
  - Advertising
  - T1
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
  - url: https://developers.google.com/
    name: Google for Developers - from AI and Cloud to Mobile and Web
    type: Portal
  - url: https://discord.com/invite/google-dev-community
    name: Discord
    type: Discord
  - url: https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw
    name: Videos
    type: Videos
  - url: >-
      https://console.cloud.google.com/apis/dashboard?pli=1&inv=1&invt=Ab3RcQ&project=api-project-111046942866
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
        description: >-
          Our state-of-the-art multipurpose model, which excels at coding and
          complex reasoning tasks.
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
        description: >-
          Our state-of-the-art multipurpose model, which excels at coding and
          complex reasoning tasks.
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
        description: >-
          Our native audio models optimized for higher quality audio outputs
          with better pacing, voice naturalness, verbosity, and mood.
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
        description: >-
          Our native audio models optimized for higher quality audio outputs
          with better pacing, voice naturalness, verbosity, and mood.
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
        description: >-
          Our 2.5 Flash text-to-speech audio model optimized for
          price-performant, low-latency, controllable speech generation.
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
        description: >-
          Our 2.5 Flash text-to-speech audio model optimized for
          price-performant, low-latency, controllable speech generation.
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
        description: >-
          Our 2.5 Pro text-to-speech audio model optimized for powerful,
          low-latency speech generation for more natural outputs and easier to
          steer prompts.
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
        description: >-
          Our 2.5 Pro text-to-speech audio model optimized for powerful,
          low-latency speech generation for more natural outputs and easier to
          steer prompts.
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
        description: >-
          Get everyday help from Google AI to tackle tasks at work, school or
          home.
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
          - name: >-
              Get more access to our most capable model 2.5 Pro, Deep Research
              on 2.5 Pro and unlock video generation with Veo 3 Fast, our video
              generation model that maintains high-quality while optimizing for
              speed
          - name: >-
              Access our AI filmmaking tool custom built with Veo 3 Fast to
              create cinematic scenes and stories
          - name: Higher limits for image-to-video-creation with Veo 2
          - name: >-
              Get access to Gemini 2.5 Pro model and Deep Search in AI Mode,
              plus expanded access to AI-powered calling for local business
              pricing (US only)
          - name: >-
              Higher task limits when using Jules, our asynchronous coding agent
              for software development
          - name: >-
              Research and writing assistant with 5x more Audio Overviews,
              notebooks, and more
          - name: Access Gemini directly in Google apps, Gmail, Docs, Vids, and more
          - name: our personal assistant to browse the web
          - name: early access
          - name: 2 TB of total storage for Photos, Drive, and Gmail
        description: >-
          Get more access to new and powerful features to boost your
          productivity and creativity.
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
          - name: >-
              Highest level of access to Veo 3, our state-of-the-art video
              generation model, and access to Gemini 2.5 Deep Think, our most
              advanced reasoning model
          - name: >-
              Highest level of access to our AI filmmaking tool with access to
              Veo 3 and premium features like ingredients to video
          - name: Highest limits for image-to-video creation with Veo 2
          - name: >-
              Highest limits to Gemini 2.5 Pro model and Deep Search in AI Mode,
              plus AI-powered calling for local business pricing (US only)
          - name: >-
              Highest task limits when using Jules, our asynchronous coding
              agent for software development
          - name: Highest limits and best model capabilities (later this year)
          - name: >-
              Highest limits to Gemini directly in Google apps, Gmail, Docs,
              Vids, and more
          - name: Streamline tasks with an agentic research prototype
          - name: early access
          - name: YouTube ad-free, offline, and in the background
          - name: 30 TB of total storage for Photos, Drive, and Gmail
        description: >-
          Unlock the highest level of access to the best of Google AI and
          exclusive features.
    name: Plans
    type: Plans
  - url: https://docs.anthropic.com/en/api/service-tiers
    data:
      - name: Free
        description: Users in eligible countries.
      - name: Tier 1
        description: Billing account linked to the project.
      - name: Tier 2
        description: >-
          Total spend greater than $250 and at least 30 days since successful
          payment.  
      - name: Tier 4
        description: >-
          Total spend greater than $1,000 and at least 30 days since successful
          payment  .  
    name: Tiers
    type: Tiers
    description: >-
      Rate limits are tied to the project's usage tier. As your API usage and
      spending increase, you'll have an option to upgrade to a higher tier with
      increased rate limits. The qualifications for Tiers 2 and 3 are based on
      the total cumulative spending on Google Cloud services (including, but not
      limited to, the Gemini API) for the billing account linked to your
      project.
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
    description: >-
      The following table lists the rate limits for all standard Gemini API
      calls.
created: '2023-11-08'
modified: '2025-12-29'
description: |-
  Google Cloud APIs are programmatic interfaces to Google Cloud Platform
  services. They are a key part of Google Cloud Platform, allowing you to easily
  add the power of everything from computing to networking to storage to
  machine-learning-based data analysis to your applications.
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.19'
---