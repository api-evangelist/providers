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
  score: 0.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/11agents-ai/mcp/11agents-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/11agents-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/11agents-ai/well-known/11agents-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/11agents-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/11agents-ai/hosts/11agents-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/11agents-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/11agents-ai/vendors/11agents-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/11agents-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/11agents-ai/packages/11agents-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/11agents-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/11agents-ai/packages/11agents-ai-packages.yml
  title: ''
  type: Packages
  url: packages/11agents-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/11agents-ai/security/11agents-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/11agents-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://11agents.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://11agents.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://11agents.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://11agents.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://11agents.ai/login
- group: operate
  title: ''
  type: Support
  url: https://11agents.ai/#faq
coverage:
  checked: '2026-10-31'
  detail: The site provides product information but no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://11agents.ai/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: 11agents is a startup offering a suite of eleven specialized AI agents that handle every growth marketing channel. Each agent runs on a dedicated desktop device and is offered as a one‑time hire for $999 per year, including hardware and the first year of service. The product launches on Kickstarter in Q3 2026 and aims to simplify GTM operations for businesses by providing AI‑driven SEO, social, advertising, and content agents. The company’s website presents the product details, pricing, FAQ, privacy policy, and terms of service.
image: https://11agents.ai/hero-hardware.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.11agents.ai.
  name: 11agents MCP Server
  slug: 11agents-ai-mcp-yml
modified: '2026-10-31'
name: 11agents
nav: Providers
network: true
overview: '11agents is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Automation, Software-as-a-Service, and Startups.


  11agents'' developer surface includes pricing, signup flow, support, and 10 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 11Agents Ai Domain Security
  slug: 11agents-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 11agents-ai
tags:
- Artificial Intelligence
- Marketing
- Automation
- Software-as-a-Service
- Startups
- Go-To-Market
website: https://11agents.ai/
---
