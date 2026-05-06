---
aid: thermo-fisher-scientific
url: https://raw.githubusercontent.com/api-evangelist/thermo-fisher-scientific/refs/heads/main/apis.yml
apis:
  - aid: thermo-fisher-scientific:samplemanager-lims
    name: Thermo Fisher SampleManager LIMS REST API
    tags:
      - LIMS
      - Laboratory
      - Life Sciences
      - Sample Management
      - REST API
    humanURL: https://www.thermofisher.com/us/en/home/digital-solutions/lab-informatics/lab-information-management-systems-lims/solutions/samplemanager.html
    baseURL: https://{your-server}:{port}/smpwcfrestvgsm
    properties:
      - url: https://www.thermofisher.com/us/en/home/digital-solutions/lab-informatics/lab-information-management-systems-lims/solutions/samplemanager.html
        type: Documentation
      - url: openapi/thermo-fisher-samplemanager-openapi.yml
        type: OpenAPI
    description: The Thermo Scientific SampleManager LIMS REST API enables secure connection between software applications and the SampleManager LIMS system for simplified data exchange. Provides access to sample data, workflows, entities, results, and laboratory operations. Runs on port 56105 and supports token authentication.
  - aid: thermo-fisher-scientific:nanodrop-ultra
    name: Thermo Fisher NanoDrop Ultra Web API
    tags:
      - Spectrophotometry
      - Laboratory Instruments
      - Life Sciences
      - REST API
      - UV-Vis
    humanURL: https://documents.thermofisher.com/TFS-Assets/CAD/manuals/nanodrop-ultra-api-reference-manual-m024.pdf
    baseURL: https://{nanodrop-instrument-ip}
    properties:
      - url: https://documents.thermofisher.com/TFS-Assets/CAD/manuals/nanodrop-ultra-api-reference-manual-m024.pdf
        type: Documentation
      - url: openapi/thermo-fisher-nanodrop-openapi.yml
        type: OpenAPI
    description: The Thermo Scientific NanoDrop Ultra Web API provides RESTful access to instrument control and data export for the NanoDrop Ultra microvolume UV-Vis spectrophotometer. Enables laboratory informatics integration, automated measurement workflows, and data retrieval from the instrument.
  - aid: thermo-fisher-scientific:connect-platform
    name: Thermo Fisher Connect Platform OData API
    tags:
      - Platform
      - OData
      - Laboratory
      - Life Sciences
      - Integration
    humanURL: https://www.thermofisher.com/us/en/home/digital-science/thermo-fisher-connect.html
    baseURL: https://api.thermofisher.com
    properties:
      - url: https://www.thermofisher.com/blog/connectedlab/platform-for-science-developer-portal-beta/
        type: Documentation
    description: The Thermo Fisher Connect Platform OData API provides standards-based interoperability for laboratory data management, enabling integration between instruments, LIMS, ELN, and enterprise systems through the OData REST protocol.
name: Thermo Fisher Scientific
tags:
  - Life Sciences
  - Laboratory
  - Scientific Instruments
  - LIMS
  - Diagnostics
  - Biosciences
  - Fortune 500
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-21'
modified: '2026-05-03'
position: Consuming
description: Thermo Fisher Scientific is the world leader in serving science, providing analytical instruments, life sciences solutions, specialty diagnostics, laboratory products, and biopharma services. Developer APIs enable laboratory automation, instrument control, LIMS integration, and data management across life science workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Thermo Fisher Scientific Website
    url: https://www.thermofisher.com
    type: Website
  - name: Thermo Fisher Connect Platform
    url: https://www.thermofisher.com/us/en/home/digital-science/thermo-fisher-connect.html
    type: Documentation
  - name: Connected Lab Blog
    url: https://www.thermofisher.com/blog/connectedlab/
    type: Blog
  - name: Developer Portal (Beta)
    url: https://www.thermofisher.com/blog/connectedlab/platform-for-science-developer-portal-beta/
    type: Documentation
  - name: Instrument API GitHub
    url: https://github.com/thermofisherlsms/iapi
    type: GitHubRepository
  - name: GitHub Organization
    url: https://github.com/thermofisherlsms
    type: GitHubOrganization
---
