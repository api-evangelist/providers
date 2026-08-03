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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Degreed REST API provides HTTP-based access to manage learning data within the Degreed platform. It covers user management, learning content (articles, books, courses, videos, podcasts, events), p
  name: Degreed API
  slug: degreed-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/degreed-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/degreed-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/plans/degreed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/rate-limits/degreed-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/finops/degreed-finops.yml
created: 2026-06-13
description: Degreed is a learning experience platform with a REST API for managing learning pathways, tracking skill development, accessing content integrations, and reporting workforce upskilling data. The API enables organizations to manage users, content, completions, skills, pathways, accomplishments, and social learning features using OAuth 2.0 authentication. Multi-region deployments are supported across US, EU, and Canada data centers.
finops:
- name: Degreed Finops
  service_category: ''
  slug: degreed-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/degreed.png
jsonld:
- class_count: 0
  name: Degreed Context
  property_count: 8
  slug: degreed-context
layout: provider
modified: 2026-06-13
name: Degreed
nav: Providers
network: true
overview: 'Degreed publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Learning Experience Platform, Skill Development, Learning Pathways, Workforce Upskilling, and eLearning.


  The Degreed catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Degreed Plans Pricing
  plan_count: 3
  slug: degreed-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 2
  name: Degreed Rate Limits
  slug: degreed-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 8.1
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/screenshots/degreed-2026-06-20T175855.png
security:
- kind: domain-security
  name: Degreed Domain Security
  slug: degreed-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Degreed Trust Center
  slug: degreed-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: degreed
tags:
- Learning Experience Platform
- Skill Development
- Learning Pathways
- Workforce Upskilling
- eLearning
- HR Technology
---
