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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: The Degreed REST API provides HTTP-based access to manage learning data within the Degreed platform. It covers user management, learning content (articles, books, courses, videos, podcasts, events), p
  name: Degreed API
  slug: degreed-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://degreed.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/security/degreed-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/degreed-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/security/degreed-domain-security.yml
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
modified: '2026-09-16'
name: Degreed
nav: Providers
network: true
overview: 'Degreed publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Learning Experience Platform, Skill Development, Learning Pathways, Workforce Upskilling, and E-Learning.


  The Degreed catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Degreed Plans Pricing
  plan_count: 3
  slug: degreed-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Degreed Rate Limits
  slug: degreed-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 10.7
    discoverability: 68.5
    operational_transparency: 28.9
  previous_composite: 23.9
  provenance:
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- E-Learning
- HR Technology
website: https://degreed.com
---
