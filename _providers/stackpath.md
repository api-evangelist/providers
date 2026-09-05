---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.stackpath.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stackpath-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/stackpath-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stackpath-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/stackpath-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stackpath-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stackpath-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stackpath-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stackpath-llms.txt
coverage:
  checked: '2026-08-29'
  detail: StackPath ceased operations in June 2024 and was dissolved; every API and developer host - api., gateway., developer., docs., control. and status.stackpath.com - has been withdrawn from DNS, the github.com/stackpath organization returns 404, and www.stackpath.com serves an 835-byte empty black placeholder page.
  evidence:
  - status: 200
    url: https://www.stackpath.com/
  - status: 0
    url: https://developer.stackpath.com/docs/en/getting-started/
  - status: 0
    url: https://gateway.stackpath.com/
  - status: 404
    url: https://api.github.com/orgs/stackpath
  - status: 404
    url: https://www.stackpath.com/.well-known/security.txt
  - status: 404
    url: https://www.stackpath.com/llms.txt
  reason: defunct
  state: none
created: '2026-08-29'
description: StackPath was an American edge computing platform provider headquartered in Dallas, Texas, founded in 2015 by SoftLayer co-founder Lance Crosby. It sold CDN, WAF/WAAP, DNS, SSL, object storage, edge compute (containers and VMs), serverless scripting and monitoring as a single edge platform, driven by a public REST API at gateway.stackpath.com with OAuth2 client-credentials auth and per-service OpenAPI definitions. The company exited the CDN business in 2023 (roughly 100 enterprise CDN contracts went to Akamai), sold its web application and API protection assets to Gcore in March 2024, then announced in June 2024 that it was ceasing operations and liquidating its remaining assets. All StackPath API, developer-portal, control-panel and status hosts have since been withdrawn from DNS and the company no longer publishes any machine-readable API contract.
layout: provider
modified: '2026-08-29'
name: StackPath
nav: Providers
network: true
overview: 'StackPath is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Edge Computing, Content Delivery Network, Web Application Firewall, and DNS.


  StackPath''s developer surface includes CLI and 8 more developer resources.'
plans:
- name: Stackpath Plans Pricing
  plan_count: 0
  slug: stackpath-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Stackpath Rate Limits
  slug: stackpath-rate-limits
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/screenshots/stackpath-2026-09-02T160712.png
security:
- kind: domain-security
  name: Stackpath Domain Security
  slug: stackpath-domain-security
  summary_line: TLSv1.3 · HSTS
slug: stackpath
tags:
- Company
- Edge Computing
- Content Delivery Network
- Web Application Firewall
- DNS
- Object Storage
- Serverless
- Defunct
website: https://www.stackpath.com/
---
