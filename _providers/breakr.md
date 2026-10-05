---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breakr/refs/heads/main/security/breakr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breakr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.breakr.app
- group: operate
  title: ''
  type: Contact
  url: https://www.breakr.app/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breakr.app/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breakr.app/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://m.breakr.app/register
created: '2026-10-03'
description: Breakr provides an operating system for creator ecosystems, offering tools for campaign management, creator discovery, CRM, payments, escrow, analytics, and AI assistance. The platform enables brands, agencies, and creators to run campaigns, manage finances, and automate workflows, with a focus on secure escrow‑protected payments and AI‑driven insights. It aims to streamline the creator economy by integrating product, payment, and relationship layers into a single ledger.
layout: provider
modified: '2026-10-03'
name: Breakr
nav: Providers
network: true
overview: 'Breakr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, Fintech, Software-as-a-Service, and Payments.


  Breakr''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Breakr Domain Security
  slug: breakr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: breakr
tags:
- Company
- Creator Economy
- Fintech
- Software-as-a-Service
- Payments
website: https://www.breakr.app
---
