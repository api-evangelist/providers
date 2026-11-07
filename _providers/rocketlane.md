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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Rocketlane Agentic Access
  operation_count: 76
  slug: rocketlane-agentic-access
  summary_line: 76 operations · 46 acting
api_count: 1
apis:
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for comments resource
  name: Rocketlane Comments API
  slug: rocketlane-comments-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for conversations resource
  name: Rocketlane Conversations API
  slug: rocketlane-conversations-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for fields resource
  name: Rocketlane Fields API
  slug: rocketlane-fields-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for invoices resource
  name: Rocketlane Invoices API
  slug: rocketlane-invoices-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for phases resource
  name: Rocketlane Phases API
  slug: rocketlane-phases-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for projects resource
  name: Rocketlane Projects API
  slug: rocketlane-projects-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for resource allocation resource
  name: Rocketlane Resource Allocations API
  slug: rocketlane-resource-allocations-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for space tabs resource
  name: Rocketlane Space Documents API
  slug: rocketlane-space-documents-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for space resource
  name: Rocketlane Spaces API
  slug: rocketlane-spaces-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for tasks resource
  name: Rocketlane Tasks API
  slug: rocketlane-tasks-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for time-offs resource
  name: Rocketlane Time-Offs API
  slug: rocketlane-time-offs-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for time entries and timesheets
  name: Rocketlane Time Tracking API
  slug: rocketlane-time-tracking-api
- baseURL: https://api.rocketlane.com/api/1.0/
  baseurl_source: declared
  description: Endpoints for users resource
  name: Rocketlane Users API
  slug: rocketlane-users-api
artifact_total: 39
asyncapis:
- description: ''
  name: Rocketlane Webhooks
  slug: rocketlane-webhooks
collections:
- collection_type: open
  name: Rocketlane Comments API
  slug: open-rocketlane-comments-api
- collection_type: open
  name: Rocketlane Comments Conversations API
  slug: open-rocketlane-conversations-api
- collection_type: open
  name: Rocketlane Comments Fields API
  slug: open-rocketlane-fields-api
- collection_type: open
  name: Rocketlane Comments Invoices API
  slug: open-rocketlane-invoices-api
- collection_type: open
  name: Rocketlane Comments Phases API
  slug: open-rocketlane-phases-api
- collection_type: open
  name: Rocketlane Comments Projects API
  slug: open-rocketlane-projects-api
- collection_type: open
  name: Rocketlane Comments Resource Allocations API
  slug: open-rocketlane-resource-allocations-api
- collection_type: open
  name: Rocketlane Comments Space Documents API
  slug: open-rocketlane-space-documents-api
- collection_type: open
  name: Rocketlane Comments Spaces API
  slug: open-rocketlane-spaces-api
- collection_type: open
  name: Rocketlane Comments Tasks API
  slug: open-rocketlane-tasks-api
- collection_type: open
  name: Rocketlane Comments Time-Offs API
  slug: open-rocketlane-time-offs-api
- collection_type: open
  name: Rocketlane Comments Time Tracking API
  slug: open-rocketlane-time-tracking-api
- collection_type: open
  name: Rocketlane Comments Users API
  slug: open-rocketlane-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/rocketlane/plans/rocketlane-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rocketlane-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/rocketlane/capabilities/rocketlane-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/rocketlane-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/rocketlane/agentic-access/rocketlane-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rocketlane-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.rocketlane.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.rocketlane.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.rocketlane.com/reference/tasks
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.rocketlane.com/docs/overview
- group: operate
  title: ''
  type: Support
  url: https://help.rocketlane.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.rocketlane.com/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rocketlane.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.rocketlane.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.rocketlane.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rocketlane.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rocketlane.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rocketlane
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rocketlane.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.rocketlane.com/trust
- group: auth
  title: ''
  type: Security
  url: https://www.rocketlane.com/responsible-disclosure
- group: agent
  href: https://artifacts.apis.io/rocketlane/llms/rocketlane-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rocketlane-llms.txt
- group: agent
  href: https://artifacts.apis.io/rocketlane/well-known/rocketlane-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rocketlane-well-known.yml
- group: build
  href: https://artifacts.apis.io/rocketlane/packages/rocketlane-packages.yml
  title: ''
  type: Packages
  url: packages/rocketlane-packages.yml
