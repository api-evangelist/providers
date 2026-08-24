---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Artera's outbound SMS API, marketed to health systems and Artera Marketplace vendors as the SendMessage API. It sends real-time text messages to patients from the health system's trusted Artera number
  name: Artera Messaging API (MAPI)
  slug: artera-messaging-api-mapi
- description: A Marketplace-vendor API that attaches custom partner content to a patient's upcoming or past appointment or encounter, including post-discharge content. Vendors call Artera with Appointment and/or En
  name: Artera Extended Data API
  slug: artera-extended-data-api
artifact_total: 9
asyncapis:
- description: ''
  name: Artera Webhooks
  slug: artera-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://artera.io/
- group: company
  title: ''
  type: Blog
  url: https://artera.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://artera.io/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artera.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artera.io/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://safebase.artera.io/
- group: auth
  title: ''
  type: Compliance
  url: https://artera.io/trust-center/
- group: auth
  title: ''
  type: Security
  url: https://artera.io/vulnerability-disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/artera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artera-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.artera.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.artera.io/login
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.artera.io/docs/0dbfeef0-de7e-4dee-8435-09c5cffd7ed1/specification
- group: start
  title: ''
  type: GettingStarted
  url: https://knowledge.artera.io/en_US/get-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.wellapp.com/s/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.artera.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/artera-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://knowledge.artera.io/en_US/release-notes/2026-releases
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/artera-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/artera-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/artera-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/artera-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/artera-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/artera-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/artera-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/artera-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/artera-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/artera-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/artera-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/artera-llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://artera.io/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://app.wellapp.com/login
- group: docs
  title: ''
  type: TechnicalSpecifications
  url: https://knowledge.artera.io/en_US/technical-specifications/1239793-technical-specifications
coverage:
  checked: '2026-08-15'
  detail: Artera runs a real API program — a Messaging API (MAPI) and an Extended Data API, both named in its public knowledge base and monitored as "SendMessage API" on its status page — but every specification sits behind account registration at apidocs.artera.io, whose own TLS certificate expired 2026-01-27, so the documented portal link fails certificate validation and only resolves over plain http to an SPA that returns the same HTML shell for /openapi.json as for every other path.
  evidence:
  - status: 0
    url: https://apidocs.artera.io/docs/0dbfeef0-de7e-4dee-8435-09c5cffd7ed1/specification
  - status: 200
    url: https://apidocs.artera.app/openapi.json
  - status: 404
    url: https://api.artera.io/openapi.json
  - status: 200
    url: https://api.artera.io/health
  - status: 200
    url: https://knowledge.artera.io/en_US/use-cases-and-add-ons/messaging-api-mapi
  reason: partner-login
  state: gated
created: '2026-07-17'
description: Artera is a healthcare technology company providing an AI-powered patient communication and engagement platform used by hospitals, health systems, and medical practices to unify how they reach and care for patients. The platform orchestrates SMS, voice, email, and chat across the patient journey — appointment scheduling and reminders, patient intake, payments, referral management, care-gap closure, prescription refills, multilingual engagement, and after-hours call routing and triage — increasingly through agentic AI. Artera connects to the EHR and patient-facing vendors via API, FHIR, and HL7v2 integrations with major systems including Epic, Oracle Health, MEDITECH, athenahealth, eClinicalWorks, Veradigm, NextGen, Greenway, ModMed, AdvancedMD, and Netsmart. The company maintains a strong security and compliance posture (SOC 2 Type 2, HITRUST, ISO 27001/27017/27018/27701, FedRAMP, HIPAA). It was surfaced as a Techstars portfolio company and added to the API Evangelist network.
image: https://artera.io/wp-content/uploads/2024/03/cropped-favicon-300x300.png
layout: provider
modified: '2026-07-18'
name: Artera
nav: Providers
network: true
overview: 'Artera publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Patient Communication, Patient Engagement, and Health IT.


  The Artera catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Artera''s developer surface includes engineering blog, support, documentation, API reference, getting-started guide, changelog, release notes, and 26 more developer resources.'
plans:
- name: Artera Plans Pricing
  plan_count: 0
  slug: artera-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Artera Rate Limits
  slug: artera-rate-limits
score:
  band: developing
  composite: 53.7
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 53.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artera/refs/heads/main/screenshots/artera-2026-07-25T201322.png
security:
- kind: authentication
  name: Artera Authentication
  slug: artera-authentication
  summary_line: oauth2/apiKey/saml2 · 3 schemes
- kind: domain-security
  name: Artera Domain Security
  slug: artera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Artera Vulnerability Disclosure
  slug: artera-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Artera Trust Center
  slug: artera-trust-center
  summary_line: SOC 2 Type 2, HITRUST, ISO 27001, ISO 27017, ISO 27018, ISO 27701, FedRAMP
slug: artera
tags:
- Company
- Healthcare
- Patient Communication
- Patient Engagement
- Health IT
- EHR Integration
- FHIR
- Agentic AI
website: https://artera.io/
---
