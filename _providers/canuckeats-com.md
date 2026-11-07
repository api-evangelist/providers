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
    agentic_access: derived
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
  score: 4.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Canuckeats Com Agentic Access
  operation_count: 2
  slug: canuckeats-com-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Food delivery ordering for AI agents across Canada.
  name: Agent API
  slug: agent-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/canuckeats-com/agentic-access/canuckeats-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canuckeats-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/canuckeats-com/rules/canuckeats-com-rules.yml
  title: ''
  type: Spectral
  url: rules/canuckeats-com-rules.yml
- group: design
  href: https://artifacts.apis.io/canuckeats-com/conformance/canuckeats-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canuckeats-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canuckeats-com/llms/canuckeats-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canuckeats-com-llms.txt
- group: other
  href: https://artifacts.apis.io/canuckeats-com/hosts/canuckeats-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canuckeats-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/canuckeats-com/vendors/canuckeats-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canuckeats-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://canuckeats.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/canuckeats
- group: auth
  href: https://artifacts.apis.io/canuckeats-com/authentication/canuckeats-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canuckeats-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/canuckeats-com/security/canuckeats-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canuckeats-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canuckeats.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mcp.canuckeats.com/
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.canuckeats.com/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://canuckeats.com/blogs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canuckeats.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canuckeats.com/terms
- group: operate
  title: ''
  type: Contact
  url: https://canuckeats.com/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://mcp.canuckeats.com/openapi.json
  - status: 401
    url: https://mcp.canuckeats.com/mcp
  - status: 200
    url: https://canuckeats.com/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: Canuck Eats is a Canadian food‑delivery comparison service that started in Merritt, BC in 2017. It shows customers the crossed‑out competitor price on every menu item, letting them see how much they save versus DoorDash and UberEats. Today the service operates in 80+ Canadian cities, covering British Columbia, Alberta, Saskatchewan, Manitoba, Ontario, Quebec, the Atlantic provinces and the territories, providing transparent pricing and local restaurant options.
image: https://canuckeats.com/opengraph-image.jpg
layout: provider
modified: '2026-11-04'
name: Canuck Eats
nav: Providers
network: true
overview: 'Canuck Eats is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Food Delivery, Canada, Price Comparison, Restaurant, and Marketplace.


  The Canuck Eats catalog on APIs.io includes 1 Spectral governance ruleset.


  Canuck Eats'' developer surface includes authentication, documentation, API reference, engineering blog, and 13 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Canuck Eats API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: canuckeats-com-rules
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 67.0
    operational_transparency: 2.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Canuckeats Com Authentication
  slug: canuckeats-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Canuckeats Com Domain Security
  slug: canuckeats-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canuckeats-com
tags:
- Food Delivery
- Canada
- Price Comparison
- Restaurant
- Marketplace
website: https://canuckeats.com/
---
