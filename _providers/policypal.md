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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://policypal.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PolicyPal
- group: auth
  title: ''
  type: DomainSecurity
  url: security/policypal-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/policypal-well-known.yml
created: '2026-07-17'
description: PolicyPal is a Singapore-based InsurTech and digital insurance broker founded in 2016 by Val Yap that lets consumers buy, understand, and organize their insurance policies from a mobile app using OCR and rule-based policy digitization. Backed by 500 Global (500 Startups), PayPal Incubation, and Startupbootcamp FinTech, it was the first startup to graduate from the MAS FinTech Regulatory Sandbox and was acquired by Hong Kong's AMTD Digital in 2020. As of 2025 PolicyPal Pte. Ltd. and its entities (including PolicyPal Tech Pte. Ltd., Baoxianbaobao Pte. Ltd. and the ValueChampion brand) are no longer regulated by MAS, and the consumer website is undergoing a revamp. PolicyPal does not currently publish a public developer API, SDK, or documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/policypal.png
layout: provider
modified: '2026-07-20'
name: PolicyPal
nav: Providers
network: true
overview: PolicyPal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurtech, Fintech, Insurance, and Insurance Broker.
random_paper: 7
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/policypal/refs/heads/main/screenshots/policypal-2026-09-02T151647.png
security:
- kind: domain-security
  name: Policypal Domain Security
  slug: policypal-domain-security
  summary_line: TLSv1.3
slug: policypal
tags:
- Company
- Insurtech
- Fintech
- Insurance
- Insurance Broker
- Personal Finance
- Singapore
website: https://policypal.com
---
