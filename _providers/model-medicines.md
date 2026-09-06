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
  url: security/model-medicines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modelmedicines.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modelmedicines.com/privacy-policy
created: '2026-07-17'
description: Model Medicines is an AI-first biotechnology company based in San Diego, California, discovering and developing first-in-class small-molecule drugs by targeting fundamental disease mechanisms it calls biological choke points. Its end-to-end GALILEO AI engine spans drug design, target discovery, and preclinical development, supported by specialized models including AmesNet for regulatory-grade toxicology prediction and ChemPrint for chemical property prediction. Lead programs target RdRp Thumb-1 (a conserved allosteric pocket on viral RNA-dependent RNA polymerase) and BRD4, with lead assets MDL-001, a broad-spectrum oral antiviral candidate, and MDL-4102. Surfaced as a portfolio company of 8vc and added to the API Evangelist network. As of this enrichment pass Model Medicines publishes no public API, developer portal, SDK, or documentation surface; its AI platform is used internally for drug discovery.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/model-medicines.png
layout: provider
modified: '2026-07-20'
name: Model Medicines
nav: Providers
network: true
overview: Model Medicines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Drug Discovery, Artificial Intelligence, and Pharmaceuticals.
random_paper: 7
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 1
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Model Medicines Domain Security
  slug: model-medicines-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: model-medicines
tags:
- Company
- Biotechnology
- Drug Discovery
- Artificial Intelligence
- Pharmaceuticals
- Small Molecules
- Life Sciences
website: https://modelmedicines.com
---
