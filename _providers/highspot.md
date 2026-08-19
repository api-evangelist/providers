---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.6
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'The Highspot REST API provides programmatic access to the Highspot sales enablement platform, enabling management of content (spots and items), users, groups, pitches, domain settings, and analytics. '
  name: Highspot API
  slug: highspot-api
- description: The Highspot MCP Server leverages the Model Context Protocol to provide LLMs with access to sales content, knowledge, insights, and actions within Highspot. Enables searching content, accessing deal-s
  name: Highspot MCP Server
  slug: highspot-mcp-server
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/highspot-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/highspot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/highspot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.highspot.com/
- group: build
  title: ''
  type: IntegrationDirectory
  url: https://exchange.highspot.com/integrations
- group: agent
  title: ''
  type: MCPServer
  url: https://www.highspot.com/product/mcp-server/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.highspot.com/pricing/
- group: operate
  title: ''
  type: Status
  url: https://status.highspot.com/
- group: auth
  title: ''
  type: Security
  url: https://www.highspot.com/trust/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.highspot.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.highspot.com/terms/
- group: operate
  title: ''
  type: Contact
  url: https://www.highspot.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.highspot.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/highspot
- group: build
  title: ''
  type: GitHub
  url: https://github.com/highspot
- group: commercial
  title: ''
  type: Plans
  url: plans/highspot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/highspot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/highspot-finops.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/highspot-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/highspot-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/highspot-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/highspot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/highspot-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/highspot-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/highspot-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/highspot-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/highspot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.highspot.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.highspot.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.highspot.com/
- group: operate
  title: ''
  type: Community
  url: https://community.highspot.com/
- group: operate
  title: ''
  type: Support
  url: https://www.highspot.com/contact/
- group: start
  title: ''
  type: Login
  url: https://app.highspot.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.highspot.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/highspot
created: '2026-06-13'
description: Highspot is a sales enablement and go-to-market platform whose API surface splits in two. A per-tenant REST API at https://api-{instance}.highspot.com/v1.0 covers spots, items, item content, users, groups, pitches and analytics, authenticated with an API client key and secret issued from account settings; it has no public reference and no published OpenAPI. Alongside it Highspot runs a first-party remote MCP server at https://mcp.highspot.com/mcp, verified live, secured with OAuth 2.1 (dynamic client registration, PKCE, scopes mcp:read / mcp:write / offline_access) and discoverable through RFC 8414 and RFC 9728 metadata documents. The MCP server exposes content search, instant answers, deal context, content recommendations, linked pitches, Digital Room generation and Highspot Agents to OpenAI, Anthropic and Microsoft Copilot clients. Both the MCP server and the Insights Layer APIs are gated to the top "Best" subscription tier.
finops:
- name: Highspot Finops
  service_category: ''
  slug: highspot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/highspot.png
layout: provider
mcp_servers:
- description: ''
  name: highspot-mcp.yml
  slug: highspot-mcpyml
- description: ''
  name: mcp-server
  slug: mcp-server
modified: '2026-08-14'
name: Highspot
nav: Providers
network: true
overview: 'Highspot publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Enablement, Content Management, Pitch Analytics, CRM Integration, and Buyer Engagement.


  Highspot''s developer surface includes pricing, status page, privacy policy, engineering blog, GitHub presence, authentication, support, and 28 more developer resources.'
plans:
- name: Highspot Plans Pricing
  plan_count: 3
  slug: highspot-plans-pricing
random_paper: 125
rate_limits:
- limit_count: 2
  name: Highspot Rate Limits
  slug: highspot-rate-limits
scopes:
- name: Highspot Scopes
  scope_count: 3
  slug: highspot-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 38.8
  delta: -4.1
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 42.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/highspot/refs/heads/main/screenshots/highspot-2026-06-20T182731.png
security:
- kind: authentication
  name: Highspot Authentication
  slug: highspot-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Highspot Domain Security
  slug: highspot-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Highspot Vulnerability Disclosure
  slug: highspot-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Highspot Trust Center
  slug: highspot-trust-center
  summary_line: ISO 27001, GDPR
slug: highspot
tags:
- Sales Enablement
- Content Management
- Pitch Analytics
- CRM Integration
- Buyer Engagement
- Training
- Coaching
- AI
- MCP Server
website: https://www.highspot.com/
---
