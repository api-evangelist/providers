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
api_count: 1
apis:
- description: Alphapoint provides financial infrastructure APIs for digital assets, including treasury, trading, liquidity, and compliance solutions.
  name: Alphapoint API
  slug: alphapoint-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/alphapoint/refs/heads/main/changelog/alphapoint-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alphapoint-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alphapoint/refs/heads/main/llms/alphapoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alphapoint-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alphapoint/refs/heads/main/hosts/alphapoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphapoint-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alphapoint/refs/heads/main/vendors/alphapoint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphapoint-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://alphapoint.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alphapoint/refs/heads/main/security/alphapoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphapoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alphapoint.com
- group: docs
  title: ''
  type: APIReference
  url: https://alphapoint.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://alphapoint.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://alphapoint.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alphapoint.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alphapoint.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://alphapoint.com/contact
coverage:
  checked: '2026-10-05'
  detail: The Alphapoint site redirects API reference to a different domain and provides no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 301
    url: https://alphapoint.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Alphapoint provides financial infrastructure for digital assets, offering treasury, trading, liquidity, and compliance solutions for institutions, fintechs, and governments. Their platform enables stablecoin issuance, institutional crypto trading, and integrated treasury management, supporting regulatory compliance and security.
image: https://cdn.prod.website-files.com/69c13839d2e0cdff302bb2e7/69f080ce7206cfbd0f9f352a_alphapoint%20open%20graph.png
layout: provider
modified: '2026-09-24'
name: Alphapoint
nav: Providers
network: true
overview: 'Alphapoint is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Treasury, Trading, Payments, Liquidity, and Digital Assets.


  Alphapoint''s developer surface includes changelog, API reference, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.8
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 0.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alphapoint Domain Security
  slug: alphapoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alphapoint
tags:
- Treasury
- Trading
- Payments
- Liquidity
- Digital Assets
- Institutional Finance
website: https://alphapoint.com
---
