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
  url: security/creditas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.creditas.com
- group: company
  title: ''
  type: About
  url: https://www.creditas.com/quem-somos
- group: company
  title: ''
  type: Blog
  url: https://www.creditas.com/exponencial/
- group: operate
  title: ''
  type: Support
  url: https://www.creditas.com/canais-de-atendimento
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creditas.com/legal/termos-condicoes
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creditas.com/legal/politica-privacidade
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Creditas
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/creditas-llms.txt
created: '2026-07-17'
description: Creditas is a Brazilian digital lending fintech founded in 2012 and headquartered in Sao Paulo, operating in Brazil and Mexico. It provides secured consumer credit - loans backed by real estate (home equity) and vehicles, plus private payroll (consignado privado) loans - alongside auto insurance, multi-bank real estate and vehicle financing, and a corporate benefits platform (salary advance, flexible-benefits cards, and financial education). Regulated by the Banco Central do Brasil, Creditas has originated over R$12 billion in credit. It is backed by QED Investors and the SoftBank Vision Fund. No public developer API program or OpenAPI has been identified; this profile captures the company public identity, its published llms.txt, and its domain security posture.
image: https://images.ctfassets.net/n3x4bsh5l2so/1HmeS6eXTudm2vvxDAxGBt/6c5a15b384c9bcacb7f14c9447aec8f7/creditas-garantia-proximo-passo.jpg
layout: provider
modified: '2026-07-18'
name: Creditas
nav: Providers
network: true
overview: 'Creditas is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Credit, Fintech, Lending, and Brazil.


  Creditas'' developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/creditas/refs/heads/main/screenshots/creditas-2026-07-25T210718.png
security:
- kind: domain-security
  name: Creditas Domain Security
  slug: creditas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: creditas
tags:
- Company
- Credit
- Fintech
- Lending
- Brazil
- Insurance
- Financial-Services
- Payroll Loans
website: https://www.creditas.com
---
