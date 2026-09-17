---
access_model:
  confidence: high
  label: Enterprise licence, sales-gated
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - pricing
  - authentication
  - documentation
  trial: false
  try_now: false
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.9
  scored_at: '2026-09-16'
api_count: 9
apis:
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The Accessibility API API from Diebold Nixdorf — 4 operation(s) for accessibility api.
  name: Diebold Nixdorf Accessibility API
  slug: diebold-accessibility-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: Request processing in Account BC
  name: Diebold Nixdorf Account BC API
  slug: diebold-account-bc-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: Fetches account information.
  name: Diebold Nixdorf Account Information API
  slug: diebold-account-information-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The Account Management API API from Diebold Nixdorf — 9 operation(s) for account management api.
  name: Diebold Nixdorf Account Management API
  slug: diebold-account-management-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: Performs a transaction.
  name: Diebold Nixdorf Account Processing API
  slug: diebold-account-processing-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The Activation Methods API from Diebold Nixdorf — 3 operation(s) for activation methods.
  name: Diebold Nixdorf Activation Methods API
  slug: diebold-activation-methods-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: Authentication request for a transaction.
  name: Diebold Nixdorf Authentication API
  slug: diebold-authentication-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The Authorization Processing API API from Diebold Nixdorf — 31 operation(s) for authorization processing api.
  name: Diebold Nixdorf Authorization Processing API
  slug: diebold-authorization-processing-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: Fetches consumer information.
  name: Diebold Nixdorf Consumer Information API
  slug: diebold-consumer-information-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The Device API API from Diebold Nixdorf — 2 operation(s) for device api.
  name: Diebold Nixdorf Device API
  slug: diebold-device-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The DN Assist API API from Diebold Nixdorf — 23 operation(s) for dn assist api.
  name: Diebold Nixdorf DN Assist API
  slug: diebold-dn-assist-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The Miscellaneous API API from Diebold Nixdorf — 10 operation(s) for miscellaneous api.
  name: Diebold Nixdorf Miscellaneous API
  slug: diebold-miscellaneous-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: Public Payment Initiation API (PI-API) of DieboldNixdorf to access the Transaction Middleware.
  name: Diebold Nixdorf Payment Initiation API
  slug: diebold-payment-initiation-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The Prestaged Transaction API API from Diebold Nixdorf — 7 operation(s) for prestaged transaction api.
  name: Diebold Nixdorf Prestaged Transaction API
  slug: diebold-prestaged-transaction-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The SBP API API from Diebold Nixdorf — 2 operation(s) for sbp api.
  name: Diebold Nixdorf SBP API
  slug: diebold-sbp-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The SEPA Credit Transfer Instant API API from Diebold Nixdorf — 2 operation(s) for sepa credit transfer instant api.
  name: Diebold Nixdorf SEPA Credit Transfer Instant API
  slug: diebold-sepa-credit-transfer-instant-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The Standing Order API API from Diebold Nixdorf — 4 operation(s) for standing order api.
  name: Diebold Nixdorf Standing Order API
  slug: diebold-standing-order-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The TM Authorization API API from Diebold Nixdorf — 3 operation(s) for tm authorization api.
  name: Diebold Nixdorf TM Authorization API
  slug: diebold-tm-authorization-api-api
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: The TM OAuth API API from Diebold Nixdorf — 5 operation(s) for tm oauth api.
  name: Diebold Nixdorf TM OAuth API
  slug: diebold-tm-oauth-api-api
artifact_total: 25
asyncapis:
- description: ''
  name: Diebold Webhooks
  slug: diebold-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/overlays/diebold-dn-open-backend-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diebold-dn-open-backend-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/overlays/diebold-dn-online-mobile-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diebold-dn-online-mobile-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/overlays/diebold-dn-assist-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diebold-dn-assist-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/overlays/diebold-dn-payment-initiation-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diebold-dn-payment-initiation-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/overlays/diebold-dn-tm-authorization-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diebold-dn-tm-authorization-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/overlays/diebold-dn-account-bc-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diebold-dn-account-bc-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/overlays/diebold-dn-secure-business-processing-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diebold-dn-secure-business-processing-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/overlays/diebold-tm-pre-digitization-api-outbound-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diebold-tm-pre-digitization-api-outbound-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/authentication/diebold-authentication.yml
  title: ''
  type: Authentication
  url: authentication/diebold-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/security/diebold-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/diebold-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/security/diebold-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diebold-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/diebold
- group: company
  title: ''
  type: Website
  url: https://www.dieboldnixdorf.com
