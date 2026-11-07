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
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 88
  human_in_the_loop: 2
  name: Portone Agentic Access
  operation_count: 147
  slug: portone-agentic-access
  summary_line: 147 operations · 88 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Legacy V1 (Iamport) REST API on api.iamport.kr — token-authenticated (POST /users/getToken with imp_key/imp_secret) payment lookup, cancellation, non-authenticated and scheduled payments, virtual acco
  name: PortOne REST API (V1, legacy Iamport)
  slug: portone-rest-api-v1
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Banks API from PortOne — 1 operation(s) for banks.
  name: PortOne Banks API
  slug: portone-banks-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Billing Keys API from PortOne — 4 operation(s) for billing keys.
  name: PortOne Billing Keys API
  slug: portone-billing-keys-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Cash Receipts API from PortOne — 1 operation(s) for cash receipts.
  name: PortOne Cash Receipts API
  slug: portone-cash-receipts-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Checkout Profiles API from PortOne — 1 operation(s) for checkout profiles.
  name: PortOne Checkout Profiles API
  slug: portone-checkout-profiles-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Identity Verifications API from PortOne — 5 operation(s) for identity verifications.
  name: PortOne Identity Verifications API
  slug: portone-identity-verifications-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Kakaopay API from PortOne — 1 operation(s) for kakaopay.
  name: PortOne Kakaopay API
  slug: portone-kakaopay-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Login API from PortOne — 1 operation(s) for login.
  name: PortOne Login API
  slug: portone-login-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Payment Events By Cursor API from PortOne — 1 operation(s) for payment events by cursor.
  name: PortOne Payment Events By Cursor API
  slug: portone-payment-events-by-cursor-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Payment Gateways API from PortOne — 1 operation(s) for payment gateways.
  name: PortOne Payment Gateways API
  slug: portone-payment-gateways-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Payment Reconciliations API from PortOne — 2 operation(s) for payment reconciliations.
  name: PortOne Payment Reconciliations API
  slug: portone-payment-reconciliations-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Payment Schedules API from PortOne — 2 operation(s) for payment schedules.
  name: PortOne Payment Schedules API
  slug: portone-payment-schedules-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Payment Sessions API from PortOne — 3 operation(s) for payment sessions.
  name: PortOne Payment Sessions API
  slug: portone-payment-sessions-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Payments API from PortOne — 18 operation(s) for payments.
  name: PortOne Payments API
  slug: portone-payments-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Payments By Cursor API from PortOne — 1 operation(s) for payments by cursor.
  name: PortOne Payments By Cursor API
  slug: portone-payments-by-cursor-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Paymentwall API from PortOne — 1 operation(s) for paymentwall.
  name: PortOne Paymentwall API
  slug: portone-paymentwall-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Platform API from PortOne — 44 operation(s) for platform.
  name: PortOne Platform API
  slug: portone-platform-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Promotions API from PortOne — 1 operation(s) for promotions.
  name: PortOne Promotions API
  slug: portone-promotions-api
- baseURL: https://api.portone.io
  baseurl_source: declared
  description: The Token API from PortOne — 1 operation(s) for token.
  name: PortOne Token API
  slug: portone-token-api
- baseURL: https://api.iamport.kr
  baseurl_source: declared
  description: The B2B API from PortOne — 26 operation(s) for b2b.
  name: PortOne B2B API
  slug: portone-b2-b-api
artifact_total: 72
asyncapis:
- description: ''
  name: Portone Webhooks
  slug: portone-webhooks
collections:
- collection_type: postman
  name: PortOne B2b API
  slug: postman-portone-b2b-api
- collection_type: postman
  name: PortOne B2b Banks API
  slug: postman-portone-banks-api
- collection_type: postman
  name: PortOne B2b Billing Keys API
  slug: postman-portone-billing-keys-api
- collection_type: postman
  name: PortOne B2b Cash Receipts API
  slug: postman-portone-cash-receipts-api
- collection_type: postman
  name: PortOne B2b Checkout Profiles API
  slug: postman-portone-checkout-profiles-api
- collection_type: postman
  name: PortOne B2b Identity Verifications API
  slug: postman-portone-identity-verifications-api
- collection_type: postman
  name: PortOne B2b Kakaopay API
  slug: postman-portone-kakaopay-api
- collection_type: postman
  name: PortOne B2b Login API
  slug: postman-portone-login-api
