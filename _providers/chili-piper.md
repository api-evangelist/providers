---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    agent_skills: true
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Chili Piper Agentic Access
  operation_count: 73
  slug: chili-piper-agentic-access
  summary_line: 73 operations · 52 acting
api_count: 19
apis:
- description: Official hosted remote MCP server for Chili Piper, served over streamable HTTP at https://fire.chilipiper.com/api/fire-edge/v1/org/mcp. Supports OAuth (Admin, browser-based) and API-key bearer authent
  name: Chili Piper MCP Server
  slug: mcp
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The availability API from Chili Piper — 1 operation(s) for availability.
  name: Chili Piper Availability API
  slug: chili-piper-availability-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The chat API from Chili Piper — 1 operation(s) for chat.
  name: Chili Piper Chat API
  slug: chili-piper-chat-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The concierge API from Chili Piper — 4 operation(s) for concierge.
  name: Chili Piper Concierge API
  slug: chili-piper-concierge-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The distribution API from Chili Piper — 3 operation(s) for distribution.
  name: Chili Piper Distribution API
  slug: chili-piper-distribution-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The distro API from Chili Piper — 7 operation(s) for distro.
  name: Chili Piper Distro API
  slug: chili-piper-distro-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The meeting-type API from Chili Piper — 4 operation(s) for meeting-type.
  name: Chili Piper Meeting Type API
  slug: chili-piper-meeting-type-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The meeting-type-reminder API from Chili Piper — 3 operation(s) for meeting-type-reminder.
  name: Chili Piper Meeting Type Reminder API
  slug: chili-piper-meeting-type-reminder-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The meetings API from Chili Piper — 4 operation(s) for meetings.
  name: Chili Piper Meetings API
  slug: chili-piper-meetings-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The rule API from Chili Piper — 2 operation(s) for rule.
  name: Chili Piper Rule API
  slug: chili-piper-rule-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The team API from Chili Piper — 5 operation(s) for team.
  name: Chili Piper Team API
  slug: chili-piper-team-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The tenant API from Chili Piper — 1 operation(s) for tenant.
  name: Chili Piper Tenant API
  slug: chili-piper-tenant-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The user API from Chili Piper — 4 operation(s) for user.
  name: Chili Piper User API
  slug: chili-piper-user-api
- baseURL: https://fire.chilipiper.com/api/fire-edge
  baseurl_source: declared
  description: The workspace API from Chili Piper — 4 operation(s) for workspace.
  name: Chili Piper Workspace API
  slug: chili-piper-workspace-api
- baseURL: https://fire.chilipiper.com/api/fire-edge/v1/org/mcp
  baseurl_source: declared
  description: The Hand off API from Chili Piper — 3 operation(s) for hand off.
  name: Chili Piper Hand off API
  slug: chili-piper-hand-off-api
- baseURL: https://fire.chilipiper.com/api/fire-edge/v1/org/mcp
  baseurl_source: declared
  description: The Scheduling Links API from Chili Piper — 13 operation(s) for scheduling links.
  name: Chili Piper Scheduling Links API
  slug: chili-piper-scheduling-links-api
artifact_total: 63
asyncapis:
- description: ''
  name: Chili Piper Webhooks
  slug: chili-piper-webhooks
collections:
- collection_type: open
  name: Chili Piper — Inspector Actions Availability API
  slug: open-chili-piper-availability-api
- collection_type: open
  name: Chili Piper — Conversation Inspector Actions Chat API
  slug: open-chili-piper-chat-api
- collection_type: open
  name: Chili Piper Concierge API
  slug: open-chili-piper-concierge-api
- collection_type: open
  name: Chili Piper Distribution API
  slug: open-chili-piper-distribution-api
- collection_type: open
  name: Chili Piper Distro API
  slug: open-chili-piper-distro-api
- collection_type: open
  name: Chili Piper — Router Configuration Actions Handoff API
  slug: open-chili-piper-handoff-api
- collection_type: open
  name: Chili Piper Meeting Type API
  slug: open-chili-piper-meeting-type-api
- collection_type: open
  name: Chili Piper — Meeting Type Management Actions Meeting Type Reminder API
  slug: open-chili-piper-meeting-type-reminder-api
