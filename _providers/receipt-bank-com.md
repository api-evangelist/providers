---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.precision.dext.com
  baseurl_source: declared
  description: 'Dext API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Dext API
  slug: receipt-bank-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/receipt-bank-com/rules/receipt-bank-com-rules.yml
  title: ''
  type: Spectral
  url: rules/receipt-bank-com-rules.yml
- group: design
  href: https://artifacts.apis.io/receipt-bank-com/json-ld/receipt-bank-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/receipt-bank-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/receipt-bank-com/vocabulary/receipt-bank-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/receipt-bank-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/receipt-bank-com/data-model/receipt-bank-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/receipt-bank-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/receipt-bank-com/conformance/receipt-bank-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/receipt-bank-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/receipt-bank-com/llms/receipt-bank-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/receipt-bank-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/receipt-bank-com/well-known/receipt-bank-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/receipt-bank-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/receipt-bank-com/well-known/receipt-bank-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/receipt-bank-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/receipt-bank-com/hosts/receipt-bank-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/receipt-bank-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/receipt-bank-com/vendors/receipt-bank-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/receipt-bank-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.dext.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dext.com/en/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://help.dext.com/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dext.com/en/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://dext.com/partner/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://dext.com/en/news
- group: start
  title: ''
  type: Login
  url: https://app.dext.com/login/
- group: company
  title: ''
  type: Blog
  url: https://dext.com/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.dext.com/en/articles/416705-getting-started-with-dext-for-businesses
- group: docs
  title: ''
  type: Documentation
  url: https://help.dext.com/
- group: auth
  href: https://artifacts.apis.io/receipt-bank-com/security/receipt-bank-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/receipt-bank-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.receipt-bank.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.receipt-bank.com/mcp
  - status: 403
    url: https://assets.dext.com/mcp
  - status: 200
    url: https://www.receipt-bank.com/
  reason: partner-login
  state: gated
created: '2026-10-25'
description: Dext, formerly Receipt Bank, provides bookkeeping automation software for businesses and accountants. Their platform captures receipts, manages expenses, integrates with accounting systems, and offers AI‑assisted bookkeeping features. Serving sectors like construction, professional services, hospitality, and retail, Dext helps automate data entry, improve client data health, and streamline financial workflows across multi‑entity businesses.
image: https://dext.com/og-logo.png
json_schemas:
- name: GetClientsClientidActivityStatsResponse
  property_count: 3
  slug: receipt-bank-com-get-clients-clientid-activity-stats-response
- name: GetClientsClientidResponse
  property_count: 13
  slug: receipt-bank-com-get-clients-clientid-response
- name: GetClientsResponse
  property_count: 6
  slug: receipt-bank-com-get-clients-response
jsonld:
- class_count: 3
  name: Receipt Bank Com Context
  property_count: 16
  slug: receipt-bank-com-context
layout: provider
modified: '2026-10-25'
name: Dext
nav: Providers
network: true
overview: 'Dext is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bookkeeping, Automation, Accounting, and AI.


  The Dext catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dext''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Dext API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: receipt-bank-com-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 23.3
    developer_ergonomics: 28.6
    discoverability: 67.9
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Receipt Bank Com Domain Security
  slug: receipt-bank-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: receipt-bank-com
tags:
- Company
- Bookkeeping
- Automation
- Accounting
- AI
website: https://www.receipt-bank.com/
---
