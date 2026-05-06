---
aid: redfin
url: https://raw.githubusercontent.com/api-evangelist/redfin/refs/heads/main/apis.yml
name: Redfin
description: Redfin is a technology-powered real estate brokerage that provides property search, home value estimates, listing details, neighborhood statistics, commute data, and downloadable housing market data across the United States. Their platform exposes a Stingray REST API used by the Redfin website and mobile apps, a GIS CSV Export endpoint for bulk property downloads, and the Redfin Data Center for time-series housing market statistics at national, metro, state, county, city, ZIP code, and neighborhood levels.
tags:
  - CSV Export
  - GIS
  - Home Values
  - Housing Market
  - Listings
  - Property Data
  - Real Estate
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-20'
modified: '2026-05-02'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: redfin:redfin-stingray-api
    name: Redfin Stingray API
    description: The Redfin Stingray API is the internal REST API powering the Redfin website and mobile applications. It provides endpoints for property search, listing details, home value estimates (Redfin Estimate), neighborhood statistics, commute information, and GIS-based map data. Accessible at redfin.com/stingray endpoints and reverse-engineered by the developer community.
    humanURL: https://www.redfin.com
    tags:
      - GIS
      - Home Values
      - Listings
      - Property Data
      - Property Search
      - Real Estate
    properties:
      - type: Documentation
        url: https://github.com/alientechsw/RedfinPlus/blob/master/docs/REDFIN.md
      - type: OpenAPI
        url: openapi/redfin-stingray-api-openapi.yml
      - type: SpectralRules
        url: rules/redfin-rules.yml
      - type: NaftikoCapeability
        url: capabilities/shared/stingray-api.yaml
  - aid: redfin:redfin-gis-csv-api
    name: Redfin GIS CSV Export API
    description: The Redfin GIS CSV Export API provides bulk property data downloads in CSV format. Returns up to 350 property records per request including address, price, beds, baths, square footage, lot size, year built, days on market, property type, and listing status.
    humanURL: https://www.redfin.com
    tags:
      - Bulk Data
      - CSV
      - Export
      - GIS
      - Property Data
      - Real Estate
    properties:
      - type: Documentation
        url: https://github.com/alientechsw/RedfinPlus/blob/master/docs/REDFIN.md
      - type: OpenAPI
        url: openapi/redfin-gis-csv-api-openapi.yml
  - aid: redfin:redfin-data-center
    name: Redfin Data Center
    description: The Redfin Data Center provides downloadable housing market data for metropolitan areas, cities, neighborhoods, and ZIP codes across the United States. Data is available at national, metro, state, county, city, ZIP code, and neighborhood levels. Datasets cover median sale prices, homes sold, new listings, days on market, inventory, and price drops. Files are served as compressed TSV from Amazon S3.
    humanURL: https://www.redfin.com/news/data-center/
    tags:
      - Analytics
      - CSV
      - Housing Market
      - Market Data
      - Real Estate
      - Statistics
    properties:
      - type: Documentation
        url: https://www.redfin.com/news/data-center/
      - type: Documentation
        url: https://support.redfin.com/hc/en-us/articles/360016476931-Downloading-Data
      - type: OpenAPI
        url: openapi/redfin-data-center-openapi.yml
      - type: JSONSchema
        url: json-schema/redfin-market-tracker-schema.json
      - type: JSONSchema
        url: json-schema/redfin-property-schema.json
      - type: JSONLd
        url: json-ld/redfin-context.jsonld
      - type: JSONStructure
        url: json-structure/redfin-property-structure.json
      - type: JSONStructure
        url: json-structure/redfin-market-tracker-structure.json
      - type: NaftikoCapeability
        url: capabilities/shared/data-center.yaml
      - type: Vocabulary
        url: vocabulary/redfin-vocabulary.yml
common:
  - name: Redfin Website
    url: https://www.redfin.com
    type: Website
  - name: Redfin Blog
    url: https://www.redfin.com/news/
    type: Blog
  - name: Redfin Support
    url: https://support.redfin.com
    type: Support
  - name: Redfin Privacy Policy
    url: https://www.redfin.com/about/privacy-policy
    type: PrivacyPolicy
  - name: Redfin Terms of Use
    url: https://www.redfin.com/about/terms-of-use
    type: TermsOfService
  - name: Redfin Login
    url: https://www.redfin.com/login
    type: Login
  - name: Redfin Data Center
    url: https://www.redfin.com/news/data-center/
    type: DataCenter
  - name: Redfin News Room
    url: https://www.redfin.com/news/
    type: News
  - name: Redfin on LinkedIn
    url: https://www.linkedin.com/company/redfin
    type: LinkedIn
  - name: Redfin on X
    url: https://twitter.com/redfin
    type: X
  - name: Redfin Investor Relations
    url: https://investors.redfin.com/
    type: InvestorRelations
  - name: Redfin GitHub
    url: https://github.com/redfin
    type: GitHubOrg
  - name: Redfin Capabilities - Property Research
    url: capabilities/property-research.yaml
    type: NaftikoCapeability
  - name: Redfin Capabilities - Market Analytics
    url: capabilities/market-analytics.yaml
    type: NaftikoCapeability
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
