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
  url: security/nuvig-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nuvigtx.com/
- group: company
  title: ''
  type: About
  url: https://nuvigtx.com/science/
- group: other
  title: ''
  type: Science
  url: https://nuvigtx.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://nuvigtx.com/pipeline/
- group: other
  title: ''
  type: Team
  url: https://nuvigtx.com/team/
- group: company
  title: ''
  type: News
  url: https://nuvigtx.com/news/
- group: company
  title: ''
  type: Blog
  url: https://nuvigtx.com/news/
- group: company
  title: ''
  type: BlogFeeds
  url: https://nuvigtx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://nuvigtx.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://nuvigtx.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nuvigtx.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuvigtx.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://nuvigtx.com/cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nuvig-therapeutics-inc
- group: company
  title: ''
  type: Twitter
  url: https://x.com/nuvigtx
- group: company
  title: ''
  type: Investors
  url: https://www.hiive.com/securities/nuvig-therapeutics-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nuvig-therapeutics-llms.txt
coverage:
  checked: '2026-08-04'
  detail: Nuvig is a clinical-stage biotech whose product is a drug candidate (NVG-2089), not software — nuvigtx.com is a five-page corporate WordPress site with no /developers, /api or /docs path, no GitHub organization, and no package on any registry.
  evidence:
  - status: 404
    url: https://nuvigtx.com/developers
  - status: 404
    url: https://nuvigtx.com/openapi.json
  - status: 404
    url: https://nuvigtx.com/.well-known/agent-card.json
  - status: 200
    url: https://nuvigtx.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'Nuvig Therapeutics, Inc. is a privately held, clinical-stage biotechnology company headquartered at 3450 Hillview Avenue, Palo Alto, California, developing next-generation immunomodulators for chronic autoimmune and inflammatory disease. Its lead investigational candidate, NVG-2089, is an engineered Fc fragment designed to selectively engage type II Fc receptors and harness an endogenous regulatory mechanism that resolves autoimmune dysregulation while preserving normal immune function; the first patient was dosed in a Phase 2 trial in chronic inflammatory demyelinating polyneuropathy (CIDP) in May 2025. The company announced a $161 million Series B financing in December 2024. Nuvig is a therapeutics developer, not a software vendor: as of August 2026 it publishes no developer portal, API reference, SDK, GitHub organization, or machine-readable API contract of any kind. Its public web surface is a corporate WordPress site covering science, pipeline, team, news and careers,
  from which the only machine-readable artifact published is a Yoast-generated llms.txt.'
image: https://nuvigtx.com/wp-content/uploads/2022/04/bg-logo-nuvig.svg
layout: provider
modified: '2026-08-04'
name: Nuvig Therapeutics
nav: Providers
network: true
overview: 'Nuvig Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Immunology, and Autoimmune Disease.


  Nuvig Therapeutics'' developer surface includes product news, engineering blog, and 16 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuvig-therapeutics/refs/heads/main/screenshots/nuvig-therapeutics-2026-08-07T185808.png
security:
- kind: domain-security
  name: Nuvig Therapeutics Domain Security
  slug: nuvig-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nuvig-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Immunology
- Autoimmune Disease
- Therapeutics
- Clinical Trials
- Life Sciences
- United States
website: https://nuvigtx.com/
---
