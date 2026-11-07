---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 67
  human_in_the_loop: 0
  name: Google Pay Agentic Access
  operation_count: 99
  slug: google-pay-agentic-access
  summary_line: 99 operations · 67 acting
api_count: 28
apis:
- description: Enables integration of the Google Pay payment method into web applications, allowing merchants to accept payments from cards saved to Google Accounts. The API provides JavaScript client methods for im
  name: Google Pay API
  slug: google-pay-api
- description: Enables integration of Google Pay into Android applications, allowing users to pay with cards saved to their Google Account. The API provides methods to check payment readiness and load payment data f
  name: Google Pay API for Android
  slug: google-pay-api-for-android
- description: Provides services hosted by Google for processing facilitated payment events as part of Google Standard Payments. Payment integrators use this API to report and manage transaction events within the Go
  name: Google Pay Facilitated Transaction Event API
  slug: google-pay-facilitated-transaction-event-api
- description: Enables payment integrators to enroll cards, retrieve virtual card numbers, manage transactions, and handle authentication challenges for virtual card payments. Used by issuers and payment service pro
  name: Google Pay Virtual Cards API
  slug: google-pay-virtual-cards-api
- description: Allows card issuers to provision payment cards directly into Google Pay and Google Wallet from their own applications. Issuers can set default payment tokens, manage token lifecycle, and enable push p
  name: Google Pay Push Provisioning API
  slug: google-pay-push-provisioning-api
- description: Enables Android applications to scan credit and debit cards using the device camera to extract card number and expiration date through on-device optical character recognition. Processing occurs entire
  name: Google Pay Payment Card Recognition API
  slug: google-pay-payment-card-recognition-api
- description: A toolkit for developers in India to integrate their Android, iOS, and web applications with Google Pay for accepting UPI and card-based payments. Supports merchant onboarding, payment initiation, and
  name: Google Pay India Merchant SDK
  slug: google-pay-india-merchant-sdk
- description: A standard for securely and efficiently exchanging commerce data between merchant and platform systems to enable checkout experiences directly on Google surfaces including Search and Gemini. Merchants
  name: Google Universal Commerce Protocol
  slug: google-universal-commerce-protocol
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The eventticketclass API from Google Pay — 3 operation(s) for eventticketclass.
  name: Google Pay Eventticketclass API
  slug: google-pay-eventticketclass-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The eventticketobject API from Google Pay — 4 operation(s) for eventticketobject.
  name: Google Pay Eventticketobject API
  slug: google-pay-eventticketobject-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The flightclass API from Google Pay — 3 operation(s) for flightclass.
  name: Google Pay Flightclass API
  slug: google-pay-flightclass-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The flightobject API from Google Pay — 3 operation(s) for flightobject.
  name: Google Pay Flightobject API
  slug: google-pay-flightobject-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The genericclass API from Google Pay — 3 operation(s) for genericclass.
  name: Google Pay Genericclass API
  slug: google-pay-genericclass-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The genericobject API from Google Pay — 3 operation(s) for genericobject.
  name: Google Pay Genericobject API
  slug: google-pay-genericobject-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The giftcardclass API from Google Pay — 3 operation(s) for giftcardclass.
  name: Google Pay Giftcardclass API
  slug: google-pay-giftcardclass-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The giftcardobject API from Google Pay — 3 operation(s) for giftcardobject.
  name: Google Pay Giftcardobject API
  slug: google-pay-giftcardobject-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The issuer API from Google Pay — 2 operation(s) for issuer.
  name: Google Pay Issuer API
  slug: google-pay-issuer-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The jwt API from Google Pay — 2 operation(s) for jwt.
  name: Google Pay JWT API
  slug: google-pay-jwt-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The loyaltyclass API from Google Pay — 3 operation(s) for loyaltyclass.
  name: Google Pay Loyaltyclass API
  slug: google-pay-loyaltyclass-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The loyaltyobject API from Google Pay — 4 operation(s) for loyaltyobject.
  name: Google Pay Loyaltyobject API
  slug: google-pay-loyaltyobject-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The media API from Google Pay — 2 operation(s) for media.
  name: Google Pay Media API
  slug: google-pay-media-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The offerclass API from Google Pay — 3 operation(s) for offerclass.
  name: Google Pay Offerclass API
  slug: google-pay-offerclass-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The offerobject API from Google Pay — 3 operation(s) for offerobject.
  name: Google Pay Offerobject API
  slug: google-pay-offerobject-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The permissions API from Google Pay — 1 operation(s) for permissions.
  name: Google Pay Permissions API
  slug: google-pay-permissions-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The smarttap API from Google Pay — 1 operation(s) for smarttap.
  name: Google Pay Smarttap API
  slug: google-pay-smarttap-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The transitclass API from Google Pay — 3 operation(s) for transitclass.
  name: Google Pay Transitclass API
  slug: google-pay-transitclass-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The transitobject API from Google Pay — 3 operation(s) for transitobject.
  name: Google Pay Transitobject API
  slug: google-pay-transitobject-api
