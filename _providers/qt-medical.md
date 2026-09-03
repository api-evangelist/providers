---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.qtmedical.com/en
- group: operate
  title: ''
  type: Support
  url: https://www.qtmedical.com/en/contact
- group: docs
  title: ''
  type: Documentation
  url: https://www.qtmedical.com/en/downloads
- group: company
  title: ''
  type: Blog
  url: https://www.qtmedical.com/en/page-categories/blog
- group: start
  title: ''
  type: Login
  url: https://dashboard.qtmedical.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qtmedical.com/en/term
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qtmedical.com/en/privacy
- group: auth
  title: ''
  type: Compliance
  url: conformance/qt-medical-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qt-medical-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qt-medical-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/qt-medical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qt-medical-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qt-medical-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: QT Medical advertises "API available for EMR integration*** (Extra fee)" on its own PCA 500 page and an ADK for telehealth partners on its telehealth applications page, but ships no developer portal, no API reference and no machine-readable contract — both are obtained only by contacting sales@qtmedical.com, and the documented default EMR path is a manually uploaded PDF report.
  evidence:
  - status: 200
    url: https://qtmedical.com/en-gb/PCA_500
  - status: 200
    url: https://www.qtmedical.com/en/applications/others
  - status: 404
    url: https://dashboard.qtmedical.com/openapi.json
  - status: 404
    url: https://www.qtmedical.com/.well-known/agent-card.json
  - status: 404
    url: https://www.qtmedical.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: QT Medical, Inc. is a Diamond Bar, California medical device company building the PCA 500, an FDA-cleared, hospital-quality wireless 12-lead electrocardiogram (ECG) recorder for professional and personal use, paired with the patented QHeart prepositioned electrode sensor, QT ECG mobile and Windows applications, and a HIPAA- and GDPR-compliant cloud (the QTM Dashboard) where recorded ECGs are stored, reviewed and shared. The PCA 500 carries 510(k) clearances for adult, pediatric and acute-care use and additional clearances from CE, Japan PMDA, Australia TGA and Health Canada. QT Medical advertises an API for EMR integration and an ADK for telehealth partners embedding ECG capture in their own mobile applications, but publishes no developer portal, no API reference and no machine-readable contract; both are obtained through its sales team.
image: https://www.qtmedical.com/frontend/images/logo.png
layout: provider
modified: '2026-08-26'
name: QT Medical
nav: Providers
network: true
overview: 'QT Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Medical Devices, and ECG.


  QT Medical''s developer surface includes support, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Qt Medical Plans Pricing
  plan_count: 0
  slug: qt-medical-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Qt Medical Rate Limits
  slug: qt-medical-rate-limits
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qt-medical/refs/heads/main/screenshots/qt-medical-2026-09-02T152546.png
security:
- kind: domain-security
  name: Qt Medical Domain Security
  slug: qt-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qt-medical
tags:
- Company
- Health
- Healthcare
- Medical Devices
- ECG
- Cardiology
- Remote Patient Monitoring
- Telehealth
- HIPAA
- Digital Health
website: https://www.qtmedical.com/en
---
