---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for automated image, PDF, and video generation
  name: Orshot API
  slug: orshot-api
artifact_total: 6
asyncapis:
- description: ''
  name: Orshot Com Webhooks
  slug: orshot-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/orshot-com/plans/orshot-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orshot-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/orshot-com/asyncapi/orshot-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/orshot-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/orshot-com/changelog/orshot-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/orshot-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/orshot-com/authentication/orshot-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/orshot-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/orshot-com/conformance/orshot-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orshot-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/orshot-com/llms/orshot-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orshot-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/orshot-com/mcp/orshot-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/orshot-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/orshot-com/well-known/orshot-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/orshot-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/orshot-com/hosts/orshot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orshot-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/orshot-com/vendors/orshot-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orshot-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orshot.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orshot.com/privacy
- group: start
  title: ''
  type: Login
  url: https://orshot.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://orshot.com/blog/category/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://orshot.com/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://orshot.com/docs/partner-program/getting-started
- group: auth
  href: https://artifacts.apis.io/orshot-com/security/orshot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orshot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orshot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://orshot.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://orshot.com/docs/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://orshot.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://orshot.com/blog
- group: operate
  title: ''
  type: Support
  url: https://orshot.com/help
created: '2026-10-30'
description: Orshot provides an API for automated image, PDF, and video generation, enabling developers and AI agents to create media assets programmatically. The platform offers template-based rendering, approval flows, and integrations with tools like n8n, Make, Zapier, and popular AI agents. It supports a wide range of use cases from marketing content creation to video production, with a focus on scalability and ease of integration.
image: https://api.orshot.com/v1/studio/dynamic-url/orshot-home.jpg?templateId=16224&sign=0d403b27a1710d2d&v=20260912
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.orshot.com.
  name: orshot-com MCP Server
  slug: orshot-com-mcp-yml
modified: '2026-10-30'
name: orshot-com
nav: Providers
network: true
overview: 'orshot-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Automation, and Artificial Intelligence.


  The orshot-com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  orshot-com''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Orshot Com Plans Pricing
  plan_count: 6
  slug: orshot-com-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 34.5
    discoverability: 56.7
    operational_transparency: 15.8
  previous_composite: 49.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/orshot-com/orshot-com-2026-11-03T140735.png
security:
- kind: authentication
  name: Orshot Com Authentication
  slug: orshot-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Orshot Com Domain Security
  slug: orshot-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orshot-com
tags:
- Company
- Media
- Automation
- Artificial Intelligence
website: https://orshot.com/
---
