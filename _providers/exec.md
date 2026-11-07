---
access_model:
  confidence: high
  label: Free tier, then self-serve checkout
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - authentication
  - https://www.exec.com/pricing
  - https://docs.exec.com/platform/plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Exec Agentic Access
  operation_count: 32
  slug: exec-agentic-access
  summary_line: 32 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.exec.com/rest/v1
  baseurl_source: declared
  description: The Collections API from Exec — 1 operation(s) for collections.
  name: Exec Collections API
  slug: exec-collections-api
- baseURL: https://api.exec.com/rest/v1
  baseurl_source: declared
  description: The Knowledge Hub - Folders API from Exec — 2 operation(s) for knowledge hub - folders.
  name: Exec Knowledge Hub - Folders API
  slug: exec-knowledge-hub-folders-api
- baseURL: https://api.exec.com/rest/v1
  baseurl_source: declared
  description: The Knowledge Hub - Pages API from Exec — 3 operation(s) for knowledge hub - pages.
  name: Exec Knowledge Hub - Pages API
  slug: exec-knowledge-hub-pages-api
- baseURL: https://api.exec.com/rest/v1
  baseurl_source: declared
  description: The Knowledge Hub - Sources API from Exec — 2 operation(s) for knowledge hub - sources.
  name: Exec Knowledge Hub - Sources API
  slug: exec-knowledge-hub-sources-api
- baseURL: https://api.exec.com/rest/v1
  baseurl_source: declared
  description: The Scenario Studio API from Exec — 3 operation(s) for scenario studio.
  name: Exec Scenario Studio API
  slug: exec-scenario-studio-api
- baseURL: https://api.exec.com/rest/v1
  baseurl_source: declared
  description: The Scenarios API from Exec — 6 operation(s) for scenarios.
  name: Exec Scenarios API
  slug: exec-scenarios-api
- baseURL: https://api.exec.com/rest/v1
  baseurl_source: declared
  description: The Sessions API from Exec — 2 operation(s) for sessions.
  name: Exec Sessions API
  slug: exec-sessions-api
- baseURL: https://api.exec.com/rest/v1
  baseurl_source: declared
  description: The Skills API from Exec — 2 operation(s) for skills.
  name: Exec Skills API
  slug: exec-skills-api
- baseURL: https://api.exec.com/rest/v1
  baseurl_source: declared
  description: The Workspace API from Exec — 3 operation(s) for workspace.
  name: Exec Workspace API
  slug: exec-workspace-api
artifact_total: 32
asyncapis:
- description: ''
  name: Exec Webhooks
  slug: exec-webhooks
collections:
- collection_type: open
  name: Exec Collections API
  slug: open-exec-collections-api
- collection_type: open
  name: Exec Collections Knowledge Hub - Folders API
  slug: open-exec-knowledge-hub-folders-api
- collection_type: open
  name: Exec Collections Knowledge Hub - Pages API
  slug: open-exec-knowledge-hub-pages-api
- collection_type: open
  name: Exec Collections Knowledge Hub - Sources API
  slug: open-exec-knowledge-hub-sources-api
- collection_type: open
  name: Exec Collections Scenario Studio API
  slug: open-exec-scenario-studio-api
- collection_type: open
  name: Exec Collections Scenarios API
  slug: open-exec-scenarios-api
- collection_type: open
  name: Exec Collections Sessions API
  slug: open-exec-sessions-api
- collection_type: open
  name: Exec Collections Skills API
  slug: open-exec-skills-api
- collection_type: open
  name: Exec Collections Workspace API
  slug: open-exec-workspace-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/exec/overview
- group: other
  href: https://artifacts.apis.io/exec/capabilities/exec-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/exec-capability-edges.yml
- group: docs
  href: https://artifacts.apis.io/exec/openapi/_original/exec-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/exec-openapi-original.yml
- group: agent
  href: https://artifacts.apis.io/exec/agentic-access/exec-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/exec-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/exec/security/exec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/exec-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/exec/authentication/exec-authentication.yml
  title: ''
  type: Authentication
  url: authentication/exec-authentication.yml
- group: design
  href: https://artifacts.apis.io/exec/conventions/exec-conventions.yml
  title: ''
  type: Conventions
  url: conventions/exec-conventions.yml
