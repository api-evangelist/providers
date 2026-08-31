---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans/permutive-plans-pricing.yml
  - https://permutive.com/request-a-demo
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Permutive Agentic Access
  operation_count: 23
  slug: permutive-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 11
apis:
- description: Retrieve contextual cohort targeting values for a page URL without processing any user data, for ad-server integration. Returns cohort codes, per-destination activation mappings and content classifica
  name: Permutive Contextual API
  slug: permutive-contextual-api
- description: Permutive's Model Context Protocol surface. A live, anonymous documentation MCP server at https://docs.permutive.com/mcp (search, virtual-filesystem query, feedback), plus an invitation-only audience-
  name: Permutive MCP Server
  slug: permutive-mcp
- description: The API version 1 API from Permutive — 2 operation(s) for api version 1.
  name: Permutive API version 1 API
  slug: permutive-api-version-1-api
- description: The v1 API from Permutive — 5 operation(s) for v1.
  name: Permutive V1 API
  slug: permutive-v1-api
- description: The v2.0 API from Permutive — 4 operation(s) for v2.0.
  name: Permutive V2.0 API
  slug: permutive-v2-0-api
- description: The v2 API from Permutive — 2 operation(s) for v2.
  name: Permutive V2 API
  slug: permutive-v2-api
artifact_total: 22
asyncapis:
- description: ''
  name: Permutive Webhooks
  slug: permutive-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cohorts API
  slug: open-permutive-cohorts-api
- collection_type: open
  name: Permutive Cohorts Contextual API
  slug: open-permutive-contextual-api
- collection_type: open
  name: Events API
  slug: open-permutive-events-api
- collection_type: open
  name: Identity API
  slug: open-permutive-identity-api
- collection_type: open
  name: Custom Cohort Segmentation API
  slug: open-permutive-segmentation-api
- collection_type: open
  name: Taxonomy API
  slug: open-permutive-taxonomy-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/permutive-manage-cohorts.md
- group: other
  title: ''
  type: Overlay
  url: overlays/permutive-events-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/permutive-track-and-identify.md
- group: other
  title: ''
  type: Overlay
  url: overlays/permutive-identity-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/permutive-segmentation-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/permutive-segment-without-an-sdk.md
- group: other
  title: ''
  type: Overlay
  url: overlays/permutive-taxonomy-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/permutive-manage-import-taxonomy.md
- group: company
  title: ''
  type: Website
  url: https://permutive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.permutive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.permutive.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.permutive.com/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.permutive.com/introduction
- group: start
  title: ''
  type: Quickstart
  url: https://docs.permutive.com/implementation-overview
- group: company
  title: ''
  type: Blog
  url: https://permutive.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/permutive-engineering
- group: operate
  title: ''
  type: Support
  url: https://support.permutive.com/
- group: start
  title: ''
  type: Login
  url: https://dash.permutive.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://permutive.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://permutive.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.permutive.com/
- group: auth
  title: ''
  type: Security
  url: https://docs.permutive.com/governance/security
- group: auth
  title: ''
  type: Compliance
  url: https://trust.permutive.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/permutive-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/permutive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/permutive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/permutive-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/permutive-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/permutive-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/permutive-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/permutive-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/permutive-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/permutive-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/permutive-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/permutive-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/permutive-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/permutive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/permutive-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/permutive-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/permutive-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/permutive-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/permutive-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/permutive-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/permutive-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/permutive-cohorts-api-overlay.yaml
created: '2026-07-17'
description: Permutive is a predictive data collaboration and activation platform for premium publishers, advertisers and agencies. Its platform spans a Data Management Platform, a Data Clean Room for privacy-safe collaboration with 150+ premium publishers, AI-curated audiences, and the Halo agentic suite that scales direct buying. The developer platform exposes six REST APIs — Events, Identity, Contextual, Custom Cohort Segmentation, Cohorts and Taxonomy — plus web, mobile and CTV SDKs, an anonymous documentation Model Context Protocol server, and an invitation-only audience-intelligence MCP server that makes cohort discovery, reach measurement and audience comparison available to AI agents. Authentication is a workspace-scoped API key; every call is bounded by the workspace that owns the key.
image: https://mintcdn.com/permutive/zX9G7jjpccuZZlEf/logo/permutive-logo-light.svg
layout: provider
mcp_servers:
- description: ''
  name: Permutive MCP Server
  slug: permutive-mcp-server
modified: '2026-08-13'
name: Permutive
nav: Providers
network: true
overview: 'Permutive publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contextual API, API version 1 API, V1 API, and 2 more. Tagged areas include Company, Publishing, Advertising, AdTech, and MarTech.


  The Permutive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Permutive''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, support, authentication, and 39 more developer resources.'
plans:
- name: Permutive Plans Pricing
  plan_count: 0
  slug: permutive-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Permutive Rate Limits
  slug: permutive-rate-limits
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 24
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 60.2
    developer_ergonomics: 66.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 16.7
      total: 6
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/permutive/refs/heads/main/screenshots/permutive-2026-08-17T081200.png
security:
- kind: authentication
  name: Permutive Authentication
  slug: permutive-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Permutive Domain Security
  slug: permutive-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Permutive Vulnerability Disclosure
  slug: permutive-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Permutive Trust Center
  slug: permutive-trust-center
  summary_line: SOC 2 Type II, SOC 3
slug: permutive
tags:
- Company
- Publishing
- Advertising
- AdTech
- MarTech
- Audience
- Data Collaboration
- Data Management Platform
- Contextual
- Identity
- Segmentation
- Agents
website: https://permutive.com/
---
