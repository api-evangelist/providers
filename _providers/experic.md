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
  url: security/experic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/experic-llms.txt
- group: company
  title: ''
  type: Website
  url: https://expericservices.com/
- group: company
  title: ''
  type: About
  url: https://expericservices.com/the-experic-difference/
- group: operate
  title: ''
  type: Support
  url: https://expericservices.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://expericservices.com/news-events/
- group: company
  title: ''
  type: BlogRSS
  url: https://expericservices.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://expericservices.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epic-csc-llc/
coverage:
  checked: '2026-08-12'
  detail: Experic is a pharmaceutical CDMO selling physical development, manufacturing and clinical-supply services; its entire 142-URL sitemap is marketing, resource, news and careers pages with no developer, docs, API or portal path, and every contract-discovery probe (openapi.json, swagger.json, api-docs, graphql, llms.txt, all eight /.well-known/ paths) returned 404 from the origin, with the only machine-readable endpoint being the marketing site's own WordPress /wp-json/ CMS surface.
  evidence:
  - status: 404
    url: https://expericservices.com/openapi.json
  - status: 404
    url: https://expericservices.com/graphql
  - status: 404
    url: https://expericservices.com/llms.txt
  - status: 404
    url: https://expericservices.com/.well-known/agent-card.json
  - status: 404
    url: https://expericservices.com/.well-known/security.txt
  - status: 0
    url: https://api.expericservices.com/
  - status: 0
    url: https://developer.expericservices.com/
  - status: 200
    url: https://expericservices.com/page-sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: Experic is a specialist powder-handling contract development and manufacturing organization (CDMO) founded in 2018, headquartered in Cranbury, New Jersey, with an EU clinical supply center in Ireland. The company provides process, analytical and formulation development, clinical and commercial cGMP manufacturing, dry powder inhalation (DPI) and capsule/powder dosing, autoinjector and pen assembly, and clinical trial packaging, labeling, storage and logistics. Experic is a physical-goods manufacturing and clinical supply services business; it publishes no public developer program, API documentation, or machine-readable API contract.
image: https://expericservices.com/wp-content/uploads/2025/02/cropped-favicon-X-270x270.png
layout: provider
modified: '2026-08-12'
name: Experic
nav: Providers
network: true
overview: 'Experic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Life Sciences, Manufacturing, and CDMO.


  Experic''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 5
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/experic/refs/heads/main/screenshots/experic-2026-09-02T145452.png
security:
- kind: domain-security
  name: Experic Domain Security
  slug: experic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: experic
tags:
- Company
- Pharmaceuticals
- Life Sciences
- Manufacturing
- CDMO
- Clinical Trials
- Contract Manufacturing
- Drug Delivery
- Supply Chain
- Packaging
website: https://expericservices.com/
---
