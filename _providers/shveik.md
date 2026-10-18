---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 72
  human_in_the_loop: 0
  name: Shveik Agentic Access
  operation_count: 77
  slug: shveik-agentic-access
  summary_line: 77 operations · 72 acting
api_count: 10
apis:
- baseURL: https://agdata.shveik.dev/v1
  baseurl_source: declared
  description: Free, unpaid API metadata.
  name: shveik Discovery API
  slug: shveik-discovery-api
- baseURL: https://agdata.shveik.dev/v1
  baseurl_source: declared
  description: Synchronous data retrieval; each request completes in the HTTP response.
  name: shveik Scraping API
  slug: shveik-scraping-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://agdata.shveik.dev/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://agproxy.shveik.dev/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://agvps.shveik.dev/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://agmail.shveik.dev/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://agpay.shveik.dev/mcp
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/rate-limits/shveik-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shveik-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/agentic-access/shveik-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shveik-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/plans/shveik-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shveik-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/rules/shveik-rules.yml
  title: ''
  type: Spectral
  url: rules/shveik-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/json-ld/shveik-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shveik-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/vocabulary/shveik-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shveik-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/data-model/shveik-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shveik-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/conventions/shveik-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/shveik-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/conventions/shveik-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shveik-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/errors/shveik-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shveik-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/conformance/shveik-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shveik-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/llms/shveik-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shveik-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/a2a/shveik-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/shveik-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/well-known/shveik-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shveik-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/hosts/shveik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shveik-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/authentication/shveik-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shveik-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/security/shveik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shveik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shveik.dev
- group: docs
  title: ''
  type: Documentation
  url: https://agdata.shveik.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://agdata.shveik.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agdata.shveik.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agdata.shveik.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://agdata.shveik.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.shveik.dev
- group: docs
  title: ''
  type: APIReference
  url: https://agdata.shveik.dev/docs
created: '2026-10-09'
description: 'shveik.dev runs five pay-per-call APIs built for AI agents and paid per request in stablecoins over x402 and MPP, with no account or subscription: agdata (unblocking and web data - any URL as Markdown, screenshots, transcripts, maps and social data), agproxy (residential proxy packs and raw fetch), agvps (monthly Linux servers), agmail (hourly email inboxes with OTP extraction) and agpay (escrow-style holds between agents). Each ships an OpenAPI 3.1 contract and a remote MCP server.'
json_schemas:
- name: Error
  property_count: 2
  slug: shveik-error
jsonld:
- class_count: 1
  name: Shveik Context
  property_count: 2
  slug: shveik-context
layout: provider
mcp_servers:
- description: ''
  name: shveik MCP Server
  slug: mcp
- description: ''
  name: shveik MCP Server
  slug: mcp-2
- description: ''
  name: shveik MCP Server
  slug: mcp-3
- description: ''
  name: shveik MCP Server
  slug: mcp-4
- description: ''
  name: shveik MCP Server
  slug: mcp-5
modified: '2026-10-09'
name: shveik
nav: Providers
network: true
overview: 'shveik publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API and Scraping API. Tagged areas include Company, AI Agents, x402, Web Scraping, and Proxies.


  The shveik catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  shveik''s developer surface includes authentication, documentation, pricing, support, engineering blog, API reference, and 24 more developer resources.'
plans:
- name: Shveik Plans Pricing
  plan_count: 1
  slug: shveik-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Shveik Rate Limits
  slug: shveik-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: shveik API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: shveik-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 70.2
    catalog_earned_first_party: 16.0
    catalog_gap: 44.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 54.3
    developer_ergonomics: 35.7
    discoverability: 76.7
    operational_transparency: 21.1
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/shveik/refs/heads/main/screenshots/shveik-2026-10-11T125832.png
security:
- kind: authentication
  name: Shveik Authentication
  slug: shveik-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Shveik Domain Security
  slug: shveik-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shveik
tags:
- Company
- AI Agents
- x402
- Web Scraping
- Proxies
- Email
- VPS
- Escrow
- MCP
- Stablecoins
website: https://shveik.dev
---
