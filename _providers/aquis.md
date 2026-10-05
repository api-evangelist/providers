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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aquis/refs/heads/main/llms/aquis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aquis-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aquis/refs/heads/main/well-known/aquis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aquis-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquis/refs/heads/main/hosts/aquis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquis-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquis/refs/heads/main/vendors/aquis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aquis-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aquis/refs/heads/main/security/aquis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aquis.eu
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Aquis Exchange is a creator and facilitator of next‑generation financial markets, offering accessible, simple and efficient stock exchanges, trading venues and technology. It provides market data, connectivity, and regulatory documentation for members and participants across Europe.
image: https://aqx-web-prod-s3-public-read.s3.eu-west-2.amazonaws.com/placeholder_social_aquis_e1e50419e8.jpg
layout: provider
modified: '2026-09-25'
name: AQUIS
nav: Providers
network: true
overview: AQUIS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Exchange, Market Data, and Trading.
random_paper: 19
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
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
  name: Aquis Domain Security
  slug: aquis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aquis
tags:
- Company
- Finance
- Exchange
- Market Data
- Trading
website: https://www.aquis.eu
---
