---
aid: discourse
name: Discourse
description: At Discourse, our mission is to democratize online community and teamwork by raising the standard of civilized discourse on the Internet. We achieve this through delivering the best community and forum software. The Discourse API exposes administrative and content endpoints for categories, topics, posts, users, groups, tags, uploads, badges, and more.
url: https://raw.githubusercontent.com/api-evangelist/discourse/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Communities
  - Forums
  - Open Source
created: '2023-11-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: discourse:discourse-api
    name: Discourse API
    description: The Discourse API exposes the full set of REST endpoints used to manage a Discourse forum, including categories, topics, posts, users, groups, tags, badges, uploads, search, site settings, and admin operations. Authentication uses an API Key plus an Api-Username header issued from the Discourse admin panel.
    humanURL: https://www.discourse.org/
    baseURL: https://meta.discourse.org
    tags:
      - Categories
      - Forums
      - Groups
      - Posts
      - Tags
      - Topics
      - Users
    properties:
      - type: Documentation
        url: https://docs.discourse.org/
      - type: OpenAPI
        url: openapi/discourse-openapi.json
      - type: GitHubRepo
        url: https://github.com/discourse/discourse_api
    contact:
      - FN: Discourse Support
        url: https://meta.discourse.org/t/what-is-discourse-api/166416
common:
  - url: https://www.discourse.org/
    type: Website
  - url: https://docs.discourse.org/
    type: Documentation
  - url: https://meta.discourse.org/
    type: Community
  - url: https://www.discourse.org/pricing
    type: Plans
  - url: https://blog.discourse.org/
    type: Blog
  - url: https://www.discourse.org/plugins
    type: Plugins
  - url: https://www.discourse.org/integrations
    type: Integrations
  - url: https://github.com/discourse/discourse
    type: GitHubRepo
  - url: https://github.com/discourse
    type: GitHubOrg
  - url: https://www.discourse.org/privacy
    type: PrivacyPolicy
  - url: https://www.discourse.org/tos
    type: TermsOfService
  - url: https://status.discourse.org/
    type: Status
  - url: https://meta.discourse.org/c/support/api/52
    type: Support
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
---
