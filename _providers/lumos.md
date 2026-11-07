---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Lumos Agentic Access
  operation_count: 67
  slug: lumos-agentic-access
  summary_line: 67 operations · 33 acting
api_count: 2
apis:
- description: The Lumos Connector SDK allows developers to build custom connectors that integrate third-party applications with the Lumos platform, enabling automated provisioning, deprovisioning, and access manage
  name: Lumos Connector SDK
  slug: connector-sdk
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Tasks API from Lumos — 8 operation(s) for tasks.
  name: Lumos Tasks API
  slug: lumos-tasks-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: Create and manage access review campaigns — scheduled reviews of who has access to what across your connected apps. **Typical workflow for creating a review:** 1. `GET /apps` — find the domain app UUI
  name: Lumos Access Reviews API
  slug: lumos-access-reviews-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Core API from Lumos — 27 operation(s) for core.
  name: Lumos Core API
  slug: lumos-core-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Integration Webhooks API from Lumos — 2 operation(s) for integration webhooks.
  name: Lumos Integration Webhooks API
  slug: lumos-integration-webhooks-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: Knowledge entries are the documents and notes Lumos agents draw on when they answer access questions. Each entry carries a title, body, tags, and product scopes, plus an optional file attachment. Beca
  name: Lumos Knowledge API
  slug: lumos-knowledge-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Lifecycle Management API from Lumos — 3 operation(s) for lifecycle management.
  name: Lumos Lifecycle Management API
  slug: lumos-lifecycle-management-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Meta API from Lumos — 2 operation(s) for meta.
  name: Lumos Meta API
  slug: lumos-meta-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The Vendor Management API from Lumos — 4 operation(s) for vendor management.
  name: Lumos Vendor Management API
  slug: lumos-vendor-management-api
- baseURL: https://api.lumos.com
  baseurl_source: declared
  description: The App Store API from Lumos — 11 operation(s) for app store.
  name: Lumos App Store API
  slug: lumos-app-store-api
artifact_total: 39
asyncapis:
- description: ''
  name: Lumos Webhooks
  slug: lumos-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/lumos/capabilities/lumos-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lumos-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/lumos/agentic-access/lumos-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lumos-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lumos/security/lumos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lumos-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lumos/authentication/lumos-authentication.yml
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
  href: https://artifacts.apis.io/lumos/mcp/lumos-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lumos-mcp.yml
- group: build
  href: https://artifacts.apis.io/lumos/mcp/lumos-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lumos-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/lumos/scopes/lumos-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lumos-scopes.yml
- group: agent
  href: https://artifacts.apis.io/lumos/well-known/lumos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lumos-well-known.yml
- group: build
  href: https://artifacts.apis.io/lumos/packages/lumos-packages.yml
  title: ''
  type: Packages
  url: packages/lumos-packages.yml
- group: build
  href: https://artifacts.apis.io/lumos/packages/lumos-packages.yml
  title: ''
  type: SDKs
  url: packages/lumos-packages.yml
- group: build
  href: https://artifacts.apis.io/lumos/cli/lumos-cli.yml
  title: ''
  type: CLI
  url: cli/lumos-cli.yml
- group: agent
  href: https://artifacts.apis.io/lumos/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lumos/conventions/lumos-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lumos-conventions.yml
- group: design
  href: https://artifacts.apis.io/lumos/errors/lumos-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/lumos-error-codes.yml
- group: design
  href: https://artifacts.apis.io/lumos/data-model/lumos-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lumos-data-model.yml
- group: design
  href: https://artifacts.apis.io/lumos/lifecycle/lumos-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lumos-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/lumos/changelog/lumos-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lumos-changelog.yml
- group: design
  href: https://artifacts.apis.io/lumos/conformance/lumos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lumos-conformance.yml
- group: design
  href: https://artifacts.apis.io/lumos/asyncapi/lumos-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lumos-webhooks.yml
- group: other
  href: https://artifacts.apis.io/lumos/overlays/lumos-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lumos-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/lumos/llms/lumos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lumos-llms.txt
- group: operate
  href: https://artifacts.apis.io/lumos/rate-limits/lumos-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lumos-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lumos/plans/lumos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lumos-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/lumos/finops/lumos-finops.yml
  title: ''
  type: FinOps
  url: finops/lumos-finops.yml
created: '2026-03-16'
description: Lumos is the first Autonomous Identity Platform that helps organizations discover and manage access to all apps with enhanced security, increased productivity, and reduced cost. Lumos automates access requests, enforces least privilege, speeds up user access reviews, and eliminates extra SaaS app spending through 80+ connectors and an API.
finops:
- has_sources: true
  method: derived
  name: Lumos Finops
  primary_unit: ''
  service_category: ''
  slug: lumos-finops
  template: true
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
overview: 'Lumos publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Tasks API, Access Reviews API, Core API, and 7 more. Tagged areas include Identity and Access Management, Access Reviews, Deprovisioning, Identity Governance, and Identity Platform.


  The Lumos catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Lumos'' developer surface includes authentication, documentation, support, getting-started guide, engineering blog, signup flow, CLI, and 35 more developer resources.'
plans:
- name: Lumos Plans Pricing
  plan_count: 0
  slug: lumos-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Lumos Rate Limits
  slug: lumos-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Lumos API Rules
  rule_count: 54
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 10
  slug: lumos-rules
scopes:
- name: Lumos Scopes
  scope_count: 14
  slug: lumos-scopes
  summary_line: 14 scopes · authorization_code
score:
  band: strong
  composite: 62.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.8
  facets:
    access_clarity: 35.5
    contract_governance: 31.8
    contract_quality: 66.0
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 63.2
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/lumos/lumos-2026-06-20T184756.png
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
skill_count: 4
skills:
- name: lumos-clear-task-queue
  slug: lumos-clear-task-queue
- name: lumos-offboard-user
  slug: lumos-offboard-user
- name: lumos-request-access
  slug: lumos-request-access
- name: lumos-run-access-review
  slug: lumos-run-access-review
slug: lumos
tags:
- Identity and Access Management
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
