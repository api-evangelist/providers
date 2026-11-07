---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Vitally Agentic Access
  operation_count: 31
  slug: vitally-agentic-access
  summary_line: 31 operations · 14 acting
api_count: 9
apis:
- baseURL: https://rest.vitally.io/resources
  baseurl_source: declared
  description: The Accounts API from Vitally — 3 operation(s) for accounts.
  name: Vitally Accounts API
  slug: vitally-accounts-api
- baseURL: https://rest.vitally.io/resources
  baseurl_source: declared
  description: The Admins API from Vitally — 1 operation(s) for admins.
  name: Vitally Admins API
  slug: vitally-admins-api
- baseURL: https://rest.vitally.io/resources
  baseurl_source: declared
  description: The Conversations API from Vitally — 1 operation(s) for conversations.
  name: Vitally Conversations API
  slug: vitally-conversations-api
- baseURL: https://rest.vitally.io/resources
  baseurl_source: declared
  description: The Custom Objects API from Vitally — 1 operation(s) for custom objects.
  name: Vitally Custom Objects API
  slug: vitally-custom-objects-api
- baseURL: https://rest.vitally.io/resources
  baseurl_source: declared
  description: The Notes API from Vitally — 2 operation(s) for notes.
  name: Vitally Notes API
  slug: vitally-notes-api
- baseURL: https://rest.vitally.io/resources
  baseurl_source: declared
  description: The NPS Responses API from Vitally — 2 operation(s) for nps responses.
  name: Vitally NPS Responses API
  slug: vitally-nps-responses-api
- baseURL: https://rest.vitally.io/resources
  baseurl_source: declared
  description: The Organizations API from Vitally — 2 operation(s) for organizations.
  name: Vitally Organizations API
  slug: vitally-organizations-api
- baseURL: https://rest.vitally.io/resources
  baseurl_source: declared
  description: The Tasks API from Vitally — 2 operation(s) for tasks.
  name: Vitally Tasks API
  slug: vitally-tasks-api
- baseURL: https://rest.vitally.io/resources
  baseurl_source: declared
  description: The Users API from Vitally — 3 operation(s) for users.
  name: Vitally Users API
  slug: vitally-users-api
artifact_total: 32
asyncapis:
- description: ''
  name: Vitally Webhooks
  slug: vitally-webhooks
collections:
- collection_type: open
  name: Vitally REST Accounts API
  slug: open-vitally-accounts-api
- collection_type: open
  name: Vitally REST Accounts Admins API
  slug: open-vitally-admins-api
- collection_type: open
  name: Vitally REST Accounts Conversations API
  slug: open-vitally-conversations-api
- collection_type: open
  name: Vitally REST Accounts Custom Objects API
  slug: open-vitally-custom-objects-api
- collection_type: open
  name: Vitally REST Accounts Notes API
  slug: open-vitally-notes-api
- collection_type: open
  name: Vitally REST Accounts NPS Responses API
  slug: open-vitally-nps-responses-api
- collection_type: open
  name: Vitally REST Accounts Organizations API
  slug: open-vitally-organizations-api
- collection_type: open
  name: Vitally REST Accounts Tasks API
  slug: open-vitally-tasks-api
- collection_type: open
  name: Vitally REST Accounts Users API
  slug: open-vitally-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vitally/overview
- group: commercial
  href: https://artifacts.apis.io/vitally/plans/vitally-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vitally-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/vitally/overlays/vitally-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vitally-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://vitally.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vitally.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vitally.io/en/articles/9880649-rest-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vitally.io/en/articles/11048953-getting-started-with-vitally-as-an-admin
- group: operate
  title: ''
  type: Support
  url: https://docs.vitally.io/
- group: company
  title: ''
  type: Blog
  url: https://www.vitally.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vitally.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.vitally.io/demo-request
- group: start
  title: ''
  type: Login
  url: https://login.vitally.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vitally.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vitally.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://vitally.statuspage.io
- group: operate
  href: https://artifacts.apis.io/vitally/changelog/vitally-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vitally-changelog.yml
- group: agent
  href: https://artifacts.apis.io/vitally/mcp/vitally-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vitally-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vitally/llms/vitally-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vitally-llms.txt
