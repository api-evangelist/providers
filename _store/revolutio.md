---
aid: revolutio
name: Revolutio
description: Revolutio provides smart structural engineering software and a Hazard API (formerly CHECKWIND.API) that delivers site-specific wind, snow, ice, and seismic load parameters for structural engineering and construction projects. The API is trusted by over 750 companies and 5000 users worldwide across construction, fabrication, power distribution, signage, structural engineering, and telecommunications. It covers 40+ countries and supports standards including AS/NZS 1170.2, AS 4055, and ASCE 7.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Engineering
  - Hazard
  - Weather
  - Structural Engineering
  - Wind Analysis
  - Construction
url: https://raw.githubusercontent.com/api-evangelist/revolutio/refs/heads/main/apis.yml
created: '2025-02-17'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: revolutio:revolutio-hazard-api
    name: Revolutio Hazard API
    description: The Revolutio Hazard API (formerly CHECKWIND.API) v4 provides site-specific wind, snow, ice, and seismic hazard parameters for structural engineering. Given a latitude/longitude and optional structure height, the API returns design parameters per AS/NZS 1170.2, AS 4055, ASCE 7, and other international standards. Uses a credit-based subscription model where only successful requests consume credits.
    humanURL: https://www.revolutio.com.au/software/hazardapi/
    baseURL: https://api.revolutio.com.au
    tags:
      - Wind Analysis
      - Snow Loading
      - Seismic
      - Structural Engineering
      - Hazard API
      - AS/NZS 1170
      - ASCE 7
    properties:
      - type: Documentation
        url: https://www.revolutio.com.au/support/hazardapi/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/revolutio/refs/heads/main/openapi/revolutio-hazard-api-openapi.yml
      - type: Swagger
        url: https://api.revolutio.com.au/swagger/index.html
    contact:
      - FN: Revolutio Support
        url: https://www.revolutio.com.au/
        email: support@revolutio.com.au
features:
  - name: Wind Analysis
    description: Site-specific wind region, terrain category, topographic class, and shielding class detection
  - name: Snow and Ice Loading
    description: Snow region, elevation class, ground load, and ice region parameters
  - name: Seismic Analysis
    description: Seismic hazard class and site classification
  - name: Machine Learning Detection
    description: ML-based terrain/exposure detection algorithm for improved accuracy
  - name: Multi-Standard Support
    description: Supports AS/NZS 1170.2, AS 4055, ASCE 7, and other international standards
  - name: Global Coverage
    description: 40+ countries across Oceania, Asia, Middle East, North America, South America, and Europe
  - name: Credit-Based Billing
    description: Credit subscription model — only successful requests consume credits
useCases:
  - name: Structural Engineering Design
    description: Determine design wind loads for buildings, structures, and infrastructure
  - name: Construction Project Assessment
    description: Rapid site-specific hazard evaluation for project feasibility and permit applications
  - name: Telecommunications Infrastructure
    description: Wind load calculations for telecommunications towers and antenna structures
  - name: Software Integration
    description: Embed hazard analysis in structural engineering software like SPACE GASS
solutions:
  - name: Structural Engineering Software Integration
    description: Embed site-specific hazard parameters directly into engineering calculation workflows
common:
  - type: Website
    url: https://www.revolutio.com.au/
  - type: Documentation
    url: https://www.revolutio.com.au/support/hazardapi/
  - type: Swagger
    url: https://api.revolutio.com.au/swagger/index.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