- baseURL: https://walletobjects.googleapis.com
  baseurl_source: declared
  description: The walletobjects API from Google Pay — 1 operation(s) for walletobjects.
  name: Google Pay Walletobjects API
  slug: google-pay-walletobjects-api
artifact_total: 49
common:
- group: agent
  href: https://artifacts.apis.io/google-pay/agentic-access/google-pay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-pay-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/google-pay/rules/google-pay-rules.yml
  title: ''
  type: Spectral
  url: rules/google-pay-rules.yml
- group: design
  href: https://artifacts.apis.io/google-pay/json-ld/google-pay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-pay-context.jsonld
- group: design
  href: https://artifacts.apis.io/google-pay/vocabulary/google-pay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/google-pay-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/google-pay/data-model/google-pay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-pay-data-model.yml
- group: other
  href: https://artifacts.apis.io/google-pay/hosts/google-pay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/google-pay-hosts.yml
- group: build
  href: https://artifacts.apis.io/google-pay/integrations/google-pay-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/google-pay-integration-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/pay/api/faq
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: auth
  href: https://artifacts.apis.io/google-pay/security/google-pay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-pay-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-pay/security/google-pay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-pay-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-pay
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/pay
- group: docs
  title: ''
  type: Brand Guidelines
  url: https://developers.google.com/pay/api/web/guides/brand-guidelines
- group: commercial
  title: ''
  type: TermsOfService
  url: https://payments.developers.google.com/terms/sellertos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/pay/api/web/guides/tutorial
- group: build
  href: https://artifacts.apis.io/google-pay/packages/google-pay-packages.yml
  title: ''
  type: SDKs
  url: packages/google-pay-packages.yml
- group: start
  title: ''
  type: Console
  url: https://pay.google.com/business/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.google.com/pay/api/status
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/pay/api/web/support/troubleshooting
- group: company
  title: ''
  type: Blog
  url: https://developers.googleblog.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/pay/api/web/support/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google-pay
- group: operate
  title: ''
  type: FAQ
  url: https://developers.google.com/pay/api/web/support/faq
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/pay/api/web
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/pay/api/web/reference/client
- group: start
  title: ''
  type: SignUp
  url: https://pay.google.com/business/console/
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: auth
  href: https://artifacts.apis.io/google-pay/well-known/google-pay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-pay-security.txt
- group: agent
  href: https://artifacts.apis.io/google-pay/well-known/google-pay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-pay-well-known.yml
- group: agent
  href: https://artifacts.apis.io/google-pay/mcp/google-pay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/google-pay-mcp.yml
- group: build
  href: https://artifacts.apis.io/google-pay/mcp/google-pay-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/google-pay-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/google-pay/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/google-pay/llms/google-pay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-pay-llms.txt
- group: build
  href: https://artifacts.apis.io/google-pay/packages/google-pay-packages.yml
  title: ''
  type: Packages
  url: packages/google-pay-packages.yml
- group: auth
  href: https://artifacts.apis.io/google-pay/authentication/google-pay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-pay-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-pay/scopes/google-pay-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-pay-scopes.yml
- group: design
  href: https://artifacts.apis.io/google-pay/errors/google-pay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-pay-problem-types.yml
- group: design
  href: https://artifacts.apis.io/google-pay/lifecycle/google-pay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-pay-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/google-pay/changelog/google-pay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-pay-changelog.yml
- group: design
  href: https://artifacts.apis.io/google-pay/conventions/google-pay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-pay-conventions.yml
- group: design
  href: https://artifacts.apis.io/google-pay/conformance/google-pay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-pay-conformance.yml
- group: start
  href: https://artifacts.apis.io/google-pay/sandbox/google-pay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/google-pay-sandbox.yml
- group: design
  href: https://artifacts.apis.io/google-pay/components/google-pay-components.yml
  title: ''
  type: Components
  url: components/google-pay-components.yml
