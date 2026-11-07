---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Catalyst Edge provides a SEC filing intelligence platform that scans every SEC EDGAR filing overnight. Users can explore results via a live scanner interface or the 3D Cerebro HUD.
  name: Catalyst Edge Filing Events API
  slug: catalyst-edge-filing-events-api
- baseURL: https://api.catalystedgescanner.com
  baseurl_source: declared
  description: 'Catalyst Edge API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Catalyst Edge API
  slug: catalystedgescanner-com-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/catalystedgescanner-com/plans/catalystedgescanner-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/catalystedgescanner-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/catalystedgescanner-com/rules/catalystedgescanner-com-rules.yml
  title: ''
  type: Spectral
  url: rules/catalystedgescanner-com-rules.yml
- group: design
  href: https://artifacts.apis.io/catalystedgescanner-com/json-ld/catalystedgescanner-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/catalystedgescanner-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/catalystedgescanner-com/vocabulary/catalystedgescanner-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/catalystedgescanner-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/catalystedgescanner-com/data-model/catalystedgescanner-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/catalystedgescanner-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/catalystedgescanner-com/cli/catalystedgescanner-com-cli.yml
  title: ''
  type: CLI
  url: cli/catalystedgescanner-com-cli.yml
- group: design
  href: https://artifacts.apis.io/catalystedgescanner-com/conformance/catalystedgescanner-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/catalystedgescanner-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/catalystedgescanner-com/llms/catalystedgescanner-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catalystedgescanner-com-llms.txt
- group: other
  href: https://artifacts.apis.io/catalystedgescanner-com/a2a/catalystedgescanner-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/catalystedgescanner-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/catalystedgescanner-com/mcp/catalystedgescanner-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/catalystedgescanner-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/catalystedgescanner-com/well-known/catalystedgescanner-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/catalystedgescanner-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/catalystedgescanner-com/hosts/catalystedgescanner-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catalystedgescanner-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/catalystedgescanner-com/vendors/catalystedgescanner-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catalystedgescanner-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://catalystedgescanner.com/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://catalystedgescanner.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://catalystedgescanner.com/status/
- group: auth
  title: ''
  type: Security
  url: https://catalystedgescanner.com/security/
- group: build
  title: ''
  type: SDKs
  url: https://catalystedgescanner.com/sdk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catalystedgescanner.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://catalystedgescanner.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://catalystedgescanner.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://catalystedgescanner.com/developers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://catalystedgescanner.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://catalystedgescanner.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://catalystedgescanner.com/blog/short-squeeze-setup-checklist/
- group: auth
  href: https://artifacts.apis.io/catalystedgescanner-com/security/catalystedgescanner-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catalystedgescanner-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catalystedgescanner.com/
coverage:
  checked: '2026-11-04'
  detail: OpenAPI file at /openapi.json describes a different product and does not belong to Catalyst Edge.
  evidence:
  - status: 200
    url: https://catalystedgescanner.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Catalyst Edge provides a SEC filing intelligence platform that scans every SEC EDGAR filing overnight. It scores stocks using a multi‑factor catalyst model considering filing type, sentiment, recency, and macro factors, delivering top picks for free by 4 AM ET. Users can explore results via a live scanner interface or the 3D Cerebro HUD, enabling deeper insight into market catalysts.
image: https://catalystedgescanner.com/og/landing.png
json_schemas:
- name: GetV1DailyResponse
  property_count: 16
  slug: catalystedgescanner-com-get-v1-daily-response
- name: PostApiV1FilingRulesRequest
  property_count: 3
  slug: catalystedgescanner-com-post-api-v1-filing-rules-request
- name: PostApiV1FilingSignupRequest
  property_count: 1
  slug: catalystedgescanner-com-post-api-v1-filing-signup-request
- name: PostApiV1FilingUpgradeRequest
  property_count: 1
  slug: catalystedgescanner-com-post-api-v1-filing-upgrade-request
jsonld:
- class_count: 4
  name: Catalystedgescanner Com Context
  property_count: 20
  slug: catalystedgescanner-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at catalystedgescanner.com.
  name: Catalyst Edge MCP Server
  slug: catalystedgescanner-com-mcp-yml
modified: '2026-11-04'
name: Catalyst Edge
nav: Providers
network: true
overview: 'Catalyst Edge is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, SEC, Market Data, Analytics, and Platform.


  The Catalyst Edge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Catalyst Edge''s developer surface includes CLI, pricing, changelog, engineering blog, getting-started guide, and 22 more developer resources.'
plans:
- name: Catalystedgescanner Com Plans Pricing
  plan_count: 6
  slug: catalystedgescanner-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Catalyst Edge API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: catalystedgescanner-com-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 51.3
    contract_governance: 35.6
    contract_quality: 23.5
    developer_ergonomics: 26.2
    discoverability: 57.5
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Catalystedgescanner Com Domain Security
  slug: catalystedgescanner-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: catalystedgescanner-com
tags:
- Finance
- SEC
- Market Data
- Analytics
- Platform
website: https://catalystedgescanner.com/
---
