---
aid: rubygems
name: RubyGems
description: RubyGems.org is the Ruby community's primary gem hosting service, providing the infrastructure for publishing, discovering, and installing Ruby gems. The RubyGems API enables programmatic access to gem metadata, version information, download statistics, search, owner management, webhooks, and the compact index used by Bundler for dependency resolution. RubyGems.org hosts over 160,000 gems with billions of total downloads.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Ruby
  - Package Manager
  - Open Source
  - Developer Tools
created: '2025-01-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/rubygems/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: rubygems:gems-api
    name: RubyGems Gems API
    description: The RubyGems Gems API (v1) provides endpoints for retrieving gem metadata, listing owned gems, submitting new gems, yanking gem versions, managing gem ownership, retrieving user profiles, querying gem dependencies, and exchanging OIDC tokens for API keys for trusted publishing workflows.
    humanURL: https://guides.rubygems.org/rubygems-org-api/
    baseURL: https://rubygems.org/api/v1
    tags:
      - Ruby
      - Gems
      - Package Manager
    properties:
      - type: Documentation
        url: https://guides.rubygems.org/rubygems-org-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rubygems/refs/heads/main/openapi/rubygems-gems-api-openapi.yml
  - aid: rubygems:api-v2
    name: RubyGems API V2
    description: The RubyGems API V2 provides improved endpoints for querying detailed gem version information including metadata, dependencies, checksums, and platform-specific builds. Designed to better support modern tooling and dependency resolution workflows.
    humanURL: https://guides.rubygems.org/rubygems-org-api-v2/
    baseURL: https://rubygems.org/api/v2
    tags:
      - Ruby
      - Gems
      - Versions
      - Package Manager
    properties:
      - type: Documentation
        url: https://guides.rubygems.org/rubygems-org-api-v2/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rubygems/refs/heads/main/openapi/rubygems-api-v2-openapi.yml
  - aid: rubygems:downloads-api
    name: RubyGems Downloads API
    description: The RubyGems Downloads API provides download count statistics for gems and individual gem versions hosted on RubyGems.org.
    humanURL: https://guides.rubygems.org/rubygems-org-api/
    baseURL: https://rubygems.org/api/v1
    tags:
      - Ruby
      - Downloads
      - Statistics
    properties:
      - type: Documentation
        url: https://guides.rubygems.org/rubygems-org-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rubygems/refs/heads/main/openapi/rubygems-downloads-api-openapi.yml
  - aid: rubygems:search-api
    name: RubyGems Search API
    description: The RubyGems Search API allows developers to search for gems by matching a query string against gem names and descriptions. Returns paginated results of active gems.
    humanURL: https://guides.rubygems.org/rubygems-org-api/
    baseURL: https://rubygems.org/api/v1
    tags:
      - Ruby
      - Search
      - Discovery
    properties:
      - type: Documentation
        url: https://guides.rubygems.org/rubygems-org-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rubygems/refs/heads/main/openapi/rubygems-search-api-openapi.yml
  - aid: rubygems:activity-api
    name: RubyGems Activity API
    description: The RubyGems Activity API provides activity feeds of the most recently added and most recently updated gems on RubyGems.org, useful for monitoring new releases and tracking ecosystem changes.
    humanURL: https://guides.rubygems.org/rubygems-org-api/
    baseURL: https://rubygems.org/api/v1
    tags:
      - Ruby
      - Activity
      - Monitoring
    properties:
      - type: Documentation
        url: https://guides.rubygems.org/rubygems-org-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rubygems/refs/heads/main/openapi/rubygems-activity-api-openapi.yml
  - aid: rubygems:webhooks-api
    name: RubyGems Webhooks API
    description: The RubyGems Webhooks API enables webhook subscriptions that fire when gems are pushed to RubyGems.org. Webhooks can be scoped to a specific gem or applied globally using a wildcard. Includes test-fire functionality and HMAC signature verification.
    humanURL: https://guides.rubygems.org/rubygems-org-api/
    baseURL: https://rubygems.org/api/v1
    tags:
      - Ruby
      - Webhooks
      - Events
    properties:
      - type: Documentation
        url: https://guides.rubygems.org/rubygems-org-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rubygems/refs/heads/main/openapi/rubygems-webhooks-api-openapi.yml
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/rubygems/refs/heads/main/asyncapi/rubygems-webhooks-asyncapi.yml
common:
  - type: Portal
    url: https://rubygems.org/
  - type: Documentation
    url: https://guides.rubygems.org/
  - type: Authentication
    url: https://guides.rubygems.org/api-key-scopes/
  - type: GitHub
    url: https://github.com/rubygems/rubygems.org
  - type: Status
    url: https://status.rubygems.org/
  - type: Blog
    url: https://blog.rubygems.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
