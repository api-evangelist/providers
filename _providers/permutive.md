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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Permutive Agentic Access
  operation_count: 23
  slug: permutive-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 6
apis:
- baseURL: https://api.permutive.com/ctx/v1
  baseurl_source: declared
  description: Retrieve contextual cohort targeting values for a page URL without processing any user data, for ad-server integration. Returns cohort codes, per-destination activation mappings and content classifica
  name: Permutive Contextual API
  slug: permutive-contextual-api
- description: Permutive's Model Context Protocol surface. A live, anonymous documentation MCP server at https://docs.permutive.com/mcp (search, virtual-filesystem query, feedback), plus an invitation-only audience-
  name: Permutive MCP Server
  slug: permutive-mcp
- baseURL: https://api.permutive.com/ctx/v1
  baseurl_source: declared
  description: Create, read, update and delete audience cohorts.
  name: Permutive Cohorts API
  slug: permutive-cohorts-api
- baseURL: https://api.permutive.com/ctx/v1
  baseurl_source: declared
  description: Track first-party behavioural events into Permutive.
  name: Permutive Events API
  slug: permutive-events-api
- baseURL: https://api.permutive.com/ctx/v1
  baseurl_source: declared
  description: Create user IDs and associate identities with a Permutive user.
  name: Permutive Identity API
  slug: permutive-identity-api
- baseURL: https://api.permutive.com/ctx/v1
  baseurl_source: declared
  description: Cohort-based Segmentation (CCS) — evaluate a user's events into cohorts.
  name: Permutive Segmentation API
  slug: permutive-segmentation-api
- baseURL: https://api.permutive.com/ctx/v1
  baseurl_source: declared
  description: Manage second-party data imports and their segment taxonomy.
  name: Permutive Taxonomy API
  slug: permutive-taxonomy-api
artifact_total: 29
asyncapis:
- description: ''
  name: Permutive Webhooks
  slug: permutive-webhooks
collections:
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
- group: company
  title: ''
  type: Blog
  url: https://permutive.com/news-publishers
- group: company
  title: ''
  type: BlogRSS
  url: https://permutive.com/feed
- group: agent
  href: https://artifacts.apis.io/permutive/skills/permutive-manage-cohorts.md
  title: ''
  type: AgentSkill
  url: skills/permutive-manage-cohorts.md
- group: other
  href: https://artifacts.apis.io/permutive/overlays/permutive-events-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/permutive-events-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/permutive/skills/permutive-track-and-identify.md
  title: ''
  type: AgentSkill
  url: skills/permutive-track-and-identify.md
- group: other
  href: https://artifacts.apis.io/permutive/overlays/permutive-identity-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/permutive-identity-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/permutive/overlays/permutive-segmentation-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/permutive-segmentation-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/permutive/skills/permutive-segment-without-an-sdk.md
  title: ''
  type: AgentSkill
  url: skills/permutive-segment-without-an-sdk.md
- group: other
  href: https://artifacts.apis.io/permutive/overlays/permutive-taxonomy-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/permutive-taxonomy-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/permutive/skills/permutive-manage-import-taxonomy.md
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
  href: https://artifacts.apis.io/permutive/security/permutive-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/permutive-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/permutive/security/permutive-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/permutive-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/permutive/security/permutive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/permutive-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/permutive/authentication/permutive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/permutive-authentication.yml
- group: design
  href: https://artifacts.apis.io/permutive/conventions/permutive-conventions.yml
  title: ''
  type: Conventions
  url: conventions/permutive-conventions.yml
- group: design
  href: https://artifacts.apis.io/permutive/errors/permutive-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/permutive-problem-types.yml
- group: design
  href: https://artifacts.apis.io/permutive/lifecycle/permutive-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/permutive-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/permutive/changelog/permutive-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/permutive-changelog.yml
- group: design
  href: https://artifacts.apis.io/permutive/data-model/permutive-data-model.yml
  title: ''
  type: DataModel
  url: data-model/permutive-data-model.yml
