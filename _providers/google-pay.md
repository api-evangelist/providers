---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-09-18'
api_count: 9
apis:
- description: Enables integration of the Google Pay payment method into web applications, allowing merchants to accept payments from cards saved to Google Accounts. The API provides JavaScript client methods for im
  name: Google Pay API
  slug: google-pay-api
- description: Enables integration of Google Pay into Android applications, allowing users to pay with cards saved to their Google Account. The API provides methods to check payment readiness and load payment data f
  name: Google Pay API for Android
  slug: google-pay-api-for-android
- description: APIs for creating and managing digital passes for Google Wallet, including loyalty cards, event tickets, boarding passes, transit tickets, gift cards, offers, and generic passes. Issuers can define pa
  name: Google Wallet API
  slug: google-wallet-api
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
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/security/google-pay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-pay-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/security/google-pay-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/packages/google-pay-packages.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/well-known/google-pay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-pay-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/well-known/google-pay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-pay-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/mcp/google-pay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/google-pay-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/mcp/google-pay-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/google-pay-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/llms/google-pay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-pay-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/packages/google-pay-packages.yml
  title: ''
  type: Packages
  url: packages/google-pay-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/authentication/google-pay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-pay-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/scopes/google-pay-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-pay-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/errors/google-pay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-pay-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/lifecycle/google-pay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-pay-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/changelog/google-pay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-pay-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/conventions/google-pay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-pay-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/conformance/google-pay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-pay-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/sandbox/google-pay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/google-pay-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/components/google-pay-components.yml
  title: ''
  type: Components
  url: components/google-pay-components.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/json-schema/google-pay-ucp-payment-handler-config.json
  title: ''
  type: JSONSchema
  url: json-schema/google-pay-ucp-payment-handler-config.json
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/rate-limits/google-pay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-pay-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/plans/google-pay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-pay-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/finops/google-pay-finops.yml
  title: ''
  type: FinOps
  url: finops/google-pay-finops.yml
created: '2024-01-01'
description: Google Pay is Google's digital wallet and payment surface, exposed to developers as a family of distinct APIs rather than one endpoint. The Google Pay API for Web and Android is a client-side payment sheet that returns a signed, ECIES-encrypted payment token for a merchant's gateway to decrypt; the Google Wallet API is a REST service on walletobjects.googleapis.com for issuing loyalty cards, event tickets, boarding passes, transit tickets, gift cards and offers; Google Standard Payments carries the integrator APIs for issuers and PSPs; and the Google Pay & Wallet Developer MCP server gives AI coding agents live access to merchant profiles, integration status and the official documentation.
finops:
- name: Google Pay Finops
  service_category: API
  slug: google-pay-finops
image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
json_schemas:
- name: Google Pay Payment Handler Configuration
  property_count: 5
  slug: google-pay-ucp-payment-handler-config
layout: provider
mcp_servers:
- description: 'Google''s first-party remote MCP server for Google Pay and Google Wallet developers. It exposes documentation search over the official Google Pay and Google Wallet docs plus live read and write access '
  name: Google Pay & Wallet Developer MCP server
  slug: google-pay-wallet-developer-mcp-server
modified: '2026-09-12'
name: Google Pay
nav: Providers
network: true
overview: 'Google Pay publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agentic Commerce, Checkout, Contactless Payments, Digital Wallet, and Merchants.


  Google Pay''s developer surface includes developer portal, getting-started guide, developer console, support, engineering blog, changelog, FAQ, and 34 more developer resources.'
plans:
- name: Google Pay Plans Pricing
  plan_count: 1
  slug: google-pay-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Google Pay Rate Limits
  slug: google-pay-rate-limits
scopes:
- name: Google Pay Scopes
  scope_count: 3
  slug: google-pay-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.0
    catalog_earned_first_party: 16.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 73.2
    discoverability: 88.9
    operational_transparency: 65.8
  previous_composite: 51.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/google-pay/refs/heads/main/screenshots/google-pay-2026-06-20T182221.png
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
