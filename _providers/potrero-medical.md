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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/potrero-medical-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/potrero-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accuryn.com/
- group: company
  title: ''
  type: About
  url: https://accuryn.com/company/
- group: other
  title: ''
  type: Product
  url: https://accuryn.com/product/
- group: company
  title: ''
  type: Blog
  url: https://accuryn.com/knowledgehub/
- group: company
  title: ''
  type: BlogRSS
  url: https://accuryn.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://accuryn.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accuryn.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/potrero-medical/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@accurynmedical8399/
coverage:
  checked: '2026-08-26'
  detail: Potrero Medical (now Accuryn Medical) ships a regulated hardware monitor whose data reaches the EMR through third-party Capsule medical device integration, and its entire web presence is a WordPress marketing site — accuryn.com/openapi.json and every /.well-known/ path return 404, api./docs./developer.accuryn.com do not resolve, and GitHub, npm and PyPI hold no first-party code.
  evidence:
  - status: 404
    url: https://accuryn.com/openapi.json
  - status: 404
    url: https://accuryn.com/.well-known/api-catalog
  - status: 404
    url: https://accuryn.com/.well-known/agent-card.json
  - status: 200
    url: https://potreromed.com/
  - status: 0
    url: https://api.accuryn.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Potrero Medical — which completed a restructuring and now operates as Accuryn Medical — is a Hayward, California predictive-health medical device company founded in 2012. Its FDA-cleared Accuryn Monitoring System turns a Foley catheter into a critical-care sensor, automatically measuring urine output, intra-abdominal pressure and core body temperature so clinicians can detect acute kidney injury, sepsis and abdominal compartment syndrome earlier while reducing CAUTI risk. The monitor reaches the EMR through Capsule medical device integration rather than a first-party developer API: as of August 2026 the company publishes no public API, SDK, developer portal or machine-readable contract of any kind, and its only web surface is a WordPress marketing site at accuryn.com.'
layout: provider
modified: '2026-08-26'
name: Potrero Medical
nav: Providers
network: true
overview: 'Potrero Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Patient Monitoring, and Critical Care.


  Potrero Medical''s developer surface includes engineering blog, support, YouTube channel, and 8 more developer resources.'
plans:
- name: Potrero Medical Plans Pricing
  plan_count: 0
  slug: potrero-medical-plans-pricing
random_paper: 10
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/potrero-medical/refs/heads/main/screenshots/potrero-medical-2026-09-02T151831.png
security:
- kind: domain-security
  name: Potrero Medical Domain Security
  slug: potrero-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: potrero-medical
tags:
- Company
- Medical Devices
- Healthcare
- Patient Monitoring
- Critical Care
- Medical Device Integration
- Predictive Health
website: https://accuryn.com/
---
