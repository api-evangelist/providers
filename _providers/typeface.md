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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Typeface Agentic Access
  operation_count: 64
  slug: typeface-agentic-access
  summary_line: 64 operations · 38 acting
api_count: 4
apis:
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Audiences API from Typeface — 3 operation(s) for audiences.
  name: Typeface Audiences API
  slug: typeface-audiences-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Authentication API from Typeface — 3 operation(s) for authentication.
  name: Typeface Authentication API
  slug: typeface-authentication-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Basic Services API from Typeface — 1 operation(s) for basic services.
  name: Typeface Basic Services API
  slug: typeface-basic-services-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Brand Kits API from Typeface — 6 operation(s) for brand kits.
  name: Typeface Brand Kits API
  slug: typeface-brand-kits-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Content Generation API from Typeface — 3 operation(s) for content generation.
  name: Typeface Content Generation API
  slug: typeface-content-generation-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Content Service API from Typeface — 3 operation(s) for content service.
  name: Typeface Content Service API
  slug: typeface-content-service-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Digital Assets API from Typeface — 7 operation(s) for digital assets.
  name: Typeface Digital Assets API
  slug: typeface-digital-assets-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Discovery API from Typeface — 2 operation(s) for discovery.
  name: Typeface Discovery API
  slug: typeface-discovery-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Feeds API from Typeface — 4 operation(s) for feeds.
  name: Typeface Feeds API
  slug: typeface-feeds-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Profile Service API from Typeface — 2 operation(s) for profile service.
  name: Typeface Profile Service API
  slug: typeface-profile-service-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Projects API from Typeface — 4 operation(s) for projects.
  name: Typeface Projects API
  slug: typeface-projects-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Provisioning API from Typeface — 2 operation(s) for provisioning.
  name: Typeface Provisioning API
  slug: typeface-provisioning-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Provisioning Service API from Typeface — 1 operation(s) for provisioning service.
  name: Typeface Provisioning Service API
  slug: typeface-provisioning-service-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Search Service API from Typeface — 1 operation(s) for search service.
  name: Typeface Search Service API
  slug: typeface-search-service-api
- baseURL: https://api-us.typeface.ai
  baseurl_source: declared
  description: The Tag Library API from Typeface — 3 operation(s) for tag library.
  name: Typeface Tag Library API
  slug: typeface-tag-library-api
artifact_total: 41
asyncapis:
- description: ''
  name: Typeface Webhooks
  slug: typeface-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Typeface Audiences API
  slug: open-typeface-audiences-api
- collection_type: open
  name: Typeface Audiences Authentication API
  slug: open-typeface-authentication-api
- collection_type: open
  name: Typeface Audiences Basic Services API
  slug: open-typeface-basic-services-api
- collection_type: open
  name: Typeface Audiences Brand Kits API
  slug: open-typeface-brand-kits-api
- collection_type: open
  name: Typeface Audiences Content Generation API
  slug: open-typeface-content-generation-api
- collection_type: open
  name: Typeface Audiences Content Service API
  slug: open-typeface-content-service-api
- collection_type: open
  name: Typeface Audiences Digital Assets API
  slug: open-typeface-digital-assets-api
- collection_type: open
  name: Typeface Audiences Discovery API
  slug: open-typeface-discovery-api
- collection_type: open
  name: Typeface Audiences Feeds API
  slug: open-typeface-feeds-api
- collection_type: open
  name: Typeface Audiences Profile Service API
  slug: open-typeface-profile-service-api
- collection_type: open
  name: Typeface Audiences Projects API
  slug: open-typeface-projects-api
- collection_type: open
  name: Typeface Audiences Provisioning API
  slug: open-typeface-provisioning-api
- collection_type: open
  name: Typeface Audiences Provisioning Service API
  slug: open-typeface-provisioning-service-api
- collection_type: open
  name: Typeface Audiences Search Service API
  slug: open-typeface-search-service-api
- collection_type: open
  name: Typeface Audiences Tag Library API
  slug: open-typeface-tag-library-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/typeface-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.typeface.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.typeface.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.typeface.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.typeface.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.typeface.ai/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/typeface-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/typeface-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/typeface-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/typeface-tool-crosswalk.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/typeface-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/typeface-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/typeface-agentic-access.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/typeface-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/typeface-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/typeface-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/typeface-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/typeface-packages.yml
- group: design
  title: ''
  type: Components
  url: components/typeface-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/typeface-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.typeface.ai
- group: auth
  title: ''
  type: TrustCenter
  url: security/typeface-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/typeface-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.typeface.ai/security-and-governance
- group: auth
  title: ''
  type: DomainSecurity
  url: security/typeface-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/typeface-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/typeface-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.typeface.ai
- group: design
  title: ''
  type: Conventions
  url: conventions/typeface-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/typeface-data-model.yml
- group: company
  title: ''
  type: Blog
  url: https://www.typeface.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://support.typeface.ai
- group: start
  title: ''
  type: Login
  url: https://app.typeface.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.typeface.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.typeface.ai/privacy
created: '2026-07-17'
description: Typeface is an enterprise marketing AI platform that orchestrates AI agents, brand intelligence, and workflows to create personalized, on-brand campaigns at scale. Its developer platform exposes REST APIs (bearer JWT via application credentials) for identity discovery, teams, projects, brand kits, audiences, layouts, assets, tags, content workflows, document search, and asynchronous batch content generation, plus outbound/inbound webhooks, a hosted MCP server with OAuth 2.1, an A2A agent surface, SCIM 2.0 provisioning, and 30+ marketing-stack connectors.
image: https://images.ctfassets.net/x690ow8339ug/g36Rl9hYe43Kx6buA0HBv/752c90259d7655c7accbb0ce0697a67e/Agentic-AI.png
layout: provider
mcp_servers:
- description: ''
  name: Typeface MCP Server
  slug: typeface-mcp-server
modified: '2026-08-13'
name: Typeface
nav: Providers
network: true
overview: 'Typeface publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Audiences API, Authentication API, Basic Services API, and 12 more. Tagged areas include Company, Artificial Intelligence, Content Generation, Marketing, and Agents.


  The Typeface catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Typeface''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, and 30 more developer resources.'
plans:
- name: Typeface Plans Pricing
  plan_count: 0
  slug: typeface-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Typeface Rate Limits
  slug: typeface-rate-limits
scopes:
- name: Typeface Scopes
  scope_count: 4
  slug: typeface-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/typeface/refs/heads/main/screenshots/typeface-2026-08-17T082511.png
security:
- kind: authentication
  name: Typeface Authentication
  slug: typeface-authentication
  summary_line: http-bearer/oauth2 · 3 schemes
- kind: domain-security
  name: Typeface Domain Security
  slug: typeface-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Typeface Vulnerability Disclosure
  slug: typeface-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Typeface Trust Center
  slug: typeface-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: typeface
tags:
- Company
- Artificial Intelligence
- Content Generation
- Marketing
- Agents
- Generative AI
- Brand Management
- Enterprise
website: https://www.typeface.ai
---
