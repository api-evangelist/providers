---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for Elytron Labs AI‑powered e‑commerce tools.
  name: Elytron Labs API
  slug: elytron-labs-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/elytron-in/llms/elytron-in-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elytron-in-llms.txt
- group: agent
  href: https://artifacts.apis.io/elytron-in/mcp/elytron-in-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elytron-in-mcp.yml
- group: agent
  href: https://artifacts.apis.io/elytron-in/well-known/elytron-in-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elytron-in-well-known.yml
- group: other
  href: https://artifacts.apis.io/elytron-in/hosts/elytron-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elytron-in-hosts.yml
- group: other
  href: https://artifacts.apis.io/elytron-in/vendors/elytron-in-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elytron-in-vendors.yml
- group: auth
  href: https://artifacts.apis.io/elytron-in/security/elytron-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elytron-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elytron.in/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elytron.in/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elytron.in/terms-of-service
- group: docs
  title: ''
  type: Documentation
  url: https://elytron.in/underwing/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript and contain no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://elytron.in/underwing/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Elytron Labs builds AI‑powered infrastructure for e‑commerce merchants, offering tools like Pollen and DripSync that enable product recommendation integration with AI agents and automated image generation. The company helps online retailers enhance product discovery, feed management, and visual content through AI, supporting platforms such as Shopify, WooCommerce, Google, and Meta.
image: https://elytron.in/wp-content/themes/elytron/img/underwing-hero.png?v=2
layout: provider
mcp_servers:
- description: Remote MCP server at pollen.elytron.in.
  name: elytron-in MCP Server
  slug: elytron-in-mcp-yml
modified: '2026-10-30'
name: elytron-in
nav: Providers
network: true
overview: 'elytron-in is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, E-Commerce, Software-as-a-Service, and Retail.


  elytron-in''s developer surface includes documentation and 9 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/elytron-in/elytron-in-2026-11-03T131435.png
security:
- kind: domain-security
  name: Elytron In Domain Security
  slug: elytron-in-domain-security
  summary_line: TLSv1.3
slug: elytron-in
tags:
- Company
- Artificial Intelligence
- E-Commerce
- Software-as-a-Service
- Retail
website: https://elytron.in/
---
