---
aid: national-aeronautics-and-space-administration
name: The National Aeronautics and Space Administration
description: NASA explores the unknown in air and space, innovates for the benefit of humanity, and inspires the world through discovery. The api.nasa.gov portal hosts a federated set of APIs that make NASA imagery, science, and mission data accessible to application developers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://api.nasa.gov/
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Government
  - Science
  - Space
  - Imagery
  - Earth Observation
apis:
  - aid: national-aeronautics-and-space-administration:apod
    name: APOD - Astronomy Picture of the Day
    description: One of the most popular websites at NASA is the Astronomy Picture of the Day. This API exposes the same featured image with metadata.
    humanURL: https://api.nasa.gov/
    baseURL: https://api.nasa.gov/planetary/apod
    tags:
      - Astronomy
      - Imagery
    properties:
      - type: Documentation
        url: https://api.nasa.gov/
      - type: SourceCode
        url: https://github.com/nasa/apod-api
  - aid: national-aeronautics-and-space-administration:neows
    name: NeoWs - Near Earth Object Web Service
    description: Near Earth Object Web Service is a RESTful web service for near earth Asteroid information including closest approach data and orbital data.
    humanURL: https://api.nasa.gov/
    baseURL: https://api.nasa.gov/neo/rest/v1
    tags:
      - Asteroids
      - Space
    properties:
      - type: Documentation
        url: https://api.nasa.gov/
      - type: SourceCode
        url: https://github.com/SpaceRocks/NeoWs
  - aid: national-aeronautics-and-space-administration:donki
    name: DONKI - Space Weather Database Of Notifications, Knowledge, Information
    description: The Space Weather Database Of Notifications, Knowledge, Information (DONKI) is a comprehensive online tool for space weather forecasters, scientists, and researchers.
    humanURL: https://api.nasa.gov/
    baseURL: https://api.nasa.gov/DONKI
    tags:
      - Space Weather
      - Science
    properties:
      - type: Documentation
        url: https://api.nasa.gov/
  - aid: national-aeronautics-and-space-administration:earth
    name: Earth Imagery and Assets
    description: Earth imagery API providing Landsat 8 imagery and asset metadata for a given lat/lon location and date.
    humanURL: https://api.nasa.gov/
    baseURL: https://api.nasa.gov/planetary/earth
    tags:
      - Earth Observation
      - Imagery
    properties:
      - type: Documentation
        url: https://api.nasa.gov/
  - aid: national-aeronautics-and-space-administration:eonet
    name: EONET - Earth Observatory Natural Event Tracker
    description: EONET is a prototype web service that provides a curated source of continuously updated natural event metadata.
    humanURL: https://eonet.gsfc.nasa.gov/
    baseURL: https://eonet.gsfc.nasa.gov/api/v3
    tags:
      - Earth Observation
      - Natural Events
    properties:
      - type: Documentation
        url: https://eonet.gsfc.nasa.gov/docs/v3
  - aid: national-aeronautics-and-space-administration:epic
    name: EPIC - Earth Polychromatic Imaging Camera
    description: The EPIC API provides full disc imagery of the Earth captured by the DSCOVR spacecraft, including natural and enhanced color images.
    humanURL: https://epic.gsfc.nasa.gov/
    baseURL: https://api.nasa.gov/EPIC/api
    tags:
      - Earth Observation
      - Imagery
    properties:
      - type: Documentation
        url: https://epic.gsfc.nasa.gov/about/api
  - aid: national-aeronautics-and-space-administration:mars-rover-photos
    name: Mars Rover Photos
    description: Image data gathered by NASA's Curiosity, Opportunity, Perseverance, and Spirit rovers on Mars, accessible through this API.
    humanURL: https://api.nasa.gov/
    baseURL: https://api.nasa.gov/mars-photos/api/v1
    tags:
      - Mars
      - Imagery
      - Rover
    properties:
      - type: Documentation
        url: https://api.nasa.gov/
      - type: SourceCode
        url: https://github.com/chrisccerami/mars-photo-api
  - aid: national-aeronautics-and-space-administration:nasa-image-library
    name: NASA Image and Video Library
    description: The NASA Image and Video Library API exposes the public NASA media library content including imagery, video, and audio.
    humanURL: https://images.nasa.gov/
    baseURL: https://images-api.nasa.gov
    tags:
      - Imagery
      - Video
      - Media
    properties:
      - type: Documentation
        url: https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf
  - aid: national-aeronautics-and-space-administration:tle
    name: TLE - Two Line Element Set
    description: The TLE API provides up to date two line element set records, the standardized format for distributing earth-orbiting object orbital data.
    humanURL: https://tle.ivanstanojevic.me/
    baseURL: https://tle.ivanstanojevic.me/api
    tags:
      - Satellites
      - Orbital Data
    properties:
      - type: Documentation
        url: https://tle.ivanstanojevic.me/
  - aid: national-aeronautics-and-space-administration:exoplanet
    name: Exoplanet Archive API
    description: Programmatic access to NASA's Exoplanet Archive database of confirmed exoplanets and planet candidates.
    humanURL: https://exoplanetarchive.ipac.caltech.edu/
    baseURL: https://exoplanetarchive.ipac.caltech.edu/TAP
    tags:
      - Exoplanets
      - Astronomy
    properties:
      - type: Documentation
        url: https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html
  - aid: national-aeronautics-and-space-administration:insight
    name: InSight - Mars Weather Service
    description: Per-Sol summary data for each of the last seven available Sols (Martian days) from the InSight lander on Mars.
    humanURL: https://api.nasa.gov/
    baseURL: https://api.nasa.gov/insight_weather
    tags:
      - Mars
      - Weather
    properties:
      - type: Documentation
        url: https://api.nasa.gov/
  - aid: national-aeronautics-and-space-administration:techport
    name: TechPort
    description: RESTful web services to make NASA technology project data available in a machine readable format.
    humanURL: https://techport.nasa.gov/
    baseURL: https://api.nasa.gov/techport/api
    tags:
      - Technology
      - Research
    properties:
      - type: Documentation
        url: https://techport.nasa.gov/api
  - aid: national-aeronautics-and-space-administration:ssd-cneos
    name: SSD/CNEOS - Solar System Dynamics and Center for Near-Earth Object Studies
    description: Provides access to a number of resources from the Solar System Dynamics group and the Center for Near-Earth Object Studies.
    humanURL: https://ssd-api.jpl.nasa.gov/
    baseURL: https://ssd-api.jpl.nasa.gov
    tags:
      - Solar System
      - Asteroids
      - Comets
    properties:
      - type: Documentation
        url: https://ssd-api.jpl.nasa.gov/doc/
common:
  - type: Portal
    url: https://api.nasa.gov/
  - type: Website
    url: https://www.nasa.gov/
  - type: SignUp
    url: https://api.nasa.gov/#signUp
  - type: TermsOfService
    url: https://www.nasa.gov/about/highlights/HP_Privacy.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
