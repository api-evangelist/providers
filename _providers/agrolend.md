---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://agrolend.agr.br/quem-somos/
- group: operate
  title: ''
  type: Support
  url: https://agrolend.agr.br/contato/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agrolend
- group: company
  title: ''
  type: Blog
  url: https://agrolend.agr.br/informativo-agrolend/
- group: auth
  title: ''
  type: Compliance
  url: https://agrolend.agr.br/relatorios/
- group: auth
  title: ''
  type: Security
  url: https://agrolend.agr.br/wp-content/uploads/2026/07/AGROLEND-CIBERSEGURANCA_FEV26.pdf
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agrolend/refs/heads/main/conformance/agrolend-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agrolend-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrolend/refs/heads/main/security/agrolend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrolend-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrolend/refs/heads/main/llms/agrolend-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agrolend-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agrolend/refs/heads/main/plans/agrolend-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agrolend-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agrolend/refs/heads/main/rate-limits/agrolend-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agrolend-rate-limits.yml
coverage:
  checked: '2026-09-13'
  detail: 'The only Agrolend API host, parceiro.agrolend.agr.br, sits behind blanket HTTP Basic auth and returns 401 with WWW-Authenticate: Basic on every path including /v3/api-docs and /openapi.json, while the docs.agrolend.agr.br and portal.agrolend.agr.br subdomains that would have carried the reference have been dead since their wildcard certificate expired on 2025-03-06 and now return 504 from an empty load balancer.'
  evidence:
  - status: 401
    url: https://parceiro.agrolend.agr.br/
  - status: 401
    url: https://parceiro.agrolend.agr.br/v3/api-docs.yaml
  - status: 504
    url: https://docs.agrolend.agr.br/
  - status: 504
    url: https://portal.agrolend.agr.br/
  - status: 404
    url: https://agrolend.agr.br/.well-known/api-catalog
  - status: 200
    url: https://data.directory.openbankingbrasil.org.br/participants
  reason: partner-login
  state: gated
created: '2026-09-13'
description: Agrolend is a Brazilian agricultural-credit fintech — legally Agrolend Sociedade de Credito, Financiamento e Investimento S/A (CNPJ 43.774.196/0001-84), a Banco Central do Brasil regulated SCFI headquartered in Sao Paulo. Founded in 2020, it originates working capital, receivables discount, liability-extension and inter-chain credit for small and mid-sized rural producers, distributing through agricultural retailers, cooperatives and input industries rather than direct to farm, and funds the book partly through FGC-covered LCA notes sold on third-party investment platforms. Its stated differentiator is a cloud-native, AI-assisted credit engine that underwrites without requiring farm or grain collateral. Agrolend publishes no developer portal, no API reference and no machine-readable contract; the only API surface reachable from the public internet is the partner-area backend at parceiro.agrolend.agr.br, which answers HTTP Basic 401 on every path.
image: https://agrolend.agr.br/wp-content/uploads/2023/05/Logo-Agrolend.png
layout: provider
modified: '2026-09-13'
name: Agrolend
nav: Providers
network: true
overview: 'Agrolend is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Financial-Services, and Lending.


  Agrolend''s developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Agrolend Plans Pricing
  plan_count: 0
  slug: agrolend-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Agrolend Rate Limits
  slug: agrolend-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 11.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 20.3
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agrolend Domain Security
  slug: agrolend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agrolend
tags:
- Company
- Agriculture
- AgTech
- Financial-Services
- Lending
- Credit
- Fintech
- Brazil
- Rural Finance
- Banking
website: https://agrolend.agr.br/quem-somos/
---
