---
name: Salesforce Net Zero Cloud
description: The Salesforce Net Zero Cloud API enables organizations to track, analyze, and report on their carbon emissions and sustainability data. It provides programmatic access to environmental data, carbon accounting, and ESG reporting capabilities including Scope 1, 2, and 3 emissions tracking, energy consumption, waste management, water usage, and sustainability goal management.
image: https://www.salesforce.com/content/dam/web/en_us/www/images/logo-salesforce.svg
url: https://www.salesforce.com/products/net-zero-cloud/overview/
created: '2024'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Carbon Accounting
  - Carbon Emissions
  - Climate
  - Environmental
  - ESG
  - Net Zero
  - Sustainability
apis:
  - name: Net Zero Cloud REST API
    description: REST API for managing carbon emissions data, sustainability records, and environmental impact tracking within Net Zero Cloud. Supports Scope 1, 2, and 3 emissions, energy consumption, waste disposal, water withdrawal, and sustainability goals.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/logo-salesforce.svg
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.netzero_api.meta/netzero_api/
    baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
    tags:
      - Carbon Emissions
      - Emissions Tracking
      - REST
      - Sustainability
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.netzero_api.meta/netzero_api/
      - type: OpenAPI
        url: openapi/salesforce-net-zero-cloud-rest-api-openapi.yml
      - type: Authentication
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
      - type: Rate Limits
        url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/
    contact:
      - type: Support
        url: https://help.salesforce.com/
  - name: Carbon Accounting API
    description: API endpoints for carbon footprint calculations, emission factors, and sustainability metrics aggregation. Enables retrieval of emission factors and calculation of CO2e from activity data.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.netzero_api.meta/netzero_api/
    baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
    tags:
      - Carbon Accounting
      - Emission Factors
      - Footprint Calculation
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.netzero_api.meta/netzero_api/
  - name: Sustainability Data API
    description: API for accessing and managing sustainability data including energy consumption, waste management, water usage, and renewable energy tracking.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.netzero_api.meta/netzero_api/
    baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
    tags:
      - Energy Consumption
      - Sustainability Data
      - Waste Management
      - Water Usage
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.netzero_api.meta/netzero_api/
common:
  - type: Developer Portal
    url: https://developer.salesforce.com/
  - type: Getting Started
    url: https://trailhead.salesforce.com/content/learn/modules/net-zero-cloud-basics
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  - type: Status
    url: https://status.salesforce.com/
  - type: Terms of Service
    url: https://www.salesforce.com/company/legal/agreements/
  - type: Privacy Policy
    url: https://www.salesforce.com/company/privacy/
  - type: Trailhead Learning
    url: https://trailhead.salesforce.com/content/learn/trails/get-started-with-net-zero-cloud
  - type: Release Notes
    url: https://help.salesforce.com/s/articleView?id=release-notes.salesforce_release_notes.htm
  - type: Support
    url: https://help.salesforce.com/
  - type: GitHub Organization
    url: https://github.com/salesforce
  - type: Spectral Rules
    url: rules/salesforce-net-zero-cloud-rules.yml
  - type: Capabilities
    url: capabilities/carbon-accounting.yaml
  - type: JSON Schema
    url: json-schema/salesforce-net-zero-cloud-carbon-emission-schema.json
    title: Carbon Emission Schema
  - type: JSON Schema
    url: json-schema/salesforce-net-zero-cloud-sustainability-goal-schema.json
    title: Sustainability Goal Schema
  - type: JSON-LD Context
    url: json-ld/salesforce-net-zero-cloud-context.jsonld
  - type: Vocabulary
    url: vocabulary/salesforce-net-zero-cloud-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include: []
---
