---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/redsys/hosts/redsys-hosts.yml
  title: ''
  type: Hosts
  url: hosts/redsys-hosts.yml
- group: build
  href: https://artifacts.apis.io/redsys/packages/redsys-packages.yml
  title: ''
  type: SDKs
  url: packages/redsys-packages.yml
- group: build
  href: https://artifacts.apis.io/redsys/packages/redsys-packages.yml
  title: ''
  type: Packages
  url: packages/redsys-packages.yml
- group: auth
  href: https://artifacts.apis.io/redsys/security/redsys-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/redsys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redsys.es/
- group: company
  title: ''
  type: Blog
  url: https://redsys.es/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pagosonline.redsys.es/desarrolladores-inicio/
- group: docs
  title: ''
  type: Documentation
  url: https://pagosonline.redsys.es/desarrolladores-inicio/
- group: docs
  title: ''
  type: APIReference
  url: https://pagosonline.redsys.es/desarrolladores-inicio/
- group: start
  title: ''
  type: GettingStarted
  url: https://pagosonline.redsys.es/desarrolladores-inicio/
- group: operate
  title: ''
  type: Support
  url: https://redsys.es/contacto
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redsys.es/aviso-legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redsys.es/politica-de-privacidad
- group: commercial
  title: ''
  type: Pricing
  url: https://redsys.es/politica-corporativa
coverage:
  checked: '2026-10-27'
  detail: No public developer documentation or API specifications were found on redsys.es or its subdomains.
  evidence:
  - status: 200
    url: https://redsys.es/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Redsys is a leading Spanish payment services provider with over 40 years of experience. It offers a comprehensive suite of acquiring, issuing, and interbank services, supporting merchants, financial institutions, and digital platforms. The company focuses on innovation, security, and high‑quality payment solutions across Spain and Latin America, serving a wide range of industries including retail, health, and e‑commerce.
layout: provider
modified: '2026-10-27'
name: Redsys
nav: Providers
network: true
overview: 'Redsys is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Financial Services, Acquiring, and Issuing.


  Redsys'' developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, and 8 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 0
  name: Redsys Rate Limits
  slug: redsys-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Redsys Domain Security
  slug: redsys-domain-security
  summary_line: TLSv1.2 · DMARC
slug: redsys
tags:
- Company
- Payments
- Financial Services
- Acquiring
- Issuing
website: https://redsys.es/
---
