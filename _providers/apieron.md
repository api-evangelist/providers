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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: Acquirer
  url: https://www.niox.com/
created: '2026-07-17'
description: Apieron Inc. was a private, venture-backed medical device company headquartered in Menlo Park, California, formed in early 2001 to develop a simple-to-use, non-invasive monitor for the measurement of exhaled nitric oxide (eNO) as an aid in the management of asthma. Its patented biosensor platform enabled highly sensitive detection of selected analytes, and its Insight eNO System received U.S. Food and Drug Administration clearance and launched in the United States in 2008. Following that launch Aerocrine filed patent-infringement complaints against Apieron and Apieron counterclaimed; citing the legal setbacks and a lack of financing, Apieron filed a Chapter 7 bankruptcy petition in the U.S. Bankruptcy Court for the Northern District of California on 30 March 2010. At a court auction on 12 May 2010 Aerocrine acquired all of Apieron's business assets, including its patent and trademark portfolio, ending the litigation; the Insight product was discontinued and not returned to supply.
  Apieron was a clinical-hardware company and never published a public API, developer portal, SDK, or machine-readable interface. This profile is retained as a historical record of the Canaan Partners portfolio and is not an active API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apieron.png
layout: provider
modified: '2026-09-15'
name: Apieron
nav: Providers
network: true
overview: Apieron is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Respiratory, and Asthma.
random_paper: 2
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/apieron/refs/heads/main/screenshots/apieron-2026-07-25T200623.png
slug: apieron
tags:
- Company
- Medical Devices
- Healthcare
- Respiratory
- Asthma
- Diagnostics
- Biosensors
- Acquired
- Historical
- Defunct
---
