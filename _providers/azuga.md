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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://services.azuga.com
  baseurl_source: declared
  description: The Azuga Ws Oauth API from Azuga — 4 operation(s) for azuga ws oauth.
  name: Azuga Azuga Ws Oauth API
  slug: azuga-azuga-ws-oauth-api
artifact_total: 9
asyncapis:
- description: ''
  name: Azuga Webhooks
  slug: azuga-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/plans/azuga-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/azuga-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/rules/azuga-rules.yml
  title: ''
  type: Spectral
  url: rules/azuga-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/json-ld/azuga-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/azuga-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/vocabulary/azuga-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/azuga-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/asyncapi/azuga-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/azuga-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/data-model/azuga-data-model.yml
  title: ''
  type: DataModel
  url: data-model/azuga-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.azuga.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/authentication/azuga-authentication.yml
  title: ''
  type: Authentication
  url: authentication/azuga-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/conformance/azuga-conformance.yml
  title: ''
  type: Conformance
  url: conformance/azuga-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/llms/azuga-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azuga-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/hosts/azuga-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azuga-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/vendors/azuga-vendors.yml
  title: ''
  type: Vendors
  url: vendors/azuga-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.azuga.com/help-center
- group: auth
  title: ''
  type: Security
  url: https://www.azuga.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.azuga.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.azuga.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.azuga.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.azuga.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.azuga.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://developer.azuga.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.azuga.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.azuga.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.azugaeld.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/security/azuga-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/azuga-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azuga/refs/heads/main/security/azuga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azuga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.azuga.com
coverage:
  checked: '2026-10-14'
  detail: The developer portal provides reference documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract is publicly accessible.
  evidence:
  - status: 200
    url: https://developer.azuga.com/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Azuga provides comprehensive fleet management software and GPS tracking solutions, delivering an end‑to‑end platform that includes AI‑powered dashcams, insurance tools, telematics, driver safety analytics, and customizable reporting. The service helps businesses of all sizes maximize vehicle ROI, reduce operational costs, ensure regulatory compliance, and improve driver behavior through real‑time insights and automated alerts.
image: https://cdn.prod.website-files.com/5bc4b66f898dce69ebbe7ca9/68112a7cb6955eddec782950_Opengraph%20Thumbnail%20New%20UI.webp
json_schemas:
- name: PostAzugaWsOauthV3AssetsCreateResponse
  property_count: 2
  slug: azuga-post-azuga-ws-oauth-v3-assets-create-response
jsonld:
- class_count: 1
  name: Azuga Context
  property_count: 2
  slug: azuga-context
layout: provider
modified: '2026-10-13'
name: Azuga
nav: Providers
network: true
overview: 'Azuga is listed with 1 API on the [APIs.io](https://apis.io/) network: Azuga Ws Oauth API. Tagged areas include Company, Fleet Management, GPS Tracking, Telematics, and Software-as-a-Service.


  The Azuga catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Azuga''s developer surface includes authentication, support, pricing, changelog, engineering blog, API reference, getting-started guide, and 19 more developer resources.'
plans:
- name: Azuga Plans Pricing
  plan_count: 4
  slug: azuga-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Azuga API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: azuga-rules
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 65.2
    catalog_earned_first_party: 12.0
    catalog_gap: 49.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 26.9
    developer_ergonomics: 57.1
    discoverability: 75.0
    operational_transparency: 34.2
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
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Azuga Authentication
  slug: azuga-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Azuga Domain Security
  slug: azuga-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Azuga Trust Center
  slug: azuga-trust-center
  summary_line: SOC 2, ISO 27001
slug: azuga
tags:
- Company
- Fleet Management
- GPS Tracking
- Telematics
- Software-as-a-Service
website: https://www.azuga.com
---
