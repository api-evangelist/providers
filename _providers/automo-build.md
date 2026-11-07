---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://mcp.automo.build
  baseurl_source: declared
  description: The Agent API from Automo — 3 operation(s) for agent.
  name: Automo Agent API
  slug: automo-build-agent-api
- baseURL: https://mcp.automo.build
  baseurl_source: declared
  description: The Mcp API from Automo — 1 operation(s) for mcp.
  name: Automo MCP API
  slug: automo-build-mcp-api
- baseURL: https://mcp.automo.build
  baseurl_source: declared
  description: The Oauth API from Automo — 3 operation(s) for oauth.
  name: Automo OAuth API
  slug: automo-build-oauth-api
- baseURL: https://mcp.automo.build
  baseurl_source: declared
  description: The Openapi.json API from Automo — 1 operation(s) for openapi.json.
  name: Automo Openapi.json API
  slug: automo-build-openapi-json-api
- baseURL: https://mcp.automo.build
  baseurl_source: declared
  description: The .well Known API from Automo — 4 operation(s) for .well known.
  name: Automo .well Known API
  slug: automo-build-well-known-api
artifact_total: 29
common:
- group: operate
  href: https://artifacts.apis.io/automo-build/rate-limits/automo-build-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/automo-build-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/automo-build/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/automo-build/data-model/automo-build-data-model.yml
  title: ''
  type: DataModel
  url: data-model/automo-build-data-model.yml
- group: build
  href: https://artifacts.apis.io/automo-build/cli/automo-build-cli.yml
  title: ''
  type: CLI
  url: cli/automo-build-cli.yml
- group: design
  href: https://artifacts.apis.io/automo-build/conventions/automo-build-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/automo-build-conventions.yml
- group: design
  href: https://artifacts.apis.io/automo-build/conventions/automo-build-conventions.yml
  title: ''
  type: Conventions
  url: conventions/automo-build-conventions.yml
- group: auth
  href: https://artifacts.apis.io/automo-build/authentication/automo-build-authentication.yml
  title: ''
  type: Authentication
  url: authentication/automo-build-authentication.yml
- group: auth
  href: https://artifacts.apis.io/automo-build/scopes/automo-build-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/automo-build-scopes.yml
- group: operate
  href: https://artifacts.apis.io/automo-build/lifecycle/automo-build-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/automo-build-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/automo-build/lifecycle/automo-build-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/automo-build-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/automo-build/errors/automo-build-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/automo-build-problem-types.yml
- group: design
  href: https://artifacts.apis.io/automo-build/conformance/automo-build-conformance.yml
  title: ''
  type: Conformance
  url: conformance/automo-build-conformance.yml
- group: agent
  href: https://artifacts.apis.io/automo-build/llms/automo-build-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automo-build-llms.txt
- group: agent
  href: https://artifacts.apis.io/automo-build/mcp/automo-build-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/automo-build-mcp.yml
- group: auth
  href: https://artifacts.apis.io/automo-build/well-known/automo-build-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/automo-build-security.txt
- group: agent
  href: https://artifacts.apis.io/automo-build/well-known/automo-build-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/automo-build-well-known.yml
- group: other
  href: https://artifacts.apis.io/automo-build/hosts/automo-build-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automo-build-hosts.yml
- group: other
  href: https://artifacts.apis.io/automo-build/vendors/automo-build-vendors.yml
  title: ''
  type: Vendors
  url: vendors/automo-build-vendors.yml
- group: build
  href: https://artifacts.apis.io/automo-build/packages/automo-build-packages.yml
  title: ''
  type: SDKs
  url: packages/automo-build-packages.yml
- group: build
  href: https://artifacts.apis.io/automo-build/packages/automo-build-packages.yml
  title: ''
  type: Packages
  url: packages/automo-build-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.automo.build/
- group: auth
  title: ''
  type: Security
  url: https://automo.build/security
- group: auth
  href: https://artifacts.apis.io/automo-build/security/automo-build-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/automo-build-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/automo-build/security/automo-build-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automo-build-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://automo.build/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://automo.build/developers
