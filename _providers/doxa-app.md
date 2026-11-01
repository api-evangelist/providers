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
  score: 6.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/doxa-app/plans/doxa-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doxa-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/doxa-app/llms/doxa-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doxa-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/doxa-app/mcp/doxa-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/doxa-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/doxa-app/well-known/doxa-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doxa-app-security.txt
- group: agent
  href: https://artifacts.apis.io/doxa-app/well-known/doxa-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doxa-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/doxa-app/hosts/doxa-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doxa-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/doxa-app/vendors/doxa-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doxa-app-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://doxa.app/blog/way/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doxa.app/terms
- group: auth
  title: ''
  type: Security
  url: https://doxa.app/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doxa.app/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://doxa.app/grace/media
- group: start
  title: ''
  type: Login
  url: https://doxa.app/app/login
- group: auth
  href: https://artifacts.apis.io/doxa-app/security/doxa-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/doxa-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/doxa-app/security/doxa-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doxa-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doxa.app/
- group: docs
  title: ''
  type: Documentation
  url: https://doxa.app/about
- group: commercial
  title: ''
  type: Pricing
  url: https://doxa.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://doxa.app/blog/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 200
    url: https://doxa.app/mcp/v1
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Doxa is a prophetic encouragement app that provides Bible resources, courses, and community features for churches, youth leaders, and individuals seeking spiritual growth. The platform offers a range of tools including daily devotionals, AI‑driven Christian insights, and a marketplace of grace‑focused content. It aims to help users hear, prophesy, record, test, remember, and trust in their faith journey through an engaging mobile and web experience.
image: https://doxa.app/images/og-image.png?v=852cca4faf
layout: provider
mcp_servers:
- description: Remote MCP server at doxa.app.
  name: doxa-app MCP Server
  slug: doxa-app-mcp-yml
modified: '2026-10-30'
name: doxa-app
nav: Providers
network: true
overview: 'doxa-app is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Faith, Community, MobileApp, BibleResources, and Prophetic.


  doxa-app''s developer surface includes documentation, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Doxa App Plans Pricing
  plan_count: 2
  slug: doxa-app-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doxa App Domain Security
  slug: doxa-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Doxa App Vulnerability Disclosure
  slug: doxa-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: doxa-app
tags:
- Faith
- Community
- MobileApp
- BibleResources
- Prophetic
website: https://doxa.app/
---
