---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bestprintondemand Agentic Access
  operation_count: 4
  slug: bestprintondemand-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://bestprintondemand.co/api/v1
  baseurl_source: declared
  description: Find print-on-demand products, get every supplier's base price, US shipping and total for one product (with profit at a sell price after a sales channel's fees), compare two suppliers, and list attrib
  name: BestPrintOnDemand API
  slug: bestprintondemand-print-on-demand-costs-api
artifact_total: 7
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/agentic-access/bestprintondemand-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bestprintondemand-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/rules/bestprintondemand-rules.yml
  title: ''
  type: Spectral
  url: rules/bestprintondemand-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/json-ld/bestprintondemand-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bestprintondemand-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/vocabulary/bestprintondemand-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bestprintondemand-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/data-model/bestprintondemand-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bestprintondemand-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/errors/bestprintondemand-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bestprintondemand-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/conformance/bestprintondemand-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bestprintondemand-conformance.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://bestprintondemand.co/price-changes
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/llms/bestprintondemand-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bestprintondemand-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/hosts/bestprintondemand-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestprintondemand-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/vendors/bestprintondemand-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestprintondemand-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bestprintondemand.co/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bestprintondemand.co/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://bestprintondemand.co/blog
- group: docs
  title: ''
  type: APIReference
  url: https://bestprintondemand.co/data
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/security/bestprintondemand-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestprintondemand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestprintondemand.co
- group: docs
  title: ''
  type: Documentation
  url: https://bestprintondemand.co/data#api
- group: other
  title: ''
  type: APIsJSON
  url: https://bestprintondemand.co/apis.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestprintondemand/refs/heads/main/mcp/bestprintondemand-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bestprintondemand-mcp.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://bestprintondemand.co/openapi.json
created: '2026-10-06'
description: BestPrintOnDemand provides a live, keyless JSON API for on-demand printing services. Their API offers endpoints to list products, retrieve cost estimates, and compare pricing across major POD suppliers such as Printful, Printify, and Gelato. The service includes an OpenAPI 3.2 specification at /openapi.json and a simple API index at /api/v1. Data is sourced with timestamps and supplier references, enabling developers to integrate real-time pricing into e‑commerce platforms and custom applications.
image: https://bestprintondemand.co/opengraph-image
json_schemas:
- name: Answer
  property_count: 1
  slug: bestprintondemand-answer
jsonld:
- class_count: 2
  name: Bestprintondemand Context
  property_count: 2
  slug: bestprintondemand-context
layout: provider
mcp_servers:
- description: BestPrintOnDemand serves a remote Model Context Protocol server (Streamable HTTP) on its own host, listed in the official MCP Registry as co.bestprintondemand/print-on-demand-costs. No key or account;
  name: BestPrintOnDemand MCP Server
  slug: bestprintondemand-mcp-yml
modified: '2026-10-12'
name: BestPrintOnDemand
nav: Providers
network: true
overview: 'BestPrintOnDemand publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Print on Demand, Pricing, and OpenAPI.


  The BestPrintOnDemand catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BestPrintOnDemand''s developer surface includes pricing, engineering blog, API reference, documentation, and 17 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: BestPrintOnDemand API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: bestprintondemand-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 56.7
    developer_ergonomics: 19.0
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Bestprintondemand Domain Security
  slug: bestprintondemand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bestprintondemand
tags:
- Company
- Print on Demand
- Pricing
- OpenAPI
website: https://bestprintondemand.co
---
