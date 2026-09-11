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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adlai-nortye-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adlainortye.com/
- group: company
  title: ''
  type: About
  url: https://www.adlainortye.com/index.php/about
- group: other
  title: ''
  type: x-DrugPipeline
  url: https://www.adlainortye.com/index.php/products
- group: operate
  title: ''
  type: PressReleases
  url: https://www.adlainortye.com/index.php/news
- group: operate
  title: ''
  type: Support
  url: https://www.adlainortye.com/index.php/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adlainortye.com/index.php/termOfUse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adlainortye.com/index.php/privacyPolicy
- group: company
  title: ''
  type: Careers
  url: https://www.adlainortye.com/index.php/recruit
- group: company
  title: ''
  type: Partners
  url: https://www.adlainortye.com/index.php/partner_business
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adlainortye/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/AdlaiNortyeBio
- group: other
  title: ''
  type: x-SecondaryMarket
  url: https://forgeglobal.com/adlai-nortye_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adlai-nortye-llms.txt
coverage:
  checked: '2026-09-07'
  detail: 'Adlai Nortye is a clinical-stage oncology drug developer (Nasdaq: ANL) whose product is a molecule, not software - its corporate site has no developer, docs or API section at all, and every contract probe across www, ir and cn returned 403 or 404.'
  evidence:
  - status: 404
    url: https://www.adlainortye.com/openapi.json
  - status: 404
    url: https://www.adlainortye.com/llms.txt
  - status: 403
    url: https://www.adlainortye.com/.well-known/agent-card.json
  - status: 404
    url: https://www.adlainortye.com/apis.json
  - status: 403
    url: https://ir.adlainortye.com/
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: 'Adlai Nortye is a global clinical-stage biopharmaceutical company, headquartered in Hangzhou, China with US operations in New Jersey, developing differentiated immuno-oncology and precision-targeted cancer medicines. Its pipeline covers two therapeutic areas: precision RAS pathway targeted therapies — the oral pan-RAS(ON) inhibitor AN9025 and the CEACAM5-targeting antibody-drug conjugate AN4035 built on the company''s proprietary RASiCA (RAS Inhibitor Conjugated Antibody) platform — and next-generation PD-1/L1 pathway modulating immunotherapies including AN8025, a multi-functional T-cell and antigen-presenting-cell modulating fusion protein, plus the oral EP4 antagonist AN0025 (palupiprant). The company is listed on Nasdaq under the ticker ANL. Adlai Nortye publishes no developer program, API, SDK or machine-readable contract of any kind.'
image: https://www.adlainortye.com/static/web/img/logob_20210415.svg
layout: provider
modified: '2026-09-07'
name: Adlai Nortye
nav: Providers
network: true
overview: 'Adlai Nortye is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Healthcare.


  Adlai Nortye''s developer surface includes support and 13 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 10.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adlai Nortye Domain Security
  slug: adlai-nortye-domain-security
  summary_line: TLSv1.2 · HSTS
slug: adlai-nortye
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Healthcare
- Oncology
- Clinical Trials
- Drug Development
website: https://www.adlainortye.com/
---
