---
aid: skywest
url: https://raw.githubusercontent.com/api-evangelist/skywest/refs/heads/main/apis.yml
name: SkyWest Airlines
tags:
  - Airlines
  - Aviation
  - Regional Airline
  - Transportation
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-02'
modified: '2026-05-02'
position: Consumer
segments:
  - Transportation
  - Aviation
description: SkyWest Airlines is the largest regional airline in North America, headquartered in St. George, Utah. Operating under partnership agreements with United Airlines, Delta Air Lines, American Airlines, and Alaska Airlines, SkyWest serves over 256 destinations across the United States, Canada, and Mexico with a fleet of 500+ Bombardier regional jets (CRJ200, CRJ550, CRJ900). Founded in 1972, SkyWest carries over 46 million passengers annually operating as United Express, Delta Connection, American Eagle, and Alaska SkyWest. The company does not offer a public developer API; flight data is accessible through third-party aviation data providers.
apis:
  - aid: skywest:flight-data
    name: SkyWest Flight Data
    tags:
      - Flight Status
      - Aviation
      - Flight Tracking
    humanURL: https://www.skywest.com
    properties:
      - url: https://airlabs.co/skywest-airlines-developer-api
        type: ThirdPartyAPI
      - url: https://www.flightradar24.com/data/airlines/oo-skw
        type: FlightTracking
      - url: https://www.skywest.com/about-skywest-airlines/facts
        type: FactSheet
      - url: json-ld/skywest-context.jsonld
        type: JSON-LD
      - url: vocabulary/skywest-vocabulary.yml
        type: Vocabulary
    description: SkyWest Airlines flight data including flight status, schedules, and routes is accessible through third-party aviation APIs such as AirLabs. SkyWest operates under IATA code OO / ICAO code SKW and serves 256 destinations across North America.
common:
  - type: Website
    url: https://www.skywest.com
  - type: About
    url: https://www.skywest.com/about-skywest-airlines/
  - type: FactSheet
    url: https://www.skywest.com/about-skywest-airlines/facts
  - type: History
    url: https://www.skywest.com/about-skywest-airlines/skywest-history
  - type: Careers
    url: https://www.skywest.com/careers/
  - type: FlightStatus
    url: https://www.skywest.com/fly-skywest-airlines/flight-status/
  - type: ThirdPartyAPI
    url: https://airlabs.co/skywest-airlines-developer-api
  - type: FlightTracking
    url: https://www.flightradar24.com/data/airlines/oo-skw
  - type: Press
    url: https://www.skywest.com/about-skywest-airlines/press-room/
  - type: JSON-LD
    url: json-ld/skywest-context.jsonld
  - type: Vocabulary
    url: vocabulary/skywest-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
