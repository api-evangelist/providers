---
aid: defense-nuclear-facilities-safety-board
name: Defense Nuclear Facilities Safety Board
description: The Defense Nuclear Facilities Safety Board (DNFSB) is an independent organization within the executive branch of the United States Government chartered to provide recommendations and advice to the President and the Secretary of Energy on public health and safety issues at Department of Energy defense nuclear facilities. The DNFSB publishes recommendations, letters, technical reports, weekly site-representative reports, and rulemaking notices through its public website and FOIA reading room. The agency does not publish a developer-oriented API; programmatic users rely on document downloads, RSS feeds, and Federal Register integrations.
url: https://raw.githubusercontent.com/api-evangelist/defense-nuclear-facilities-safety-board/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
xType: government
access: 3rd-Party
position: Consuming
tags:
  - Defense
  - DNFSB
  - Energy
  - Federal Government
  - Health
  - Independent Agency
  - Nuclear
  - Safety
created: '2024-12-03'
modified: '2026-04-28'
apis:
  - aid: defense-nuclear-facilities-safety-board:defense-nuclear-facilities-safety-board-website
    name: DNFSB Website
    description: Public-facing website of the Defense Nuclear Facilities Safety Board providing organizational information, board members, hearings, and publications. The site does not expose a developer API.
    humanURL: https://www.dnfsb.gov
    tags:
      - Federal Government
      - Website
    properties:
      - type: Documentation
        url: https://www.dnfsb.gov
  - aid: defense-nuclear-facilities-safety-board:defense-nuclear-facilities-safety-board-recommendations
    name: DNFSB Recommendations and Reports
    description: Library of formal recommendations, technical reports, letters, and weekly site-representative reports published by the Defense Nuclear Facilities Safety Board. Documents are available for download but there is no developer API.
    humanURL: https://www.dnfsb.gov/documents
    tags:
      - Documents
      - Recommendations
      - Reports
    properties:
      - type: Documentation
        url: https://www.dnfsb.gov/documents
  - aid: defense-nuclear-facilities-safety-board:defense-nuclear-facilities-safety-board-foia
    name: DNFSB FOIA Reading Room
    description: Online portal that publishes records released under the Freedom of Information Act and frequently requested documents. Records are browsable and downloadable but there is no documented API.
    humanURL: https://www.dnfsb.gov/foia
    tags:
      - FOIA
      - Open Records
      - Transparency
    properties:
      - type: Documentation
        url: https://www.dnfsb.gov/foia
common:
  - type: Website
    url: https://www.dnfsb.gov
  - type: Documentation
    url: https://www.dnfsb.gov/documents
  - type: News
    url: https://www.dnfsb.gov/news
  - type: ContactUs
    url: https://www.dnfsb.gov/contact-us
  - type: PrivacyPolicy
    url: https://www.dnfsb.gov/privacy-and-security
  - type: FOIA
    url: https://www.dnfsb.gov/foia
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
