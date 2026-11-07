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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 69.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Smklog Com Agentic Access
  operation_count: 5
  slug: smklog-com-agentic-access
  summary_line: 5 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://quote-api.smklog.com
  baseurl_source: declared
  description: Agent-prepared payment sessions completed by a human on smklog.com.
  name: SMKlog Checkout API
  slug: smklog-com-checkout-api
- baseURL: https://quote-api.smklog.com
  baseurl_source: declared
  description: Liveness.
  name: SMKlog Operations API
  slug: smklog-com-operations-api
- baseURL: https://quote-api.smklog.com
  baseurl_source: declared
  description: Live parcel rate quotes from a US origin.
  name: SMKlog Quotes API
  slug: smklog-com-quotes-api
artifact_total: 35
collections:
- collection_type: postman
  name: SMKlog Quote API 1.4.0
  slug: postman-smklog-com-quote-api
common:
- group: other
  href: https://artifacts.apis.io/smklog-com/capabilities/smklog-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/smklog-com-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/smklog-com/plans/smklog-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smklog-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/smklog-com/rate-limits/smklog-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/smklog-com-rate-limits.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://smklog.com/feed.xml
- group: other
  href: https://artifacts.apis.io/smklog-com/overlays/smklog-com-quote-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/smklog-com-quote-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/smklog-com/security/smklog-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/smklog-com-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://smklog.com/
- group: docs
  title: ''
  type: Documentation
  url: https://smklog.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://quote-api.smklog.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://smklog.com/repack-line
- group: operate
  title: ''
  type: Support
  url: https://smklog.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://smklog.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smklog.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smklog.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smklog
- group: agent
  href: https://artifacts.apis.io/smklog-com/llms/smklog-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smklog-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://smklog.com/llms.txt
- group: other
  href: https://artifacts.apis.io/smklog-com/a2a/smklog-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/smklog-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/smklog-com/mcp/smklog-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/smklog-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/smklog-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/smklog-com/well-known/smklog-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smklog-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/smklog-com/well-known/smklog-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/smklog-com-security.txt
- group: auth
  title: ''
  type: Security
  url: https://smklog.com/.well-known/security.txt
- group: build
  href: https://artifacts.apis.io/smklog-com/packages/smklog-com-packages.yml
  title: ''
  type: Packages
  url: packages/smklog-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/smklog-com/authentication/smklog-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smklog-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/smklog-com/scopes/smklog-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/smklog-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/smklog-com/security/smklog-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smklog-com-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://smklog.com/privacy
- group: company
  title: ''
  type: About
  url: https://smklog.com/about
- group: other
  title: ''
  type: Leadership
  url: https://smklog.com/about
- group: company
  title: ''
  type: Newsroom
  url: https://smklog.com/news/
- group: company
  title: ''
  type: Blog
  url: https://smklog.com/lp/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://smklog.com/developers/
- group: build
  title: ''
  type: Examples
  url: https://smklog.com/developers/samples/
- group: other
  title: ''
  type: Playground
  url: https://smklog.com/developers/playground
- group: start
  title: ''
  type: Console
  url: https://smklog.com/developers/playground
- group: build
  title: ''
  type: Postman
  url: https://smklog.com/developers/postman/smklog-quote-api.postman_collection.json
- group: auth
  title: ''
  type: OAuthAuthorizationServer
  url: https://quote-api.smklog.com/.well-known/oauth-authorization-server
- group: auth
  title: ''
  type: OAuthProtectedResource
  url: https://quote-api.smklog.com/.well-known/oauth-protected-resource
- group: commercial
  title: ''
  type: Plans
  url: https://smklog.com/pricing
- group: commercial
  title: ''
  type: FinOps
  url: https://smklog.com/developers/finops.yaml
- group: operate
  title: ''
  type: RateLimits
  url: https://smklog.com/developers/rate-limits
- group: operate
  title: ''
  type: RateLimits
  url: https://smklog.com/developers/rate-limits.yaml
- group: operate
  title: ''
  type: StatusPage
  url: https://smklog.com/developers/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://smklog.com/news/
- group: design
  title: ''
  type: Versioning
  url: https://smklog.com/developers/#versioning
- group: design
  title: ''
  type: SpectralRules
  url: https://smklog.com/developers/spectral.yaml
- group: design
  title: ''
  type: Vocabulary
  url: https://smklog.com/developers/vocabulary.yaml
