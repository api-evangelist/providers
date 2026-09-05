---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://panora.dev/'', ''status'': 301, ''note'': ''declared website redirects to https://getpanora.com/ — a different registrable domain (panora.dev -> getpanora.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- description: Unified API platform allowing developers to integrate with hundreds of third-party tools through a single API.
  name: Panora Unified API
  slug: panora
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/panora-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/panora-exchange
- group: start
  title: ''
  type: Portal
  url: https://panora.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.panora.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/panoratech/Panora
- group: company
  title: ''
  type: Website
  url: https://panora.dev/
created: '2026-03-16'
description: Panora is an open-source unified API platform that allows developers to integrate with hundreds of third-party tools through a single API. It provides a unified interface for CRM, HR, accounting, and other integrations.
finops:
- name: Panora Finops
  service_category: API
  slug: panora-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/panora.png
layout: provider
modified: '2026-04-28'
name: Panora
nav: Providers
network: true
overview: 'Panora publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Integration, Open-Source, and Unified-API.


  Panora''s developer surface includes developer portal, documentation, and 4 more developer resources.'
plans:
- name: Panora Plans Pricing
  plan_count: 3
  slug: panora-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Panora Rate Limits
  slug: panora-rate-limits
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 6
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
    developer_ergonomics: 20.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/panora/refs/heads/main/screenshots/panora-2026-06-20T191340.png
security:
- kind: domain-security
  name: Panora Domain Security
  slug: panora-domain-security
  summary_line: TLSv1.3 · DMARC
slug: panora
tags:
- CRM
- Integration
- Open-Source
- Unified-API
website: https://panora.dev/
---
