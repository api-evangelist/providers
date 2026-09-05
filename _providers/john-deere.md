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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
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
random_paper: 6
rate_limits:
- limit_count: 1
  name: John Deere Rate Limits
  slug: john-deere-rate-limits
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
