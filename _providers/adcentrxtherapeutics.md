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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adcentrxtherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adcentrx.com/
- group: company
  title: ''
  type: About
  url: https://www.adcentrx.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.adcentrx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.adcentrx.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.adcentrx.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adcentrx.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adcentrx.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adcentrx-therapeutics
coverage:
  checked: '2026-09-07'
  detail: Adcentrx Therapeutics is a clinical-stage oncology biotech developing antibody-drug conjugates (ADRX-0706, ADRX-0405); its only web property is a SiteGround-hosted WordPress corporate/investor site whose entire path space answers HTTP 202 with an sg-captcha robot challenge, and no api., docs., developer. or portal. host exists in DNS - the site nav, read from an Internet Archive snapshot, has no developer section.
  evidence:
  - status: 202
    url: https://www.adcentrx.com/
  - status: 202
    url: https://www.adcentrx.com/.well-known/api-catalog
  - status: 202
    url: https://www.adcentrx.com/openapi.json
  - status: 200
    url: http://web.archive.org/web/20260810050011/https://www.adcentrx.com/
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: 'Adcentrx Therapeutics is a clinical-stage biotechnology company headquartered in San Diego, California, developing next-generation antibody-drug conjugates (ADCs) and protein conjugate therapeutics for cancer and other life-threatening diseases. Its proprietary i-Conjugation technology platform pairs stable conjugation chemistry and protease-cleavable linkers with novel small-molecule payloads; the clinical pipeline includes ADRX-0706 (Nectin-4) and ADRX-0405 (STEAP1). The company was surfaced via the API Evangelist harvest backlog (source: secondary-market). It publishes a corporate and investor-relations website only — no developer program, API, SDK, or machine-readable specification of any kind was found.'
image: https://www.adcentrx.com/wp-content/uploads/2021/11/Adcentrx-logo.png
layout: provider
modified: '2026-09-07'
name: Adcentrx Therapeutics
nav: Providers
network: true
overview: 'Adcentrx Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Oncology.


  Adcentrx Therapeutics'' developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 12
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
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
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
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adcentrxtherapeutics Domain Security
  slug: adcentrxtherapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adcentrxtherapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Oncology
- Healthcare
- Clinical Stage
- Antibody Drug Conjugates
website: https://www.adcentrx.com/
---
