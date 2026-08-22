---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.9
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: 'REST API for brands and advertisers: partners, programs, contracts, actions and conversions, deals, promo codes, catalogs, ads, tracking links, invoices, exception lists, reports and bulk export jobs.'
  name: Impact Brand API
  slug: brand-api
- description: 'REST API for media partners, publishers and creators: programs, contracts, actions and action inquiries, clicks, ads, tracking links, promo codes, catalogs, stores, media properties, invoices, tax doc'
  name: Impact Partner API
  slug: partner-api
- description: 'REST API for agencies managing multiple advertiser accounts: advertiser roster, company information, compliance content submission, report export and job management. Version 3.'
  name: Impact Agency API
  slug: agency-api
- description: 'REST and GraphQL API for impact.com Advocate, the customer-referral product acquired as SaaSquatch: participants, referrals, referral codes, rewards and reward balances, share links, data exports and '
  name: Impact Advocate API
  slug: advocate-api
- description: Remote Model Context Protocol server for impact.com. Fifteen documented tools give an AI assistant account-scoped access to performance analytics, invoices, partner and program discovery, promo codes,
  name: Impact MCP Server
  slug: mcp-server
artifact_total: 16
asyncapis:
- description: ''
  name: Impact Webhooks
  slug: impact-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/impact-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://impact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.impact.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ImpactInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/impactdotcom
- group: company
  title: ''
  type: Blog
  url: https://impact.com/press-releases/
- group: commercial
  title: ''
  type: Pricing
  url: https://impact.com/get-started/
- group: other
  title: ''
  type: X
  url: https://x.com/impactdotcom
- group: commercial
  title: ''
  type: Plans
  url: plans/impact-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/impact-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/impact-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/impact-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://integrations.impact.com/
- group: docs
  title: ''
  type: APIReference
  url: https://integrations.impact.com/brand-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://integrations.impact.com/rest-apis/api-quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.impact.com/
- group: start
  title: ''
  type: SignUp
  url: https://impact.com/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://impact.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impact.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.impact.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/impact-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/impact-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/impact-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/impact-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/impact-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/impact-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/impact-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/impact-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/impact-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/impact-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/impact-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/impact-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/impact-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/impact-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/impact-packages.yml
- group: design
  title: ''
  type: Components
  url: components/impact-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/impact-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/impact-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impact-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/impact-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/impact-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/impact-webhooks.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/impact-advocate-graphql.yml
created: '2026-06-13'
description: impact.com is a partnership management platform for affiliate, creator, influencer and customer-referral programs. It publishes four REST API personas - Brand v14, Partner v16, Agency v3 and Advocate v13 - across 69 OpenAPI 3.1 documents and 245 operations, a remote OAuth 2.1 MCP server at mcp.impact.com, first-party agent skills, an Advocate GraphQL endpoint, webhook and postback event delivery, and an agent-readable developer portal that serves llms.txt, per-page markdown and a live documentation question interface.
finops:
- name: Impact Finops
  service_category: ''
  slug: impact-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/impact.png
jsonld:
- class_count: 0
  name: Impact Context
  property_count: 2
  slug: impact-context
layout: provider
mcp_servers:
- description: ''
  name: impact-mcp.yml
  slug: impact-mcpyml
modified: '2026-08-13'
name: Impact
nav: Providers
network: true
overview: 'Impact publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Brand API, Partner API, Agency API, and 1 more. Tagged areas include Affiliate, Partnerships, Performance Marketing, Commission, and Tracking.


  The Impact catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Impact''s developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, support, signup flow, and 39 more developer resources.'
plans:
- name: Impact Plans Pricing
  plan_count: 0
  slug: impact-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Impact Rate Limits
  slug: impact-rate-limits
scopes:
- name: Impact Scopes
  scope_count: 0
  slug: impact-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 68.3
  delta: -0.7
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 16.7
    contract_quality: 65.7
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 94.7
  previous_composite: 69.0
  provenance:
    conformance: derived
    contracts:
      callable: 98.6
      derived: 0
      marker_coverage: 0.0
      total: 69
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/impact/refs/heads/main/screenshots/impact-2026-06-20T183254.png
security:
- kind: authentication
  name: Impact Authentication
  slug: impact-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Impact Domain Security
  slug: impact-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Impact Vulnerability Disclosure
  slug: impact-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Impact Trust Center
  slug: impact-trust-center
  summary_line: SOC 1 Type II, ISO/IEC 27001:2022, PCI DSS Level 4
slug: impact
tags:
- Affiliate
- Partnerships
- Performance Marketing
- Commission
- Tracking
- Creator Economy
- Partner Management
- Referral
- Attribution
- Payouts
- Marketing
- Advertising
- MCP
- Agents
website: https://impact.com/
---
