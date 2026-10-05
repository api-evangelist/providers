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
  href: https://raw.githubusercontent.com/api-evangelist/bigvalue/refs/heads/main/vendors/bigvalue-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bigvalue-vendors.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bigvalue/refs/heads/main/changelog/bigvalue-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bigvalue-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigvalue/refs/heads/main/llms/bigvalue-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bigvalue-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigvalue/refs/heads/main/hosts/bigvalue-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigvalue-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://bigvalue.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://bigvalue.ai/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bigvalue.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigvalue/refs/heads/main/security/bigvalue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigvalue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bigvalue.ai
coverage:
  checked: '2026-09-28'
  detail: Documentation at https://docs.bigvalue.ai provides HTML pages but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://docs.bigvalue.ai
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bigvalue is a South Korean proptech company providing AI‑powered real‑estate valuation services. Its platform offers automated property value assessment for the Korean market, delivering data‑driven pricing intelligence to buyers, sellers, agents, and financial institutions.
image: https://bigvalue.ai/images/og/og-light.png
layout: provider
modified: '2026-09-28'
name: Bigvalue
nav: Providers
network: true
overview: 'Bigvalue is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PropTech, Artificial Intelligence, Real Estate, and Data Analytics.


  Bigvalue''s developer surface includes changelog, pricing, documentation, and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bigvalue Domain Security
  slug: bigvalue-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bigvalue
tags:
- Company
- PropTech
- Artificial Intelligence
- Real Estate
- Data Analytics
website: https://bigvalue.ai
---
