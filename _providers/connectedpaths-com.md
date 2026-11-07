---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Connect your LinkedIn Ads and Google Ads accounts to Claude and ChatGPT. Run campaign reviews, performance analysis, and weekly diagnostics directly in AI chat.
  name: Connected Paths MCP API
  slug: connected-paths-mcp-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/connectedpaths-com/llms/connectedpaths-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connectedpaths-com-llms.txt
- group: other
  href: https://artifacts.apis.io/connectedpaths-com/hosts/connectedpaths-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connectedpaths-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/connectedpaths-com/vendors/connectedpaths-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connectedpaths-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/connectedpaths-com/security/connectedpaths-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connectedpaths-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connectedpaths.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://connectedpaths.com/guides/ceo-ai-implementation/
- group: operate
  title: ''
  type: Support
  url: https://connectedpaths.com/#contact
- group: company
  title: ''
  type: Blog
  url: https://connectedpaths.com/insights/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://connectedpaths.com/privacy-policy/
coverage:
  checked: '2026-10-30'
  detail: Connected Paths provides MCP tools but does not publish any machine‑readable API specification.
  evidence:
  - status: 404
    url: https://connectedpaths.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Connected Paths is an AI implementation consultancy founded by Riaz Kanani, based in London and serving established businesses worldwide. The firm helps CEOs develop and execute AI strategies, offering services from AI readiness assessments to full‑scale implementation, covering strategy, operations, marketing, and technology integration. Through a hands‑on approach, Connected Paths works with CEOs to identify business challenges, design AI solutions, and drive measurable growth.
image: https://connectedpaths.com/connected_paths_logo_trans.png
layout: provider
modified: '2026-10-29'
name: connectedpaths-com
nav: Providers
network: true
overview: 'connectedpaths-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Consultancy, Strategy, Implementation, and CEO.


  connectedpaths-com''s developer surface includes getting-started guide, support, engineering blog, and 6 more developer resources.'
random_paper: 7
scopes:
- name: Connectedpaths Com Scopes
  scope_count: 0
  slug: connectedpaths-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/connectedpaths-com/connectedpaths-com-2026-11-03T125114.png
security:
- kind: authentication
  name: Connectedpaths Com Authentication
  slug: connectedpaths-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Connectedpaths Com Domain Security
  slug: connectedpaths-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: connectedpaths-com
tags:
- Artificial Intelligence
- Consultancy
- Strategy
- Implementation
- CEO
- London
website: https://connectedpaths.com/
---
