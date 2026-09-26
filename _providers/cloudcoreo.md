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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloudCoreo
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudcoreo/refs/heads/main/cli/cloudcoreo-cli.yml
  title: ''
  type: CLI
  url: cli/cloudcoreo-cli.yml
created: '2026-07-17'
description: 'CloudCoreo was a Seattle-based cloud security startup (founded 2016, seed round led by Madrona Venture Group) that built a cloud configuration and vulnerability-assessment platform to identify and remediate misconfigurations across public multi-cloud environments (AWS, Azure, GCP). VMware acquired CloudCoreo in February 2018 and folded the team and product into VMware Cloud Services, where it became the basis of CloudHealth Secure State. The standalone CloudCoreo service and developer surface have since been retired: cloudcoreo.com is now a parked/for-sale domain and there is no live public API. The CloudCoreo GitHub organization remains, hosting the now-deprecated first-party CLI. This profile is a historical/lineage record, not an active API provider.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudcoreo.png
layout: provider
modified: '2026-09-15'
name: Cloudcoreo
nav: Providers
network: true
overview: 'Cloudcoreo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Security, Cloud Configuration, Vulnerability Management, and Multi-Cloud.


  Cloudcoreo''s developer surface includes CLI and 1 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 2
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudcoreo/refs/heads/main/screenshots/cloudcoreo-2026-07-25T205704.png
slug: cloudcoreo
tags:
- Company
- Cloud Security
- Cloud Configuration
- Vulnerability Management
- Multi-Cloud
- DevSecOps
- Acquired
- Defunct
---
