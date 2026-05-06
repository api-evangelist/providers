---
aid: americorps
url: https://raw.githubusercontent.com/api-evangelist/americorps/refs/heads/main/apis.yml
name: AmeriCorps
description: AmeriCorps is a federal agency that engages millions of Americans in service to their communities through programs including AmeriCorps State and National, AmeriCorps VISTA, AmeriCorps NCCC, AmeriCorps Seniors, and the Volunteer Generation Fund. Established in 1993 under the Corporation for National and Community Service (CNCS), AmeriCorps addresses critical community needs in education, disaster response, environmental conservation, economic opportunity, and healthy futures. The agency operates the AmeriCorps Open Data portal (data.americorps.gov) providing programmatic access to research, evaluation, and program data via the Socrata Open Data API (SODA).
tags:
  - Federal Government
  - National Service
  - Volunteerism
  - Community Development
  - Civic Engagement
  - Education
  - Disaster Response
  - Environmental Conservation
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
apis:
  - aid: americorps:americorps-open-data-soda-api
    name: AmeriCorps Open Data SODA API
    tags:
      - Open Data
      - Research
      - Evaluation
      - National Service
    humanURL: https://data.americorps.gov
    baseURL: https://data.americorps.gov/resource
    properties:
      - url: https://data.americorps.gov
        type: Documentation
      - url: https://data.americorps.gov/api/views
        type: DataAPI
    description: The AmeriCorps Open Data portal provides programmatic access to AmeriCorps research, evaluation, and program datasets via the Socrata Open Data API (SODA). The portal includes datasets on program outcomes, member experiences, return on investment studies, evidence snapshots for each AmeriCorps program, and evaluation reports. Data is available in JSON, CSV, XML, and RDF formats, with OData endpoints for connecting to tools like Excel and Tableau.
common:
  - type: Website
    url: https://americorps.gov
  - type: Portal
    url: https://data.americorps.gov
    name: AmeriCorps Open Data Portal
  - type: DataAPI
    url: https://data.americorps.gov/api/views
    name: SODA Dataset Discovery Endpoint
  - type: GettingStarted
    url: https://dev.socrata.com/docs/endpoints.html
    name: Socrata SODA API Documentation
  - type: GitHubOrganization
    url: https://github.com/americorps
    name: AmeriCorps GitHub
  - type: Features
    data:
      - name: AmeriCorps State and National
        description: Program engaging more than 75,000 Americans in intensive service through nonprofits, schools, public agencies, and community organizations addressing critical needs across all 50 states.
      - name: AmeriCorps VISTA
        description: Volunteers in Service to America (VISTA) program placing members with nonprofits and public agencies to build capacity and fight poverty.
      - name: AmeriCorps NCCC
        description: National Civilian Community Corps residential service program for young adults completing team-based service projects on environmental and disaster relief efforts.
      - name: AmeriCorps Seniors
        description: Programs engaging adults 55 and older in volunteer service through RSVP, Foster Grandparents, and Senior Companions programs.
      - name: Evidence Exchange Open Data
        description: Research and evaluation data portal (data.americorps.gov) providing SODA API access to program effectiveness studies, member outcome data, and ROI analyses.
      - name: Volunteer Generation Fund
        description: Grant program supporting organizations that recruit, manage, and support volunteers to meet critical community needs.
  - type: UseCases
    data:
      - name: Program Evaluation Research
        description: Accessing AmeriCorps program evaluation reports and impact data via the SODA API to conduct independent research on national service effectiveness.
      - name: Grant Management and Reporting
        description: Partners and grantees accessing program data and reporting resources to manage AmeriCorps grants and measure member outcomes.
      - name: Volunteer Engagement Analytics
        description: Analyzing volunteer engagement patterns, member satisfaction data, and civic participation trends using AmeriCorps open datasets.
      - name: Policy and Advocacy Research
        description: Accessing return-on-investment studies, evidence snapshots, and program outcome data to support policy development and advocacy for national service.
  - type: Integrations
    data:
      - name: Socrata Open Data API
        description: Standard Socrata SODA API integration enabling applications to query, filter, and aggregate AmeriCorps program data programmatically.
      - name: OData Endpoints
        description: OData V2 and V4 endpoints enabling connection to Microsoft Excel, Tableau, Power BI, and other business intelligence tools.
      - name: eGrants Grant Management System
        description: AmeriCorps eGrants system for grantee organizations to submit applications, manage awards, and report on AmeriCorps program activities.
created: '2024-11-21'
modified: '2026-04-19'
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
