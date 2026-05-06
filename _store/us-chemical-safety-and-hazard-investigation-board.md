---
aid: us-chemical-safety-and-hazard-investigation-board
name: US Chemical Safety and Hazard Investigation Board
description: The US Chemical Safety and Hazard Investigation Board (CSB) is an independent federal agency responsible for investigating chemical accidents and hazards across the United States. The board conducts thorough investigations into incidents involving the release of hazardous chemicals, explosions, fires, and other accidents that pose a threat to public safety and the environment. The CSB publishes investigation reports, safety recommendations, and incident data, and maintains a public database of completed investigations and safety recommendations. While no formal public API is available, the CSB makes incident data available through its website and periodic compiled reports under its Accidental Release Reporting Rule transparency initiative.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Chemical Safety
  - Incident Investigation
  - Hazardous Materials
  - Public Safety
  - Environmental Safety
created: '2024-12-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/us-chemical-safety-and-hazard-investigation-board/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: us-chemical-safety-and-hazard-investigation-board:us-chemical-safety-and-hazard-investigation-board
    name: US Chemical Safety and Hazard Investigation Board
    description: The CSB does not currently offer a formal public API. However, it maintains public databases of investigations, recommendations, and incident reports accessible through its website. The CSB releases periodic volumes of compiled incident reports under its Accidental Release Reporting Rule, and maintains a recommendations database with status tracking for over 1,000 safety recommendations issued to industry and regulatory agencies.
    humanURL: https://www.csb.gov
    tags:
      - Federal Government
      - Chemical Safety
      - Incident Investigation
      - Hazardous Materials
      - Public Safety
      - Environmental Safety
    properties:
      - type: Documentation
        url: https://www.csb.gov
      - type: Website
        url: https://www.csb.gov
      - type: Investigations
        url: https://www.csb.gov/investigations/
      - type: CompletedInvestigations
        url: https://www.csb.gov/investigations/completed-investigations/
      - type: Recommendations
        url: https://www.csb.gov/recommendations/
      - type: Documents
        url: https://www.csb.gov/documents/
      - type: IncidentReports
        url: https://www.csb.gov/csb-releases-volume-4-of-incident-reports/
      - type: FOIA
        url: https://www.foia.gov/agency-search.html?id=7afb6c7b-57be-49e4-b04a-0f3d06917b0c&type=component
features:
  - name: Investigation Database
    description: Searchable database of current and completed chemical accident investigations
  - name: Recommendations Database
    description: Database of over 1,000 safety recommendations with open/closed status tracking
  - name: Incident Reports
    description: Periodic compilations of incidents reported under the Accidental Release Reporting Rule
  - name: Safety Videos
    description: Animated and documentary safety videos illustrating accident causes
  - name: Investigation Reports
    description: Full investigation reports with root cause analysis and recommendations
  - name: FOIA Access
    description: Freedom of Information Act requests for agency records
useCases:
  - name: Chemical Safety Research
    description: Research chemical accident patterns, root causes, and contributing factors
  - name: Regulatory Compliance
    description: Review CSB recommendations to industry and regulatory agencies for compliance guidance
  - name: Safety Training
    description: Use CSB investigation reports and videos for industrial safety training
  - name: Policy Analysis
    description: Analyze recommendations and their status for chemical safety policy development
  - name: Incident Reporting
    description: Submit reports of chemical releases under the Accidental Release Reporting Rule
solutions:
  - name: Process Safety Management
    description: Support process safety management programs with CSB investigation findings
  - name: Hazard Analysis
    description: Inform process hazard analyses with lessons learned from CSB investigations
integrations:
  - name: PubChem
    description: CSB is a data source for PubChem chemical safety data
    url: https://pubchem.ncbi.nlm.nih.gov/source/U.S.%20Chemical%20Safety%20and%20Hazard%20Investigation%20Board%20(CSB)
  - name: Federal Register
    description: CSB rulemakings and regulatory notices published in the Federal Register
    url: https://www.federalregister.gov/agencies/chemical-safety-and-hazard-investigation-board
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
