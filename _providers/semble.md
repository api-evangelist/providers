---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: GraphQL queries and mutations over the Semble patient record — patients, demographics, phone numbers, relationships, labels, memberships, access groups, allergy records, free-text records, patient doc
  name: Semble Patients API
  slug: semble-patients-api
- description: 'GraphQL surface for appointments and scheduling — bookings, bookings-by-id, availabilities, availability rules, availability settings, availability slots, online booking configurations, out-of-office '
  name: Semble Scheduling & Bookings API
  slug: semble-scheduling-api
- description: GraphQL surface for clinical documentation and care pathways — consultations, clinical pathways, clinical reports, episodes and episode types, letters, working diagnoses, diagnosis codes, forms and qu
  name: Semble Clinical API
  slug: semble-clinical-api
- description: GraphQL surface for e-prescribing and diagnostics — prescriptions, repeat prescriptions and lab / pathology orders and results, integrated with Semble's pharmacy and lab partner network.
  name: Semble Prescriptions & Labs API
  slug: semble-prescriptions-labs-api
- description: GraphQL surface for practice finances — invoices, invoice payments and line items, account statements, products, price profiles, price rules and price adjustment rules, and Semble Pay payment terminal
  name: Semble Billing & Payments API
  slug: semble-billing-payments-api
- description: GraphQL surface for practice administration and platform integration — practice details, users, contacts, tasks, labels, patient documents, practice template documents, integration tokens and webhooks
  name: Semble Practice & Platform API
  slug: semble-practice-platform-api
artifact_total: 11
asyncapis:
- description: ''
  name: Semble Webhooks
  slug: semble-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/semble-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/semble-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.semble.io/
- group: design
  title: ''
  type: Conformance
  url: conformance/semble-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/semble-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/semble-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/semble-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/semble-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/semble-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/semble-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/semble-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.semble.io/docs/release-notes/
- group: company
  title: ''
  type: Website
  url: https://www.semble.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.semble.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.semble.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.semble.io/docs/API/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.semble.io/api-access
- group: auth
  title: ''
  type: Authentication
  url: https://docs.semble.io/docs/authentication/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.semble.io/
- group: auth
  title: ''
  type: Security
  url: https://trust.semble.io/
- group: company
  title: ''
  type: Blog
  url: https://www.semble.io/blog
- group: operate
  title: ''
  type: Support
  url: https://help.semble.io/
- group: start
  title: ''
  type: SignUp
  url: https://www.semble.io/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.semble.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.semble.io/privacy-policy
created: '2026-07-24'
description: Semble is a London-headquartered (7 Bell Yard, London, WC2A 2JR) cloud clinical and practice-management platform for United Kingdom private and independent healthcare providers, from solo clinicians to corporate and enterprise clinics. Its modular EHR unifies patient records, appointment scheduling and online booking, video consultations, e-prescribing, pathology/lab ordering, clinical documentation, invoicing and payments (Semble Pay) and patient communications. Semble exposes a single open, secure public GraphQL API at https://open.semble.io/graphql, available to Semble clinics at no extra cost, letting developers read and write patients, bookings, availability, consultations, clinical pathways, prescriptions, labs, invoices, tasks, forms, questionnaires and webhooks. Authentication is API-key / token based (an x-token header carrying a role-scoped token that expires after 12 hours) rather than SMART-on-FHIR; the API is GraphQL-native and does not publish an HL7 FHIR CapabilityStatement
  or a downloadable OpenAPI. Semble emphasises GDPR compliance and UK healthcare security standards, with data encrypted in transit and at rest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Semble
nav: Providers
network: true
overview: 'Semble publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United Kingdom, EHR, Practice Management, and GraphQL.


  The Semble catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Semble''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, support, and 19 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 1
  name: Semble Rate Limits
  slug: semble-rate-limits
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 51.9
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/semble/refs/heads/main/screenshots/semble-2026-08-17T081757.png
security:
- kind: authentication
  name: Semble Authentication
  slug: semble-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Semble Domain Security
  slug: semble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Semble Trust Center
  slug: semble-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: semble
tags:
- Healthcare
- United Kingdom
- EHR
- Practice Management
- GraphQL
- Patient Records
- Scheduling
- e-Prescribing
- Interoperability
- Digital Health
website: https://www.semble.io/
---
