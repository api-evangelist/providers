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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Kreya is a GUI client for gRPC and REST APIs with innovative features for environments, authorizations, and more.
  name: Kreya
  slug: kreya
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kreya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kreya.app/
- group: docs
  title: ''
  type: Documentation
  url: https://kreya.app/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/riok/Kreya
- group: company
  title: ''
  type: Blog
  url: https://kreya.app/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://kreya.app/llms.txt
created: '2026-03-16'
description: Kreya is a GUI client for gRPC, REST, GraphQL, WebSocket, and Server-Sent Events APIs. All data is stored in git-diffable files for easy reviews and versioning. Kreya provides automated snapshot and scripted tests, flexible environments, and support for all gRPC streaming modes.
finops:
- name: Kreya Finops
  service_category: API
  slug: kreya-finops
graphqls:
- description: ''
  name: Kreya GraphQL API
  slug: kreya-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kreya.png
layout: provider
modified: '2026-04-28'
name: Kreya
nav: Providers
network: true
overview: 'Kreya publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Client, Developer Tools, gRPC, and REST.


  Kreya''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Kreya Plans Pricing
  plan_count: 3
  slug: kreya-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Kreya Rate Limits
  slug: kreya-rate-limits
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kreya/refs/heads/main/screenshots/kreya-2026-06-20T184156.png
security:
- kind: domain-security
  name: Kreya Domain Security
  slug: kreya-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kreya
tags:
- API Client
- Developer Tools
- gRPC
- REST
website: https://kreya.app/
---