- group: docs
  title: ''
  type: Documentation
  url: https://automo.build/developers
- group: docs
  title: ''
  type: APIReference
  url: https://automo.build/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://automo.build/developers#quickstart
- group: operate
  title: ''
  type: Support
  url: https://automo.build/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://automo.build/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://automo.build/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://automo.build/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Desygner
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://mcp.automo.build/openapi.json
  - status: 401
    url: https://mcp.automo.build/mcp
  - status: 401
    url: https://mcp.automo.build/graphql
  - status: 200
    url: https://automo.build/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Automo is an AI‑assisted engineering platform that builds production software from plain language. It describes apps, builds real React, TypeScript and Supabase code, tests, governs changes, and deploys anywhere. Automo Build offers a full delivery loop with Builder, Guardrails, QA, Security, Doctor, Conductor, and deployment infrastructure. Teams get a CTO, Coder, QA analyst, Security engineer, Doctor, and SysOps operator for each workspace, enabling visible, governed hand‑offs. Automo Group, legal name Automo AI Pte Ltd, is based in Singapore and provides the Automo Build platform to enterprises seeking reliable AI‑driven software creation.
image: https://usnucnguvktksltkwjkn.supabase.co/storage/v1/object/public/generated-images/1ccb9e98-821b-4195-a850-6d7ae6469d15/67ad0355-5998-4790-8ba8-de9f39459775.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.automo.build.
  name: Automo MCP Server
  slug: automo-build-mcp-yml
modified: '2026-11-02'
name: Automo
nav: Providers
network: true
overview: 'Automo publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, MCP API, OAuth API, and 2 more. Tagged areas include Artificial Intelligence, Platform, Low-Code, Automation, and Software Development.


  Automo''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, pricing, and 27 more developer resources.'
plans:
- name: Automo Build Plans Pricing
  plan_count: 0
  slug: automo-build-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Automo Build Rate Limits
  slug: automo-build-rate-limits
scopes:
- name: Automo Build Scopes
  scope_count: 0
  slug: automo-build-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 27.0
    developer_ergonomics: 54.0
    discoverability: 65.0
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 40.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 64.3
      total: 14
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Automo Build Authentication
  slug: automo-build-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Automo Build Domain Security
  slug: automo-build-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Automo Build Vulnerability Disclosure
  slug: automo-build-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 17
skills:
- name: automo-build-agent-access-pilot-request
  slug: automo-build-agent-access-pilot-request
- name: autonet-lpricing
  slug: automo-build-autonet-lpricing
- name: create-lcallback-linbox
  slug: automo-build-create-lcallback-linbox
- name: create-ldiagnostic-lwatch
  slug: automo-build-create-ldiagnostic-lwatch
- name: create-lfunding-lcheckout
  slug: automo-build-create-lfunding-lcheckout
- name: create-lutility-laccount
  slug: automo-build-create-lutility-laccount
- name: delete-lcallback-linbox
  slug: automo-build-delete-lcallback-linbox
- name: automo-build-monitor-agent
  slug: automo-build-monitor-agent
- name: read-lcallback-levents
  slug: automo-build-read-lcallback-levents
- name: read-ldiagnostic-lwatch
  slug: automo-build-read-ldiagnostic-lwatch
- name: receive-lcallback
  slug: automo-build-receive-lcallback
- name: request-lmonthly-lcredits
  slug: automo-build-request-lmonthly-lcredits
- name: run-autonet-sandbox
  slug: automo-build-run-autonet-sandbox
- name: run-lautonet-lsandbox
  slug: automo-build-run-lautonet-lsandbox
- name: run-lcredit-ldiagnostic
  slug: automo-build-run-lcredit-ldiagnostic
- name: utility-laccount
  slug: automo-build-utility-laccount
- name: utility-lcatalog
  slug: automo-build-utility-lcatalog
slug: automo-build
tags:
- Artificial Intelligence
- Platform
- Low-Code
- Automation
- Software Development
website: https://automo.build/
---
