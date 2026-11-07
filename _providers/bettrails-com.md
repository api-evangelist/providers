---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/bettrails-com/security/bettrails-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bettrails-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bettrails-com/llms/bettrails-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bettrails-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bettrails-com/mcp/bettrails-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bettrails-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bettrails-com/well-known/bettrails-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bettrails-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bettrails-com/well-known/bettrails-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bettrails-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bettrails-com/hosts/bettrails-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bettrails-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bettrails.com/terms.php
- group: start
  title: ''
  type: SignUp
  url: https://bettrails.com/signup-free.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bettrails.com/privacy.php
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bettrails
- group: auth
  href: https://artifacts.apis.io/bettrails-com/security/bettrails-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bettrails-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bettrails-com/security/bettrails-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bettrails-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bettrails.com/
coverage:
  checked: '2026-11-02'
  detail: Bettrails provides only a public website with analytics data and no public API documentation.
  evidence:
  - status: 200
    url: https://bettrails.com
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Bettrails is an independent eSports analytics laboratory offering real‑time data, ELO ratings, and predictive models across multiple virtual football leagues, League of Legends, Dota 2, CS2, VALORANT, and NBA 2K. It provides minute‑by‑minute statistics, head‑to‑head comparisons, and confidence‑weighted forecasts for competitive gaming enthusiasts and analysts.
image: https://bettrails.com/og-cover-es.png
layout: provider
mcp_servers:
- description: Remote MCP server at bettrails.com.
  name: Bettrails MCP Server
  slug: bettrails-com-mcp-yml
modified: '2026-11-02'
name: Bettrails
nav: Providers
network: true
overview: 'Bettrails is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Esports, Analytics, Real-Time Data, and Gaming.


  Bettrails'' developer surface includes signup flow and 12 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 13.2
  provenance:
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bettrails Com Domain Security
  slug: bettrails-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bettrails Com Vulnerability Disclosure
  slug: bettrails-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 6
skills:
- name: alert-link
  slug: bettrails-com-alert-link
- name: esoccer-head-to-head
  slug: bettrails-com-esoccer-head-to-head
- name: esoccer-player
  slug: bettrails-com-esoccer-player
- name: read-page
  slug: bettrails-com-read-page
- name: read-page
  slug: bettrails-com-read_page
- name: search
  slug: bettrails-com-search
slug: bettrails-com
tags:
- Company
- Esports
- Analytics
- Real-Time Data
- Gaming
website: https://bettrails.com/
---
