---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/docketbird/refs/heads/main/llms/docketbird-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docketbird-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/docketbird/refs/heads/main/well-known/docketbird-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docketbird-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docketbird/refs/heads/main/security/docketbird-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docketbird-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.docketbird.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.docketbird.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docketbird.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.docketbird.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.docketbird.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docketbird.com/privacy_policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docketbird.com/terms_of_use
- group: operate
  title: ''
  type: Support
  url: https://www.docketbird.com/contact
coverage:
  checked: 2026-09-21
  detail: Documentation pages return 403 and no machine‑readable spec is available.
  evidence:
  - status: 403
    url: https://api.docketbird.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: DocketBird provides a comprehensive platform for tracking federal and state court filings, deadlines, and documents. It integrates with all U.S. federal courts and over 7,000 state courts, offering automated calendaring, document delivery, and research tools. Users can start a 30‑day free trial, book demos, and access a searchable database of cases and court information, ensuring they never miss critical legal deadlines.
layout: provider
modified: '2026-09-21'
name: DocketBird
nav: Providers
network: true
overview: 'DocketBird is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal Tech, CourtFiling, Document-Management, and Automation.


  DocketBird''s developer surface includes documentation, pricing, signup flow, support, and 7 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 53.7
    operational_transparency: 0.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docketbird Domain Security
  slug: docketbird-domain-security
  summary_line: TLSv1.2 · DMARC
slug: docketbird
tags:
- Company
- Legal Tech
- CourtFiling
- Document-Management
- Automation
website: https://www.docketbird.com/
---
