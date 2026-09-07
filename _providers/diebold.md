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
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-09-06'
api_count: 8
apis:
- baseURL: https://{customer-host}:8080/OB-API-REST/v2
  baseurl_source: declared
  description: Public REST API of Diebold Nixdorf for banking core system integration — authentication, account information, consumer information and account processing operations used by Vynamic Transaction Middlew
  name: DN Open Backend API
  slug: dn-open-backend-api
- baseURL: https://{customer-host}:8080/tm-om-api/v4
  baseurl_source: declared
  description: Diebold Nixdorf Online & Mobile API — the Vynamic Transaction Middleware surface used by online and mobile banking channels for cardless and mobile-initiated self-service transactions. 35 paths, beare
  name: DN Online & Mobile API
  slug: dn-online-mobile-api
- baseURL: https://{customer-host}:8080/tm-assist-api/v1
  baseurl_source: declared
  description: Diebold Nixdorf API for SelfService Assistance — remote assistance, session and device interaction operations against self-service terminals. 23 paths with basic, bearer and JWE-bearer authentication;
  name: DN Assist API
  slug: dn-assist-api
- baseURL: https://{customer-host}:8080/pi-api/v1
  baseurl_source: declared
  description: Public Payment Initiation API (PI-API) of Diebold Nixdorf providing access to the Vynamic Transaction Middleware for initiating payments. Declares an OpenID Connect scheme against a Microsoft Entra ID
  name: DN Payment Initiation API
  slug: dn-payment-initiation-api
- baseURL: https://{customer-host}:8080/oauth-api/v1
  baseurl_source: declared
  description: Public TM Authorization API of Diebold Nixdorf used to obtain and manage access tokens for the Vynamic Transaction Middleware. 8 paths with HTTP basic and bearer schemes; OpenAPI 3.0.3, version 1.8.1.
  name: DN TM Authorization API
  slug: dn-tm-authorization-api
- baseURL: https://{customer-host}:8080/account/v1
  baseurl_source: declared
  description: Public API of Diebold Nixdorf for account balance management, exposing balance and account business-component operations to the Vynamic banking stack. 5 paths; OpenAPI 3.0.1, version 1.0.0.
  name: DN Account BC API
  slug: dn-account-bc-api
- baseURL: https://{customer-host}:8080/tm-sbp-api/v1
  baseurl_source: declared
  description: Diebold Nixdorf API for invoking predefined, configurable business process flows with a single request (formerly the Pledge API), authorized through an external OpenID Connect provider configured in t
  name: DN Secure Business Processing API
  slug: dn-secure-business-processing-api
- baseURL: https://{issuer-host}
  baseurl_source: declared
  description: Outbound Diebold Nixdorf API used to inform card issuers of services requested by, or on behalf of, their account holders, so issuers can guide the account holder experience through the token requesto
  name: TM Pre-Digitization API (Outbound)
  slug: tm-pre-digitization-api-outbound
artifact_total: 14
asyncapis:
- description: ''
  name: Diebold Webhooks
  slug: diebold-webhooks
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/diebold-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/diebold-vulnerability-disclosure.yml
- group: auth
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
  title: ''
  type: Security
  url: security/diebold-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/diebold-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/diebold-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/diebold-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/diebold-decline-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/diebold-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/diebold-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/diebold-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/diebold-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/diebold-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/diebold-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/diebold-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/diebold-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/diebold-mcp.yml
- group: design
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
overview: 'Diebold Nixdorf publishes 8 APIs on the [APIs.io](https://apis.io/) network, including DN Open Backend API, DN Online & Mobile API, DN Assist API, and 5 more. Tagged areas include Banking, Retail, ATM, Self-Service, and Point-of-Sale.


  The Diebold Nixdorf catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Diebold Nixdorf''s developer surface includes authentication, support, sandbox, documentation, API reference, and 23 more developer resources.'
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
random_paper: 9
rate_limits:
- limit_count: 0
  name: Diebold Rate Limits
  slug: diebold-rate-limits
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 42.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 61.6
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 3.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
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
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
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
