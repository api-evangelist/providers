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
  score: 9.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/loc-tax/llms/loc-tax-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loc-tax-llms.txt
- group: agent
  href: https://artifacts.apis.io/loc-tax/well-known/loc-tax-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loc-tax-well-known.yml
- group: other
  href: https://artifacts.apis.io/loc-tax/hosts/loc-tax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loc-tax-hosts.yml
- group: other
  href: https://artifacts.apis.io/loc-tax/vendors/loc-tax-vendors.yml
  title: ''
  type: Vendors
  url: vendors/loc-tax-vendors.yml
- group: auth
  href: https://artifacts.apis.io/loc-tax/security/loc-tax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loc-tax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.loctax.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.loctax.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.loctax.com/privacy-statement-general
- group: docs
  title: ''
  type: Documentation
  url: https://www.loctax.com/resources
created: '2026-10-25'
description: Loctax provides a global tax intelligence platform powered by AI, delivering actionable tax insights across 220+ jurisdictions. It integrates IBFD’s authoritative tax content, offering real-time answers on permanent establishments, withholding tax, corporate tax, transfer pricing, and more. Users can ask tax questions specific to their corporate structures, receive cited positions, and leverage compliance tools, all within a secure, SOC 2, GDPR, and ISO 27001‑compliant environment.
image: https://cdn.sanity.io/images/rdg0q6if/production/adf6461dc682cd7885b71a88b3b1e2c7f592778a-2400x1260.png?w=1200&h=630
layout: provider
modified: '2026-10-25'
name: Loctax
nav: Providers
network: true
overview: 'Loctax is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tax, AI, Platform, Global, and Compliance.


  Loctax''s developer surface includes documentation and 8 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Loc Tax Domain Security
  slug: loc-tax-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: loc-tax
tags:
- Tax
- AI
- Platform
- Global
- Compliance
website: https://www.loctax.com/
---
