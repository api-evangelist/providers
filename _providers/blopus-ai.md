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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Blopus.ai provides a web search API for AI agents, offering fresh structured search results and image search.
  name: Blopus Search API
  slug: blopus-search-api
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/blopus-ai/changelog/blopus-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blopus-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/blopus-ai/security/blopus-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/blopus-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blopus-ai/authentication/blopus-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blopus-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/blopus-ai/well-known/blopus-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blopus-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/blopus-ai/well-known/blopus-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blopus-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/blopus-ai/hosts/blopus-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blopus-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/blopus-ai/vendors/blopus-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blopus-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/blopus-ai/packages/blopus-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/blopus-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/blopus-ai/packages/blopus-ai-packages.yml
  title: ''
  type: Packages
  url: packages/blopus-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blopus.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blopus.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://blopus.ai/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blopus-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://blopus.ai/docs/changelog
- group: auth
  href: https://artifacts.apis.io/blopus-ai/security/blopus-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blopus-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blopus-ai/security/blopus-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blopus-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blopus.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://blopus.ai/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://blopus.ai/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://blopus.ai/docs/support
- group: commercial
  title: ''
  type: Pricing
  url: https://blopus.ai/docs/limits
coverage:
  checked: '2026-10-30'
  detail: Documentation pages exist but no OpenAPI or other machine-readable contract was found.
  evidence:
  - status: 404
    url: https://blopus.ai/docs/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Blopus.ai provides a web search API and MCP server designed for AI agents and large language models. It offers a single REST endpoint and an MCP-compatible interface, delivering fresh, structured search results from its own continuously crawled index. The service includes features like image search, rate limits, billing plans, and comprehensive documentation for developers.
image: https://blopus.ai/assets/og-blopus.png
layout: provider
modified: '2026-10-30'
name: blopus-ai
nav: Providers
network: true
overview: 'blopus-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Search, API, and MCP.


  blopus-ai''s developer surface includes changelog, authentication, documentation, getting-started guide, support, pricing, and 15 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 31.6
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
- kind: authentication
  name: Blopus Ai Authentication
  slug: blopus-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blopus Ai Domain Security
  slug: blopus-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blopus Ai Vulnerability Disclosure
  slug: blopus-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blopus-ai
tags:
- Company
- AI
- Search
- API
- MCP
website: https://blopus.ai/
---