- group: design
  href: https://artifacts.apis.io/exec/conventions/exec-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/exec-conventions.yml
- group: operate
  href: https://artifacts.apis.io/exec/rate-limits/exec-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/exec-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/exec/errors/exec-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/exec-error-codes.yml
- group: design
  href: https://artifacts.apis.io/exec/lifecycle/exec-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/exec-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.exec.com
- group: design
  href: https://artifacts.apis.io/exec/conformance/exec-conformance.yml
  title: ''
  type: Conformance
  url: conformance/exec-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.exec.com/enterprise-privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/exec.com/trust/j0xkhh5zesxvojinovqlpm
- group: design
  href: https://artifacts.apis.io/exec/data-model/exec-data-model.yml
  title: ''
  type: DataModel
  url: data-model/exec-data-model.yml
- group: other
  href: https://artifacts.apis.io/exec/overlays/exec-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/exec-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/exec/asyncapi/exec-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/exec-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/exec/mcp/exec-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/exec-mcp.yml
- group: build
  href: https://artifacts.apis.io/exec/mcp/exec-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/exec-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/exec/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/exec/components/exec-components.yml
  title: ''
  type: Components
  url: components/exec-components.yml
- group: commercial
  href: https://artifacts.apis.io/exec/plans/exec-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/exec-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/exec/llms/exec-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/exec-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.exec.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.exec.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.exec.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.exec.com/api-reference/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.exec.com
- group: company
  title: ''
  type: Blog
  url: https://www.exec.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.exec.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.exec.com/start
- group: start
  title: ''
  type: Login
  url: https://www.exec.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exec.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exec.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.exec.com
created: '2026-07-17'
description: 'Exec is an AI-powered roleplay and sales-training platform (exec.com) for practicing high-stakes conversations. Teams run voice-based AI roleplays, automatically score real calls, build structured programs and certifications, coach one-on-one, and manage training content in a Knowledge Hub. The Exec REST API gives programmatic access to a workspace: members and groups, scenarios and collections, roleplay sessions and analytics, skills and proficiency, Scenario Studio job creation, and Knowledge Hub pages and sources. Backed by a16z.'
finops:
- has_sources: true
  method: derived
  name: Exec Finops
  primary_unit: seat
  service_category: ''
  slug: exec-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exec.png
layout: provider
modified: '2026-08-14'
name: Exec
nav: Providers
network: true
overview: 'Exec publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Collections API, Knowledge Hub - Folders API, Knowledge Hub - Pages API, and 6 more. Tagged areas include Company, Artificial Intelligence, Sales Enablement, Training, and Roleplay.


  The Exec catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Exec''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Exec Plans Pricing
  plan_count: 4
  slug: exec-plans-pricing
- name: Exec Price Estimates
  plan_count: 0
  slug: exec-price-estimates
random_paper: 13
rate_limits:
- limit_count: 3
  name: Exec Rate Limits
  slug: exec-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Exec API Rules
  rule_count: 62
  severity_counts:
    error: 51
    hint: 0
    info: 3
    warn: 8
  slug: exec-rules
score:
  band: exemplar
  composite: 70.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 66.9
    developer_ergonomics: 65.5
    discoverability: 73.2
    operational_transparency: 47.4
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Education & Research
    regime_id: education
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/exec/exec-2026-07-25T213855.png
security:
- kind: authentication
  name: Exec Authentication
  slug: exec-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Exec Domain Security
  slug: exec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Exec Trust Center
  slug: exec-trust-center
  summary_line: SOC 2 Type II, SOC 3
skill_count: 4
skills:
- name: Assign a scenario and track team performance
  slug: exec-assign-and-track
- name: Create an AI roleplay scenario with Exec Scenario Studio
  slug: exec-create-scenario
- name: Manage Knowledge Hub pages and sources
  slug: exec-knowledge-hub
- name: Exec
  slug: exec-provider-skill
slug: exec
tags:
- Company
- Artificial Intelligence
- Sales Enablement
- Training
- Roleplay
- Coaching
- Learning
- Knowledge Management
- LMS
website: https://www.exec.com
---
