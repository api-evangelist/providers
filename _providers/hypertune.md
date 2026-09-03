---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Hypertune Agentic Access
  operation_count: 2
  slug: hypertune-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Programmatic and Git-based management of flags, experiments, and configuration. Hypertune versions all flags, experiments, analytics events, and app configuration together in a single Git-based histor
  name: Hypertune Management API
  slug: hypertune-management-api
- baseURL: https://edge.hypertune.com/graphql
  baseurl_source: declared
  description: The GraphQL API from Hypertune — 1 operation(s) for graphql.
  name: Hypertune GraphQL API
  slug: hypertune-graphql-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hypertune Edge GraphQL API
  slug: open-hypertune-graphql-api
- collection_type: open
  name: Hypertune Edge API
  slug: open-hypertune
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hypertune-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hypertune-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hypertune-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hypertunehq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hypertune
- group: company
  title: ''
  type: Website
  url: https://www.hypertune.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hypertune.com
- group: commercial
  title: ''
  type: Plans
  url: plans/hypertune-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hypertune-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hypertune-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hypertune.com/blog
created: '2026-06-20'
description: Hypertune is a type-safe, Git-based platform for feature flags, A/B testing, experimentation, analytics, and app configuration. Flag logic is authored in Hyperlang and modeled as a GraphQL schema; SDKs use a CLI to generate fully typed clients, fetch flag logic once from Hypertune Edge (Cloudflare CDN) at initialization, then evaluate flags locally and synchronously in memory. A GraphQL Edge API offers a no-SDK path, and analytics events are flushed back to Hypertune Edge in the background.
finops:
- name: Hypertune Finops
  service_category: Developer Tools
  slug: hypertune-finops
graphqls:
- description: Conceptual, representative GraphQL schema for the [Hypertune](https://www.hypertune.com/)
  name: Hypertune GraphQL Schema
  slug: hypertune-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hypertune.png
layout: provider
modified: '2026-06-20'
name: Hypertune
nav: Providers
network: true
overview: 'Hypertune publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Feature Flags, Experimentation, A/B Testing, Analytics, and App Configuration.


  Hypertune''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Hypertune Plans Pricing
  plan_count: 4
  slug: hypertune-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Hypertune Rate Limits
  slug: hypertune-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hypertune/refs/heads/main/screenshots/hypertune-2026-06-20T183051.png
security:
- kind: authentication
  name: Hypertune Authentication
  slug: hypertune-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hypertune Domain Security
  slug: hypertune-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hypertune
tags:
- Feature Flags
- Experimentation
- A/B Testing
- Analytics
- App Configuration
- GraphQL
- Edge
website: https://www.hypertune.com
---
