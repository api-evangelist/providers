---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The John Deere API allows developers to access and integrate data from John Deere's connected agricultural equipment and software platforms. The API surfaces equipment performance, field conditions, m
  name: John Deere API
  slug: john-deere
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/john-deere-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JohnDeere
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/john-deere
- group: company
  title: ''
  type: Website
  url: https://developer.deere.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.deere.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deere.com/
created: '2025-02-12'
description: John Deere is a renowned American corporation that specializes in manufacturing agricultural, construction, and forestry machinery. The company, founded in 1837 by John Deere, has a long history of innovation and has become a leader in the industry. John Deere's products include tractors, combines, excavators, and other equipment designed to support and improve farming and construction operations.
finops:
- name: John Deere Finops
  service_category: Agriculture / Equipment Telemetry
  slug: john-deere-finops
graphqls:
- description: This conceptual GraphQL schema represents the John Deere precision agriculture and equipment API domain. John Deere's developer platform (https://developer.deere.com/) exposes machine telemetry, field
  name: John Deere GraphQL Schema
  slug: john-deere-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/john-deere.png
layout: provider
modified: '2026-04-28'
name: John Deere
nav: Providers
network: true
overview: 'John Deere publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Combines, Construction, Excavators, and Forestry.


  John Deere''s developer surface includes developer portal, documentation, and 4 more developer resources.'
plans:
- name: John Deere Plans Pricing
  plan_count: 1
  slug: john-deere-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 1
  name: John Deere Rate Limits
  slug: john-deere-rate-limits
score:
  band: thin
  composite: 29.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 43.2
    developer_ergonomics: 17.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/john-deere/refs/heads/main/screenshots/john-deere-2026-06-20T183749.png
security:
- kind: domain-security
  name: John Deere Domain Security
  slug: john-deere-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: john-deere
tags:
- Agriculture
- Combines
- Construction
- Excavators
- Forestry
- Machinery
- Tractors
website: https://developer.deere.com/
---
