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
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://fintua.com/security/
- group: agent
  href: https://artifacts.apis.io/fintua/well-known/fintua-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fintua-well-known.yml
- group: other
  href: https://artifacts.apis.io/fintua/hosts/fintua-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fintua-hosts.yml
- group: other
  href: https://artifacts.apis.io/fintua/vendors/fintua-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fintua-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fintua.com/terms-and-conditions/
- group: auth
  title: ''
  type: Security
  url: https://fintua.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fintua.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://fintua.com/comply/pricing/
- group: auth
  href: https://artifacts.apis.io/fintua/security/fintua-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fintua-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fintua/security/fintua-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fintua-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fintua.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fintua.com/platform/
- group: company
  title: ''
  type: Blog
  url: https://fintua.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://fintua.com/contact/
coverage:
  checked: '2026-10-27'
  detail: Access to OpenAPI spec URLs returned HTTP 403, indicating a partner login gate.
  evidence:
  - status: 403
    url: https://developer.fintua.com/openapi.json
  - status: 403
    url: https://developer.fintua.com/openapi.yaml
  reason: partner-login
  state: gated
created: '2026-10-26'
description: Fintua provides a comprehensive platform for indirect tax compliance, offering solutions for VAT registration, e‑invoicing, VAT recovery, and global payment integration. Their services include consultancy, data transformation, audit review, and a suite of tools to help businesses manage VAT obligations across multiple jurisdictions, supported by a resource library, webinars, and a community of tax experts.
image: https://fintua.com/wp-content/uploads/2025/06/Fintua-Open-Graph-Image.jpg
layout: provider
modified: '2026-10-26'
name: Fintua
nav: Providers
network: true
overview: 'Fintua is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tax, Compliance, VAT, and eInvoicing.


  Fintua''s developer surface includes pricing, documentation, engineering blog, support, and 10 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fintua Domain Security
  slug: fintua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fintua Trust Center
  slug: fintua-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: fintua
tags:
- Company
- Tax
- Compliance
- VAT
- eInvoicing
website: https://fintua.com/
---
