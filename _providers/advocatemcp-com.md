---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: See how Advocate turns your business information into a structured profile that AI assistants can find, understand, and cite, without promising rankings or placement.
  name: Advocate API
  slug: advocate-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/advocatemcp-com/plans/advocatemcp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/advocatemcp-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/advocatemcp-com/llms/advocatemcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/advocatemcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/advocatemcp-com/mcp/advocatemcp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/advocatemcp-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/advocatemcp-com/hosts/advocatemcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/advocatemcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/advocatemcp-com/vendors/advocatemcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/advocatemcp-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/advocatemcp-com/security/advocatemcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/advocatemcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advocatemcp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.advocatemcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.advocatemcp.com/how-it-works
- group: start
  title: ''
  type: GettingStarted
  url: https://app.advocatemcp.com/request-access
- group: start
  title: ''
  type: SignUp
  url: https://app.advocatemcp.com/request-access
- group: commercial
  title: ''
  type: Pricing
  url: https://app.advocatemcp.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://app.advocatemcp.com/contact?intent=general
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.advocatemcp.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.advocatemcp.com/terms
coverage:
  checked: '2026-11-01'
  detail: No machine-readable API contract (OpenAPI, GraphQL, AsyncAPI, or MCP spec) could be retrieved; GET returned 405 and POST returned 406.
  evidence:
  - status: 405
    url: https://advocatemcp.com/mcp
  - status: 406
    url: https://advocatemcp.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Advocate helps businesses get found by AI. As search shifts from Google results to AI assistants like ChatGPT, Claude, Perplexity, and Gemini, most businesses are invisible to them. Advocate gives each business its own live connection point that serves accurate, structured business information directly to AI systems when customers ask, hours, services, pricing, and more, and routes the resulting leads back to the business. We work with businesses of all kinds, local service providers like plumbers, HVAC contractors, electricians, and dentists, as well as e-commerce and online businesses, who want to show up when customers ask AI for recommendations, not just when they search Google.
image: https://app.advocatemcp.com/opengraph-image?123d2b4c6d58b1d1
layout: provider
mcp_servers:
- description: Remote MCP server at advocatemcp.com.
  name: Advocate MCP Server
  slug: advocatemcp-com-mcp-yml
modified: '2026-10-31'
name: Advocate
nav: Providers
network: true
overview: 'Advocate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Business, Directory, Local, and Services.


  Advocate''s developer surface includes documentation, getting-started guide, signup flow, pricing, support, and 10 more developer resources.'
plans:
- name: Advocatemcp Com Plans Pricing
  plan_count: 3
  slug: advocatemcp-com-plans-pricing
random_paper: 11
scopes:
- name: Advocatemcp Com Scopes
  scope_count: 0
  slug: advocatemcp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 29.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Advocatemcp Com Authentication
  slug: advocatemcp-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Advocatemcp Com Domain Security
  slug: advocatemcp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: advocatemcp-com
tags:
- Artificial Intelligence
- Business
- Directory
- Local
- Services
website: https://advocatemcp.com/
---