- group: operate
  title: ''
  type: Support
  url: https://www.dieboldnixdorf.com/en-us/support
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/security/diebold-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/diebold-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/conventions/diebold-conventions.yml
  title: ''
  type: Conventions
  url: conventions/diebold-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/conventions/diebold-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/diebold-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/errors/diebold-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/diebold-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/errors/diebold-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/diebold-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/conformance/diebold-conformance.yml
  title: ''
  type: Conformance
  url: conformance/diebold-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/lifecycle/diebold-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/diebold-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/data-model/diebold-data-model.yml
  title: ''
  type: DataModel
  url: data-model/diebold-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/plans/diebold-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/diebold-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/rate-limits/diebold-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/diebold-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/sandbox/diebold-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/diebold-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/packages/diebold-packages.yml
  title: ''
  type: Packages
  url: packages/diebold-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/llms/diebold-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diebold-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/mcp/diebold-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/diebold-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/asyncapi/diebold-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/diebold-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vrp-api.dieboldnixdorf.com/vrp/docs/vynamic-retail-platform-vrp
- group: docs
  title: ''
  type: Documentation
  url: https://api.swaggerhub.com/apis/Diebold-Nixdorf
- group: docs
  title: ''
  type: APIReference
  url: https://api.swaggerhub.com/apis/Diebold-Nixdorf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dieboldnixdorf.com/en-us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dieboldnixdorf.com/en-us/privacy-policy/global-privacy-notice
- group: operate
  title: ''
  type: Contact
  url: https://www.dieboldnixdorf.com/en-us/contact-us
created: '2026-03-24'
description: 'Diebold Nixdorf is a global provider of connected commerce technology for the financial and retail industries — ATMs and self-service terminals, retail point-of-sale hardware, the Vynamic software portfolio (Payments, Transaction Middleware, Self-Service, Security, Retail Platform) and the managed services around them. Its integration surface is enterprise and customer-deployed rather than self-serve: eight public OpenAPI definitions for the Vynamic banking stack are published through the company''s SwaggerHub organization, while the Vynamic Retail Platform developer portal sits behind a login and the former developer community no longer resolves. There is no public signup, pricing page or published rate limit, and every specification names a customer-hosted server.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diebold.png
layout: provider
modified: '2026-09-06'
name: Diebold Nixdorf
nav: Providers
network: true
overview: 'Diebold Nixdorf publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Accessibility API, Account BC API, Account Information API, and 16 more. Tagged areas include Banking, Retail, ATM, Self-Service, and Point-of-Sale.


  The Diebold Nixdorf catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Diebold Nixdorf''s developer surface includes authentication, support, sandbox, documentation, API reference, and 31 more developer resources.'
plans:
- name: Diebold Plans Pricing
  plan_count: 0
  slug: diebold-plans-pricing
press:
- date: '2026-05-25'
  title: Diebold Nixdorf's post
  url: https://www.facebook.com/DieboldNixdorf/posts/ai-driven-efficiency-is-only-the-beginning-the-real-opportunity-lies-in-using-in/1371052748393889/
- date: '2026-05-25'
  title: SeeChange Partners with Diebold Nixdorf to Transform ...
  url: https://www.prnewswire.com/news-releases/seechange-partners-with-diebold-nixdorf-to-transform-retail-checkout-through-the-power-of-ai-301722354.html
- date: '2026-05-25'
  title: Diebold Nixdorf declares war on shrink in retail stores with ...
  url: https://retailtechinnovationhub.com/home/2024/1/19/diebold-nixdorf-declares-war-on-shrink-in-retail-stores-with-artificial-intelligence-powered-offering
- date: '2026-05-25'
  title: Artificial Intelligence (AI)
  url: https://www.dieboldnixdorf.com/en-us/retail/artificial-intelligence-ai/
- date: '2026-05-25'
  title: Diebold Nixdorf taps SeeChange machine learning for self- ...
  url: https://www.kioskmarketplace.com/news/diebold-nixdorf-taps-seechange-machine-learning-for-self-checkout-solutions/
random_paper: 19
rate_limits:
- limit_count: 0
  name: Diebold Rate Limits
  slug: diebold-rate-limits
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 61.6
    developer_ergonomics: 51.8
    discoverability: 81.5
    operational_transparency: 18.4
  previous_composite: 45.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: berlin-group-nextgenpsd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/diebold/refs/heads/main/screenshots/diebold-2026-06-20T180010.png
security:
- kind: authentication
  name: Diebold Authentication
  slug: diebold-authentication
  summary_line: http/openIdConnect · 3 schemes
- kind: domain-security
  name: Diebold Domain Security
  slug: diebold-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Diebold Vulnerability Disclosure
  slug: diebold-vulnerability-disclosure
  summary_line: Hackerone
slug: diebold
tags:
- Banking
- Retail
- ATM
- Self-Service
- Point-of-Sale
- Payments
- Transaction Middleware
- Vynamic
- Open Banking
- Fortune 1000
website: https://www.dieboldnixdorf.com
---
