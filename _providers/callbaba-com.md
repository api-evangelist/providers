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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.callbaba.com/
- group: agent
  href: https://artifacts.apis.io/callbaba-com/well-known/callbaba-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/callbaba-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/callbaba-com/hosts/callbaba-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/callbaba-com-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.callbaba.com/updates/press/
- group: company
  title: ''
  type: Blog
  url: https://www.callbaba.com/blog/
- group: auth
  href: https://artifacts.apis.io/callbaba-com/security/callbaba-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/callbaba-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/callbaba-com/security/callbaba-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/callbaba-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.callbaba.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.callbaba.com/api/mcp
  - status: 200
    url: https://www.callbaba.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Baba provides healthcare advocacy services that help individuals, families, payers, and providers manage appointments, prescriptions, insurance paperwork, medical equipment, transportation, and other care‑related needs. Advocates work with existing doctors and insurers, and the service is covered by Medicare for eligible members, so most users pay nothing out of pocket. The platform uses AI tools to identify missed refills, unbooked referrals, and pending authorizations, then contacts users to arrange follow‑up actions.
image: https://www.callbaba.com/og-image.png
layout: provider
modified: '2026-10-24'
name: Baba
nav: Providers
network: true
overview: 'Baba is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare Advocacy, Patient Support, Medicare, Medical Equipment, and Prescription Assistance.


  Baba''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Callbaba Com Domain Security
  slug: callbaba-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Callbaba Com Trust Center
  slug: callbaba-com-trust-center
  summary_line: SOC 2, HIPAA
slug: callbaba-com
tags:
- Healthcare Advocacy
- Patient Support
- Medicare
- Medical Equipment
- Prescription Assistance
- Transportation Services
website: https://www.callbaba.com/
---
