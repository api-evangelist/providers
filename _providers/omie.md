---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/omie/refs/heads/main/llms/omie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/omie-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/omie/refs/heads/main/well-known/omie-ajuda-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/omie-ajuda-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/omie/refs/heads/main/well-known/omie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/omie-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omie/refs/heads/main/hosts/omie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/omie-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omie/refs/heads/main/vendors/omie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/omie-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.omie.com.br/blog/pricing-e-markup-definir-melhor-preco-de-venda-de-servicos/
- group: company
  title: ''
  type: Newsroom
  url: https://www.omie.com.br/news/contabilidade-8-min/
- group: start
  title: ''
  type: Login
  url: https://app.omie.com.br/login/
- group: company
  title: ''
  type: Blog
  url: https://blog.omie.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.omie.com.br/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/omie/refs/heads/main/security/omie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/omie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.omie.com.br
coverage:
  checked: '2026-10-14'
  detail: Developer portal pages load content via JavaScript, preventing static retrieval of machine‑readable specifications.
  evidence:
  - status: 200
    url: https://developer.omie.com.br/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Omie is a Brazilian cloud-based ERP and financial management platform for small and medium-sized businesses. It offers integrated modules for accounting, invoicing, inventory, sales, purchasing, and cash flow management, all accessible via a web interface and mobile apps. The service emphasizes automation of tax compliance, real-time reporting, and integration with banking and e‑commerce solutions, helping companies streamline operations and improve financial visibility.
layout: provider
modified: '2026-10-14'
name: Omie
nav: Providers
network: true
overview: 'Omie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, Finance, Software-as-a-Service, Brazil, and Small Business.


  Omie''s developer surface includes pricing, engineering blog, documentation, and 9 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Omie Domain Security
  slug: omie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: omie
tags:
- ERP
- Finance
- Software-as-a-Service
- Brazil
- Small Business
website: https://www.omie.com.br
---
