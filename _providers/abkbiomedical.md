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
- group: company
  title: ''
  type: Website
  url: https://abkbiomedical.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/abk-biomedical-inc-
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/abkbiomedical
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abkbiomedical-domain-security.yml
coverage:
  checked: '2026-09-06'
  detail: 'ABK Biomedical manufactures implantable radioembolization and embolic microspheres (Eye90, Easi-Vue) in its own Halifax cleanroom rather than software: no api., developer., dev., portal., app. or data. host exists in DNS, there is no GitHub organization and no package under this name on npm or PyPI, and abkbiomedical.com is a SiteGround-hosted marketing site whose every path — /robots.txt included — answers HTTP 202 with an sg-captcha interstitial rather than any document.'
  evidence:
  - status: 202
    url: https://abkbiomedical.com/.well-known/api-catalog
  - status: 202
    url: https://abkbiomedical.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/abkbiomedical
  - status: 404
    url: https://pypi.org/pypi/abkbiomedical/json
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=abkbiomedical
  - status: 200
    url: https://equityzen.com/company/abkbiomedical
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: ABK Biomedical Inc. is a Halifax, Nova Scotia medical device company founded in 2012 as a spin-out of Dalhousie University, developing and manufacturing imageable embolic microspheres for interventional oncology. Its lead product, Eye90 microspheres, is a yttrium-90 radioembolization device built on a proprietary imageable glass composition that is directly visible under fluoroscopy, X-ray and CT during and after the procedure, and it was granted FDA Breakthrough Device Designation for unresectable hepatocellular carcinoma and studied in the ROUTE90 pivotal trial. Its Easi-Vue embolic microspheres received FDA 510(k) clearance for embolization of hypervascular tumors and arteriovenous malformations. Devices are produced in the company's own cleanroom manufacturing facility in Halifax, with a second office in Ladera Ranch, California. ABK Biomedical is a regulated medical device manufacturer rather than a software vendor, and as of this profile it publishes no developer program,
  API documentation, SDK, or machine-readable API contract of any kind.
layout: provider
modified: '2026-09-06'
name: ABK Biomedical
nav: Providers
network: true
overview: ABK Biomedical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Interventional Oncology, Radioembolization, Medical Imaging, and Oncology.
random_paper: 12
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
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
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
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abkbiomedical Domain Security
  slug: abkbiomedical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: abkbiomedical
tags:
- Medical Devices
- Interventional Oncology
- Radioembolization
- Medical Imaging
- Oncology
- Healthcare
- Manufacturing
- Canada
- Company
website: https://abkbiomedical.com/
---
