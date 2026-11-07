---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Autoview's API for trading automation, accessed via the MCP endpoint.
  name: Autoview API
  slug: autoview-api
- baseURL: https://api.autoview.com
  baseurl_source: declared
  description: 'Autoview API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Autoview API
  slug: autoview-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/autoview-com/plans/autoview-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autoview-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/autoview-com/rules/autoview-com-rules.yml
  title: ''
  type: Spectral
  url: rules/autoview-com-rules.yml
- group: design
  href: https://artifacts.apis.io/autoview-com/json-ld/autoview-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/autoview-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/autoview-com/vocabulary/autoview-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autoview-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/autoview-com/data-model/autoview-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autoview-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/autoview-com/cli/autoview-com-cli.yml
  title: ''
  type: CLI
  url: cli/autoview-com-cli.yml
- group: start
  href: https://artifacts.apis.io/autoview-com/sandbox/autoview-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/autoview-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/autoview-com/conformance/autoview-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autoview-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autoview-com/llms/autoview-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoview-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/autoview-com/mcp/autoview-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/autoview-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/autoview-com/well-known/autoview-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autoview-com-security.txt
- group: agent
  href: https://artifacts.apis.io/autoview-com/well-known/autoview-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autoview-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/autoview-com/hosts/autoview-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoview-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/autoview-com/vendors/autoview-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autoview-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autoview.com/terms-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.autoview.com
- group: auth
  title: ''
  type: Security
  url: https://autoview.com/security/
- group: start
  title: ''
  type: Sandbox
  url: https://autoview.com/sandbox/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autoview.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://autoview.com/guides/mcp-getting-started/
- group: auth
  href: https://artifacts.apis.io/autoview-com/security/autoview-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autoview-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/autoview-com/security/autoview-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoview-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autoview.com/
- group: docs
  title: ''
  type: Documentation
  url: https://autoview.com/guides/
- group: commercial
  title: ''
  type: Pricing
  url: https://autoview.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://autoview.com/register/
- group: start
  title: ''
  type: Login
  url: https://autoview.com/login/
created: '2026-11-02'
description: Autoview provides a webhook-driven automation platform that connects trading signals from sources like TradingView, custom scripts, Zapier, or AI agents to over 20 brokers and exchanges. Running in the cloud 24/7, it turns alerts into real trades instantly, offering free tiers and paid plans for traders seeking reliable, low-latency execution across crypto, forex, and futures markets.
image: https://autoview.com/img/logo/logo-orange-white.png
json_schemas:
- name: GetSpotCurrencyPairsResponse
  property_count: 1
  slug: autoview-com-get-spot-currency-pairs-response
- name: PostMcpHttp11Request
  property_count: 4
  slug: autoview-com-post-mcp-http11-request
jsonld:
- class_count: 2
  name: Autoview Com Context
  property_count: 5
  slug: autoview-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.autoview.com.
  name: Autoview MCP Server
  slug: autoview-com-mcp-yml
modified: '2026-11-02'
name: Autoview
nav: Providers
network: true
overview: 'Autoview is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Trading, Automation, Webhook, and Cryptocurrency.


  The Autoview catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Autoview''s developer surface includes CLI, sandbox, getting-started guide, documentation, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Autoview Com Plans Pricing
  plan_count: 4
  slug: autoview-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Autoview Com Rate Limits
  slug: autoview-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Autoview API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: autoview-com-rules
scopes:
- name: Autoview Com Scopes
  scope_count: 0
  slug: autoview-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 21.4
    discoverability: 65.0
    operational_transparency: 13.2
  previous_composite: 43.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 39.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Autoview Com Authentication
  slug: autoview-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Autoview Com Domain Security
  slug: autoview-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Autoview Com Vulnerability Disclosure
  slug: autoview-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: autoview-com
tags:
- Finance
- Trading
- Automation
- Webhook
- Cryptocurrency
website: https://autoview.com/
---
