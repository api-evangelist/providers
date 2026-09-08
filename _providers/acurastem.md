---
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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acurastem-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acurastem-llms.txt
- group: company
  title: ''
  type: Website
  url: https://acurastem.com/
- group: company
  title: ''
  type: About
  url: https://acurastem.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://acurastem.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://acurastem.com/media
- group: company
  title: ''
  type: Careers
  url: https://acurastem.com/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acurastem.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/12903559/
- group: other
  title: ''
  type: X
  url: https://x.com/acurastem
coverage:
  checked: '2026-09-06'
  detail: AcuraStem is a preclinical ALS/FTD therapeutics developer whose entire public web presence is a six-page Concrete CMS 9.5.2 marketing site (about, science, therapeutics, media, careers) with no developer, API, or data-access section, no API subdomain resolving in DNS, and an empty GitHub organization with zero public repositories.
  evidence:
  - status: 200
    url: https://acurastem.com/
  - status: 404
    url: https://acurastem.com/openapi.json
  - status: 404
    url: https://acurastem.com/.well-known/api-catalog
  - status: 404
    url: https://acurastem.com/llms.txt
  - status: 200
    url: https://acurastem.com/sitemap.xml
  - status: 200
    url: https://api.github.com/orgs/acurastem
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'AcuraStem, Inc. is a privately held, patient-based biotechnology company headquartered in Monrovia, California, developing therapeutics for neurodegenerative diseases including sporadic ALS (amyotrophic lateral sclerosis) and frontotemporal dementia (FTD). The company''s proprietary iNeuroRx drug-discovery platform builds disease models from induced pluripotent stem cells (iPSC) taken from individual patients, in place of animal models, and pairs them with machine-learning analysis to identify and validate targets. Its lead antisense oligonucleotide candidate, AS-241 (PIKFYVE), is advancing toward first-in-human testing with California Institute for Regenerative Medicine (CIRM) grant support. AcuraStem is a therapeutics developer rather than a software vendor: it publishes no public API, developer portal, SDK, or machine-readable contract of any kind. This profile records that absence with the probe evidence behind it.'
image: https://acurastem.com/application/files/7516/7235/4056/acs_logo_notag.png
layout: provider
modified: '2026-09-06'
name: AcuraStem
nav: Providers
network: true
overview: 'AcuraStem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Life Sciences, and Drug Discovery.


  AcuraStem''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acurastem Domain Security
  slug: acurastem-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acurastem
tags:
- Company
- Biotechnology
- Therapeutics
- Life Sciences
- Drug Discovery
- Neuroscience
- Neurodegenerative Disease
- ALS
- Stem Cells
- Machine Learning
- Private Company
website: https://acurastem.com/
---
