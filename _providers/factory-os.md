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
  url: security/factory-os-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/factory-os-llms.txt
- group: company
  title: ''
  type: Website
  url: https://harbinger.homes/
- group: company
  title: ''
  type: FormerWebsite
  url: https://factoryos.com/
- group: operate
  title: ''
  type: Contact
  url: https://harbinger.homes/contact
- group: company
  title: ''
  type: Careers
  url: https://recruiting.paylocity.com/recruiting/jobs/All/f6d0f7bd-df42-43ee-8899-f5e5bc26297e/Harbinger-Production-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harbinger-production/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/factoryos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/factoryos
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/factory-os_stock/
coverage:
  checked: '2026-08-12'
  detail: Factory OS manufactures physical wood-frame housing modules on an assembly line in Vallejo, California — after its May 2024 rename to Harbinger Homes, factoryos.com 301-redirects every path (including /api, /docs, /developers and all /.well-known/*) to harbinger.homes, which is a two-URL Framer marketing brochure whose own sitemap.xml lists only / and /contact, and where /openapi.json, /graphql, /llms.txt and every /.well-known/ path return a real 404; no api./docs./developer. subdomain resolves on either domain, and the company's own GitHub organization has no public repositories.
  evidence:
  - status: 301
    url: https://factoryos.com/openapi.json
  - status: 404
    url: https://harbinger.homes/openapi.json
  - status: 404
    url: https://harbinger.homes/graphql
  - status: 404
    url: https://harbinger.homes/llms.txt
  - status: 404
    url: https://harbinger.homes/.well-known/agent-card.json
  - status: 404
    url: https://harbinger.homes/.well-known/security.txt
  - status: 200
    url: https://harbinger.homes/sitemap.xml
  - status: 200
    url: https://harbinger.homes/
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Factory OS (styled Factory_OS) is an off-site construction company founded in 2017 by Rick Holliday and Larry Pace that industrialized multifamily and affordable housing production on an assembly line inside a 275,000-square-foot facility in Building 680 on Mare Island in Vallejo, California. Union carpenters build wood-frame housing modules across roughly two dozen stations in a 33-step process, and the finished modules are trucked to the project site and assembled — an approach the company says cuts production time by about half and production cost by a quarter against conventional site-built construction. It raised roughly $132 million across three rounds, including $60 million from JPMorgan Chase and Saint-Gobain in 2021, and delivered more than 4,000 homes across California and Hawaii, about 90 percent of them affordable housing. In May 2024 the company was recapitalized and renamed Harbinger Homes (legal entity Harbinger Production Inc.), with Tom Smith as CEO and Kevin
  Brown as president; factoryos.com now 301-redirects every path to harbinger.homes. Harbinger filed a WARN notice on 12 February 2026 covering all 280 employees, citing a lack of new business and loss of capital funding, with layoffs beginning 13 April 2026. Factory OS is a manufacturer of physical housing modules, not a software company: it operates no developer program, API, SDK, webhook surface or machine-readable specification of any kind, and its GitHub organization has no public repositories.'
image: https://framerusercontent.com/images/dGrxSMGKQjOw59MximONvOdWOU.jpg
layout: provider
modified: '2026-08-12'
name: Factory OS
nav: Providers
network: true
overview: Factory OS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Modular Construction, Offsite Construction, and Manufacturing.
random_paper: 2
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Factory Os Domain Security
  slug: factory-os-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: factory-os
tags:
- Company
- Construction
- Modular Construction
- Offsite Construction
- Manufacturing
- Affordable Housing
- Multifamily Housing
- Real-Estate
- Construction Technology
website: https://harbinger.homes/
---
