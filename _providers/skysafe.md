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
- group: company
  title: ''
  type: Website
  url: https://www.skysafe.io/
- group: start
  title: ''
  type: Login
  url: https://app.skysafe.io
- group: company
  title: ''
  type: Blog
  url: https://blog.skysafe.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skysafe
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skysafe.io/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skysafe-domain-security.yml
created: '2026-07-17'
description: SkySafe is a San Diego-based drone-detection and airspace-intelligence company (founded 2015, backed by a16z) whose cloud SaaS platform lets airports, critical infrastructure, law enforcement, universities, correctional facilities, and government customers detect, track, analyze, and act on every drone in their airspace in real time. The platform surfaces precise drone location, altitude, velocity, flight status, launch point, and pilot location, receives and analyzes Remote ID, retains historical flight telemetry for forensic "Prosecutor-Ready" reporting, and pushes instant notifications via SMS, Microsoft Teams, Slack, or CommandCentral Aware. SkySafe advertises integration APIs that push detection, forensics, and analytics into third-party command centers and mitigation workflows, but its developer surface (app.skysafe.io, docs.skysafe.io, api.skysafe.io) sits entirely behind customer authentication — there is no public developer portal, API reference, or OpenAPI specification
  to harvest.
image: https://framerusercontent.com/assets/hFauWGviPo27ihfi7neacjU9qkE.png
layout: provider
modified: '2026-07-21'
name: SkySafe
nav: Providers
network: true
overview: 'SkySafe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drone Detection, Counter-UAS, Airspace Intelligence, and Security.


  SkySafe''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skysafe/refs/heads/main/screenshots/skysafe-2026-09-02T155816.png
security:
- kind: domain-security
  name: Skysafe Domain Security
  slug: skysafe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skysafe
tags:
- Company
- Drone Detection
- Counter-UAS
- Airspace Intelligence
- Security
- Public Safety
- Remote ID
- Signals Intelligence
website: https://www.skysafe.io/
---
