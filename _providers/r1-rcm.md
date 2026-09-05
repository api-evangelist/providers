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
- description: The R1 RCM API provides access to platform services and data for enterprise integration and automation.
  name: R1 RCM API
  slug: r1-rcm-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/r1-rcm-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/r1-rcm-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/r1-rcm
- group: company
  title: ''
  type: Website
  url: https://www.r1rcm.com
created: '2026-04-19'
description: R1 RCM is a major US corporation and Fortune 1000 company. The R1 RCM API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: R1 Rcm Finops
  service_category: Healthcare Services
  slug: r1-rcm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/r1-rcm.png
layout: provider
modified: '2026-04-19'
name: R1 RCM
nav: Providers
network: true
overview: R1 RCM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Revenue Cycle, and Technology.
plans:
- name: R1 Rcm Plans Pricing
  plan_count: 1
  slug: r1-rcm-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: R1 Rcm Rate Limits
  slug: r1-rcm-rate-limits
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/r1-rcm/refs/heads/main/screenshots/r1-rcm-2026-06-20T192500.png
security:
- kind: domain-security
  name: R1 Rcm Domain Security
  slug: r1-rcm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: R1 Rcm Trust Center
  slug: r1-rcm-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: r1-rcm
tags:
- Healthcare
- Revenue Cycle
- Technology
website: https://www.r1rcm.com
---
