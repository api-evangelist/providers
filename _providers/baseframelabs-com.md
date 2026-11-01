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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer tools API suite documented at the ProjScan docs page.
  name: Baseframe Labs API
  slug: baseframe-labs-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/baseframelabs-com/security/baseframelabs-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/baseframelabs-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/baseframelabs-com/llms/baseframelabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/baseframelabs-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/baseframelabs-com/mcp/baseframelabs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/baseframelabs-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/baseframelabs-com/well-known/baseframelabs-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/baseframelabs-com-security.txt
- group: auth
  href: https://artifacts.apis.io/baseframelabs-com/well-known/baseframelabs-com-baseframelabs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/baseframelabs-com-baseframelabs-security.txt
- group: agent
  href: https://artifacts.apis.io/baseframelabs-com/well-known/baseframelabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/baseframelabs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/baseframelabs-com/hosts/baseframelabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baseframelabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/baseframelabs-com/vendors/baseframelabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baseframelabs-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abhiyoheswaran1
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.baseframelabs.com/apps/projscan/changelog
- group: auth
  href: https://artifacts.apis.io/baseframelabs-com/security/baseframelabs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/baseframelabs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/baseframelabs-com/security/baseframelabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baseframelabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baseframelabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.baseframelabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.baseframelabs.com/apps/projscan/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.baseframelabs.com/apps/projscan/docs
- group: operate
  title: ''
  type: Support
  url: https://www.baseframelabs.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baseframelabs.com/apps/nightmark/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baseframelabs.com/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are served as a JavaScript single-page app, preventing machine‑readable extraction of an OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.baseframelabs.com/apps/projscan/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Baseframe Labs is an independent software studio focused on developer tools. It builds local, deterministic tools that surface the real state of a codebase, enabling trust in code changes. The studio offers a suite of products including ProjScan, AgentLoopKit, AgentFlight, VerisKit, TokenTrace, Swiss Auto Data, EndpointOS, CampaignPacks, Nightmark, and SparkPath, providing market data, API infrastructure, and daily utilities for engineers.
image: https://www.baseframelabs.com/opengraph-image?e1aa2bdc551ad0c7
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.baseframelabs.com.
  name: baseframelabs-com MCP Server
  slug: baseframelabs-com-mcp-yml
modified: '2026-10-30'
name: baseframelabs-com
nav: Providers
network: true
overview: 'baseframelabs-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Software Studio, Independent, and Open Source.


  baseframelabs-com''s developer surface includes changelog, documentation, getting-started guide, support, and 15 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 56.7
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baseframelabs Com Domain Security
  slug: baseframelabs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Baseframelabs Com Vulnerability Disclosure
  slug: baseframelabs-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: baseframelabs-com
tags:
- Company
- Developer Tools
- Software Studio
- Independent
- Open Source
website: https://baseframelabs.com/
---
