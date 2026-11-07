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
  try_now: false
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
  name: Liferay Agentic Access
  operation_count: 8
  slug: liferay-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 1
apis:
- baseURL: http://localhost:8080/o/headless-admin-user/v1.0
  baseurl_source: declared
  description: Manage roles and role associations
  name: Liferay Roles API
  slug: liferay-roles-api
artifact_total: 11
collections:
- collection_type: open
  name: Liferay Roles API
  slug: open-liferay-roles-api
- collection_type: open
  name: Liferay Roles API
  slug: open-liferay
common:
- group: commercial
  href: https://artifacts.apis.io/liferay/plans/liferay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/liferay-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/liferay/rate-limits/liferay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/liferay-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/liferay/finops/liferay-finops.yml
  title: ''
  type: FinOps
  url: finops/liferay-finops.yml
- group: other
  href: https://artifacts.apis.io/liferay/capabilities/liferay-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/liferay-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://liferay.com
- group: agent
  href: https://artifacts.apis.io/liferay/agentic-access/liferay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/liferay-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/liferay/security/liferay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/liferay-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/liferay/security/liferay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/liferay-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/liferay/authentication/liferay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/liferay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liferay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liferay-inc-
- group: company
  title: ''
  type: Blog
  url: https://www.liferay.com/blog
created: '2025-01-08'
description: Liferay DXP is an open-source digital experience platform offering headless REST APIs for managing users, roles, permissions, content, and site configuration. The Roles API lets you list, retrieve, and associate or dissociate regular, site, and organization roles for users.
finops:
- has_sources: false
  method: generated
  name: Liferay Finops
  primary_unit: request
  service_category: API
  slug: liferay-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liferay.png
layout: provider
modified: '2026-09-16'
name: Liferay
nav: Providers
network: true
overview: 'Liferay publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Roles API. Tagged areas include Open Source, Digital Experience, DXP, Roles, and User.


  The Liferay catalog on APIs.io includes 1 Spectral governance ruleset.


  Liferay''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Liferay Plans Pricing
  plan_count: 3
  slug: liferay-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Liferay Rate Limits
  slug: liferay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Liferay API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: liferay-rules
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 39.2
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 25.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/liferay/liferay-2026-06-20T184517.png
security:
- kind: authentication
  name: Liferay Authentication
  slug: liferay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Liferay Domain Security
  slug: liferay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Liferay Vulnerability Disclosure
  slug: liferay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: liferay
tags:
- Open Source
- Digital Experience
- DXP
- Roles
- User
- Permissions
- Headless
website: https://liferay.com
---
