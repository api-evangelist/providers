---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trumark-financial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trumark-financial-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trumark-financial-credit-union
- group: company
  title: ''
  type: Website
  url: https://www.trumarkfinancial.org/
created: '2026-05-05'
description: A Philadelphia-area credit union providing a full range of personal and business banking products and financial services to members across the region.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trumark-financial.png
layout: provider
modified: '2026-05-05'
name: Trumark Financial
nav: Providers
network: true
overview: Trumark Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Credit Union, Banking, Financial-Services, and Philadelphia.
random_paper: 9
score:
  band: minimal
  composite: 0.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 14.0
    catalog_earned_first_party: 0.0
    catalog_gap: 101.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 25.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 0.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trumark-financial/refs/heads/main/screenshots/trumark-financial-2026-06-20T195800.png
security:
- kind: domain-security
  name: Trumark Financial Domain Security
  slug: trumark-financial-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Trumark Financial Vulnerability Disclosure
  slug: trumark-financial-vulnerability-disclosure
  summary_line: disclosure policy published
slug: trumark-financial
tags:
- Credit Union
- Banking
- Financial-Services
- Philadelphia
website: https://www.trumarkfinancial.org/
---
