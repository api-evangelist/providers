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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fintech-farm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fintech-farm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fintech-farm.com/
- group: auth
  title: ''
  type: Security
  url: https://www.fintech-farm.com/security
- group: operate
  title: ''
  type: Support
  url: mailto:hello@fintech-farm.com
- group: company
  title: ''
  type: Blog
  url: https://www.fintech-farm.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fintech-Farm-Ltd
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fintech-farm-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fintech-farm-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fintech-farm-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/fintech-farm-plans-pricing.yml
coverage:
  checked: '2026-08-12'
  detail: 'Fintech Farm sells bank partnerships, not API access — it builds and operates a neobank jointly with a licensed local bank — so there is no developer portal, no API reference and no API host at all: api.fintech-farm.com, developers.fintech-farm.com and docs.fintech-farm.com are all NXDOMAIN, and the only non-public surface, dev.fintech-farm.com, answers HTTP 401 behind HTTP Basic auth.'
  evidence:
  - status: 404
    url: https://www.fintech-farm.com/developers
  - status: 404
    url: https://www.fintech-farm.com/openapi.json
  - status: 401
    url: https://dev.fintech-farm.com/
  - status: 200
    url: https://www.fintech-farm.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: Fintech Farm is a London-based fintech company that builds and operates credit-led digital banks (neobanks) in emerging markets in partnership with licensed local banks. Founded in 2020 by Dmytro Dubilet (co-founder of Monobank), Nick Bezkrovnyy and Oleksandr Vityaz, the company supplies an end-to-end stack — mobile banking apps, an AI-driven credit engine and credit-risk models, customer acquisition and retention programs, and customer service operations — and is compensated on the performance of the resulting bank. Its launches include Leobank in Azerbaijan, Liobank in Vietnam, Simbank with DosCredoBank in Kyrgyzstan, Roarbank with Unity Bank in India, Tez with Hamkorbank in Uzbekistan, and Credit+ in Morocco. Fintech Farm is a business-to-business bank-partnership provider and publishes no public developer program, API documentation or machine-readable API contract; its integration surface is delivered privately to partner banks.
image: https://fintech-farm.com/opengraph-image.jpg
layout: provider
modified: '2026-08-12'
name: Fintech Farm
nav: Providers
network: true
overview: 'Fintech Farm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial-Services, Neobank, and Digital Banking.


  Fintech Farm''s developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Fintech Farm Plans Pricing
  plan_count: 0
  slug: fintech-farm-plans-pricing
random_paper: 7
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Fintech Farm Domain Security
  slug: fintech-farm-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Fintech Farm Vulnerability Disclosure
  slug: fintech-farm-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: fintech-farm
tags:
- Company
- Banking
- Financial-Services
- Neobank
- Digital Banking
- Fintech
- Credit
- Emerging Markets
- Banking as a Service
- Mobile Banking
website: https://www.fintech-farm.com/
---
