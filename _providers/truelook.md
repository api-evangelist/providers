---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: TrueLook offers a cloud platform for construction site security; however no public machine‑readable API specification is available.
  name: TrueLook API
  slug: truelook-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.truelook.com/
- group: agent
  href: https://artifacts.apis.io/truelook/llms/truelook-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/truelook-llms.txt
- group: other
  href: https://artifacts.apis.io/truelook/hosts/truelook-hosts.yml
  title: ''
  type: Hosts
  url: hosts/truelook-hosts.yml
- group: other
  href: https://artifacts.apis.io/truelook/vendors/truelook-vendors.yml
  title: ''
  type: Vendors
  url: vendors/truelook-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.truelook.com/release-notes
- group: docs
  title: ''
  type: Documentation
  url: https://help.truelook.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truelook
- group: auth
  href: https://artifacts.apis.io/truelook/security/truelook-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/truelook-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/truelook/security/truelook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/truelook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://truelook.com/
- group: company
  title: ''
  type: Blog
  url: https://www.truelook.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.truelook.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.truelook.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truelook.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truelook.com/terms-conditions
coverage:
  checked: '2026-10-28'
  detail: All attempted OpenAPI spec URLs on truelook.com and its subdomains returned 301 redirects, 404, or 403, and no OpenAPI document was found.
  evidence:
  - status: 301
    url: https://truelook.com/openapi.json
  - status: 404
    url: https://support.truelook.com/openapi.json
  - status: 403
    url: https://trust.truelook.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: TrueLook provides construction site security and intelligence through high-definition cameras, AI-driven analytics, and a cloud platform that delivers live video, time-lapse documentation, PPE detection, and automated alerts. The solution integrates with construction management tools such as Procore, offering remote monitoring, incident reporting, and data-driven insights for owners, contractors, and insurers.
image: https://www.truelook.com/favicon.ico
layout: provider
modified: '2026-10-28'
name: TrueLook
nav: Providers
network: true
overview: 'TrueLook is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Security, AI, Video, and Monitoring.


  TrueLook''s developer surface includes changelog, documentation, engineering blog, support, pricing, and 10 more developer resources.'
plans:
- name: Truelook Plans Pricing
  plan_count: 0
  slug: truelook-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Truelook Rate Limits
  slug: truelook-rate-limits
scopes:
- name: Truelook Scopes
  scope_count: 0
  slug: truelook-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Truelook Authentication
  slug: truelook-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Truelook Domain Security
  slug: truelook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Truelook Trust Center
  slug: truelook-trust-center
  summary_line: SOC 2, ISO 27001
slug: truelook
tags:
- Construction
- Security
- AI
- Video
- Monitoring
- SaaS
website: https://truelook.com/
---
