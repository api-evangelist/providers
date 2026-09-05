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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The BioCloud data-as-a-service platform API that ingests continuous vital-signs telemetry from BioButton / BioSticker wearables via BioHub gateways and the BioMobile app, and serves it to BioDashboard
  name: BioIntelliSense BioCloud API
  slug: biocloud
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biointellisense-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biointellisense.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.biointellisense.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://www.biointellisense.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.biointellisense.com/category/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biointellisense.com/platform-and-product-user-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biointellisense.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.biointellisense.com/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.biointellisense.com/legal
- group: operate
  title: ''
  type: SLA
  url: https://www.biointellisense.com/service-level-agreement/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.biointellisense.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.biointellisense.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://jobs.lever.co/biointellisense
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/biointellisense_stock/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/biointellisense-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/biointellisense-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/biointellisense-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/biointellisense-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/biointellisense-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/biointellisense-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/biointellisense-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/biointellisense-llms.txt
created: '2026-08-02'
description: BioIntelliSense is a Golden, Colorado continuous health monitoring company whose FDA-cleared BioButton multi-patient wearable, BioSticker, BioHub cellular/Wi-Fi gateways, BioMobile smartphone app and BioDashboard exception-management software stream medical-grade vital signs — heart rate, respiratory rate, skin temperature, body position, activity and sleep — from in-facility acute care through post-acute and at-home remote patient monitoring. Device telemetry flows over Bluetooth to a gateway and into the BioCloud data-as-a-service platform, where analytics and clinician alerting run and where third-party and EMR/EHR integrations (HL7 into Epic and peers) consume the data. The BioCloud API host is live but entirely authentication-gated, with no publicly published developer portal, OpenAPI definition, SDKs or self-service onboarding — integration is arranged commercially under a Master Services Agreement.
image: https://www.biointellisense.com/wp-content/uploads/2025/10/512x512-300x300.png
layout: provider
modified: '2026-08-02'
name: BioIntelliSense
nav: Providers
network: true
overview: 'BioIntelliSense publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Remote Patient Monitoring, and Wearables.


  BioIntelliSense''s developer surface includes documentation, support, engineering blog, legal docs, authentication, and 17 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 28.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa-cpra
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitech
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 56.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biointellisense/refs/heads/main/screenshots/biointellisense-2026-08-07T162500.png
security:
- kind: authentication
  name: Biointellisense Authentication
  slug: biointellisense-authentication
  summary_line: unknown-bearer · 1 scheme
- kind: domain-security
  name: Biointellisense Domain Security
  slug: biointellisense-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biointellisense
tags:
- Company
- Health
- Healthcare
- Remote Patient Monitoring
- Wearables
- Medical Devices
- Vital Signs
- Continuous Monitoring
- Digital Health
- Data as a Service
website: https://www.biointellisense.com/
---
