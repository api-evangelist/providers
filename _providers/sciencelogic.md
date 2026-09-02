---
access_model:
  confidence: high
  label: Commercial, per managed device per month, with a 14-day trial
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://sciencelogic.com/why-sciencelogic/pricing
  trial: true
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.9
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: The ScienceLogic AI Platform (Skylar) — AIOps, IT infrastructure and application observability, service management, network configuration compliance, and automated remediation.
  name: ScienceLogic
  slug: sciencelogic
- description: The REST API for Skylar Compliance (formerly Restorepoint) — ScienceLogic's network configuration and change management product. 314 operations across 193 paths covering devices, configuration backups
  name: Skylar Compliance API
  slug: skylar-compliance-api
- description: 'The GraphQL API for Skylar One (formerly SL1). ScienceLogic''s forward-looking interface — the default AP2 user interface uses it exclusively and makes no REST calls, and performance and log data held '
  name: Skylar One GraphQL API
  slug: skylar-one-graphql-api
- description: The REST API for Skylar One (formerly SL1), giving external systems programmatic access to tickets, devices, organizations, events, monitoring policies, dynamic applications, schedules, thresholds and
  name: Skylar One REST API
  slug: skylar-one-rest-api
- description: 'A FastMCP server published by the ScienceLogic GitHub organization exposing 22 read-only tools across two sub-servers — Skylar One (backed by the SL1 GraphQL API) and Skylar Compliance (backed by the '
  name: ScienceLogic MCP Server
  slug: sciencelogic-mcp
artifact_total: 13
asyncapis:
- description: ''
  name: Sciencelogic Webhooks
  slug: sciencelogic-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://sciencelogic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sciencelogic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sciencelogic.com/dev-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sciencelogic.com/skylar_compliance/api/5-6/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sciencelogic.com/latest/Content/Web_Content_Dev_and_Integration/ScienceLogic_API/api_intro.htm
- group: company
  title: ''
  type: Blog
  url: https://sciencelogic.com/feed
- group: operate
  title: ''
  type: Support
  url: https://support.sciencelogic.com/s/
- group: operate
  title: ''
  type: Community
  url: https://community.sciencelogic.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScienceLogic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sciencelogic
- group: commercial
  title: ''
  type: Pricing
  url: https://sciencelogic.com/why-sciencelogic/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sciencelogic.com/get-free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sciencelogic.com/company/standard-terms-and-conditions-v20260116
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sciencelogic.com/company/legal
- group: auth
  title: ''
  type: Authentication
  url: authentication/sciencelogic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sciencelogic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sciencelogic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sciencelogic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sciencelogic-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sciencelogic-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sciencelogic-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sciencelogic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sciencelogic-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sciencelogic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sciencelogic-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sciencelogic-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/sciencelogic-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sciencelogic-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sciencelogic-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sciencelogic-skylar-compliance-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sciencelogic-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sciencelogic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sciencelogic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sciencelogic-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sciencelogic-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sciencelogic.com/llms.txt
created: '2026-03-27'
description: ScienceLogic is an AIOps and IT operations company whose ScienceLogic AI Platform — rebranded in 2026 as the Skylar family — covers infrastructure and application observability, network configuration and compliance, and workflow automation. Skylar One (formerly SL1) is the observability platform, with a REST API and a GraphQL API served from the customer's own Administration Portal, All-In-One Appliance or Database Server; ScienceLogic states that GraphQL is the forward path and that the REST API is now limited to bug fixes. Skylar Compliance (formerly Restorepoint, acquired by ScienceLogic) publishes a 314-operation OpenAPI 3.0 contract for configuration backup, change detection, compliance policy testing and device restore. Skylar Automation (formerly PowerFlow) handles ITSM and CMDB integration, and Skylar AI adds Advisor and Analytics on top. The ScienceLogic GitHub organization also publishes an MCP server that exposes read-only Skylar One and Skylar Compliance tools to
  AI agents. Products are deployed on customer appliances, SaaS, or private/public cloud, and are licensed per managed device per month.
finops:
- name: Sciencelogic Finops
  service_category: API
  slug: sciencelogic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sciencelogic.png
layout: provider
mcp_servers:
- description: 'A FastMCP server published by the ScienceLogic GitHub organization that gives AI agents access to ScienceLogic products through their existing APIs. It mounts two sub-servers in one process: Skylar Co'
  name: ScienceLogic MCP (mcp-sl)
  slug: sciencelogic-mcp-mcp-sl
modified: '2026-08-29'
name: ScienceLogic
nav: Providers
network: true
overview: 'ScienceLogic publishes 1 API on the [APIs.io](https://apis.io/) network: Skylar Compliance API. Tagged areas include AIOps, IT Operations, Observability, Monitoring, and Network Configuration Management.


  The ScienceLogic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ScienceLogic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Sciencelogic Plans Pricing
  plan_count: 4
  slug: sciencelogic-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Sciencelogic Rate Limits
  slug: sciencelogic-rate-limits
score:
  band: strong
  composite: 58.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 3.4
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 0.0
    contract_quality: 59.2
    developer_ergonomics: 58.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 54.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/screenshots/sciencelogic-2026-06-20T193537.png
security:
- kind: authentication
  name: Sciencelogic Authentication
  slug: sciencelogic-authentication
  summary_line: apiKey/openIdConnect · 3 schemes
- kind: domain-security
  name: Sciencelogic Domain Security
  slug: sciencelogic-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Sciencelogic Trust Center
  slug: sciencelogic-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, CSA STAR
slug: sciencelogic
tags:
- AIOps
- IT Operations
- Observability
- Monitoring
- Network Configuration Management
- Compliance
- Automation
- Incident Management
website: https://sciencelogic.com
---
