---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Campiamo provides campsite management software with online bookings, payments, and channel sync.
  name: Campiamo API
  slug: campiamo-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/campiamo-com/plans/campiamo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/campiamo-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/campiamo-com/security/campiamo-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/campiamo-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/campiamo-com/llms/campiamo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/campiamo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/campiamo-com/mcp/campiamo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/campiamo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-opendata-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-opendata-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-open-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-open-data-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-developers-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-developer-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-datahub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-datahub-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-data-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-apis-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-api-security.txt
- group: auth
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-api-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campiamo-com-api-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/campiamo-com/well-known/campiamo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/campiamo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/campiamo-com/hosts/campiamo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/campiamo-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://campiamo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://campiamo.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://campiamo.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://campiamo.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://campiamo.com/docs/account/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.campiamo.com/
- group: auth
  href: https://artifacts.apis.io/campiamo-com/security/campiamo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/campiamo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/campiamo-com/security/campiamo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/campiamo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://campiamo.com/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages exist but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found.
  evidence:
  - status: 302
    url: https://api.campiamo.com/openapi.json
  - status: 200
    url: https://apis.campiamo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Campiamo provides campsite management software for UK and European campsites, glamping sites and holiday parks. It offers online bookings, payments, channel sync, a free website, and a 0% commission model with free and paid plans.
image: https://campiamo.com/images/og-default.png?v=7e9f1d26
layout: provider
mcp_servers:
- description: Remote MCP server at campiamo.com.
  name: Campiamo MCP Server
  slug: campiamo-com-mcp-yml
modified: '2026-11-04'
name: Campiamo
nav: Providers
network: true
overview: 'Campiamo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Campsite Management, Booking, Software, United Kingdom, and Europe.


  Campiamo''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 23 more developer resources.'
plans:
- name: Campiamo Com Plans Pricing
  plan_count: 3
  slug: campiamo-com-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Campiamo Com Domain Security
  slug: campiamo-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Campiamo Com Vulnerability Disclosure
  slug: campiamo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: campiamo-com
tags:
- Campsite Management
- Booking
- Software
- United Kingdom
- Europe
website: https://campiamo.com/
---
