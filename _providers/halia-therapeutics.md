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
- group: company
  title: ''
  type: Website
  url: https://haliatx.com/
- group: company
  title: ''
  type: About
  url: https://haliatx.com/about
- group: company
  title: ''
  type: Blog
  url: https://haliatx.com/news
- group: operate
  title: ''
  type: Support
  url: https://haliatx.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://haliatx.com/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/halia-therapeutics-domain-security.yml
coverage:
  checked: '2026-08-22'
  detail: Halia Therapeutics is a clinical-stage biopharmaceutical developer whose only public web property is a Webflow marketing site; every OpenAPI/GraphQL/MCP/A2A discovery path on haliatx.com returns a 404 HTML page, no api/dev/docs/portal subdomain resolves in DNS, and no GitHub organization exists under haliatx or halia-therapeutics.
  evidence:
  - status: 404
    url: https://haliatx.com/openapi.json
  - status: 404
    url: https://haliatx.com/.well-known/api-catalog
  - status: 404
    url: https://haliatx.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/haliatx
  - status: 200
    url: https://haliatx.com/
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'Halia Therapeutics, Inc. is a privately held clinical-stage biopharmaceutical company headquartered in Lehi, Utah, founded in 2017 and led by CEO Dr. David Bearss. Halia discovers and develops small-molecule therapies that target the immune system''s inflammatory response — chiefly allosteric NEK7/NLRP3 inflammasome inhibition and LRRK2 inhibition — to resolve the chronic inflammation that drives hematologic, metabolic and neurodegenerative disease. Its lead clinical program, ofirnoflast (HT-6184), holds FDA Fast Track and Orphan Drug designation for lower-risk myelodysplastic syndromes; HT-4253, an LRRK2 inhibitor aimed at neuroinflammation and Alzheimer''s prevention in APOE4 carriers, has completed a first-in-human Phase 1 study. The company also markets a "genetic resilience" research platform (GENMOR) built on family-cohort genomics. Halia is a drug developer, not a software vendor: it publishes a Webflow corporate site with pipeline, platform and press pages, and no developer
  program, public API, SDK or machine-readable specification of any kind.'
image: https://cdn.prod.website-files.com/688b451b45ceaa63f2f18f66/688cae0819292502275bf280_Company%20Logo.svg
layout: provider
modified: '2026-08-22'
name: Halia Therapeutics
nav: Providers
network: true
overview: 'Halia Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Drug Discovery.


  Halia Therapeutics'' developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/halia-therapeutics/refs/heads/main/screenshots/halia-therapeutics-2026-09-02T145653.png
security:
- kind: domain-security
  name: Halia Therapeutics Domain Security
  slug: halia-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: halia-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Drug Discovery
- Clinical Trials
- Immunology
- Neuroscience
- Genomics
- Health
website: https://haliatx.com/
---
