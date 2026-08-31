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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 74
  human_in_the_loop: 2
  name: Hooklogic Criteo Agentic Access
  operation_count: 114
  slug: hooklogic-criteo-agentic-access
  summary_line: 114 operations · 74 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Accounts API from HookLogic (Criteo) — 12 operation(s) for accounts.
  name: HookLogic (Criteo) Accounts API
  slug: hooklogic-criteo-accounts-api
- description: The Analytics API from HookLogic (Criteo) — 12 operation(s) for analytics.
  name: HookLogic (Criteo) Analytics API
  slug: hooklogic-criteo-analytics-api
- description: The Audience API from HookLogic (Criteo) — 8 operation(s) for audience.
  name: HookLogic (Criteo) Audience API
  slug: hooklogic-criteo-audience-api
- description: The Balance API from HookLogic (Criteo) — 6 operation(s) for balance.
  name: HookLogic (Criteo) Balance API
  slug: hooklogic-criteo-balance-api
- description: The Billing API from HookLogic (Criteo) — 3 operation(s) for billing.
  name: HookLogic (Criteo) Billing API
  slug: hooklogic-criteo-billing-api
- description: The Campaign API from HookLogic (Criteo) — 54 operation(s) for campaign.
  name: HookLogic (Criteo) Campaign API
  slug: hooklogic-criteo-campaign-api
- description: The Catalog API from HookLogic (Criteo) — 2 operation(s) for catalog.
  name: HookLogic (Criteo) Catalog API
  slug: hooklogic-criteo-catalog-api
- description: The Gateway API from HookLogic (Criteo) — 1 operation(s) for gateway.
  name: HookLogic (Criteo) Gateway API
  slug: hooklogic-criteo-gateway-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Criteo Accounts API
  slug: open-hooklogic-criteo-accounts-api
- collection_type: open
  name: Criteo Accounts Analytics API
  slug: open-hooklogic-criteo-analytics-api
- collection_type: open
  name: Criteo Accounts Audience API
  slug: open-hooklogic-criteo-audience-api
- collection_type: open
  name: Criteo Accounts Balance API
  slug: open-hooklogic-criteo-balance-api
- collection_type: open
  name: Criteo Accounts Billing API
  slug: open-hooklogic-criteo-billing-api
- collection_type: open
  name: Criteo Accounts Campaign API
  slug: open-hooklogic-criteo-campaign-api
- collection_type: open
  name: Criteo Accounts Catalog API
  slug: open-hooklogic-criteo-catalog-api
- collection_type: open
  name: Criteo Accounts Gateway API
  slug: open-hooklogic-criteo-gateway-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hooklogic-criteo-capability-edges.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hooklogic-criteo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/hooklogic-criteo-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hooklogic-criteo-scopes.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/hooklogic-criteo-a2a.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hooklogic-criteo-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hooklogic-criteo-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/hooklogic-criteo-components.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.criteo.com
- group: start
  title: ''
  type: Quickstart
  url: https://developers.criteo.com/criteo-apis/docs/connect-to-the-api
- group: other
  title: ''
  type: Overlay
  url: overlays/hooklogic-criteo-retailmedia-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.criteo.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.criteo.com/retail-media/docs/welcome-to-criteo
- group: docs
  title: ''
  type: APIReference
  url: https://developers.criteo.com/criteo-apis/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.criteo.com/criteo-apis/docs/connect-to-the-api
- group: operate
  title: ''
  type: Support
  url: https://developers.criteo.com/criteo-apis/docs/escalation-guidelines
- group: company
  title: ''
  type: Blog
  url: https://www.criteo.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/criteo
- group: start
  title: ''
  type: SignUp
  url: https://developers.criteo.com/criteo-apis/docs/create-your-partner-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.criteo.com/criteo-apis/docs/criteo-api-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.criteo.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/realcriteo/workspace/criteo/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/hooklogic-criteo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hooklogic-criteo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hooklogic-criteo-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hooklogic-criteo-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hooklogic-criteo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.criteo.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.criteo.com/criteo-apis/docs/versioning-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hooklogic-criteo-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/hooklogic-criteo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hooklogic-criteo-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hooklogic-criteo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hooklogic-criteo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hooklogic-criteo-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hooklogic-criteo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hooklogic-criteo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hooklogic-criteo-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hooklogic-criteo-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hooklogic-criteo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://api.criteo.com/.well-known/security.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hooklogic-criteo-agentic-access.yml
created: '2026-07-17'
description: HookLogic was a retail-media advertising exchange and ad server that let brands buy sponsored-product placements in retailer search results (Walmart, Target, Best Buy). Criteo acquired HookLogic for ~$250M in 2016, and the product line is now delivered as the Criteo Retail Media API — a REST API for retailers, brands, and agencies to programmatically create, launch, monitor, and report on retail-media campaigns. It uses OAuth 2.0 (client-credentials and authorization-code flows), RFC 7807 error bodies, date-based API versioning, and ships officially supported Python, PHP, and Java SDKs.
image: https://avatars.githubusercontent.com/u/1713646?v=4
layout: provider
mcp_servers:
- description: ''
  name: Criteo Docs
  slug: criteo-docs
modified: '2026-08-13'
name: HookLogic (Criteo)
nav: Providers
network: true
overview: 'HookLogic (Criteo) publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Analytics API, Audience API, and 5 more. Tagged areas include Company, Commerce, Retail Media, Advertising, and E-Commerce.


  HookLogic (Criteo)''s developer surface includes quickstart, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 36 more developer resources.'
plans:
- name: Hooklogic Criteo Plans Pricing
  plan_count: 0
  slug: hooklogic-criteo-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Hooklogic Criteo Rate Limits
  slug: hooklogic-criteo-rate-limits
scopes:
- name: Hooklogic Criteo Scopes
  scope_count: 11
  slug: hooklogic-criteo-scopes
  summary_line: 11 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 25
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 49.4
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 78.9
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hooklogic-criteo/refs/heads/main/screenshots/hooklogic-criteo-2026-07-25T221415.png
security:
- kind: authentication
  name: Hooklogic Criteo Authentication
  slug: hooklogic-criteo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hooklogic Criteo Domain Security
  slug: hooklogic-criteo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hooklogic Criteo Vulnerability Disclosure
  slug: hooklogic-criteo-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Hooklogic Criteo Trust Center
  slug: hooklogic-criteo-trust-center
  summary_line: SOC 2, ISO 27001
slug: hooklogic-criteo
tags:
- Company
- Commerce
- Retail Media
- Advertising
- E-Commerce
- Marketing
- Retail
website: https://developers.criteo.com
---
