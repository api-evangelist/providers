---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://brighthealthplan.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.neuehealth.com/bhc/brighthealthcare — a different registrable domain (brighthealthplan.com -> neuehealth.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bright-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brighthealthplan.com/
coverage:
  checked: '2026-08-10'
  detail: Bright HealthCare shut down all health-plan operations effective 2024-12-31 and brighthealthplan.com now 301s to a NeueHealth runout notice; the old www.brighthealthplan.com host 301s to www.brighthealthcare.com, which returns HTTP 530 with no origin behind it, and the successor NeueHealth site publishes no developer, API or interoperability page at all.
  evidence:
  - status: 530
    url: https://www.brighthealthplan.com/
  - status: 200
    url: https://brighthealthplan.com/
  - status: 404
    url: https://www.neuehealth.com/developers
  - status: 404
    url: https://www.neuehealth.com/interoperability
  - status: 404
    url: https://www.neuehealth.com/.well-known/api-catalog
  - status: 404
    url: https://api.github.com/orgs/brighthealth
  reason: defunct
  state: none
created: '2026-07-17'
description: Bright Health Group was a Minneapolis-based healthtech and health-insurance company founded in 2016 by former UnitedHealthcare CEO Bob Sheehy, offering individual, family, and Medicare Advantage plans on the ACA exchanges through its Bright HealthCare brand. Backed by Redpoint Ventures and other venture investors, the company went public in 2021, then exited the insurance business, rebranded to NeueHealth in January 2024 to focus on value-based care delivery (NeueCare) and provider enablement (NeueSolutions), and shut down all remaining Bright HealthCare health-plan operations effective December 31, 2024. NeueHealth was subsequently taken private by New Enterprise Associates. Bright Health never published a public developer program, API, or documentation surface; runout operations are handled under the NeueHealth corporate brand.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bright-health.png
layout: provider
modified: '2026-08-10'
name: Bright Health
nav: Providers
network: true
overview: Bright Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Health Insurance, Insurance, and Medicare Advantage.
random_paper: 13
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 3
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
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bright-health/refs/heads/main/screenshots/bright-health-2026-07-25T203825.png
security:
- kind: domain-security
  name: Bright Health Domain Security
  slug: bright-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bright-health
tags:
- Company
- Health Tech
- Health Insurance
- Insurance
- Medicare Advantage
- ACA
- Value-Based Care
- Defunct Brand
website: https://brighthealthplan.com/
---
