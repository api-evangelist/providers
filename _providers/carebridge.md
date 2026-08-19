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
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carebridge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carebridgehealth.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carebridgehealth.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.carebridgehealth.com/contact
created: '2026-07-17'
description: 'CareBridge is a home and community-based healthcare company that delivers 24/7 virtual and in-home care coordination to high-risk, largely Medicaid populations on behalf of health plans. Its interdisciplinary care teams address members'' physical, behavioral, and social health needs, and the company operates three core service lines: 24/7 member support, decision support (durable medical equipment and technology provisioning), and Electronic Visit Verification (EVV) technology used by state Medicaid programs and managed-care organizations. Headquartered in Nashville, Tennessee, CareBridge was surfaced as a portfolio company of GV. As of this enrichment pass the company publishes no public developer portal, API documentation, OpenAPI/AsyncAPI specification, SDKs, or /.well-known discovery surface; this profile therefore captures its public identity and domain-security posture only.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carebridge.png
layout: provider
modified: '2026-07-18'
name: CareBridge *
nav: Providers
network: true
overview: 'CareBridge * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Healthcare, Home Health, and Care Coordination.


  CareBridge *''s developer surface includes support and 3 more developer resources.'
random_paper: 138
score:
  band: minimal
  composite: 7.1
  delta: -1.5
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carebridge/refs/heads/main/screenshots/carebridge-2026-07-25T204527.png
security:
- kind: domain-security
  name: Carebridge Domain Security
  slug: carebridge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carebridge
tags:
- Company
- Life Sciences
- Healthcare
- Home Health
- Care Coordination
- Electronic Visit Verification
- Medicaid
- Managed Care
website: https://www.carebridgehealth.com
---
