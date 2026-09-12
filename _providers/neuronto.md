---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-12'
api_count: 1
apis:
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: 'Search, explore and audit Agentic Resource Discovery entries: MCP servers, A2A agents, OpenAPI services and documentation. REST, MCP and A2A answer from one index. No key, no signup.'
  name: Neuronto ARD Registry API
  slug: ard-registry
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neuronto-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/neuronto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/neuronto-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/neuronto-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/neuronto-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neuronto-llms.txt
- group: company
  title: ''
  type: Website
  url: https://neuronto.com
- group: design
  title: ''
  type: Conformance
  url: conformance/neuronto-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neuronto-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/neuronto-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/neuronto-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/neuronto-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/neuronto-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://neuronto.com/pricing
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neuronto-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://neuronto.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://neuronto.com/feed.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://neuronto.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://neuronto.com/publish
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neuronto
created: '2026-08-31'
description: Agentic Resource Discovery (ARD) index. One search covers this index and every other public ARD registry, and results carry the tools each MCP server actually exposes, read from its own tools/list. The index holds 15,412 resources from 6,926 publishers, 14,522 verified to respond, and answers over REST, MCP and A2A with no key and no signup.
image: https://neuronto.com/icon.svg
layout: provider
mcp_servers:
- description: Official hosted MCP server for the Neuronto ARD Registry. tools/list answered a live anonymous POST on 2026-09-07 (HTTP 200, application/json) with 4 tools; the response is saved verbatim in neuronto-
  name: Neuronto ARD Registry MCP Server
  slug: neuronto-ard-registry-mcp-server
modified: '2026-09-07'
name: Neuronto ARD Registry
nav: Providers
network: true
overview: 'Neuronto ARD Registry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agentic Resource Discovery, ARD, MCP, A2A, and API Discovery.


  Neuronto ARD Registry''s developer surface includes CLI, authentication, pricing, engineering blog, getting-started guide, and 16 more developer resources.'
plans:
- name: Neuronto Plans Pricing
  plan_count: 4
  slug: neuronto-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Neuronto Rate Limits
  slug: neuronto-rate-limits
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 58.0
    catalog_earned_first_party: 24.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 39.6
    developer_ergonomics: 51.8
    discoverability: 70.4
    operational_transparency: 34.2
  previous_composite: 43.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Neuronto Authentication
  slug: neuronto-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Neuronto Domain Security
  slug: neuronto-domain-security
  summary_line: TLSv1.3 · HSTS
slug: neuronto
tags:
- Agentic Resource Discovery
- ARD
- MCP
- A2A
- API Discovery
- Registry
website: https://neuronto.com
---
