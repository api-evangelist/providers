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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Jargon's collaborative modelling platform for designing, governing, and scaling domain models with generation of OpenAPI, JSON Schema, and JSON-LD artifacts. A public REST API is not currently publish
  name: Jargon Platform
  slug: jargon-platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jargon-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JargonInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jargon-com
- group: company
  title: ''
  type: Website
  url: https://jargon.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jargon.sh
- group: company
  title: ''
  type: Blog
  url: https://blog.jargon.sh/feed.xml
created: '2025-01-08'
description: Jargon is a platform for Domain Driven Design for APIs and Enterprise Data Modelling. It provides text-based modelling, template-based API design, real-time validation, version control with breaking change detection, and generation of artifacts including JSON Schema, OpenAPI specifications, and JSON-LD. Jargon supports DevOps-driven collaborative modelling for teams designing and governing domains at enterprise scale.
finops:
- name: Jargon Finops
  service_category: API
  slug: jargon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jargon.png
layout: provider
modified: '2026-04-28'
name: Jargon
nav: Providers
network: true
overview: 'Jargon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, Data Modelling, Domain Driven Design, Domains, and JSON Schema.


  Jargon''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Jargon Plans Pricing
  plan_count: 3
  slug: jargon-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Jargon Rate Limits
  slug: jargon-rate-limits
score:
  band: emerging
  composite: 12.8
  delta: -0.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jargon/refs/heads/main/screenshots/jargon-2026-06-20T183702.png
security:
- kind: domain-security
  name: Jargon Domain Security
  slug: jargon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jargon
tags:
- API Design
- Data Modelling
- Domain Driven Design
- Domains
- JSON Schema
- OpenAPI
- Platform
website: https://jargon.sh/
---
