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
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Ziina Agentic Access
  operation_count: 8
  slug: ziina-agentic-access
  summary_line: 8 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api-v2.ziina.com/api
  baseurl_source: declared
  description: Retrieve the authenticated account profile.
  name: Ziina Account API
  slug: ziina-account-api
- baseURL: https://api-v2.ziina.com/api
  baseurl_source: declared
  description: The Log API from Ziina — 1 operation(s) for log.
  name: Ziina Log API
  slug: ziina-log-api
- baseURL: https://api-v2.ziina.com/api
  baseurl_source: declared
  description: Create and retrieve payment intents (hosted/embedded checkout).
  name: Ziina PaymentIntent API
  slug: ziina-paymentintent-api
- baseURL: https://api-v2.ziina.com/api
  baseurl_source: declared
  description: Issue and retrieve refunds against a payment intent.
  name: Ziina Refund API
  slug: ziina-refund-api
- baseURL: https://api-v2.ziina.com/api
  baseurl_source: declared
  description: Initiate and retrieve peer transfers between Ziina accounts.
  name: Ziina Transfer API
  slug: ziina-transfer-api
- baseURL: https://api-v2.ziina.com/api
  baseurl_source: declared
  description: Register or delete a webhook endpoint for payment events.
  name: Ziina Webhook API
  slug: ziina-webhook-api
- baseURL: https://api-v2.ziina.com/api
  baseurl_source: declared
  description: Service status.
  name: Ziina Health Check API
  slug: ziina-health-check-api
arazzos:
- description: Create a payment intent, then poll it until the payment reaches a terminal status. Seed inputs with test=true to run in Ziina test mode.
  name: Ziina - accept a payment and confirm
  slug: ziina-accept-payment.arazzo
- description: Issue a refund against an existing payment intent, then poll the refund until it reaches a terminal status.
  name: Ziina - refund a payment and confirm
  slug: ziina-refund-payment.arazzo
artifact_total: 38
asyncapis:
- description: Event surface for Ziina payment webhooks. When a webhook URL is registered (POST /webhook), Ziina delivers events as HTTP POST callbacks over HTTPS to that URL. Non-2xx responses are retried up to 3 t
  name: Ziina Webhooks
  slug: ziina-webhooks-asyncapi
collections:
- collection_type: postman
  name: Ziina Account API
  slug: postman-ziina-account-api
- collection_type: postman
  name: Ziina Account HealthCheck API
  slug: postman-ziina-healthcheck-api
- collection_type: postman
  name: Ziina Account Log API
  slug: postman-ziina-log-api
- collection_type: postman
  name: Ziina Account PaymentIntent API
  slug: postman-ziina-paymentintent-api
- collection_type: postman
  name: Ziina Account Refund API
  slug: postman-ziina-refund-api
- collection_type: postman
  name: Ziina Account Transfer API
  slug: postman-ziina-transfer-api
- collection_type: postman
  name: Ziina Account Webhook API
  slug: postman-ziina-webhook-api
- collection_type: open
  name: Ziina Account API
  slug: open-ziina-account-api
- collection_type: open
  name: Ziina Account HealthCheck API
  slug: open-ziina-healthcheck-api
- collection_type: open
  name: Ziina Account Log API
  slug: open-ziina-log-api
- collection_type: open
  name: Ziina Account PaymentIntent API
  slug: open-ziina-paymentintent-api
- collection_type: open
  name: Ziina Account Refund API
  slug: open-ziina-refund-api
- collection_type: open
  name: Ziina Account Transfer API
  slug: open-ziina-transfer-api
- collection_type: open
  name: Ziina Account Webhook API
  slug: open-ziina-webhook-api
common:
- group: other
  href: https://artifacts.apis.io/ziina/capabilities/ziina-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ziina-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ziina/overview
- group: agent
  href: https://artifacts.apis.io/ziina/agentic-access/ziina-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ziina-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ziina/security/ziina-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ziina-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ziina/security/ziina-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ziina-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ziina/security/ziina-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ziina-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ziina/authentication/ziina-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ziina-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ziina-co
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ziina
- group: company
  title: ''
  type: Website
  url: https://ziina.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ziina.com
- group: commercial
  href: https://artifacts.apis.io/ziina/plans/ziina-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ziina-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ziina/rate-limits/ziina-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ziina-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ziina/finops/ziina-finops.yml
  title: ''
  type: FinOps
  url: finops/ziina-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ziina.com/blog
- group: auth
  href: https://artifacts.apis.io/ziina/scopes/ziina-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ziina-scopes.yml
