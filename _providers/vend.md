---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.vendhq.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.lightspeedhq.com/vend/ — a different registrable domain (vendhq.com -> lightspeedhq.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.vendhq.com
- group: docs
  title: ''
  type: Documentation
  url: https://x-series-api.lightspeedhq.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vend-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vend-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vend-domain-security.yml
created: '2026-07-17'
description: Vend was a cloud-based retail point-of-sale and inventory management software company founded in Auckland, New Zealand, backed by investors including Point Nine. Lightspeed announced its acquisition of Vend in March 2021 for approximately US$350 million, and the product lives on as Lightspeed Retail (X-Series). vendhq.com redirects to lightspeedhq.com/vend/, and the former Vend API is documented today at x-series-api.lightspeedhq.com. The X-Series API surface is profiled in the API Evangelist network under the Lightspeed provider, so this profile records the acquired Vend brand rather than duplicating that API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vend.png
layout: provider
modified: '2026-07-21'
name: Vend
nav: Providers
network: true
overview: 'Vend is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Point-of-Sale, Commerce, and Inventory.


  Vend''s developer surface includes documentation and 4 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vend/refs/heads/main/screenshots/vend-2026-09-02T165632.png
security:
- kind: domain-security
  name: Vend Domain Security
  slug: vend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vend
tags:
- Company
- Retail
- Point-of-Sale
- Commerce
- Inventory
- Acquired
website: https://www.vendhq.com
---
