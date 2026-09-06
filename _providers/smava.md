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
  url: security/smava-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smava.de/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smava
created: '2026-07-17'
description: Smava (smava GmbH) is a Berlin-based German consumer-finance marketplace, founded in 2007, that lets borrowers compare personal, auto, and mortgage loan offers from more than 20 partner banks for amounts ranging from EUR 1,000 to EUR 120,000, without impacting their SCHUFA credit score. The company operates a digital, data-driven loan-brokerage platform serving consumers across Germany and employs roughly 600 people. It was added to the API Evangelist network as a portfolio company of Earlybird. As of this enrichment pass Smava is a consumer (B2C) web and mobile-app business and publishes no public developer API, developer portal, OpenAPI specification, or well-known API discovery endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smava.png
layout: provider
modified: '2026-07-21'
name: Smava
nav: Providers
network: true
overview: Smava is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, Loan Comparison, and Consumer Finance.
random_paper: 11
score:
  band: minimal
  composite: 5.3
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
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smava/refs/heads/main/screenshots/smava-2026-09-02T155944.png
security:
- kind: domain-security
  name: Smava Domain Security
  slug: smava-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smava
tags:
- Company
- Fintech
- Lending
- Loan Comparison
- Consumer Finance
- Marketplace
- Germany
website: https://www.smava.de/
---