- group: design
  href: https://artifacts.apis.io/ziina/conventions/ziina-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ziina-conventions.yml
- group: design
  href: https://artifacts.apis.io/ziina/conventions/ziina-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ziina-conventions.yml
- group: design
  href: https://artifacts.apis.io/ziina/errors/ziina-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ziina-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ziina/conformance/ziina-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ziina-conformance.yml
- group: auth
  href: https://artifacts.apis.io/ziina/security/ziina-trust-center.yml
  title: ''
  type: Compliance
  url: security/ziina-trust-center.yml
- group: design
  href: https://artifacts.apis.io/ziina/lifecycle/ziina-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ziina-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/ziina/sandbox/ziina-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ziina-sandbox.yml
- group: design
  href: https://artifacts.apis.io/ziina/data-model/ziina-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ziina-data-model.yml
- group: design
  href: https://artifacts.apis.io/ziina/components/ziina-components.yml
  title: ''
  type: Components
  url: components/ziina-components.yml
- group: agent
  href: https://artifacts.apis.io/ziina/well-known/ziina-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ziina-well-known.yml
- group: agent
  href: https://artifacts.apis.io/ziina/llms/ziina-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ziina-llms.txt
- group: agent
  href: https://artifacts.apis.io/ziina/mcp/ziina-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ziina-mcp.yml
- group: other
  href: https://artifacts.apis.io/ziina/overlays/ziina-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ziina-openapi-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/ziina/asyncapi/ziina-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/ziina-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/ziina/asyncapi/ziina-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/ziina-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/ziina/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ziina/arazzo/ziina-accept-payment.arazzo.yml
  title: ''
  type: Arazzo
  url: arazzo/ziina-accept-payment.arazzo.yml
- group: design
  href: https://artifacts.apis.io/ziina/arazzo/ziina-refund-payment.arazzo.yml
  title: ''
  type: Arazzo
  url: arazzo/ziina-refund-payment.arazzo.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ziina.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ziina.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ziina.com/api-reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://ziina.com/help-center
- group: commercial
  title: ''
  type: Pricing
  url: https://ziina.com/fees
- group: start
  title: ''
  type: SignUp
  url: https://ziina.com/business/connect
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ziina.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ziina.com/privacy
created: '2026-07-17'
description: Ziina is a Dubai-based (UAE) fintech offering an instant money and payments platform for consumers and businesses. Its REST API lets developers create hosted and embedded payment intents, issue refunds, run peer transfers between Ziina accounts, and register webhooks. Amounts are in the currency's minor unit (fils for AED), auth is HTTP bearer (JWT) via OAuth 2.0 scopes, and settlement is in AED with multi-currency acceptance.
finops:
- has_sources: true
  method: generated
  name: Ziina Finops
  primary_unit: ''
  service_category: Payments and Financial Services
  slug: ziina-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ziina.png
layout: provider
modified: '2026-07-17'
name: Ziina
nav: Providers
network: true
overview: 'Ziina publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Log API, PaymentIntent API, and 4 more. Tagged areas include Payments, Fintech, United Arab Emirates, MENA, and Money Transfer.


  The Ziina catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Ziina''s developer surface includes authentication, documentation, engineering blog, sandbox, getting-started guide, API reference, support, and 35 more developer resources.'
plans:
- name: Ziina Plans Pricing
  plan_count: 3
  slug: ziina-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Ziina Rate Limits
  slug: ziina-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Ziina API Rules
  rule_count: 59
  severity_counts:
    error: 54
    hint: 0
    info: 3
    warn: 2
  slug: ziina-rules
scopes:
- name: Ziina Scopes
  scope_count: 7
  slug: ziina-scopes
  summary_line: 7 scopes
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 34
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 52.3
    developer_ergonomics: 67.3
    discoverability: 73.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-arab-emirates
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ziina/ziina-2026-08-17T083107.png
security:
- kind: authentication
  name: Ziina Authentication
  slug: ziina-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ziina Domain Security
  slug: ziina-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ziina Vulnerability Disclosure
  slug: ziina-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ziina Trust Center
  slug: ziina-trust-center
  summary_line: PCI DSS
skill_count: 4
skills:
- name: Accept a payment with Ziina
  slug: ziina-accept-a-payment
- name: Issue a refund with Ziina
  slug: ziina-issue-a-refund
- name: Register a Ziina webhook
  slug: ziina-register-webhook
- name: Transfer money between Ziina accounts
  slug: ziina-transfer-money
slug: ziina
tags:
- Payments
- Fintech
- United Arab Emirates
- MENA
- Money Transfer
- Wallets
website: https://ziina.com/
---
