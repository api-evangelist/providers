---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The CafeX Audit Events API allows the retrieval of audit event data for CafeX tenants. Events can be filtered by a required time range and by optional service, event type, action, user, app, workspace
  name: CafeX Audit Events API
  slug: audit-events
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/cafex-communications/lifecycle/cafex-communications-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cafex-communications-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/cafex-communications/hosts/cafex-communications-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cafex-communications-hosts.yml
- group: other
  href: https://artifacts.apis.io/cafex-communications/vendors/cafex-communications-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cafex-communications-vendors.yml
- group: build
  href: https://artifacts.apis.io/cafex-communications/packages/cafex-communications-packages.yml
  title: ''
  type: SDKs
  url: packages/cafex-communications-packages.yml
- group: auth
  href: https://artifacts.apis.io/cafex-communications/security/cafex-communications-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cafex-communications-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cafex.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://support.cafex.com/support/solutions
- group: docs
  title: ''
  type: APIReference
  url: https://support.cafex.com/support/solutions/articles/73000645442-accessing-audit-information-programmatically
- group: start
  title: ''
  type: GettingStarted
  url: https://support.cafex.com/support/solutions/articles/73000646926-building-your-first-app
- group: operate
  title: ''
  type: Support
  url: https://support.cafex.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://cafex.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cafexcomms
- group: start
  title: ''
  type: Login
  url: https://app.cafex.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cafex.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.cafex.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cafex.ai/
- group: auth
  href: https://artifacts.apis.io/cafex-communications/security/cafex-communications-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cafex-communications-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cafex.ai/
- group: auth
  href: https://artifacts.apis.io/cafex-communications/authentication/cafex-communications-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cafex-communications-authentication.yml
- group: design
  href: https://artifacts.apis.io/cafex-communications/conventions/cafex-communications-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cafex-communications-conventions.yml
- group: design
  href: https://artifacts.apis.io/cafex-communications/lifecycle/cafex-communications-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cafex-communications-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cafex-communications/conformance/cafex-communications-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cafex-communications-conformance.yml
- group: build
  href: https://artifacts.apis.io/cafex-communications/packages/cafex-communications-packages.yml
  title: ''
  type: Packages
  url: packages/cafex-communications-packages.yml
coverage:
  checked: '2026-10-20'
  detail: CafeX documents its one public API (the Audit Events search API at app.cafex.com/audit-search-rest) only as prose in a Freshdesk help-center article, with no OpenAPI, AsyncAPI, GraphQL, llms.txt or agent card on any of its hosts, and the docs generator found no reference-shaped page to build a contract from.
  evidence:
  - status: 200
    url: https://support.cafex.com/support/solutions/articles/73000645442-accessing-audit-information-programmatically
  - status: 401
    url: https://support.cafex.com/mcp
  - status: 200
    url: https://status.cafex.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-08'
description: CafeX Communications, Inc. is a US-headquartered software company (founded 2013) that builds a low-code platform for developing intelligent applications and agentic systems for regulated industries — banking, insurance, healthcare and government. The current CafeX AI platform is delivered as a multi-tenant SaaS at app.cafex.com and is organised into App Studio (App Builder, Flow Builder, Rule Builder, Data Tables and API Lab), Data Studio (Data AI, Data Gateway, Data Visualizer) and Agent Studio (Agent Builder, LM Insights). CafeX began life as a WebRTC and embedded-communications vendor (Fusion Client, Live Assist, CafeX Meetings, later the Challo collaboration workspace) and has since repositioned around AI workflow and process automation. Its one publicly documented, publicly callable API is the CafeX Audit Events API, a tenant-scoped REST search endpoint for audit event data secured with OAuth 2.0 client credentials.
image: https://cafex.ai/asset/svg/logo/dark/lockup-wide.svg
layout: provider
modified: '2026-08-08'
name: CafeX Communications
nav: Providers
network: true
overview: 'CafeX Communications is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Low-Code, Workflow Automation, AI Agents, and Audit and Compliance.


  CafeX Communications'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 33.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cafex-communications/cafex-communications-2026-09-02T145000.png
security:
- kind: authentication
  name: Cafex Communications Authentication
  slug: cafex-communications-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Cafex Communications Domain Security
  slug: cafex-communications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cafex Communications Trust Center
  slug: cafex-communications-trust-center
  summary_line: ISO 27001, SOC 2, ISO 42001
slug: cafex-communications
tags:
- Company
- Low-Code
- Workflow Automation
- AI Agents
- Audit and Compliance
- Collaboration
- Enterprise Software
- Regulated Industries
- Process Automation
website: https://cafex.ai/
---
