---
aid: appalachian-regional-commission
url: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/apis.yml
name: Appalachian Regional Commission
tags:
  - Appalachia
  - Economic Development
  - Federal Government
  - Government
  - Infrastructure
  - Regional Development
  - Workforce Development
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21'
modified: '2026-04-19'
position: Consuming
description: The Appalachian Regional Commission (ARC) is a federal-state partnership that invests in Appalachia's economic future by funding projects that promote economic development, infrastructure improvement, workforce training, and community development across 423 counties in 13 states. ARC provides research data, county-level economic reports, and maps via its Data Report Tool at data.arc.gov.
apis:
  - aid: appalachian-regional-commission:arc-data-reports
    name: ARC Data Report Tool
    description: The ARC Data Report Tool provides state- and county-level data for the entire Appalachian Region across six topic areas comparing Appalachian data with national averages. Data covers economic, demographic, and quality-of-life factors including income, poverty, unemployment, education, and health metrics. Reports are available for every Appalachian state and county.
    humanURL: https://data.arc.gov/data
    tags:
      - County Data
      - Demographics
      - Economic Data
      - Open Data
      - Regional Data
    properties:
      - type: Documentation
        url: https://www.arc.gov/research-and-data/
      - type: Portal
        url: https://data.arc.gov/data
common:
  - type: Documentation
    url: https://www.arc.gov/research-and-data/
  - type: Portal
    url: https://data.arc.gov/data
  - type: Features
    data:
      - name: County-Level Data Reports
        description: State and county-level data reports for all 423 Appalachian counties across six topic areas.
      - name: Regional Comparison Data
        description: Appalachian Region data compared against national averages for benchmarking.
      - name: Research Reports
        description: Regular research publications addressing socioeconomic issues in the Appalachian Region.
      - name: Maps
        description: Geographic mapping data and visualizations covering the Appalachian Region.
      - name: Grant Program Data
        description: Data on ARC's investment portfolios, grants, and program evaluations.
  - type: UseCases
    data:
      - name: Economic Research
        description: Access county-level economic, demographic, and quality-of-life data for Appalachian research.
      - name: Grant Program Analysis
        description: Evaluate ARC investment portfolios and grant outcomes across the Appalachian Region.
      - name: Policy Development
        description: Use regional data to inform economic development and infrastructure policy decisions.
      - name: Community Development Planning
        description: Access local data to support community-level economic development planning.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