- group: design
  href: https://artifacts.apis.io/permutive/conformance/permutive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/permutive-conformance.yml
- group: operate
  href: https://artifacts.apis.io/permutive/rate-limits/permutive-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/permutive-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/permutive/plans/permutive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/permutive-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/permutive/asyncapi/permutive-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/permutive-webhooks.yml
- group: build
  href: https://artifacts.apis.io/permutive/packages/permutive-packages.yml
  title: ''
  type: Packages
  url: packages/permutive-packages.yml
- group: build
  href: https://artifacts.apis.io/permutive/packages/permutive-packages.yml
  title: ''
  type: SDKs
  url: packages/permutive-packages.yml
- group: agent
  href: https://artifacts.apis.io/permutive/mcp/permutive-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/permutive-mcp.yml
- group: build
  href: https://artifacts.apis.io/permutive/mcp/permutive-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/permutive-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/permutive/a2a/permutive-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/permutive-a2a.yml
- group: agent
  href: https://artifacts.apis.io/permutive/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/permutive/well-known/permutive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/permutive-well-known.yml
- group: agent
  href: https://artifacts.apis.io/permutive/llms/permutive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/permutive-llms.txt
- group: agent
  href: https://artifacts.apis.io/permutive/agentic-access/permutive-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/permutive-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/permutive/overlays/permutive-cohorts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/permutive-cohorts-api-overlay.yaml
created: '2026-07-17'
description: Permutive is a predictive data collaboration and activation platform for premium publishers, advertisers and agencies. Its platform spans a Data Management Platform, a Data Clean Room for privacy-safe collaboration with 150+ premium publishers, AI-curated audiences, and the Halo agentic suite that scales direct buying. The developer platform exposes six REST APIs — Events, Identity, Contextual, Custom Cohort Segmentation, Cohorts and Taxonomy — plus web, mobile and CTV SDKs, an anonymous documentation Model Context Protocol server, and an invitation-only audience-intelligence MCP server that makes cohort discovery, reach measurement and audience comparison available to AI agents. Authentication is a workspace-scoped API key; every call is bounded by the workspace that owns the key.
finops:
- has_sources: true
  method: derived
  name: Permutive Finops
  primary_unit: ''
  service_category: ''
  slug: permutive-finops
  template: true
image: https://mintcdn.com/permutive/zX9G7jjpccuZZlEf/logo/permutive-logo-light.svg
layout: provider
mcp_servers:
- description: Remote MCP server at developer.permutive.com.
  name: Permutive MCP Server
  slug: permutive-mcp-yml
modified: '2026-10-06'
name: Permutive
nav: Providers
network: true
overview: 'Permutive publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contextual API, Cohorts API, Events API, and 4 more. Tagged areas include Company, Publishing, Advertising, AdTech, and MarTech.


  The Permutive catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Permutive''s developer surface includes engineering blog, documentation, API reference, getting-started guide, quickstart, support, authentication, and 41 more developer resources.'
plans:
- name: Permutive Plans Pricing
  plan_count: 0
  slug: permutive-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Permutive Rate Limits
  slug: permutive-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Permutive API Rules
  rule_count: 59
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 2
  slug: permutive-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 23.6
    developer_ergonomics: 66.7
    discoverability: 80.0
    operational_transparency: 52.6
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/permutive/permutive-2026-08-17T081200.png
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
skill_count: 5
skills:
- name: Manage Permutive audience cohorts
  slug: permutive-manage-cohorts
- name: Manage Permutive import segment taxonomy
  slug: permutive-manage-import-taxonomy
- name: Permutive
  slug: permutive-provider-published-skill
- name: Segment users without a Permutive SDK
  slug: permutive-segment-without-an-sdk
- name: Track events and identify Permutive users
  slug: permutive-track-and-identify
slug: permutive
tags:
- Company
- Publishing
- Advertising
- AdTech
- MarTech
- Audiences
- Data Collaboration
- Data Management Platform
- Contextual
- Identity
- Segmentation
- Agents
- A2A
website: https://permutive.com/
---
