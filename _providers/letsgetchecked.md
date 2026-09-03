---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: Version 1 of the LetsGetChecked Orders API. Create a pre-activated test-kit order against a client-supplied order identifier (PUT is documented as idempotent), query order status from dispatch through
  name: LetsGetChecked Orders API (Version 1)
  slug: orders-api-v1
- description: Version 2 of the LetsGetChecked Orders API, documented September 2023. Adds an order-item model with per-item identifiers and statuses, a PATCH endpoint for cancelling an order item up to the KitArriv
  name: LetsGetChecked Orders API (Version 2)
  slug: orders-api-v2
- description: Read laboratory results for test kits processed by the LetsGetChecked lab. Retrieve a full result set for a barcode (with optional alpha code), fetch just the result status, or pull the raw lab result
  name: LetsGetChecked Results API
  slug: results-api
- description: Retrieve and download the results letters LetsGetChecked generates for patients and for a patient's Primary Care Provider. List outreach notifications for a client program with date filtering and X-Co
  name: LetsGetChecked Outreach API
  slug: outreach-api
- description: Event-driven webhook notifications delivered by POST to client-supplied endpoints whenever an order, result or outreach resource changes. Payloads carry a resource identifier, a callback URL back into
  name: LetsGetChecked API Notifications (Webhooks)
  slug: api-notifications
artifact_total: 10
asyncapis:
- description: ''
  name: Letsgetchecked Notifications Webhooks
  slug: letsgetchecked-notifications-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.letsgetchecked.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.letsgetchecked.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.letsgetchecked.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.letsgetchecked.com/documentation/API%20Reference/Getting%20Started/api-operations/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.letsgetchecked.com/documentation/API%20Reference/Getting%20Started/integration-process/
- group: operate
  title: ''
  type: Support
  url: https://help.letsgetchecked.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.letsgetchecked.com/articles/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.letsgetchecked.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LetsGetChecked
- group: start
  title: ''
  type: SignUp
  url: https://www.letsgetchecked.com/register/
- group: start
  title: ''
  type: Login
  url: https://halo.letsgetchecked.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.letsgetchecked.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.letsgetchecked.com/privacy-policy/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.letsgetchecked.com/contact-us/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.letsgetchecked.com/documentation/release-notes/release_notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/letsgetchecked-changelog.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/letsgetchecked-glossary.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/letsgetchecked-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/letsgetchecked-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/letsgetchecked-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/letsgetchecked-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/letsgetchecked-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/letsgetchecked-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.letsgetchecked.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/letsgetchecked-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/letsgetchecked-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.letsgetchecked.com/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/letsgetchecked-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/letsgetchecked-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/letsgetchecked-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/letsgetchecked-notifications-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/letsgetchecked-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/letsgetchecked-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/letsgetchecked-llms.txt
created: '2026-08-04'
description: 'LetsGetChecked (operating as LetsGetChecked powered by FuzeHealth) is an Irish-American virtual care company that runs an end-to-end diagnostics and care platform: it manufactures at-home sample-collection kits, operates its own CLIA-accredited laboratories in the United States and Europe, and layers telehealth consultations, clinical review and affiliate-pharmacy prescription delivery on top of the results. Its Halo platform is a purpose-built EMR that exposes B2B REST APIs — the Orders API (v1 and v2), the Results API and the Outreach API — plus event-driven webhook notifications, so employers, health plans, providers, public-sector programs and life-sciences partners can order pre-activated test kits, track kit fulfillment, and retrieve laboratory results in JSON, HL7 or PDF form inside their own systems.'
image: https://images.ctfassets.net/lnbo4srla2av/7bEYT5tJiJCJ62SSjGaWa7/3d7fba1af10b361826b727f988132700/og-image_1200x630.png
layout: provider
modified: '2026-08-04'
name: LetsGetChecked
nav: Providers
network: true
overview: 'LetsGetChecked publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Diagnostics, and Laboratory.


  The LetsGetChecked catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LetsGetChecked''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 27 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 33.3
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 64.8
    governance: 33.3
    operational_transparency: 31.6
  previous_composite: 50.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 48.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/letsgetchecked/refs/heads/main/screenshots/letsgetchecked-2026-08-07T171554.png
security:
- kind: authentication
  name: Letsgetchecked Authentication
  slug: letsgetchecked-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Letsgetchecked Domain Security
  slug: letsgetchecked-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Letsgetchecked Vulnerability Disclosure
  slug: letsgetchecked-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Letsgetchecked Trust Center
  slug: letsgetchecked-trust-center
  summary_line: GDPR, HITRUST, NIST, ISO 13485
slug: letsgetchecked
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Laboratory
- Telehealth
- Medical Testing
- Pharmacy
- Order
- Results
- Webhook
- HL7
- LOINC
website: https://www.letsgetchecked.com/
---
