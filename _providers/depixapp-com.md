---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 2
  name: Depixapp Com Agentic Access
  operation_count: 48
  slug: depixapp-com-agentic-access
  summary_line: 48 operations · 25 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The @depixapp/mcp MCP server. Per depixapp.com/llms.txt, Level 1 is hosted at https://mcp.depixapp.com/mcp (MCP Streamable HTTP, OAuth 2.1, receive-only tools) and Level 2 runs locally via npx -y @dep
  name: DePix MCP Server
  slug: depix-mcp
- baseURL: https://api.depixapp.com
  baseurl_source: declared
  description: Account self-service — the verification state that gates the merchant tools.
  name: DePix App Account API
  slug: depixapp-com-account-api
- baseURL: https://api.depixapp.com
  baseurl_source: declared
  description: Agent self-onboarding (keypair-signed). Registration requires an operator token (anti-farm anchor).
  name: DePix App Agents API
  slug: depixapp-com-agents-api
- baseURL: https://api.depixapp.com
  baseurl_source: declared
  description: Charging via checkouts (scopes `merchant_write`/`merchant_read`).
  name: DePix App Checkouts API
  slug: depixapp-com-checkouts-api
- baseURL: https://api.depixapp.com
  baseurl_source: declared
  description: Merchant profile self-service — edit the light fields (scope `merchant_write`); read via GET /api/me (`merchant_read`).
  name: DePix App Merchant API
  slug: depixapp-com-merchant-api
- baseURL: https://api.depixapp.com
  baseurl_source: declared
  description: Service metadata.
  name: DePix App Meta API
  slug: depixapp-com-meta-api
- baseURL: https://api.depixapp.com
  baseurl_source: declared
  description: Deposits and withdrawals by API key (scopes `wallet_write` for money movement, `wallet_read` for status).
  name: DePix App Pay API
  slug: depixapp-com-pay-api
- baseURL: https://api.depixapp.com
  baseurl_source: declared
  description: Reusable products (scopes `merchant_write`/`merchant_read`).
  name: DePix App Products API
  slug: depixapp-com-products-api
- baseURL: https://api.depixapp.com
  baseurl_source: declared
  description: Unauthenticated payer-side endpoints.
  name: DePix App Public API
  slug: depixapp-com-public-api
- baseURL: https://api.depixapp.com
  baseurl_source: declared
  description: The support API from DePix App — 6 operation(s) for support.
  name: DePix App Support API
  slug: depixapp-com-support-api
artifact_total: 31
asyncapis:
- description: ''
  name: Depixapp Com Webhooks
  slug: depixapp-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/depixapp-com/agentic-access/depixapp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/depixapp-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/depixapp-com/rate-limits/depixapp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/depixapp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/depixapp-com/plans/depixapp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/depixapp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/rules/depixapp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/depixapp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/json-ld/depixapp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/depixapp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/depixapp-com/vocabulary/depixapp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/depixapp-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/depixapp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/asyncapi/depixapp-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/depixapp-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/data-model/depixapp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/depixapp-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/components/depixapp-com-components.yml
  title: ''
  type: Components
  url: components/depixapp-com-components.yml
- group: build
  href: https://artifacts.apis.io/depixapp-com/cli/depixapp-com-cli.yml
  title: ''
  type: CLI
  url: cli/depixapp-com-cli.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/conventions/depixapp-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/depixapp-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/conventions/depixapp-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/depixapp-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/depixapp-com/sandbox/depixapp-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/depixapp-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/depixapp-com/security/depixapp-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/depixapp-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/depixapp-com/scopes/depixapp-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/depixapp-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/lifecycle/depixapp-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/depixapp-com-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/depixapp-com/errors/depixapp-com-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/depixapp-com-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/errors/depixapp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/depixapp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/depixapp-com/conformance/depixapp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/depixapp-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/depixapp-com/overlays/depixapp-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/depixapp-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/depixapp-com/llms/depixapp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/depixapp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/depixapp-com/a2a/depixapp-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/depixapp-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/depixapp-com/mcp/depixapp-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/depixapp-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/depixapp-com/mcp/depixapp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/depixapp-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/depixapp-com/well-known/depixapp-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/depixapp-com-security.txt
