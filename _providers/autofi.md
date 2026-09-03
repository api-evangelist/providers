---
access_model:
  confidence: medium
  label: Public reference, sales-gated credentials
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - openapi
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
    dry_run_mode: true
    dynamic_client_registration: false
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
  score: 48.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Autofi Agentic Access
  operation_count: 11
  slug: autofi-agentic-access
  summary_line: 11 operations · 9 acting
api_count: 2
apis:
- description: 'Live, OAuth-protected Model Context Protocol server served from the WordPress installation behind autofi.com, discovered through RFC 9728 protected-resource metadata. It is a site/content MCP surface '
  name: AutoFi MCP Server
  slug: autofi-mcp-server
- baseURL: https://api.autofi.com
  baseurl_source: declared
  description: To authorize requests to the AutoFi API you will need an `Access Token` (JWT). Requesting an `Access Token` requires authentication credentials which you can retrieve from the AutoFi admin panel (comi
  name: AutoFi Authorization API
  slug: autofi-authorization-api
- baseURL: https://api.autofi.com
  baseurl_source: declared
  description: The Calculate Payment API from AutoFi — 3 operation(s) for calculate payment.
  name: AutoFi Calculate Payment API
  slug: autofi-calculate-payment-api
- baseURL: https://api.autofi.com
  baseurl_source: declared
  description: A `dealer` is a required entity when requesting to create a loan application. If the dealer does not exist you need to first create the `dealer` to acquire the unique `dealer code` from AutoFi.
  name: AutoFi Dealers API
  slug: autofi-dealers-api
- baseURL: https://api.autofi.com
  baseurl_source: declared
  description: The Dealmaker API from AutoFi — 2 operation(s) for dealmaker.
  name: AutoFi Dealmaker API
  slug: autofi-dealmaker-api
- baseURL: https://api.autofi.com
  baseurl_source: declared
  description: This section provides the methods available to submit and retrieve loan applications for your organization.
  name: AutoFi Loan Applications API
  slug: autofi-loan-applications-api
- baseURL: https://api.autofi.com
  baseurl_source: declared
  description: The Prequalification API from AutoFi — 1 operation(s) for prequalification.
  name: AutoFi Prequalification API
  slug: autofi-prequalification-api
artifact_total: 19
asyncapis:
- description: ''
  name: Autofi Webhooks
  slug: autofi-webhooks
collections:
- collection_type: open
  name: AutoFi API
  slug: open-autofi-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/autofi-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://autofi.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.autofi.com/api.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.autofi.com/api.html
- group: company
  title: ''
  type: Blog
  url: https://www.autofi.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.autofi.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://www.autofi.com/request-demo/
- group: start
  title: ''
  type: Login
  url: https://portal.autofi.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.autofi.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autofi.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AutoFi
- group: operate
  title: ''
  type: StatusPage
  url: https://status.autofi.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.autofi.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.autofi.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.autofi.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autofi-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/autofi-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autofi-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/autofi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/autofi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/autofi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autofi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/autofi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/autofi-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/autofi-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/autofi-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/autofi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/autofi-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/autofi-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/autofi-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/autofi-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/autofi-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/autofi-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/autofi-api-overlay.yaml
created: '2026-07-17'
description: AutoFi ("The Sales Momentum Company") is an AI-powered automotive commerce platform that connects online and in-store car-buying experiences for dealerships, OEMs, lenders, and online marketplaces. Its products span digital retailing (online financing exploration and personalized deal paths with real payments and options), showroom solutions (in-store deal-structuring tools that preserve dealership profitability and buyer transparency), Dealmaker deal structuring, and Smartlink lead management. AutoFi publicly documents a REST API — the Lending-as-a-Service surface — at api.autofi.com covering JWT client credential authorization, loan application creation and retrieval, Dealmaker and credit application submission, dealer lookup, cash/finance/lease payment estimation, and prequalification, with a UAT sandbox that can simulate lender decisions. AutoFi was surfaced as a portfolio company of 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autofi.png
layout: provider
mcp_servers:
- description: ''
  name: AutoFi MCP Server
  slug: autofi-mcp-server
- description: ''
  name: AutoFi MCP Server
  slug: autofi-mcp-server-2
modified: '2026-08-14'
name: AutoFi
nav: Providers
network: true
overview: 'AutoFi publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Calculate Payment API, Dealers API, and 3 more. Tagged areas include Company, Automotive, Fintech, Digital Retail, and Auto Finance.


  The AutoFi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AutoFi''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, sandbox, and 28 more developer resources.'
plans:
- name: Autofi Plans Pricing
  plan_count: 0
  slug: autofi-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Autofi Rate Limits
  slug: autofi-rate-limits
scopes:
- name: Autofi Scopes
  scope_count: 7
  slug: autofi-scopes
  summary_line: 7 scopes
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 59.1
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autofi/refs/heads/main/screenshots/autofi-2026-07-25T201824.png
security:
- kind: authentication
  name: Autofi Authentication
  slug: autofi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Autofi Domain Security
  slug: autofi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Autofi Vulnerability Disclosure
  slug: autofi-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Autofi Trust Center
  slug: autofi-trust-center
  summary_line: SOC 2, SOC 3
slug: autofi
tags:
- Company
- Automotive
- Fintech
- Digital Retail
- Auto Finance
- Dealerships
- Sales Enablement
- Software-as-a-Service
- Lending
- Loan Origination
- Credit Decisioning
- Payment Calculation
- Prequalification
website: https://autofi.com
---
