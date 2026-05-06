---
aid: asce-amplify
url: https://raw.githubusercontent.com/api-evangelist/asce-amplify/refs/heads/main/apis.yml
name: ASCE Amplify
tags:
  - Civil Engineering
  - Hazard Data
  - Engineering Standards
  - Infrastructure
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-19'
description: ASCE Amplify is a platform created by the American Society of Civil Engineers (ASCE) that provides civil engineering data and advocacy tools. The platform includes the ASCE Hazard Tool API, which provides a simple interface to query locations in the United States for environmental hazard data by geographic location. The Hazard Tool API covers seismic, wind, snow, ice, flood, and other environmental hazard loads used in structural design per ASCE standards. ASCE Amplify also supports advocacy, connecting civil engineers with elected officials to advocate for infrastructure investment and sustainable practices.
apis:
  - aid: asce-amplify:hazard-tool-api
    name: ASCE Hazard Tool API
    description: The ASCE Hazard Tool API provides a simple interface to query locations in the United States for environmental hazard data by geographic location. It provides site-specific hazard values used in structural engineering design including seismic ground motion parameters, wind speeds, snow loads, ice loads, and flood data in accordance with ASCE 7 and related standards. Access requires an ASCE membership or license.
    humanURL: https://amplify.asce.org/api
    baseURL: https://amplify.asce.org/api
    tags:
      - Civil Engineering
      - Hazard Data
      - Seismic
      - Wind
      - Snow
      - Structural Engineering
    properties:
      - type: Documentation
        url: https://amplify.asce.org/api
      - type: Authentication
        url: https://amplify.asce.org/api
common:
  - type: Portal
    url: https://amplify.asce.org/
    title: ASCE Amplify Platform
  - type: Portal
    url: https://www.asce.org/
    title: ASCE Website
  - type: Features
    data:
      - name: Geographic Hazard Lookup
        description: Query any US location by latitude and longitude or address to retrieve site-specific environmental hazard values for structural design, including ASCE 7 seismic, wind, snow, and ice parameters.
      - name: ASCE 7 Seismic Parameters
        description: Retrieve seismic design parameters including Ss, S1, SMS, SM1, SDS, SD1, and spectral acceleration values per ASCE 7 for any US location.
      - name: Wind Speed Data
        description: Access design wind speed values for various risk categories and exposure categories per ASCE 7 for structural wind load calculations.
      - name: Snow and Ice Load Data
        description: Retrieve ground snow load values and ice storm data for design of roof structures and overhead transmission lines per ASCE 7.
      - name: Civil Engineer Advocacy
        description: Tools for ASCE members to contact elected officials and advocate for infrastructure funding, engineering standards, and professional issues.
  - type: UseCases
    data:
      - name: Structural Design
        description: Structural engineers use the ASCE Hazard Tool API to obtain site-specific hazard parameters for building and infrastructure design in compliance with ASCE 7 and building codes.
      - name: Site Assessment
        description: Civil engineers perform preliminary site assessments for new construction projects by querying multiple locations for hazard comparisons.
      - name: Software Integration
        description: Structural engineering software vendors integrate the ASCE Hazard Tool API to automatically populate design parameters based on project location.
  - type: Integrations
    data:
      - name: ASCE 7 Standards
        description: API values directly correspond to ASCE 7 Minimum Design Loads for Buildings and Other Structures, the primary reference standard for US structural engineering.
      - name: IBC Building Codes
        description: Hazard parameters from the API align with International Building Code requirements that reference ASCE 7 for environmental load design values.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
