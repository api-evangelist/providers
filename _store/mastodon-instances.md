---
aid: mastodon-instances
name: Mastodon Instances
description: Mastodon Instances (instances.social) is a service for discovering Mastodon server instances. Its API allows developers to search for instances by criteria including language, user count, and stability, and to retrieve metadata about specific instances.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/mastodon-instances/refs/heads/main/apis.yml
tags:
  - Fediverse
  - Mastodon
  - Search
  - Social
created: '2024-12-02'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mastodon-instances:mastodon-instances
    name: Mastodon Instances API
    tags:
      - Mastodon
      - Search
      - Social
    humanURL: https://instances.social
    baseURL: https://instances.social/api
    properties:
      - url: https://instances.social/api/doc/
        type: Documentation
    description: The instances.social API allows searching for and retrieving information about Mastodon server instances, including user counts, language, software version, and uptime statistics.
common:
  - type: Portal
    url: https://instances.social
  - type: Sign Up
    url: https://instances.social/api/token
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
