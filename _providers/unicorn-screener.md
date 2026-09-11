---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: HTTP JSON API, 4 paths in the served OpenAPI 3.1; a keyless agent lookup answers live.
  name: Unicorn Screener API
  slug: unicorn-screener-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unicorn-screener-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unicornscreener.vc
- group: start
  title: ''
  type: DeveloperPortal
  url: https://unicornscreener.vc/docs/ai-agents
- group: company
  title: ''
  type: Blog
  url: https://unicornscreener.vc/blog
- group: operate
  title: ''
  type: Support
  url: https://unicornscreener.vc/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unicornscreener.vc/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unicornscreener.vc/privacy-policy
created: '2026-09-10'
description: 'Startup research and screening over an HTTP JSON API: resolve a company name, look up a startup score and summary, request an asynchronous screening, and follow its status to a permanent web memo. For early-stage company research and comparison.'
image: https://unicornscreener.vc/opengraph-image?9ac05864e0a0ce88
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived from the public keyless Unicorn Screener Agent API. Nobody ships an MCP server today; these tools map 1:1 to the OpenAPI operations an agent can already call over pl
  name: Unicorn Screener (candidate MCP)
  slug: unicorn-screener-candidate-mcp
modified: '2026-09-10'
name: Unicorn Screener
nav: Providers
network: true
overview: 'Unicorn Screener publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Venture Capital, Startups, Company Research, Screening, and Investing.


  Unicorn Screener''s developer surface includes engineering blog, support, and 5 more developer resources.'
plans:
- name: Unicorn Screener Plans Pricing
  plan_count: 3
  slug: unicorn-screener-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Unicorn Screener Rate Limits
  slug: unicorn-screener-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 58.0
    catalog_earned_first_party: 24.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 39.9
    discoverability: 70.4
    governance: 0.0
    operational_transparency: 31.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Unicorn Screener Authentication
  slug: unicorn-screener-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Unicorn Screener Domain Security
  slug: unicorn-screener-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unicorn-screener
tags:
- Venture Capital
- Startups
- Company Research
- Screening
- Investing
- AI Agents
website: https://unicornscreener.vc
---
