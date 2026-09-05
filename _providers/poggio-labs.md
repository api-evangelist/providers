---
access_model:
  confidence: high
  label: Free 14-day trial, then $49/user/month
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - https://poggio.io/pricing
  - plans/poggio-labs-plans-pricing.yml
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 2
  name: Poggio Labs Agentic Access
  operation_count: 36
  slug: poggio-labs-agentic-access
  summary_line: 36 operations · 21 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Versioned REST API (v2) exposing Poggio account intelligence, context search, account digests, the superagent chat, Salesforce account-plan writeback, and third-party integration registration. Secured
  name: Poggio REST API v2
  slug: poggio-rest-api-v2
- description: Hosted, remote Model Context Protocol server exposing Poggio account intelligence to AI clients — search and fetch account intelligence documents, create or recreate accounts, and query the Poggio ass
  name: Poggio MCP Server
  slug: poggio-mcp-server
- description: 'Stateless Streamable HTTP MCP service shipped with Goalkeeper, exposing 11 tools for creating and reading goals, appending status/health/evaluation reports, and managing labels. Supports MCP protocol '
  name: Goalkeeper MCP Server
  slug: goalkeeper-mcp-server
- baseURL: https://api.poggio.io/v2
  baseurl_source: declared
  description: Scoped credentials owned by an organization and user.
  name: Poggio Labs API Tokens API
  slug: poggio-labs-api-tokens-api
- baseURL: https://api.poggio.io/v2
  baseurl_source: declared
  description: User session lifecycle.
  name: Poggio Labs Authentication API
  slug: poggio-labs-authentication-api
- baseURL: https://api.poggio.io/v2
  baseurl_source: declared
  description: Organization goals and their label taxonomy.
  name: Poggio Labs Goals API
  slug: poggio-labs-goals-api
- baseURL: https://api.poggio.io/v2
  baseurl_source: declared
  description: Organization membership and active organization selection.
  name: Poggio Labs Organizations API
  slug: poggio-labs-organizations-api
- baseURL: https://api.poggio.io/v2
  baseurl_source: declared
  description: Service status endpoints.
  name: Poggio Labs System API
  slug: poggio-labs-system-api
artifact_total: 17
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/poggiolabs/goalkeeper/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/poggio-labs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/poggio-labs-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://poggio.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://poggio.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://poggio.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://poggio.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://poggio.io/docs
- group: company
  title: ''
  type: Blog
  url: https://poggio.io/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://poggio.io/pricing
- group: start
  title: ''
  type: Login
  url: https://poggio.io/app/sign-in
- group: start
  title: ''
  type: SignUp
  url: https://poggio.io/app/sign-up
- group: operate
  title: ''
  type: Support
  url: mailto:hello@poggio.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://poggio.io/docs/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://poggio.io/docs/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.poggio.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.poggio.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/poggiolabs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/poggio-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/poggio-labs-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/poggio-labs-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/poggio-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/poggio-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/poggio-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/poggio-labs-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poggio-labs-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/poggio-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/poggio-labs-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/poggio-labs-packages.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/poggio-labs-goalkeeper-openapi.json
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/poggiolabs/goalkeeper
- group: design
  title: ''
  type: Idempotency
  url: conventions/poggio-labs-goalkeeper-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/poggio-labs-goalkeeper-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/poggio-labs-goalkeeper-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/poggio-labs-goalkeeper-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/poggio-labs-goalkeeper-scopes.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/poggio-labs-goalkeeper-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/poggio-labs-goalkeeper-overlay.yaml
created: '2026-07-17'
description: Poggio (Poggio Labs) is an AI revenue intelligence platform for enterprise sales teams — a "Revenue Superagent" that unlocks Salesforce investment by combining deep-research AI agents with a unified context engine connecting CRM, call recordings (Gong), documents, and real-time web intelligence to arm sellers with always-current account knowledge, prioritization, relationship maps, and automated account plans. Poggio exposes its intelligence programmatically through a versioned REST API (v2) and a hosted Model Context Protocol (MCP) server, both secured with OAuth 2.0 (authorization code, client credentials, refresh token) and dynamic client registration, plus native Slack, Salesforce/Agentforce, Highspot, and Gong integrations. Poggio Labs also ships Goalkeeper, an Apache-2.0 self-hosted "durable goals" service for teams of people and AI agents, with its own OpenAPI 3.1 REST API and a stateless Streamable HTTP MCP server distributed as container images. Backed by Accel.
image: https://poggio.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Poggio Labs MCP Server
  slug: poggio-labs-mcp-server
- description: ''
  name: Poggio Labs MCP Server
  slug: poggio-labs-mcp-server-2
modified: '2026-08-13'
name: Poggio Labs
nav: Providers
network: true
overview: 'Poggio Labs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including API Tokens API, Authentication API, Goals API, and 2 more. Tagged areas include Company, Artificial Intelligence, Revenue Intelligence, Sales, and Account Intelligence.


  Poggio Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 32 more developer resources.'
plans:
- name: Poggio Labs Plans Pricing
  plan_count: 3
  slug: poggio-labs-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Poggio Labs Rate Limits
  slug: poggio-labs-rate-limits
scopes:
- name: Poggio Labs Goalkeeper Scopes
  scope_count: 6
  slug: poggio-labs-goalkeeper-scopes
  summary_line: 6 scopes
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 48.8
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/poggio-labs/refs/heads/main/screenshots/poggio-labs-2026-08-17T081318.png
security:
- kind: authentication
  name: Poggio Labs Authentication
  slug: poggio-labs-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Poggio Labs Domain Security
  slug: poggio-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Poggio Labs Trust Center
  slug: poggio-labs-trust-center
  summary_line: SOC 2, ISO 27001
slug: poggio-labs
tags:
- Company
- Artificial Intelligence
- Revenue Intelligence
- Sales
- Account Intelligence
- CRM
- Salesforce
- MCP
- AI Agents
- Enterprise
- Open-Source
- Goals
- Gong
- Slack
website: https://poggio.io/
---
