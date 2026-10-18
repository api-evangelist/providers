---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Huron Consulting Group API provides access to platform services and data for enterprise integration and automation.
  name: Huron Consulting Group API
  slug: huron-consulting-group-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/huron-consulting-group/refs/heads/main/plans/huron-consulting-group-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/huron-consulting-group-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/huron-consulting-group/refs/heads/main/rate-limits/huron-consulting-group-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/huron-consulting-group-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/huron-consulting-group/refs/heads/main/finops/huron-consulting-group-finops.yml
  title: ''
  type: FinOps
  url: finops/huron-consulting-group-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.huronconsultinggroup.com/en/insights
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/huron-consulting-group/refs/heads/main/security/huron-consulting-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/huron-consulting-group-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/huronconsulting
- group: company
  title: ''
  type: Website
  url: https://www.huronconsultinggroup.com
created: '2026-04-19'
description: Huron Consulting Group is a major US corporation and Fortune 1000 company. The Huron Consulting Group API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- has_sources: true
  method: generated
  name: Huron Consulting Group Finops
  primary_unit: ''
  service_category: Management Consulting
  slug: huron-consulting-group-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/huron-consulting-group.png
layout: provider
modified: '2026-10-06'
name: Huron Consulting Group
nav: Providers
network: true
overview: 'Huron Consulting Group is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Consulting, Healthcare, and Education.


  Huron Consulting Group''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Huron Consulting Group Plans Pricing
  plan_count: 1
  slug: huron-consulting-group-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Huron Consulting Group Rate Limits
  slug: huron-consulting-group-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/huron-consulting-group/refs/heads/main/screenshots/huron-consulting-group-2026-06-20T182955.png
security:
- kind: domain-security
  name: Huron Consulting Group Domain Security
  slug: huron-consulting-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: huron-consulting-group
tags:
- Consulting
- Healthcare
- Education
website: https://www.huronconsultinggroup.com
---
