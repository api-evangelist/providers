---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Lumos Agentic Access
  operation_count: 67
  slug: lumos-agentic-access
  summary_line: 67 operations · 33 acting
api_count: 1
apis:
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Lumos REST API enables programmatic access to the Lumos identity platform for automating tasks such as managing users, apps, access requests, and governance workflows. All requests require a beare
  name: Lumos REST API
  slug: rest-api
- description: The Lumos Connector SDK allows developers to build custom connectors that integrate third-party applications with the Lumos platform, enabling automated provisioning, deprovisioning, and access manage
  name: Lumos Connector SDK
  slug: connector-sdk
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The AccessPolicies API from Lumos — 2 operation(s) for accesspolicies.
  name: Lumos AccessPolicies API
  slug: lumos-accesspolicies-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The AccessRequests API from Lumos — 3 operation(s) for accessrequests.
  name: Lumos AccessRequests API
  slug: lumos-accessrequests-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The AccessReviews API from Lumos — 5 operation(s) for accessreviews.
  name: Lumos AccessReviews API
  slug: lumos-accessreviews-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Accounts API from Lumos — 3 operation(s) for accounts.
  name: Lumos Accounts API
  slug: lumos-accounts-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Activity API from Lumos — 4 operation(s) for activity.
  name: Lumos Activity API
  slug: lumos-activity-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Apps API from Lumos — 4 operation(s) for apps.
  name: Lumos Apps API
  slug: lumos-apps-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The AppStore API from Lumos — 4 operation(s) for appstore.
  name: Lumos AppStore API
  slug: lumos-appstore-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Groups API from Lumos — 3 operation(s) for groups.
  name: Lumos Groups API
  slug: lumos-groups-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The PreApprovalRules API from Lumos — 2 operation(s) for preapprovalrules.
  name: Lumos PreApprovalRules API
  slug: lumos-preapprovalrules-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Tasks API from Lumos — 8 operation(s) for tasks.
  name: Lumos Tasks API
  slug: lumos-tasks-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Users API from Lumos — 6 operation(s) for users.
  name: Lumos Users API
  slug: lumos-users-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Utility API from Lumos — 1 operation(s) for utility.
  name: Lumos Utility API
  slug: lumos-utility-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Vendors API from Lumos — 4 operation(s) for vendors.
  name: Lumos Vendors API
  slug: lumos-vendors-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Webhooks API from Lumos — 1 operation(s) for webhooks.
  name: Lumos Webhooks API
  slug: lumos-webhooks-api
artifact_total: 41
asyncapis:
- description: ''
  name: Lumos Webhooks
  slug: lumos-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lumos REST AccessPolicies API
  slug: open-lumos-accesspolicies-api
- collection_type: open
  name: Lumos REST AccessPolicies AccessRequests API
  slug: open-lumos-accessrequests-api
- collection_type: open
  name: Lumos REST AccessPolicies Accounts API
  slug: open-lumos-accounts-api
- collection_type: open
  name: Lumos REST AccessPolicies Activity API
  slug: open-lumos-activity-api
- collection_type: open
  name: Lumos REST AccessPolicies Apps API
  slug: open-lumos-apps-api
- collection_type: open
  name: Lumos REST AccessPolicies AppStore API
  slug: open-lumos-appstore-api
- collection_type: open
  name: Lumos REST AccessPolicies Groups API
  slug: open-lumos-groups-api
- collection_type: open
  name: Lumos REST AccessPolicies PreApprovalRules API
  slug: open-lumos-preapprovalrules-api
- collection_type: open
  name: Lumos REST AccessPolicies Tasks API
  slug: open-lumos-tasks-api
- collection_type: open
  name: Lumos REST AccessPolicies Users API
  slug: open-lumos-users-api
- collection_type: open
  name: Lumos REST AccessPolicies Utility API
  slug: open-lumos-utility-api
- collection_type: open
  name: Lumos REST AccessPolicies Vendors API
  slug: open-lumos-vendors-api
- collection_type: open
  name: Lumos REST AccessPolicies Webhooks API
  slug: open-lumos-webhooks-api
- collection_type: open
  name: Lumos REST API
  slug: open-lumos
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lumos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lumos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lumos-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lumos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lumos.com/
- group: operate
  title: ''
  type: Support
  url: https://support.lumos.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.lumos.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.lumos.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.lumosidentity.com/
- group: start
  title: ''
  type: Signup
  url: https://www.lumos.com/demo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamlumos
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lumosidentity
- group: build
  title: ''
  type: CLI
  url: https://developers.lumos.com/docs/cli
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.lumos.com/llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.lumos.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.lumos.com/reference/lumos-api
- group: operate
  title: ''
  type: Roadmap
  url: https://developers.lumos.com/page/public-roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lumos.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lumos.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lumos.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lumos.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lumos-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lumos-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lumos-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lumos-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/lumos-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lumos-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lumos-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lumos-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lumos-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lumos-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lumos-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lumos-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lumos-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lumos-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lumos-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lumos-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lumos-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lumos-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lumos-finops.yml
created: '2026-03-16'
description: Lumos is the first Autonomous Identity Platform that helps organizations discover and manage access to all apps with enhanced security, increased productivity, and reduced cost. Lumos automates access requests, enforces least privilege, speeds up user access reviews, and eliminates extra SaaS app spending through 80+ connectors and an API.
finops:
- name: Lumos Finops
  service_category: API
  slug: lumos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lumos.png
layout: provider
mcp_servers:
- description: 'Lumos ships TWO first-party remote MCP servers on its own API host: an end-user server for self-service access requests, and an admin server whose tools are selected per-connection through a `toolsets'
  name: Lumos MCP
  slug: lumos-mcp
modified: '2026-08-29'
name: Lumos
nav: Providers
network: true
overview: 'Lumos publishes 15 APIs on the [APIs.io](https://apis.io/) network, including REST API, AccessPolicies API, AccessRequests API, and 12 more. Tagged areas include Access Management, Access Reviews, Deprovisioning, Identity Governance, and Identity Platform.


  The Lumos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lumos'' developer surface includes authentication, documentation, support, getting-started guide, engineering blog, signup flow, CLI, and 34 more developer resources.'
plans:
- name: Lumos Plans Pricing
  plan_count: 0
  slug: lumos-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Lumos Rate Limits
  slug: lumos-rate-limits
scopes:
- name: Lumos Scopes
  scope_count: 0
  slug: lumos-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 61.5
    developer_ergonomics: 50.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lumos/refs/heads/main/screenshots/lumos-2026-06-20T184756.png
security:
- kind: authentication
  name: Lumos Authentication
  slug: lumos-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lumos Domain Security
  slug: lumos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lumos Trust Center
  slug: lumos-trust-center
  summary_line: trust center published
slug: lumos
tags:
- Access Management
- Access Reviews
- Deprovisioning
- Identity Governance
- Identity Platform
- Least Privilege
- Provisioning
- SaaS Management
- Shadow IT
website: https://www.lumos.com/
---