- collection_type: postman
  name: PortOne B2b Payment Events By Cursor API
  slug: postman-portone-payment-events-by-cursor-api
- collection_type: postman
  name: PortOne B2b Payment Gateways API
  slug: postman-portone-payment-gateways-api
- collection_type: postman
  name: PortOne B2b Payment Reconciliations API
  slug: postman-portone-payment-reconciliations-api
- collection_type: postman
  name: PortOne B2b Payment Schedules API
  slug: postman-portone-payment-schedules-api
- collection_type: postman
  name: PortOne B2b Payment Sessions API
  slug: postman-portone-payment-sessions-api
- collection_type: postman
  name: PortOne B2b Payments API
  slug: postman-portone-payments-api
- collection_type: postman
  name: PortOne B2b Payments By Cursor API
  slug: postman-portone-payments-by-cursor-api
- collection_type: postman
  name: PortOne B2b Paymentwall API
  slug: postman-portone-paymentwall-api
- collection_type: postman
  name: PortOne B2b Platform API
  slug: postman-portone-platform-api
- collection_type: postman
  name: PortOne B2b Promotions API
  slug: postman-portone-promotions-api
- collection_type: postman
  name: PortOne B2b Token API
  slug: postman-portone-token-api
- collection_type: open
  name: PortOne B2b API
  slug: open-portone-b2b-api
- collection_type: open
  name: PortOne B2b Banks API
  slug: open-portone-banks-api
- collection_type: open
  name: PortOne B2b Billing Keys API
  slug: open-portone-billing-keys-api
- collection_type: open
  name: PortOne B2b Cash Receipts API
  slug: open-portone-cash-receipts-api
- collection_type: open
  name: PortOne B2b Checkout Profiles API
  slug: open-portone-checkout-profiles-api
- collection_type: open
  name: PortOne B2b Identity Verifications API
  slug: open-portone-identity-verifications-api
- collection_type: open
  name: PortOne B2b Kakaopay API
  slug: open-portone-kakaopay-api
- collection_type: open
  name: PortOne B2b Login API
  slug: open-portone-login-api
- collection_type: open
  name: PortOne B2b Payment Events By Cursor API
  slug: open-portone-payment-events-by-cursor-api
- collection_type: open
  name: PortOne B2b Payment Gateways API
  slug: open-portone-payment-gateways-api
- collection_type: open
  name: PortOne B2b Payment Reconciliations API
  slug: open-portone-payment-reconciliations-api
- collection_type: open
  name: PortOne B2b Payment Schedules API
  slug: open-portone-payment-schedules-api
- collection_type: open
  name: PortOne B2b Payment Sessions API
  slug: open-portone-payment-sessions-api
- collection_type: open
  name: PortOne B2b Payments API
  slug: open-portone-payments-api
- collection_type: open
  name: PortOne B2b Payments By Cursor API
  slug: open-portone-payments-by-cursor-api
- collection_type: open
  name: PortOne B2b Paymentwall API
  slug: open-portone-paymentwall-api
- collection_type: open
  name: PortOne B2b Platform API
  slug: open-portone-platform-api
- collection_type: open
  name: PortOne B2b Promotions API
  slug: open-portone-promotions-api
- collection_type: open
  name: PortOne B2b Token API
  slug: open-portone-token-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.portone.io/rss.xml
- group: other
  href: https://artifacts.apis.io/portone/capabilities/portone-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/portone-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/portone/overview
- group: agent
  href: https://artifacts.apis.io/portone/agentic-access/portone-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/portone-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/portone/security/portone-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/portone-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/portone/security/portone-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/portone-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/portone/security/portone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/portone-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/portone/authentication/portone-authentication.yml
  title: ''
  type: Authentication
  url: authentication/portone-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/portone-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/portoneglobal
- group: company
  title: ''
  type: Website
  url: https://portone.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.portone.io/
- group: commercial
  href: https://artifacts.apis.io/portone/plans/portone-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/portone-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/portone/rate-limits/portone-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/portone-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/portone/finops/portone-finops.yml
  title: ''
  type: FinOps
  url: finops/portone-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://developers.portone.io/opi/ko/support/release-note
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.portone.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.portone.io/opi/ko/quick-guide/payment
- group: operate
  title: ''
  type: Support
  url: https://developers.portone.io/opi/ko/support/contact
