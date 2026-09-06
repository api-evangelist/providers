---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://emtech.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.emtech.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emtech.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.emtech.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.emtech.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://emtech.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://emtech.com/resources/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emtech.com
- group: start
  title: ''
  type: SignUp
  url: https://app.emtech.com/register
- group: start
  title: ''
  type: Login
  url: https://app.emtech.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emtech.com/terms-&-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emtech.com/privacy-policy
- group: other
  title: ''
  type: Marketplace
  url: https://emtech.com/beyond-suite/marketplace
- group: auth
  title: ''
  type: Authentication
  url: authentication/emtech-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/emtech-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/emtech-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emtech-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/emtech-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/emtech-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emtech-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emtech-llms.txt
created: '2026-07-17'
description: EMTECH is a financial-technology company founded in 2019 that modernizes financial market infrastructure for central banks, financial regulators, and financial service providers. Its Beyond Suite delivers regulatory sandbox management (Beyond Sandbox), digital cash and central bank digital currency infrastructure (Beyond Cash), automated compliance operations (Beyond Compliance), and risk-based supervision (Beyond Supervision), exposed through regulatory-reporting and data-ingestion APIs for microlending, remittance, payments, virtual assets, crowdfunding, consumer protection, and a CBDC simulator. EMTECH works with African central banks including the Bank of Ghana, the Central Bank of Nigeria, and Liberia, and is SOC 2 and ISO 27001 certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emtech.png
layout: provider
modified: '2026-07-19'
name: EMTECH
nav: Providers
network: true
overview: 'EMTECH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, RegTech, Central Banking, and CBDC.


  EMTECH''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 14 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 32.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emtech/refs/heads/main/screenshots/emtech-2026-07-25T213255.png
security:
- kind: authentication
  name: Emtech Authentication
  slug: emtech-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Emtech Domain Security
  slug: emtech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: emtech
tags:
- Company
- Financial-Services
- RegTech
- Central Banking
- CBDC
- Digital Currency
- Compliance
- Regulatory Reporting
- Fintech
- Payments
website: https://emtech.com
---
