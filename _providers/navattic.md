---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Navattic's hosted, remote Model Context Protocol server — the company's primary machine-readable product surface. Agents authenticate with an OAuth 2.1 authorization-code flow (PKCE, dynamic client re
  name: Navattic MCP Server
  slug: navattic-mcp-server
- description: The Health API from Navattic — 1 operation(s) for health.
  name: Navattic Health API
  slug: navattic-health-api
artifact_total: 13
asyncapis:
- description: ''
  name: Navattic Webhooks
  slug: navattic-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/navattic-website-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/navattic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navattic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.navattic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.navattic.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Navattic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/navattic
- group: company
  title: ''
  type: Blog
  url: https://www.navattic.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.navattic.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.navattic.com
- group: other
  title: ''
  type: X
  url: https://x.com/navattic
- group: commercial
  title: ''
  type: Plans
  url: plans/navattic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/navattic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/navattic-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/navattic-context.jsonld
- group: auth
  title: ''
  type: Security
  url: https://www.navattic.com/company/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/navattic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.navattic.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/navattic-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/navattic-api-catalog.json
- group: other
  title: ''
  type: ContentSignal
  url: well-known/navattic-robots.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/navattic-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/navattic-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/navattic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/navattic-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/navattic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/navattic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/navattic-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/navattic-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/navattic-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/navattic-packages.yml
- group: design
  title: ''
  type: Components
  url: components/navattic-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/navattic-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/navattic-webhooks.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.navattic.com/build/demo
- group: operate
  title: ''
  type: Support
  url: https://www.navattic.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.navattic.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.navattic.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.navattic.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.navattic.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Navattic
created: 2026-06-13
description: Navattic is an interactive product demo platform that enables marketing and sales teams to create, manage, and embed no-code product demos without engineering involvement. The platform provides a REST API and webhook integration for automating demo workflows and syncing engagement data with CRM, marketing automation, and analytics tools. Navattic supports integrations with HubSpot, Salesforce, Marketo, Segment, Gong, and dozens of other go-to-market platforms. Teams use Navattic to accelerate sales cycles, improve lead qualification, and deliver personalized demo experiences across their entire funnel.
finops:
- name: Navattic Finops
  service_category: ''
  slug: navattic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/navattic.png
jsonld:
- class_count: 21
  name: Navattic Context
  property_count: 0
  slug: navattic-context
layout: provider
mcp_servers:
- description: Navattic ships a first-party, hosted remote MCP server. It is the company's primary machine-readable product surface — there is no public REST API reference — and it is reachable by any MCP client tha
  name: Navattic MCP Server
  slug: navattic-mcp-server
modified: 2026-08-13
name: Navattic
nav: Providers
network: true
overview: 'Navattic publishes 1 API on the [APIs.io](https://apis.io/) network: Health API. Tagged areas include Interactive Demos, Product Demo, Sales Enablement, Marketing, and No-Code.


  The Navattic catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Navattic''s developer surface includes documentation, engineering blog, pricing, authentication, changelog, getting-started guide, support, and 36 more developer resources.'
plans:
- name: Navattic Plans Pricing
  plan_count: 5
  slug: navattic-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Navattic Rate Limits
  slug: navattic-rate-limits
scopes:
- name: Navattic Scopes
  scope_count: 11
  slug: navattic-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 25
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 57.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 59.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/navattic/refs/heads/main/screenshots/navattic-2026-06-20T190058.png
security:
- kind: authentication
  name: Navattic Authentication
  slug: navattic-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Navattic Domain Security
  slug: navattic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Navattic Vulnerability Disclosure
  slug: navattic-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Navattic Trust Center
  slug: navattic-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: navattic
tags:
- Interactive Demos
- Product Demo
- Sales Enablement
- Marketing
- No-Code
- Webhook
- CRM Integration
- Sales Automation
- MCP
- Agents
- Product Analytics
website: https://www.navattic.com/
---
