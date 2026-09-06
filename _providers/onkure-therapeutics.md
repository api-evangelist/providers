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
  url: security/onkure-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onkuretherapeutics.com/
- group: company
  title: ''
  type: About
  url: https://onkuretherapeutics.com/about/company/
- group: operate
  title: ''
  type: Support
  url: https://onkuretherapeutics.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onkuretherapeutics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onkuretherapeutics.com/privacy-policy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.onkuretherapeutics.com/
- group: company
  title: ''
  type: News
  url: https://investors.onkuretherapeutics.com/news-events/news-releases
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onkure-tx/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/OnKureTx
- group: agent
  title: ''
  type: WellKnown-Probe
  url: well-known/onkure-therapeutics-well-known.yml
coverage:
  checked: '2026-08-26'
  detail: 'OnKure is a clinical-stage biopharmaceutical company whose product is a drug candidate (OKI-219), not software: its onkuretherapeutics.com site is a WordPress marketing presence with only About/Pipeline/Careers/Contact sections, the sole machine-readable surface is the default WordPress /wp-json/ CMS endpoint exposing Yoast, Wordfence and Redirection plugin routes rather than any OnKure API, and api/developer/docs/graphql/mcp subdomains do not resolve in DNS.'
  evidence:
  - status: 404
    url: https://onkuretherapeutics.com/openapi.json
  - status: 404
    url: https://onkuretherapeutics.com/.well-known/agent-card.json
  - status: 404
    url: https://onkuretherapeutics.com/llms.txt
  - status: 0
    url: https://api.onkuretherapeutics.com/openapi.json
  - status: 200
    url: https://onkuretherapeutics.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'OnKure Therapeutics (Nasdaq: OKUR) is a publicly traded, clinical-stage biopharmaceutical company headquartered in Boulder, Colorado, developing precision medicines for people with cancer. The company designs mutant-selective small-molecule inhibitors against oncogenic drivers in the PI3K pathway; its lead program OKI-219 is a selective PI3K-alpha H1047R inhibitor in clinical development, with additional discovery programs targeting further PI3K-alpha mutations. OnKure became publicly listed through its 2024 combination with Reneo Pharmaceuticals. It is a therapeutics developer rather than a software vendor: it operates a corporate and investor relations web presence and publishes no developer program, public API, SDK, or machine-readable API contract.'
image: https://onkuretherapeutics.com/wp-content/uploads/logo-onkure-color-min.png
layout: provider
modified: '2026-08-26'
name: OnKure Therapeutics
nav: Providers
network: true
overview: 'OnKure Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Precision Medicine.


  OnKure Therapeutics'' developer surface includes support, product news, and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.0
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onkure-therapeutics/refs/heads/main/screenshots/onkure-therapeutics-2026-09-02T150847.png
security:
- kind: domain-security
  name: Onkure Therapeutics Domain Security
  slug: onkure-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: onkure-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Precision Medicine
- Clinical Trials
- Life Sciences
- Drug Discovery
- Publicly Traded
website: https://onkuretherapeutics.com/
---
