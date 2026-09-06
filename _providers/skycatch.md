---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://skycatch.com'', ''status'': 308, ''note'': ''declared website redirects to https://rpmglobal.com/caterpillar-expands-mining-technology-capabilities-with-skycatch-acquisition/ — a different registrable domain (skycatch.com -> rpmglobal.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skycatch-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skycatch.com
- group: start
  title: ''
  type: Login
  url: https://datahub.skycatch.com
- group: company
  title: ''
  type: Website
  url: http://skycatch.com
created: '2026-07-17'
description: Skycatch built spatial data capture, processing, and analytics for mining and construction sites, turning drone and aerial imagery into high-precision 3D data, volumetrics, and AI-driven site insights. Its products included Spatial Sight, Spatial DataHub (datahub.skycatch.com), and EdgeServer for on-site edge processing. Skycatch was acquired by Caterpillar Inc. on July 7, 2026 (following Caterpillar's RPMGlobal acquisition) to expand its mining technology capabilities. A developer platform exists at docs.skycatch.com but is password-gated, and no public API specification is available. Originally surfaced as a GV (Google Ventures) portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skycatch.png
layout: provider
modified: '2026-07-21'
name: Skycatch
nav: Providers
network: true
overview: 'Skycatch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Drones, Aerial Imagery, and Geospatial.


  Skycatch''s developer surface includes documentation and 3 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skycatch/refs/heads/main/screenshots/skycatch-2026-09-02T155753.png
security:
- kind: domain-security
  name: Skycatch Domain Security
  slug: skycatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skycatch
tags:
- Company
- Frontier Tech
- Drones
- Aerial Imagery
- Geospatial
- 3D Mapping
- Mining
- Construction
- Photogrammetry
- Analytics
website: http://skycatch.com
---
