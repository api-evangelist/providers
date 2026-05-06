---
aid: google-data-studio
name: Google Data Studio
description: Google Data Studio, now rebranded as Looker Studio, is a free data visualization and business intelligence tool from Google that transforms data into customizable, shareable dashboards and reports. It connects to a wide range of data sources and supports community connectors and visualizations for extensibility.
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
url: https://lookerstudio.google.com
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Analytics
  - Business Intelligence
  - Dashboards
  - Data
  - Reporting
  - Visualization
apis:
  - name: Google Data Studio API
    description: The Looker Studio API enables programmatic management of Looker Studio assets, including searching for assets and managing permissions within Google Workspace or Cloud Identity organizations.
    image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
    humanURL: https://developers.google.com/looker-studio/integrate/api
    baseURL: https://datastudio.googleapis.com
    tags:
      - Assets
      - Data Sources
      - Permissions
      - Reports
    properties:
      - type: Documentation
        url: https://developers.google.com/looker-studio/integrate/api
      - type: OpenAPI
        url: openapi/google-data-studio-api-openapi.yml
      - type: OpenAPI
        url: https://datastudio.googleapis.com/$discovery/rest?version=v1
      - type: Reference
        url: https://developers.google.com/looker-studio/integrate/api/reference
      - type: Authentication
        url: https://developers.google.com/looker-studio/integrate/api
      - type: Change Log
        url: https://developers.google.com/looker-studio/integrate/api/changelog
  - name: Looker Studio Linking API
    description: The Linking API provides a reliable interface to configure and forward users directly to a pre-configured Looker Studio report via URL parameters, enabling one-click report creation experiences.
    image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
    humanURL: https://developers.google.com/looker-studio/integrate/linking-api
    tags:
      - Embedding
      - Integration
      - Linking
      - Reports
    properties:
      - type: Documentation
        url: https://developers.google.com/looker-studio/integrate/linking-api
      - type: OpenAPI
        url: openapi/google-data-studio-linking-api-openapi.yml
  - name: Looker Studio Community Connectors
    description: Community Connectors enable direct connections from Looker Studio to any internet-accessible data source using Google Apps Script. Developers implement getAuthType, getConfig, getSchema, and getData functions to build custom connectors.
    image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
    humanURL: https://developers.google.com/looker-studio/connector
    tags:
      - Apps Script
      - Connectors
      - Data Sources
      - Integration
    properties:
      - type: Documentation
        url: https://developers.google.com/looker-studio/connector
      - type: Reference
        url: https://developers.google.com/looker-studio/connector/reference
      - type: Getting Started
        url: https://developers.google.com/looker-studio/connector/build
      - type: Change Log
        url: https://developers.google.com/looker-studio/connector/changelog
      - type: Codelabs
        url: https://codelabs.developers.google.com/codelabs/community-connectors
  - name: Looker Studio Community Visualizations
    description: Community Visualizations allow developers to build and share custom JavaScript visualizations in Looker Studio using the dscc helper library, extending the platform with custom chart types and visual components.
    image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
    humanURL: https://developers.google.com/looker-studio/visualization
    tags:
      - Charts
      - Custom Components
      - JavaScript
      - Visualizations
    properties:
      - type: Documentation
        url: https://developers.google.com/looker-studio/visualization
      - type: Getting Started
        url: https://developers.google.com/looker-studio/visualization/get-started
      - type: Reference
        url: https://developers.google.com/looker-studio/visualization/library-reference
      - type: Libraries
        url: https://developers.google.com/looker-studio/visualization/library
      - type: Codelabs
        url: https://codelabs.developers.google.com/codelabs/community-visualization
      - type: Open Source
        url: https://developers.google.com/looker-studio/visualization/open-source
common:
  - type: OpenAPI
    url: openapi/google-data-studio-api-openapi.yml
  - type: OpenAPI
    url: openapi/google-data-studio-linking-api-openapi.yml
  - type: JSON Schema
    url: json-schema/google-data-studio-asset-schema.json
  - type: JSON Schema
    url: json-schema/google-data-studio-permissions-schema.json
  - type: JSON Schema
    url: json-schema/google-data-studio-connector-schema.json
  - type: JSON Schema
    url: json-schema/google-data-studio-report-schema.json
  - type: JSON Schema
    url: json-schema/google-data-studio-datasource-schema.json
  - type: JSON-LD
    url: json-ld/google-data-studio-context.jsonld
  - type: Portal
    url: https://lookerstudio.google.com
  - type: Documentation
    url: https://docs.cloud.google.com/looker/docs/studio
  - type: Getting Started
    url: https://support.google.com/looker-studio/answer/6283323
  - type: Authentication
    url: https://developers.google.com/looker-studio/integrate/api
  - type: Blog
    url: https://cloud.google.com/blog/products/data-analytics
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://support.google.com/looker-studio
  - type: Terms of Service
    url: https://support.google.com/looker-studio/answer/7019158
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: GitHub Organization
    url: https://github.com/looker-open-source
  - type: Community
    url: https://www.googlecloudcommunity.com/gc/Looker-Studio/bd-p/looker-studio
  - type: Gallery
    url: https://lookerstudio.google.com/gallery
  - type: Change Log
    url: https://docs.cloud.google.com/looker-studio/docs/release-notes
  - type: Pricing
    url: https://cloud.google.com/looker/pricing
  - type: Website
    url: https://cloud.google.com/looker-studio
  - type: Login
    url: https://lookerstudio.google.com/?requirelogin=1
  - type: Sign Up
    url: https://lookerstudio.google.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
