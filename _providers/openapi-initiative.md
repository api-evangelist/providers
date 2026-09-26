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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: API for accessing OpenAPI Initiative resources, specifications, and tooling ecosystem documentation for defining standard interfaces to RESTful APIs.
  name: OpenAPI Initiative API
  slug: openapi-initiative-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openapi-initiative/refs/heads/main/security/openapi-initiative-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openapi-initiative-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/open-api-initiative
- group: docs
  title: ''
  type: Documentation
  url: https://spec.openapis.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/OAI
created: '2026-03-16'
description: The OpenAPI Initiative is a Linux Foundation project that promotes the OpenAPI Specification for defining standard, language-agnostic interfaces to RESTful APIs. It provides governance, tooling ecosystem support, and community collaboration for the most widely adopted API description format.
finops:
- name: Openapi Initiative Finops
  service_category: API
  slug: openapi-initiative-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openapi-initiative.png
layout: provider
modified: '2026-04-28'
name: OpenAPI Initiative
nav: Providers
network: true
overview: 'OpenAPI Initiative publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Linux Foundation, Specification, and Standards.


  OpenAPI Initiative''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Openapi Initiative Plans Pricing
  plan_count: 3
  slug: openapi-initiative-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Openapi Initiative Rate Limits
  slug: openapi-initiative-rate-limits
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 13.2
  previous_composite: 11.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/openapi-initiative/refs/heads/main/screenshots/openapi-initiative-2026-06-20T190907.png
security:
- kind: domain-security
  name: Openapi Initiative Domain Security
  slug: openapi-initiative-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openapi-initiative
tags:
- Linux Foundation
- Specification
- Standards
---
