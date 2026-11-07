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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Vlastná databáza európskych subjektov (59M+) naprieč 23 živými trhmi (FR, GB, RO, SK, UA, GR, CZ, BE, NO, IE, FI, CH, PL, AT, CY, LT, LV, EE, SI, ES, IT, NL, HR) nad otvorenými dátami + enrichment (BI
  name: Entyrix API
  slug: entyrix-api
artifact_total: 13
asyncapis:
- description: ''
  name: Entyrix Com Webhooks
  slug: entyrix-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/entyrix-com/rules/entyrix-com-rules.yml
  title: ''
  type: Spectral
  url: rules/entyrix-com-rules.yml
- group: design
  href: https://artifacts.apis.io/entyrix-com/json-ld/entyrix-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/entyrix-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/entyrix-com/vocabulary/entyrix-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/entyrix-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/entyrix-com/asyncapi/entyrix-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/entyrix-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/entyrix-com/rate-limits/entyrix-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/entyrix-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/entyrix-com/plans/entyrix-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/entyrix-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/entyrix-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/entyrix-com/data-model/entyrix-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/entyrix-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://entyrix.com/security
- group: auth
  href: https://artifacts.apis.io/entyrix-com/authentication/entyrix-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/entyrix-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/entyrix-com/scopes/entyrix-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/entyrix-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/entyrix-com/lifecycle/entyrix-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/entyrix-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/entyrix-com/errors/entyrix-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/entyrix-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/entyrix-com/conformance/entyrix-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/entyrix-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/entyrix-com/llms/entyrix-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/entyrix-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/entyrix-com/mcp/entyrix-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/entyrix-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/entyrix-com/well-known/entyrix-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/entyrix-com-security.txt
- group: auth
  href: https://artifacts.apis.io/entyrix-com/well-known/entyrix-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/entyrix-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/entyrix-com/well-known/entyrix-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/entyrix-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/entyrix-com/hosts/entyrix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/entyrix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/entyrix-com/vendors/entyrix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/entyrix-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/entyrix-com/packages/entyrix-com-packages.yml
  title: ''
  type: SDKs
  url: packages/entyrix-com-packages.yml
- group: build
  href: https://artifacts.apis.io/entyrix-com/packages/entyrix-com-packages.yml
  title: ''
  type: Packages
  url: packages/entyrix-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://entyrix.com/security
- group: start
  title: ''
  type: Login
  url: https://entyrix.com/en/login
- group: auth
  href: https://artifacts.apis.io/entyrix-com/security/entyrix-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/entyrix-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/entyrix-com/security/entyrix-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/entyrix-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/entyrix-com/security/entyrix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/entyrix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://entyrix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://entyrix.com/api/v1/docs
- group: docs
  title: ''
  type: Documentation
  url: https://entyrix.com/api/v1/docs
- group: docs
  title: ''
  type: APIReference
  url: https://entyrix.com/api/v1/public/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://entyrix.com/api/v1/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://entyrix.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://entyrix.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://entyrix.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://entyrix.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://entyrix.com/status
created: '2026-10-30'
description: Entyrix provides European business data compliance and KYC services via a REST API, offering company identity, ownership, sanctions, credit scoring, insolvency monitoring, NIS2 scope checks, public contract and EU fund data, with quickstart guides, OpenAPI documentation, and data feeds. The platform aggregates registers from 23 markets, delivering up-to-date information for risk assessment and regulatory compliance.
image: https://entyrix.com/api/v1/public/favicon.svg
jsonld:
- class_count: 4
  name: Entyrix Com Context
  property_count: 17
  slug: entyrix-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at entyrix.com.
  name: entyrix-com MCP Server
  slug: entyrix-com-mcp-yml
modified: '2026-10-30'
name: entyrix-com
nav: Providers
network: true
overview: 'entyrix-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Business Data, Compliance, KYC, and European.


  The entyrix-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  entyrix-com''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, and 32 more developer resources.'
plans:
- name: Entyrix Com Plans Pricing
  plan_count: 5
  slug: entyrix-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 9
  name: Entyrix Com Rate Limits
  slug: entyrix-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: entyrix-com API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: entyrix-com-rules
scopes:
- name: Entyrix Com Scopes
  scope_count: 3
  slug: entyrix-com-scopes
  summary_line: 3 scopes
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 69.8
    catalog_earned_first_party: 24.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.0
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 49.4
    developer_ergonomics: 42.3
    discoverability: 56.7
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 67.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/entyrix-com/entyrix-com-2026-11-03T131543.png
security:
- kind: authentication
  name: Entyrix Com Authentication
  slug: entyrix-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Entyrix Com Domain Security
  slug: entyrix-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Entyrix Com Vulnerability Disclosure
  slug: entyrix-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Entyrix Com Trust Center
  slug: entyrix-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: example-skill
  slug: entyrix-com-example-skill
slug: entyrix-com
tags:
- Business Data
- Compliance
- KYC
- European
website: https://entyrix.com/
---
