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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Anteproof Com Agentic Access
  operation_count: 36
  slug: anteproof-com-agentic-access
  summary_line: 36 operations · 12 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Account API from Anteproof — 1 operation(s) for account.
  name: Anteproof Account API
  slug: anteproof-com-account-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Anchor API from Anteproof — 1 operation(s) for anchor.
  name: Anteproof Anchor API
  slug: anteproof-com-anchor-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Billing API from Anteproof — 3 operation(s) for billing.
  name: Anteproof Billing API
  slug: anteproof-com-billing-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Calibration API from Anteproof — 2 operation(s) for calibration.
  name: Anteproof Calibration API
  slug: anteproof-com-calibration-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Chain API from Anteproof — 2 operation(s) for chain.
  name: Anteproof Chain API
  slug: anteproof-com-chain-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Coverage Preview API from Anteproof — 1 operation(s) for coverage preview.
  name: Anteproof Coverage Preview API
  slug: anteproof-com-coverage-preview-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Digest API from Anteproof — 1 operation(s) for digest.
  name: Anteproof Digest API
  slug: anteproof-com-digest-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Entities API from Anteproof — 3 operation(s) for entities.
  name: Anteproof Entities API
  slug: anteproof-com-entities-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Forecasts API from Anteproof — 1 operation(s) for forecasts.
  name: Anteproof Forecasts API
  slug: anteproof-com-forecasts-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Freshness API from Anteproof — 1 operation(s) for freshness.
  name: Anteproof Freshness API
  slug: anteproof-com-freshness-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Me API from Anteproof — 9 operation(s) for me.
  name: Anteproof Me API
  slug: anteproof-com-me-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Proof API from Anteproof — 1 operation(s) for proof.
  name: Anteproof Proof API
  slug: anteproof-com-proof-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Questions API from Anteproof — 1 operation(s) for questions.
  name: Anteproof Questions API
  slug: anteproof-com-questions-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Risk API from Anteproof — 3 operation(s) for risk.
  name: Anteproof Risk API
  slug: anteproof-com-risk-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Stats API from Anteproof — 1 operation(s) for stats.
  name: Anteproof Stats API
  slug: anteproof-com-stats-api
- baseURL: https://api.anteproof.com
  baseurl_source: declared
  description: The Support API from Anteproof — 1 operation(s) for support.
  name: Anteproof Support API
  slug: anteproof-com-support-api
artifact_total: 33
common:
- group: agent
  href: https://artifacts.apis.io/anteproof-com/agentic-access/anteproof-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anteproof-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/anteproof-com/rate-limits/anteproof-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anteproof-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/anteproof-com/plans/anteproof-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anteproof-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/anteproof-com/rules/anteproof-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anteproof-com-rules.yml
- group: design
  href: https://artifacts.apis.io/anteproof-com/json-ld/anteproof-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anteproof-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/anteproof-com/vocabulary/anteproof-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anteproof-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anteproof-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anteproof-com/data-model/anteproof-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anteproof-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://anteproof.com/legal
- group: auth
  href: https://artifacts.apis.io/anteproof-com/authentication/anteproof-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anteproof-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/anteproof-com/errors/anteproof-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anteproof-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anteproof-com/conformance/anteproof-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anteproof-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anteproof-com/mcp/anteproof-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anteproof-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/anteproof-com/well-known/anteproof-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anteproof-com-security.txt
- group: auth
  href: https://artifacts.apis.io/anteproof-com/well-known/anteproof-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anteproof-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/anteproof-com/well-known/anteproof-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anteproof-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anteproof-com/hosts/anteproof-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anteproof-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anteproof-com/vendors/anteproof-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anteproof-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/anteproof-com/security/anteproof-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anteproof-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anteproof-com/security/anteproof-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anteproof-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anteproof.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anteproof.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anteproof.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://anteproof.com/docs
- group: operate
  title: ''
  type: Support
  url: https://anteproof.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://anteproof.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anteproof.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anteproof.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anteproof
created: '2026-11-01'
description: 'Anteproof provides dated probabilities that a repository will maintain its recent commit pace and publish a release within 90 days, each accompanied by a public receipt. The service helps engineers and coding agents assess dependency maintenance risk by offering two forecasts per repository: commit target achievement and release publication. Users can query the REST API or MCP server to retrieve risk scores, forecast logs, question details, and calibration records. The platform aims to improve software supply chain reliability.'
image: https://anteproof.com/favicon.png
json_schemas:
- name: AlertsBody
  property_count: 4
  slug: anteproof-com-alerts-body
- name: CheckoutBody
  property_count: 1
  slug: anteproof-com-checkout-body
- name: KeyBody
  property_count: 1
  slug: anteproof-com-key-body
- name: RiskBatchRequest
  property_count: 2
  slug: anteproof-com-risk-batch-request
- name: SupportBody
  property_count: 6
  slug: anteproof-com-support-body
- name: WatchBody
  property_count: 1
  slug: anteproof-com-watch-body
jsonld:
- class_count: 9
  name: Anteproof Com Context
  property_count: 23
  slug: anteproof-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at anteproof.com requiring an API key.
  name: Anteproof MCP Server
  slug: anteproof-com-mcp-yml
modified: '2026-11-01'
name: Anteproof
nav: Providers
network: true
overview: 'Anteproof publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Anchor API, Billing API, and 13 more. Tagged areas include Dependency, Risk Management, Analytics, Open Source, and Software.


  The Anteproof catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anteproof''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 23 more developer resources.'
plans:
- name: Anteproof Com Plans Pricing
  plan_count: 2
  slug: anteproof-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Anteproof Com Rate Limits
  slug: anteproof-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Anteproof API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: anteproof-com-rules
scopes:
- name: Anteproof Com Scopes
  scope_count: 0
  slug: anteproof-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 54.8
    developer_ergonomics: 35.0
    discoverability: 65.0
    operational_transparency: 28.9
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anteproof Com Authentication
  slug: anteproof-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Anteproof Com Domain Security
  slug: anteproof-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Anteproof Com Vulnerability Disclosure
  slug: anteproof-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: list-forecasts
  slug: anteproof-com-list-forecasts-skill
slug: anteproof-com
tags:
- Dependency
- Risk Management
- Analytics
- Open Source
- Software
website: https://anteproof.com/
---
