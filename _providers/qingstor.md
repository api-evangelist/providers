---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/qingstor/hosts/qingstor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qingstor-hosts.yml
- group: build
  href: https://artifacts.apis.io/qingstor/packages/qingstor-packages.yml
  title: ''
  type: Packages
  url: packages/qingstor-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qingcloud.com/
- group: start
  title: ''
  type: SignUp
  url: https://console.qingcloud.com/signup?redirect_uri=https%3A%2F%2Fwww.qingcloud.com
- group: auth
  title: ''
  type: Security
  url: https://docsv4.qingcloud.com/user_guide/security/waf/
- group: build
  title: ''
  type: SDKs
  url: https://docsv4.qingcloud.com/user_guide/development_docs/sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://qingcloud.com/pricing-regulation
- group: company
  title: ''
  type: Newsroom
  url: https://www.qingcloud.com/press
- group: auth
  href: https://artifacts.apis.io/qingstor/security/qingstor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qingstor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qingcloud.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://qingcloud.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: QingStor, operating under the QingCloud brand, provides enterprise‑grade cloud computing, AI infrastructure, and storage solutions. It offers public, private, and hybrid cloud services, including elastic compute, bare‑metal, GPU instances, container platforms, and a suite of data services such as databases, object storage, and big‑data analytics. The company serves a wide range of industries with AI‑driven solutions and supports developers through extensive documentation and APIs.
layout: provider
modified: '2026-10-28'
name: QingStor
nav: Providers
network: true
overview: 'QingStor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Infrastructure, AI, Storage, and Enterprise.


  QingStor''s developer surface includes signup flow, pricing, and 8 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qingstor Domain Security
  slug: qingstor-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: qingstor
tags:
- Cloud
- Infrastructure
- AI
- Storage
- Enterprise
website: https://qingcloud.com/
---
