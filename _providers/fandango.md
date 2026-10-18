---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: GraphQL API for Fandango services such as redeem and store.
  name: GraphQL API
  slug: graphql-api
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fandango/refs/heads/main/llms/fandango-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fandango-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fandango/refs/heads/main/mcp/fandango-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fandango-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fandango/refs/heads/main/well-known/fandango-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fandango-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fandango/refs/heads/main/hosts/fandango-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fandango-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fandango/refs/heads/main/vendors/fandango-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fandango-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fandango.com/policies/terms-and-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fandango.com/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fandango
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fandango/refs/heads/main/security/fandango-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fandango-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fandango.com
- group: operate
  title: ''
  type: Support
  url: https://support.fandango.com
coverage:
  checked: '2026-10-13'
  detail: GraphQL schema requires authentication, preventing unauthenticated access.
  evidence:
  - status: 200
    url: https://redeem.fandango.com/api/graphql
  reason: partner-login
  state: gated
created: '2026-10-13'
description: Fandango is a leading online ticketing platform for movies, offering users the ability to browse showtimes, purchase tickets, and discover entertainment content. The company provides a consumer-facing website and mobile apps, and exposes APIs for partners to integrate ticketing, pricing, and promotional features into their services. Fandango’s services include movie listings, theater information, ticket sales, gift cards, and loyalty programs, serving millions of moviegoers across the United States.
image: https://images.fandango.com/mobile/web/img/assets/logo-fandango.svg
layout: provider
mcp_servers:
- description: Remote MCP server at fandango-media.myshopify.com.
  name: Fandango MCP Server
  slug: fandango-mcp-yml
modified: '2026-10-13'
name: Fandango
nav: Providers
network: true
overview: 'Fandango is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Entertainment, Ticketing, and Movies.


  Fandango''s developer surface includes support and 10 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.7
    operational_transparency: 5.3
  provenance:
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fandango Domain Security
  slug: fandango-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fandango
tags:
- Company
- Entertainment
- Ticketing
- Movies
website: https://www.fandango.com
---
