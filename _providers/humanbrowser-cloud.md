---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.0
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Humanbrowser Cloud Agentic Access
  operation_count: 6
  slug: humanbrowser-cloud-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 3
apis:
- baseURL: https://humanbrowser.cloud
  baseurl_source: declared
  description: The REST account side of Human Browser, published as OpenAPI 3.1.0 at https://humanbrowser.cloud/openapi.json with servers[] https://humanbrowser.cloud (account) and https://agent.humanbrowser.cloud (
  name: Human Browser API
  slug: human-browser-api
- description: 'Model Context Protocol access to the same browser runtime, shipped two ways: a hosted Streamable HTTP endpoint at https://agent.humanbrowser.cloud/mcp that requires the hb_live_ bearer token (anonymou'
  name: Human Browser MCP Server
  slug: humanbrowser-mcp-server
- description: 'Agent2Agent protocol surface: an agent card (protocolVersion 0.3.0, JSONRPC, version 5.1.0) served byte-identically from https://agent.humanbrowser.cloud/.well-known/agent-card.json and the website ap'
  name: Human Browser A2A Agent
  slug: humanbrowser-a2a-agent
artifact_total: 13
asyncapis:
- description: ''
  name: Humanbrowser Cloud Webhooks
  slug: humanbrowser-cloud-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://humanbrowser.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://humanbrowser.cloud/docs
- group: docs
  title: ''
  type: APIReference
  url: https://humanbrowser.cloud/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://humanbrowser.cloud/install
- group: commercial
  title: ''
  type: Pricing
  url: https://humanbrowser.cloud/install
- group: company
  title: ''
  type: Blog
  url: https://humanbrowser.cloud/blog
- group: operate
  title: ''
  type: Support
  url: https://humanbrowser.cloud/contact
- group: start
  title: ''
  type: SignUp
  url: https://humanbrowser.cloud/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://humanbrowser.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://humanbrowser.cloud/privacy
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/a2a/humanbrowser-cloud-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/humanbrowser-cloud-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/mcp/humanbrowser-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/humanbrowser-cloud-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/mcp/humanbrowser-cloud-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/humanbrowser-cloud-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/well-known/humanbrowser-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/humanbrowser-cloud-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/llms/humanbrowser-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/humanbrowser-cloud-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://humanbrowser.cloud/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/packages/humanbrowser-cloud-packages.yml
  title: ''
  type: Packages
  url: packages/humanbrowser-cloud-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/packages/humanbrowser-cloud-packages.yml
  title: ''
  type: SDKs
  url: packages/humanbrowser-cloud-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/cli/humanbrowser-cloud-cli.yml
  title: ''
  type: CLI
  url: cli/humanbrowser-cloud-cli.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/plans/humanbrowser-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/humanbrowser-cloud-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/rate-limits/humanbrowser-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/humanbrowser-cloud-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/conformance/humanbrowser-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/humanbrowser-cloud-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/lifecycle/humanbrowser-cloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/humanbrowser-cloud-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/conventions/humanbrowser-cloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/humanbrowser-cloud-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/errors/humanbrowser-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/humanbrowser-cloud-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/data-model/humanbrowser-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/humanbrowser-cloud-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/sandbox/humanbrowser-cloud-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/humanbrowser-cloud-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/asyncapi/humanbrowser-cloud-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/humanbrowser-cloud-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/skills/humanbrowser-cloud-human-browser.md
  title: ''
  type: AgentSkill
  url: skills/humanbrowser-cloud-human-browser.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/authentication/humanbrowser-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/humanbrowser-cloud-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/scopes/humanbrowser-cloud-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/humanbrowser-cloud-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/security/humanbrowser-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/humanbrowser-cloud-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/security/humanbrowser-cloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/humanbrowser-cloud-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/security/humanbrowser-cloud-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/humanbrowser-cloud-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/agentic-access/humanbrowser-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/humanbrowser-cloud-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/regulatory/humanbrowser-cloud-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/humanbrowser-cloud-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/regulatory/humanbrowser-cloud-regulatory-posture.yml
  title: ''
  type: Subprocessors
  url: regulatory/humanbrowser-cloud-regulatory-posture.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/humanbrowser-cloud/refs/heads/main/regulatory/humanbrowser-cloud-regulatory-posture.yml
  title: ''
  type: IncidentNotification
  url: regulatory/humanbrowser-cloud-regulatory-posture.yml
created: '2026-09-19'
description: 'Virix Labs is the trading name of Virix Ltd, a London software company (England & Wales no. 16325097, incorporated March 2025) that builds and operates Human Browser at humanbrowser.cloud: a hosted "cloud Chromium for AI agents" that runs a natural-language browser goal on a residential IP behind a live viewer a person can watch and take over, with CAPTCHA handling, persistent per-token cookie profiles and metered prepaid pricing ($0.10 per browser-minute, $4/GB bandwidth, $0.005 per solved CAPTCHA). The same runtime is exposed four ways: an A2A 0.3.0 agent card at /.well-known/agent-card.json with nine skills and a JSON-RPC endpoint at agent.humanbrowser.cloud/a2a; a Model Context Protocol server both hosted (agent.humanbrowser.cloud/mcp, with RFC 9728 protected-resource and RFC 8414 authorization-server metadata) and shipped as a stdio server in the npm package @virixlabs/humanbrowser; a six-operation OpenAPI 3.1.0 REST account API at humanbrowser.cloud/openapi.json; and
  an OpenAI plugin manifest plus llms.txt. Virix Labs also sells agent-run marketing and web-operations services at virixlabs.com.'
image: https://humanbrowser.cloud/logo-512.png
layout: provider
mcp_servers:
- description: ''
  name: Virix Labs MCP Server
  slug: virix-labs-mcp-server
- description: ''
  name: Human Browser MCP endpoint (Streamable HTTP)
  slug: human-browser-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Virix Labs
nav: Providers
network: true
overview: 'Virix Labs publishes 1 API on the [APIs.io](https://apis.io/) network: Human Browser API. Tagged areas include Browser Automation, Cloud Browser, AI Agents, A2A, and MCP.


  The Virix Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Virix Labs'' developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 32 more developer resources.'
plans:
- name: Humanbrowser Cloud Plans Pricing
  plan_count: 7
  slug: humanbrowser-cloud-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Humanbrowser Cloud Rate Limits
  slug: humanbrowser-cloud-rate-limits
scopes:
- name: Humanbrowser Cloud Scopes
  scope_count: 5
  slug: humanbrowser-cloud-scopes
  summary_line: 5 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 61.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 60.4
    developer_ergonomics: 76.2
    discoverability: 81.5
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Humanbrowser Cloud Authentication
  slug: humanbrowser-cloud-authentication
  summary_line: http/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Humanbrowser Cloud Domain Security
  slug: humanbrowser-cloud-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Humanbrowser Cloud Vulnerability Disclosure
  slug: humanbrowser-cloud-vulnerability-disclosure
  summary_line: disclosure policy published
slug: humanbrowser-cloud
tags:
- Browser Automation
- Cloud Browser
- AI Agents
- A2A
- MCP
- Web Scraping
- Residential Proxies
- CAPTCHA Solving
- Human-in-the-Loop
- Computer Use
- Agent-Native
- United Kingdom
website: https://humanbrowser.cloud/
---
