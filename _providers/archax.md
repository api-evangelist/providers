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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/archax/refs/heads/main/llms/archax-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/archax-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/archax/refs/heads/main/hosts/archax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/archax-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/archax/refs/heads/main/vendors/archax-vendors.yml
  title: ''
  type: Vendors
  url: vendors/archax-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archax/refs/heads/main/security/archax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://archax.com
coverage:
  checked: 2026-09-25
  detail: Archax website returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://archax.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Archax builds regulated infrastructure for tokenising, trading, and safekeeping real-world assets. Authorized across the UK and EU, Archax provides a secure, compliant platform for digital asset markets, offering institutional-grade solutions for asset tokenisation, secondary market trading, and custodial services, enabling investors to access tokenised real-world assets with confidence and regulatory oversight.
layout: provider
modified: '2026-09-25'
name: Archax
nav: Providers
network: true
overview: Archax is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Digital Assets, Tokenisation, Trading Platform, and Regulated.
random_paper: 15
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Archax Domain Security
  slug: archax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: archax
tags:
- Fintech
- Digital Assets
- Tokenisation
- Trading Platform
- Regulated
website: https://archax.com
---
