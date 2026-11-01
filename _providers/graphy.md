---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Graphy Agentic Access
  operation_count: 7
  slug: graphy-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 1
apis:
- baseURL: https://agents.graphy.dev
  baseurl_source: declared
  description: The Agents API from Graphy — 7 operation(s) for agents.
  name: Graphy Agents API
  slug: graphy-agents-api
artifact_total: 10
collections:
- collection_type: open
  name: Graphy AI Agents API
  slug: open-graphy-agents-api
common:
- group: commercial
  href: https://artifacts.apis.io/graphy/plans/graphy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/graphy-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/graphy/overlays/graphy-agents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/graphy-agents-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/graphy/agentic-access/graphy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/graphy-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://graphy.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://graphy.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.graphy.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.graphy.dev/agents/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.graphy.dev/agents/quickstart
- group: company
  title: ''
  type: Blog
  url: https://graphy.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://graphy.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://graphy.app/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://graphy.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://graphy.app/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.graphy.app/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.graphy.dev/agents/versioning
- group: start
  title: ''
  type: Sandbox
  url: https://playground.graphy.dev/
- group: operate
  href: https://artifacts.apis.io/graphy/changelog/graphy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/graphy-changelog.yml
- group: design
  href: https://artifacts.apis.io/graphy/lifecycle/graphy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/graphy-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/graphy/authentication/graphy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/graphy-authentication.yml
- group: auth
  href: https://artifacts.apis.io/graphy/security/graphy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/graphy-domain-security.yml
- group: build
  href: https://artifacts.apis.io/graphy/packages/graphy-packages.yml
  title: ''
  type: Packages
  url: packages/graphy-packages.yml
- group: build
  href: https://artifacts.apis.io/graphy/packages/graphy-packages.yml
  title: ''
  type: SDKs
  url: packages/graphy-packages.yml
- group: design
  href: https://artifacts.apis.io/graphy/components/graphy-components.yml
  title: ''
  type: Components
  url: components/graphy-components.yml
- group: agent
  href: https://artifacts.apis.io/graphy/mcp/graphy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/graphy-mcp.yml
- group: agent
  href: https://artifacts.apis.io/graphy/llms/graphy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/graphy-llms.txt
- group: design
  href: https://artifacts.apis.io/graphy/errors/graphy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/graphy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/graphy/conventions/graphy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/graphy-conventions.yml
- group: design
  href: https://artifacts.apis.io/graphy/conformance/graphy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/graphy-conformance.yml
- group: design
  href: https://artifacts.apis.io/graphy/data-model/graphy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/graphy-data-model.yml
- group: agent
  href: https://artifacts.apis.io/graphy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Graphy is an AI-powered data visualization platform that turns raw data into presentation-ready charts and interactive data stories. Alongside its no-code chart maker (Google Sheets, CSV and Excel import, AI insights, conversational data chat and 20+ chart types), Graphy ships a developer platform at graphy.dev: an AI Agents API that generates, mutates, annotates, narrates, extracts and deterministically evaluates charts from natural language — streamed as Server-Sent Events — plus a React charting SDK and editor for embedding editable, story-driven data experiences inside your own product. Backed by Seedcamp, Coatue, General Catalyst and Northzone.'
finops:
- has_sources: true
  method: derived
  name: Graphy Finops
  primary_unit: user/month
  service_category: ''
  slug: graphy-finops
  template: false
image: https://framerusercontent.com/assets/HQAKsmFxtBCYp0V86Kb4PbbCjx4.png
layout: provider
modified: '2026-07-19'
name: Graphy
nav: Providers
network: true
overview: 'Graphy publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agents API. Tagged areas include Company, Data Visualization, Charts, Charting, and Analytics.


  Graphy''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, sandbox, and 23 more developer resources.'
plans:
- name: Graphy Plans Pricing
  plan_count: 3
  slug: graphy-plans-pricing
- name: Graphy Price Estimates
  plan_count: 0
  slug: graphy-price-estimates
random_paper: 3
score:
  band: strong
  composite: 57.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 53.3
    developer_ergonomics: 68.5
    discoverability: 66.1
    operational_transparency: 39.5
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/graphy/graphy-2026-07-25T220250.png
security:
- kind: authentication
  name: Graphy Authentication
  slug: graphy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Graphy Domain Security
  slug: graphy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Extract data and build a chart with Graphy
  slug: graphy-extract-and-visualize
- name: Refine and annotate a chart with Graphy
  slug: graphy-refine-chart
slug: graphy
tags:
- Company
- Data Visualization
- Charts
- Charting
- Analytics
- Artificial Intelligence
- Data Storytelling
- Developer Tools
- SDK
- Agents
website: https://graphy.app
---
