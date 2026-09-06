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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/satellite-bio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/satellite-bio-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/satellite-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://satellite.bio/
- group: company
  title: ''
  type: Careers
  url: https://satellite.bio/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/satellite-bio/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/satellite-bio-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/satellite-bio-well-known.yml
created: '2026-07-17'
description: Satellite Bio is a biotechnology company developing off-the-shelf liver cell therapies to treat severe and life-threatening liver diseases. Its tissue therapeutics platform engineers functional hepatocytes designed to engraft and restore liver function, combining the biological power of liver cells with scalable manufacturing and distribution. The company is headquartered in Newton, Massachusetts and is backed by Lightspeed Venture Partners. Satellite Bio is a life-sciences company and does not currently publish a public developer platform, API, or technical integration surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/satellite-bio.png
layout: provider
modified: '2026-07-21'
name: Satellite Bio
nav: Providers
network: true
overview: Satellite Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Tissue Therapeutics.
random_paper: 3
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/satellite-bio/refs/heads/main/screenshots/satellite-bio-2026-09-02T154423.png
security:
- kind: domain-security
  name: Satellite Bio Domain Security
  slug: satellite-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Satellite Bio Vulnerability Disclosure
  slug: satellite-bio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: satellite-bio
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Therapy
- Tissue Therapeutics
- Liver Disease
- Regenerative Medicine
- Pharmaceuticals
website: https://satellite.bio/
---
