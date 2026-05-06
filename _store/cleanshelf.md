---
aid: cleanshelf
name: Cleanshelf
url: https://raw.githubusercontent.com/api-evangelist/cleanshelf/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
status: Acquired
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Acquired
  - License Management
  - SaaS Management
  - Shadow IT
  - SMP
  - Software Asset Management
  - Spend Optimization
description: Cleanshelf was a SaaS management platform that helped enterprises discover and inventory their SaaS applications, optimize software licenses, track spend, and surface shadow IT. Cleanshelf was acquired by Zylo in 2021 and its capabilities have been folded into the Zylo enterprise SaaS spend optimization platform. The Cleanshelf product brand and standalone API are no longer maintained; equivalent programmatic capabilities are now exposed through the Zylo Developer Hub at developer.zylo.com.
apis:
  - aid: cleanshelf:zylo-api
    name: Zylo Platform API (successor)
    tags:
      - License Management
      - SaaS Management
      - Spend
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.zylo.com/
    properties:
      - url: https://developer.zylo.com/
        type: Documentation
      - url: https://developer.zylo.com/reference
        type: API Reference
    description: The Zylo Platform API is the successor to Cleanshelf. It exposes SaaS application discovery, inventory, license, contract, and spend data so enterprises can integrate Zylo with finance, procurement, and IT systems. A legacy v1.0 API remains documented for older Cleanshelf-era integrations.
  - aid: cleanshelf:zylo-legacy-api
    name: Zylo Legacy API (Cleanshelf-era)
    tags:
      - Cleanshelf
      - Legacy
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.zylo.com/v1.0/reference/zylo-legacy-api
    properties:
      - url: https://developer.zylo.com/v1.0/reference/zylo-legacy-api
        type: Documentation
    description: Legacy v1.0 endpoints retained from the original Cleanshelf product line. New integrations should use the modern Zylo Platform API.
common:
  - type: Website
    url: https://zylo.com/
  - type: Acquirer
    url: https://zylo.com/
  - type: Acquisition Announcement
    url: https://zylo.com/news/zylo-acquires-cleanshelf/
  - type: Application
    url: https://app.zylo.com/
  - type: Portal
    url: https://developer.zylo.com/
  - type: Privacy Policy
    url: https://zylo.com/privacy-policy/
  - type: Terms of Service
    url: https://zylo.com/legal/
  - type: Support
    url: https://help.zylo.com/
  - type: JSON-LD
    url: json-ld/cleanshelf-context.jsonld
  - type: Spectral
    url: rules/cleanshelf-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cleanshelf-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
