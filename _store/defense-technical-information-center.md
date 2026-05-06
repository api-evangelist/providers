---
aid: defense-technical-information-center
name: Defense Technical Information Center
description: The Defense Technical Information Center (DTIC) is the U.S. Department of Defense field activity that acquires, manages, and disseminates scientific and technical information from DoD-funded research, development, test, and evaluation. DTIC operates a public Research and Engineering (R&E) Gateway, the Discover service for searching technical reports, the DoDTechSpace and Minsky natural-language platforms for defense researchers, and Dimensions for collaborative discovery. Most DTIC services require authentication tied to DoD or registered-user roles. DTIC does not publicly publish a developer API, though tools such as Dimensions and Minsky offer programmatic capabilities to authorized users.
url: https://raw.githubusercontent.com/api-evangelist/defense-technical-information-center/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
xType: government
access: 3rd-Party
position: Consuming
tags:
  - Defense
  - Department of Defense
  - DTIC
  - Federal Government
  - Knowledge Management
  - Library
  - Research
  - Scientific and Technical Information
created: '2024-12-25'
modified: '2026-04-28'
apis:
  - aid: defense-technical-information-center:defense-technical-information-center-website
    name: DTIC Website
    description: Public-facing website of the Defense Technical Information Center describing DTIC services, products, and access programs. The site links to Discover, R&E Gateway, training, and registration but does not publish a developer API.
    humanURL: https://www.dtic.mil
    tags:
      - Federal Government
      - Website
    properties:
      - type: Documentation
        url: https://www.dtic.mil
  - aid: defense-technical-information-center:defense-technical-information-center-discover
    name: DTIC Discover
    description: Search platform for DTIC's collection of technical reports and other scientific and technical information assets. Discover offers faceted search, citation export, and document download for authorized users. Programmatic access is not publicly documented.
    humanURL: https://discover.dtic.mil
    tags:
      - Discovery
      - Search
      - Technical Reports
    properties:
      - type: Documentation
        url: https://discover.dtic.mil
  - aid: defense-technical-information-center:defense-technical-information-center-re-gateway
    name: DTIC Research and Engineering (R&E) Gateway
    description: Authenticated portal for DoD researchers and registered users to access DTIC research and engineering resources, planning documents, and program information.
    humanURL: https://discover.dtic.mil
    tags:
      - Engineering
      - R&E
      - Research
    properties:
      - type: Documentation
        url: https://discover.dtic.mil
  - aid: defense-technical-information-center:defense-technical-information-center-dodtechspace
    name: DoDTechSpace
    description: Collaboration platform for DoD scientists, engineers, and program managers operated by DTIC for sharing knowledge, communities of practice, and project information.
    humanURL: https://www.dodtechspace.mil
    tags:
      - Collaboration
      - Communities of Practice
    properties:
      - type: Documentation
        url: https://www.dodtechspace.mil
  - aid: defense-technical-information-center:defense-technical-information-center-foia
    name: DTIC FOIA Reading Room
    description: Online portal that publishes records released under the Freedom of Information Act. Records are browsable and downloadable but there is no documented API.
    humanURL: https://www.dtic.mil/foia
    tags:
      - FOIA
      - Open Records
      - Transparency
    properties:
      - type: Documentation
        url: https://www.dtic.mil/foia
common:
  - type: Website
    url: https://www.dtic.mil
  - type: Documentation
    url: https://www.dtic.mil/about-dtic
  - type: News
    url: https://www.dtic.mil/dtic-digest
  - type: ContactUs
    url: https://www.dtic.mil/contact-us
  - type: PrivacyPolicy
    url: https://www.dtic.mil/website-policies
  - type: FOIA
    url: https://www.dtic.mil/foia
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
