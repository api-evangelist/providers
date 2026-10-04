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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-03'
api_count: 4
apis:
- description: BindHQ Insurance API provides programmatic access to insurance platform features.
  name: Insurance API
  slug: insurance-api
- description: The Policies API from Bind — 2 operation(s) for policies.
  name: Bind Policies API
  slug: bind-policies-api
- description: The Quotes API from Bind — 1 operation(s) for quotes.
  name: Bind Quotes API
  slug: bind-quotes-api
- description: The Reports API from Bind — 1 operation(s) for reports.
  name: Bind Reports API
  slug: bind-reports-api
artifact_total: 10
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/plans/bind-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bind-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/rules/bind-rules.yml
  title: ''
  type: Spectral
  url: rules/bind-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/json-ld/bind-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bind-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/vocabulary/bind-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bind-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/data-model/bind-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bind-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/conformance/bind-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bind-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/llms/bind-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bind-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/hosts/bind-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bind-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/vendors/bind-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bind-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bind/refs/heads/main/security/bind-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bindhq.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bindhq.com/portal
- group: docs
  title: ''
  type: APIReference
  url: https://www.bindhq.com/insurance-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bindhq.com/insurance-api
- group: operate
  title: ''
  type: Support
  url: https://support.bindhq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bindhq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bindhq.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bindhq.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bindhq.com/legal/privacy-policy
coverage:
  checked: '2026-09-28'
  detail: Insurance API documentation is a JavaScript‑rendered Framer site with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://www.bindhq.com/insurance-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: BindHQ provides a composable insurance infrastructure platform for specialty insurers, MGAs, and brokers. Their APIs enable policy administration, underwriting, rating, and data access through a headless architecture, supporting digital distribution, delegated authority operations, and integration with carrier reporting systems. The platform offers flexible, scalable solutions for managing insurance products and automating workflows via modern API-driven services.
image: https://framerusercontent.com/images/8UlogeRvnNxYazVcp56Y4cn7Zx4.png
json_schemas:
- name: PostApiV2QuotesRequest
  property_count: 4
  slug: bind-post-api-v2-quotes-request
- name: PostApiV2QuotesResponse
  property_count: 3
  slug: bind-post-api-v2-quotes-response
jsonld:
- class_count: 2
  name: Bind Context
  property_count: 7
  slug: bind-context
layout: provider
modified: '2026-09-28'
name: Bind
nav: Providers
network: true
overview: 'Bind publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Policies API, Quotes API, Reports API, and 1 more. Tagged areas include Insurance, Platform, Composable, and Specialty.


  The Bind catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bind''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Bind Plans Pricing
  plan_count: 3
  slug: bind-plans-pricing
random_paper: 17
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bind API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: bind-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 35.7
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Bind Domain Security
  slug: bind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bind
tags:
- Insurance
- Platform
- Composable
- Specialty
website: https://www.bindhq.com
---
