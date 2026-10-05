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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apifiny/refs/heads/main/hosts/apifiny-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apifiny-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apifiny/refs/heads/main/vendors/apifiny-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apifiny-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apifiny/refs/heads/main/packages/apifiny-packages.yml
  title: ''
  type: SDKs
  url: packages/apifiny-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apifiny/refs/heads/main/packages/apifiny-packages.yml
  title: ''
  type: Packages
  url: packages/apifiny-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://doc.apifiny.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apifiny/refs/heads/main/security/apifiny-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apifiny-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apifiny.com/
coverage:
  detail: Documentation endpoint returns only an anti-abuse JSON message, no OpenAPI or other spec.
  evidence:
  - status: 200
    url: https://doc.apifiny.com
  - status: 0
    url: https://api.apifiny.com/openapi.json
  - status: 404
    url: https://apifiny.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Apifiny provides liquidity and market making services for digital asset exchanges, offering a suite of APIs that enable trading, order management, and market data access. The company focuses on bridging traditional finance infrastructure with the crypto ecosystem, delivering robust, low-latency connectivity for institutional clients. Through partnerships with major exchanges, Apifiny facilitates seamless integration, risk management, and compliance tools, empowering firms to launch and operate digital asset markets efficiently.
layout: provider
modified: '2026-09-25'
name: Apifiny
nav: Providers
network: true
overview: 'Apifiny is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Market Making, Liquidity Provisioning, and Partner Platforms.


  Apifiny''s developer surface includes documentation and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Apifiny Domain Security
  slug: apifiny-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apifiny
tags:
- Market Making
- Liquidity Provisioning
- Partner Platforms
website: https://apifiny.com/
---
