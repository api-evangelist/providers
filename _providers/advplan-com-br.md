---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Advplan Com Br Agentic Access
  operation_count: 30
  slug: advplan-com-br-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 1
apis:
- baseURL: https://lp.advplan.com.br
  baseurl_source: declared
  description: Processos e casos, com linha do tempo e fases
  name: AdvPlan Casos API
  slug: advplan-com-br-casos-api
- baseURL: https://lp.advplan.com.br
  baseurl_source: declared
  description: Cadastro de clientes do escritório
  name: AdvPlan Clientes API
  slug: advplan-com-br-clientes-api
- baseURL: https://lp.advplan.com.br
  baseurl_source: declared
  description: Honorários e despesas
  name: AdvPlan Cobranças API
  slug: advplan-com-br-cobran-as-api
- baseURL: https://lp.advplan.com.br
  baseurl_source: declared
  description: Documentos do caso e geração a partir de modelos
  name: AdvPlan Documentos API
  slug: advplan-com-br-documentos-api
- baseURL: https://lp.advplan.com.br
  baseurl_source: declared
  description: Prazos processuais. Criar prazo pela API NÃO dispensa a aprovação humana no painel.
  name: AdvPlan Prazos API
  slug: advplan-com-br-prazos-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/advplan-com-br/agentic-access/advplan-com-br-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/advplan-com-br-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/advplan-com-br/rules/advplan-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/advplan-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/advplan-com-br/vocabulary/advplan-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/advplan-com-br-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/advplan-com-br/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/advplan-com-br/errors/advplan-com-br-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/advplan-com-br-problem-types.yml
- group: design
  href: https://artifacts.apis.io/advplan-com-br/conformance/advplan-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/advplan-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/advplan-com-br/llms/advplan-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/advplan-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/advplan-com-br/well-known/advplan-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/advplan-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/advplan-com-br/hosts/advplan-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/advplan-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/advplan-com-br/vendors/advplan-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/advplan-com-br-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.advplan.com.br/
- group: auth
  href: https://artifacts.apis.io/advplan-com-br/security/advplan-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/advplan-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advplan.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://advplan.com.br/docs
- group: docs
  title: ''
  type: APIReference
  url: https://advplan.com.br/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://advplan.com.br/cadastro
- group: operate
  title: ''
  type: Support
  url: mailto:contato@advplan.com.br
- group: commercial
  title: ''
  type: Pricing
  url: https://advplan.com.br/quanto-custa-software-juridico
- group: start
  title: ''
  type: SignUp
  url: https://advplan.com.br/cadastro
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.advplan.com.br/mcp
  - status: 200
    url: https://advplan.com.br/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: AdvPlan is a Brazilian legal‑tech platform that uses artificial intelligence to assist lawyers in managing cases, deadlines, documents, finances and client communications. The system reads publications from the DJEN (Diário de Justiça Eletrônico Nacional), automatically calculates deadlines accounting for holidays and suspensions, and presents suggested actions for attorney approval. It integrates WhatsApp, calendar sync, and offers a free 14‑day trial without requiring a credit card. AdvPlan aims to reduce operational risk for law firms by centralising workflow in a single web‑based interface.
image: https://advplan.com.br/images/advplan/og-image.png
layout: provider
modified: '2026-10-31'
name: AdvPlan
nav: Providers
network: true
overview: 'AdvPlan publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Casos API, Clientes API, Cobranças API, and 2 more. Tagged areas include Legal Tech, Artificial Intelligence, Software, Brazil, and LawPractice.


  The AdvPlan catalog on APIs.io includes 1 Spectral governance ruleset.


  AdvPlan''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, and 13 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AdvPlan API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: advplan-com-br-rules
scopes:
- name: Advplan Com Br Scopes
  scope_count: 0
  slug: advplan-com-br-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 30.2
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Advplan Com Br Authentication
  slug: advplan-com-br-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Advplan Com Br Domain Security
  slug: advplan-com-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: create-case
  slug: advplan-com-br-create-case
- name: list-cases
  slug: advplan-com-br-list-cases
slug: advplan-com-br
tags:
- Legal Tech
- Artificial Intelligence
- Software
- Brazil
- LawPractice
website: https://advplan.com.br/
---
