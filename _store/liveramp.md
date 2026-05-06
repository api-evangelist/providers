---
aid: liveramp
name: LiveRamp
description: LiveRamp is a data connectivity platform that enables enterprises to safely connect, control, and activate first-party customer data across the digital ecosystem. Their developer platform exposes a suite of REST APIs for identity resolution, data activation, clean-room collaboration, marketplace data access, and privacy-first authenticated traffic.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Connectivity
  - Identity Resolution
  - Activation
  - Clean Room
  - Privacy
  - AdTech
url: https://raw.githubusercontent.com/api-evangelist/liveramp/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: liveramp:activation-api
    name: LiveRamp Activation API
    description: Programmatic activation of first-party and marketplace data across destination partners and connected platforms in the LiveRamp network.
    humanURL: https://developers.liveramp.com/activation-api
    tags:
      - Activation
      - AdTech
      - Marketing
    properties:
      - type: Documentation
        url: https://developers.liveramp.com/activation-api
  - aid: liveramp:ats-api
    name: LiveRamp Authenticated Traffic Solution (ATS) API
    description: Privacy-first, PII-based authentication API enabling programmatic addressability without third-party cookies via RampID envelopes.
    humanURL: https://developers.liveramp.com/authenticatedtraffic-api
    tags:
      - Identity
      - Privacy
      - Authentication
    properties:
      - type: Documentation
        url: https://developers.liveramp.com/authenticatedtraffic-api
  - aid: liveramp:clean-room-api
    name: LiveRamp Clean Room API
    description: API for setting up and managing clean rooms, data sources, and collaborative analytics queries between data partners.
    humanURL: https://developers.liveramp.com/clean-room-api
    tags:
      - Clean Room
      - Data Collaboration
      - Privacy
    properties:
      - type: Documentation
        url: https://developers.liveramp.com/clean-room-api
  - aid: liveramp:datamarketplace-buyer-api
    name: LiveRamp Data Marketplace Buyer API
    description: API enabling platforms to host third-party segments from the LiveRamp Data Marketplace and access detailed segment metadata.
    humanURL: https://developers.liveramp.com/datamarketplace-buyer-api
    tags:
      - Data Marketplace
      - Segments
      - AdTech
    properties:
      - type: Documentation
        url: https://developers.liveramp.com/datamarketplace-buyer-api
  - aid: liveramp:abilitec-api
    name: LiveRamp AbiliTec API
    description: Identity resolution API that resolves offline PII data into stable AbiliTec links for enterprise customer-database unification.
    humanURL: https://developers.liveramp.com/abilitec-api
    tags:
      - Identity
      - Resolution
      - PII
    properties:
      - type: Documentation
        url: https://developers.liveramp.com/abilitec-api
  - aid: liveramp:rampid-api
    name: LiveRamp RampID API
    description: API for matching data to the LiveRamp Identity Graph, including envelope decryption and translation between pseudonymous identifiers.
    humanURL: https://developers.liveramp.com/rampid-api
    tags:
      - Identity
      - RampID
      - Pseudonymous
    properties:
      - type: Documentation
        url: https://developers.liveramp.com/rampid-api
  - aid: liveramp:job-management-api
    name: LiveRamp Safe Haven Job Management API
    description: Automates Python, PySpark, and BigQuery jobs running in LiveRamp's Safe Haven Analytics Environment.
    humanURL: https://developers.liveramp.com/ae-job-management-api
    tags:
      - Analytics
      - Automation
      - Jobs
    properties:
      - type: Documentation
        url: https://developers.liveramp.com/ae-job-management-api
  - aid: liveramp:privacy-api
    name: LiveRamp Privacy API
    description: Automates data subject requests including opt-outs, deletions, and consent updates across the LiveRamp ecosystem.
    humanURL: https://developers.liveramp.com/privacy-api
    tags:
      - Privacy
      - Consent
      - Compliance
    properties:
      - type: Documentation
        url: https://developers.liveramp.com/privacy-api
  - aid: liveramp:sidecar
    name: LiveRamp Sidecar
    description: Service enabling SSPs to decrypt RampID identity envelopes into DSP-specific identifiers for programmatic activation.
    humanURL: https://sidecar.readme.io/
    tags:
      - SSP
      - Programmatic
      - Identity
    properties:
      - type: Documentation
        url: https://sidecar.readme.io/
common:
  - type: Website
    url: https://liveramp.com
  - type: Portal
    url: https://developers.liveramp.com/
  - type: Documentation
    url: https://docs.liveramp.com/
  - type: SupportPortal
    url: https://support.liveramp.com/
  - type: Blog
    url: https://liveramp.com/blog/
  - type: GitHubOrganization
    url: https://github.com/LiveRamp
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
