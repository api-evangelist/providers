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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: MCP JSON-RPC API for jobctl, allowing AI agents to manage job applications via token-authenticated calls.
  name: jobctl MCP API
  slug: jobctl-mcp-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/jobctl-app/cli/jobctl-app-cli.yml
  title: ''
  type: CLI
  url: cli/jobctl-app-cli.yml
- group: auth
  href: https://artifacts.apis.io/jobctl-app/authentication/jobctl-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jobctl-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/jobctl-app/conformance/jobctl-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jobctl-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jobctl-app/llms/jobctl-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jobctl-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/jobctl-app/well-known/jobctl-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jobctl-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/jobctl-app/hosts/jobctl-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jobctl-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/jobctl-app/vendors/jobctl-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jobctl-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/jobctl-app/packages/jobctl-app-packages.yml
  title: ''
  type: SDKs
  url: packages/jobctl-app-packages.yml
- group: build
  href: https://artifacts.apis.io/jobctl-app/packages/jobctl-app-packages.yml
  title: ''
  type: Packages
  url: packages/jobctl-app-packages.yml
- group: auth
  href: https://artifacts.apis.io/jobctl-app/security/jobctl-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jobctl-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jobctl.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.jobctl.app
- group: docs
  title: ''
  type: Documentation
  url: https://jobctl.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://jobctl.app/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://jobctl.app/docs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jobctl.app/privacy/
created: '2026-10-30'
description: jobctl is a job application tracker designed for developers, leveraging AI coding agents such as Claude, Codex, and Cursor to automatically record each job application, interview, and status across the MCP platform. The service offers a free dashboard where users can manage their job search workflow, generate insights, and integrate with popular AI tools. It provides an API for programmatic access, supporting OAuth token authentication and detailed endpoints for creating, updating, and querying applications. jobctl aims to streamline the job hunting process for technical professionals, improving organization and visibility of opportunities.
image: https://jobctl.app/og.png
layout: provider
modified: '2026-10-30'
name: jobctl-app
nav: Providers
network: true
overview: 'jobctl-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Job-Tracking, Developer-Tools, AI, and MCP.


  jobctl-app''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Jobctl App Authentication
  slug: jobctl-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jobctl App Domain Security
  slug: jobctl-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jobctl-app
tags:
- Company
- Job-Tracking
- Developer-Tools
- AI
- MCP
- Productivity
website: https://jobctl.app/
---
