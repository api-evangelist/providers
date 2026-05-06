---
aid: federal-aviation-administration
name: Federal Aviation Administration
description: The Federal Aviation Administration (FAA) is the U.S. Department of Transportation agency responsible for the regulation and oversight of civil aviation. The FAA publishes a range of public data products and APIs covering airport status, NOTAMs, aeronautical information, airmen and aircraft registries, and System Wide Information Management (SWIM) feeds for air traffic operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Aviation
  - Federal Government
url: https://raw.githubusercontent.com/api-evangelist/federal-aviation-administration/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-aviation-administration:notam-api
    name: FAA NOTAM
    description: The FAA NOTAM API provides access to Notices to Air Missions (NOTAMs), which are time-critical aeronautical information that could affect a pilot's decision to make a flight. The API allows developers to query active NOTAMs by location, type, and effective date for use in flight planning and situational awareness applications.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://api.faa.gov/notamapi/
    baseURL: https://external-api.faa.gov/notamapi/v1
    tags:
      - Aeronautical Information
      - Air Traffic
      - NOTAM
    properties:
      - type: Documentation
        url: https://api.faa.gov/notamapi/
  - aid: federal-aviation-administration:airport-status
    name: FAA Airport Status
    description: The FAA Airport Status Web Service (ASWS) provides current airport conditions, including delays and ground stops, for major United States airports. Developers can use the service to retrieve real-time status information for use in flight planning, traveler-facing applications, and operational dashboards.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.faa.gov/data_research/aviation_data_statistics
    baseURL: https://soa.smext.faa.gov/asws
    tags:
      - Airport
      - Air Traffic
      - Delays
    properties:
      - type: Documentation
        url: https://www.faa.gov/data_research/aviation_data_statistics
  - aid: federal-aviation-administration:nasr-subscription
    name: FAA NASR Subscription
    description: The FAA National Airspace System Resources (NASR) Subscription provides authoritative aeronautical data covering airports, navigation aids, airways, fixes, and special-use airspace on a 28-day publication cycle. The data is the source of truth used to update aeronautical charts and flight planning systems.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://nfdc.faa.gov/nfdcApps/services/ajv5/airportSubscriberFile.jsp
    tags:
      - Aeronautical Information
      - Airports
      - Navigation
    properties:
      - type: Documentation
        url: https://nfdc.faa.gov/nfdcApps/services/ajv5/airportSubscriberFile.jsp
  - aid: federal-aviation-administration:airmen-registry
    name: FAA Airmen Registry
    description: The FAA Airmen Registry provides downloadable data on certificated pilots and other airmen in the United States, including pilot certificates, ratings, and medical certificates. The dataset supports verification, research, and analytics use cases.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.faa.gov/licenses_certificates/airmen_certification/releasable_airmen_download
    tags:
      - Airmen
      - Certification
      - Pilots
    properties:
      - type: Documentation
        url: https://www.faa.gov/licenses_certificates/airmen_certification/releasable_airmen_download
  - aid: federal-aviation-administration:aircraft-registry
    name: FAA Aircraft Registry
    description: The FAA Aircraft Registry provides downloadable data on civil aircraft registered in the United States, including registration, ownership, and airworthiness information. The dataset is widely used for safety analysis, fleet research, and aircraft tracking applications.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download
    tags:
      - Aircraft
      - Registration
      - Certification
    properties:
      - type: Documentation
        url: https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download
  - aid: federal-aviation-administration:swim
    name: FAA System Wide Information Management
    description: The FAA System Wide Information Management (SWIM) program is a service-oriented information sharing platform that delivers real-time National Airspace System data to authorized consumers. SWIM publishes message-oriented data streams covering flight, weather, surveillance, and aeronautical information through a common infrastructure.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.faa.gov/air_traffic/technology/swim
    tags:
      - Air Traffic
      - Real-Time
      - System Wide Information Management
    properties:
      - type: Documentation
        url: https://www.faa.gov/air_traffic/technology/swim
common:
  - type: Website
    url: https://www.faa.gov/
  - type: Documentation
    url: https://www.faa.gov/data_research
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
