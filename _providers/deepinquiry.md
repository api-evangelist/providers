---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Deepinquiry Agentic Access
  operation_count: 4
  slug: deepinquiry-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.deepinquiry.ai/api
  baseurl_source: declared
  description: Read-only access to the verified-facts corpus.
  name: DeepInquiry Verified Facts API (Machine Accountability Corp) Facts API
  slug: deepinquiry-facts-api
- baseURL: https://api.deepinquiry.ai/api
  baseurl_source: declared
  description: Semantic search across the corpus.
  name: DeepInquiry Verified Facts API (Machine Accountability Corp) Search API
  slug: deepinquiry-search-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/deepinquiry/agentic-access/deepinquiry-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deepinquiry-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/deepinquiry/rate-limits/deepinquiry-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deepinquiry-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/deepinquiry/plans/deepinquiry-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deepinquiry-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deepinquiry/rules/deepinquiry-rules.yml
  title: ''
  type: Spectral
  url: rules/deepinquiry-rules.yml
- group: design
  href: https://artifacts.apis.io/deepinquiry/json-ld/deepinquiry-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deepinquiry-context.jsonld
- group: design
  href: https://artifacts.apis.io/deepinquiry/vocabulary/deepinquiry-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deepinquiry-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deepinquiry/data-model/deepinquiry-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deepinquiry-data-model.yml
- group: design
  href: https://artifacts.apis.io/deepinquiry/conventions/deepinquiry-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deepinquiry-conventions.yml
- group: auth
  href: https://artifacts.apis.io/deepinquiry/authentication/deepinquiry-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deepinquiry-authentication.yml
- group: design
  href: https://artifacts.apis.io/deepinquiry/errors/deepinquiry-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deepinquiry-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deepinquiry/conformance/deepinquiry-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deepinquiry-conformance.yml
- group: other
  href: https://artifacts.apis.io/deepinquiry/overlays/deepinquiry-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/deepinquiry-openapi-overlay.yml
- group: agent
  href: https://artifacts.apis.io/deepinquiry/llms/deepinquiry-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deepinquiry-llms.txt
- group: agent
  href: https://artifacts.apis.io/deepinquiry/mcp/deepinquiry-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deepinquiry-mcp.yml
- group: agent
  href: https://artifacts.apis.io/deepinquiry/well-known/deepinquiry-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deepinquiry-well-known.yml
- group: other
  href: https://artifacts.apis.io/deepinquiry/hosts/deepinquiry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepinquiry-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepinquiry/vendors/deepinquiry-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepinquiry-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.deepinquiry.ai/signin
- group: auth
  href: https://artifacts.apis.io/deepinquiry/security/deepinquiry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepinquiry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deepinquiry.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.deepinquiry.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.deepinquiry.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.deepinquiry.ai/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deepinquiry.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deepinquiry.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deepinquiry.ai/privacy
created: '2026-10-17'
description: DeepInquiry Verified Facts API (Machine Accountability Corp) provides a curated, verifiable fact database accessible via a RESTful API. Each fact is cross‑checked against multiple sources, cited, dated, and cryptographically signed, offering users trustworthy data for applications ranging from research to product development. The service includes tiered pricing, API key authentication, and detailed usage limits, ensuring both free access for low‑volume needs and scalable plans for enterprise integration.
image: https://www.deepinquiry.ai/opengraph-image?01749e82229af5bc
json_schemas:
- name: FactList
  property_count: 2
  slug: deepinquiry-fact-list
- name: Fact
  property_count: 15
  slug: deepinquiry-fact
- name: FactWithClusters
  property_count: 16
  slug: deepinquiry-fact-with-clusters
- name: SearchResult
  property_count: 2
  slug: deepinquiry-search-result
jsonld:
- class_count: 5
  name: Deepinquiry Context
  property_count: 26
  slug: deepinquiry-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.deepinquiry.ai requiring an API key.
  name: DeepInquiry Verified Facts API (Machine Accountability Corp) MCP Server
  slug: deepinquiry-mcp-yml
modified: '2026-10-17'
name: DeepInquiry Verified Facts API (Machine Accountability Corp)
nav: Providers
network: true
overview: 'DeepInquiry Verified Facts API (Machine Accountability Corp) publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Facts API and Search API. Tagged areas include Company, Facts, Verification, and Data.


  The DeepInquiry Verified Facts API (Machine Accountability Corp) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeepInquiry Verified Facts API (Machine Accountability Corp)''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 21 more developer resources.'
plans:
- name: Deepinquiry Plans Pricing
  plan_count: 5
  slug: deepinquiry-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Deepinquiry Rate Limits
  slug: deepinquiry-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: DeepInquiry Verified Facts API (Machine Accountability Corp) API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: deepinquiry-rules
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 66.9
    developer_ergonomics: 26.2
    discoverability: 66.7
    operational_transparency: 31.6
  previous_composite: 54.9
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/deepinquiry/deepinquiry-2026-11-03T130427.png
security:
- kind: authentication
  name: Deepinquiry Authentication
  slug: deepinquiry-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Deepinquiry Domain Security
  slug: deepinquiry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: deepinquiry
tags:
- Company
- Facts
- Verification
- Data
website: https://www.deepinquiry.ai/
---
