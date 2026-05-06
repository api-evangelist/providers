---
aid: europeana
name: Europeana
description: Europeana empowers the cultural heritage sector in its digital transformation. It develops expertise, tools, and policies to embrace digital change and encourage partnerships that foster innovation, making it easier for people to use cultural heritage for education, research, creation, and recreation. The Europeana platform aggregates metadata for over 50 million digitized items from more than 3,500 cultural institutions across Europe and exposes them through public APIs.
url: https://raw.githubusercontent.com/api-evangelist/europeana/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
position: Consumer
access: 3rd-Party
created: '2023-11-23'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Archives
  - Cultural Heritage
  - Europe
  - Libraries
  - Museums
  - Search
apis:
  - aid: europeana:europeana-search-and-record-api
    name: Europeana Search and Record API
    description: The Europeana Search and Record API exposes the federated catalog of over 50 million cultural heritage items aggregated from European museums, libraries, archives, and audiovisual collections. The Search endpoint supports keyword, facet, and filter queries; the Record endpoint returns the full EDM metadata for a single object.
    humanURL: https://pro.europeana.eu/page/intro
    baseURL: https://api.europeana.eu/record/v2
    tags:
      - Cultural Heritage
      - Museums
      - Search
      - Records
    properties:
      - url: https://pro.europeana.eu/page/apis
        type: Documentation
      - url: https://pro.europeana.eu/page/api-rest-console
        type: Console
      - url: https://pro.europeana.eu/pages/get-api
        type: SignUp
      - url: https://github.com/europeana/api2
        type: SourceCode
      - url: openapi/europeana-openapi.yml
        type: OpenAPI
common:
  - url: https://pro.europeana.eu/
    type: Portal
  - url: https://pro.europeana.eu/page/news
    type: News
  - url: https://pro.europeana.eu/page/events
    type: Events
  - url: https://www.europeana.eu/en/rights
    type: Terms of Service
  - url: https://www.europeana.eu/en/rights/privacy-policy
    type: Privacy Policy
  - url: https://pro.europeana.eu/about-us/office-employees
    type: Contact
  - url: https://pro.europeana.eu/page/api-libraries-and-plugins
    type: Libraries
  - url: https://github.com/europeana/api2/releases/
    type: Change Log
  - url: https://pro.europeana.eu/page/record#get-started
    type: Getting Started
  - url: https://pro.europeana.eu/pages/get-api
    type: SignUp
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
