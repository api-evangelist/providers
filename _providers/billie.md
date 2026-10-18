---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Billie Agentic Access
  operation_count: 18
  slug: billie-agentic-access
  summary_line: 18 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://paella.billie.io/api/v2
  baseurl_source: declared
  description: This API uses OAuth 2.0 for secure authentication. Different keys are used for the `sandbox` and `production` environments. Both systems operate completely independent, however both show largely the s
  name: Billie Authentication API
  slug: billie-authentication-api
- baseURL: https://paella.billie.io/api/v2
  baseurl_source: declared
  description: The Back-end Order Creation API from Billie — 2 operation(s) for back-end order creation.
  name: Billie Back-end Order Creation API
  slug: billie-back-end-order-creation-api
- baseURL: https://paella.billie.io/api/v2
  baseurl_source: declared
  description: The Captures API from Billie — 5 operation(s) for captures.
  name: Billie Captures API
  slug: billie-captures-api
- baseURL: https://paella.billie.io/api/v2
  baseurl_source: declared
  description: '## To integrate the Billie checkout widget, the following steps are required: 1. Add the Billie checkout widget bundle to your checkout page 2. Provide config data _(with the `session_id` from the ser'
  name: Billie Front-end Order Creation API
  slug: billie-front-end-order-creation-api
- baseURL: https://paella.billie.io/api/v2
  baseurl_source: declared
  description: The Order Management API from Billie — 2 operation(s) for order management.
  name: Billie Order Management API
  slug: billie-order-management-api
artifact_total: 19
asyncapis:
- description: ''
  name: Billie Webhooks
  slug: billie-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/agentic-access/billie-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/billie-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/rules/billie-rules.yml
  title: ''
  type: Spectral
  url: rules/billie-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/json-ld/billie-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/billie-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/vocabulary/billie-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/billie-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/hosts/billie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billie-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/vendors/billie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billie-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/scopes/billie-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/billie-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/security/billie-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/billie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://billie.io/coordinated-vulnerability-disclosure-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/security/billie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billie.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.billie.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billie.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.billie.io/reference/integration-checklist
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.billie.io/docs/get-started-with-billies-api-integration
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/authentication/billie-authentication.yml
  title: ''
  type: Authentication
  url: authentication/billie-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/packages/billie-packages.yml
  title: ''
  type: SDKs
  url: packages/billie-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/packages/billie-packages.yml
  title: ''
  type: Packages
  url: packages/billie-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/sandbox/billie-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/billie-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/asyncapi/billie-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/billie-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/mcp/billie-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/billie-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/llms/billie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billie-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/well-known/billie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/billie-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/well-known/billie-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/billie-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/conventions/billie-conventions.yml
  title: ''
  type: Conventions
  url: conventions/billie-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/errors/billie-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/billie-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/errors/billie-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/billie-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/lifecycle/billie-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/billie-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.billie.io/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/conformance/billie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/billie-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/data-model/billie-data-model.yml
  title: ''
  type: DataModel
  url: data-model/billie-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/components/billie-components.yml
  title: ''
  type: Components
  url: components/billie-components.yml
- group: operate
  title: ''
  type: Support
  url: https://help.billie.io/merchant/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.billie.io/merchant/s/
- group: company
  title: ''
  type: Blog
  url: https://www.billie.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ozean12
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.billie.io/public/registration
- group: start
  title: ''
  type: Login
  url: https://dashboard.billie.io/public/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.billie.io/datenschutz
- group: other
  title: ''
  type: Imprint
  url: https://www.billie.io/impressum
created: '2026-07-17'
description: Billie is a Berlin-based B2B "buy now, pay later" (BNPL) payment provider that lets merchants offer business buyers invoice purchase, pay-after-delivery, and installment terms at checkout while Billie assumes the credit and fraud risk and pays the merchant out. Its Payment API v2 (paella.billie.io) uses OAuth 2.0 client-credentials and covers checkout sessions, a hosted payment page, direct backend order creation, order management, captures (invoicing), payment confirmation, refunds/credit notes, and a webhook event surface. Billie also ships an embeddable checkout widget, a PHP SDK, e-commerce plugins (Shopware, Magento, WooCommerce, JTL), and partner routes via Klarna, Mollie, Adyen, Stripe, and Kustom. Backed by Creandum and Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/billie.png
json_schemas:
- name: Order Creation Request
  property_count: 9
  slug: billie-create-order-request
- name: Get Invoice Response
  property_count: 13
  slug: billie-get-invoice-response
- name: Hpp Checkout Session Create Request
  property_count: 11
  slug: billie-hpp-checkout-session-ecommerce
- name: Hpp Checkout Session Create Request
  property_count: 11
  slug: billie-hpp-checkout-session-instore
- name: Hpp Checkout Session Create Request
  property_count: 11
  slug: billie-hpp-checkout-session-telesales
- name: Order Entity
  property_count: 13
  slug: billie-order
jsonld:
- class_count: 34
  name: Billie Context
  property_count: 106
  slug: billie-context
layout: provider
modified: '2026-07-18'
name: Billie
nav: Providers
network: true
overview: 'Billie publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Back-end Order Creation API, Captures API, and 2 more. Tagged areas include Company, Fintech, Payments, Buy Now Pay Later, and B2B.


  The Billie catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Billie''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 34 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Billie API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 1
  slug: billie-rules
scopes:
- name: Billie Scopes
  scope_count: 1
  slug: billie-scopes
  summary_line: 1 scope · password
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.8
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 67.9
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/screenshots/billie-2026-07-25T202942.png
security:
- kind: authentication
  name: Billie Authentication
  slug: billie-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Billie Domain Security
  slug: billie-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Billie Vulnerability Disclosure
  slug: billie-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: billie
tags:
- Company
- Fintech
- Payments
- Buy Now Pay Later
- B2B
- Invoicing
- Checkout
- Germany
website: https://www.billie.io/
---
