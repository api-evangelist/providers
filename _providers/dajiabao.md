---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://dajiabao.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dajiabao-domain-security.yml
created: '2026-07-17'
description: 'dajiabao is a company surfaced as a portfolio company of the Chinese venture firm Qiming and added to the API Evangelist network as a lead for enrichment. An enrichment pass on 2026-07-20 found no reachable public surface: dajiabao.com resolves in DNS (139.196.207.93, an Alibaba Cloud Shanghai address, nameservers at eName) but both TCP/80 and TCP/443 time out, so there is no website, developer portal, documentation, or /.well-known/ discovery surface to profile. Mail is delegated to Tencent Exmail (mxbiz1/mxbiz2.qq.com), which indicates the registration is still actively used even though the web presence is dark. Searches of npm, PyPI, and crates.io returned no packages under this name, and the company publishes no OpenAPI, SDK, CLI, or MCP surface that the network can index. This profile is retained as a verified-dark lead and should be re-probed on a later round in case the company relaunches a public site.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dajiabao.png
layout: provider
modified: '2026-07-20'
name: dajiabao
nav: Providers
network: true
overview: dajiabao is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture Backed, Qiming, China, and Portfolio Lead.
random_paper: 13
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Dajiabao Domain Security
  slug: dajiabao-domain-security
  summary_line: no transport/DNS hardening detected
slug: dajiabao
tags:
- Company
- Venture Backed
- Qiming
- China
- Portfolio Lead
website: https://dajiabao.com
---
