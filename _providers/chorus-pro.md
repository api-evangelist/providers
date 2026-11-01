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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Chorus Pro API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Chorus Pro API
  slug: chorus-pro-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/chorus-pro/vendors/chorus-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chorus-pro-vendors.yml
- group: design
  href: https://artifacts.apis.io/chorus-pro/rules/chorus-pro-rules.yml
  title: ''
  type: Spectral
  url: rules/chorus-pro-rules.yml
- group: design
  href: https://artifacts.apis.io/chorus-pro/vocabulary/chorus-pro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chorus-pro-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chorus-pro/conformance/chorus-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chorus-pro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chorus-pro/llms/chorus-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chorus-pro-llms.txt
- group: agent
  href: https://artifacts.apis.io/chorus-pro/well-known/chorus-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chorus-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/chorus-pro/hosts/chorus-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chorus-pro-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.data.gouv.fr/pages/legal/legal-notice
- group: operate
  title: ''
  type: Support
  url: https://www.data.gouv.fr/support
- group: start
  title: ''
  type: SignUp
  url: https://www.data.gouv.fr/register?next=/dataservices
- group: docs
  title: ''
  type: APIReference
  url: https://www.data.gouv.fr/pages/spd/reference
- group: docs
  title: ''
  type: Documentation
  url: https://doc.transport.data.gouv.fr/
- group: auth
  href: https://artifacts.apis.io/chorus-pro/security/chorus-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chorus-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chorus-pro.gouv.fr/
coverage:
  checked: '2026-10-27'
  detail: No public developer program or API documentation was found for Chorus Pro.
  evidence:
  - status: 302
    url: https://portail.chorus-pro.gouv.fr/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Chorus Pro is the French public platform for electronic invoicing and payment processing between public administrations and their suppliers. It provides a portal where businesses can submit, track, and manage invoices, access payment status, and retrieve related documentation, supporting the French e‑invoicing ecosystem.
layout: provider
modified: '2026-10-27'
name: Chorus Pro
nav: Providers
network: true
overview: 'Chorus Pro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, PublicSector, France, and E-invoicing.


  The Chorus Pro catalog on APIs.io includes 1 Spectral governance ruleset.


  Chorus Pro''s developer surface includes support, signup flow, API reference, documentation, and 10 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Chorus Pro API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: chorus-pro-rules
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chorus Pro Domain Security
  slug: chorus-pro-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: chorus-pro
tags:
- Company
- Payments
- PublicSector
- France
- E-invoicing
website: https://chorus-pro.gouv.fr/
---
