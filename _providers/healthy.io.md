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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthy.io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://healthy.io/
- group: company
  title: ''
  type: About
  url: https://healthy.io/about-us/
- group: operate
  title: ''
  type: Support
  url: https://healthy.io/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HealthyIO
- group: commercial
  title: ''
  type: TermsOfService
  url: https://healthy.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://healthy.io/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://healthy.io/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://healthy.io/trust-center/compliance/certifications
- group: auth
  title: ''
  type: Security
  url: https://healthy.io/trust-center/security/reporting-suspected-vulnerabilities
- group: company
  title: ''
  type: Careers
  url: https://healthy.io/careers/
- group: other
  title: ''
  type: Patents
  url: https://healthy.io/patents/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/healthy.io-stock
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/healthy.io-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/healthy.io-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/healthy.io-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/healthy.io-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/healthy.io-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthy.io-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Healthy.io runs a documentation host and a status host, but both docs.healthy.io and status.healthy.io 302-redirect every path to a healthyio.cloudflareaccess.com SSO login, so the EMR/SMART-on-FHIR integration surface the homepage advertises cannot be read, parsed or evaluated by anyone without a Healthy.io identity.
  evidence:
  - status: 302
    url: https://docs.healthy.io/
  - status: 302
    url: https://status.healthy.io/
  - status: 404
    url: https://healthy.io/.well-known/smart-configuration
  - status: 404
    url: https://healthy.io/developers
  reason: partner-login
  state: gated
created: '2026-08-22'
description: Healthy.io is a digital-health company that turns an ordinary smartphone camera into a clinical-grade measurement device, using colorimetric analysis, computer vision and machine learning trained on more than a million tagged color-spectrum images. Its Minuteful product line covers home urinalysis for chronic kidney disease (Minuteful Kidney, FDA 510(k) cleared and CE marked), urinary tract infection testing (Minuteful UTI), a ten-parameter urinalysis panel (Minuteful 10), and digitized chronic wound assessment (Minuteful for Wound). The company sells to health systems, provider groups and payers - including Medicare Advantage and nonprofit health plans - rather than to developers, and states that its technology integrates into most EMRs via SMART on FHIR. Healthy.io operates from Boston, London and Tel Aviv, and publishes a detailed public trust center covering security, privacy, availability and compliance, including a coordinated vulnerability disclosure policy.
image: https://www.datocms-assets.com/38808/1614769561-homepage-thumbnail-min.jpg
layout: provider
modified: '2026-08-22'
name: Healthy.io
nav: Providers
network: true
overview: 'Healthy.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Medical Devices.


  Healthy.io''s developer surface includes support and 18 more developer resources.'
plans:
- name: Healthy.Io Plans Pricing
  plan_count: 0
  slug: healthy.io-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 21.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthy.io/refs/heads/main/screenshots/healthy.io-2026-09-02T145712.png
security:
- kind: domain-security
  name: Healthy.Io Domain Security
  slug: healthy.io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Healthy.Io Vulnerability Disclosure
  slug: healthy.io-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Healthy.Io Trust Center
  slug: healthy.io-trust-center
  summary_line: ISO/IEC 27001:2013, ISO 22301:2019, ISO 13485:2016, HITRUST, UK Cyber Essentials, NHS Data Security and Protection Toolkit
slug: healthy.io
tags:
- Company
- Health
- Healthcare
- Digital Health
- Medical Devices
- Diagnostics
- Urinalysis
- Kidney Care
- Wound Care
- Computer-Vision
- Remote Patient Monitoring
- Telehealth
- SMART on FHIR
- HIPAA
website: https://healthy.io/
---
