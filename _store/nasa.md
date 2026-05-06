---
aid: nasa
name: NASA
description: NASA (National Aeronautics and Space Administration) provides a suite of public APIs at api.nasa.gov offering access to space, Earth science, and aeronautics data. Key APIs include Astronomy Picture of the Day (APOD), Mars Rover Photos, Near Earth Object Web Service (NeoWs), DONKI space weather events, EPIC Earth imagery, and the NASA Image and Video Library. All APIs are free and accessible with an API key.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/nasa/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Government
  - Science
  - Space
apis:
  - aid: nasa:apod
    name: NASA Astronomy Picture of the Day (APOD) API
    tags:
      - Astronomy
      - Images
      - Space
    humanURL: https://api.nasa.gov/#apod
    properties:
      - url: https://api.nasa.gov/#apod
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/nasa/refs/heads/main/openapi/nasa-apod-openapi.yml
        type: OpenAPI
    description: The Astronomy Picture of the Day API provides access to NASA's popular APOD service, returning the astronomy picture or video of the day along with an explanation written by a professional astronomer.
  - aid: nasa:mars-rover-photos
    name: NASA Mars Rover Photos API
    tags:
      - Images
      - Mars
      - Rovers
      - Space
    humanURL: https://api.nasa.gov/#MarsPhotos
    properties:
      - url: https://api.nasa.gov/#MarsPhotos
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/nasa/refs/heads/main/openapi/nasa-mars-rover-photos-openapi.yml
        type: OpenAPI
    description: The Mars Rover Photos API provides access to images collected by NASA's Curiosity, Opportunity, and Spirit rovers on Mars.
  - aid: nasa:neo
    name: NASA NeoWs (Near Earth Object Web Service) API
    tags:
      - Asteroids
      - Near Earth Objects
      - Space
    humanURL: https://api.nasa.gov/#NeoWS
    properties:
      - url: https://api.nasa.gov/#NeoWS
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/nasa/refs/heads/main/openapi/nasa-neo-openapi.yml
        type: OpenAPI
    description: NeoWs is a RESTful web service for near-Earth asteroid information sourced from the NASA JPL Asteroid team.
  - aid: nasa:donki
    name: NASA DONKI (Space Weather) API
    tags:
      - Solar
      - Space
      - Space Weather
    humanURL: https://api.nasa.gov/#DONKI
    properties:
      - url: https://api.nasa.gov/#DONKI
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/nasa/refs/heads/main/openapi/nasa-donki-openapi.yml
        type: OpenAPI
    description: The DONKI API provides access to space weather events and notifications from NASA's Space Weather Database Of Notifications, Knowledge, Information.
  - aid: nasa:epic
    name: NASA EPIC (Earth Polychromatic Imaging Camera) API
    tags:
      - Earth
      - Images
      - Space
    humanURL: https://api.nasa.gov/#EPIC
    properties:
      - url: https://api.nasa.gov/#EPIC
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/nasa/refs/heads/main/openapi/nasa-epic-openapi.yml
        type: OpenAPI
    description: The EPIC API provides access to imagery from NASA's Earth Polychromatic Imaging Camera onboard the DSCOVR spacecraft.
  - aid: nasa:image-and-video-library
    name: NASA Image and Video Library API
    tags:
      - Images
      - Media
      - Space
      - Video
    humanURL: https://api.nasa.gov/#Images
    properties:
      - url: https://api.nasa.gov/#Images
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/nasa/refs/heads/main/openapi/nasa-nasa-image-and-video-library-openapi.yml
        type: OpenAPI
    description: The NASA Image and Video Library API provides access to NASA's media archive including images, videos, and audio.
common:
  - url: https://api.nasa.gov
    type: Portal
  - url: https://www.nasa.gov
    type: Website
  - url: https://data.nasa.gov
    type: Documentation
  - url: https://github.com/nasa
    type: GitHub Organization
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
