---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sprig Agentic Access
  operation_count: 6
  slug: sprig-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.sprig.com
  baseurl_source: declared
  description: The Purge API from Sprig — 1 operation(s) for purge.
  name: Sprig Purge API
  slug: sprig-purge-api
- baseURL: https://api.sprig.com
  baseurl_source: declared
  description: The Responses API from Sprig — 1 operation(s) for responses.
  name: Sprig Responses API
  slug: sprig-responses-api
- baseURL: https://api.sprig.com
  baseurl_source: declared
  description: The Surveys API from Sprig — 1 operation(s) for surveys.
  name: Sprig Surveys API
  slug: sprig-surveys-api
- baseURL: https://api.sprig.com
  baseurl_source: declared
  description: The Themes API from Sprig — 1 operation(s) for themes.
  name: Sprig Themes API
  slug: sprig-themes-api
- baseURL: https://api.sprig.com
  baseurl_source: declared
  description: The Users API from Sprig — 2 operation(s) for users.
  name: Sprig Users API
  slug: sprig-users-api
artifact_total: 18
asyncapis:
- description: ''
  name: Sprig Webhooks
  slug: sprig-webhooks
collections:
- collection_type: open
  name: Sprig V1 API
  slug: open-sprig-v1-api
- collection_type: open
  name: Sprig V1 V2 API
  slug: open-sprig-v2-api
common:
- group: commercial
  href: https://artifacts.apis.io/sprig/plans/sprig-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sprig-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/sprig/capabilities/sprig-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sprig-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/sprig/overlays/sprig-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sprig-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sprig.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sprig.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sprig.com/reference/sprig-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sprig.com/docs/installation/introduction-web/web-javascript
- group: operate
  href: https://artifacts.apis.io/sprig/changelog/sprig-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sprig-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sprig.com/
- group: company
  title: ''
  type: Blog
  url: https://sprig.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://sprig.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.sprig.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sprig.com/ssa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sprig.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@sprig.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UserLeap
- group: build
  href: https://artifacts.apis.io/sprig/packages/sprig-packages.yml
  title: ''
  type: Packages
  url: packages/sprig-packages.yml
- group: build
  href: https://artifacts.apis.io/sprig/packages/sprig-packages.yml
  title: ''
  type: SDKs
  url: packages/sprig-packages.yml
- group: agent
  href: https://artifacts.apis.io/sprig/mcp/sprig-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sprig-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sprig/well-known/sprig-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sprig-well-known.yml
- group: agent
  href: https://artifacts.apis.io/sprig/llms/sprig-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sprig-llms.txt
- group: design
  href: https://artifacts.apis.io/sprig/conformance/sprig-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sprig-conformance.yml
- group: design
  href: https://artifacts.apis.io/sprig/lifecycle/sprig-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sprig-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sprig/conventions/sprig-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sprig-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sprig/scopes/sprig-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sprig-scopes.yml
- group: design
  href: https://artifacts.apis.io/sprig/asyncapi/sprig-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sprig-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/sprig/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sprig/agentic-access/sprig-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sprig-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sprig/security/sprig-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sprig-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sprig/authentication/sprig-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sprig-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sprig.com/
created: '2026-07-17'
description: Sprig is a continuous product-research platform that helps teams automatically capture user insights to improve their product, user experience, and marketing. Sprig delivers in-product studies and surveys to specific users at specific moments across web and mobile, then uses AI to synthesize responses into themes. For developers, Sprig ships a REST API (api.sprig.com) to export studies, responses, and themes and to manage users, web/mobile SDKs (JavaScript, iOS, Android, React Native, Flutter), a webhook event surface, and an official hosted MCP server for AI clients. Formerly UserLeap.
finops:
- has_sources: true
  method: derived
  name: Sprig Finops
  primary_unit: ''
  service_category: ''
  slug: sprig-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sprig.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.sprig.com over HTTP; 3 tools listed.
  name: Sprig MCP Server
  slug: sprig
modified: '2026-07-21'
name: Sprig
nav: Providers
network: true
overview: 'Sprig publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Purge API, Responses API, Surveys API, and 2 more. Tagged areas include Company, Product Research, Surveys, User Insights, and Customer Experience.


  The Sprig catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Sprig''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Sprig Plans Pricing
  plan_count: 1
  slug: sprig-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Sprig API Rules
  rule_count: 62
  severity_counts:
    error: 59
    hint: 0
    info: 2
    warn: 1
  slug: sprig-rules
scopes:
- name: Sprig Scopes
  scope_count: 5
  slug: sprig-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 59.4
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/sprig/sprig-2026-08-17T082046.png
security:
- kind: authentication
  name: Sprig Authentication
  slug: sprig-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sprig Domain Security
  slug: sprig-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 2
skills:
- name: Export Sprig study results
  slug: sprig-export-study-results
- name: Manage Sprig users and honor privacy requests
  slug: sprig-manage-users-and-privacy
slug: sprig
tags:
- Company
- Product Research
- Surveys
- User Insights
- Customer Experience
- Analytics
- Product Analytics
- Artificial Intelligence
- Software-as-a-Service
website: https://sprig.com/
---
