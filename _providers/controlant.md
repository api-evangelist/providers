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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.controlant.com/quality
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/llms/controlant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/controlant-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/well-known/controlant-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/controlant-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/well-known/controlant-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/controlant-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/well-known/controlant-controlant-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/controlant-controlant-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/well-known/controlant-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/controlant-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/hosts/controlant-hosts.yml
  title: ''
  type: Hosts
  url: hosts/controlant-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/vendors/controlant-vendors.yml
  title: ''
  type: Vendors
  url: vendors/controlant-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.controlant.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.controlant.com/?lang=en
- group: operate
  title: ''
  type: StatusPage
  url: https://status.controlant.com/
- group: auth
  title: ''
  type: Security
  url: https://www.controlant.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.controlant.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.controlant.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/security/controlant-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/controlant-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/security/controlant-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/controlant-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlant/refs/heads/main/security/controlant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/controlant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.controlant.com
coverage:
  checked: '2026-10-10'
  detail: Controlant's website provides no developer program or public API documentation.
  evidence:
  - status: 200
    url: https://www.controlant.com
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Controlant provides real‑time, GxP‑validated pharma supply‑chain visibility through its Saga devices and platform. It monitors temperature, location and status of shipments across the globe, offering data sharing via Delta Sharing, streaming, and an Integrations API. Founded in 2009, Controlant serves top pharma companies, delivering millions of shipments in over 180 countries with 24/7 monitoring and rapid response.
image: https://www.controlant.com/posters/hero-poster.jpg
layout: provider
modified: '2026-10-10'
name: Controlant
nav: Providers
network: true
overview: 'Controlant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharma, Supply Chain, Real-time Monitoring, and Data Sharing.


  Controlant''s developer surface includes support and 17 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Controlant Domain Security
  slug: controlant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Controlant Vulnerability Disclosure
  slug: controlant-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Controlant Trust Center
  slug: controlant-trust-center
  summary_line: SOC 2, ISO 27001
slug: controlant
tags:
- Company
- Pharma
- Supply Chain
- Real-time Monitoring
- Data Sharing
website: https://www.controlant.com
---
