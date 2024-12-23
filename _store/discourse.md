---
aid: discourse
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/discourse.yml
apis:
  - aid: discourse:discourse-api
    name: Discourse API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    contact:
      - FN: Discourse Support
        url: https://meta.discourse.org/t/what-is-discourse-api/166416
        email: ''
    humanURL: https://www.discourse.org/
    properties:
      - url: https://docs.discourse.org/
        type: Documentation
      - url: https://docs.discourse.org/openapi.json
        type: OpenAPI
    description: >+
      At Discourse, our mission is to democratize online community and teamwork
      by raising the standard of civilized discourse on the Internet. We achieve
      this through delivering the best community and forum software.

name: Discourse
tags:
  - Communities
  - Forums
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.discourse.org/pricing
    type: Plans
  - url: https://blog.discourse.org/
    type: Blog
  - url: https://www.discourse.org/plugins
    type: Plugins
  - url: https://www.discourse.org/integrations
    type: Integrations
  - url: https://github.com/discourse/discourse
    type: Github Repo
  - url: https://www.discourse.org/privacy
    type: Privacy Policy
  - url: https://status.discourse.org/
    type: Status
created: 2023/11/13
modified: '2024-11-14'
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: overlays/apis-io-search.yml
    type: API Evangelist Ratings
position: Consumer
description: >+
  At Discourse, our mission is to democratize online community and teamwork by
  raising the standard of civilized discourse on the Internet. We achieve this
  through delivering the best community and forum software.

maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
---