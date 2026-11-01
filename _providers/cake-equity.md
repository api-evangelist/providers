---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cakeequity.com/changelog/pulley-migration-built-into-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cakeequity.com/
- group: commercial
  href: https://artifacts.apis.io/cake-equity/plans/cake-equity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cake-equity-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cake-equity/changelog/cake-equity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cake-equity-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cakeequity.com/
- group: design
  href: https://artifacts.apis.io/cake-equity/conformance/cake-equity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cake-equity-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cake-equity/llms/cake-equity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cake-equity-llms.txt
- group: agent
  href: https://artifacts.apis.io/cake-equity/well-known/cake-equity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cake-equity-well-known.yml
- group: other
  href: https://artifacts.apis.io/cake-equity/hosts/cake-equity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cake-equity-hosts.yml
- group: other
  href: https://artifacts.apis.io/cake-equity/vendors/cake-equity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cake-equity-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cakeequity.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cakeequity.com/changelog
- group: auth
  href: https://artifacts.apis.io/cake-equity/security/cake-equity-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cake-equity-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cake-equity/security/cake-equity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cake-equity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cakeequity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.cakeequity.com/
- group: operate
  title: ''
  type: Support
  url: https://help.cakeequity.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cakeequity.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cakeequity.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.cakeequity.com/setup_company
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cakeequity.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cakeequity.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cake-equity/workspace
coverage:
  checked: '2026-10-06'
  detail: The provider's documentation sites and API host return no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contracts.
  evidence:
  - status: 0
    url: https://api.cakeequity.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Cake Equity provides a cap table and equity management platform for growing startups. It offers tools for accurate cap tables, compliance readiness, equity grant tracking, scenario modeling for raises, and an employee app that turns equity ownership into a performance driver. The platform supports migrations from other solutions and serves companies at all stages of growth, aiming to simplify complex equity workflows and improve decision‑making for finance and legal teams.
finops:
- has_sources: true
  method: derived
  name: Cake Equity Finops
  primary_unit: subscription
  service_category: ''
  slug: cake-equity-finops
  template: false
image: https://cdn.prod.website-files.com/63ca0685daa2425d2057a7a8/6a6832ced9f01e4d4b1bd43e_OG_Image.webp
layout: provider
modified: '2026-10-06'
name: Cake Equity
nav: Providers
network: true
overview: 'Cake Equity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Equity, Cap Table, Startups, and Software-as-a-Service.


  Cake Equity''s developer surface includes getting-started guide, documentation, changelog, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Cake Equity Plans Pricing
  plan_count: 5
  slug: cake-equity-plans-pricing
random_paper: 18
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 48.2
    operational_transparency: 26.3
  previous_composite: 39.6
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cake Equity Domain Security
  slug: cake-equity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cake Equity Trust Center
  slug: cake-equity-trust-center
  summary_line: ISO 27001
slug: cake-equity
tags:
- Company
- Equity
- Cap Table
- Startups
- Software-as-a-Service
- Finance
website: https://www.cakeequity.com/
---
