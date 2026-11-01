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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Trakis provides an audit and compliance platform; API details are not publicly documented.
  name: Trakis API
  slug: trakis-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/trakis-io/security/trakis-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/trakis-io-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/trakis-io/llms/trakis-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trakis-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/trakis-io/mcp/trakis-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trakis-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/trakis-io/well-known/trakis-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/trakis-io-security.txt
- group: agent
  href: https://artifacts.apis.io/trakis-io/well-known/trakis-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trakis-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/trakis-io/hosts/trakis-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trakis-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/trakis-io/vendors/trakis-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trakis-io-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://trakis.io/blog
- group: auth
  href: https://artifacts.apis.io/trakis-io/security/trakis-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trakis-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/trakis-io/security/trakis-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trakis-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trakis.io/
- group: docs
  title: ''
  type: Documentation
  url: https://trakis.io/rules
- group: operate
  title: ''
  type: Support
  url: https://trakis.io/bot
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trakis.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trakis.io/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://trakis.io/about
- group: start
  title: ''
  type: SignUp
  url: https://trakis.io/signup
created: '2026-10-30'
description: Trakis provides a free SEO audit tool for small websites, counting each SEO problem once and showing which pages are affected. It offers a simple interface to generate reports, integrates with AI assistants, and aims to help site owners and agencies quickly identify and fix issues. The service is free, with optional sign‑up via Google or email, and delivers audit results within an hour.
image: https://trakis.io/og.png?v=e
layout: provider
mcp_servers:
- description: Remote MCP server at trakis.io.
  name: trakis-io MCP Server
  slug: trakis-io-mcp-yml
modified: '2026-10-30'
name: trakis-io
nav: Providers
network: true
overview: 'trakis-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SEO, Audit, Free, and AI.


  trakis-io''s developer surface includes engineering blog, documentation, support, getting-started guide, signup flow, and 12 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trakis Io Domain Security
  slug: trakis-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trakis Io Vulnerability Disclosure
  slug: trakis-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: trakis-io
tags:
- Company
- SEO
- Audit
- Free
- AI
website: https://trakis.io/
---
