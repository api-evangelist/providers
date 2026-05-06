---
aid: ice
name: U.S. Immigration and Customs Enforcement (ICE)
description: U.S. Immigration and Customs Enforcement (ICE) is a federal law enforcement agency under the U.S. Department of Homeland Security responsible for enforcing federal immigration and customs laws. ICE does not publish a general-purpose developer API portal, but provides public-facing systems, open data, statistics, and FOIA resources used by researchers, attorneys, journalists, and the public.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Customs Enforcement
  - DHS
  - Federal Government
  - Government
  - Immigration
  - Law Enforcement
  - Open Data
url: https://raw.githubusercontent.com/api-evangelist/ice/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ice:ice-online-detainee-locator-system
    name: ICE Online Detainee Locator System (ODLS)
    description: The Online Detainee Locator System is a public-facing search tool that allows the public to locate detainees currently in ICE custody by A-Number and country of birth, or by biographical information. The system is provided as a web search interface; no public developer API is published.
    humanURL: https://locator.ice.gov/
    tags:
      - Custody
      - Detainee Locator
      - Search
    properties:
      - type: Website
        url: https://locator.ice.gov/
      - type: Documentation
        url: https://www.ice.gov/detain/detention-management
  - aid: ice:ice-ero-statistics
    name: ICE ERO Custody and Enforcement Statistics
    description: Enforcement and Removal Operations (ERO) publishes custody arrest, enforcement, and removal statistics in machine-readable formats (CSV/Excel) at regular reporting cadence. These datasets are published as downloadable files rather than through a versioned developer API.
    humanURL: https://www.ice.gov/statistics
    tags:
      - Enforcement
      - Removals
      - Statistics
    properties:
      - type: Documentation
        url: https://www.ice.gov/statistics
      - type: Reports
        url: https://www.ice.gov/spotlight/statistics
  - aid: ice:ice-foia
    name: ICE FOIA Library
    description: ICE's Freedom of Information Act (FOIA) program provides a public reading room and electronic FOIA library with frequently requested records, policy directives, and data releases. Records are released as documents and bulk data files rather than through a programmatic API.
    humanURL: https://www.ice.gov/foia
    tags:
      - FOIA
      - Public Records
      - Transparency
    properties:
      - type: Documentation
        url: https://www.ice.gov/foia
      - type: Library
        url: https://www.ice.gov/foia/library
      - type: Submit Request
        url: https://www.ice.gov/foia/submit-request
common:
  - type: Website
    url: https://www.ice.gov/
  - type: News
    url: https://www.ice.gov/news/all
  - type: Statistics
    url: https://www.ice.gov/statistics
  - type: FOIA
    url: https://www.ice.gov/foia
  - type: Detainee Locator
    url: https://locator.ice.gov/
  - type: Contact
    url: https://www.ice.gov/contact
  - type: Privacy Policy
    url: https://www.ice.gov/about/privacy
  - type: Open Data
    url: https://www.dhs.gov/data
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
