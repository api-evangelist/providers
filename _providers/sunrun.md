---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
- description: The Sunrun API provides access to platform services and data for enterprise integration and automation.
  name: Sunrun API
  slug: sunrun-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sunrun-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunrun-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SunRun
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sunrun
- group: company
  title: ''
  type: Website
  url: https://www.sunrun.com
created: '2026-04-19'
description: Sunrun is a major US corporation and Fortune 1000 company. The Sunrun API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Sunrun Finops
  service_category: Residential Solar & Storage
  slug: sunrun-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sunrun.png
layout: provider
modified: '2026-04-19'
name: Sunrun
nav: Providers
network: true
overview: Sunrun publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Residential Solar and Clean Energy.
plans:
- name: Sunrun Plans Pricing
  plan_count: 1
  slug: sunrun-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Sunrun Rate Limits
  slug: sunrun-rate-limits
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sunrun/refs/heads/main/screenshots/sunrun-2026-06-20T194705.png
security:
- kind: domain-security
  name: Sunrun Domain Security
  slug: sunrun-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sunrun Vulnerability Disclosure
  slug: sunrun-vulnerability-disclosure
  summary_line: disclosure policy published
slug: sunrun
tags:
- Residential Solar
- Clean Energy
website: https://www.sunrun.com
---
