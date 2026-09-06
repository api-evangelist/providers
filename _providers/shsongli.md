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
  url: security/shsongli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shsongli.com
created: '2026-07-17'
description: 'shsongli (Shanghai Pine & Power / Songli Biotech Co., Ltd.) is a Shanghai-based biotechnology and medical-device maker specializing in the R&D, manufacture and sale of biological hemostatic products, most notably animal-derived quick-dissolving fibrin glue with independent IP, used in surgery and expanding into tissue engineering. The company operates a Class III medical-device line and is ISO 13485 and GMP certified. Surfaced as a portfolio company of the venture firm qiming and added to the API Evangelist network. The enrichment pass found no public developer or API surface: the shsongli.com domain returns 404 on every path (EIMS web server) with an expired TLS certificate, and no docs, portal, packages, MCP, llms.txt, /.well-known/ endpoints, or security program were published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shsongli.png
layout: provider
modified: '2026-07-21'
name: shsongli
nav: Providers
network: true
overview: shsongli is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Medical Devices, Healthcare, and Hemostatic Products.
random_paper: 10
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 1
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
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Shsongli Domain Security
  slug: shsongli-domain-security
  summary_line: no transport/DNS hardening detected
slug: shsongli
tags:
- Company
- Biotechnology
- Medical Devices
- Healthcare
- Hemostatic Products
- Tissue Engineering
- China
website: https://shsongli.com
---
