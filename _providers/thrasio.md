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
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.thrasio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.thrasio.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thrasio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thrasio.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.thrasio.com/hc/en-us/p/Privacy-Policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.thrasio.com/accessibility
- group: company
  title: ''
  type: Careers
  url: https://www.thrasio.com/company/careers
- group: company
  title: ''
  type: Partners
  url: https://www.thrasio.com/commercial-opportunities
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thrasio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/thrasio
- group: other
  title: ''
  type: StockProfile
  url: https://forgeglobal.com/thrasio_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thrasio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thrasio-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Thrasio is an Amazon-marketplace brand aggregator selling physical consumer goods; api./developer./docs.thrasio.com do not resolve at all, and its only public GitHub repos are a CircleCI Helm chart and a forked Ruby gem.
  evidence:
  - status: 404
    url: https://www.thrasio.com/developers
  - status: 404
    url: https://www.thrasio.com/openapi.json
  - status: 404
    url: https://www.thrasio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.thrasio.com/llms.txt
  - status: 0
    url: https://api.thrasio.com/
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Thrasio is a consumer products company founded in 2018 and headquartered in Walpole, Massachusetts, that acquires and operates e-commerce-native consumer brands — principally Amazon marketplace sellers — and then scales them with data science, supply-chain and marketing operations. The company states it is one of Amazon''s top five sellers, that its products reach more than 80 million households, and that it sells across 150+ retailers. Thrasio is a brand aggregator and operator rather than a software vendor: it publishes no developer portal, no public API, no SDKs and no machine-readable specifications, and its own marketplace integrations run over Amazon''s Selling Partner API rather than over any Thrasio-published interface.'
layout: provider
modified: '2026-08-05'
name: Thrasio
nav: Providers
network: true
overview: 'Thrasio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Consumer Goods, Retail, and Marketplace.


  Thrasio''s developer surface includes engineering blog, YouTube channel, and 11 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Thrasio Domain Security
  slug: thrasio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thrasio
tags:
- Company
- E-Commerce
- Consumer Goods
- Retail
- Marketplace
- Brands
- Amazon
website: https://www.thrasio.com/
---
