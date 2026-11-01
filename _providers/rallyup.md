---
agent_readiness:
  band: human-only
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/rallyup/plans/rallyup-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rallyup-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://rallyup.com/security/
- group: agent
  href: https://artifacts.apis.io/rallyup/llms/rallyup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rallyup-llms.txt
- group: other
  href: https://artifacts.apis.io/rallyup/hosts/rallyup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rallyup-hosts.yml
- group: other
  href: https://artifacts.apis.io/rallyup/vendors/rallyup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rallyup-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rallyup.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://rallyup.com/contact-support/
- group: auth
  title: ''
  type: Security
  url: https://rallyup.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rallyup.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://rallyup.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://go.rallyup.com/account/profile/signin
- group: company
  title: ''
  type: Blog
  url: https://rallyup.com/blog/
- group: auth
  href: https://artifacts.apis.io/rallyup/security/rallyup-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/rallyup-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/rallyup/security/rallyup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rallyup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rallyup.com/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's API hosts.
  evidence:
  - status: 404
    url: https://api.rallyup.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Rally Up provides a powerful digital fundraising platform that enables organizations to create, manage, and promote online fundraising campaigns. The solution offers tools for event ticketing, donation processing, peer-to-peer fundraising, and real-time analytics, helping nonprofits and causes elevate their campaigns and achieve their financial goals through innovative, cloud‑based technology.
layout: provider
modified: '2026-10-27'
name: Rally Up
nav: Providers
network: true
overview: 'Rally Up is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fundraising, Nonprofit, SaaS, and DigitalPlatform.


  Rally Up''s developer surface includes support, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Rallyup Plans Pricing
  plan_count: 2
  slug: rallyup-plans-pricing
random_paper: 9
scopes:
- name: Rallyup Scopes
  scope_count: 0
  slug: rallyup-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rallyup Authentication
  slug: rallyup-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rallyup Domain Security
  slug: rallyup-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Rallyup Trust Center
  slug: rallyup-trust-center
  summary_line: SOC 2, GDPR
slug: rallyup
tags:
- Company
- Fundraising
- Nonprofit
- SaaS
- DigitalPlatform
website: https://rallyup.com/
---
