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
  url: security/openeyes-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openeyes.com/
- group: company
  title: ''
  type: Blog
  url: https://openeyes.com/blog/
- group: start
  title: ''
  type: Login
  url: https://dashboard.openeyes.com/
created: '2026-07-17'
description: OpenEyes Insurance (OpenEyes Insurance Agency, Inc.) is an Austin, Texas-based insurtech startup, with an additional New York office, that provides commercial auto insurance for truck and bus fleet operators bundled with proprietary risk-prevention technology. Its offering pairs fleet coverage with real-time driver monitoring, AI dashcams, safety analytics, customized driver training, and 24/7 claims management, serving both insurance agents (For Agents) and fleet operators directly (For Fleets). Founded by Yoav Oron (CEO), Dr. Omry Sendik (CTO), and Dan Charash (Chairman), OpenEyes emerged from stealth in February 2023 with a $23M Series A led by Insight Partners with Pitango First. The company operates a customer-facing fleet dashboard but does not publish a public developer API, portal, or documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openeyes-insurance.png
layout: provider
modified: '2026-07-20'
name: OpenEyes Insurance
nav: Providers
network: true
overview: 'OpenEyes Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Commercial Auto Insurance, and Fleet Management.


  OpenEyes Insurance''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openeyes-insurance/refs/heads/main/screenshots/openeyes-insurance-2026-08-07T190602.png
security:
- kind: domain-security
  name: Openeyes Insurance Domain Security
  slug: openeyes-insurance-domain-security
  summary_line: TLSv1.3
slug: openeyes-insurance
tags:
- Company
- Insurance
- Insurtech
- Commercial Auto Insurance
- Fleet Management
- Telematics
- Risk Management
website: https://openeyes.com/
---
