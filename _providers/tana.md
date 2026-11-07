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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tana Agentic Access
  operation_count: 1
  slug: tana-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://europe-west1-tagr-prod.cloudfunctions.net
  baseurl_source: declared
  description: The AddToNodeV2 API from Tana — 1 operation(s) for addtonodev2.
  name: Tana AddToNodeV2 API
  slug: tana-addtonodev2-api
artifact_total: 14
collections:
- collection_type: open
  name: Tana Documentation AddToNodeV2 API
  slug: open-tana-addtonodev2-api
- collection_type: open
  name: Tana Documentation AddToNodeV2 Docs API
  slug: open-tana-docs-api
common:
- group: commercial
  href: https://artifacts.apis.io/tana/plans/tana-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tana-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tana.inc/api/docs
- group: docs
  title: ''
  type: Documentation
  url: https://tana.inc/learn
- group: docs
  title: ''
  type: APIReference
  url: https://outliner.tana.inc/learn/features/input-api
- group: start
  title: ''
  type: GettingStarted
  url: https://outliner.tana.inc/help/getting-started
- group: company
  title: ''
  type: Blog
  url: https://tana.inc/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://tana.inc/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tana.inc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tana.inc/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tanainc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tana.inc
- group: auth
  href: https://artifacts.apis.io/tana/authentication/tana-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tana-authentication.yml
- group: docs
  href: https://artifacts.apis.io/tana/openapi/_original/tana-input-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/tana-input-api-openapi.yml
- group: docs
  href: https://artifacts.apis.io/tana/openapi/tana-docs-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/tana-docs-api-openapi.yml
- group: other
  href: https://artifacts.apis.io/tana/overlays/tana-input-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tana-input-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/tana/overlays/tana-docs-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tana-docs-api-overlay.yaml
- group: build
  href: https://artifacts.apis.io/tana/packages/tana-packages.yml
  title: ''
  type: Packages
  url: packages/tana-packages.yml
- group: build
  href: https://artifacts.apis.io/tana/packages/tana-packages.yml
  title: ''
  type: SDKs
  url: packages/tana-packages.yml
- group: operate
  href: https://artifacts.apis.io/tana/rate-limits/tana-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tana-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/tana/conventions/tana-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tana-conventions.yml
- group: design
  href: https://artifacts.apis.io/tana/errors/tana-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tana-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tana/lifecycle/tana-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tana-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tana/data-model/tana-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tana-data-model.yml
- group: design
  href: https://artifacts.apis.io/tana/conformance/tana-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tana-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tana/mcp/tana-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tana-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tana/llms/tana-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tana-llms.txt
- group: agent
  href: https://artifacts.apis.io/tana/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/tana/agentic-access/tana-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tana-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/tana/security/tana-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tana-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tana/security/tana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tana.inc
created: '2026-07-17'
description: 'Tana Inc. builds two products that share the Tana brand: Tana, an agentic meeting platform where AI agents do real work during native video calls and land decisions, tasks, and drafts in a persistent context graph; and Tana Outliner, a knowledge-management tool built on an infinite outliner with supertags and nodes. Tana exposes two public HTTP APIs — the Tana Input API for programmatically adding nodes, fields, and supertags to an Outliner workspace graph (workspace-scoped bearer-token auth), and a public agent-native Documentation API for searching and reading Tana docs as clean markdown. Backed by Lightspeed Venture Partners and Northzone.'
finops:
- has_sources: true
  method: derived
  name: Tana Finops
  primary_unit: user
  service_category: ''
  slug: tana-finops
  template: false
image: https://tana.inc/opengraph-image/default
layout: provider
modified: '2026-07-21'
name: Tana
nav: Providers
network: true
overview: 'Tana publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: AddToNodeV2 API. Tagged areas include Company, Note Taking, Knowledge Management, Productivity, and Artificial Intelligence.


  The Tana catalog on APIs.io includes 1 Spectral governance ruleset.


  Tana''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, authentication, and 25 more developer resources.'
plans:
- name: Tana Plans Pricing
  plan_count: 3
  slug: tana-plans-pricing
- name: Tana Price Estimates
  plan_count: 0
  slug: tana-price-estimates
random_paper: 12
rate_limits:
- limit_count: 0
  name: Tana Rate Limits
  slug: tana-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Tana API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: tana-rules
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 53.9
    developer_ergonomics: 61.3
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
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
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tana/tana-2026-08-17T082245.png
security:
- kind: authentication
  name: Tana Authentication
  slug: tana-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tana Domain Security
  slug: tana-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Tana Trust Center
  slug: tana-trust-center
  summary_line: trust center published
skill_count: 2
skills:
- name: Add content to a Tana graph
  slug: tana-add-to-graph
- name: Search and read Tana documentation
  slug: tana-search-docs
slug: tana
tags:
- Company
- Note Taking
- Knowledge Management
- Productivity
- Artificial Intelligence
- Meetings
- Agents
- Collaboration
- Outliner
website: https://tana.inc
---