- group: auth
  href: https://artifacts.apis.io/depixapp-com/well-known/depixapp-com-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/depixapp-com-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/depixapp-com/well-known/depixapp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/depixapp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/depixapp-com/hosts/depixapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/depixapp-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/depixapp-com/integrations/depixapp-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/depixapp-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/depixapp-com/vendors/depixapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/depixapp-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/depixapp-com/packages/depixapp-com-packages.yml
  title: ''
  type: SDKs
  url: packages/depixapp-com-packages.yml
- group: build
  href: https://artifacts.apis.io/depixapp-com/packages/depixapp-com-packages.yml
  title: ''
  type: Packages
  url: packages/depixapp-com-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.depixapp.com</span
- group: auth
  href: https://artifacts.apis.io/depixapp-com/authentication/depixapp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/depixapp-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/depixapp-com/security/depixapp-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/depixapp-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/depixapp-com/security/depixapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/depixapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://depixapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://depixapp.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://depixapp.com/blog/
- group: start
  title: ''
  type: Login
  url: https://depixapp.com/app/login
- group: start
  title: ''
  type: SignUp
  url: https://depixapp.com/app/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://depixapp.com/termos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://depixapp.com/privacidade/
- group: company
  title: ''
  type: About
  url: https://depixapp.com/blog/about/
created: '2026-11-05'
description: DePix App is a Brazilian non-custodial Pix payment gateway built on the Liquid Network. Merchants and individuals accept ordinary Pix payments and receive DePix, a BRL-pegged stablecoin (1 DePix = 1 real), into their own wallet. A REST API with API-key auth (sandbox sk_test_ keys) covers checkouts, products, dated charges, BRL on-ramp to DePix and off-ramp to Pix, alongside a BTCPay Server plugin and an MCP server (@depixapp/mcp) for AI agents. The site is Portuguese-first (pt_BR) with an English version.
image: https://depixapp.com/social-preview.png
json_schemas:
- name: AgentRegisterResponse
  property_count: 1
  slug: depixapp-com-agent-register-response
- name: CheckoutCreateRequest
  property_count: 10
  slug: depixapp-com-checkout-create-request
- name: CheckoutListResponse
  property_count: 4
  slug: depixapp-com-checkout-list-response
- name: MerchantCheckoutRequest
  property_count: 6
  slug: depixapp-com-merchant-checkout-request
- name: VaultStatusResponse
  property_count: 9
  slug: depixapp-com-vault-status-response
- name: VerificationStatusResponse
  property_count: 13
  slug: depixapp-com-verification-status-response
jsonld:
- class_count: 68
  name: Depixapp Com Context
  property_count: 168
  slug: depixapp-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.depixapp.com requiring OAuth.
  name: DePix App MCP Server (@depixapp/mcp)
  slug: depix-app-mcp-server-depixapp-mcp
modified: '2026-11-05'
name: DePix App
nav: Providers
network: true
overview: 'DePix App publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Checkouts API, and 7 more. Tagged areas include Company, Payments, Pix, Stablecoins, and Cryptocurrency.


  The DePix App catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DePix App''s developer surface includes CLI, sandbox, authentication, documentation, engineering blog, signup flow, and 39 more developer resources.'
plans:
- name: Depixapp Com Plans Pricing
  plan_count: 3
  slug: depixapp-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 37
  name: Depixapp Com Rate Limits
  slug: depixapp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: DePix App API Rules
  rule_count: 66
  severity_counts:
    error: 54
    hint: 0
    info: 3
    warn: 9
  slug: depixapp-com-rules
scopes:
- name: Depixapp Com Scopes
  scope_count: 4
  slug: depixapp-com-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 63.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 76.2
    developer_ergonomics: 56.5
    discoverability: 65.0
    operational_transparency: 50.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 36.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Depixapp Com Authentication
  slug: depixapp-com-authentication
  summary_line: http/signed-request · 3 schemes
- kind: domain-security
  name: Depixapp Com Domain Security
  slug: depixapp-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Depixapp Com Vulnerability Disclosure
  slug: depixapp-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: accept-pix-checkout
  slug: depixapp-com-accept-pix-checkout
- name: manage-products-and-charges
  slug: depixapp-com-manage-products-and-charges
- name: onramp-offramp
  slug: depixapp-com-onramp-offramp
- name: support-ticket
  slug: depixapp-com-support-ticket
slug: depixapp-com
tags:
- Company
- Payments
- Pix
- Stablecoins
- Cryptocurrency
- Bitcoin
- Liquid Network
- Brazil
- MCP
website: https://depixapp.com/
---
