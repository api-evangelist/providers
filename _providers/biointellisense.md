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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-03'
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
random_paper: 89
score:
  band: thin
  composite: 28.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 56.3
  schema_version: 0.9
  scored_at: '2026-08-03'
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
