---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.1
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Usersnap Agentic Access
  operation_count: 8
  slug: usersnap-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- baseURL: https://platform.usersnap.com/v0.1
  baseurl_source: declared
  description: Feedback related endpoints
  name: Usersnap Feedback API
  slug: usersnap-feedback-api
- baseURL: https://platform.usersnap.com/v0.1
  baseurl_source: declared
  description: Available options for submission
  name: Usersnap Pre Submit API
  slug: usersnap-pre-submit-api
- baseURL: https://platform.usersnap.com/v0.1
  baseurl_source: declared
  description: Project related endpoints
  name: Usersnap Project API
  slug: usersnap-project-api
- baseURL: https://platform.usersnap.com/v0.1
  baseurl_source: declared
  description: Submit feedback
  name: Usersnap Submit API
  slug: usersnap-submit-api
artifact_total: 21
asyncapis:
- description: ''
  name: Usersnap Webhooks
  slug: usersnap-webhooks
collections:
- collection_type: postman
  name: Usersnap feedback API
  slug: postman-usersnap-feedback-api
- collection_type: postman
  name: Usersnap feedback pre_submit API
  slug: postman-usersnap-pre-submit-api
- collection_type: postman
  name: Usersnap feedback project API
  slug: postman-usersnap-project-api
- collection_type: postman
  name: Usersnap feedback submit API
  slug: postman-usersnap-submit-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Usersnap feedback API
  slug: open-usersnap-feedback-api
- collection_type: open
  name: Usersnap feedback pre_submit API
  slug: open-usersnap-pre-submit-api
- collection_type: open
  name: Usersnap feedback project API
  slug: open-usersnap-project-api
- collection_type: open
  name: Usersnap feedback submit API
  slug: open-usersnap-submit-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/overlays/usersnap-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/usersnap-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/usersnap/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/agentic-access/usersnap-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/usersnap-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/security/usersnap-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/usersnap-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/security/usersnap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usersnap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usersnap.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.usersnap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.usersnap.com/docs/getting-started-with-usersnap
- group: docs
  title: ''
  type: APIReference
  url: https://help.usersnap.com/reference/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.usersnap.com/docs/getting-started-with-usersnap
- group: operate
  title: ''
  type: Support
  url: https://usersnap.com/contact
- group: company
  title: ''
  type: Blog
  url: https://usersnap.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://usersnap.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usersnap.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usersnap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usersnap.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usersnap.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://usersnap.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.usersnap.com/
- group: auth
  title: ''
  type: Security
  url: https://usersnap.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/security/usersnap-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/usersnap-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://usersnap.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://portal.usersnap.com/changelog/2bdcb520-7c12-4691-b9fe-94784b8bd8d6
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/changelog/usersnap-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/usersnap-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/llms/usersnap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usersnap-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/mcp/usersnap-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/usersnap-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/packages/usersnap-packages.yml
  title: ''
  type: Packages
  url: packages/usersnap-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/packages/usersnap-packages.yml
  title: ''
  type: SDKs
  url: packages/usersnap-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/well-known/usersnap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usersnap-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/authentication/usersnap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usersnap-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/scopes/usersnap-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/usersnap-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/errors/usersnap-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usersnap-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/conventions/usersnap-conventions.yml
  title: ''
  type: Conventions
  url: conventions/usersnap-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/conformance/usersnap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usersnap-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/lifecycle/usersnap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/usersnap-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/data-model/usersnap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usersnap-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/components/usersnap-components.yml
  title: ''
  type: Components
  url: components/usersnap-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/asyncapi/usersnap-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/usersnap-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Usersnap is a user feedback platform from Perg/Linz, Austria that lets product, development, customer success, and marketing teams capture, organize, and act on user feedback with embeddable widgets for screenshots, screen recordings, ratings, and surveys. Beyond the widgets, Usersnap ships a plan-gated platform REST API (JWT bearer auth) for submitting and querying feedback, HMAC-signed webhooks, an official npm browser package, and a hosted MCP server (mcp.usersnap.com) secured with OAuth 2.1 + PKCE so AI assistants can query feedback and create opportunities.
image: https://github.com/usersnap.png
layout: provider
mcp_servers:
- description: ''
  name: Usersnap MCP Server
  slug: usersnap-mcp-server
modified: '2026-07-21'
name: Usersnap
nav: Providers
network: true
overview: 'Usersnap publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Feedback API, Pre Submit API, Project API, and 1 more. Tagged areas include Company, Feedback, Bug Tracking, Customer Experience, and Product Management.


  The Usersnap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Usersnap''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 1
scopes:
- name: Usersnap Scopes
  scope_count: 2
  slug: usersnap-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 53.0
    discoverability: 75.0
    operational_transparency: 44.7
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/usersnap/refs/heads/main/screenshots/usersnap-2026-08-17T082655.png
security:
- kind: authentication
  name: Usersnap Authentication
  slug: usersnap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Usersnap Domain Security
  slug: usersnap-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Usersnap Vulnerability Disclosure
  slug: usersnap-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Usersnap Trust Center
  slug: usersnap-trust-center
  summary_line: trust center published
slug: usersnap
tags:
- Company
- Feedback
- Bug Tracking
- Customer Experience
- Product Management
- Surveys
- Software-as-a-Service
website: https://usersnap.com
---
