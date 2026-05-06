---
aid: artemis
name: Artemis
description: NASA's Artemis program is the next generation of lunar exploration, aiming to return humans to the Moon and establish a sustainable presence for future missions to Mars. The program includes the Space Launch System (SLS) rocket, Orion spacecraft, the Lunar Gateway space station, and commercial lunar landers from SpaceX and Blue Origin. NASA's Open APIs provide programmatic access to Artemis-related data, including mission imagery, space weather, and planetary data through api.nasa.gov. The program operates under NASA's Science Mission Directorate and Exploration Systems Development Mission Directorate.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Exploration
  - Lunar
  - Moon
  - NASA
  - Space
  - Government
url: https://raw.githubusercontent.com/api-evangelist/artemis/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: artemis:nasa-open-api
    name: NASA Open APIs
    description: NASA's Open API platform at api.nasa.gov provides programmatic access to NASA data including the Astronomy Picture of the Day (APOD), Near Earth Object Web Service (NeoWs), NASA Image and Video Library, Mars Rover Photos, EPIC Earth imagery, and space weather data relevant to Artemis mission planning and operations.
    humanURL: https://api.nasa.gov/
    baseURL: https://api.nasa.gov
    tags:
      - Space
      - NASA
      - Science
      - Imagery
      - Open Data
    properties:
      - type: Documentation
        url: https://api.nasa.gov/
      - type: GettingStarted
        url: https://api.nasa.gov/#getting-started
  - aid: artemis:nasa-tech-transfer-api
    name: NASA Technology Transfer API
    description: The NASA Technology Transfer API provides programmatic access to the NASA patent portfolio, software catalog, and spinoff technologies developed through the Artemis program and other NASA missions, enabling technology licensing and commercialization queries.
    humanURL: https://technology.nasa.gov/
    baseURL: https://technology.nasa.gov
    tags:
      - Technology
      - Patents
      - Software
      - Licensing
    properties:
      - type: Documentation
        url: https://technology.nasa.gov/
common:
  - type: Portal
    url: https://www.nasa.gov/artemis/
    title: Artemis Program Website
  - type: Documentation
    url: https://api.nasa.gov/
    title: NASA Open APIs
  - type: GitHubOrganization
    url: https://github.com/nasa
    title: NASA GitHub Organization
  - type: SignUp
    url: https://api.nasa.gov/#signUp
    title: API Key Signup
  - type: PrivacyPolicy
    url: https://www.nasa.gov/privacy/
    title: Privacy Policy
  - type: Features
    data:
      - name: Astronomy Picture of the Day API
        description: Daily NASA astronomy images with descriptions and metadata, providing a public showcase of space imagery relevant to Artemis and broader space exploration.
      - name: Near Earth Object Web Service
        description: NeoWs API provides data on near earth asteroids and their orbital parameters, supporting space situational awareness for lunar missions.
      - name: Mars Rover Photos API
        description: Access to photos captured by Curiosity, Opportunity, and Spirit Mars rovers, providing precursor science data for future crewed Mars missions planned after Artemis establishes lunar presence.
      - name: EPIC Earth Imagery
        description: Earth Polychromatic Imaging Camera imagery showing full-disc Earth imagery, relevant to climate monitoring that informs long-duration space missions.
      - name: Space Weather Database Of Notifications, Knowledge, Information
        description: DONKI API provides solar flare, geomagnetic storm, and space weather data critical for mission planning and crew safety on Artemis lunar missions.
  - type: UseCases
    data:
      - name: Mission Data Integration
        description: Researchers and mission planners integrate NASA Open APIs to build dashboards and tools that aggregate space weather, trajectory, and imagery data for Artemis mission support.
      - name: Education and Outreach
        description: Educators and developers build Artemis-themed applications using NASA imagery and mission data to engage the public in lunar exploration.
      - name: Research Applications
        description: Scientists access planetary and space environment data programmatically to support research that informs Artemis crew safety and mission planning.
      - name: Technology Transfer
        description: Companies and universities query the NASA Technology Transfer API to identify Artemis-developed patents and software available for licensing.
  - type: Integrations
    data:
      - name: SpaceX Starship
        description: Commercial lunar lander integration for Artemis III and V crewed lunar surface missions.
      - name: Blue Origin Blue Moon
        description: Commercial lunar lander selected for Artemis IV crewed lunar landing mission.
      - name: Commercial Lunar Payload Services (CLPS)
        description: Program integrating multiple commercial providers to deliver science payloads to the lunar surface in support of Artemis science objectives.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
