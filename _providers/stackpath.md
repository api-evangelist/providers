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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/vendor-facets/stackpath-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/stackpath-vendor-facets.yml
- group: company
  title: ''
  type: Website
  url: https://www.stackpath.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/security/stackpath-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stackpath-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/packages/stackpath-packages.yml
  title: ''
  type: Packages
  url: packages/stackpath-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/packages/stackpath-packages.yml
  title: ''
  type: SDKs
  url: packages/stackpath-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/cli/stackpath-cli.yml
  title: ''
  type: CLI
  url: cli/stackpath-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/lifecycle/stackpath-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stackpath-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/plans/stackpath-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stackpath-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/rate-limits/stackpath-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stackpath-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/llms/stackpath-llms.txt
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
modified: '2026-09-15'
name: StackPath
nav: Providers
network: true
overview: 'StackPath is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Edge Computing, CDN, Web Application Firewall, and DNS.


  StackPath''s developer surface includes CLI and 9 more developer resources.'
plans:
- name: Stackpath Plans Pricing
  plan_count: 0
  slug: stackpath-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Stackpath Rate Limits
  slug: stackpath-rate-limits
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- CDN
- Web Application Firewall
- DNS
- Object Storage
- Serverless
- Defunct
website: https://www.stackpath.com/
---
