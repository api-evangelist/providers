---
aid: mastodon
url: https://raw.githubusercontent.com/api-search/mastodon/refs/heads/main/apis.yml
apis:
  - aid: mastodon:mastodon
    name: Mastodon API
    tags:
      - Social Networks
    humanURL: https://docs.joinmastodon.org/
    properties:
      - url: https://docs.joinmastodon.org/client/intro/
        type: Documentation
      - url: openapi/mastodon.yml
        type: OpenAPI
    description: This is an OpenAPI for the Mastodon API.
name: Mastodon
tags:
  - Open-Source
  - Social Networks
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-16'
modified: '2026-04-28'
position: Consumer
description: Mastodon is a open source, self-hosted, social networking service. Mastodon uses the ActivityPub protocol for federation which allows users to communicate between independent Mastodon instances and other ActivityPub compatible services. Mastodon has microblogging features similar to Twitter, and is generally considered to be a part of the Fediverse.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Getting started with the API - Mastodon documentation
    url: https://docs.joinmastodon.org/client/intro/
    type: GettingStarted
  - name: Rate limits - Mastodon documentation
    url: https://docs.joinmastodon.org/api/rate-limits/
    type: RateLimits
  - name: OAuth Tokens - Mastodon documentation
    url: https://docs.joinmastodon.org/api/oauth-tokens/
    type: Authentication
  - name: OAuth Scopes - Mastodon documentation
    description: OAuth Scopes
    url: https://docs.joinmastodon.org/api/oauth-scopes/
    type: OauthScopes
  - name: Postman Workspace
    description: This is an API Evangelist workspace.
    url: https://www.postman.com/api-evangelist/mastodon/overview
    type: PostmanWorkspace
---