- group: other
  title: ''
  type: Overlay
  url: https://smklog.com/developers/overlay.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://smklog.com/developers/schemas/context.jsonld
- group: other
  title: ''
  type: SBOM
  url: https://smklog.com/developers/sbom.cdx.json
- group: auth
  title: ''
  type: TrustCenter
  url: https://smklog.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://smklog.com/trust/compliance
- group: operate
  title: ''
  type: Deprecation
  url: https://smklog.com/trust/commitments#deprecation
- group: operate
  title: ''
  type: SupportLifetime
  url: https://smklog.com/trust/commitments#support-lifetime
- group: operate
  title: ''
  type: IncidentNotification
  url: https://smklog.com/trust/commitments#incident-notification
- group: other
  title: ''
  type: ExitAssistance
  url: https://smklog.com/trust/commitments#exit-assistance
- group: other
  title: ''
  type: TransparencyReport
  url: https://smklog.com/trust/commitments#transparency-report
- group: operate
  title: ''
  type: RoadMap
  url: https://smklog.com/trust/commitments#roadmap
- group: other
  title: ''
  type: Subprocessors
  url: https://smklog.com/trust/subprocessors
- group: other
  title: ''
  type: DataResidency
  url: https://smklog.com/trust/data-residency
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://smklog.com/.well-known/security.txt
- group: operate
  title: ''
  type: Contact
  url: mailto:info@smklog.com
- group: other
  title: ''
  type: APICatalog
  url: https://smklog.com/.well-known/api-catalog
- group: other
  title: ''
  type: AICatalog
  url: https://smklog.com/.well-known/ai-catalog.json
- group: agent
  title: ''
  type: MCPServerCard
  url: https://smklog.com/.well-known/mcp/server-card.json
- group: agent
  title: ''
  type: AgentSkills
  url: https://smklog.com/.well-known/agent-skills/index.json
- group: other
  title: ''
  type: HTTPMessageSignatures
  url: https://smklog.com/.well-known/http-message-signatures-directory
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/smklog/parcel-shipping-rates-mcp
- group: design
  href: https://artifacts.apis.io/smklog-com/rules/smklog-com-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/smklog-com-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/smklog-com/vocabulary/smklog-com-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/smklog-com-vocabulary.yaml
- group: commercial
  href: https://artifacts.apis.io/smklog-com/finops/smklog-com-finops.yml
  title: ''
  type: FinOps
  url: finops/smklog-com-finops.yml
- group: design
  href: https://artifacts.apis.io/smklog-com/json-ld/smklog-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/smklog-com-context.jsonld
- group: build
  href: https://artifacts.apis.io/smklog-com/postman/smklog-com-quote-api.postman_collection.json
  title: ''
  type: Postman
  url: postman/smklog-com-quote-api.postman_collection.json
- group: other
  href: https://artifacts.apis.io/smklog-com/overlays/smklog-com-agent-crosswalk-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/smklog-com-agent-crosswalk-overlay.yaml
- group: build
  href: https://artifacts.apis.io/smklog-com/examples/smklog-com-get-parcel-quote-request-example.json
  title: ''
  type: Examples
  url: examples/smklog-com-get-parcel-quote-request-example.json
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/smklog/smklog-sdk
- group: build
  title: ''
  type: SDK
  url: https://www.npmjs.com/package/smklog
- group: build
  title: ''
  type: SDK
  url: https://pypi.org/project/smklog-sdk/
- group: build
  title: ''
  type: SDK
  url: https://github.com/smklog/smklog-sdk/tree/main/go
- group: build
  title: ''
  type: CLI
  url: https://pypi.org/project/smklog-sdk/#command-line
created: '2026-09-19'
description: 'SMKlog (SMKLOG-2022 LLC, Berkeley Heights, New Jersey) is an independent US parcel shipping calculator and label seller: describe an item in plain words, get live USPS, UPS, FedEx and DHL Express rates from a US origin to the US, Canada, the UK, Germany or Australia, and buy the label online. The same pricing engine is published for machines as the SMKlog Quote API on quote-api.smklog.com: an OpenAPI 3.1 contract with no key required, a remote MCP server with five tools (plus an open-source stdio bridge), an A2A agent card, an RFC 9727 api-catalog, RFC 8414/9728 OAuth metadata for an optional client_credentials rate-limit tier, two provider-published Agent Skills and an llms.txt. Agents price and prepare checkout; a human always completes payment on smklog.com.'
examples:
- key_count: 4
  name: Smklog Com Cancel Payment Session Responses Example
  slug: smklog-com-cancel-payment-session-responses-example
