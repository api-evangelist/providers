---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Access-as-a-Service is Payactiv's API-driven infrastructure for embedding Earned Wage Access, debit and payroll card programs, instant payouts, and HCM workforce-data workflows into a partner platform
  name: Payactiv Access-as-a-Service API
  slug: payactiv-access-as-a-service-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://payactiv.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.payactiv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://payactiv.com/developers/
- group: start
  title: ''
  type: SignUp
  url: https://developer.payactiv.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://developer.payactiv.com/#/login
- group: operate
  title: ''
  type: Support
  url: https://payactiv.com/help/
- group: company
  title: ''
  type: Blog
  url: https://payactiv.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://payactiv.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://payactiv.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://payactiv.com/trust-center/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payactiv.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payactiv-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/payactiv-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payactiv-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/payactiv-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payactiv-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payactiv-lifecycle.yml
coverage:
  checked: '2026-08-04'
  detail: Payactiv markets an OpenAPI-based Access-as-a-Service reference, change log and sandbox, but the portal at developer.payactiv.com is an Angular SPA marked noindex,nofollow that loads every spec from apidevelopergatewayservice.payactiv.com/users/modules/{id}, which returns 401 without portal credentials.
  evidence:
  - status: 401
    url: https://apidevelopergatewayservice.payactiv.com/users/modules/1
  - status: 200
    url: https://developer.payactiv.com/openapi.json
  - status: 500
    url: https://api.payactiv.com/openapi.json
  - status: 404
    url: https://payactiv.com/.well-known/agent-card.json
  reason: partner-login
  state: gated
created: '2026-08-04'
description: Payactiv is a Milpitas, California financial-worktech company that provides Earned Wage Access (EWA), a digital wallet, Visa prepaid and payroll cards, savings and financial-wellness services to hourly workers through their employers. Its developer-facing product, Access-as-a-Service, packages that platform as modular APIs so HCM, HRIS, payroll and benefits platforms can embed earned wage access, card issuance and transactions, instant payouts and workforce-data workflows under their own brand. The API surface is documented as OpenAPI-based inside a developer portal at developer.payactiv.com, which also carries the platform change log and sandbox environments; the portal requires an account, so no public specification, reference or sandbox values are reachable anonymously. Payactiv is registered with NMLS (ID 2591928) and holds state EWA licenses, and publishes a Trust Center citing SOC 2, ISO 27001, PCI DSS and CCPA.
image: https://payactiv.com/wp-content/uploads/2021/04/cropped-siteicon-192x192.png
layout: provider
modified: '2026-08-04'
name: PayActiv
nav: Providers
network: true
overview: 'PayActiv publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Earned Wage Access, Payments, and Payroll.


  PayActiv''s developer surface includes documentation, signup flow, support, engineering blog, and 13 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 26.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payactiv/refs/heads/main/screenshots/payactiv-2026-08-07T191623.png
security:
- kind: domain-security
  name: Payactiv Domain Security
  slug: payactiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Payactiv Trust Center
  slug: payactiv-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, CCPA, Visa Service Provider, Certified B Corporation
slug: payactiv
tags:
- Company
- Financial-Services
- Earned Wage Access
- Payments
- Payroll
- Human Resources
- Cards
- Financial Wellness
- Fintech
website: https://payactiv.com/
---
