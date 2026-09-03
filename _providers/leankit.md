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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Bulk export API for LeanKit / Planview AgilePlace reporting data — cards, card lane positions, blocked card history, comments, connections, lanes, tags, and user assignments — consumed from Excel, Pow
  name: Planview AgilePlace Advanced Reporting API
  slug: advanced-reporting-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The account API from LeanKit — 1 operation(s) for account.
  name: LeanKit account API
  slug: leankit-account-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The attachment API from LeanKit — 3 operation(s) for attachment.
  name: LeanKit attachment API
  slug: leankit-attachment-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The automation API from LeanKit — 5 operation(s) for automation.
  name: LeanKit automation API
  slug: leankit-automation-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The board API from LeanKit — 15 operation(s) for board.
  name: LeanKit board API
  slug: leankit-board-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The board-filter API from LeanKit — 2 operation(s) for board-filter.
  name: LeanKit board-filter API
  slug: leankit-board-filter-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The board-level API from LeanKit — 1 operation(s) for board-level.
  name: LeanKit board-level API
  slug: leankit-board-level-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The board-template API from LeanKit — 2 operation(s) for board-template.
  name: LeanKit board-template API
  slug: leankit-board-template-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The card API from LeanKit — 8 operation(s) for card.
  name: LeanKit card API
  slug: leankit-card-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The card-scoring API from LeanKit — 1 operation(s) for card-scoring.
  name: LeanKit card-scoring API
  slug: leankit-card-scoring-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The card-type API from LeanKit — 2 operation(s) for card-type.
  name: LeanKit card-type API
  slug: leankit-card-type-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The comment API from LeanKit — 2 operation(s) for comment.
  name: LeanKit comment API
  slug: leankit-comment-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The config API from LeanKit — 1 operation(s) for config.
  name: LeanKit config API
  slug: leankit-config-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The connections API from LeanKit — 8 operation(s) for connections.
  name: LeanKit connections API
  slug: leankit-connections-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The custom-field API from LeanKit — 1 operation(s) for custom-field.
  name: LeanKit custom-field API
  slug: leankit-custom-field-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The custom-icon API from LeanKit — 2 operation(s) for custom-icon.
  name: LeanKit custom-icon API
  slug: leankit-custom-icon-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The dependencies API from LeanKit — 2 operation(s) for dependencies.
  name: LeanKit dependencies API
  slug: leankit-dependencies-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The lane API from LeanKit — 1 operation(s) for lane.
  name: LeanKit lane API
  slug: leankit-lane-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The planning-series API from LeanKit — 6 operation(s) for planning-series.
  name: LeanKit planning-series API
  slug: leankit-planning-series-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The tags API from LeanKit — 2 operation(s) for tags.
  name: LeanKit tags API
  slug: leankit-tags-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The team API from LeanKit — 5 operation(s) for team.
  name: LeanKit team API
  slug: leankit-team-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The token-auth API from LeanKit — 2 operation(s) for token-auth.
  name: LeanKit token-auth API
  slug: leankit-token-auth-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The user API from LeanKit — 6 operation(s) for user.
  name: LeanKit user API
  slug: leankit-user-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The user-invitation API from LeanKit — 2 operation(s) for user-invitation.
  name: LeanKit user-invitation API
  slug: leankit-user-invitation-api
- baseURL: https://myaccount.leankit.com/io
  baseurl_source: declared
  description: The users API from LeanKit — 2 operation(s) for users.
  name: LeanKit users API
  slug: leankit-users-api
artifact_total: 78
asyncapis:
- description: ''
  name: Leankit Automation Webhooks
  slug: leankit-automation-webhooks
collections:
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account API
  slug: postman-leankit-account-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account attachment API
  slug: postman-leankit-attachment-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account automation API
  slug: postman-leankit-automation-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account board API
  slug: postman-leankit-board-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account board-filter API
  slug: postman-leankit-board-filter-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account board-level API
  slug: postman-leankit-board-level-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account board-template API
  slug: postman-leankit-board-template-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account card API
  slug: postman-leankit-card-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account card-scoring API
  slug: postman-leankit-card-scoring-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account card-type API
  slug: postman-leankit-card-type-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account comment API
  slug: postman-leankit-comment-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account config API
  slug: postman-leankit-config-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account connections API
  slug: postman-leankit-connections-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account custom-field API
  slug: postman-leankit-custom-field-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account custom-icon API
  slug: postman-leankit-custom-icon-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account dependencies API
  slug: postman-leankit-dependencies-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account lane API
  slug: postman-leankit-lane-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account planning-series API
  slug: postman-leankit-planning-series-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account tags API
  slug: postman-leankit-tags-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account team API
  slug: postman-leankit-team-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account token-auth API
  slug: postman-leankit-token-auth-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account user API
  slug: postman-leankit-user-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account user-invitation API
  slug: postman-leankit-user-invitation-api
