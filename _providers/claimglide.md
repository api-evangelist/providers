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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/claimglide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claimglide.com/
- group: operate
  title: ''
  type: Support
  url: mailto:contact@claimglide.com
created: '2026-07-17'
description: Claimglide (ClaimGlide) is an AI-powered software platform that automates the end-to-end prior-authorization process for private medical practices and healthcare providers. It generates prior-auth submissions using payer-approved language, auto-pulls clinical data from EMR systems, follows up with payers, tracks authorization timelines, and auto-generates appeal letters to increase the share of prior-auths approved and shorten turnaround time. Claimglide integrates with major EMR/EHR platforms including eClinicalWorks, athenahealth, NextGen Healthcare, and ModMed, and states HIPAA compliance. Founded in 2025 in Seattle by Nami Lindquist and backed by Y Combinator (Winter 2026 batch), the company was added to the API Evangelist network as a portfolio lead. No public API, developer documentation, or developer portal is published at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/claimglide.png
layout: provider
modified: '2026-07-18'
name: Claimglide
nav: Providers
network: true
overview: 'Claimglide is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Prior Authorization, and Health Insurance.


  Claimglide''s developer surface includes support and 2 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/claimglide/refs/heads/main/screenshots/claimglide-2026-07-25T205453.png
security:
- kind: domain-security
  name: Claimglide Domain Security
  slug: claimglide-domain-security
  summary_line: TLSv1.2 · DMARC
slug: claimglide
tags:
- Company
- Healthcare
- Digital Health
- Prior Authorization
- Health Insurance
- Revenue Cycle Management
- Medical Claims
- Artificial Intelligence
- Appeals
website: https://claimglide.com/
---
