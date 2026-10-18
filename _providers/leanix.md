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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Leanix Agentic Access
  operation_count: 22
  slug: leanix-agentic-access
  summary_line: 22 operations · 11 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The configurations API from LeanIX — 1 operation(s) for configurations.
  name: LeanIX Configurations API
  slug: leanix-configurations-api
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The examples API from LeanIX — 2 operation(s) for examples.
  name: LeanIX Examples API
  slug: leanix-examples-api
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The fastSynchronizationRuns API from LeanIX — 2 operation(s) for fastsynchronizationruns.
  name: LeanIX Fast Synchronization Runs API
  slug: leanix-fastsynchronizationruns-api
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The storages API from LeanIX — 1 operation(s) for storages.
  name: LeanIX Storages API
  slug: leanix-storages-api
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The synchronizationRuns API from LeanIX — 13 operation(s) for synchronizationruns.
  name: LeanIX Synchronization Runs API
  slug: leanix-synchronizationruns-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Integration configurations API
  slug: open-leanix-configurations-api
- collection_type: open
  name: Integration configurations examples API
  slug: open-leanix-examples-api
- collection_type: open
  name: Integration configurations fastSynchronizationRuns API
  slug: open-leanix-fastsynchronizationruns-api
- collection_type: open
  name: Integration configurations storages API
  slug: open-leanix-storages-api
- collection_type: open
  name: Integration configurations synchronizationRuns API
  slug: open-leanix-synchronizationruns-api
- collection_type: open
  name: Integration API
  slug: open-leanix
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/plans/leanix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leanix-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/rate-limits/leanix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leanix-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/finops/leanix-finops.yml
  title: ''
  type: FinOps
  url: finops/leanix-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/agentic-access/leanix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/leanix-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/security/leanix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/leanix-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/security/leanix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leanix-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/authentication/leanix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leanix-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/scopes/leanix-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/leanix-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leanix
- group: company
  title: ''
  type: Website
  url: https://www.leanix.net
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/leanix/ea
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leanix
- group: company
  title: ''
  type: Blog
  url: https://www.leanix.net/en/blog
created: '2026-03-27'
description: LeanIX (now SAP LeanIX) is an enterprise architecture and SaaS management platform providing IT portfolio management, application portfolio rationalization, SaaS discovery, and technology risk management. The platform exposes REST APIs for integrating with the fact sheet inventory, running inbound and outbound synchronizations, and managing workspace data.
finops:
- has_sources: false
  method: generated
  name: Leanix Finops
  primary_unit: ''
  service_category: API
  slug: leanix-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leanix.png
layout: provider
modified: '2026-05-19'
name: LeanIX
nav: Providers
network: true
overview: 'LeanIX publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Configurations API, Examples API, Fast Synchronization Runs API, and 2 more. Tagged areas include Enterprise Architecture, SaaS Management, IT Portfolio Management, Application Portfolio, and Technology Risk.


  LeanIX''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Leanix Plans Pricing
  plan_count: 3
  slug: leanix-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Leanix Rate Limits
  slug: leanix-rate-limits
scopes:
- name: Leanix Scopes
  scope_count: 0
  slug: leanix-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 40.0
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/screenshots/leanix-2026-06-20T184359.png
security:
- kind: authentication
  name: Leanix Authentication
  slug: leanix-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Leanix Domain Security
  slug: leanix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Leanix Vulnerability Disclosure
  slug: leanix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: leanix
tags:
- Enterprise Architecture
- SaaS Management
- IT Portfolio Management
- Application Portfolio
- Technology Risk
website: https://www.leanix.net
---
