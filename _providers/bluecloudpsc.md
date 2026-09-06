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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluecloudpsc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluecloudpsc.com
created: '2026-07-17'
description: Blue Cloud Pediatric Surgery Centers operates accredited ambulatory surgery centers specializing in pediatric and special-needs dental and oral surgery care delivered under general anesthesia. Positioning itself as the largest pediatric surgery center company in the United States, Blue Cloud partners with dentists and payors across multiple U.S. locations with a mission to expand access to care, exemplify safety and quality, and reduce costs to patients and payors. Headquartered in The Woodlands, Texas, the company is a portfolio company of Norwest Venture Partners. Blue Cloud is a healthcare services provider and does not publish any public developer API, SDK, or documentation surface; this profile is maintained for network identity and demand-side coverage.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bluecloudpsc.png
layout: provider
modified: '2026-07-18'
name: Blue Cloud Pediatric Surgery Centers
nav: Providers
network: true
overview: Blue Cloud Pediatric Surgery Centers is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Pediatric, Dental, and Oral Surgery.
random_paper: 4
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluecloudpsc/refs/heads/main/screenshots/bluecloudpsc-2026-07-25T203443.png
security:
- kind: domain-security
  name: Bluecloudpsc Domain Security
  slug: bluecloudpsc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluecloudpsc
tags:
- Company
- Healthcare
- Pediatric
- Dental
- Oral Surgery
- Ambulatory Surgery Center
- Anesthesia
website: https://bluecloudpsc.com
---
