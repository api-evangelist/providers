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
    error_semantics: documented
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
  score: 10.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides BookingAutomation integration allowing automated syncing of booking data via ChargeAutomation's API.
  name: BookingAutomation API
  slug: bookingautomation-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/chargeautomation/rate-limits/chargeautomation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chargeautomation-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chargeautomation/plans/chargeautomation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chargeautomation-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/chargeautomation/authentication/chargeautomation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chargeautomation-authentication.yml
- group: design
  href: https://artifacts.apis.io/chargeautomation/errors/chargeautomation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chargeautomation-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chargeautomation/conformance/chargeautomation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chargeautomation-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chargeautomation/llms/chargeautomation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chargeautomation-llms.txt
- group: auth
  href: https://artifacts.apis.io/chargeautomation/well-known/chargeautomation-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chargeautomation-help-security.txt
- group: agent
  href: https://artifacts.apis.io/chargeautomation/well-known/chargeautomation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chargeautomation-well-known.yml
- group: other
  href: https://artifacts.apis.io/chargeautomation/hosts/chargeautomation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chargeautomation-hosts.yml
- group: other
  href: https://artifacts.apis.io/chargeautomation/vendors/chargeautomation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chargeautomation-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chargeautomation.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://help.chargeautomation.com/en/?_gl=1*1q587zh*_gcl_au*MTM0ODI1Njk4NC4xNzQ0Mjg5MTE4
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chargeautomation.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://chargeautomation.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.chargeautomation.com/login
- group: company
  title: ''
  type: Blog
  url: https://chargeautomation.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: http://help.chargeautomation.com/en/articles/10331994-sales-onboarding-support-links
- group: docs
  title: ''
  type: Documentation
  url: https://help.chargeautomation.com/
- group: auth
  href: https://artifacts.apis.io/chargeautomation/security/chargeautomation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chargeautomation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chargeautomation.com/
coverage:
  checked: '2026-10-28'
  detail: Documentation provides integration guides but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://help.chargeautomation.com/en/articles/14156479-bookingautomation-api-chargeautomation-integration.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: ChargeAutomation provides guest experience software for hotels, vacation rentals, and property managers, enabling online check‑in, secure payments, deposits, upsells, and guest access management from a single platform. The solution automates the entire stay lifecycle, streamlining operations for hospitality businesses while enhancing guest satisfaction through seamless digital interactions. With integrations to major property management systems, ChargeAutomation helps operators reduce manual work, improve revenue, and deliver a modern, contact‑less experience.
image: https://chargeautomation.com/wp-content/uploads/2026/10/og-homepage-1200x630-1.png
layout: provider
modified: '2026-10-28'
name: ChargeAutomation
nav: Providers
network: true
overview: 'ChargeAutomation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Guest Experience, Payments, and Property Management.


  ChargeAutomation''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Chargeautomation Plans Pricing
  plan_count: 4
  slug: chargeautomation-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Chargeautomation Rate Limits
  slug: chargeautomation-rate-limits
scopes:
- name: Chargeautomation Scopes
  scope_count: 0
  slug: chargeautomation-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 42.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chargeautomation Authentication
  slug: chargeautomation-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chargeautomation Domain Security
  slug: chargeautomation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chargeautomation
tags:
- Company
- Hospitality
- Guest Experience
- Payments
- Property Management
website: https://chargeautomation.com/
---
