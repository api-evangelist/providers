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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 93
  human_in_the_loop: 7
  name: Zippykid Agentic Access
  operation_count: 149
  slug: zippykid-agentic-access
  summary_line: 149 operations · 93 acting · 7 human-in-the-loop
api_count: 8
apis:
- description: The account API from ZippyKid — 4 operation(s) for account.
  name: ZippyKid account API
  slug: zippykid-account-api
- description: The activity API from ZippyKid — 2 operation(s) for activity.
  name: ZippyKid activity API
  slug: zippykid-activity-api
- description: The auth API from ZippyKid — 2 operation(s) for auth.
  name: ZippyKid auth API
  slug: zippykid-auth-api
- description: The collaborators API from ZippyKid — 8 operation(s) for collaborators.
  name: ZippyKid collaborators API
  slug: zippykid-collaborators-api
- description: 'The http: API from ZippyKid — 1 operation(s) for http:.'
  name: 'ZippyKid http: API'
  slug: zippykid-http-api
- description: The mu-plugins API from ZippyKid — 2 operation(s) for mu-plugins.
  name: ZippyKid mu-plugins API
  slug: zippykid-mu-plugins-api
- description: The sites API from ZippyKid — 88 operation(s) for sites.
  name: ZippyKid sites API
  slug: zippykid-sites-api
- description: The zones API from ZippyKid — 5 operation(s) for zones.
  name: ZippyKid zones API
  slug: zippykid-zones-api
artifact_total: 23
asyncapis:
- description: ''
  name: Zippykid Webhooks
  slug: zippykid-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: OpenAPI
  url: openapi/_original/zippykid-pressable-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/zippykid-pressable-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zippykid-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zippykid-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zippykid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zippykid-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zippykid-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zippykid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zippykid-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zippykid-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zippykid-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zippykid-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zippykid-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zippykid-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zippykid-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zippykid-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: ZippyKid is the company behind Pressable, a managed WordPress hosting platform now operated as an Automattic brand and built on Automattic's WP Cloud infrastructure. Surfaced as a 500 Global portfolio company and added to the API Evangelist network, Pressable delivers managed WordPress hosting with autoscaling, a global CDN, Jetpack Security, daily backups, and SSH/Git/WP-CLI access. For developers and agencies it exposes a full OAuth 2.0 REST API (v1) covering sites, domains, DNS zones, Git deploys, plugins, themes, edge cache and collaborators; 66 webhook events; and a published remote MCP server (75+ tools) for AI-driven site management from Claude, Gemini CLI and ChatGPT.
image: https://i0.wp.com/pressable.com/wp-content/uploads/2024/07/dk-pressable-hosting.png
layout: provider
mcp_servers:
- description: ''
  name: ZippyKid MCP Server
  slug: zippykid-mcp-server
modified: '2026-07-21'
name: ZippyKid
nav: Providers
network: true
overview: 'ZippyKid publishes 8 APIs on the [APIs.io](https://apis.io/) network, including account API, activity API, auth API, and 5 more. Tagged areas include Company, WordPress, Managed Hosting, WordPress Hosting, and Web Hosting.


  The ZippyKid catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZippyKid''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 2
scopes:
- name: Zippykid Scopes
  scope_count: 13
  slug: zippykid-scopes
  summary_line: 13 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 16.7
    contract_quality: 58.4
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 49.7
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zippykid/refs/heads/main/screenshots/zippykid-2026-08-17T083111.png
security:
- kind: authentication
  name: Zippykid Authentication
  slug: zippykid-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Zippykid Domain Security
  slug: zippykid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
