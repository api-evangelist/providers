---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://your-organization.tachyus.com/api/v1
  baseurl_source: declared
  description: Daily/monthly production records for a well.
  name: Tachyus Production Data API
  slug: tachyus-production-data-api
- baseURL: https://your-organization.tachyus.com/api/v1
  baseurl_source: declared
  description: Projects map to a specific geographic or operational asset.
  name: Tachyus Projects API
  slug: tachyus-projects-api
- baseURL: https://your-organization.tachyus.com/api/v1
  baseurl_source: declared
  description: Wells belong to projects.
  name: Tachyus Wells API
  slug: tachyus-wells-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tachapps Production Data API
  slug: open-tachyus-production-data-api
- collection_type: open
  name: Tachapps Production Data Projects API
  slug: open-tachyus-projects-api
- collection_type: open
  name: Tachapps Production Data Wells API
  slug: open-tachyus-wells-api
common:
- group: company
  title: ''
  type: Website
  url: https://tachyus.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tachyus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tachyus.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tachyus.com/api/introduction.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tachyus.com/guide/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tachyus
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tachyus.com/_files/ugd/3ab73f_d653d64a6d4640b3a35762afb01ac3ef.pdf
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tachyus-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tachyus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tachyus-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tachyus-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tachyus-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tachyus-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tachyus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tachyus-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tachyus-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tachyus-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tachyus-tachapps-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/tachyus-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tachyus-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tachyus-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tachyus provides AI-powered operational optimization and greenhouse-gas emissions management software for the energy and industrial sectors, combining data, reservoir physics, and machine learning. Its Tachapps platform spans Strateon (production and injection allocation), Aqueon (conventional reservoir management and optimization), and Aurion (GHG emissions accounting, monitoring, forecasting, and regulatory reporting). The Tachapps REST API (v1) is organized around Projects, Wells, and Production Data, using Bearer API-token authentication with scopes, JSON over HTTPS, cursor-based pagination, and per-plan rate limits.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tachyus.png
layout: provider
modified: '2026-07-21'
name: Tachyus
nav: Providers
network: true
overview: 'Tachyus publishes 3 APIs on the [APIs.io](https://apis.io/) network: Production Data API, Projects API, and Wells API. Tagged areas include Company, Energy, Oil and Gas, Reservoir Management, and Production Optimization.


  Tachyus'' developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 17 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 3
  name: Tachyus Rate Limits
  slug: tachyus-rate-limits
scopes:
- name: Tachyus Scopes
  scope_count: 6
  slug: tachyus-scopes
  summary_line: 6 scopes
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 16.7
    developer_ergonomics: 32.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 32.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 51.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tachyus/refs/heads/main/screenshots/tachyus-2026-08-17T082238.png
security:
- kind: authentication
  name: Tachyus Authentication
  slug: tachyus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tachyus Domain Security
  slug: tachyus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tachyus
tags:
- Company
- Energy
- Oil and Gas
- Reservoir Management
- Production Optimization
- Emissions Management
- Machine-Learning
- Analytics
website: https://tachyus.com
---
