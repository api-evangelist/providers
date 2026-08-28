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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: HSDP is Philips' cloud platform for building connected health applications. It packages a suite of building-block services - including Identity and Access Management, Provisioning, IoT/Connect for dev
  name: Philips HealthSuite Digital Platform (HSDP)
  slug: hsdp
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/philips-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/philips-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/philips-software
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/philips
- group: company
  title: ''
  type: Website
  url: https://www.philips.com/
- group: company
  title: ''
  type: HealthcareWebsite
  url: https://www.usa.philips.com/healthcare
- group: start
  title: ''
  type: HSDPPortal
  url: https://www.hsdp.io/
- group: operate
  title: ''
  type: HSDPStatus
  url: https://status.hsdp.io/
created: '2026-05-05'
description: A Dutch multinational health technology company focused on diagnostic imaging, patient monitoring, image-guided therapy, ultrasound, sleep and respiratory care, and connected care solutions. Philips transitioned from a diversified electronics conglomerate to a dedicated healthcare technology leader and operates the HealthSuite Digital Platform (HSDP) as its cloud-based platform for connected health applications. HSDP exposes Identity & Access Management, Provisioning, IoT/Connect, Foundation, Cognitive, Clinical Data, and Notification building blocks to enable consumer health and professional healthcare applications, but access is gated behind a customer portal at www.hsdp.io with developer documentation distributed to authenticated customers and partners rather than the open public web. Philips also operates vertical Connected Care offerings (Patient Monitoring, eICU/Capsule, Sleep & Respiratory Care/SimplyGo, IntelliSpace) layered on HSDP. The legacy Philips Hue lighting API
  is no longer a Philips offering - Hue has been spun off into Signify and is published at developers.meethue.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/philips.png
layout: provider
modified: '2026-05-09'
name: Philips
nav: Providers
network: true
overview: Philips publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Medical Devices, Connected Care, Patient Monitoring, and HealthSuite.
random_paper: 5
score:
  band: minimal
  composite: 8.7
  delta: 2.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 6.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/philips/refs/heads/main/screenshots/philips-2026-06-20T191638.png
security:
- kind: domain-security
  name: Philips Domain Security
  slug: philips-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Philips Vulnerability Disclosure
  slug: philips-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: philips
tags:
- Healthcare
- Medical Devices
- Connected Care
- Patient Monitoring
- HealthSuite
- HSDP
- Imaging
- IoT
- Cloud Platform
website: https://www.philips.com/
---
