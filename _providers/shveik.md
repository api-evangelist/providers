---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
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
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.4
  scored_at: '2026-10-31'
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
artifact_total: 17
common:
- group: commercial
  href: https://artifacts.apis.io/shveik/finops/shveik-finops.yml
  title: ''
  type: FinOps
  url: finops/shveik-finops.yml
- group: agent
  href: https://artifacts.apis.io/shveik/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/shveik/well-known/shveik-agvps-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shveik-agvps-security.txt
- group: auth
  href: https://artifacts.apis.io/shveik/well-known/shveik-agproxy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shveik-agproxy-security.txt
- group: auth
  href: https://artifacts.apis.io/shveik/well-known/shveik-agpay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shveik-agpay-security.txt
- group: auth
  href: https://artifacts.apis.io/shveik/well-known/shveik-agmail-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shveik-agmail-security.txt
- group: auth
  href: https://artifacts.apis.io/shveik/well-known/shveik-agdata-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shveik-agdata-security.txt
- group: build
  href: https://artifacts.apis.io/shveik/integrations/shveik-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/shveik-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/shveik/capabilities/shveik-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/shveik-capability-edges.yml
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
  href: https://artifacts.apis.io/shveik/rate-limits/shveik-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shveik-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/shveik/agentic-access/shveik-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shveik-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/shveik/plans/shveik-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shveik-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/shveik/rules/shveik-rules.yml
  title: ''
  type: Spectral
  url: rules/shveik-rules.yml
- group: design
  href: https://artifacts.apis.io/shveik/json-ld/shveik-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shveik-context.jsonld
- group: design
  href: https://artifacts.apis.io/shveik/vocabulary/shveik-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shveik-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/shveik/data-model/shveik-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shveik-data-model.yml
- group: design
  href: https://artifacts.apis.io/shveik/conventions/shveik-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/shveik-conventions.yml
- group: design
  href: https://artifacts.apis.io/shveik/conventions/shveik-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shveik-conventions.yml
- group: design
  href: https://artifacts.apis.io/shveik/errors/shveik-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shveik-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shveik/conformance/shveik-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shveik-conformance.yml
- group: agent
  href: https://artifacts.apis.io/shveik/llms/shveik-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shveik-llms.txt
- group: other
  href: https://artifacts.apis.io/shveik/a2a/shveik-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/shveik-a2a.yml
- group: agent
  href: https://artifacts.apis.io/shveik/well-known/shveik-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shveik-well-known.yml
- group: other
  href: https://artifacts.apis.io/shveik/hosts/shveik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shveik-hosts.yml
- group: auth
  href: https://artifacts.apis.io/shveik/authentication/shveik-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shveik-authentication.yml
- group: auth
  href: https://artifacts.apis.io/shveik/security/shveik-domain-security.yml
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
description: Shveik crafts quality software with a focus on simplicity and functionality. It specializes in web development, desktop development, solution architecture, consulting, and AI & Machine Learning. The company operates five pay-per-call APIs for AI agents, billed in stablecoins via x402 and MPP, requiring no account or subscription. The APIs include agdata for web data extraction (Markdown, screenshots, transcripts, maps, social data), agproxy for residential proxy packs, agvps for monthly Linux servers, agmail for hourly email inboxes with OTP extraction, and agpay for escrow-style holds between agents. All APIs provide OpenAPI 3.1 contracts and remote MCP servers.
finops:
- has_sources: true
  method: derived
  name: Shveik Finops
  primary_unit: ''
  service_category: ''
  slug: shveik-finops
  template: true
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


  shveik''s developer surface includes authentication, documentation, pricing, support, engineering blog, API reference, and 33 more developer resources.'
plans:
- name: Shveik Plans Pricing
  plan_count: 1
  slug: shveik-plans-pricing
random_paper: 2
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
  composite: 47.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 70.2
    catalog_earned_first_party: 16.0
    catalog_gap: 44.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 54.4
    developer_ergonomics: 37.5
    discoverability: 73.3
    operational_transparency: 31.6
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shveik/shveik-2026-10-11T125832.png
security:
- kind: authentication
  name: Shveik Authentication
  slug: shveik-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Shveik Domain Security
  slug: shveik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: shveik-scrape-amazon-product-and-reviews
  slug: shveik-scrape-amazon-product-and-reviews
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
