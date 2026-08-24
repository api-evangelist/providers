---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: 'Cloud-to-cloud API that connects Empatica Health Monitoring Platform data to a sponsor''s or CRO''s own clinical trial systems in real time. Documented capabilities: participant onboarding from external'
  name: Empatica Cloud API
  slug: empatica-cloud-api
- description: 'Live REST host observed at https://api.empatica.com/v2/ that backs Empatica''s mobile apps and web portals. Probed anonymously on 2026-08-12: POST /v2/login answers a JSON error envelope, GET /v2/users'
  name: Empatica Platform API (api.empatica.com)
  slug: empatica-platform-api
- description: The primary programmatic data interface for the Empatica Health Monitoring Platform. High-frequency raw data from EmbracePlus is uploaded to the Empatica Cloud every 30 minutes and made available in a
  name: Empatica Cloud Data Access (S3)
  slug: empatica-cloud-data-access
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/empatica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.empatica.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.empatica.com/manuals/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.empatica.com/hc/en-us/articles/13796731471261-Basic-steps-to-start-data-collection
- group: operate
  title: ''
  type: Support
  url: https://support.empatica.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.empatica.com/submitrequest/
- group: company
  title: ''
  type: Blog
  url: https://www.empatica.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/empatica
- group: commercial
  title: ''
  type: Pricing
  url: https://www.empatica.com/store/platform-professional/
- group: start
  title: ''
  type: Login
  url: https://care.empatica.com/login
- group: start
  title: ''
  type: SignUp
  url: https://www.empatica.com/start-care/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.empatica.com/purchase-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.empatica.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.empatica.com/legal/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.empatica.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.empatica.com/research/e4-sunset/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/empatica-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/empatica-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/empatica-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/empatica-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/empatica-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/empatica-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/empatica-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/empatica-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/empatica-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/empatica-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/empatica-rate-limits.yml
created: '2026-08-12'
description: 'Empatica Inc. is an MIT Media Lab spinoff, founded in Cambridge, Massachusetts, that builds FDA-cleared medical wearables — EmbracePlus, EmbraceMini and the EpiMonitor epilepsy monitoring system — together with the Empatica Health Monitoring Platform, a cloud platform for continuous, remote physiological data collection in clinical research and patient monitoring. The platform captures raw sensor streams (PPG/blood volume pulse, electrodermal activity, skin temperature, accelerometer, gyroscope, steps, systolic peaks, participant tags) and derives 300+ digital measures used as digital endpoints by pharmaceutical sponsors and CROs. Programmatic access is delivered three ways: a cloud-to-cloud Cloud API that pushes participant management, wearing compliance and digital biomarker data into a sponsor''s CTMS/EDC; an AWS S3 data bucket addressed with Care Portal-issued Data Access Keys, where high-frequency raw data lands every 30 minutes as Apache Avro files; and a live REST host
  at api.empatica.com backing Empatica''s own apps and portals. The Cloud API reference is issued only to contracted clients, so no OpenAPI, AsyncAPI or public API reference is published.'
image: https://cdn.sanity.io/images/ggwhkgro/production/672c80e64ce4b99e66a90a38c82364a4e5674f68-3600x1155.png
layout: provider
modified: '2026-08-12'
name: Empatica
nav: Providers
network: true
overview: 'Empatica publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Wearables, and Medical Devices.


  Empatica''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Empatica Plans Pricing
  plan_count: 6
  slug: empatica-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Empatica Rate Limits
  slug: empatica-rate-limits
score:
  band: developing
  composite: 40.0
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 40.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Empatica Authentication
  slug: empatica-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Empatica Domain Security
  slug: empatica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Empatica Vulnerability Disclosure
  slug: empatica-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Empatica Trust Center
  slug: empatica-trust-center
  summary_line: UNI CEI EN ISO 13485:2021, ISO/IEC 27001:2022, MDSAP, CE marking under EU MDR 2017/745, FDA 510(k) clearances, TGA ARTG listings (Australia), Health Canada Medical Device Licences
slug: empatica
tags:
- Company
- Healthcare
- Digital Health
- Wearables
- Medical Devices
- Clinical Trials
- Remote Patient Monitoring
- Digital Biomarkers
- Life Sciences
- Sensor Data
website: https://www.empatica.com/
---
