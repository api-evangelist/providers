---
aid: terrain-discovery-environment-api
name: Terrain Discovery Environment API
description: Terrain is the primary REST API gateway for CyVerse's Discovery Environment (DE), an open-source data science workbench. Terrain validates user authentication via Keycloak/JWT and orchestrates calls to backend microservices covering filesystem operations, application management, data analysis, metadata annotation, notifications, and persistent identifier management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bioinformatics
  - Data Science
  - Life Sciences
  - Filesystem
  - Cloud Computing
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/terrain-discovery-environment-api/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: terrain-discovery-environment-api:terrain-api
    name: Terrain API
    description: The Terrain API is the main entry-point REST service for the CyVerse Discovery Environment. It handles authentication via Keycloak JWT tokens and orchestrates calls to backend services for filesystem management, app execution, data analysis, metadata, notifications, and more.
    humanURL: https://cyverse.org/Science-APIs
    baseURL: https://de.cyverse.org/terrain
    tags:
      - Bioinformatics
      - Filesystem
      - Data Analysis
      - Applications
      - Notifications
    properties:
      - url: https://docs.cyverse.org/services/api_overview/
        type: Documentation
      - url: https://de.cyverse.org/terrain/docs
        type: SwaggerUI
      - url: https://github.com/cyverse-de/terrain
        type: Repository
      - url: https://raw.githubusercontent.com/api-evangelist/terrain-discovery-environment-api/refs/heads/main/openapi/terrain-openapi.yml
        type: OpenAPI
common:
  - name: CyVerse Developer Portal
    url: https://cyverse.org/Science-APIs
    type: Portal
  - name: CyVerse Documentation
    url: https://docs.cyverse.org
    type: Documentation
  - name: Terrain GitHub Repository
    url: https://github.com/cyverse-de/terrain
    type: Repository
  - name: Discovery Environment
    url: https://de.cyverse.org
    type: Portal
  - name: Terrain API Webinar
    url: https://cyverse.org/webinar_TerrainAPI
    type: Webinar
  - name: Keycloak Authentication
    url: https://docs.cyverse.org/services/getting_started/
    type: Authentication
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
