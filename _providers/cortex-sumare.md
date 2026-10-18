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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cortex-sumare/refs/heads/main/well-known/cortex-sumare-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cortex-sumare-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cortex-sumare/refs/heads/main/well-known/cortex-sumare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cortex-sumare-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cortex-sumare/refs/heads/main/llms/cortex-sumare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cortex-sumare-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortex-sumare/refs/heads/main/hosts/cortex-sumare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cortex-sumare-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortex-sumare/refs/heads/main/vendors/cortex-sumare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cortex-sumare-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.cortex-intelligence.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.cortex-intelligence.com/blog/sales-ops
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cortex-sumare/refs/heads/main/security/cortex-sumare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cortex-sumare-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cortex-sumare/refs/heads/main/security/cortex-sumare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cortex-sumare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cortex-intelligence.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.cortex-intelligence.com/mcp
  - status: 403
    url: https://cortex-intelligence.com/mcp
  - status: 200
    url: https://www.cortex-intelligence.com/
  - status: 200
    url: https://www.hiive.com/securities/cortex-sumare-stock
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: 'Cortex Sumare is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-11'
name: Cortex Sumare
nav: Providers
network: true
overview: 'Cortex Sumare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Go-to-Market Intelligence, Geomarketing, and AI Analytics.


  Cortex Sumare''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 33.9
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cortex Sumare Domain Security
  slug: cortex-sumare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cortex Sumare Vulnerability Disclosure
  slug: cortex-sumare-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cortex-sumare
tags:
- Go-to-Market Intelligence
- Geomarketing
- AI Analytics
website: https://www.cortex-intelligence.com/
---
