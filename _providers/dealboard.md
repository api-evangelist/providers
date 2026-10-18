---
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-17'
api_count: 5
apis:
- baseURL: https://app.getdealboard.com
  baseurl_source: declared
  description: The Boards API from Dealboard — 1 operation(s) for boards.
  name: Dealboard Boards API
  slug: dealboard-boards-api
- baseURL: https://app.getdealboard.com
  baseurl_source: declared
  description: The Dealboard API API from Dealboard — 2 operation(s) for dealboard api.
  name: Dealboard Dealboard API
  slug: dealboard-dealboard-api-api
- baseURL: https://app.getdealboard.com
  baseurl_source: declared
  description: The Deals API from Dealboard — 1 operation(s) for deals.
  name: Dealboard Deals API
  slug: dealboard-deals-api
- baseURL: https://app.getdealboard.com
  baseurl_source: declared
  description: The Reports API from Dealboard — 1 operation(s) for reports.
  name: Dealboard Reports API
  slug: dealboard-reports-api
- baseURL: https://app.getdealboard.com
  baseurl_source: declared
  description: The Templates API from Dealboard — 1 operation(s) for templates.
  name: Dealboard Templates API
  slug: dealboard-templates-api
artifact_total: 8
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dealboard/refs/heads/main/plans/dealboard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dealboard-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealboard/refs/heads/main/rules/dealboard-rules.yml
  title: ''
  type: Spectral
  url: rules/dealboard-rules.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dealboard/refs/heads/main/changelog/dealboard-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dealboard-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealboard/refs/heads/main/conformance/dealboard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealboard-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dealboard/refs/heads/main/llms/dealboard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dealboard-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dealboard/refs/heads/main/well-known/dealboard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealboard-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealboard/refs/heads/main/hosts/dealboard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealboard-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealboard/refs/heads/main/vendors/dealboard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealboard-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getdealboard.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getdealboard.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://getdealboard.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.getdealboard.com/sign-in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getdealboard.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://getdealboard.com/developers/reference/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getdealboard
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealboard/refs/heads/main/security/dealboard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealboard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getdealboard.com
- group: docs
  title: ''
  type: Documentation
  url: https://getdealboard.com/developers/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://app.getdealboard.com/openapi.json
  - status: 401
    url: https://app.getdealboard.com/mcp
  - status: 200
    url: https://getdealboard.com
  reason: partner-login
  state: gated
created: '2026-10-15'
description: Dealboard is a visual sales pipeline and CRM platform that automatically captures emails, meetings, and call notes into deals. It integrates with Gmail, Google Calendar, and AI tools like ChatGPT, Claude, and Grok, offering a REST API for reading and writing deals, leads, and pipeline data. Users can get started for free without a credit card, and the service provides webhooks and an MCP server for AI agents.
image: https://getdealboard.com/og/home.png
layout: provider
modified: '2026-10-15'
name: Dealboard
nav: Providers
network: true
overview: 'Dealboard is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Boards API, Dealboard API, Deals API, and 2 more. Tagged areas include Company, CRM, Sales, Artificial Intelligence, and Integration.


  The Dealboard catalog on APIs.io includes 1 Spectral governance ruleset.


  Dealboard''s developer surface includes changelog, pricing, API reference, documentation, and 14 more developer resources.'
plans:
- name: Dealboard Plans Pricing
  plan_count: 2
  slug: dealboard-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Dealboard API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: dealboard-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 51.8
    catalog_earned_first_party: 8.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 15.9
    contract_quality: 11.9
    developer_ergonomics: 26.2
    discoverability: 78.6
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Dealboard Domain Security
  slug: dealboard-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dealboard
tags:
- Company
- CRM
- Sales
- Artificial Intelligence
- Integration
website: https://getdealboard.com
---