- collection_type: open
  name: Chili Piper Meetings API
  slug: open-chili-piper-meetings-api
- collection_type: open
  name: Chili Piper Rule API
  slug: open-chili-piper-rule-api
- collection_type: open
  name: Chili Piper Scheduling Links API
  slug: open-chili-piper-schedulinglinks-api
- collection_type: open
  name: Chili Piper Team API
  slug: open-chili-piper-team-api
- collection_type: open
  name: Chili Piper — Concierge Router Builder Actions Tenant API
  slug: open-chili-piper-tenant-api
- collection_type: open
  name: Chili Piper User API
  slug: open-chili-piper-user-api
- collection_type: open
  name: Chili Piper Workspace API
  slug: open-chili-piper-workspace-api
common:
- group: other
  href: https://artifacts.apis.io/chili-piper/capabilities/chili-piper-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/chili-piper-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/chili-piper/agentic-access/chili-piper-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chili-piper-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/chili-piper/overlays/chili-piper-availability-inspector-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/chili-piper-availability-inspector-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.chilipiper.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.chilipiper.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://help.chilipiper.com/hc/en-us/articles/35576029581971-Edge-API-References
- group: start
  title: ''
  type: GettingStarted
  url: https://help.chilipiper.com/hc/en-us/articles/30935152032275-Using-Concierge-via-the-Edge-API
- group: operate
  title: ''
  type: Support
  url: https://help.chilipiper.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.chilipiper.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chili-Piper
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chilipiper.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.chilipiper.com/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chilipiper.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chilipiper.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chilipiper.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.chilipiper.com/security
- group: auth
  title: ''
  type: Security
  url: https://github.com/Chili-Piper/mcp-assets/blob/main/SECURITY.md
- group: agent
  href: https://artifacts.apis.io/chili-piper/llms/chili-piper-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chili-piper-llms.txt
- group: build
  href: https://artifacts.apis.io/chili-piper/packages/chili-piper-packages.yml
  title: ''
  type: Packages
  url: packages/chili-piper-packages.yml
- group: build
  href: https://artifacts.apis.io/chili-piper/packages/chili-piper-packages.yml
  title: ''
  type: SDKs
  url: packages/chili-piper-packages.yml
- group: design
  href: https://artifacts.apis.io/chili-piper/components/chili-piper-components.yml
  title: ''
  type: Components
  url: components/chili-piper-components.yml
- group: agent
  href: https://artifacts.apis.io/chili-piper/well-known/chili-piper-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chili-piper-well-known.yml
- group: auth
  href: https://artifacts.apis.io/chili-piper/authentication/chili-piper-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chili-piper-authentication.yml
- group: auth
  href: https://artifacts.apis.io/chili-piper/scopes/chili-piper-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/chili-piper-scopes.yml
- group: design
  href: https://artifacts.apis.io/chili-piper/conventions/chili-piper-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chili-piper-conventions.yml
- group: design
  href: https://artifacts.apis.io/chili-piper/errors/chili-piper-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chili-piper-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chili-piper/lifecycle/chili-piper-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/chili-piper-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/chili-piper/conformance/chili-piper-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chili-piper-conformance.yml
- group: auth
  href: https://artifacts.apis.io/chili-piper/security/chili-piper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chili-piper-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/chili-piper/security/chili-piper-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chili-piper-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/chili-piper/data-model/chili-piper-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chili-piper-data-model.yml
- group: design
  href: https://artifacts.apis.io/chili-piper/asyncapi/chili-piper-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/chili-piper-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/chili-piper/changelog/chili-piper-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chili-piper-changelog.yml
- group: agent
  href: https://artifacts.apis.io/chili-piper/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.chilipiper.com/
- group: agent
  href: https://artifacts.apis.io/chili-piper/mcp/chili-piper-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chili-piper-mcp.yml
- group: build
  href: https://artifacts.apis.io/chili-piper/mcp/chili-piper-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/chili-piper-tool-crosswalk.yml
- group: commercial
  href: https://artifacts.apis.io/chili-piper/plans/chili-piper-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chili-piper-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/chili-piper/rate-limits/chili-piper-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chili-piper-rate-limits.yml
