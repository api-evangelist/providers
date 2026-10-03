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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: AutoFlight provides aerial transport services via its drone platform.
  name: Autoflight API
  slug: autoflight-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autoflight/refs/heads/main/well-known/autoflight-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autoflight-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autoflight/refs/heads/main/well-known/autoflight-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autoflight-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autoflight/refs/heads/main/hosts/autoflight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoflight-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autoflight.com/en/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.autoflight.com/en/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autoflight/refs/heads/main/security/autoflight-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autoflight-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autoflight/refs/heads/main/security/autoflight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoflight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autoflight.com/en/
coverage:
  checked: 2026-09-26
  detail: The Autoflight website renders content via JavaScript, preventing automated extraction of API specifications.
  evidence:
  - status: 200
    url: https://www.autoflight.com/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Autoflight builds the future of mass individual aerial transport, offering high‑reliability, all‑weather capable drone solutions for personal and commercial flight. The company focuses on innovative aviation technology, safety, and sustainability, aiming to democratize air mobility for everyday users and businesses alike.
layout: provider
modified: '2026-09-26'
name: Autoflight
nav: Providers
network: true
overview: Autoflight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include eVTOL, Air Taxi, Advanced Air Mobility, Aviation, and Transportation.
random_paper: 1
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autoflight Domain Security
  slug: autoflight-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Autoflight Vulnerability Disclosure
  slug: autoflight-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: autoflight
tags:
- eVTOL
- Air Taxi
- Advanced Air Mobility
- Aviation
- Transportation
- Certification
website: https://www.autoflight.com/en/
---
