---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 99
  human_in_the_loop: 1
  name: Linkbreakers Com Agentic Access
  operation_count: 173
  slug: linkbreakers-com-agentic-access
  summary_line: 173 operations · 99 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Claiming a workspace an AI agent registered for itself. An agent registers at the authorization server (https://mcp.linkbreakers.com/agent/identity, see https://linkbreakers.com/auth.md) and hands a p
  name: linkbreakers-com Agent Identity API
  slug: linkbreakers-com-agent-identity-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: What the workspace has used of each limit its plan sets, read from the same counters that enforce them.
  name: linkbreakers-com Allowances API
  slug: linkbreakers-com-allowances-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing analytics dashboards with flexible, config-driven widgets. Each widget defines its own data source and visualization.
  name: linkbreakers-com Analytics Dashboard API
  slug: linkbreakers-com-analytics-dashboard-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for retrieving aggregated analytics data for dashboard widgets including geographic breakdown, device distribution, and visitor trends.
  name: linkbreakers-com Analytics Data API
  slug: linkbreakers-com-analytics-data-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: The permissions an API token or OAuth grant can hold. Every authenticated endpoint requires exactly one scope, declared on the operation.
  name: linkbreakers-com API Scopes API
  slug: linkbreakers-com-api-scopes-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Context-aware assistant that delegates to specialized sub-assistants based on the resource being edited.
  name: linkbreakers-com Assistant API
  slug: linkbreakers-com-assistant-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for handling authentication in Linkbreakers. These endpoints allow you to sign in, request password reset, and reset passwords.
  name: linkbreakers-com Auth API
  slug: linkbreakers-com-auth-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing custom domains in Linkbreakers. These endpoints allow you to register, verify, and manage custom domains for your workspace.
  name: linkbreakers-com Custom Domains API
  slug: linkbreakers-com-custom-domains-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing directories in Linkbreakers. Directories let you organize links and other directories into a hierarchical folder structure.
  name: linkbreakers-com Directories API
  slug: linkbreakers-com-directories-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing events in Linkbreakers. These endpoints allow you to collect data and list events.
  name: linkbreakers-com Events API
  slug: linkbreakers-com-events-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Connect your Google account to automatically sync form responses from links that redirect to Google Forms.
  name: linkbreakers-com Google Forms Integrations API
  slug: linkbreakers-com-google-forms-integrations-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: The IntegrationsService API from linkbreakers-com — 1 operation(s) for integrationsservice.
  name: linkbreakers-com Integrations Service API
  slug: linkbreakers-com-integrationsservice-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Long-running operations. An endpoint that works in the background answers 202 Accepted with a job and a Location header; poll GET /v1/jobs/{id} until the status is JOB_STATUS_SUCCEEDED or JOB_STATUS_F
  name: linkbreakers-com Jobs API
  slug: linkbreakers-com-jobs-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing link-level data collection settings in Linkbreakers.
  name: linkbreakers-com Link Settings API
  slug: linkbreakers-com-link-settings-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing shortened links in Linkbreakers. These endpoints allow you to create, retrieve, list, and delete shortened links for your workspace.
  name: linkbreakers-com Links API
  slug: linkbreakers-com-links-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing media files in Linkbreakers. These endpoints allow you to upload, retrieve, list, and delete media files for your workspace.
  name: linkbreakers-com Media API
  slug: linkbreakers-com-media-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing members in Linkbreakers. These endpoints allow you to invite, retrieve, update, and delete members.
  name: linkbreakers-com Members API
  slug: linkbreakers-com-members-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing Page Theme Templates in Linkbreakers. These endpoints allow you to create, retrieve, update, publish, import, and delete reusable page styling.
  name: linkbreakers-com Page Theme Templates API
  slug: linkbreakers-com-page-theme-templates-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing page visual themes. These endpoints allow you to create, read, and update themes for canvas, cover, badge, container, typography, footer logo, and interactive elements.
  name: linkbreakers-com Page Themes API
  slug: linkbreakers-com-page-themes-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: 'Public pricing catalog: the plans, what each costs and what each allows. Prices come from the billing provider and limits from the code that enforces them.'
  name: linkbreakers-com Pricing API
  slug: linkbreakers-com-pricing-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing QR Code Designs in Linkbreakers. These endpoints allow you to create, retrieve, update, and delete QR Code Designs.
  name: linkbreakers-com QR Code Designs API
  slug: linkbreakers-com-qr-code-designs-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing QR Code Templates in Linkbreakers. These endpoints allow you to create, retrieve, update, and delete QR Code Templates.
  name: linkbreakers-com QR Code Templates API
  slug: linkbreakers-com-qr-code-templates-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing the Slack integration. Connect your Slack workspace to receive real-time notifications when events occur on your links.
  name: linkbreakers-com Slack Integrations API
  slug: linkbreakers-com-slack-integrations-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing tags in Linkbreakers. These endpoints allow you to search for tags in a workspace.
  name: linkbreakers-com Tags API
  slug: linkbreakers-com-tags-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: The Time Series API from linkbreakers-com — 1 operation(s) for time series.
  name: linkbreakers-com Time Series API
  slug: linkbreakers-com-time-series-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Identify and manage visitors. Accepts system fields like $email, $phone and arbitrary key/value attributes.
  name: linkbreakers-com Visitors API
  slug: linkbreakers-com-visitors-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing webhooks in Linkbreakers. These endpoints allow you to create, list, and delete webhooks for event notifications.
  name: linkbreakers-com Webhooks API
  slug: linkbreakers-com-webhooks-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing workflow steps in Linkbreakers. Workflow steps define the behavior of links, such as redirection destinations and data collection flows.
  name: linkbreakers-com Workflow Steps API
  slug: linkbreakers-com-workflow-steps-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for analyzing workspace activity within Linkbreakers, covering rolling event totals, audience reach, and calendar heatmaps.
  name: linkbreakers-com Workspace Metrics API
  slug: linkbreakers-com-workspace-metrics-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing workspace tokens in Linkbreakers. These endpoints allow you to create, list, and delete workspace tokens for authentication.
  name: linkbreakers-com Workspace Tokens API
  slug: linkbreakers-com-workspace-tokens-api
- baseURL: https://api.linkbreakers.com
  baseurl_source: declared
  description: Endpoints for managing workspaces in Linkbreakers. These endpoints allow you to update and get workspaces.
  name: linkbreakers-com Workspaces API
  slug: linkbreakers-com-workspaces-api
artifact_total: 52
common:
- group: auth
  href: https://artifacts.apis.io/linkbreakers-com/well-known/linkbreakers-com-crates-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/linkbreakers-com-crates-security.txt
- group: agent
  href: https://artifacts.apis.io/linkbreakers-com/agentic-access/linkbreakers-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/linkbreakers-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/linkbreakers-com/rate-limits/linkbreakers-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/linkbreakers-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/linkbreakers-com/plans/linkbreakers-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/linkbreakers-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/linkbreakers-com/rules/linkbreakers-com-rules.yml
  title: ''
  type: Spectral
  url: rules/linkbreakers-com-rules.yml
- group: design
  href: https://artifacts.apis.io/linkbreakers-com/json-ld/linkbreakers-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linkbreakers-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/linkbreakers-com/vocabulary/linkbreakers-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/linkbreakers-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/linkbreakers-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/linkbreakers-com/data-model/linkbreakers-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/linkbreakers-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/linkbreakers-com/cli/linkbreakers-com-cli.yml
  title: ''
  type: CLI
  url: cli/linkbreakers-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/linkbreakers-com/changelog/linkbreakers-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/linkbreakers-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/linkbreakers-com/conventions/linkbreakers-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/linkbreakers-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/linkbreakers-com/conventions/linkbreakers-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/linkbreakers-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/linkbreakers-com/security/linkbreakers-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/linkbreakers-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/linkbreakers-com/authentication/linkbreakers-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/linkbreakers-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/linkbreakers-com/scopes/linkbreakers-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/linkbreakers-com-scopes.yml
- group: operate
  href: https://artifacts.apis.io/linkbreakers-com/lifecycle/linkbreakers-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/linkbreakers-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/linkbreakers-com/lifecycle/linkbreakers-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/linkbreakers-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/linkbreakers-com/errors/linkbreakers-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/linkbreakers-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/linkbreakers-com/conformance/linkbreakers-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/linkbreakers-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/linkbreakers-com/llms/linkbreakers-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/linkbreakers-com-llms.txt
- group: build
  href: https://artifacts.apis.io/linkbreakers-com/mcp/linkbreakers-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/linkbreakers-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/linkbreakers-com/mcp/linkbreakers-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/linkbreakers-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/linkbreakers-com/well-known/linkbreakers-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/linkbreakers-com-security.txt
- group: agent
  href: https://artifacts.apis.io/linkbreakers-com/well-known/linkbreakers-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/linkbreakers-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/linkbreakers-com/hosts/linkbreakers-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linkbreakers-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/linkbreakers-com/vendors/linkbreakers-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linkbreakers-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/linkbreakers-com/packages/linkbreakers-com-packages.yml
  title: ''
  type: Packages
  url: packages/linkbreakers-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://linkbreakers.com/help/api/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://linkbreakers.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://linkbreakers.com/sdk/go
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linkbreakers.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/linkbreakers-com/linkbreakers-cli/releases/tag/v1.185.0
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.linkbreakers.com</code
- group: auth
  href: https://artifacts.apis.io/linkbreakers-com/security/linkbreakers-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/linkbreakers-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/linkbreakers-com/security/linkbreakers-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linkbreakers-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://linkbreakers.com/
- group: docs
  title: ''
  type: Documentation
  url: https://linkbreakers.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://linkbreakers.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://linkbreakers.com/developers
- group: operate
  title: ''
  type: Support
  url: https://linkbreakers.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkbreakers-com
- group: commercial
  title: ''
  type: Pricing
  url: https://linkbreakers.com/pricing.md
created: '2026-10-30'
description: Linkbreakers provides a RESTful API that enables developers to generate dynamic QR codes, create and manage short links, receive real‑time scan webhooks, and access analytics. The platform offers SDKs for multiple languages, a Managed Compute Platform (MCP) for AI agents, and a free tier with no credit‑card required. It targets businesses seeking lead capture and workflow automation through QR code interactions.
image: https://linkbreakers.com/linkbreakers-symbol.svg
json_schemas:
- name: CreateContactLinkRequest
  property_count: 16
  slug: linkbreakers-com-create-contact-link-request
- name: CreateThankYouLinkRequest
  property_count: 16
  slug: linkbreakers-com-create-thank-you-link-request
- name: CreateWorkspaceTokenRequest represents the request to create a new workspace token
  property_count: 3
  slug: linkbreakers-com-create-workspace-token-request
- name: Request to create a new workflow step
  property_count: 7
  slug: linkbreakers-com-workflow-steps-service-create-body
- name: Workspace
  property_count: 22
  slug: linkbreakers-com-workspace
- name: WorkspaceTokensServiceUpdateBody
  property_count: 3
  slug: linkbreakers-com-workspace-tokens-service-update-body
jsonld:
- class_count: 120
  name: Linkbreakers Com Context
  property_count: 214
  slug: linkbreakers-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.linkbreakers.com requiring OAuth.
  name: linkbreakers-com MCP Server
  slug: linkbreakers-com-mcp-yml
modified: '2026-10-30'
name: linkbreakers-com
nav: Providers
network: true
overview: 'linkbreakers-com publishes 31 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Identity API, Allowances API, Analytics Dashboard API, and 28 more. Tagged areas include QR Codes, Lead Capture, Webhook, and SDK.


  The linkbreakers-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  linkbreakers-com''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, support, and 36 more developer resources.'
plans:
- name: Linkbreakers Com Plans Pricing
  plan_count: 2
  slug: linkbreakers-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Linkbreakers Com Rate Limits
  slug: linkbreakers-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 118
  extends:
  - spectral:oas
  name: linkbreakers-com API Rules
  rule_count: 77
  severity_counts:
    error: 61
    hint: 0
    info: 3
    warn: 13
  slug: linkbreakers-com-rules
scopes:
- name: Linkbreakers Com Scopes
  scope_count: 0
  slug: linkbreakers-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.6
  coverage:
    artifact_dirs: 33
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 67.0
    developer_ergonomics: 54.0
    discoverability: 66.7
    operational_transparency: 64.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 71.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/linkbreakers-com/linkbreakers-com-2026-11-03T134913.png
security:
- kind: authentication
  name: Linkbreakers Com Authentication
  slug: linkbreakers-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Linkbreakers Com Domain Security
  slug: linkbreakers-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Linkbreakers Com Vulnerability Disclosure
  slug: linkbreakers-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: create-link
  slug: linkbreakers-com-create-link
- name: create-workflow-step
  slug: linkbreakers-com-create-workflow-step
- name: list-events
  slug: linkbreakers-com-list-events
- name: list-visitors
  slug: linkbreakers-com-list-visitors
- name: update-qrcode-design
  slug: linkbreakers-com-update-qrcode-design
slug: linkbreakers-com
tags:
- QR Codes
- Lead Capture
- Webhook
- SDK
website: https://linkbreakers.com/
---
