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
  url: security/aardvark-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aardvark-therapeutics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://aardvarktherapeutics.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aardvarktherapeutics.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aardvarktherapeutics.com/legal/terms-of-use/
- group: operate
  title: ''
  type: Contact
  url: https://aardvarktherapeutics.com/contact/
- group: company
  title: ''
  type: News
  url: https://aardvarktherapeutics.com/in-the-news/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.aardvarktherapeutics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aardvark-Therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/aardvark-therapeutics_stock/
coverage:
  checked: '2026-08-06'
  detail: Aardvark Therapeutics is a clinical-stage biopharmaceutical company whose product is a drug (ARD-101), not software — its entire site is a seven-page WordPress marketing presence (home, science, programs, team, news, contact, legal) with no developer, API or documentation section anywhere in its sitemap.
  evidence:
  - status: 404
    url: https://aardvarktherapeutics.com/openapi.json
  - status: 404
    url: https://aardvarktherapeutics.com/developers
  - status: 404
    url: https://aardvarktherapeutics.com/.well-known/agent-card.json
  - status: 200
    url: https://aardvarktherapeutics.com/page-sitemap.xml
  - status: 200
    url: https://api.github.com/orgs/aardvark-therapeutics
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Aardvark Therapeutics, Inc. is a Nasdaq-listed (AARD) clinical-stage biopharmaceutical company developing novel small-molecule therapies designed to inhibit hunger and treat metabolic disease. Its lead candidate, ARD-101, is an oral, gut-restricted agonist of bitter taste receptors (TAS2Rs) on the luminal side of the intestine, which triggers the release of satiety hormones to suppress hunger signaling; it has been evaluated for hyperphagia associated with Prader-Willi Syndrome, including the Phase 3 HERO trial, as well as in obesity and hypothalamic obesity. The company operates purely as a drug-development organization: its public web presence consists of science, programs, team, news and investor-relations material, and it publishes no developer program, public API, SDK, webhook surface or machine-readable specification of any kind.'
image: https://i0.wp.com/aardvarktherapeutics.com/wp-content/uploads/2022/11/d-footer-logo.png
layout: provider
modified: '2026-08-06'
name: Aardvark Therapeutics
nav: Providers
network: true
overview: 'Aardvark Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Aardvark Therapeutics'' developer surface includes product news and 9 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.4
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aardvark-therapeutics/refs/heads/main/screenshots/aardvark-therapeutics-2026-08-07T160736.png
security:
- kind: domain-security
  name: Aardvark Therapeutics Domain Security
  slug: aardvark-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aardvark-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Drug Development
- Rare Disease
- Metabolic Health
website: https://aardvarktherapeutics.com/
---
