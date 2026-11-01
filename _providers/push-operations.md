---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Push Operations provides a cloud‑based platform for payroll, HR, scheduling, and workforce management via its API.
  name: Push Operations API
  slug: push-operations-api-2
- description: 'Push Operations API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Push Operations API
  slug: push-operations-api
artifact_total: 9
common:
- group: operate
  href: https://artifacts.apis.io/push-operations/rate-limits/push-operations-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/push-operations-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/push-operations/rules/push-operations-rules.yml
  title: ''
  type: Spectral
  url: rules/push-operations-rules.yml
- group: design
  href: https://artifacts.apis.io/push-operations/vocabulary/push-operations-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/push-operations-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/push-operations/conventions/push-operations-conventions.yml
  title: ''
  type: Conventions
  url: conventions/push-operations-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://app.drata.com/trust/9cc3aa81-0c38-11ee-865f-029d78a187d9
- group: auth
  href: https://artifacts.apis.io/push-operations/authentication/push-operations-authentication.yml
  title: ''
  type: Authentication
  url: authentication/push-operations-authentication.yml
- group: design
  href: https://artifacts.apis.io/push-operations/conformance/push-operations-conformance.yml
  title: ''
  type: Conformance
  url: conformance/push-operations-conformance.yml
- group: auth
  href: https://artifacts.apis.io/push-operations/well-known/push-operations-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/push-operations-status-security.txt
- group: agent
  href: https://artifacts.apis.io/push-operations/well-known/push-operations-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/push-operations-well-known.yml
- group: other
  href: https://artifacts.apis.io/push-operations/hosts/push-operations-hosts.yml
  title: ''
  type: Hosts
  url: hosts/push-operations-hosts.yml
- group: other
  href: https://artifacts.apis.io/push-operations/vendors/push-operations-vendors.yml
  title: ''
  type: Vendors
  url: vendors/push-operations-vendors.yml
- group: auth
  href: https://artifacts.apis.io/push-operations/security/push-operations-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/push-operations-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/push-operations/security/push-operations-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/push-operations-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pushoperations.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.pushoperations.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pushoperations.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pushoperations.com/book-a-demo
- group: start
  title: ''
  type: SignUp
  url: https://app-elb.pushoperations.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pushoperations.com/pushpricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pushoperations.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.pushoperations.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pushoperations.com/terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://www.pushoperations.com/blog
- group: build
  title: ''
  type: Postman
  url: https://documenter.gw.postman.com/api/collections/6099159/U16jLk57?segregateAuth=true&versionTag=latest
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pushoperations
coverage:
  checked: '2026-10-28'
  detail: API documentation requires a partner login to access the API reference.
  evidence:
  - status: 404
    url: https://developers.pushoperations.com/api
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Push Operations provides a cloud‑based platform for payroll, human resources, scheduling, time tracking, and workforce management tailored primarily to the hospitality industry. The SaaS solution automates payroll processing, employee onboarding, shift scheduling, compliance reporting, and offers real‑time business intelligence dashboards. It serves restaurants, quick‑service chains, coffee shops, pizzerias, pubs and breweries, enabling them to streamline operations, reduce manual effort, and improve profitability.
image: https://cdn.prod.website-files.com/5fb89486431df956d62ce163/67f99f88a9d06caf8bea67f2_pushoperations-all-in-one-people-management.avif
layout: provider
modified: '2026-10-28'
name: Push Operations
nav: Providers
network: true
overview: 'Push Operations is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payroll, HR, Workforce Management, SaaS, and Hospitality.


  The Push Operations catalog on APIs.io includes 1 Spectral governance ruleset.


  Push Operations'' developer surface includes authentication, documentation, getting-started guide, signup flow, pricing, support, engineering blog, and 18 more developer resources.'
plans:
- name: Push Operations Plans Pricing
  plan_count: 0
  slug: push-operations-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Push Operations Rate Limits
  slug: push-operations-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Push Operations API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: push-operations-rules
scopes:
- name: Push Operations Scopes
  scope_count: 0
  slug: push-operations-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 54.8
    discoverability: 57.1
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Push Operations Authentication
  slug: push-operations-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Push Operations Domain Security
  slug: push-operations-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Push Operations Trust Center
  slug: push-operations-trust-center
  summary_line: SOC 2, ISO 27001
slug: push-operations
tags:
- Payroll
- HR
- Workforce Management
- SaaS
- Hospitality
- Company
website: https://pushoperations.com/
---
