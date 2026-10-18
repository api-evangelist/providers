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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/claira/refs/heads/main/hosts/claira-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claira-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/claira/refs/heads/main/vendors/claira-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claira-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/claira/refs/heads/main/packages/claira-packages.yml
  title: ''
  type: SDKs
  url: packages/claira-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/claira/refs/heads/main/packages/claira-packages.yml
  title: ''
  type: Packages
  url: packages/claira-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.claira.io/insights/category/News
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/claira/refs/heads/main/security/claira-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claira-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.claira.io/
coverage:
  checked: '2026-10-08'
  detail: Claira's website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.claira.io/
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Claira is an AI-driven platform that streamlines private market investment analysis and decision-making. Founded in 2018 and based in New York City, it offers an agentic AI system to capture, organize, preserve, and analyze institutional knowledge, accelerating deal flow for financial institutions and investors. Backed by leading investors, Claira provides tools for deal management, data extraction, and workflow automation across the private markets.
image: http://static1.squarespace.com/static/66c08dc3c081aa18be147ef0/t/6701d85e394d534bccdb7730/1728174174939/CL+%281080+x+500+px%29+%281%29.png?format=1500w
layout: provider
modified: '2026-10-08'
name: Claira
nav: Providers
network: true
overview: Claira is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Finance, PrivateMarkets, DealManagement, and New York.
random_paper: 4
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claira Domain Security
  slug: claira-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: claira
tags:
- Artificial Intelligence
- Finance
- PrivateMarkets
- DealManagement
- New York
website: https://www.claira.io/
---
