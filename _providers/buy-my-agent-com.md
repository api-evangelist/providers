---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
- description: API for accessing agents, listings and marketplace functionality as documented in the developer portal.
  name: Buy My Agent API
  slug: buy-my-agent-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/buy-my-agent-com/plans/buy-my-agent-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buy-my-agent-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/buy-my-agent-com/llms/buy-my-agent-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buy-my-agent-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/buy-my-agent-com/mcp/buy-my-agent-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buy-my-agent-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/buy-my-agent-com/well-known/buy-my-agent-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buy-my-agent-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/buy-my-agent-com/hosts/buy-my-agent-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buy-my-agent-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buy-my-agent-com/vendors/buy-my-agent-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buy-my-agent-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buy-my-agent.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.buy-my-agent.com/help
- group: auth
  title: ''
  type: Security
  url: https://www.buy-my-agent.com/categories/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buy-my-agent.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buy-my-agent.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.buy-my-agent.com/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.buy-my-agent.com/browse/audience/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.buy-my-agent.com/browse/use-case/client-onboarding/audience/consultants
- group: auth
  href: https://artifacts.apis.io/buy-my-agent-com/security/buy-my-agent-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buy-my-agent-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buy-my-agent.com/
coverage:
  checked: '2026-11-03'
  detail: Developer portal pages are rendered HTML without machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 200
    url: https://www.buy-my-agent.com/browse/audience/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Buy My Agent is a curated marketplace to list and subscribe to business-ready AI workflows. Creators keep the subscriber relationship; the platform charges a 10% commission on sales. The platform offers free agents for businesses to integrate, with a focus on AI-driven automation and workflow solutions.
image: https://www.buy-my-agent.com/opengraph-image?eec4d4180efbf320
layout: provider
mcp_servers:
- description: Remote MCP server at www.buy-my-agent.com.
  name: Buy My Agent MCP Server
  slug: buy-my-agent-com-mcp-yml
modified: '2026-11-03'
name: Buy My Agent
nav: Providers
network: true
overview: 'Buy My Agent is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Automation, Agents, and Business.


  Buy My Agent''s developer surface includes support, pricing, documentation, getting-started guide, and 12 more developer resources.'
plans:
- name: Buy My Agent Com Plans Pricing
  plan_count: 1
  slug: buy-my-agent-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 56.7
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buy My Agent Com Domain Security
  slug: buy-my-agent-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buy-my-agent-com
tags:
- Artificial Intelligence
- Marketplace
- Automation
- Agents
- Business
website: https://buy-my-agent.com/
---
