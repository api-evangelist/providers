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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/captura/refs/heads/main/vendors/captura-vendors.yml
  title: ''
  type: Vendors
  url: vendors/captura-vendors.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.captura.io/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/captura/refs/heads/main/conformance/captura-conformance.yml
  title: ''
  type: Conformance
  url: conformance/captura-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/captura/refs/heads/main/llms/captura-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/captura-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/captura/refs/heads/main/well-known/captura-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/captura-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/captura/refs/heads/main/well-known/captura-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/captura-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/captura/refs/heads/main/hosts/captura-hosts.yml
  title: ''
  type: Hosts
  url: hosts/captura-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.captura.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.captura.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hs.captura.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://captura.io/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://captura.io/news
- group: start
  title: ''
  type: Login
  url: https://captura.io/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/captura/refs/heads/main/security/captura-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/captura-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/captura/refs/heads/main/security/captura-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/captura-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://captura.io
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://hs.captura.io/mcp
  - status: 200
    url: https://captura.io
  - status: 403
    url: https://equityzen.com/company/captura
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Captura provides an all‑in‑one photography suite for studios and businesses, offering workflow management, yearbook creation, AI‑enhanced image editing, print lab services, and more. Their platform connects every step of the photography process, helping over 500 businesses streamline operations, increase revenue, and deliver professional results efficiently.
image: https://captura-prod.ams3.digitaloceanspaces.com/assets/facebook-new-home.png
layout: provider
modified: '2026-10-06'
name: Captura
nav: Providers
network: true
overview: 'Captura is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Photography, Software-as-a-Service, Workflows, and Imaging.


  Captura''s developer surface includes support, pricing, and 14 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Captura Domain Security
  slug: captura-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Captura Trust Center
  slug: captura-trust-center
  summary_line: SOC 2
slug: captura
tags:
- Company
- Photography
- Software-as-a-Service
- Workflows
- Imaging
website: https://captura.io
---
