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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: The Connect API from AllFly — 4 operation(s) for connect.
  name: AllFly Connect API
  slug: allfly-connect-api
- description: The Events API from AllFly — 1 operation(s) for events.
  name: AllFly Events API
  slug: allfly-events-api
artifact_total: 12
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/rules/allfly-rules.yml
  title: ''
  type: Spectral
  url: rules/allfly-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/json-ld/allfly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allfly-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/vocabulary/allfly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allfly-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/data-model/allfly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allfly-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/authentication/allfly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allfly-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/conformance/allfly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allfly-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/well-known/allfly-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/allfly-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/well-known/allfly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allfly-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/hosts/allfly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allfly-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/vendors/allfly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allfly-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://allfly.io/post/priced-out-of-vegas-here-are-5-alternative-destinations-for-your-next-meeting
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allfly/refs/heads/main/security/allfly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allfly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allfly.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.allflyquest.com/en/
- group: company
  title: ''
  type: Blog
  url: https://allfly.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allfly.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.allflyquest.com/en/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://api.allflyquest.com/mcp
  - status: 403
    url: https://help.allflyquest.com/mcp
  - status: 200
    url: https://allfly.io/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: AllFly is a modern travel platform that simplifies group and corporate travel. It offers a marketplace for booking flights for teams, custom charter services, and a forecasting tool to estimate travel costs. The platform provides resources such as blogs, case studies, and e‑books, and supports integrations for corporate travel management.
json_schemas:
- name: GetApiConnectV1WebhooksResponse
  property_count: 1
  slug: allfly-get-api-connect-v1-webhooks-response
- name: GetApiConnectV1WebhooksWebhookidResponse
  property_count: 5
  slug: allfly-get-api-connect-v1-webhooks-webhookid-response
- name: GetApiConnectV1WebhooksWebhookidSecretResponse
  property_count: 1
  slug: allfly-get-api-connect-v1-webhooks-webhookid-secret-response
- name: PostApiConnectV1WebhooksRequest
  property_count: 5
  slug: allfly-post-api-connect-v1-webhooks-request
- name: PostApiConnectV1WebhooksWebhookidSecretRotateResponse
  property_count: 1
  slug: allfly-post-api-connect-v1-webhooks-webhookid-secret-rotate-response
- name: PutApiConnectV1WebhooksWebhookidRequest
  property_count: 5
  slug: allfly-put-api-connect-v1-webhooks-webhookid-request
jsonld:
- class_count: 7
  name: Allfly Context
  property_count: 8
  slug: allfly-context
layout: provider
modified: '2026-09-24'
name: AllFly
nav: Providers
network: true
overview: 'AllFly is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Connect API and Events API. Tagged areas include Travel, CorporateTravel, Marketplace, Booking, and Software-as-a-Service.


  The AllFly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AllFly''s developer surface includes authentication, pricing, documentation, engineering blog, support, and 12 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AllFly API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: allfly-rules
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 24.2
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 25.8
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 0.3
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Allfly Authentication
  slug: allfly-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Allfly Domain Security
  slug: allfly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allfly
tags:
- Travel
- CorporateTravel
- Marketplace
- Booking
- Software-as-a-Service
website: https://allfly.io/
---
