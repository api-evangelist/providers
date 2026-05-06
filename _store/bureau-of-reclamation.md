---
aid: bureau-of-reclamation
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-reclamation/refs/heads/main/apis.yml
name: Bureau of Reclamation
tags:
  - Energy
  - Federal Government
  - Infrastructure
  - Water
  - Hydrology
  - Reservoirs
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-30'
modified: '2026-04-23'
position: Consumer
description: Established in 1902, the Bureau of Reclamation is best known for the dams, powerplants, and canals it constructed in the 17 western states. These water projects led to homesteading and promoted the economic development of the West. Reclamation has constructed more than 600 dams and reservoirs including Hoover Dam on the Colorado River and Grand Coulee on the Columbia River.
apis:
  - aid: bureau-of-reclamation:reclamation-information-sharing-environment-rise
    name: Reclamation Information Sharing Environment (RISE) API
    tags:
      - Federal Government
      - Water
      - Hydrology
      - Time Series
    humanURL: https://data.usbr.gov/rise/api
    baseURL: https://data.usbr.gov/rise/api/
    properties:
      - url: https://data.usbr.gov/rise/api
        type: Documentation
      - url: https://data.usbr.gov/
        type: Portal
      - url: https://catalog.data.gov/dataset?organization=usbr-gov
        type: DataAPI
    description: The RISE API allows users to query Bureau of Reclamation water resource data programmatically, returning JSON objects. For Geospatial and File Upload datasets, only metadata can be queried. For time series datasets, both metadata and data can be queried. Data includes hydrometric measurements, reservoir levels, streamflow, and water quality.
    features:
      - Time Series Data
      - Hydrometric Measurements
      - Reservoir Level Data
      - Streamflow Data
      - Water Quality Data
      - Geospatial Metadata
      - JSON Format
      - Paginated Results
    useCases:
      - Water resource planning
      - Drought monitoring
      - Hydroelectric generation analysis
      - Environmental flow studies
      - Water rights management
      - Climate research
    endpoints:
      - path: /catalog-item
        description: Query catalog items
      - path: /catalog-record
        description: Query catalog records
      - path: /location
        description: Query monitoring locations
      - path: /parameter
        description: Query measured parameters
      - path: /result
        description: Query time series results
      - path: /reclamation-region
        description: Query Reclamation regions
      - path: /model-run
        description: Query model run data
common:
  - type: Website
    url: https://www.usbr.gov
  - type: Portal
    url: https://data.usbr.gov/
  - type: Privacy Policy
    url: https://www.usbr.gov/privacy.html
  - type: Data Portal
    url: https://catalog.data.gov/dataset?organization=usbr-gov
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
