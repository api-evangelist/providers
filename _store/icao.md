---
aid: icao
name: ICAO
description: The International Civil Aviation Organization (ICAO) is a specialized agency of the United Nations that codifies the principles and techniques of international air navigation and fosters the planning and development of international air transport. ICAO's API Data Service provides 50+ continuously updated APIs covering states, airports, operators, airspace, occurrences, and aircraft, including official reference datasets such as DOC7910 location indicators, DOC8585 operator three-letter codes, and DOC8643 aircraft type designators.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Airlines
  - Airports
  - Airspace
  - Aviation
  - Reference Data
  - Standards
  - United Nations
url: https://raw.githubusercontent.com/api-evangelist/icao/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: icao:icao-api-data-service
    name: ICAO API Data Service
    description: The ICAO API Data Service provides programmatic access to authoritative civil aviation data published by ICAO, with continuously updated endpoints across six data areas. An API key is required and responses are available in CSV and JSON formats; pricing tiers include booster packs, full data-set packages, and unlimited-call subscriptions.
    humanURL: https://applications.icao.int/dataservices/default.aspx
    tags:
      - Aviation Data
      - Reference Data
    properties:
      - type: Documentation
        url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
      - type: Portal
        url: https://applications.icao.int/dataservices/default.aspx
      - type: Samples
        url: https://applications.icao.int/dataservices/api-data-samples
      - type: Terms of Service
        url: https://www.icao.int/sites/default/files/Aviation-API-Data-Service/Documents/User-Terms-and-Condtions-for-ICAO-API-Data-Service-APIs-LEB_FINAL_13.04.21.pdf
  - aid: icao:icao-states-api
    name: ICAO States API
    description: Endpoints providing reference and statistical data on ICAO Member States, including state-level aviation activity, agreements, and contracting state metadata.
    humanURL: https://applications.icao.int/dataservices/default.aspx
    tags:
      - States
      - Reference Data
    properties:
      - type: Documentation
        url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
  - aid: icao:icao-airports-api
    name: ICAO Airports API
    description: Endpoints exposing ICAO airport reference data including DOC7910 location indicators, airport metadata, and related aerodrome information.
    humanURL: https://applications.icao.int/dataservices/default.aspx
    tags:
      - Airports
      - DOC7910
      - Reference Data
    properties:
      - type: Documentation
        url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
  - aid: icao:icao-operators-api
    name: ICAO Operators API
    description: Endpoints providing operator reference data including DOC8585 three-letter operator designators, telephony, and operator details for airlines and aircraft operators.
    humanURL: https://applications.icao.int/dataservices/default.aspx
    tags:
      - DOC8585
      - Operators
      - Reference Data
    properties:
      - type: Documentation
        url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
  - aid: icao:icao-airspace-api
    name: ICAO Airspace API
    description: Endpoints providing airspace, navigation, and route data including flight information regions and airspace structures relevant to international air navigation.
    humanURL: https://applications.icao.int/dataservices/default.aspx
    tags:
      - Airspace
      - Navigation
    properties:
      - type: Documentation
        url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
  - aid: icao:icao-occurrences-api
    name: ICAO Occurrences API
    description: Endpoints providing access to aviation safety occurrence data, including accident and incident records reported through ICAO's safety information systems.
    humanURL: https://applications.icao.int/dataservices/default.aspx
    tags:
      - Accidents
      - Incidents
      - Safety
    properties:
      - type: Documentation
        url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
  - aid: icao:icao-aircraft-api
    name: ICAO Aircraft API
    description: Endpoints providing aircraft reference data including DOC8643 aircraft type designators, manufacturer information, and aircraft performance categories.
    humanURL: https://applications.icao.int/dataservices/default.aspx
    tags:
      - Aircraft
      - DOC8643
      - Reference Data
    properties:
      - type: Documentation
        url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
common:
  - type: Website
    url: https://www.icao.int/
  - type: Portal
    url: https://applications.icao.int/dataservices/default.aspx
  - type: Documentation
    url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
  - type: Samples
    url: https://applications.icao.int/dataservices/api-data-samples
  - type: Pricing
    url: https://store.icao.int/en/aviation-api-data-service
  - type: Terms of Service
    url: https://www.icao.int/sites/default/files/Aviation-API-Data-Service/Documents/User-Terms-and-Condtions-for-ICAO-API-Data-Service-APIs-LEB_FINAL_13.04.21.pdf
  - type: Support
    url: https://www.icao.int/contact/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
