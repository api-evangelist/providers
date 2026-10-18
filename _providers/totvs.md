---
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Developer portal providing documentation for TOTVS APIs.
  name: TOTVS Developer Portal
  slug: totvs-developer-portal
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/totvs/refs/heads/main/hosts/totvs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/totvs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/totvs/refs/heads/main/vendors/totvs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/totvs-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/totvs/refs/heads/main/packages/totvs-packages.yml
  title: ''
  type: SDKs
  url: packages/totvs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/totvs/refs/heads/main/packages/totvs-packages.yml
  title: ''
  type: Packages
  url: packages/totvs-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.totvs.com/blog/gestao-para-assinatura-de-documentos/webhook/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.totvs.com/blog/gestao-varejista/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.totvs.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/totvs
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/totvs/refs/heads/main/security/totvs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/totvs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.totvs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.totvs.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.totvs.com/developers
- group: operate
  title: ''
  type: Support
  url: https://www.totvs.com/contato/
coverage:
  checked: '2026-10-14'
  detail: Developer portal pages return HTML without any OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://developers.totvs.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: TOTVS is a Brazilian technology company offering software solutions for management, ERP, cloud, and digital transformation across various industries. It provides platforms for enterprise resource planning, human resources, finance, logistics, and more, serving large enterprises and SMEs in Brazil and internationally. The company emphasizes innovation, AI, and integrated services, with a strong focus on digital ecosystems and customer support.
image: https://www.totvs.com/imagens/image-share.jpg
layout: provider
modified: '2026-10-13'
name: TOTVS
nav: Providers
network: true
overview: 'TOTVS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, ERP, Cloud, and Brazil.


  TOTVS''s developer surface includes pricing, engineering blog, documentation, support, and 9 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Totvs Domain Security
  slug: totvs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: totvs
tags:
- Company
- Technology
- ERP
- Cloud
- Brazil
website: https://www.totvs.com
---