- group: start
  title: ''
  type: SignUp
  url: https://admin.portone.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terms.portone.io/
- group: build
  href: https://artifacts.apis.io/portone/packages/portone-packages.yml
  title: ''
  type: Packages
  url: packages/portone-packages.yml
- group: build
  href: https://artifacts.apis.io/portone/packages/portone-packages.yml
  title: ''
  type: SDKs
  url: packages/portone-packages.yml
- group: build
  href: https://artifacts.apis.io/portone/cli/portone-cli.yml
  title: ''
  type: CLI
  url: cli/portone-cli.yml
- group: agent
  href: https://artifacts.apis.io/portone/mcp/portone-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/portone-mcp.yml
- group: agent
  href: https://artifacts.apis.io/portone/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/portone/llms/portone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/portone-llms.txt
- group: other
  href: https://artifacts.apis.io/portone/overlays/portone-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/portone-overlay.yaml
- group: design
  href: https://artifacts.apis.io/portone/conventions/portone-conventions.yml
  title: ''
  type: Conventions
  url: conventions/portone-conventions.yml
- group: design
  href: https://artifacts.apis.io/portone/conventions/portone-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/portone-conventions.yml
- group: design
  href: https://artifacts.apis.io/portone/errors/portone-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/portone-problem-types.yml
- group: build
  href: https://artifacts.apis.io/portone/errors/portone-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/portone-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/portone/conformance/portone-conformance.yml
  title: ''
  type: Conformance
  url: conformance/portone-conformance.yml
- group: design
  href: https://artifacts.apis.io/portone/data-model/portone-data-model.yml
  title: ''
  type: DataModel
  url: data-model/portone-data-model.yml
- group: start
  href: https://artifacts.apis.io/portone/sandbox/portone-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/portone-sandbox.yml
- group: design
  href: https://artifacts.apis.io/portone/lifecycle/portone-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/portone-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://iamport.github.io/service-status/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.portone.io/api/backward-compatibility
- group: operate
  href: https://artifacts.apis.io/portone/changelog/portone-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/portone-changelog.yml
- group: design
  href: https://artifacts.apis.io/portone/asyncapi/portone-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/portone-webhooks.yml
created: '2026-07-17'
description: PortOne (formerly Iamport) is a Korea-based payment orchestration platform that lets online businesses integrate one API to reach 100+ Korean and global payment methods and PSPs. The V2 REST API (api.portone.io) covers payments, billing keys, scheduled/recurring payments, identity verification, cash receipts, B2B tax invoices, and partner settlement, with the legacy V1 API still served at api.iamport.kr.
finops:
- has_sources: true
  method: derived
  name: Portone Finops
  primary_unit: subscription
  service_category: ''
  slug: portone-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portone.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 8 tools listed.
  name: PortOne MCP Server
  slug: portone-mcp-server
modified: '2026-10-06'
name: PortOne
nav: Providers
network: true
overview: 'PortOne publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Banks API, Billing Keys API, Cash Receipts API, and 17 more. Tagged areas include Payments, Payment Orchestration, Fintech, South Korea, and Billing.


  The PortOne catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  PortOne''s developer surface includes authentication, documentation, engineering blog, getting-started guide, support, signup flow, CLI, and 33 more developer resources.'
plans:
- name: Portone Plans Pricing
  plan_count: 5
  slug: portone-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Portone Rate Limits
  slug: portone-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: PortOne API Rules
  rule_count: 58
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 14
  slug: portone-rules
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 33
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 62.7
    developer_ergonomics: 81.5
    discoverability: 71.7
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/portone/portone-2026-08-17T081325.png
security:
- kind: authentication
  name: Portone Authentication
  slug: portone-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Portone Domain Security
  slug: portone-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Portone Vulnerability Disclosure
  slug: portone-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Portone Trust Center
  slug: portone-trust-center
  summary_line: PCI DSS, ISMS
skill_count: 3
skills:
- name: Run Korean identity verification with PortOne
  slug: portone-identity-verification
- name: Look up and cancel a PortOne payment
  slug: portone-lookup-and-cancel-payment
- name: Charge a customer on file with a PortOne billing key
  slug: portone-recurring-billing
slug: portone
tags:
- Payments
- Payment Orchestration
- Fintech
- South Korea
- Billing
- Identity Verification
website: https://portone.io/
---