- collection_type: postman
  name: Planview AgilePlace API (LeanKit) v2 account users API
  slug: postman-leankit-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account API
  slug: open-leankit-account-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account attachment API
  slug: open-leankit-attachment-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account automation API
  slug: open-leankit-automation-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account board API
  slug: open-leankit-board-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account board-filter API
  slug: open-leankit-board-filter-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account board-level API
  slug: open-leankit-board-level-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account board-template API
  slug: open-leankit-board-template-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account card API
  slug: open-leankit-card-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account card-scoring API
  slug: open-leankit-card-scoring-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account card-type API
  slug: open-leankit-card-type-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account comment API
  slug: open-leankit-comment-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account config API
  slug: open-leankit-config-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account connections API
  slug: open-leankit-connections-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account custom-field API
  slug: open-leankit-custom-field-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account custom-icon API
  slug: open-leankit-custom-icon-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account dependencies API
  slug: open-leankit-dependencies-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account lane API
  slug: open-leankit-lane-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account planning-series API
  slug: open-leankit-planning-series-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account tags API
  slug: open-leankit-tags-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account team API
  slug: open-leankit-team-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account token-auth API
  slug: open-leankit-token-auth-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account user API
  slug: open-leankit-user-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account user-invitation API
  slug: open-leankit-user-invitation-api
- collection_type: open
  name: Planview AgilePlace API (LeanKit) v2 account users API
  slug: open-leankit-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/leankit-agileplace-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/leankit/overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/leankit-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.planview.com/products-solutions/products/agileplace/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://success.planview.com/Planview_AgilePlace/AgilePlace_API
- group: docs
  title: ''
  type: Documentation
  url: https://success.planview.com/Planview_AgilePlace
- group: docs
  title: ''
  type: APIReference
  url: https://success.planview.com/Planview_AgilePlace/AgilePlace_API/01_v2
- group: start
  title: ''
  type: GettingStarted
  url: https://success.planview.com/Planview_AgilePlace/Getting_Started
- group: operate
  title: ''
  type: Support
  url: https://success.planview.com/Planview_AgilePlace/Support
- group: company
  title: ''
  type: Blog
  url: https://blog.planview.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LeanKit
- group: commercial
  title: ''
  type: Pricing
  url: https://www.planview.com/products-solutions/products/agileplace/agileplace-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.planview.com/products-solutions/products/agileplace/get-agileplace/
- group: start
  title: ''
  type: Login
  url: https://login.leankit.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.planview.com/legal/legal-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.planview.com/trust/privacy/statement/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.planview.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.planview.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/leankit-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://success.planview.com/Planview_AgilePlace/Product_Releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leankit-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/leankit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leankit-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leankit-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/leankit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leankit-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/leankit-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leankit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leankit-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/leankit-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leankit-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leankit-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leankit-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/leankit-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leankit-automation-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leankit-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: LeanKit is the enterprise Kanban platform now shipped by Planview as Planview AgilePlace, used to visually track and manage the flow of work from strategy to delivery across boards, lanes, cards, taskboards, and connected parent/child hierarchies. LeanKit exposes a documented RESTful v2 API at https://<yourhostname>.leankit.com/io/ covering boards, cards, lanes, comments, attachments, card types, custom fields, custom icons, tags, teams, users, board filters, connections, dependencies, planning series and increments, and board automations, plus a SCIM 1.1 User Provisioning API and an Advanced Reporting export API. Authentication is Basic or Bearer API token, responses are JSON, list endpoints page with limit/offset, and every response carries X-RateLimit-* headers. LeanKit was acquired by Planview in 2017 and the product was renamed Planview AgilePlace; the leankit.com host remains the per-account API and application domain.
image: https://www.planview.com/wp-content/uploads/2023/06/planview-logo.svg
layout: provider
modified: '2026-07-19'
name: LeanKit
nav: Providers
network: true
overview: 'LeanKit publishes 24 APIs on the [APIs.io](https://apis.io/) network, including account API, attachment API, automation API, and 21 more. Tagged areas include Company, Kanban, Project Management, Agile, and Work Management.


  The LeanKit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LeanKit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
random_paper: 9
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 67.6
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 59.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leankit/refs/heads/main/screenshots/leankit-2026-07-25T224738.png
security:
- kind: authentication
  name: Leankit Authentication
  slug: leankit-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Leankit Domain Security
  slug: leankit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Leankit Trust Center
  slug: leankit-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: leankit
tags:
- Company
- Kanban
- Project Management
- Agile
- Work Management
- Collaboration
- Enterprise Software
- Portfolio-Management
- Workflow-Automation
- Software-as-a-Service
website: https://www.planview.com/products-solutions/products/agileplace/
---
