---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Apivault is a free, open-source API directory that serves as a gateway to a world of public APIs. It catalogs APIs across 51 categories with details on authentication method, CORS support, and HTTPS a
  name: Apivault
  slug: apivault
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apivault-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Exifly/ApiVault
created: '2025-03-01'
description: Apivault is an open-source directory and gateway for discovering public APIs. The platform catalogs thousands of free and public APIs across 51 categories including animals, anime, blockchain, cryptocurrency, finance, health, music, news, and weather, enabling developers to find and explore APIs for application development.
features:
- description: Comprehensive directory of free and public APIs across 51 categories.
  name: API Directory
- description: Search and discover APIs by category including finance, health, weather, blockchain, and more.
  name: API Search and Discovery
- description: Developers can submit their own APIs with authentication type, CORS, and HTTPS details.
  name: API Submission
- description: Discover trending and randomly surfaced APIs across the catalog.
  name: Trending and Random APIs
- description: User account management via Google sign-in for tracking submitted and liked APIs.
  name: User Accounts
- description: Fully open-source project available on GitHub under CC BY-NC-ND 4.0 license.
  name: Open Source
finops:
- name: Apivault Finops
  service_category: API
  slug: apivault-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apivault.png
layout: provider
modified: '2026-04-19'
name: Apivault
nav: Providers
network: true
overview: Apivault publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Catalog, API Directory, API Discovery, Open Source, and Public APIs.
plans:
- name: Apivault Plans Pricing
  plan_count: 3
  slug: apivault-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Apivault Rate Limits
  slug: apivault-rate-limits
score:
  band: emerging
  composite: 20.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 20.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/screenshots/apivault-2026-06-20T172306.png
security:
- kind: domain-security
  name: Apivault Domain Security
  slug: apivault-domain-security
  summary_line: TLSv1.3
slug: apivault
tags:
- API Catalog
- API Directory
- API Discovery
- Open Source
- Public APIs
use_cases:
- description: Find free and public APIs for application development across 51 categories.
  name: API Discovery
- description: Submit and promote your own API to a community of developers.
  name: API Promotion
- description: Quickly discover APIs to accelerate prototype and proof-of-concept development.
  name: Rapid Prototyping
---
