---
aid: bonneville-power-administration
name: Bonneville Power Administration
description: The Bonneville Power Administration (BPA) is a federal agency within the U.S. Department of Energy that markets wholesale electrical power from federal hydroelectric projects in the Pacific Northwest. BPA also operates and maintains about three-quarters of the high-voltage transmission in the Pacific Northwest. The agency provides publicly available GIS data, energy statistics, and operational data through its data hub and web services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bonneville-power-administration/refs/heads/main/apis.yml
created: '2024-11-25'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Energy
  - Federal Government
  - GIS
  - Hydroelectric
  - Pacific Northwest
  - Power
  - Transmission
  - Wind
apis:
  - aid: bonneville-power-administration:gis-data-api
    name: BPA GIS Data Hub API
    tags:
      - ArcGIS
      - GeoServices
      - GIS
      - Government
      - Geospatial
      - WFS
      - WMS
    humanURL: https://data-bpagis.hub.arcgis.com
    properties:
      - url: https://data-bpagis.hub.arcgis.com
        type: Documentation
      - url: https://data-bpagis.hub.arcgis.com/datasets/998ba568128d46c0a38e285235b55d0c_0/geoservice
        type: GeoService
    description: The BPA GIS Data Hub provides publicly available geospatial data from Bonneville Power Administration. The hub is built on ArcGIS and supports data downloads in multiple formats including CSV, KML, GeoJSON, GeoTIFF, and PNG. Developer API access is available through GeoServices (ArcGIS REST API), WMS (Web Map Service), and WFS (Web Feature Service) endpoints. Datasets include BPA service area boundaries, transmission infrastructure, and energy facility data.
  - aid: bonneville-power-administration:wind-solar-data
    name: BPA Wind and Solar Generation Data
    tags:
      - Energy
      - Government
      - Renewable Energy
      - Solar
      - Statistics
      - Wind
    humanURL: https://transmission.bpa.gov/business/operations/Wind/
    properties:
      - url: https://transmission.bpa.gov/business/operations/Wind/
        type: Documentation
      - url: https://transmission.bpa.gov/business/operations/Wind/twndbspt.aspx
        type: DataAPI
    description: BPA publishes real-time and historical wind and solar generation data for the Balancing Authority area. Data includes total wind generation, total solar generation, net generation, and load data available for download. The data is used for grid operations planning and renewable energy tracking.
common:
  - type: Website
    url: https://www.bpa.gov
  - type: About
    url: https://www.bpa.gov/about/
  - type: OpenData
    url: https://data-bpagis.hub.arcgis.com
  - type: DataDownload
    url: https://transmission.bpa.gov/business/operations/Wind/
  - type: CustomerPortal
    url: https://www.bpa.gov/energy-and-services/
  - type: Contact
    url: https://www.bpa.gov/about/contact/
  - name: Use Cases
    type: UseCases
    data:
      - name: GIS Data Analysis
        url: https://data-bpagis.hub.arcgis.com
        features:
          - Geospatial Data Download
          - Map Visualization
          - Service Area Data
          - Transmission Infrastructure Mapping
          - Energy Facility Locations
      - name: Renewable Energy Monitoring
        url: https://transmission.bpa.gov/business/operations/Wind/
        features:
          - Wind Generation Data
          - Solar Generation Data
          - Real-Time Generation Monitoring
          - Historical Data Access
          - Grid Load Tracking
      - name: Transmission System Monitoring
        url: https://www.bpa.gov/energy-and-services/transmission/
        features:
          - Transmission Availability
          - Hourly Firm Data
          - System Load Monitoring
          - Grid Operations Data
  - name: Features
    type: Features
    data:
      - name: GeoServices API
        url: https://data-bpagis.hub.arcgis.com
        features:
          - ArcGIS REST API
          - GeoJSON Export
          - CSV Export
          - KML Export
          - GeoTIFF Export
          - Web Map Service (WMS)
          - Web Feature Service (WFS)
      - name: Open Data Downloads
        url: https://data-bpagis.hub.arcgis.com
        features:
          - CSV Download
          - JSON Download
          - GeoJSON Download
          - Shapefile Download
          - KML Download
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
