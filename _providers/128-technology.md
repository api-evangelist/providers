---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The northbound API of the Juniper Session Smart Router (SSR) and Session Smart Conductor. A YANG-modeled configuration and state tree is exposed over a REST API rooted at /api/v1, an equivalent GraphQ
  name: Session Smart Router REST and GraphQL API
  slug: 128-technology-ssr-api
artifact_total: 6
asyncapis:
- description: ''
  name: 128 Technology Event Surface
  slug: 128-technology-event-surface
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/128-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.juniper.net/us/en/products/routers/session-smart-router.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.128technology.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.128technology.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.128technology.com/docs/intro_rest_graphql_apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.128technology.com/docs/intro_installation_overview
- group: operate
  title: ''
  type: Support
  url: https://docs.128technology.com/kb
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/128technology
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.128technology.com/docs/release_notes_128t_7.2
- group: operate
  title: ''
  type: Deprecation
  url: https://support.juniper.net/support/eol/software/ssr/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.128technology.com/docs/cc_fips_intro
- group: build
  title: ''
  type: Packages
  url: packages/128-technology-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/128-technology-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/128-technology-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/128-technology-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/128-technology-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/128-technology-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/128-technology-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/128-technology-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/128-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/128-technology-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/128-technology-llms.txt
created: '2026-09-05'
description: '128 Technology is the Burlington, Massachusetts networking company behind the Session Smart Networking platform — a 100% software-defined, session-aware IP routing and network services stack built on Secure Vector Routing (SVR), a tunnel-free routing protocol. The platform pairs the Session Smart Router (SSR) data/control plane with the Session Smart Conductor, a centralized management, policy and provisioning engine. Juniper Networks acquired 128 Technology in 2020 for $450M and the product line now ships as the Juniper Session Smart Router, but 128 Technology remains the operating identity of the developer surface: the product documentation is still served from docs.128technology.com and the open-source libraries are still published under the github.com/128technology organization and the @128technology npm scope. The SSR exposes a YANG-modeled configuration and state tree over a REST API (/api/v1), a GraphQL API, and NETCONF — all served by the customer''s own deployed router
  or conductor rather than from a vendor-hosted cloud endpoint.'
image: https://avatars.githubusercontent.com/u/13588912?v=4
layout: provider
modified: '2026-09-05'
name: 128 Technology
nav: Providers
network: true
overview: '128 Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, SD-WAN, Routing, and Network Management.


  The 128 Technology catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  128 Technology''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, CLI, and 15 more developer resources.'
plans:
- name: 128 Technology Plans Pricing
  plan_count: 0
  slug: 128-technology-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: 128 Technology Rate Limits
  slug: 128-technology-rate-limits
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 128 Technology Authentication
  slug: 128-technology-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 128 Technology Domain Security
  slug: 128-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 128-technology
tags:
- Company
- Networking
- SD-WAN
- Routing
- Network Management
- Session Smart Networking
- NETCONF
- YANG
- Telecommunications
- Infrastructure
website: https://www.juniper.net/us/en/products/routers/session-smart-router.html
---
