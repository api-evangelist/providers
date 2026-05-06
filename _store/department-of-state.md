---
aid: department-of-state
name: Department of State
description: The U.S. Department of State leads U.S. foreign policy, conducts diplomacy with foreign governments, issues U.S. passports and visas, supports U.S. citizens abroad, and publishes country-specific information and travel advisories. The Department does not currently operate a unified developer portal; instead, integrators work from public RSS feeds, web pages, the Foreign Affairs Manual, and references to internal systems (ConsularLookout, eCASE) that are not publicly accessible.
url: https://raw.githubusercontent.com/api-evangelist/department-of-state/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-12-03'
modified: '2026-04-28'
type: Index
position: Consuming
access: 3rd-Party
specificationVersion: '0.20'
tags:
  - Federal Government
  - Foreign Affairs
  - Travel
  - Consular
  - Visas
  - Passports
common:
  - url: https://www.state.gov/
    type: Portal
  - url: https://travel.state.gov/
    type: Portal
  - url: https://fam.state.gov/
    type: Reference
apis:
  - aid: department-of-state:travel-advisories
    name: State Department Travel Advisories
    description: Country-by-country travel advisories (Levels 1-4) issued by the Bureau of Consular Affairs, with RSS distribution.
    humanURL: https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html
    tags:
      - Travel
      - Advisories
      - RSS
    properties:
      - type: Documentation
        url: https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html
      - type: RSS
        url: https://travel.state.gov/_res/rss/TAsTWs.xml
  - aid: department-of-state:country-information
    name: Country Information Pages
    description: Per-country pages covering entry/exit requirements, local laws, safety, health, and U.S. embassy contacts.
    humanURL: https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages.html
    tags:
      - Country
      - Travel
    properties:
      - type: Documentation
        url: https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages.html
  - aid: department-of-state:smart-traveler-enrollment-program
    name: Smart Traveler Enrollment Program (STEP)
    description: Voluntary enrollment system for U.S. citizens traveling or residing abroad to receive embassy alerts.
    humanURL: https://step.state.gov/
    tags:
      - Travel
      - Citizen Services
    properties:
      - type: Documentation
        url: https://step.state.gov/
  - aid: department-of-state:visa-information
    name: U.S. Visa Information
    description: Reference information on nonimmigrant and immigrant visa categories, processing times, and reciprocity schedules.
    humanURL: https://travel.state.gov/content/travel/en/us-visas.html
    tags:
      - Visas
    properties:
      - type: Documentation
        url: https://travel.state.gov/content/travel/en/us-visas.html
      - type: Reference
        url: https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/fees/reciprocity-by-country.html
  - aid: department-of-state:passport-services
    name: U.S. Passport Services
    description: Public-facing passport application, renewal, and status-check resources from the Bureau of Consular Affairs.
    humanURL: https://travel.state.gov/content/travel/en/passports.html
    tags:
      - Passports
    properties:
      - type: Documentation
        url: https://travel.state.gov/content/travel/en/passports.html
      - type: Status
        url: https://travel.state.gov/content/travel/en/passports/need-passport/status.html
  - aid: department-of-state:foreign-affairs-manual
    name: Foreign Affairs Manual (FAM) and Handbook (FAH)
    description: Department-wide policy and procedural manuals issued by the Office of Directives Management.
    humanURL: https://fam.state.gov/
    tags:
      - Policy
      - Reference
    properties:
      - type: Documentation
        url: https://fam.state.gov/
  - aid: department-of-state:consular-lookout-class
    name: ConsularLookout (CLASS)
    description: Government-internal name-check system used during visa and passport adjudication. Referenced here for completeness; no public API.
    humanURL: https://travel.state.gov/content/travel/en/legal/visa-law0.html
    tags:
      - Consular
      - Internal
    properties:
      - type: Reference
        url: https://travel.state.gov/content/travel/en/legal/visa-law0.html
  - aid: department-of-state:ecase
    name: eCASE Enterprise Case Management
    description: State Department-wide enterprise case-management platform. Internal system; referenced here for organizational completeness.
    humanURL: https://www.state.gov/
    tags:
      - Case Management
      - Internal
    properties:
      - type: Reference
        url: https://www.state.gov/
  - aid: department-of-state:state-data-gov
    name: State Department Open Data on data.gov
    description: Public datasets published by the State Department through the federal open-data catalog.
    humanURL: https://catalog.data.gov/dataset?organization=state-gov
    tags:
      - Open Data
    properties:
      - type: Documentation
        url: https://catalog.data.gov/dataset?organization=state-gov
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
