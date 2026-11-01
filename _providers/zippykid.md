---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 92
  human_in_the_loop: 7
  name: Zippykid Agentic Access
  operation_count: 149
  slug: zippykid-agentic-access
  summary_line: 149 operations · 92 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://my.pressable.com/v1
  baseurl_source: declared
  description: The account API from ZippyKid — 4 operation(s) for account.
  name: ZippyKid Account API
  slug: zippykid-account-api
- baseURL: https://my.pressable.com/v1
  baseurl_source: declared
  description: The activity API from ZippyKid — 2 operation(s) for activity.
  name: ZippyKid Activity API
  slug: zippykid-activity-api
- baseURL: https://my.pressable.com/v1
  baseurl_source: declared
  description: The auth API from ZippyKid — 2 operation(s) for auth.
  name: ZippyKid Auth API
  slug: zippykid-auth-api
- baseURL: https://my.pressable.com/v1
  baseurl_source: declared
  description: The collaborators API from ZippyKid — 8 operation(s) for collaborators.
  name: ZippyKid Collaborators API
  slug: zippykid-collaborators-api
- baseURL: https://my.pressable.com/v1
  baseurl_source: declared
  description: 'The http: API from ZippyKid — 1 operation(s) for http:.'
  name: 'ZippyKid http: API'
  slug: zippykid-http-api
- baseURL: https://my.pressable.com/v1
  baseurl_source: declared
  description: The mu-plugins API from ZippyKid — 2 operation(s) for mu-plugins.
  name: ZippyKid Mu Plugins API
  slug: zippykid-mu-plugins-api
- baseURL: https://my.pressable.com/v1
  baseurl_source: declared
  description: The sites API from ZippyKid — 88 operation(s) for sites.
  name: ZippyKid Sites API
  slug: zippykid-sites-api
- baseURL: https://my.pressable.com/v1
  baseurl_source: declared
  description: The zones API from ZippyKid — 5 operation(s) for zones.
  name: ZippyKid Zones API
  slug: zippykid-zones-api
artifact_total: 27
asyncapis:
- description: ''
  name: Zippykid Webhooks
  slug: zippykid-webhooks
collections:
- collection_type: open
  name: Pressable API Documentation (v1) account API
  slug: open-zippykid-account-api
- collection_type: open
  name: Pressable API Documentation (v1) account activity API
  slug: open-zippykid-activity-api
- collection_type: open
  name: Pressable API Documentation (v1) account auth API
  slug: open-zippykid-auth-api
- collection_type: open
  name: Pressable API Documentation (v1) account collaborators API
  slug: open-zippykid-collaborators-api
- collection_type: open
  name: 'Pressable API Documentation (v1) account http: API'
  slug: open-zippykid-http-api
- collection_type: open
  name: Pressable API Documentation (v1) account mu-plugins API
  slug: open-zippykid-mu-plugins-api
- collection_type: open
  name: Pressable API Documentation (v1) account sites API
  slug: open-zippykid-sites-api
- collection_type: open
  name: Pressable API Documentation (v1) account zones API
  slug: open-zippykid-zones-api
common:
- group: commercial
  href: https://artifacts.apis.io/zippykid/plans/zippykid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zippykid-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/zippykid/capabilities/zippykid-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zippykid-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://pressable.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.pressable.com/documentation/api/v1
- group: docs
  title: ''
  type: Documentation
  url: https://my.pressable.com/documentation/api/v1
- group: docs
  title: ''
  type: APIReference
  url: https://my.pressable.com/documentation/api/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://my.pressable.com/documentation/api/v1/introduction.md
- group: operate
  title: ''
  type: Support
  url: https://pressable.com/knowledgebase/
- group: company
  title: ''
  type: Blog
  url: https://pressable.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://pressable.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://my.pressable.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pressable.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pressable.com/legal/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://pressable.com/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://pressablestatus.com/
- group: docs
  href: https://artifacts.apis.io/zippykid/openapi/_original/zippykid-pressable-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/zippykid-pressable-openapi-original.json
