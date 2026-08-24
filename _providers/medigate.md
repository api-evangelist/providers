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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'Customer-facing REST API for the Medigate (now Claroty xDome for Healthcare) device-security platform. Documents two versions — V1 (HTTP basic auth) and V2 (API token) — used to pull the Device List, '
  name: Medigate API
  slug: medigate-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://claroty.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.medigate.io/docs
- group: auth
  title: ''
  type: Authentication
  url: authentication/medigate-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medigate-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medigate-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/medigate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://web-assets.claroty.com/team82-disclosure-policy.pdf
- group: auth
  title: ''
  type: TrustCenter
  url: security/medigate-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://claroty.com/trust
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claroty.com/privacy-policy
created: '2026-07-17'
description: Medigate was a healthcare IoT / connected-medical-device cybersecurity company (headquartered in Brooklyn, NY, backed by Partech and others) that built the first security platform dedicated to healthcare IoT — device discovery, risk assessment, and clinically-aware network segmentation for hospitals. Claroty completed its acquisition of Medigate on 2022-01-10 and folded the product into "Claroty xDome for Healthcare"; the standalone brand is retired and medigate.io now redirects to claroty.com. A residual customer-facing REST API remains live at api.medigate.io (with a password-gated interactive reference at api.medigate.io/docs) that integrations use to pull device inventory, device groups, and device risk scores.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medigate.png
layout: provider
modified: '2026-07-20'
name: Medigate
nav: Providers
network: true
overview: 'Medigate publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure Saas, Cybersecurity, Healthcare, and Medical Devices.


  Medigate''s developer surface includes API reference, authentication, and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 18.8
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 33.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medigate/refs/heads/main/screenshots/medigate-2026-08-07T172351.png
security:
- kind: authentication
  name: Medigate Authentication
  slug: medigate-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Medigate Domain Security
  slug: medigate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Medigate Vulnerability Disclosure
  slug: medigate-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Medigate Trust Center
  slug: medigate-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, CSA STAR
slug: medigate
tags:
- Company
- Infrastructure Saas
- Cybersecurity
- Healthcare
- Medical Devices
- Internet of Things
- Device Security
- Network Security
website: https://claroty.com/
---
