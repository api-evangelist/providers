---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Nursa's OpenID Connect / OAuth 2.0 authorization server. Issues the JWT access tokens the Nursa Public API requires, supports the authorization code (with and without PKCE), resource owner password, i
  name: Nursa Authorization Server
  slug: auth
- description: The Clinicians API from Nursa — 4 operation(s) for clinicians.
  name: Nursa Clinicians API
  slug: nursa-clinicians-api
- description: The Downloads API from Nursa — 1 operation(s) for downloads.
  name: Nursa Downloads API
  slug: nursa-downloads-api
- description: The Facilities API from Nursa — 8 operation(s) for facilities.
  name: Nursa Facilities API
  slug: nursa-facilities-api
- description: The Facilities webhooks API from Nursa — 2 operation(s) for facilities webhooks.
  name: Nursa Facilities webhooks API
  slug: nursa-facilities-webhooks-api
- description: The Licenses API from Nursa — 1 operation(s) for licenses.
  name: Nursa Licenses API
  slug: nursa-licenses-api
- description: The Marketplace API from Nursa — 6 operation(s) for marketplace.
  name: Nursa Marketplace API
  slug: nursa-marketplace-api
- description: The Scheduled shifts API from Nursa — 2 operation(s) for scheduled shifts.
  name: Nursa Scheduled shifts API
  slug: nursa-scheduled-shifts-api
- description: The Shift reports API from Nursa — 4 operation(s) for shift reports.
  name: Nursa Shift reports API
  slug: nursa-shift-reports-api
- description: The Shift requests API from Nursa — 2 operation(s) for shift requests.
  name: Nursa Shift requests API
  slug: nursa-shift-requests-api
- description: The Shifts API from Nursa — 1 operation(s) for shifts.
  name: Nursa Shifts API
  slug: nursa-shifts-api
- description: The Support API from Nursa — 1 operation(s) for support.
  name: Nursa Support API
  slug: nursa-support-api
- description: The User webhooks API from Nursa — 2 operation(s) for user webhooks.
  name: Nursa User webhooks API
  slug: nursa-user-webhooks-api
- description: The Webhook logs API from Nursa — 1 operation(s) for webhook logs.
  name: Nursa Webhook logs API
  slug: nursa-webhook-logs-api
artifact_total: 35
asyncapis:
- description: ''
  name: Nursa Public Api V2 Webhooks
  slug: nursa-public-api-v2-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nursa Public API V2 Clinicians API
  slug: open-nursa-clinicians-api
- collection_type: open
  name: Nursa Public API V2 Downloads API
  slug: open-nursa-downloads-api
- collection_type: open
  name: Nursa Public API V2 Facilities API
  slug: open-nursa-facilities-api
- collection_type: open
  name: Nursa Public API V2 Facilities webhooks API
  slug: open-nursa-facilities-webhooks-api
- collection_type: open
  name: Nursa Public API V2 Licenses API
  slug: open-nursa-licenses-api
- collection_type: open
  name: Nursa Public API V2 Marketplace API
  slug: open-nursa-marketplace-api
- collection_type: open
  name: Nursa Public API V2 Scheduled shifts API
  slug: open-nursa-scheduled-shifts-api
- collection_type: open
  name: Nursa Public API V2 Shift reports API
  slug: open-nursa-shift-reports-api
- collection_type: open
  name: Nursa Public API V2 Shift requests API
  slug: open-nursa-shift-requests-api
- collection_type: open
  name: Nursa Public API V2 Shifts API
  slug: open-nursa-shifts-api
- collection_type: open
  name: Nursa Public API V2 Support API
  slug: open-nursa-support-api
- collection_type: open
  name: Nursa Public API V2 User webhooks API
  slug: open-nursa-user-webhooks-api
- collection_type: open
  name: Nursa Public API V2 Webhook logs API
  slug: open-nursa-webhook-logs-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nursa-mcp.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nursa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nursa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nursa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nursa.com/developers/start-here
- group: start
  title: ''
  type: Portal
  url: https://developers.prod.nursa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nursa.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nursa.com/pages/api/nursa-public-api-v-2
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nursa.com/docs/Integration%20Guideline/First%20steps/
- group: start
  title: ''
  type: SignUp
  url: https://nursa.com/signup/facility
- group: start
  title: ''
  type: Login
  url: https://app.nursa.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://nursa.com/facility/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nursa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nursa.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://nursa.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.nursa.com/help-center/
- group: operate
  title: ''
  type: Community
  url: https://community.nursa.com/
- group: company
  title: ''
  type: Blog
  url: https://nursa.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nursa-com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nursa.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nursa-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nursa-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nursa-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nursa-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nursa-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nursa-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nursa-scopes.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/nursa-packages.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/nursa-public-api-v2-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nursa-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nursa-public-api-v2-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nursa-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nursa-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nursa-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nursa-public-api-v2-overlay.yaml
created: '2026-08-04'
description: Nursa is a healthcare staffing marketplace, founded in Salt Lake City in 2019, that connects credentialed per diem (PRN) clinicians — registered nurses, licensed practical nurses, certified nursing assistants, certified medication aides and allied professionals — directly with hospitals, skilled nursing facilities, long-term and post-acute care providers, removing the traditional staffing agency from the middle. Facilities post open shifts and set their own rates, clinicians browse and request shifts, and both sides settle through Nursa's shift-report flow. Nursa publishes a Public API V2 (REST, JWT bearer, with an OpenID Connect / OAuth 2.0 authorization server) so workforce-management and scheduling platforms can post shifts, review requests, schedule clinicians, read clinician credentials and subscribe to webhooks — the integration surface behind its Covr, StaffLion, Dropstat, Maple and UKG partnerships. The company is accredited by The Joint Commission and reports more than
  4,500 facilities and 500,000 clinicians nationwide.
image: https://cdn.prod.website-files.com/636e7f8063d6538dea5ca1e4/63e3d5253bcbd6e2b35efeee_logo-horizontal-color.svg
layout: provider
mcp_servers:
- description: ''
  name: Nursa MCP Server
  slug: nursa-mcp-server
modified: '2026-08-04'
name: Nursa
nav: Providers
network: true
overview: 'Nursa publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Clinicians API, Downloads API, Facilities API, and 10 more. Tagged areas include Company, Healthcare, Health, Staffing, and Nursing.


  The Nursa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nursa''s developer surface includes developer portal, documentation, API reference, getting-started guide, signup flow, pricing, support, and 29 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 1
  name: Nursa Rate Limits
  slug: nursa-rate-limits
scopes:
- name: Nursa Scopes
  scope_count: 26
  slug: nursa-scopes
  summary_line: 26 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 60.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 68.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 60.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nursa/refs/heads/main/screenshots/nursa-2026-08-07T185748.png
security:
- kind: authentication
  name: Nursa Authentication
  slug: nursa-authentication
  summary_line: http/openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Nursa Domain Security
  slug: nursa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nursa Trust Center
  slug: nursa-trust-center
  summary_line: SOC 2
slug: nursa
tags:
- Company
- Healthcare
- Health
- Staffing
- Nursing
- Marketplace
- Workforce Management
- Scheduling
- Human Resources
- Per Diem
- Shifts
- Webhook
website: https://nursa.com/
---