- key_count: 4
  name: Smklog Com Create Payment Session Request Example
  slug: smklog-com-create-payment-session-request-example
- key_count: 4
  name: Smklog Com Create Payment Session Responses Example
  slug: smklog-com-create-payment-session-responses-example
- key_count: 4
  name: Smklog Com Get Checkout Status Responses Example
  slug: smklog-com-get-checkout-status-responses-example
- key_count: 4
  name: Smklog Com Get Parcel Quote Request Example
  slug: smklog-com-get-parcel-quote-request-example
- key_count: 4
  name: Smklog Com Get Parcel Quote Responses Example
  slug: smklog-com-get-parcel-quote-responses-example
- key_count: 4
  name: Smklog Com Status Responses Example
  slug: smklog-com-status-responses-example
finops:
- has_sources: true
  method: authored
  name: Smklog Com Finops
  primary_unit: ''
  service_category: Parcel shipping labels
  slug: smklog-com-finops
  template: false
image: https://smklog.com/assets/icon-512.png
json_schemas:
- name: CheckoutSessionRequest
  property_count: 7
  slug: smklog-com-checkout-session-request
- name: CheckoutSession
  property_count: 10
  slug: smklog-com-checkout-session
- name: CheckoutStatus
  property_count: 10
  slug: smklog-com-checkout-status
- name: Liveness
  property_count: 5
  slug: smklog-com-liveness
- name: Package
  property_count: 8
  slug: smklog-com-package
- name: Problem
  property_count: 3
  slug: smklog-com-problem
- name: QuoteRequest
  property_count: 11
  slug: smklog-com-quote-request
- name: QuoteResponse
  property_count: 10
  slug: smklog-com-quote-response
- name: Rate
  property_count: 9
  slug: smklog-com-rate
- name: WebhookEvent
  property_count: 5
  slug: smklog-com-webhook-event
jsonld:
- class_count: 9
  name: Smklog Com Context
  property_count: 65
  slug: smklog-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at quote-api.smklog.com over HTTP; 5 tools listed.
  name: SMKlog MCP Server
  slug: smklog-quotes
modified: '2026-10-12'
name: SMKlog
nav: Providers
network: true
overview: 'SMKlog publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Checkout API, Operations API, and Quotes API. Tagged areas include Company, Shipping, Logistics, Parcel Shipping, and shipping-rates.


  The SMKlog catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SMKlog''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, engineering blog, and 74 more developer resources.'
plans:
- name: Smklog Com Plans Pricing
  plan_count: 5
  slug: smklog-com-plans-pricing
- name: Smklog Com Price Estimates
  plan_count: 0
  slug: smklog-com-price-estimates
random_paper: 9
rate_limits:
- limit_count: 3
  name: Smklog Com Rate Limits
  slug: smklog-com-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: SMKlog API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 5
    warn: 7
  slug: smklog-com-spectral-rules
scopes:
- name: Smklog Com Scopes
  scope_count: 1
  slug: smklog-com-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 79.5
  coverage:
    artifact_dirs: 35
    catalog_earned: 105.5
    catalog_earned_first_party: 44.5
    catalog_gap: 9.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -16.0
  facets:
    access_clarity: 55.3
    contract_governance: 92.4
    contract_quality: 77.1
    developer_ergonomics: 67.9
    discoverability: 93.3
    operational_transparency: 61.8
  previous_composite: 95.5
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 67.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/smklog-com/smklog-com-2026-10-11T130009.png
security:
- kind: authentication
  name: Smklog Com Authentication
  slug: smklog-com-authentication
  summary_line: none/oauth2 · 2 schemes
- kind: domain-security
  name: Smklog Com Domain Security
  slug: smklog-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Smklog Com Vulnerability Disclosure
  slug: smklog-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: create-checkout-link
  slug: smklog-com-create-checkout-link
- name: get-parcel-quote
  slug: smklog-com-get-parcel-quote
slug: smklog-com
tags:
- Company
- Shipping
- Logistics
- Parcel Shipping
- shipping-rates
- Shipping Labels
- E-Commerce
- Agents
- MCP
- A2A
website: https://smklog.com/
---
