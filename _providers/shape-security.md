---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://shapesecurity.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.f5.com/products/distributed-cloud-services/bot-defense — a different registrable domain (shapesecurity.com -> f5.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shape-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://shapesecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.f5.com/products/security/shape-security
created: '2026-07-17'
description: Shape Security was an enterprise application-security company (backed by gv and wing-venture-capital) specializing in bot mitigation, credential-stuffing defense, and online-fraud prevention for login, checkout, and account-recovery flows. It was acquired by F5 in 2020 and its technology now ships as F5 Distributed Cloud Bot Defense; the shapesecurity.com domain 301-redirects wholesale into f5.com. Shape Security no longer operates an independent developer portal, public API, OpenAPI spec, or SDK surface of its own — its capabilities are delivered through the F5 Distributed Cloud platform. This profile is retained as an acquisition/lineage record in the API Evangelist network.
image: https://raw.githubusercontent.com/api-evangelist/shape-security/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-21'
name: Shape Security
nav: Providers
network: true
overview: 'Shape Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Security, Bot Mitigation, and Fraud Prevention.


  Shape Security''s developer surface includes documentation and 2 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shape-security/refs/heads/main/screenshots/shape-security-2026-09-02T155107.png
security:
- kind: domain-security
  name: Shape Security Domain Security
  slug: shape-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shape-security
tags:
- Company
- Enterprise
- Security
- Bot Mitigation
- Fraud Prevention
- Application Security
- Acquired
website: http://shapesecurity.com
---
