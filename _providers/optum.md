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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 64.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 122
  human_in_the_loop: 3
  name: Optum Agentic Access
  operation_count: 483
  slug: optum-agentic-access
  summary_line: 483 operations · 122 acting · 3 human-in-the-loop
api_count: 9
apis:
- description: RESTful JSON and native X12 EDI (270/271, 837P/837I, 276/277, 835) healthcare transaction APIs for real-time patient eligibility and coverage verification, enhanced eligibility with asynchronous cover
  name: Optum Medical Network Eligibility and Claims API
  slug: optum-medical-network-eligibility-and-claims-api
- description: 'Optum Real point-of-care APIs on the oihub gateway: pre-service eligibility, claim pre-check, claim actions, claim inquiry, patient benefit check, document search, auth referral submission, plus HL7 F'
  name: Optum Real (Medical) API
  slug: optum-real-medical-api
- description: 'Real-time dental data exchange APIs for pre-care eligibility and eligibility intelligence, pre-care cost estimates, claim submission (GraphQL-backed), claim status inquiry, and attachments with image '
  name: Optum Real for Dental API
  slug: optum-real-for-dental-api
- description: 'Pharmacy network services: a formatting rule API and telecom formatter for NCPDP-style pharmacy claim formatting, and a submitter API for managing pharmacy network submitters.'
  name: Optum Pharmacy Solutions API
  slug: optum-pharmacy-solutions-api
- description: 'Payer enrollment and document tracking for the Optum intelligent clearinghouse: PES payer enrollments, EDI enrollment, and a file and document tracking API for following submissions through the cleari'
  name: Optum Payment and Reimbursement API
  slug: optum-payment-and-reimbursement-api
- description: 'Optum Insight Platform services published on gateway.optuminsightplatform.com: NCC data acquisition, a code-search core service, CMS and Optum common physician and facility provider-directory services'
  name: Optum Insight Platform (Platform and Interoperability) API
  slug: optum-insight-platform-platform-and-interoperability-api
- description: 'Analytics and payment-integrity APIs: PROMETHEUS Analytics job submission and check-job for episode-of-care analytics, ABM care decision support, and ABM pre-pay DME, pre-pay lab and prior-authorizati'
  name: Optum Analytics and Insights API
  slug: optum-analytics-and-insights-api
- description: The platform OAuth2 token service. Security and Authorization v2 issues a one-hour JWT bearer token at /apip/auth/v2/token for the Medical Network and Dental APIs; v3 ("sentinel") issues one at /apip/
  name: Optum API Tools — Security and Authorization
  slug: optum-api-tools-security-and-authorization
- description: Optum's payer-side CMS Interoperability and Patient Access (CMS-9115-F) surface — Patient Access, Provider Directory and Payer-to-Payer exchange for the Optum behavioral and physical health plans. The
  name: Optum Interoperability APIs (CMS Patient Access)
  slug: optum-interoperability-apis-cms-patient-access
artifact_total: 17
asyncapis:
- description: ''
  name: Optum Webhooks
  slug: optum-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optum-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/optum-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.optum.com/vulnerability.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optum-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/optum-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/optum-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optum-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/optum-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/optum-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optum-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.optum.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.optum.com/apitools/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.optum.com/eligibilityandclaims/reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.optum.com/eligibilityandclaims/docs/get-started-with-optum-api
- group: operate
  title: ''
  type: Support
  url: https://community.optum.com/developers/home
- group: start
  title: ''
  type: SignUp
  url: https://marketplace.optum.com/apiservices/api-sandbox-access
- group: start
  title: ''
  type: Sandbox
  url: https://marketplace.optum.com/apiservices/api-sandbox-access
- group: company
  title: ''
  type: Website
  url: https://www.optum.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optum.com/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optum.com/privacy-policy.html
- group: build
  title: ''
  type: Packages
  url: packages/optum-packages.yml
- group: auth
  title: ''
  type: Compliance
  url: https://business.optum.com/en/federal-government/about-optum-serve/certifications-partnerships.html
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/optum-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/optum-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/optum-examples.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.optum.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/optum-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/optum-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/optum-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/optum-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://marketplace.optum.com/apiservices/api-sandbox-access
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/optum-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/optum-servers-and-provenance-overlay.yaml
- group: other
  title: ''
  type: APICatalog
  url: https://developer.optum.com/.well-known/api-catalog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Optum
- group: company
  title: ''
  type: Blog
  url: https://www.optum.com/en/newsroom.html
created: '2026-07-17'
description: 'Optum, part of UnitedHealth Group, is a health services and technology company that operates one of the largest medical, dental and pharmacy networks in the United States and runs the clearinghouse formerly known as Change Healthcare. Its developer platform (developer.optum.com) publishes eight product lines of RESTful JSON, native X12 EDI and HL7 FHIR R4 APIs: eligibility and coverage discovery, professional and institutional claim validation and submission, claim status, ERA/remittance reports, attachments, payer directory and outage feeds, prior authorization in both X12 278 and FHIR Da Vinci PAS/DTR/CRD form, provider access and bulk member match, dental pre-care estimates and claims, pharmacy formatting and submitter services, payer enrollment and document tracking, and Optum Insight Platform data, code-search and analytics services. Every API is secured with an OAuth2 client-credentials JWT bearer token over TLS 1.2+, with a free canned-response sandbox on a separate
  host. Optum also publishes an RFC 9727 API catalog at /.well-known/api-catalog, which is how the 59 OpenAPI documents in this repo were harvested.'
image: https://www.optum.com/content/dam/optum4/images/logos/optum-logo.svg
layout: provider
modified: '2026-08-14'
name: Optum
nav: Providers
network: true
overview: 'Optum publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Medical Network Eligibility and Claims API, Real (Medical) API, Real for Dental API, and 5 more. Tagged areas include Company, Healthcare, Health Insurance, Claims, and Eligibility.


  The Optum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Optum''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, sandbox, and 32 more developer resources.'
plans:
- name: Optum Plans Pricing
  plan_count: 0
  slug: optum-plans-pricing
random_paper: 118
rate_limits:
- limit_count: 0
  name: Optum Rate Limits
  slug: optum-rate-limits
scopes:
- name: Optum Scopes
  scope_count: 7
  slug: optum-scopes
  summary_line: 7 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 57.8
  delta: 26.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 59.5
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 31.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/optum/refs/heads/main/screenshots/optum-2026-08-07T190817.png
security:
- kind: authentication
  name: Optum Authentication
  slug: optum-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Optum Domain Security
  slug: optum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Optum Vulnerability Disclosure
  slug: optum-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: optum
tags:
- Company
- Healthcare
- Health Insurance
- Claims
- Eligibility
- FHIR
- Interoperability
- Pharmacy
- EDI
- X12
- Payments
- Prior Authorization
- Clearinghouse
- Revenue Cycle
- Dental
- Da Vinci
- Patient Access
- Remittance
- Attachments
- Payer Directory
website: https://www.optum.com/
---
