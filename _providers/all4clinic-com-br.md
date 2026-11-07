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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted Model Context Protocol server exposing tools for All4Clinic.
  name: All4Clinic MCP Server
  slug: all4clinic-mcp
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/all4clinic-com-br/llms/all4clinic-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/all4clinic-com-br-llms.txt
- group: other
  href: https://artifacts.apis.io/all4clinic-com-br/hosts/all4clinic-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/all4clinic-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/all4clinic-com-br/vendors/all4clinic-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/all4clinic-com-br-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://api.all4clinic.com.br/admin/login
- group: auth
  href: https://artifacts.apis.io/all4clinic-com-br/security/all4clinic-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/all4clinic-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://all4clinic.com.br/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://all4clinic.com.br/termos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://all4clinic.com.br/privacidade/
- group: commercial
  title: ''
  type: Pricing
  url: https://all4clinic.com.br/planos/
created: '2026-11-01'
description: 'Sistema de gestão para clínicas com IA de verdade: agenda multi-profissional, prontuário com transcrição da consulta, documentos com assinatura digital ICP-Brasil, cobrança do paciente por Pix, boleto e cartão, estoque com lote e validade, CRM e oito automações de WhatsApp. Dados no Brasil, conformidade com a LGPD.'
image: https://all4clinic.com.br/brand/logo-medsystem.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.all4clinic.com.br.
  name: All4Clinic MCP Server
  slug: all4clinic-com-br-mcp-yml
modified: '2026-11-01'
name: All4Clinic
nav: Providers
network: true
overview: 'All4Clinic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Clinic Management, Artificial Intelligence, Brazil, and Software-as-a-Service.


  All4Clinic''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: All4Clinic Com Br Plans Pricing
  plan_count: 0
  slug: all4clinic-com-br-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: All4Clinic Com Br Rate Limits
  slug: all4clinic-com-br-rate-limits
scopes:
- name: All4Clinic Com Br Scopes
  scope_count: 0
  slug: all4clinic-com-br-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 17.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: All4Clinic Com Br Authentication
  slug: all4clinic-com-br-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: All4Clinic Com Br Domain Security
  slug: all4clinic-com-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: all4clinic-com-br
tags:
- Healthcare
- Clinic Management
- Artificial Intelligence
- Brazil
- Software-as-a-Service
website: https://all4clinic.com.br/
---
