---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 7
apis:
- baseURL: https://gh.io
  baseurl_source: declared
  description: The Applications API from bitbank — 1 operation(s) for applications.
  name: bitbank Applications API
  slug: bitbank-applications-api
- baseURL: https://gh.io
  baseurl_source: declared
  description: The Bitbank API API from bitbank — 1 operation(s) for bitbank api.
  name: bitbank Bitbank API
  slug: bitbank-bitbank-api-api
- baseURL: https://gh.io
  baseurl_source: declared
  description: The Copilot Install API from bitbank — 1 operation(s) for copilot install.
  name: bitbank Copilot Install API
  slug: bitbank-copilot-install-api
- baseURL: https://gh.io
  baseurl_source: declared
  description: The Octocat API from bitbank — 1 operation(s) for octocat.
  name: bitbank Octocat API
  slug: bitbank-octocat-api
- baseURL: https://gh.io
  baseurl_source: declared
  description: The Organizations API from bitbank — 6 operation(s) for organizations.
  name: bitbank Organizations API
  slug: bitbank-organizations-api
- baseURL: https://gh.io
  baseurl_source: declared
  description: The Orgs API from bitbank — 39 operation(s) for orgs.
  name: bitbank Orgs API
  slug: bitbank-orgs-api
- baseURL: https://gh.io
  baseurl_source: declared
  description: The Path API from bitbank — 1 operation(s) for path.
  name: bitbank Path API
  slug: bitbank-path-api
artifact_total: 12
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://corporate.bitbank.cc/rss.xml
- group: design
  href: https://artifacts.apis.io/bitbank/rules/bitbank-rules.yml
  title: ''
  type: Spectral
  url: rules/bitbank-rules.yml
- group: design
  href: https://artifacts.apis.io/bitbank/json-ld/bitbank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bitbank-context.jsonld
- group: design
  href: https://artifacts.apis.io/bitbank/vocabulary/bitbank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bitbank-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bitbank/data-model/bitbank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bitbank-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bitbank/authentication/bitbank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bitbank-authentication.yml
- group: design
  href: https://artifacts.apis.io/bitbank/conformance/bitbank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitbank-conformance.yml
- group: other
  href: https://artifacts.apis.io/bitbank/hosts/bitbank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitbank-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitbank/vendors/bitbank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitbank-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://bitbank.cc/guide/security
- group: company
  title: ''
  type: Newsroom
  url: https://corporate.bitbank.cc/news
- group: company
  title: ''
  type: Blog
  url: https://bitbank.cc/blog
- group: auth
  href: https://artifacts.apis.io/bitbank/security/bitbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitbank.cc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitbank.cc
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/bitbankinc/bitbank-api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://bitbank.cc/guide/flow
- group: operate
  title: ''
  type: Support
  url: https://support.bitbank.cc/hc/ja/requests/new
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitbank.cc/privacy-policy
coverage:
  checked: '2026-09-28'
  detail: Docs endpoint https://docs.bitbank.cc/openapi.json returns HTML instead of a machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.bitbank.cc/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bitbank is a Japanese cryptocurrency exchange offering spot, margin, lending, staking, and API trading services. It provides a public API for market data and order execution, targeting both retail and institutional clients. The platform emphasizes security, instant JPY withdrawals, and a wide range of crypto assets.
image: https://bitbank.cc/assets/images/share.png
json_schemas:
- name: PostApplicationsClientidTokenRequest
  property_count: 1
  slug: bitbank-post-applications-clientid-token-request
jsonld:
- class_count: 1
  name: Bitbank Context
  property_count: 1
  slug: bitbank-context
layout: provider
modified: '2026-10-06'
name: bitbank
nav: Providers
network: true
overview: 'bitbank is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Bitbank API, Copilot Install API, and 4 more. Tagged areas include Cryptocurrency, Exchange, Japan, and Finance.


  The bitbank catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  bitbank''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, and 13 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: bitbank API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: bitbank-rules
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 29.8
    discoverability: 63.4
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 25.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bitbank/bitbank-2026-10-11T102359.png
security:
- kind: authentication
  name: Bitbank Authentication
  slug: bitbank-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bitbank Domain Security
  slug: bitbank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitbank
tags:
- Cryptocurrency
- Exchange
- Japan
- Finance
website: https://bitbank.cc
---
