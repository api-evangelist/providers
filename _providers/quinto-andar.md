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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.quintoandar.com.br
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.quintoandar.com.br/ajuda
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quintoandar.com.br/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quintoandar.com.br/politica-de-privacidade
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quinto-andar-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/quinto-andar-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quinto-andar-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/quinto-andar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/quintoandar
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quintoandar
created: '2026-07-17'
description: QuintoAndar is a Brazilian proptech real-estate marketplace that lets people rent and buy homes online without a guarantor, with digital visit scheduling, digital contract signing, rent and sale pricing intelligence (QPreço), owner financial management, and a real-estate consortium financing program. It operates a two-sided marketplace across major Brazilian cities including São Paulo, Rio de Janeiro, Belo Horizonte, Porto Alegre, Campinas, and Curitiba, earning revenue on rental and sales commissions. Surfaced as a portfolio company of ribbit-capital and enriched into the API Evangelist network. No public developer API surface was found; the company does publish a security.txt with a Bugcrowd bug bounty program.
image: https://www.quintoandar.com.br/favicon.ico
layout: provider
modified: '2026-08-08'
name: Quinto Andar
nav: Providers
network: true
overview: Quinto Andar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PropTech, Real-Estate, Marketplace, and Rentals.
random_paper: 17
score:
  band: emerging
  composite: 11.9
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
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 11.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quinto-andar/refs/heads/main/screenshots/quinto-andar-2026-09-02T152701.png
security:
- kind: domain-security
  name: Quinto Andar Domain Security
  slug: quinto-andar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quinto Andar Vulnerability Disclosure
  slug: quinto-andar-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: quinto-andar
tags:
- Company
- PropTech
- Real-Estate
- Marketplace
- Rentals
- Brazil
- Housing
website: https://www.quintoandar.com.br
---