- group: auth
  href: https://artifacts.apis.io/vitally/authentication/vitally-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vitally-authentication.yml
- group: operate
  href: https://artifacts.apis.io/vitally/rate-limits/vitally-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vitally-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/vitally/conventions/vitally-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vitally-conventions.yml
- group: design
  href: https://artifacts.apis.io/vitally/errors/vitally-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vitally-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vitally/lifecycle/vitally-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vitally-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/vitally/conformance/vitally-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vitally-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.vitally.io/security
- group: auth
  title: ''
  type: Security
  url: https://www.vitally.io/security
- group: auth
  href: https://artifacts.apis.io/vitally/security/vitally-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vitally-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vitally/security/vitally-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vitally-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vitally/security/vitally-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vitally-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/vitally/agentic-access/vitally-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vitally-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/vitally/data-model/vitally-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vitally-data-model.yml
- group: agent
  href: https://artifacts.apis.io/vitally/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/vitally/packages/vitally-packages.yml
  title: ''
  type: Packages
  url: packages/vitally-packages.yml
- group: build
  href: https://artifacts.apis.io/vitally/packages/vitally-packages.yml
  title: ''
  type: SDKs
  url: packages/vitally-packages.yml
- group: design
  href: https://artifacts.apis.io/vitally/asyncapi/vitally-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vitally-webhooks.yml
- group: design
  href: https://artifacts.apis.io/vitally/components/vitally-components.yml
  title: ''
  type: Components
  url: components/vitally-components.yml
created: '2026-07-17'
description: Vitally is an AI-powered Customer Success platform (CSP) that unifies customer data, health scores, and revenue context with workflow automation — Hubs, automated Playbooks, Docs, Projects, and NPS and custom surveys — plus Vitally AI (Copilot, Summaries, Meeting Recorder). Its public REST API exposes the core Customer Success objects (accounts, organizations, users, tasks, notes, conversations, NPS responses, custom objects) over HTTP Basic auth with cursor pagination and RateLimit headers, and an official remote MCP server (Beta) connects MCP-compatible AI clients to a Vitally workspace.
finops:
- has_sources: true
  method: derived
  name: Vitally Finops
  primary_unit: ''
  service_category: ''
  slug: vitally-finops
  template: true
image: https://cdn.prod.website-files.com/63d3e5f547ca0a274b2e07e1/65456c4b07c63e23bfaedbea_logo-vitally.png
layout: provider
mcp_servers:
- description: Vitally operates an official remote MCP (Model Context Protocol) server (Beta) that connects any MCP-compatible AI client (Claude, ChatGPT, Cursor) to a Vitally workspace. Authentication is a standard
  name: Vitally MCP Server
  slug: vitally
modified: '2026-07-21'
name: Vitally
nav: Providers
network: true
overview: 'Vitally is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Admins API, Conversations API, and 6 more. Tagged areas include Company, Customer Success, Software-as-a-Service, CRM, and NPS.


  The Vitally catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Vitally''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Vitally Plans Pricing
  plan_count: 3
  slug: vitally-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Vitally Rate Limits
  slug: vitally-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Vitally API Rules
  rule_count: 58
  severity_counts:
    error: 55
    hint: 0
    info: 2
    warn: 1
  slug: vitally-rules
score:
  band: strong
  composite: 61.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 24.4
    developer_ergonomics: 57.7
    discoverability: 80.0
    operational_transparency: 71.1
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/vitally/vitally-2026-08-17T082804.png
security:
- kind: authentication
  name: Vitally Authentication
  slug: vitally-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vitally Domain Security
  slug: vitally-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vitally Vulnerability Disclosure
  slug: vitally-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Vitally Trust Center
  slug: vitally-trust-center
  summary_line: SOC 2, GDPR
skill_count: 3
skills:
- name: Find at-risk accounts and summarize activity
  slug: vitally-find-at-risk-accounts
- name: Log a follow-up task on an account
  slug: vitally-log-followup-task
- name: Sync an account and its users
  slug: vitally-sync-account-and-users
slug: vitally
tags:
- Company
- Customer Success
- Software-as-a-Service
- CRM
- NPS
- Surveys
- Analytics
- Artificial Intelligence
website: https://vitally.io/
---