- group: docs
  href: https://artifacts.apis.io/google-pay/json-schema/google-pay-ucp-payment-handler-config.json
  title: ''
  type: JSONSchema
  url: json-schema/google-pay-ucp-payment-handler-config.json
- group: operate
  href: https://artifacts.apis.io/google-pay/rate-limits/google-pay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-pay-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-pay/plans/google-pay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-pay-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/google-pay/finops/google-pay-finops.yml
  title: ''
  type: FinOps
  url: finops/google-pay-finops.yml
created: '2024-01-01'
description: Google Pay is Google's digital wallet and payment surface, exposed to developers as a family of distinct APIs rather than one endpoint. The Google Pay API for Web and Android is a client-side payment sheet that returns a signed, ECIES-encrypted payment token for a merchant's gateway to decrypt; the Google Wallet API is a REST service on walletobjects.googleapis.com for issuing loyalty cards, event tickets, boarding passes, transit tickets, gift cards and offers; Google Standard Payments carries the integrator APIs for issuers and PSPs; and the Google Pay & Wallet Developer MCP server gives AI coding agents live access to merchant profiles, integration status and the official documentation.
finops:
- has_sources: true
  method: derived
  name: Google Pay Finops
  primary_unit: ''
  service_category: ''
  slug: google-pay-finops
  template: true
image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
json_schemas:
- name: EventTicketClass
  property_count: 47
  slug: google-pay-event-ticket-class
- name: FlightClass
  property_count: 42
  slug: google-pay-flight-class
- name: LoyaltyClass
  property_count: 47
  slug: google-pay-loyalty-class
- name: OfferClass
  property_count: 44
  slug: google-pay-offer-class
- name: TransitClass
  property_count: 56
  slug: google-pay-transit-class
- name: TransitObject
  property_count: 43
  slug: google-pay-transit-object
- name: Google Pay Payment Handler Configuration
  property_count: 5
  slug: google-pay-ucp-payment-handler-config
jsonld:
- class_count: 120
  name: Google Pay Context
  property_count: 324
  slug: google-pay-context
layout: provider
mcp_servers:
- description: 'Google''s first-party remote MCP server for Google Pay and Google Wallet developers. It exposes documentation search over the official Google Pay and Google Wallet docs plus live read and write access '
  name: Google Pay & Wallet Developer MCP server
  slug: google-pay-wallet-developer-mcp-server
modified: '2026-09-12'
name: Google Pay
nav: Providers
network: true
overview: 'Google Pay is listed with 28 APIs on the [APIs.io](https://apis.io/) network, including Eventticketclass API, Eventticketobject API, Flightclass API, and 25 more. Tagged areas include Agentic Commerce, Checkout, Contactless Payments, Digital Wallet, and Merchants.


  The Google Pay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Pay''s developer surface includes pricing, developer portal, getting-started guide, developer console, support, engineering blog, changelog, and 42 more developer resources.'
plans:
- name: Google Pay Plans Pricing
  plan_count: 1
  slug: google-pay-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Google Pay Rate Limits
  slug: google-pay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Google Pay API Rules
  rule_count: 56
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 4
  slug: google-pay-rules
scopes:
- name: Google Pay Scopes
  scope_count: 3
  slug: google-pay-scopes
  summary_line: 3 scopes
score:
  band: strong
  composite: 66.2
  coverage:
    artifact_dirs: 34
    catalog_earned: 81.8
    catalog_earned_first_party: 16.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.4
  facets:
    access_clarity: 60.5
    contract_governance: 35.6
    contract_quality: 61.7
    developer_ergonomics: 73.2
    discoverability: 86.7
    operational_transparency: 65.8
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
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
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/google-pay/google-pay-2026-06-20T182221.png
security:
- kind: authentication
  name: Google Pay Authentication
  slug: google-pay-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Google Pay Domain Security
  slug: google-pay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Pay Vulnerability Disclosure
  slug: google-pay-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: google-pay-integration-health
  slug: google-pay-integration-health
- name: google-pay-merchant-onboarding
  slug: google-pay-merchant-onboarding
- name: google-pay-wallet-pass-inventory
  slug: google-pay-wallet-pass-inventory
slug: google-pay
tags:
- Agentic Commerce
- Checkout
- Contactless Payments
- Digital Wallet
- Merchants
- Mobile Payments
- Payments
- Tokenization
website: https://www.google.com/
---