- group: other
  href: https://artifacts.apis.io/zippykid/overlays/zippykid-pressable-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zippykid-pressable-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/zippykid/llms/zippykid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zippykid-llms.txt
- group: agent
  href: https://artifacts.apis.io/zippykid/mcp/zippykid-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zippykid-mcp.yml
- group: auth
  href: https://artifacts.apis.io/zippykid/authentication/zippykid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zippykid-authentication.yml
- group: auth
  href: https://artifacts.apis.io/zippykid/scopes/zippykid-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/zippykid-scopes.yml
- group: design
  href: https://artifacts.apis.io/zippykid/conventions/zippykid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zippykid-conventions.yml
- group: design
  href: https://artifacts.apis.io/zippykid/errors/zippykid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zippykid-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zippykid/lifecycle/zippykid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zippykid-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/zippykid/changelog/zippykid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zippykid-changelog.yml
- group: design
  href: https://artifacts.apis.io/zippykid/asyncapi/zippykid-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/zippykid-webhooks.yml
- group: design
  href: https://artifacts.apis.io/zippykid/conformance/zippykid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zippykid-conformance.yml
- group: design
  href: https://artifacts.apis.io/zippykid/data-model/zippykid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zippykid-data-model.yml
- group: agent
  href: https://artifacts.apis.io/zippykid/well-known/zippykid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zippykid-well-known.yml
- group: auth
  href: https://artifacts.apis.io/zippykid/security/zippykid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zippykid-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/zippykid/agentic-access/zippykid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zippykid-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/zippykid/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: ZippyKid is the company behind Pressable, a managed WordPress hosting platform now operated as an Automattic brand and built on Automattic's WP Cloud infrastructure. Surfaced as a 500 Global portfolio company and added to the API Evangelist network, Pressable delivers managed WordPress hosting with autoscaling, a global CDN, Jetpack Security, daily backups, and SSH/Git/WP-CLI access. For developers and agencies it exposes a full OAuth 2.0 REST API (v1) covering sites, domains, DNS zones, Git deploys, plugins, themes, edge cache and collaborators; 66 webhook events; and a published remote MCP server (75+ tools) for AI-driven site management from Claude, Gemini CLI and ChatGPT.
finops:
- has_sources: true
  method: derived
  name: Zippykid Finops
  primary_unit: subscription
  service_category: ''
  slug: zippykid-finops
  template: false
image: https://i0.wp.com/pressable.com/wp-content/uploads/2024/07/dk-pressable-hosting.png
layout: provider
mcp_servers:
- description: Remote MCP server at pressable.com over HTTP.
  name: ZippyKid MCP Server
  slug: pressable
modified: '2026-07-21'
name: ZippyKid
nav: Providers
network: true
overview: 'ZippyKid publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Activity API, Auth API, and 5 more. Tagged areas include Company, WordPress, Managed Hosting, WordPress Hosting, and Web Hosting.


  The ZippyKid catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZippyKid''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Zippykid Plans Pricing
  plan_count: 9
  slug: zippykid-plans-pricing
- name: Zippykid Price Estimates
  plan_count: 0
  slug: zippykid-price-estimates
random_paper: 20
scopes:
- name: Zippykid Scopes
  scope_count: 13
  slug: zippykid-scopes
  summary_line: 13 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 53.2
    developer_ergonomics: 58.9
    discoverability: 65.0
    operational_transparency: 39.5
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zippykid/zippykid-2026-08-17T083111.png
security:
- kind: authentication
  name: Zippykid Authentication
  slug: zippykid-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Zippykid Domain Security
  slug: zippykid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Connect a repo and deploy to a Pressable site
  slug: zippykid-git-deploy
- name: Provision a Pressable WordPress site
  slug: zippykid-provision-site
slug: zippykid
tags:
- Company
- WordPress
- Managed Hosting
- WordPress Hosting
- Web Hosting
- WP Cloud
- MCP
- DevOps
website: https://pressable.com
---
