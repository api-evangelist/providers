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
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exelis-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exelis
- group: company
  title: ''
  type: Website
  url: https://www.l3harris.com
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Exelis_Inc.
coverage:
  checked: '2026-09-07'
  detail: Exelis Inc. ceased to exist as a company when Harris Corporation acquired it in 2015 and folded it into L3Harris in 2019; exelis.com now answers only an unconfigured OVHcloud "Site not installed" 404 page that L3Harris does not operate, exelisvis.com no longer resolves at all, and exelisinc.com resolves but refuses connections, so there is no Exelis-brand host left on which an API could be published.
  evidence:
  - status: 404
    url: https://exelis.com/
  - status: 404
    url: https://exelis.com/.well-known/security.txt
  - status: 404
    url: https://exelis.com/apis.json
  - status: 404
    url: https://www.l3harris.com/.well-known/api-catalog
  reason: defunct
  state: none
created: '2026-03-24'
description: Exelis Inc. was an American global aerospace, defense, information, and services company that produced communications systems, electronic warfare products, geospatial systems, integrated structures, and night vision equipment. Headquartered in McLean, Virginia, Exelis was acquired by Harris Corporation in 2015. Harris and L3 Technologies then merged in 2019 to form L3Harris Technologies. No public APIs are published under the Exelis brand; developer resources, if any, are tracked under L3Harris.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exelis.png
layout: provider
modified: '2026-09-07'
name: Exelis
nav: Providers
network: true
overview: Exelis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aerospace, Defense, Acquired, L3Harris, and Electronic Warfare.
press:
- date: '2026-05-25'
  title: Generative Artificial Intelligence in the DoD Acquisition ...
  url: https://acqirc.org/events/generative-artificial-intelligence-in-the-dod-acquisition-lifecycle/
- date: '2026-05-25'
  title: News & Announcements
  url: https://saalex.com/news-announcements/
- date: '2026-05-25'
  title: SparkCognition Government Systems Appoints Lieutenant ...
  url: https://www.prnewswire.com/news-releases/sparkcognition-government-systems-appoints-lieutenant-general-ken-hunzeker-ret-to-board-of-directors-301518687.html
- date: '2026-05-25'
  title: Harris completes $4.75 billion acquisition of Exelis
  url: https://rbj.net/2015/05/29/harris-completes-4-75-billion-acquisition-of-exelis/
- date: '2026-05-25'
  title: SAIC
  url: https://www.govconwire.com/s/company/saic/page/770
random_paper: 20
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
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
  previous_composite: 3.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/exelis/refs/heads/main/screenshots/exelis-2026-06-20T180930.png
security:
- kind: domain-security
  name: Exelis Domain Security
  slug: exelis-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: exelis
tags:
- Aerospace
- Defense
- Acquired
- L3Harris
- Electronic Warfare
- Geospatial
- Night Vision
- Government
- Defunct
website: https://www.l3harris.com
---
