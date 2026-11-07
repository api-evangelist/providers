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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Portal for families to manage babysitting services.
  name: Family Portal
  slug: family-portal
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/babacerta-com-br/llms/babacerta-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/babacerta-com-br-llms.txt
- group: other
  href: https://artifacts.apis.io/babacerta-com-br/hosts/babacerta-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/babacerta-com-br-hosts.yml
- group: auth
  href: https://artifacts.apis.io/babacerta-com-br/security/babacerta-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/babacerta-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://babacerta.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://babacerta.com.br/portal-da-familia/
- group: start
  title: ''
  type: GettingStarted
  url: https://babacerta.com.br/como-funciona/
- group: operate
  title: ''
  type: Support
  url: https://babacerta.com.br/suporte/
- group: company
  title: ''
  type: Blog
  url: https://babacerta.com.br/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://babacerta.com.br/termos-de-uso/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://babacerta.com.br/politica-privacidade/
coverage:
  checked: '2026-11-02'
  detail: Babá Certa provides a family portal but does not expose a public API.
  evidence:
  - status: 200
    url: https://babacerta.com.br/
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: 'A Babá Certa é o app brasileiro de babás verificadas: identidade dos dois lados, CPF na Receita Federal e antecedentes consultados por nossa conta, moderação ativa e antifraude. Vaga grátis, babá nunca paga.'
image: https://babacerta.com.br/logo-120.png
layout: provider
modified: '2026-11-02'
name: Babá Certa
nav: Providers
network: true
overview: 'Babá Certa is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Babysitting, Marketplace, Verification, Brazil, and Childcare.


  Babá Certa''s developer surface includes getting-started guide, support, engineering blog, and 7 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 15.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Babacerta Com Br Domain Security
  slug: babacerta-com-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: babacerta-com-br
tags:
- Babysitting
- Marketplace
- Verification
- Brazil
- Childcare
website: https://babacerta.com.br/
---
