---
aid: united-states-census-bureau
name: United States Census Bureau
description: The U.S. Census Bureau is the nation's leading provider of quality data about its people and economy. The Census Bureau has been rolling out datasets via APIs, providing programmatic access to demographic, economic, housing, and social statistics. The Census Data API supports queries across datasets including the American Community Survey, Decennial Census, Population Estimates, County Business Patterns, Economic Census, and International Trade, with data available at national, state, county, tract, and block group geographic levels.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/united-states-census-bureau/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Demographics
  - Federal Government
  - Open Data
  - Statistics
  - Economics
  - Population
apis:
  - aid: united-states-census-bureau:census-data-api
    name: Census Data API
    description: The Census Data API provides programmatic access to statistical data from Census Bureau surveys and datasets. Users can query demographic, economic, housing, and social data by geographic level and filter using hundreds of statistical variables. Datasets include the American Community Survey (ACS), Decennial Census, Population Estimates, County Business Patterns, Economic Census, International Trade, and more.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.census.gov/data/developers.html
    baseURL: https://api.census.gov/data
    tags:
      - Demographics
      - Statistics
      - Open Data
      - REST API
    properties:
      - type: Documentation
        url: https://www.census.gov/data/developers.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/united-states-census-bureau/refs/heads/main/openapi/census-data-api-openapi.yml
      - type: APIKeySignup
        url: https://api.census.gov/data/key_signup.html
      - type: DataSets
        url: https://www.census.gov/data/developers/data-sets.html
      - type: DiscoveryTool
        url: https://www.census.gov/data/developers/updates/new-discovery-tool.html
      - type: UserGuide
        url: https://www.census.gov/data/developers/guidance/api-user-guide.html
      - type: ExampleQueries
        url: https://www.census.gov/data/developers/guidance/api-user-guide/example-api-queries.html
  - aid: united-states-census-bureau:tigerweb-rest-api
    name: TIGERweb GeoServices REST API
    description: The TIGERweb GeoServices REST API provides access to Census Bureau geographic data including boundaries for states, counties, census tracts, block groups, and other geographic entities. Supports standard ArcGIS REST API queries for geographic features.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://tigerweb.geo.census.gov/tigerwebmain/TIGERweb_main.html
    baseURL: https://tigerweb.geo.census.gov/arcgis/rest/services
    tags:
      - Geography
      - GIS
      - Boundaries
      - Mapping
    properties:
      - type: Documentation
        url: https://tigerweb.geo.census.gov/tigerwebmain/TIGERweb_main.html
  - aid: united-states-census-bureau:geocoding-api
    name: Census Geocoding Services
    description: The Census Geocoding Services convert addresses to geographic coordinates and census geography identifiers. Supports both single-address lookups and batch geocoding for large address lists.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://geocoding.geo.census.gov/geocoder/
    baseURL: https://geocoding.geo.census.gov/geocoder
    tags:
      - Geocoding
      - Geography
      - Address
    properties:
      - type: Documentation
        url: https://geocoding.geo.census.gov/geocoder/
      - type: BatchGeocoding
        url: https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html
common:
  - type: Website
    url: https://www.census.gov/
  - type: DeveloperPortal
    url: https://www.census.gov/data/developers.html
  - type: APIKeySignup
    url: https://api.census.gov/data/key_signup.html
  - type: DataExplorer
    url: https://data.census.gov/
  - type: GitHub
    url: https://github.com/uscensusbureau
  - type: Forum
    url: https://apiforum.uscensusbureau.com/
  - type: Newsletter
    url: https://public.govdelivery.com/accounts/USCENSUS/subscriber/new?topic_id=USCENSUS_11933
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
