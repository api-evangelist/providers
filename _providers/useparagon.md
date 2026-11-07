---
access_model:
  confidence: medium
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
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Useparagon Agentic Access
  operation_count: 13
  slug: useparagon-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://zeus.useparagon.com
  baseurl_source: declared
  description: Prebuilt, LLM-ready actions across connected SaaS providers.
  name: Paragon ActionKit API
  slug: useparagon-actionkit-api
- baseURL: https://zeus.useparagon.com
  baseurl_source: declared
  description: Authenticated users and connected third-party credentials.
  name: Paragon Connect API
  slug: useparagon-connect-api
- baseURL: https://zeus.useparagon.com
  baseurl_source: declared
  description: Integrations enabled for a Paragon project.
  name: Paragon Integrations API
  slug: useparagon-integrations-api
- baseURL: https://zeus.useparagon.com
  baseurl_source: declared
  description: Normalized third-party data ingestion pipelines and records.
  name: Paragon Managed Sync API
  slug: useparagon-managed-sync-api
- baseURL: https://zeus.useparagon.com
  baseurl_source: declared
  description: Access control checks for ingested data.
  name: Paragon Permissions API
  slug: useparagon-permissions-api
- baseURL: https://zeus.useparagon.com
  baseurl_source: declared
  description: Passthrough requests to a connected user's third-party API.
  name: Paragon Proxy API
  slug: useparagon-proxy-api
- baseURL: https://zeus.useparagon.com
  baseurl_source: declared
  description: Authenticated user and connected integration state.
  name: Paragon Users API
  slug: useparagon-users-api
- baseURL: https://zeus.useparagon.com
  baseurl_source: declared
  description: Triggering workflows and checking execution status.
  name: Paragon Workflows API
  slug: useparagon-workflows-api
artifact_total: 24
collections:
- collection_type: open
  name: Paragon ActionKit API
  slug: open-useparagon-actionkit-api
- collection_type: open
  name: Paragon ActionKit Connect API
  slug: open-useparagon-connect-api
- collection_type: open
  name: Paragon ActionKit Integrations API
  slug: open-useparagon-integrations-api
- collection_type: open
  name: Paragon ActionKit Managed Sync API
  slug: open-useparagon-managed-sync-api
- collection_type: open
  name: Paragon ActionKit Permissions API
  slug: open-useparagon-permissions-api
- collection_type: open
  name: Paragon ActionKit Proxy API
  slug: open-useparagon-proxy-api
- collection_type: open
  name: Paragon ActionKit Users API
  slug: open-useparagon-users-api
- collection_type: open
  name: Paragon ActionKit Workflows API
  slug: open-useparagon-workflows-api
- collection_type: open
  name: Paragon API
  slug: open-useparagon
common:
- group: agent
  href: https://artifacts.apis.io/useparagon/agentic-access/useparagon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/useparagon-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/useparagon/security/useparagon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/useparagon-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/useparagon/authentication/useparagon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/useparagon-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useparagon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useparagon
- group: company
  title: ''
  type: Website
  url: https://www.useparagon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useparagon.com/
- group: commercial
  href: https://artifacts.apis.io/useparagon/plans/useparagon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/useparagon-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/useparagon/rate-limits/useparagon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/useparagon-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/useparagon/finops/useparagon-finops.yml
  title: ''
  type: FinOps
  url: finops/useparagon-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.useparagon.com/blog
created: '2026-07-01'
description: Paragon is an embedded integration platform (embedded iPaaS) that lets B2B SaaS companies build and ship native, third-party integrations inside their own product. Developers use the Connect SDK/Portal plus a REST API (Connect API, ActionKit, and Managed Sync) to authenticate end users into 130+ SaaS providers, trigger workflows, run agentic actions, and ingest normalized third-party data.
finops:
- has_sources: true
  method: generated
  name: Useparagon Finops
  primary_unit: ''
  service_category: Integration Platform
  slug: useparagon-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/useparagon.png
layout: provider
modified: '2026-07-01'
name: Paragon
nav: Providers
network: true
overview: 'Paragon publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including ActionKit API, Connect API, Integrations API, and 5 more. Tagged areas include Integration, iPaaS, Embedded Integrations, Workflows, and ActionKit.


  The Paragon catalog on APIs.io includes 1 Spectral governance ruleset.


  Paragon''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Useparagon Plans Pricing
  plan_count: 4
  slug: useparagon-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Useparagon Rate Limits
  slug: useparagon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Paragon API Rules
  rule_count: 67
  severity_counts:
    error: 64
    hint: 0
    info: 2
    warn: 1
  slug: useparagon-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 50.4
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/useparagon/useparagon-2026-09-02T165235.png
security:
- kind: authentication
  name: Useparagon Authentication
  slug: useparagon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Useparagon Domain Security
  slug: useparagon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: useparagon
tags:
- Integration
- iPaaS
- Embedded Integrations
- Workflows
- ActionKit
- Managed Sync
- AI Agents
website: https://www.useparagon.com/
---
