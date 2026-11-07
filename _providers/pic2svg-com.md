---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Pic2Svg Com Agentic Access
  operation_count: 1
  slug: pic2svg-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.pic2svg.com
  baseurl_source: declared
  description: The Trace API from pic2svg — 1 operation(s) for trace.
  name: pic2svg Trace API
  slug: pic2svg-com-trace-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/pic2svg-com/agentic-access/pic2svg-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pic2svg-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/pic2svg-com/plans/pic2svg-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pic2svg-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pic2svg-com/rules/pic2svg-com-rules.yml
  title: ''
  type: Spectral
  url: rules/pic2svg-com-rules.yml
- group: design
  href: https://artifacts.apis.io/pic2svg-com/json-ld/pic2svg-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pic2svg-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/pic2svg-com/vocabulary/pic2svg-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pic2svg-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pic2svg-com/data-model/pic2svg-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pic2svg-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/pic2svg-com/cli/pic2svg-com-cli.yml
  title: ''
  type: CLI
  url: cli/pic2svg-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/pic2svg-com/changelog/pic2svg-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pic2svg-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/pic2svg-com/errors/pic2svg-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pic2svg-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pic2svg-com/conformance/pic2svg-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pic2svg-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pic2svg-com/llms/pic2svg-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pic2svg-com-llms.txt
- group: build
  href: https://artifacts.apis.io/pic2svg-com/mcp/pic2svg-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pic2svg-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/pic2svg-com/mcp/pic2svg-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pic2svg-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pic2svg-com/well-known/pic2svg-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pic2svg-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/pic2svg-com/hosts/pic2svg-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pic2svg-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pic2svg-com/vendors/pic2svg-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pic2svg-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pic2svg.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pic2svg.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://pic2svg.com/changelog/
- group: auth
  href: https://artifacts.apis.io/pic2svg-com/security/pic2svg-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pic2svg-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pic2svg.com
- group: commercial
  title: ''
  type: Pricing
  url: https://pic2svg.com/pricing/
- group: operate
  title: ''
  type: Contact
  url: https://pic2svg.com/contact/
- group: start
  title: ''
  type: Login
  url: https://pic2svg.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://api.pic2svg.com
created: '2026-10-28'
description: pic2svg provides an online service that converts raster images such as JPG, PNG, and WebP into editable SVG vector graphics. The platform offers free conversions with no account required, while paid plans add support for PDF, EPS, AI, and DXF outputs. It targets designers, developers, and anyone needing scalable vector assets from bitmap sources.
image: https://pic2svg.com/pic2svg-card.jpg?v=20261023
jsonld:
- class_count: 1
  name: Pic2Svg Com Context
  property_count: 1
  slug: pic2svg-com-context
layout: provider
mcp_servers:
- description: ''
  name: pic2svg MCP Server
  slug: pic2svg-com-mcp-yml
modified: '2026-10-28'
name: pic2svg
nav: Providers
network: true
overview: 'pic2svg publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Trace API. Tagged areas include Company, Image Conversion, SVG, and Design Tools.


  The pic2svg catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pic2svg''s developer surface includes CLI, changelog, pricing, API reference, and 21 more developer resources.'
plans:
- name: Pic2Svg Com Plans Pricing
  plan_count: 3
  slug: pic2svg-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: pic2svg API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: pic2svg-com-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 49.3
    developer_ergonomics: 10.7
    discoverability: 63.3
    operational_transparency: 7.9
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pic2svg-com/pic2svg-com-2026-11-03T141205.png
security:
- kind: domain-security
  name: Pic2Svg Com Domain Security
  slug: pic2svg-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pic2svg-com
tags:
- Company
- Image Conversion
- SVG
- Design Tools
website: https://pic2svg.com
---
