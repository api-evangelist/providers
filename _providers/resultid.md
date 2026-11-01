---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Resultid Agentic Access
  operation_count: 9
  slug: resultid-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: The Endpoints API from Resultid — 8 operation(s) for endpoints.
  name: Resultid Endpoints API
  slug: resultid-endpoints-api
- description: The Insight endpoints API from Resultid — 1 operation(s) for insight endpoints.
  name: Resultid Insight endpoints API
  slug: resultid-insight-endpoints-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Blog
  url: https://www.resultid.ai/blog/
- group: agent
  href: https://artifacts.apis.io/resultid/agentic-access/resultid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/resultid-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.resultid.ai/
- group: start
  title: ''
  type: Login
  url: https://app.resultid.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.resultid.ai/
- group: other
  title: ''
  type: X
  url: https://x.com/resultid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/resultid
- group: auth
  href: https://artifacts.apis.io/resultid/security/resultid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/resultid-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Resultid
- group: docs
  title: ''
  type: Documentation
  url: https://docs.resultid.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.resultid.com/22_api_spec_test/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.resultid.com/1_getting_started/
- group: auth
  href: https://artifacts.apis.io/resultid/authentication/resultid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/resultid-authentication.yml
- group: design
  href: https://artifacts.apis.io/resultid/errors/resultid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/resultid-problem-types.yml
- group: design
  href: https://artifacts.apis.io/resultid/conventions/resultid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/resultid-conventions.yml
- group: design
  href: https://artifacts.apis.io/resultid/data-model/resultid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/resultid-data-model.yml
- group: design
  href: https://artifacts.apis.io/resultid/conformance/resultid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/resultid-conformance.yml
- group: design
  href: https://artifacts.apis.io/resultid/lifecycle/resultid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/resultid-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/resultid/packages/resultid-packages.yml
  title: ''
  type: Packages
  url: packages/resultid-packages.yml
- group: agent
  href: https://artifacts.apis.io/resultid/llms/resultid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/resultid-llms.txt
- group: agent
  href: https://artifacts.apis.io/resultid/mcp/resultid-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/resultid-mcp.yml
- group: agent
  href: https://artifacts.apis.io/resultid/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/resultid/overlays/resultid-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/resultid-api-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/resultid/rate-limits/resultid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/resultid-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/resultid/plans/resultid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/resultid-plans-pricing.yml
created: '2026-07-17'
description: 'Resultid is an enterprise Operational Intelligence platform that connects what customers say, what teams do, and what operational data shows across every product, location, and service to surface hidden revenue opportunities. It ingests data from hundreds of sources - surveys, calls, CRM systems, reviews, and service records - and applies AI to identify the behavioral patterns that separate high-performing locations from underperformers, bridging the gap between well-measured technical operations and largely invisible human operations. The platform serves automotive, airlines, hospitality, financial services, and retail enterprises. Resultid is a Techstars-backed company. It does publish a developer surface, though it is not linked from the marketing site: an MkDocs "Resultid API Docs" site at docs.resultid.com renders a FastAPI-generated OpenAPI schema of nine read operations over campaigns, insights, trackers, themes and highlight data, authenticated with an X-API-Key request
  header. The raw JSON schema is not served and no API base URL is published anywhere, so the contract is readable but not yet callable from the documentation alone.'
image: https://www.resultid.ai/images/logo-white.svg
layout: provider
modified: '2026-10-06'
name: Resultid
nav: Providers
network: true
overview: 'Resultid publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Endpoints API and Insight endpoints API. Tagged areas include Company, Operational Intelligence, Analytics, Enterprise Software, and Artificial Intelligence.


  Resultid''s developer surface includes engineering blog, documentation, API reference, getting-started guide, authentication, and 20 more developer resources.'
plans:
- name: Resultid Plans Pricing
  plan_count: 0
  slug: resultid-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Resultid Rate Limits
  slug: resultid-rate-limits
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 37.0
    developer_ergonomics: 44.6
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/resultid/resultid-2026-09-02T153609.png
security:
- kind: authentication
  name: Resultid Authentication
  slug: resultid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Resultid Domain Security
  slug: resultid-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Read a Resultid campaign's insight grid
  slug: resultid-read-campaign-insight-grid
- name: Trace a Resultid tracker value to its source highlights
  slug: resultid-trace-tracker-value-to-highlights
slug: resultid
tags:
- Company
- Operational Intelligence
- Analytics
- Enterprise Software
- Artificial Intelligence
- Customer Experience
- Data Integration
- Revenue Intelligence
website: https://www.resultid.ai/
---
