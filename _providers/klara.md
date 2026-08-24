---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klara-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klara-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.modmed.com/what-we-do/patient-communication/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klara-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klara-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/klara-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klara-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/klara-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/klara-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/klara-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/klara-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.modmed.com/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klara
- group: company
  title: ''
  type: Website
  url: https://www.klara.com/
- group: start
  title: ''
  type: Login
  url: https://doctor.klara.com/
- group: operate
  title: ''
  type: Support
  url: https://support.klara.com/s/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.klara.com/
- group: company
  title: ''
  type: Blog
  url: https://www.modmed.com/resources/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.modmed.com/schedule-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.modmed.com/klara-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modmed.com/klara-privacy/
coverage:
  checked: '2026-08-15'
  detail: Klara has no developer site of its own — developers.klara.com, docs.klara.com and developer.klara.com do not resolve in DNS, klara.com 302s every path to the ModMed product page, and the live first-party API host api.klara.com 404s every discovery path because it is the private backend for doctor.klara.com; the only Klara integration surface published anywhere is a partner-app listing inside ModMed's synapSYS marketplace, backed by the parent's portal.api.modmed.com FHIR/EMA APIs.
  evidence:
  - status: 302
    url: https://klara.com/
  - status: 0
    url: https://developers.klara.com/
  - status: 404
    url: https://api.klara.com/openapi.json
  - status: 401
    url: https://support.klara.com/en/articles/4210809-getting-started-with-modernizing-medicine-integration
  - status: 200
    url: https://synapsys.modmed.com/s/synapsys/0TU4M0000004CCRWA2/klara
  reason: marketplace-only
  state: gated
created: '2026-07-24'
description: Klara is a US healthcare patient-engagement and communication platform, now part of Modernizing Medicine (ModMed), that gives medical practices two-way secure messaging, patient texting, appointment reminders and scheduling, intake and forms, telemedicine, and automated workflow tools to reduce phone volume and staff workload. Klara markets integration with 50+ EHR and practice-management systems, but it does not publish its own self-serve public developer API, FHIR CapabilityStatement, or downloadable OpenAPI. Its parent, ModMed, operates a partner-gated developer program at portal.api.modmed.com covering an ONC-certified HL7 FHIR R4 API with SMART-on-FHIR (built for the 21st Century Cures Act, US Core, OAuth2, bulk NDJSON export) plus a proprietary FHIR API for the EMA and gGastro EHR/PM platforms and a Synapsys App Marketplace. That certified API surface belongs to ModMed's EHR products, not to the Klara messaging product itself. Home market is the United States.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-15'
name: Klara
nav: Providers
network: true
overview: 'Klara is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Patient Engagement, Patient Communication, and Secure Messaging.


  Klara''s developer surface includes support, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Klara Plans Pricing
  plan_count: 0
  slug: klara-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Klara Rate Limits
  slug: klara-rate-limits
score:
  band: thin
  composite: 26.6
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 26.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klara/refs/heads/main/screenshots/klara-2026-07-25T223943.png
security:
- kind: domain-security
  name: Klara Domain Security
  slug: klara-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Klara Vulnerability Disclosure
  slug: klara-vulnerability-disclosure
  summary_line: disclosure policy published
slug: klara
tags:
- Healthcare
- United States
- Patient Engagement
- Patient Communication
- Secure Messaging
- Telehealth
- Scheduling
- EHR Integration
website: https://www.klara.com/
---
