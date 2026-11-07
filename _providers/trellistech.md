---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.trellistech.com/api/v1
  baseurl_source: declared
  description: Trellis property contracts generated from Hono/Zod schemas.
  name: Trellis Properties API
  slug: trellistech-properties-api
- baseURL: https://app.trellistech.com/api/v1
  baseurl_source: declared
  description: Trellis task contracts generated from Hono/Zod schemas.
  name: Trellis Tasks API
  slug: trellistech-tasks-api
artifact_total: 14
collections:
- collection_type: open
  name: Trellis Public API v1 properties API
  slug: open-trellistech-properties-api
- collection_type: open
  name: Trellis Public API v1 properties tasks API
  slug: open-trellistech-tasks-api
common:
- group: commercial
  href: https://artifacts.apis.io/trellistech/plans/trellistech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trellistech-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/trellistech/capabilities/trellistech-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trellistech-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/trellistech/overlays/trellistech-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trellistech-public-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/trellistech/llms/trellistech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trellistech-llms.txt
- group: agent
  href: https://artifacts.apis.io/trellistech/mcp/trellistech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trellistech-mcp.yml
- group: build
  href: https://artifacts.apis.io/trellistech/packages/trellistech-packages.yml
  title: ''
  type: Packages
  url: packages/trellistech-packages.yml
- group: build
  href: https://artifacts.apis.io/trellistech/cli/trellistech-cli.yml
  title: ''
  type: CLI
  url: cli/trellistech-cli.yml
- group: operate
  href: https://artifacts.apis.io/trellistech/changelog/trellistech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/trellistech-changelog.yml
- group: design
  href: https://artifacts.apis.io/trellistech/lifecycle/trellistech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trellistech-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trellistech.com
- group: agent
  href: https://artifacts.apis.io/trellistech/well-known/trellistech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trellistech-well-known.yml
- group: auth
  href: https://artifacts.apis.io/trellistech/security/trellistech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trellistech-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/trellistech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.trellistech.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trellistech.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trellistech.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trellistech.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.trellistech.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trellis-tech
- group: start
  title: ''
  type: SignUp
  url: https://app.trellistech.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@trellistech.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trellistech.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trellistech.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.trellistech.com
created: '2026-07-17'
description: Trellis (Trellistech) is a Y Combinator-backed, AI-powered property operations platform for short-term and vacation rental operators. Trellis deploys AI agents across an operator's entire business - handling guest communications, coordinating field teams, and running day-to-day operations such as tasks, workforce scheduling, accounting, reviews, and the guest portal. For developers, Trellis publishes a versioned public REST API for CRUD access to tasks and properties, an official hosted MCP server (@trellistech/mcp-server) that exposes operational read and gated write tools to any MCP-compatible AI client, and connectors for property and finance systems including Guesty, Hostaway, Breezeway, Calry, Krossbooking, and Ramp.
finops:
- has_sources: true
  method: derived
  name: Trellistech Finops
  primary_unit: scales with property count
  service_category: ''
  slug: trellistech-finops
  template: false
image: https://www.trellistech.com/trellis-icon.svg
layout: provider
mcp_servers:
- description: Official Trellis Model Context Protocol server. Lets external AI clients use Trellis operational tools through a standard MCP connection - a hosted Streamable HTTP endpoint, or a stdio bridge from the
  name: Trellis MCP Server
  slug: trellis-mcp-server
modified: '2026-07-21'
name: Trellis
nav: Providers
network: true
overview: 'Trellis publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Properties API and Tasks API. Tagged areas include Company, Property Management, Vacation Rentals, Short-Term Rental, and AI Agents.


  The Trellis catalog on APIs.io includes 1 Spectral governance ruleset.


  Trellis'' developer surface includes CLI, changelog, documentation, API reference, getting-started guide, engineering blog, signup flow, and 17 more developer resources.'
plans:
- name: Trellistech Plans Pricing
  plan_count: 2
  slug: trellistech-plans-pricing
- name: Trellistech Price Estimates
  plan_count: 0
  slug: trellistech-price-estimates
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Trellis API Rules
  rule_count: 57
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 1
  slug: trellistech-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 47.8
    developer_ergonomics: 66.1
    discoverability: 71.7
    operational_transparency: 34.2
  previous_composite: 49.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trellistech/trellistech-2026-08-17T082435.png
security:
- kind: authentication
  name: Trellistech Authentication
  slug: trellistech-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Trellistech Domain Security
  slug: trellistech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Trellis Create & Assign Maintenance Task
  slug: trellistech-create-maintenance-task
- name: Trellis Daily Work-Orders Report
  slug: trellistech-daily-work-orders-report
- name: Trellis Onboard Property
  slug: trellistech-onboard-property
slug: trellistech
tags:
- Company
- Property Management
- Vacation Rentals
- Short-Term Rental
- AI Agents
- Hospitality
- Task Management
- MCP
website: https://www.trellistech.com
---