- group: build
  href: https://artifacts.apis.io/rocketlane/cli/rocketlane-cli.yml
  title: ''
  type: CLI
  url: cli/rocketlane-cli.yml
- group: agent
  href: https://artifacts.apis.io/rocketlane/mcp/rocketlane-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rocketlane-mcp.yml
- group: auth
  href: https://artifacts.apis.io/rocketlane/authentication/rocketlane-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rocketlane-authentication.yml
- group: design
  href: https://artifacts.apis.io/rocketlane/conventions/rocketlane-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rocketlane-conventions.yml
- group: design
  href: https://artifacts.apis.io/rocketlane/asyncapi/rocketlane-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rocketlane-webhooks.yml
- group: design
  href: https://artifacts.apis.io/rocketlane/lifecycle/rocketlane-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rocketlane-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rocketlane/conformance/rocketlane-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rocketlane-conformance.yml
- group: design
  href: https://artifacts.apis.io/rocketlane/data-model/rocketlane-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rocketlane-data-model.yml
- group: docs
  href: https://artifacts.apis.io/rocketlane/openapi/_original/rocketlane-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/rocketlane-openapi-original.json
- group: other
  href: https://artifacts.apis.io/rocketlane/overlays/rocketlane-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rocketlane-overlay.yaml
- group: design
  href: https://artifacts.apis.io/rocketlane/errors/rocketlane-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rocketlane-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/rocketlane/rate-limits/rocketlane-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rocketlane-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/rocketlane/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/rocketlane/security/rocketlane-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/rocketlane-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/rocketlane/security/rocketlane-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rocketlane-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rocketlane/security/rocketlane-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rocketlane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rocketlane.com
created: '2026-07-17'
description: Rocketlane is an AI-powered Professional Services Automation (PSA) platform that unifies customer onboarding, project delivery, resource management, time tracking, and professional-services financials in one system. Its public REST API (base https://api.rocketlane.com/api/1.0/) exposes projects, tasks, phases, spaces, space documents, custom fields, time entries, time-offs, resource allocations, users, and invoices, authenticated with a workspace api-key header and paginated with cursors. Outbound webhooks broadcast task, project, and phase lifecycle events, and a first-party CLI (@rocketlane/rli) supports building apps for the Rocketlane Marketplace. Originally added to the API Evangelist network as a portfolio-company lead (8vc, Insight Partners); enriched from its live developer surface.
finops:
- has_sources: true
  method: derived
  name: Rocketlane Finops
  primary_unit: team member
  service_category: ''
  slug: rocketlane-finops
  template: false
image: https://cdn.prod.website-files.com/6360d3edc696260ba2aecbc7/64e613d0f901abbf2430f1f8_banner.webp
layout: provider
modified: '2026-07-21'
name: Rocketlane
nav: Providers
network: true
overview: 'Rocketlane publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comments API, Conversations API, Fields API, and 10 more. Tagged areas include Company, Professional Services Automation, Project Management, Customer Onboarding, and Resource Management.


  The Rocketlane catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Rocketlane''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Rocketlane Plans Pricing
  plan_count: 6
  slug: rocketlane-plans-pricing
- name: Rocketlane Price Estimates
  plan_count: 0
  slug: rocketlane-price-estimates
random_paper: 8
rate_limits:
- limit_count: 2
  name: Rocketlane Rate Limits
  slug: rocketlane-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Rocketlane API Rules
  rule_count: 59
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 8
  slug: rocketlane-rules
score:
  band: exemplar
  composite: 69.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 59.1
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 57.9
  previous_composite: 65.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
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
screenshot: https://apis.io/screenshots/rocketlane/rocketlane-2026-08-17T081626.png
security:
- kind: authentication
  name: Rocketlane Authentication
  slug: rocketlane-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rocketlane Domain Security
  slug: rocketlane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rocketlane Vulnerability Disclosure
  slug: rocketlane-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Rocketlane Trust Center
  slug: rocketlane-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, CSA STAR
skill_count: 2
skills:
- name: Create a Rocketlane project from a template and add members
  slug: rocketlane-create-project-from-template
- name: Create a task and log time against it
  slug: rocketlane-task-and-time-tracking
slug: rocketlane
tags:
- Company
- Professional Services Automation
- Project Management
- Customer Onboarding
- Resource Management
- Time Tracking
- PSA
- Software-as-a-Service
website: https://rocketlane.com
---
