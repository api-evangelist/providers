---
aid: astronomy-api
name: Astronomy API
description: AstronomyAPI is a web API for retrieving astronomical information including data about celestial bodies, moon phases, planet positions, star charts, and astronomical events for a given location and time. The API provides developers with access to celestial body positions, astronomical event data, star chart generation, moon phase imagery, and deep space object search capabilities for any geographic location and date/time combination.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Astronomy
  - Celestial Data
  - Space
  - Moon Phases
  - Star Charts
url: https://raw.githubusercontent.com/api-evangelist/astronomy-api/refs/heads/main/apis.yml
created: '2024-03-30'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: astronomy-api:astronomy-api
    name: Astronomy API
    description: The Astronomy API provides access to astronomical data including celestial body positions, moon phases, planet positions, star charts, astronomical events, and deep space object search for any location and time. Endpoints cover bodies, positions, events, studio image generation, star charts, moon phase imagery, and search for stars and deep space objects.
    humanURL: https://docs.astronomyapi.com/
    baseURL: https://api.astronomyapi.com/api/v2
    tags:
      - Astronomy
      - Moon
      - Planets
      - Star Charts
    properties:
      - type: Documentation
        url: https://docs.astronomyapi.com/
      - type: GettingStarted
        url: https://docs.astronomyapi.com/getting-started
common:
  - type: Portal
    url: https://astronomyapi.com/
    title: Astronomy API Website
  - type: Documentation
    url: https://docs.astronomyapi.com/
    title: Documentation
  - type: SignUp
    url: https://astronomyapi.com/auth/signup
    title: Sign Up
  - type: Pricing
    url: https://astronomyapi.com/pricing
    title: Pricing
  - type: Features
    data:
      - name: Celestial Body Positions
        description: Retrieve real-time and historical positions of celestial bodies including planets, moons, and other astronomical objects for any geographic location and date/time.
      - name: Astronomical Events
        description: Access data on celestial events such as eclipses, conjunctions, and other notable astronomical occurrences for a given body and date range.
      - name: Star Chart Generation
        description: Generate customizable star charts as images for any sky position, date, and observer location for use in applications and publications.
      - name: Moon Phase Imagery
        description: Generate moon phase images showing the illumination and appearance of the moon for any given date and location.
      - name: Deep Space Object Search
        description: Search for stars and deep space objects by name or catalog designation to retrieve positional and descriptive data.
  - type: UseCases
    data:
      - name: Astronomy Education Apps
        description: Developers build educational astronomy applications that display real-time planet positions, star charts, and moon phases for learners and enthusiasts.
      - name: Observation Planning Tools
        description: Amateur astronomers use the API to plan observing sessions by retrieving celestial body positions and upcoming astronomical events for their location.
      - name: Astrology and Horoscope Applications
        description: Astrology apps integrate the Astronomy API for accurate planetary position data to power birth chart calculations and transit predictions.
  - type: Integrations
    data:
      - name: Mobile Astronomy Apps
        description: Mobile applications integrate the Astronomy API to provide real-time sky data and star chart overlays for stargazing experiences.
      - name: Planetarium Software
        description: Planetarium and sky simulation software integrates celestial body position data from the Astronomy API for accurate sky rendering.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
