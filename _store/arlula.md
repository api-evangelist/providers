---
aid: arlula
name: Arlula
description: Arlula is a satellite imagery marketplace and API platform providing programmatic access to archive and tasking satellite imagery from multiple providers. The Arlula API enables developers to search the global satellite archive, discover tasking opportunities, place imagery orders, and download delivered datasets including GeoTIFF imagery, preview images, and metadata files.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Earth Observation
  - Geospatial
  - Imagery
  - Remote Sensing
  - Satellites
url: https://raw.githubusercontent.com/api-evangelist/arlula/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: arlula:arlula-api
    name: Arlula API
    description: The Arlula API provides programmatic access to satellite imagery search, ordering, and delivery. It covers archive search for historical imagery, tasking for future satellite captures, and order management including campaign, dataset, and resource download operations. Authentication uses HTTP Basic with API Key and API Secret obtained from the Arlula dashboard.
    humanURL: https://arlula.com/documentation/
    baseURL: https://api.arlula.com
    tags:
      - Archive
      - Earth Observation
      - Imagery
      - Satellites
      - Tasking
    properties:
      - type: Documentation
        url: https://arlula.com/documentation/
      - type: OpenAPI
        url: openapi/arlula-openapi.yaml
      - type: JSONSchema
        url: json-schema/arlula-archive-scene-schema.json
      - type: JSONSchema
        url: json-schema/arlula-archive-search-request-schema.json
      - type: JSONSchema
        url: json-schema/arlula-tasking-opportunity-schema.json
      - type: JSONSchema
        url: json-schema/arlula-order-schema.json
      - type: JSONStructure
        url: json-structure/arlula-archive-scene-structure.json
      - type: JSONStructure
        url: json-structure/arlula-tasking-opportunity-structure.json
      - type: JSONStructure
        url: json-structure/arlula-order-structure.json
      - type: JSON-LD
        url: json-ld/arlula-api-context.jsonld
common:
  - type: Website
    url: https://arlula.com/
  - type: Documentation
    url: https://arlula.com/documentation/
  - type: GettingStarted
    url: https://arlula.com/documentation/
  - type: Portal
    url: https://dashboard.arlula.com
  - type: GitHubOrganization
    url: https://github.com/Arlula
  - type: SpectralRules
    url: rules/arlula-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/satellite-imagery-operations.yaml
  - type: Vocabulary
    url: vocabulary/arlula-vocabulary.yaml
  - type: Features
    data:
      - name: Archive Search
        description: Search a global satellite image archive from multiple providers using area-of-interest (polygon/bounding box) and temporal filters to find available historical scenes.
      - name: Satellite Tasking
        description: Commission future satellite captures by searching tasking opportunities and placing orders for specific areas of interest and time windows.
      - name: Multi-Provider Access
        description: Access imagery from multiple satellite providers through a single unified API, enabling price and resolution comparisons across providers.
      - name: Bundle Selection
        description: Choose from available product bundles (e.g., analytic, visual) when ordering scenes to match data requirements and budget.
      - name: Dataset Download
        description: Download delivered imagery resources including GeoTIFF files, preview images, and metadata through the Orders API after capture and processing.
      - name: Batch Ordering
        description: Place multiple archive or tasking orders in a single batch API request to efficiently process large-scale imagery acquisitions.
  - type: UseCases
    data:
      - name: Agricultural Monitoring
        description: Search and order archive or tasking imagery to monitor crop health, irrigation patterns, and field conditions over growing seasons.
      - name: Environmental Change Detection
        description: Acquire multi-temporal satellite imagery to detect deforestation, coastal erosion, urban expansion, or disaster impact areas.
      - name: Infrastructure Inspection
        description: Order high-resolution imagery for remote inspection of pipelines, power lines, roads, and construction site progress monitoring.
      - name: Disaster Response
        description: Rapidly search and order post-event imagery to assess damage extent and support emergency response and recovery planning.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
