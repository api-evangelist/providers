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
- description: Self employed accounting software
  name: Coconut API
  slug: coconut-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/getcoconut-com/llms/getcoconut-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getcoconut-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/getcoconut-com/well-known/getcoconut-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getcoconut-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/getcoconut-com/well-known/getcoconut-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getcoconut-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/getcoconut-com/hosts/getcoconut-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getcoconut-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getcoconut-com/vendors/getcoconut-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getcoconut-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.getcoconut.com/
- group: auth
  href: https://artifacts.apis.io/getcoconut-com/security/getcoconut-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getcoconut-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getcoconut.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getcoconut.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getcoconut.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.getcoconut.com/legal/security
- group: start
  title: ''
  type: SignUp
  url: https://web.getcoconut.com/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getcoconut.com/
- group: operate
  title: ''
  type: Support
  url: https://help.getcoconut.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getcoconut.com/legal/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getcoconut
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec endpoints on https://api.getcoconut.com return HTTP 403, indicating authentication is required.
  evidence:
  - status: 403
    url: https://api.getcoconut.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Coconut provides a modern accounting and financial management platform for small and medium businesses, offering automated bookkeeping, invoicing, expense tracking, and real-time financial insights. The company integrates with banks, payment processors, and popular SaaS tools to streamline operations and reduce manual effort. Backed by Techstars and part of the VC portfolio, Coconut aims to simplify finance for entrepreneurs through a robust API-first approach.
image: https://cdn.prod.website-files.com/6069af2a39978132d0155fd7/68494e83812cad2671383511_OG%20Image.png
layout: provider
modified: '2026-10-29'
name: Coconut
nav: Providers
network: true
overview: 'Coconut is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Accounting, SaaS, and API.


  Coconut''s developer surface includes documentation, pricing, signup flow, support, and 12 more developer resources.'
plans:
- name: Getcoconut Com Plans Pricing
  plan_count: 0
  slug: getcoconut-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Getcoconut Com Rate Limits
  slug: getcoconut-com-rate-limits
scopes:
- name: Getcoconut Com Scopes
  scope_count: 0
  slug: getcoconut-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Getcoconut Com Authentication
  slug: getcoconut-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Getcoconut Com Domain Security
  slug: getcoconut-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getcoconut-com
tags:
- Company
- FinTech
- Accounting
- SaaS
- API
website: https://www.getcoconut.com/
---
