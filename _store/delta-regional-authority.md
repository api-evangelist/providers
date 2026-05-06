---
aid: delta-regional-authority
name: Delta Regional Authority
url: https://raw.githubusercontent.com/api-evangelist/delta-regional-authority/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Economic Development
  - Federal Government
  - Grants
  - Mississippi River
  - Regional Authority
  - Rural Development
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: government
description: The Delta Regional Authority (DRA) is a federal-state partnership established in 2000 to promote and encourage economic development of the lower Mississippi River and Alabama Black Belt regions. DRA does not publish a public REST API; this profile indexes the public website, grants information, and program resources.
apis:
  - aid: delta-regional-authority:dra-website
    name: Delta Regional Authority Website
    description: The DRA website surfaces grant programs, leadership development, community investment programs, and economic development resources for the eight-state Mississippi Delta and Alabama Black Belt service area.
    humanURL: https://www.dra.gov
    tags:
      - Economic Development
      - Grants
      - Programs
    properties:
      - type: Documentation
        url: https://www.dra.gov
      - type: Programs
        url: https://www.dra.gov/programs/
      - type: Grants
        url: https://www.dra.gov/funding/
common:
  - type: Website
    url: https://www.dra.gov
  - type: News
    url: https://www.dra.gov/news/
  - type: Contact
    url: https://www.dra.gov/contact/
  - type: USAspending
    url: https://www.usaspending.gov/agency/delta-regional-authority
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
