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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cleanslate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cleanslatecenters.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cleanslate_stock/
coverage:
  checked: '2026-08-09'
  detail: 'CleanSlate is a 65-clinic outpatient addiction-treatment medical group (acquired by Spero Health on 2026-07-01) whose only public host is a WordPress marketing site — 6,945 archived URLs across its entire history contain no /api, /developers or /docs path, and no GitHub organization exists — so there is no software product to expose an API; the live site additionally answers every automated request, including /robots.txt, with a SiteGround `sg-captcha: challenge` interstitial (HTTP 202).'
  evidence:
  - status: 202
    url: https://www.cleanslatecenters.com/developers
  - status: 202
    url: https://www.cleanslatecenters.com/robots.txt
  - status: 200
    url: https://web.archive.org/cdx/search/cdx?url=cleanslatecenters.com&matchType=domain&fl=original&collapse=urlkey&limit=20000
  - status: 200
    url: https://api.github.com/search/users?q=cleanslate+type:org
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: 'CleanSlate (CleanSlate Centers) is a national outpatient medical group treating opioid and alcohol use disorder with physician-led, office-based medication-assisted treatment — FDA-approved medication combined with primary care and behavioral health therapy for polysubstance use and co-occurring disorders. Founded in 2009 in Massachusetts by Dr. Amanda Wilson in response to the opioid epidemic, it grew to more than 65 outpatient centers across eight states and raised roughly $79M in venture backing before being acquired by Spero Health on July 1, 2026. CleanSlate is a care-delivery organization: it operates clinics, not a software platform, and publishes no public API, SDK, developer portal or machine-readable specification.'
layout: provider
modified: '2026-08-09'
name: CleanSlate
nav: Providers
network: true
overview: CleanSlate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Behavioral Health, Addiction Treatment, and Opioid Use Disorder.
random_paper: 2
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cleanslate/refs/heads/main/screenshots/cleanslate-2026-09-02T145103.png
security:
- kind: domain-security
  name: Cleanslate Domain Security
  slug: cleanslate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cleanslate
tags:
- Company
- Healthcare
- Behavioral Health
- Addiction Treatment
- Opioid Use Disorder
- Medication-Assisted Treatment
- Outpatient Clinics
- United States
website: https://www.cleanslatecenters.com/
---
