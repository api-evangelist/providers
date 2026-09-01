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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mubi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mubi.com/
- group: operate
  title: ''
  type: Support
  url: https://help.mubi.com/
- group: company
  title: ''
  type: Blog
  url: https://mubi.com/en/notebook
- group: commercial
  title: ''
  type: Pricing
  url: https://mubi.com/en/us/memberships
- group: start
  title: ''
  type: SignUp
  url: https://mubi.com/en/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mubi.com/en/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mubi.com/en/privacy_policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mubi
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/mubi-stock
coverage:
  checked: '2026-08-04'
  detail: MUBI ships an end-user streaming product only — developer.mubi.com and docs.mubi.com do not resolve, mubi.com/developers 404s, and no OpenAPI, GraphQL, MCP, agent card or llms.txt is served on mubi.com, api.mubi.com, help.mubi.com or feeds.mubi.com; the api.mubi.com host that backs MUBI's own web/mobile/TV clients is undocumented and answers with "CLIENT_COUNTRY HTTP HEADER is required" rather than any published contract.
  evidence:
  - status: 404
    url: https://mubi.com/developers
  - status: 404
    url: https://api.mubi.com/openapi.json
  - status: 404
    url: https://api.mubi.com/graphql
  - status: 422
    url: https://api.mubi.com/v3/films
  - status: 404
    url: https://mubi.com/.well-known/agent-card.json
  - status: 302
    url: https://mubi.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-04'
description: MUBI is a London-headquartered global streaming service, film distributor and production company founded in 2007 by Efe Cakarel (originally as The Auteurs, rebranded MUBI in 2010). It operates a curated subscription video-on-demand service for arthouse, independent, documentary and world cinema across more than 190 countries, alongside MUBI GO (weekly cinema tickets), the Notebook film-criticism publication and print magazine, MUBI Editions, a merchandise shop, and theatrical distribution and sales arms including The Match Factory and Cineart. MUBI publishes no public developer program, API documentation, or machine-readable specification; the api.mubi.com host serves its own first-party web, mobile and TV clients only.
image: https://assets.mubicdn.net/splash/volver.jpg
layout: provider
modified: '2026-08-04'
name: MUBI
nav: Providers
network: true
overview: 'MUBI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Streaming, Media, Entertainment, and Film.


  MUBI''s developer surface includes support, engineering blog, pricing, signup flow, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Mubi Domain Security
  slug: mubi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mubi
tags:
- Company
- Streaming
- Media
- Entertainment
- Film
- Video-on-Demand
- Subscription
- Distribution
website: https://mubi.com/
---