created: '2026-08-09'
description: Chili Piper is a demand conversion platform for B2B go-to-market teams, founded in 2016 by Alina and Nicolas Vandenberghe and headquartered in New York. Its products - Concierge, Distro, Handoff, Chat AI, Web Experiences, Re-engagement and ChiliCal - turn inbound website visitors and form submissions into booked meetings by qualifying, enriching, routing and scheduling leads against Salesforce or HubSpot ownership, territory and round-robin distribution logic. For developers, Chili Piper publishes the Edge API (https://fire.chilipiper.com/api/fire-edge), a bearer-token REST surface covering users, workspaces, teams, routing rules, distributions, meetings, meeting types, scheduling links, handoff and Concierge routing; a hosted remote MCP server with 55 documented tools; official Agent Skills and ChatGPT GPT actions published under the Chili-Piper GitHub organization; a Concierge JavaScript embed distributed on npm; and custom webhooks for booked, updated and cancelled meetings.
finops:
- has_sources: true
  method: derived
  name: Chili Piper Finops
  primary_unit: user
  service_category: ''
  slug: chili-piper-finops
  template: false
image: https://cdn.prod.website-files.com/61c9fe00acd90d7271f7014e/63d787acdbdc86179f01ed1a_Favicon%20(1).png
layout: provider
mcp_servers:
- description: Remote MCP server at fire.chilipiper.com over HTTP; 55 tools listed.
  name: Chili Piper MCP Server
  slug: chili-piper
modified: '2026-08-13'
name: Chili Piper
nav: Providers
network: true
overview: 'Chili Piper publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Availability API, Chat API, Concierge API, and 13 more. Tagged areas include Scheduling, Lead Routing, Meetings, Sales, and Marketing.


  The Chili Piper catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Chili Piper''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Chili Piper Plans Pricing
  plan_count: 4
  slug: chili-piper-plans-pricing
- name: Chili Piper Price Estimates
  plan_count: 0
  slug: chili-piper-price-estimates
random_paper: 6
rate_limits:
- limit_count: 0
  name: Chili Piper Rate Limits
  slug: chili-piper-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Chili Piper API Rules
  rule_count: 63
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 9
  slug: chili-piper-rules
scopes:
- name: Chili Piper Scopes
  scope_count: 0
  slug: chili-piper-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 69.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 61.9
    discoverability: 80.0
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 69.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/chili-piper/chili-piper-2026-08-17T080410.png
security:
- kind: authentication
  name: Chili Piper Authentication
  slug: chili-piper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chili Piper Domain Security
  slug: chili-piper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chili Piper Vulnerability Disclosure
  slug: chili-piper-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Chili Piper Trust Center
  slug: chili-piper-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 19
skills:
- name: availability-inspector
  slug: chili-piper-availability-inspector
- name: chat-conversation-inspector
  slug: chili-piper-chat-conversation-inspector
- name: concierge-debugger
  slug: chili-piper-concierge-debugger
- name: concierge-router-builder
  slug: chili-piper-concierge-router-builder
- name: concierge-router-configuration
  slug: chili-piper-concierge-router-configuration
- name: distribution-analysis
  slug: chili-piper-distribution-analysis
- name: distro-debugger
  slug: chili-piper-distro-debugger
- name: distro-router-configuration
  slug: chili-piper-distro-router-configuration
- name: handoff-router-configuration
  slug: chili-piper-handoff-router-configuration
- name: meeting-inspector
  slug: chili-piper-meeting-inspector
- name: meeting-type-management
  slug: chili-piper-meeting-type-management
- name: no-show-analyzer
  slug: chili-piper-no-show-analyzer
- name: org-meeting
  slug: chili-piper-org-meeting
- name: routing-audit
  slug: chili-piper-routing-audit
- name: scheduling-link-management
  slug: chili-piper-scheduling-link-management
- name: user-copy
  slug: chili-piper-user-copy
- name: user-details
  slug: chili-piper-user-details
- name: user-meetings
  slug: chili-piper-user-meetings
- name: user-offboarding
  slug: chili-piper-user-offboarding
slug: chili-piper
tags:
- Scheduling
- Lead Routing
- Meetings
- Sales
- Marketing
- CRM
- Demand Conversion
- Appointment Booking
- Revenue Operations
- Calendar
- Agents
- MCP
website: https://www.chilipiper.com/
---
