---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: REST API for managing products, variants, offer codes, custom fields, sales, subscribers, license keys, resource subscriptions (webhooks), and the authenticated user account on Gumroad. Authentication
  name: Gumroad v2 API
  slug: v2-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gumroad-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gumroad
- group: company
  title: ''
  type: Website
  url: https://gumroad.com
- group: docs
  title: ''
  type: Documentation
  url: https://app.gumroad.com/api
- group: operate
  title: ''
  type: Help Center
  url: https://gumroad.com/help
- group: commercial
  title: ''
  type: Pricing
  url: https://gumroad.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://gumroad.com/signup
- group: other
  title: ''
  type: Discover
  url: https://gumroad.com/discover
- group: operate
  title: ''
  type: Support
  url: https://gumroad.com/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gumroad
created: '2026-05-11'
description: Gumroad is a digital commerce platform that lets creators sell e-books, courses, software, memberships, music, and physical goods directly to their audience without needing a storefront, with built-in checkout, licensing, affiliate management, and analytics. The Gumroad v2 REST API provides programmatic access to products, sales, subscribers, offer codes, license keys, customers, and the authenticated user account. Authentication uses OAuth 2.0 access tokens passed in the Authorization header.
graphqls:
- description: This document describes a conceptual GraphQL schema for the Gumroad digital commerce and creator economy platform. Gumroad enables creators to sell digital products, memberships, courses, software, mu
  name: Gumroad GraphQL Schema
  slug: gumroad-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gumroad.png
layout: provider
modified: '2026-05-30'
name: Gumroad
nav: Providers
network: true
overview: 'Gumroad publishes 1 API on the [APIs.io](https://apis.io/) network: v2 API. Tagged areas include Digital Commerce, Creator Economy, Digital Products, Memberships, and License Keys.


  Gumroad''s developer surface includes documentation, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 55
score:
  band: thin
  composite: 28.0
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 63.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gumroad/refs/heads/main/screenshots/gumroad-2026-06-20T182434.png
security:
- kind: domain-security
  name: Gumroad Domain Security
  slug: gumroad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gumroad
tags:
- Digital Commerce
- Creator Economy
- Digital Products
- Memberships
- License Keys
- Affiliates
- E-commerce
website: https://gumroad.com
---
