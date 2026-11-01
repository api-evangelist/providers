---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Mudko's Agent Ready Kit enabling AI assistants to interact with business websites. Provides endpoints for scanning sites, deploying agent‑ready files, and verifying readiness.
  name: Mudko Agent Ready Kit API
  slug: mudko-agent-ready-kit-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/mudko-com/plans/mudko-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mudko-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/mudko-com/llms/mudko-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mudko-com-llms.txt
- group: other
  href: https://artifacts.apis.io/mudko-com/a2a/mudko-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mudko-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/mudko-com/mcp/mudko-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mudko-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mudko-com/well-known/mudko-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mudko-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/mudko-com/hosts/mudko-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mudko-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/mudko-com/vendors/mudko-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mudko-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mudko-com/security/mudko-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mudko-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mudko.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mudko.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://mudko.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mudko.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mudko.com/terms
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mudko.com/tools
coverage:
  checked: '2026-10-30'
  detail: Mudko provides an MCP endpoint but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is publicly available.
  evidence:
  - status: 200
    url: https://mudko.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: 'Mudko provides an Agent Ready Kit that enables AI assistants like ChatGPT, Claude, and Perplexity to interact with a business website. The service scans, fixes, and generates agent‑callable files, offering a three‑step process: scanning the site, deploying agent‑ready files (via WordPress plugin, Cloudflare Worker, or direct deployment), and verifying the agent readiness level. Mudko’s platform aims to improve customer engagement by allowing AI agents to answer queries, book services, and provide quotes directly from the website, positioning itself as a bridge between traditional web content and conversational AI interfaces.'
image: https://mudko.com/opengraph-image?4e13062399a78431
layout: provider
mcp_servers:
- description: Remote MCP server at mudko.com.
  name: mudko-com MCP Server
  slug: mudko-com-mcp-yml
modified: '2026-10-30'
name: mudko-com
nav: Providers
network: true
overview: 'mudko-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, AgentReady, WebTools, and Automation.


  mudko-com''s developer surface includes documentation, pricing, and 12 more developer resources.'
plans:
- name: Mudko Com Plans Pricing
  plan_count: 1
  slug: mudko-com-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mudko Com Domain Security
  slug: mudko-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: mudko-com
tags:
- Company
- AI
- AgentReady
- WebTools
- Automation
website: https://mudko.com/
---
