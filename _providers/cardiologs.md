---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://cardiologs.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.philips.co.uk:443/healthcare/ambulatory-monitoring-and-diagnostics/ecg-monitoring/cardiologs-ecg-analysis — a different registrable domain (cardiologs.com -> philips.co.uk), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/philips/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardiologs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardiologs.com/
created: '2026-07-17'
description: Cardiologs is a cloud-based ECG analysis platform that uses clinically validated artificial intelligence to streamline cardiac diagnostics, helping clinicians and healthcare providers reduce the burden of manual ECG interpretation while improving diagnostic scalability and accessibility. Founded in Paris in 2014, Cardiologs was acquired by Philips in 2021 and is now offered as part of Philips ambulatory monitoring and diagnostics (ECG monitoring) portfolio. The company publishes no public developer API, SDK, or developer portal; its primary domain redirects to the Philips healthcare product page.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cardiologs.png
layout: provider
modified: '2026-07-18'
name: Cardiologs
nav: Providers
network: true
overview: Cardiologs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, ECG, Cardiac Diagnostics, and Artificial Intelligence.
random_paper: 13
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cardiologs/refs/heads/main/screenshots/cardiologs-2026-07-25T204519.png
security:
- kind: domain-security
  name: Cardiologs Domain Security
  slug: cardiologs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cardiologs
tags:
- Company
- Healthcare
- ECG
- Cardiac Diagnostics
- Artificial Intelligence
- Medical Devices
- Cardiology
- Philips
website: https://cardiologs.com/
---
