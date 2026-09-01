---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.exo.inc/
- group: docs
  title: ''
  type: Documentation
  url: https://support.exo.inc/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://support.exo.inc/hc/en-us/sections/22799151240603-Sign-In
- group: operate
  title: ''
  type: Support
  url: https://www.exo.inc/contact
- group: company
  title: ''
  type: Blog
  url: https://www.exo.inc/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exo-imaging
- group: commercial
  title: ''
  type: Pricing
  url: https://store.exo.inc/
- group: start
  title: ''
  type: Login
  url: https://cloud.exoworks.inc/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://store.exo.inc/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exo.inc/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.exo.inc/security-trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.exo.inc/security-trust-center/security
- group: other
  title: ''
  type: Investments
  url: https://www.exo.inc/investors
- group: company
  title: ''
  type: Careers
  url: https://www.exo.inc/careers
- group: auth
  title: ''
  type: Authentication
  url: authentication/exo-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/exo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/exo-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/exo-plans.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exo-llms.txt
- group: other
  title: ''
  type: EventCatalog
  url: events/exo-iris-activity-events.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/exo-trust-center.yml
created: '2026-08-04'
description: Exo (Exo Imaging, Inc.) is a Santa Clara, California medical imaging company building a handheld ultrasound ecosystem for point-of-care ultrasound (POCUS). Its silicon-based Exo Iris handheld probe pairs an FDA-cleared, on-device AI suite (SweepAI, cardiac and lung assessment, hemodynamics indicators) with Exo Works, an AWS-hosted POCUS workflow, documentation, billing, QA and credentialing platform. Exo Works is device-agnostic and connects to hospital systems over DICOM (modality worklist, PACS/VNA) and HL7 (ADT, ultrasound orders, exam results), with SAML single sign-on and Active Directory. Exo publishes no public developer API, OpenAPI, SDK or developer portal; its integration surface is the DICOM/HL7 interface engine documented for hospital IT, and its production API host (api.prod.exoworks.inc) is private to the Exo Works clients.
image: https://images.ctfassets.net/f1onadsih6xk/2h0Ji7EHg7lS6RQLWyECpx/ddb89eb356079629033488b6424535ed/home-resized.png
layout: provider
modified: '2026-08-04'
name: Exo
nav: Providers
network: true
overview: 'Exo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Medical Imaging, and Ultrasound.


  Exo''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, authentication, changelog, and 16 more developer resources.'
plans:
- name: Exo Plans
  plan_count: 11
  slug: exo-plans
random_paper: 17
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 37.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exo/refs/heads/main/screenshots/exo-2026-08-07T165307.png
security:
- kind: authentication
  name: Exo Authentication
  slug: exo-authentication
  summary_line: saml/ldap/password/mfa/biometric · 5 schemes
- kind: domain-security
  name: Exo Domain Security
  slug: exo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Exo Trust Center
  slug: exo-trust-center
  summary_line: HITRUST, SOC 2 Type II, ISO 27001, ISO 27701, HIPAA, GDPR
slug: exo
tags:
- Company
- Health
- Healthcare
- Medical Imaging
- Ultrasound
- Point of Care
- Artificial Intelligence
- Medical Devices
- DICOM
- HL7
website: https://www.exo.inc/
---
