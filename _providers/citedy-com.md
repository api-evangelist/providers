---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public contract for Citedy agent integrations.
  name: Citedy Agent API
  slug: citedy-agent-api
artifact_total: 6
asyncapis:
- description: ''
  name: Citedy Com Webhooks
  slug: citedy-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/citedy-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/citedy-com/plans/citedy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citedy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/citedy-com/asyncapi/citedy-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/citedy-com-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/citedy-com/authentication/citedy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/citedy-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/citedy-com/conformance/citedy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citedy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citedy-com/llms/citedy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citedy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/citedy-com/mcp/citedy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/citedy-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/citedy-com/well-known/citedy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citedy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/citedy-com/hosts/citedy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citedy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/citedy-com/vendors/citedy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citedy-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/citedy-com/packages/citedy-com-packages.yml
  title: ''
  type: SDKs
  url: packages/citedy-com-packages.yml
- group: build
  href: https://artifacts.apis.io/citedy-com/packages/citedy-com-packages.yml
  title: ''
  type: Packages
  url: packages/citedy-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.citedy.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Citedy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.citedy.com/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://www.citedy.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/citedy-com/security/citedy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citedy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citedy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.citedy.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.citedy.com/docs/api-reference/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.citedy.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.citedy.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.citedy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citedy.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://citedy.com/api/mcp
  - status: 401
    url: https://www.citedy.com/api/mcp
  - status: 200
    url: https://citedy.com/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Citedy provides an AI‑native content platform that automates SEO, content creation, and distribution using autonomous agents. The service combines trend analysis, competitor research, and multi‑channel publishing into a single workflow, targeting solo founders and small teams seeking to dominate search visibility without juggling multiple tools.
image: https://www.citedy.com/logo_opengraph.webp
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.citedy.com requiring an API key.
  name: Citedy MCP Server
  slug: citedy-com-mcp-yml
modified: '2026-11-03'
name: Citedy
nav: Providers
network: true
overview: 'Citedy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, SEO, Content Automation, Agents, and Platform.


  The Citedy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Citedy''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Citedy Com Plans Pricing
  plan_count: 4
  slug: citedy-com-plans-pricing
random_paper: 22
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 45.7
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Citedy Com Authentication
  slug: citedy-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Citedy Com Domain Security
  slug: citedy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citedy-com
tags:
- Artificial Intelligence
- SEO
- Content Automation
- Agents
- Platform
website: https://citedy.com/
---
