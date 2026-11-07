---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The Libryo Platform''s partner-facing RESTful API. Third-party applications integrate on behalf of a Libryo user using the OAuth 2.0 authorization-code flow, then call the versioned /api/v1 surface to '
  name: Libryo API
  slug: libryo-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/libryo/lifecycle/libryo-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/libryo-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/libryo/hosts/libryo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/libryo-hosts.yml
- group: other
  href: https://artifacts.apis.io/libryo/vendors/libryo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/libryo-vendors.yml
- group: build
  href: https://artifacts.apis.io/libryo/packages/libryo-packages.yml
  title: ''
  type: SDKs
  url: packages/libryo-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://libryo.com/terms/
- group: company
  title: ''
  type: Blog
  url: https://blog.libryo.com/what-is-a-legal-register
- group: company
  title: ''
  type: Website
  url: https://libryo.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/libryo/libryo-api-oauth-docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/libryo
- group: operate
  title: ''
  type: Support
  url: https://libryo.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://libryo.com/faqs/
- group: commercial
  title: ''
  type: Pricing
  url: https://libryo.com/pricing-regulatory-tracking/
- group: start
  title: ''
  type: Login
  url: https://my.libryo.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://libryo.com/privacy-policy/
- group: other
  title: ''
  type: CaseStudies
  url: https://libryo.com/case-studies/
- group: other
  title: ''
  type: Resources
  url: https://libryo.com/resources-legaltech/
- group: company
  title: ''
  type: About
  url: https://libryo.com/about-us/
- group: build
  href: https://artifacts.apis.io/libryo/packages/libryo-packages.yml
  title: ''
  type: Packages
  url: packages/libryo-packages.yml
- group: agent
  href: https://artifacts.apis.io/libryo/well-known/libryo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/libryo-well-known.yml
- group: auth
  href: https://artifacts.apis.io/libryo/security/libryo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/libryo-domain-security.yml
- group: design
  href: https://artifacts.apis.io/libryo/conventions/libryo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/libryo-conventions.yml
- group: design
  href: https://artifacts.apis.io/libryo/conformance/libryo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/libryo-conformance.yml
- group: design
  href: https://artifacts.apis.io/libryo/lifecycle/libryo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/libryo-lifecycle.yml
coverage:
  checked: '2026-10-20'
  detail: Libryo's only public API documentation is a 2017 OAuth authorization-code README on GitHub (my.libryo.com/oauth/authorize, api.libryo.com/api/v1/oauth/token); no OpenAPI, endpoint reference, llms.txt or MCP surface is published on any Libryo host.
  evidence:
  - status: 200
    url: https://raw.githubusercontent.com/libryo/libryo-api-oauth-docs/master/README.md
  - status: 200
    url: https://libryo.com/pricing-regulatory-tracking/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Libryo (ERM Libryo) is a regulatory compliance management platform for Environmental, Health and Safety (EHS) teams. It automates legal registers, streams site-specific regulatory obligations across jurisdictions, and tracks legislative change so that operators know which laws apply to each of their sites. Founded in 2016 with a distributed team across Cape Town, London, Toronto, Nairobi and Berlin, Libryo is now part of ERM, the sustainability consultancy. The product surface spans Libryo Sites (site-specific EHS regulatory intelligence), Libryo Assess (assessment and audit management), Libryo Collaborate, and custom legal registers, and is used in manufacturing, energy and utilities, chemicals, mining, logistics and telecoms. Libryo exposes a partner-facing RESTful API secured with OAuth 2.0 authorization-code flow, documented publicly in the libryo/libryo-api-oauth-docs repository, and also offers its regulatory content as a data-as-a-service feed into third-party GRC platforms.
image: https://libryo.com/wp-content/uploads/2025/03/cropped-favicon-32x32.png
layout: provider
modified: '2026-07-19'
name: Libryo
nav: Providers
network: true
overview: 'Libryo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Regulatory Compliance, Legal Tech, Environmental Health and Safety, and Governance Risk and Compliance.


  Libryo''s developer surface includes engineering blog, documentation, support, pricing, and 19 more developer resources.'
plans:
- name: Libryo Plans Pricing
  plan_count: 0
  slug: libryo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Libryo Rate Limits
  slug: libryo-rate-limits
scopes:
- name: Libryo Scopes
  scope_count: 3
  slug: libryo-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 28.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/libryo/libryo-2026-07-25T225027.png
security:
- kind: authentication
  name: Libryo Authentication
  slug: libryo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Libryo Domain Security
  slug: libryo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: libryo
tags:
- Company
- Regulatory Compliance
- Legal Tech
- Environmental Health and Safety
- Governance Risk and Compliance
- Legal Registers
- Regulatory Change Management
- Sustainability
- Authentication
website: https://libryo.com
---
