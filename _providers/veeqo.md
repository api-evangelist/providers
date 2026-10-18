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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: Programmatic access to product catalogs, order data, stock levels, and shipping labels.
  name: Veeqo API
  slug: veeqo-api-2
- baseURL: https://api.veeqo.com
  baseurl_source: declared
  description: The Current User API from Veeqo — 1 operation(s) for current user.
  name: Veeqo Current User API
  slug: veeqo-current-user-api
- baseURL: https://api.veeqo.com
  baseurl_source: declared
  description: The Oauth API from Veeqo — 1 operation(s) for oauth.
  name: Veeqo OAuth API
  slug: veeqo-oauth-api
- baseURL: https://api.veeqo.com
  baseurl_source: declared
  description: The Orders API from Veeqo — 1 operation(s) for orders.
  name: Veeqo Orders API
  slug: veeqo-orders-api
artifact_total: 11
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/plans/veeqo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/veeqo-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/rules/veeqo-rules.yml
  title: ''
  type: Spectral
  url: rules/veeqo-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/json-ld/veeqo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/veeqo-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/vocabulary/veeqo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/veeqo-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/data-model/veeqo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veeqo-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/conformance/veeqo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veeqo-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/llms/veeqo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veeqo-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/well-known/veeqo-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/veeqo-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/well-known/veeqo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/veeqo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/hosts/veeqo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/veeqo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/vendors/veeqo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/veeqo-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/packages/veeqo-packages.yml
  title: ''
  type: SDKs
  url: packages/veeqo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/packages/veeqo-packages.yml
  title: ''
  type: Packages
  url: packages/veeqo-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veeqo.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.veeqo.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.veeqo.com/
- group: auth
  title: ''
  type: Security
  url: https://www.veeqo.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veeqo.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.veeqo.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.veeqo.com/signin
- group: company
  title: ''
  type: Blog
  url: https://www.veeqo.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.veeqo.com/en/articles/14087861-getting-started-with-veeqo-uk
- group: docs
  title: ''
  type: Documentation
  url: https://developers.veeqo.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veeqo
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/veeqo/refs/heads/main/security/veeqo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veeqo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.veeqo.com
coverage:
  checked: '2026-10-13'
  detail: Developers site provides HTML docs but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://developers.veeqo.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Veeqo provides a cloud‑based platform that helps online retailers manage inventory, orders, shipping, and reporting across multiple sales channels. The solution integrates with major e‑commerce marketplaces, shopping carts, and shipping carriers, offering real‑time synchronization, automated fulfillment workflows, and analytics to streamline operations and improve customer experience. Veeqo’s API enables developers to programmatically access product catalogs, order data, stock levels, and shipping labels, supporting custom integrations and extensions for businesses seeking to scale their multi‑channel commerce operations.
image: https://www.veeqo.com/images/image-meta-og.png?w=1200&h=630
json_schemas:
- name: GetCurrentUserResponse
  property_count: 3
  slug: veeqo-get-current-user-response
- name: PostOauthTokenRequest
  property_count: 5
  slug: veeqo-post-oauth-token-request
- name: PostOauthTokenResponse
  property_count: 3
  slug: veeqo-post-oauth-token-response
jsonld:
- class_count: 3
  name: Veeqo Context
  property_count: 8
  slug: veeqo-context
layout: provider
modified: '2026-10-13'
name: Veeqo
nav: Providers
network: true
overview: 'Veeqo is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Current User API, OAuth API, Orders API, and 1 more. Tagged areas include Company, E-Commerce, Inventory, order-fulfillment, and multi-channel.


  The Veeqo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Veeqo''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 21 more developer resources.'
plans:
- name: Veeqo Plans Pricing
  plan_count: 3
  slug: veeqo-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Veeqo API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: veeqo-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 66.0
    catalog_earned_first_party: 12.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 21.7
    developer_ergonomics: 35.7
    discoverability: 69.6
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Veeqo Domain Security
  slug: veeqo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: veeqo
tags:
- Company
- E-Commerce
- Inventory
- order-fulfillment
- multi-channel
- Software-as-a-Service
website: https://www.veeqo.com
---
