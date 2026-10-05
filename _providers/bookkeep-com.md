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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-10-04'
api_count: 2
apis:
- description: API reference for Bookkeep version 1, covering endpoints for accounting automation.
  name: Bookkeep API v1
  slug: bookkeep-api-v1
- baseURL: https://api.bookkeep.com
  baseurl_source: declared
  description: The Entities API from Bookkeep.com — 4 operation(s) for entities.
  name: Bookkeep.com Entities API
  slug: bookkeep-com-entities-api
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/plans/bookkeep-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bookkeep-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/rules/bookkeep-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bookkeep-com-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/json-ld/bookkeep-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bookkeep-com-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/vocabulary/bookkeep-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bookkeep-com-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/data-model/bookkeep-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bookkeep-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/changelog/bookkeep-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bookkeep-com-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/conformance/bookkeep-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bookkeep-com-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/llms/bookkeep-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bookkeep-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/well-known/bookkeep-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bookkeep-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/hosts/bookkeep-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bookkeep-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/vendors/bookkeep-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bookkeep-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bookkeep.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bookkeep.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bookkeep.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: http://www.bookkeep.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://app.bookkeep.com/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://bookkeep.com/docs/account-setup/connecting-an-accounting-platform/categories-versus-subcategories
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bookkeep-com/refs/heads/main/security/bookkeep-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bookkeep-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bookkeep.com/
coverage:
  checked: '2026-10-02'
  detail: Documentation pages are rendered via Docusaurus JavaScript and no OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://www.bookkeep.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Bookkeep.com provides accounting automation solutions for Shopify and other ecommerce platforms, offering features such as automated reconciliation, sales tax compliance, multi‑bank settlement, inventory management, and integration with various POS and marketplace systems. It targets merchants, retailers, franchises, and accounting firms, delivering a unified financial workflow across online and offline sales channels.
image: https://cdn.prod.website-files.com/687660d37bb7d201bcff3f9c/687fb3e0a874a01f16200a5a_Frame%201171275227.png
json_schemas:
- name: GetV1EntitiesResponse
  property_count: 1
  slug: bookkeep-com-get-v1-entities-response
jsonld:
- class_count: 1
  name: Bookkeep Com Context
  property_count: 1
  slug: bookkeep-com-context
layout: provider
modified: '2026-10-02'
name: Bookkeep.com
nav: Providers
network: true
overview: 'Bookkeep.com publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Entities API, and 1 more. Tagged areas include Company, Accounting, Automation, Shopify, and E-Commerce.


  The Bookkeep.com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bookkeep.com''s developer surface includes changelog, pricing, documentation, signup flow, getting-started guide, and 14 more developer resources.'
plans:
- name: Bookkeep Com Plans Pricing
  plan_count: 6
  slug: bookkeep-com-plans-pricing
random_paper: 2
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Bookkeep.com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: bookkeep-com-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 21.4
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Bookkeep Com Domain Security
  slug: bookkeep-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bookkeep-com
tags:
- Company
- Accounting
- Automation
- Shopify
- E-Commerce
- Integration
website: https://www.bookkeep.com/
---
