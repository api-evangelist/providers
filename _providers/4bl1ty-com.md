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
  band: human-only
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Marketplace Control Protocol (MCP) API for interacting with the 4bl1ty platform.
  name: 4bl1ty MCP API
  slug: 4bl1ty-mcp-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/4bl1ty-com/authentication/4bl1ty-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/4bl1ty-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/4bl1ty-com/llms/4bl1ty-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/4bl1ty-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/4bl1ty-com/well-known/4bl1ty-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/4bl1ty-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/4bl1ty-com/hosts/4bl1ty-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/4bl1ty-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/4bl1ty-com/vendors/4bl1ty-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/4bl1ty-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/4bl1ty-com/security/4bl1ty-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/4bl1ty-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://4bl1ty.com/
- group: docs
  title: ''
  type: Documentation
  url: https://4bl1ty.com/mcp/api
- group: start
  title: ''
  type: GettingStarted
  url: https://4bl1ty.com/mcp/quickstart
- group: company
  title: ''
  type: Blog
  url: https://4bl1ty.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://4bl1ty.com/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://4bl1ty.com/confidentialite
- group: commercial
  title: ''
  type: Legal
  url: https://4bl1ty.com/mentions-legales
- group: agent
  title: ''
  type: LLMS
  url: https://4bl1ty.com/llms.txt
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered HTML with no machine‑readable OpenAPI or other spec.
  evidence:
  - status: 200
    url: https://4bl1ty.com/mcp/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: 4bl1ty provides a marketplace that connects AI agents with human workers to perform physical tasks that AI cannot execute. The platform lets agents publish missions, humans on the ground accept and complete them, and payments are escrowed until proof of completion is verified. It targets use‑cases like last‑mile delivery, on‑site inspections, and in‑person meetings, bridging the gap between digital intelligence and real‑world action.
image: https://4bl1ty.com/opengraph-image?eec621bca2936eb3
layout: provider
modified: '2026-10-31'
name: 4bl1ty
nav: Providers
network: true
overview: '4bl1ty is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Artificial Intelligence, Human-in-the-Loop, Task Automation, and France.


  4bl1ty''s developer surface includes authentication, documentation, getting-started guide, engineering blog, legal docs, and 9 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 17.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 4Bl1Ty Com Authentication
  slug: 4bl1ty-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: 4Bl1Ty Com Domain Security
  slug: 4bl1ty-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 4bl1ty-com
tags:
- Marketplace
- Artificial Intelligence
- Human-in-the-Loop
- Task Automation
- France
website: https://4bl1ty.com/
---
