---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://action.parabol.co/graphql
  baseurl_source: declared
  description: Public GraphQL API for Parabol. Authenticated with scoped Personal Access Tokens passed as a Bearer token. A single root `viewer` query returns the authenticated user and their teams, meetings, tasks,
  name: Parabol GraphQL API
  slug: parabol-graphql-api
artifact_total: 11
asyncapis:
- description: Real-time event streams exposed by the Parabol GraphQL API via the Subscription root type, delivered over the graphql-ws WebSocket protocol. Requires a scoped Personal Access Token.
  name: Parabol GraphQL Subscriptions
  slug: parabol-graphql-subscriptions-asyncapi
common:
- group: commercial
  href: https://artifacts.apis.io/parabol/plans/parabol-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/parabol-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.parabol.co/
- group: docs
  title: ''
  type: APIReference
  url: https://action.parabol.co/graphql
- group: docs
  title: ''
  type: Documentation
  url: https://www.parabol.co/friday-ship/introducing-the-parabol-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.parabol.co/friday-ship/introducing-the-parabol-api/
- group: company
  title: ''
  type: Blog
  url: https://www.parabol.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ParabolInc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.parabol.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://action.parabol.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parabol.co/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parabol.co/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.parabol.co/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://parabol.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/ParabolInc/parabol/releases
- group: auth
  href: https://artifacts.apis.io/parabol/authentication/parabol-authentication.yml
  title: ''
  type: Authentication
  url: authentication/parabol-authentication.yml
- group: auth
  href: https://artifacts.apis.io/parabol/scopes/parabol-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/parabol-scopes.yml
- group: design
  href: https://artifacts.apis.io/parabol/conventions/parabol-conventions.yml
  title: ''
  type: Conventions
  url: conventions/parabol-conventions.yml
- group: design
  href: https://artifacts.apis.io/parabol/errors/parabol-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/parabol-problem-types.yml
- group: design
  href: https://artifacts.apis.io/parabol/lifecycle/parabol-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/parabol-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/parabol/conformance/parabol-conformance.yml
  title: ''
  type: Conformance
  url: conformance/parabol-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.parabol.co/security-faq/
- group: auth
  href: https://artifacts.apis.io/parabol/security/parabol-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/parabol-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/parabol/security/parabol-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/parabol-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.parabol.co/security-faq/
- group: auth
  href: https://artifacts.apis.io/parabol/security/parabol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parabol-domain-security.yml
- group: design
  href: https://artifacts.apis.io/parabol/asyncapi/parabol-graphql-subscriptions-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/parabol-graphql-subscriptions-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/parabol/llms/parabol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/parabol-llms.txt
- group: build
  href: https://artifacts.apis.io/parabol/packages/parabol-packages.yml
  title: ''
  type: Packages
  url: packages/parabol-packages.yml
- group: agent
  href: https://artifacts.apis.io/parabol/mcp/parabol-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/parabol-mcp.yml
- group: agent
  href: https://artifacts.apis.io/parabol/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/parabol/data-model/parabol-data-model.yml
  title: ''
  type: DataModel
  url: data-model/parabol-data-model.yml
- group: operate
  href: https://artifacts.apis.io/parabol/changelog/parabol-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/parabol-changelog.yml
created: '2026-07-17'
description: Parabol is an open-source collaborative workspace that helps teams run more effective, inclusive, and engaging meetings — retrospectives, sprint poker estimation, check-ins/standups, and collaborative Pages documents — all in real time. Parabol exposes a public GraphQL API at action.parabol.co/graphql authenticated with scoped Personal Access Tokens (Bearer), letting developers and AI agents start meetings, create reflections and tasks, read team and organization data, and subscribe to live meeting events. The platform is dual-licensed AGPLv3, self-hostable for air-gapped deployments, and integrates with Jira, GitHub, GitLab, Linear, Azure DevOps, Slack, and Mattermost.
finops:
- has_sources: true
  method: derived
  name: Parabol Finops
  primary_unit: active user
  service_category: ''
  slug: parabol-finops
  template: false
image: https://action-files.parabol.co/production/build/favicon.ico
layout: provider
modified: '2026-07-20'
name: Parabol
nav: Providers
network: true
overview: 'Parabol is listed with 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Company, Developer Tools, Agile, Retrospectives, and Meetings.


  The Parabol catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Parabol''s developer surface includes API reference, documentation, getting-started guide, engineering blog, pricing, signup flow, support, and 25 more developer resources.'
plans:
- name: Parabol Plans Pricing
  plan_count: 3
  slug: parabol-plans-pricing
random_paper: 17
scopes:
- name: Parabol Scopes
  scope_count: 16
  slug: parabol-scopes
  summary_line: 16 scopes
score:
  band: strong
  composite: 58.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 4.5
    contract_quality: 52.2
    developer_ergonomics: 42.3
    discoverability: 73.2
    operational_transparency: 52.6
  previous_composite: 58.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/parabol/parabol-2026-08-07T191355.png
security:
- kind: authentication
  name: Parabol Authentication
  slug: parabol-authentication
  summary_line: http-bearer/personal-access-token · 1 scheme
- kind: domain-security
  name: Parabol Domain Security
  slug: parabol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Parabol Vulnerability Disclosure
  slug: parabol-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Parabol Trust Center
  slug: parabol-trust-center
  summary_line: SOC 2 Type 2, GDPR, CalOPPA
skill_count: 2
skills:
- name: Create and comment on tasks from meeting outcomes
  slug: parabol-create-tasks-from-retro
- name: Run a Parabol retrospective end to end
  slug: parabol-run-retrospective
slug: parabol
tags:
- Company
- Developer Tools
- Agile
- Retrospectives
- Meetings
- Collaboration
- GraphQL
- Team Productivity
- Open Source
- Real-Time
website: https://www.parabol.co/
---
