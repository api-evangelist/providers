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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sidecar-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sidecarhealth.com
- group: company
  title: ''
  type: Blog
  url: https://sidecarhealth.com/blog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sidecarhealth.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sidecarhealth.com/legal/privacy-statements
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sidecarhealth.com/legal/terms-of-use
- group: start
  title: ''
  type: Login
  url: https://app.sidecarhealth.com/login
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sidecar-health-well-known.yml
created: '2026-07-17'
description: Sidecar Health is a health insurance company founded in 2018 by Patrick Quigley and Veronica Osetinsky and headquartered in Columbus, Ohio. It was built to bring transparency to healthcare pricing, letting members see upfront cash prices for care and share in the savings. After launching with supplemental coverage for individuals, Sidecar established its own insurance carrier in 2021 and today serves large employers with ACA-compliant major medical plans, offered both fully insured and as administrative-services-only (ASO) for self-funded employers. It covers members in 46 states across partners in 50 industries. Sidecar Health operates member, provider, broker, and employer web portals plus a mobile app, but publishes no public developer API, OpenAPI, or partner-integration documentation; this profile captures its public identity and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sidecar-health.png
layout: provider
modified: '2026-08-08'
name: Sidecar Health
nav: Providers
network: true
overview: 'Sidecar Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Insurance, Healthcare, Insurance, and Employer Benefits.


  Sidecar Health''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sidecar-health/refs/heads/main/screenshots/sidecar-health-2026-09-02T155348.png
security:
- kind: domain-security
  name: Sidecar Health Domain Security
  slug: sidecar-health-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Sidecar Health Trust Center
  slug: sidecar-health-trust-center
  summary_line: trust center published
slug: sidecar-health
tags:
- Company
- Health Insurance
- Healthcare
- Insurance
- Employer Benefits
- ACA
- Health Plans
- Price Transparency
website: https://sidecarhealth.com
---
