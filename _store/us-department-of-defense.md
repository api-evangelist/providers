---
aid: us-department-of-defense
url: https://raw.githubusercontent.com/api-evangelist/us-department-of-defense/refs/heads/main/apis.yml
apis:
  - aid: us-department-of-defense:cwms-data-api
    name: USACE Corps Water Management System Data API
    tags:
      - Water Management
      - Hydrology
      - Army Corps of Engineers
      - Federal Government
    humanURL: https://cwms-data.usace.army.mil/cwms-data/
    properties:
      - url: https://cwms-data.usace.army.mil/cwms-data/
        type: Documentation
      - url: https://cwms-data.usace.army.mil/cwms-data/swagger-ui.html
        type: SwaggerUI
      - url: https://cwms-data-api.readthedocs.io/latest/
        type: Documentation
      - url: https://github.com/USACE/cwms-data-api
        type: GitHub
      - url: https://raw.githubusercontent.com/api-evangelist/us-department-of-defense/refs/heads/main/openapi/usace-cwms-data-api-openapi.yml
        type: OpenAPI
    description: The USACE Corps Water Management System Data API (CDA) is a REST service providing programmatic access to USACE water management data including time series measurements, monitoring locations, rating curves, reservoir levels, and operational data across Army Corps of Engineers projects. Supports both public read access and authenticated write operations.
  - aid: us-department-of-defense:lpms-api
    name: USACE Lock Performance Monitoring System API
    tags:
      - Waterways
      - Navigation
      - Locks
      - Federal Government
    humanURL: https://corpslocks.usace.army.mil/lpwb/f
    properties:
      - url: https://corpslocks.usace.army.mil/lpwb/f
        type: Documentation
      - url: https://catalog.data.gov/dataset/corps-locks
        type: DataCatalog
    description: The USACE Lock Performance Monitoring System (LPMS) API provides data on inland waterway lock operations across the US Army Corps of Engineers lock system. Endpoints return XML data for lock queue reports (past 24 hours), tonnage reports, and traffic reports (past 30 days). Tracks vessel traffic through 192 commercially active locks on US inland waterways.
  - aid: us-department-of-defense:defense-data-gov
    name: DoD Data Portal
    tags:
      - Open Data
      - Defense
      - Federal Government
    humanURL: https://data.defense.gov/Featured-API/
    properties:
      - url: https://data.defense.gov/Featured-API/
        type: Documentation
      - url: https://data.defense.gov/
        type: Portal
    description: The Department of Defense Data Portal features APIs enabling access to DoD open data across military branches, agencies, and programs. The portal surfaces selected APIs from the DoD's data strategy initiative to make defense data more accessible through reusable APIs.
  - aid: us-department-of-defense:dod-open-data
    name: DoD Open Data Platform
    tags:
      - Open Data
      - Defense
      - Datasets
      - Federal Government
    humanURL: https://www.data.mil/
    properties:
      - url: https://www.data.mil/
        type: Portal
    description: The Department of Defense Open Data Platform (data.mil) provides access to unclassified DoD datasets and data services supporting defense research, policy analysis, and public accountability.
name: US Department of Defense
tags:
  - Federal Government
  - Defense
  - Military
  - Water Management
  - Waterways
  - Open Data
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: The US Department of Defense is responsible for providing the military forces needed to deter war and protect the security of the United States. This includes overseeing the Army, Navy, Marine Corps, and Air Force, as well as coordinating with other defense agencies and organizations. The Department of Defense also plays a critical role in developing military strategies, acquiring and maintaining weapons and equipment, and ensuring the readiness and effectiveness of the armed forces. The DoD's data strategy initiatives have led to the publication of multiple public APIs including the USACE Corps Water Management System API, Lock Performance Monitoring System, and the DoD open data portal.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
