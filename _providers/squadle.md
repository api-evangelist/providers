---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://squadle.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.crunchtime.com/squadle — a different registrable domain (squadle.com -> crunchtime.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/crunchtime/
- group: company
  title: ''
  type: Website
  url: https://squadle.com
- group: start
  title: ''
  type: Login
  url: https://hq.squadle.com/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crunchtime.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crunchtime.com/en/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.crunchtime.com/security
- group: design
  title: ''
  type: Conformance
  url: conformance/squadle-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/squadle-domain-security.yml
created: '2026-07-17'
description: Squadle is a food safety and operational compliance platform for multi-unit restaurant and foodservice operations. It combines IoT remote temperature monitoring (its Remote Temperature System) with digital food-safety checklists, shift management, and patented ZeroTouch technology that automates temperature logging and triggers corrective actions. The platform reports 3.3B+ completed tasks and 100M+ temperatures measured. Squadle was acquired by Crunchtime and now operates as part of the Crunchtime Operations Execution platform; the squadle.com domain redirects to crunchtime.com/squadle. No public API or developer platform is currently published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/squadle.png
layout: provider
modified: '2026-07-21'
name: Squadle
nav: Providers
network: true
overview: Squadle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Safety, Restaurant Operations, Compliance, and IoT.
random_paper: 16
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/squadle/refs/heads/main/screenshots/squadle-2026-09-02T160638.png
security:
- kind: domain-security
  name: Squadle Domain Security
  slug: squadle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: squadle
tags:
- Company
- Food Safety
- Restaurant Operations
- Compliance
- IoT
- Temperature Monitoring
- Digital Checklists
- Restaurant Technology
website: https://squadle.com
---
