---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: 1211Holding Com Agentic Access
  operation_count: 3
  slug: 1211holding-com-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://1211holding.com
  baseurl_source: declared
  description: The Art API from 1211 — 1 operation(s) for art.
  name: 1211 Art API
  slug: 1211holding-com-art-api
- baseURL: https://1211holding.com
  baseurl_source: declared
  description: The Catalog API from 1211 — 1 operation(s) for catalog.
  name: 1211 Catalog API
  slug: 1211holding-com-catalog-api
- baseURL: https://1211holding.com
  baseurl_source: declared
  description: The Designs API from 1211 — 1 operation(s) for designs.
  name: 1211 Designs API
  slug: 1211holding-com-designs-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/1211holding-com/agentic-access/1211holding-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/1211holding-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/1211holding-com/rate-limits/1211holding-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/1211holding-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/1211holding-com/plans/1211holding-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/1211holding-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/1211holding-com/rules/1211holding-com-rules.yml
  title: ''
  type: Spectral
  url: rules/1211holding-com-rules.yml
- group: design
  href: https://artifacts.apis.io/1211holding-com/json-ld/1211holding-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/1211holding-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/1211holding-com/vocabulary/1211holding-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/1211holding-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/1211holding-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/1211holding-com/data-model/1211holding-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/1211holding-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/1211holding-com/errors/1211holding-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/1211holding-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/1211holding-com/conformance/1211holding-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/1211holding-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/1211holding-com/llms/1211holding-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/1211holding-com-llms.txt
- group: build
  href: https://artifacts.apis.io/1211holding-com/mcp/1211holding-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/1211holding-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/1211holding-com/mcp/1211holding-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/1211holding-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/1211holding-com/hosts/1211holding-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1211holding-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/1211holding-com/packages/1211holding-com-packages.yml
  title: ''
  type: SDKs
  url: packages/1211holding-com-packages.yml
- group: build
  href: https://artifacts.apis.io/1211holding-com/packages/1211holding-com-packages.yml
  title: ''
  type: Packages
  url: packages/1211holding-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/1211holding-com/security/1211holding-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1211holding-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1211holding.com/
- group: docs
  title: ''
  type: Documentation
  url: https://1211holding.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://1211holding.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://1211holding.com/make
- group: commercial
  title: ''
  type: Pricing
  url: https://1211holding.com/pricing.php
- group: start
  title: ''
  type: SignUp
  url: https://1211holding.com/signup.php
- group: start
  title: ''
  type: Login
  url: https://1211holding.com/login.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1211holding.com/legal/tos_v1.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1211holding.com/legal/privacy_v1.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/robgundling1211
created: '2026-10-31'
description: 1211 offers a print‑on‑demand service that lets anyone turn any picture into custom shirts, hoodies, hats, tumblers or tote bags. Items are printed one‑at‑a‑time after order, starting at $18, with free shipping to US addresses and no account or minimum required. Users can upload artwork directly or generate it with an AI assistant, receive a unique purchase link, and the company handles production, payment and sales tax.
image: https://1211holding.com/assets/products/tee.png
json_schemas:
- name: ArtUpload
  property_count: 2
  slug: 1211holding-com-art-upload
- name: Catalog
  property_count: 1
  slug: 1211holding-com-catalog
- name: DesignRequest
  property_count: 2
  slug: 1211holding-com-design-request
- name: Design
  property_count: 2
  slug: 1211holding-com-design
jsonld:
- class_count: 6
  name: 1211Holding Com Context
  property_count: 11
  slug: 1211holding-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at 1211holding.com.
  name: 1211 MCP Server
  slug: 1211holding-com-mcp-yml
modified: '2026-10-31'
name: '1211'
nav: Providers
network: true
overview: '1211 publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Art API, Catalog API, and Designs API. Tagged areas include Print on Demand, E-Commerce, Merchandise, and Custom Products.


  The 1211 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  1211''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, and 22 more developer resources.'
plans:
- name: 1211Holding Com Plans Pricing
  plan_count: 1
  slug: 1211holding-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: 1211Holding Com Rate Limits
  slug: 1211holding-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: 1211 API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: 1211holding-com-rules
scopes:
- name: 1211Holding Com Scopes
  scope_count: 0
  slug: 1211holding-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 27.9
    discoverability: 56.7
    operational_transparency: 34.2
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 1211Holding Com Authentication
  slug: 1211holding-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 1211Holding Com Domain Security
  slug: 1211holding-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: 1211holding-com-main
  slug: 1211holding-com-main
slug: 1211holding-com
tags:
- Print on Demand
- E-Commerce
- Merchandise
- Custom Products
website: https://1211holding.com/
---
