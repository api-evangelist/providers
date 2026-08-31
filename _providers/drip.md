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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Drip Agentic Access
  operation_count: 22
  slug: drip-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 1
apis:
- description: 'REST API for Drip exposing subscribers, tags, custom fields, broadcasts, email campaigns, events, conversions, workflows, shopper activity (orders, carts, products), purchases, and webhooks. Supports '
  name: Drip REST API
  slug: drip-api
- description: The Accounts API from Drip — 2 operation(s) for accounts.
  name: Drip Accounts API
  slug: drip-accounts-api
- description: The Broadcasts API from Drip — 2 operation(s) for broadcasts.
  name: Drip Broadcasts API
  slug: drip-broadcasts-api
- description: The Campaigns API from Drip — 5 operation(s) for campaigns.
  name: Drip Campaigns API
  slug: drip-campaigns-api
- description: The Conversions API from Drip — 1 operation(s) for conversions.
  name: Drip Conversions API
  slug: drip-conversions-api
- description: The Custom Fields API from Drip — 1 operation(s) for custom fields.
  name: Drip Custom Fields API
  slug: drip-custom-fields-api
- description: The Events API from Drip — 3 operation(s) for events.
  name: Drip Events API
  slug: drip-events-api
- description: The Forms API from Drip — 1 operation(s) for forms.
  name: Drip Forms API
  slug: drip-forms-api
- description: The Orders API from Drip — 1 operation(s) for orders.
  name: Drip Orders API
  slug: drip-orders-api
- description: The Shopper Activity API from Drip — 3 operation(s) for shopper activity.
  name: Drip Shopper Activity API
  slug: drip-shopper-activity-api
- description: The Subscribers API from Drip — 2 operation(s) for subscribers.
  name: Drip Subscribers API
  slug: drip-subscribers-api
- description: Drip operates a remote Model Context Protocol server at https://api.getdrip.com/mcp, protected by its OAuth 2.0 authorization server and discoverable through RFC 9728 protected-resource metadata. Prob
  name: Drip MCP Server
  slug: drip-mcp
artifact_total: 33
asyncapis:
- description: ''
  name: Drip Webhooks
  slug: drip-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Drip REST Accounts API
  slug: open-drip-accounts-api
- collection_type: open
  name: Drip REST Accounts Broadcasts API
  slug: open-drip-broadcasts-api
- collection_type: open
  name: Drip REST Accounts Campaigns API
  slug: open-drip-campaigns-api
- collection_type: open
  name: Drip REST Accounts Conversions API
  slug: open-drip-conversions-api
- collection_type: open
  name: Drip REST Accounts Custom Fields API
  slug: open-drip-custom-fields-api
- collection_type: open
  name: Drip REST Accounts Events API
  slug: open-drip-events-api
- collection_type: open
  name: Drip REST Accounts Forms API
  slug: open-drip-forms-api
- collection_type: open
  name: Drip REST Accounts Orders API
  slug: open-drip-orders-api
- collection_type: open
  name: Drip REST Accounts Shopper Activity API
  slug: open-drip-shopper-activity-api
- collection_type: open
  name: Drip REST Accounts Subscribers API
  slug: open-drip-subscribers-api
- collection_type: open
  name: Drip REST API
  slug: open-drip
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drip-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drip-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drip-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getdrip
- group: company
  title: ''
  type: Website
  url: https://www.drip.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.drip.com/
- group: start
  title: ''
  type: Signup
  url: https://www.drip.com/forms/79091116/submissions/new
- group: commercial
  title: ''
  type: Pricing
  url: https://www.drip.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.getdrip.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.drip.com/
- group: company
  title: ''
  type: Blog
  url: https://www.drip.com/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DripEmail
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.drip.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.drip.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.drip.com/#introduction
- group: operate
  title: ''
  type: StatusPage
  url: https://status.drip.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drip.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drip.com/privacy
- group: build
  title: ''
  type: Packages
  url: packages/drip-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/drip-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/drip-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/drip-security.txt
- group: auth
  title: ''
  type: Security
  url: security/drip-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/drip-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/drip-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/drip-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/drip-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/drip-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/drip-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/drip-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/drip-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/drip-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drip-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/drip-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/drip-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-11'
description: Drip is an email marketing and marketing automation platform built for ecommerce brands that combines subscriber management, segmentation, email campaigns, automation workflows, and shopper activity tracking. The Drip REST API gives programmatic access to subscribers, campaigns, events, workflows, broadcasts, orders, carts, and webhooks using either API token Basic authentication or OAuth 2.0.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drip.png
layout: provider
mcp_servers:
- description: 'Drip operates a real, reachable remote MCP server at https://api.getdrip.com/mcp. It is discoverable the standards-compliant way: the API host publishes RFC 9728 OAuth protected-resource metadata nami'
  name: Drip MCP Server
  slug: drip-mcp-server
modified: '2026-08-13'
name: Drip
nav: Providers
network: true
overview: 'Drip publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Broadcasts API, Campaigns API, and 7 more. Tagged areas include Email Marketing, Marketing Automation, E-Commerce, Customer Engagement, and Campaigns.


  The Drip catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Drip''s developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, API reference, and 29 more developer resources.'
plans:
- name: Drip Plans Pricing
  plan_count: 0
  slug: drip-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Drip Rate Limits
  slug: drip-rate-limits
scopes:
- name: Drip Scopes
  scope_count: 0
  slug: drip-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -2.9
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 58.5
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drip/refs/heads/main/screenshots/drip-2026-06-20T180233.png
security:
- kind: authentication
  name: Drip Authentication
  slug: drip-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Drip Domain Security
  slug: drip-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Drip Vulnerability Disclosure
  slug: drip-vulnerability-disclosure
  summary_line: disclosure policy published
slug: drip
tags:
- Email Marketing
- Marketing Automation
- E-Commerce
- Customer Engagement
- Campaigns
- Workflows
website: https://www.drip.com
---
