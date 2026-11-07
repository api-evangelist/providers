---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/imdex/authentication/imdex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/imdex-authentication.yml
- group: design
  href: https://artifacts.apis.io/imdex/conformance/imdex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/imdex-conformance.yml
- group: other
  href: https://artifacts.apis.io/imdex/hosts/imdex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/imdex-hosts.yml
- group: build
  href: https://artifacts.apis.io/imdex/integrations/imdex-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/imdex-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/imdex/vendors/imdex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/imdex-vendors.yml
- group: auth
  href: https://artifacts.apis.io/imdex/security/imdex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/imdex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.imdex.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.imdex.com/news-knowledge/news
- group: operate
  title: ''
  type: Support
  url: https://support.imdexlimited.com/csm
- group: operate
  title: ''
  type: Contact
  url: https://www.imdex.com/about/contact-us
- group: company
  title: ''
  type: About
  url: https://www.imdex.com/about
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.imdex.com/investor
- group: other
  title: ''
  type: Product
  url: https://www.imdex.com/software/hub-iq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imdex.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imdex.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/imdex-limited
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@imdexlimited7458
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/imdexlimited/
created: '2026-10-21'
description: 'IMDEX Limited (ASX: IMD) is an Australian mining-technology company that creates drilling, sensor and software solutions to help resource companies find, define and mine orebodies faster, safer and more sustainably through trusted data and innovation. Its products include downhole survey and orientation instruments, drilling optimisation products and the IMDEXHUB-IQ cloud data platform, which issues API keys for third-party integrations such as Seequent Central. IMDEX was surfaced via the API Evangelist harvest backlog (australia-apidays-2026).'
image: https://www.imdex.com/assets/img/logo_white.svg
layout: provider
modified: '2026-10-21'
name: IMDEX
nav: Providers
network: true
overview: 'IMDEX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mining, Mining Technology, Geoscience, and Drilling.


  IMDEX''s developer surface includes authentication, support, YouTube channel, and 15 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/imdex/imdex-2026-11-03T133709.png
security:
- kind: authentication
  name: Imdex Authentication
  slug: imdex-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Imdex Domain Security
  slug: imdex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imdex
tags:
- Company
- Mining
- Mining Technology
- Geoscience
- Drilling
- Data Platform
- Australia
website: https://www.imdex.com/
---
