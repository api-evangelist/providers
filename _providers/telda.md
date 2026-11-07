---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.lever.co
  baseurl_source: declared
  description: 'Telda API as documented publicly: 177 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Telda API
  slug: telda-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/telda/rules/telda-rules.yml
  title: ''
  type: Spectral
  url: rules/telda-rules.yml
- group: design
  href: https://artifacts.apis.io/telda/json-ld/telda-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/telda-context.jsonld
- group: design
  href: https://artifacts.apis.io/telda/vocabulary/telda-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/telda-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/telda/data-model/telda-data-model.yml
  title: ''
  type: DataModel
  url: data-model/telda-data-model.yml
- group: auth
  href: https://artifacts.apis.io/telda/authentication/telda-authentication.yml
  title: ''
  type: Authentication
  url: authentication/telda-authentication.yml
- group: design
  href: https://artifacts.apis.io/telda/conformance/telda-conformance.yml
  title: ''
  type: Conformance
  url: conformance/telda-conformance.yml
- group: agent
  href: https://artifacts.apis.io/telda/well-known/telda-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/telda-well-known.yml
- group: other
  href: https://artifacts.apis.io/telda/hosts/telda-hosts.yml
  title: ''
  type: Hosts
  url: hosts/telda-hosts.yml
- group: other
  href: https://artifacts.apis.io/telda/vendors/telda-vendors.yml
  title: ''
  type: Vendors
  url: vendors/telda-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lever.co/
- group: auth
  href: https://artifacts.apis.io/telda/security/telda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/telda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://telda.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://telda.app/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://telda.app/legal/privacy
- group: company
  title: ''
  type: Press
  url: https://telda.app/press.html
coverage:
  checked: '2026-10-29'
  detail: Documentation is hosted on Lever subdomains that render content via JavaScript, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://hire.lever.co/developer/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Telda is a fintech company offering a mobile-first payment card and app that enables users to send, receive, and spend money instantly. The platform integrates Apple Pay, supports biometric security, and provides real-time transaction notifications. Telda aims to simplify personal finance by allowing social payments with emojis and GIFs, categorizing spending, and offering zero-fee transfers. Backed by Sequoia Capital, Telda targets consumers seeking a seamless, low-cost digital banking experience.
image: https://telda.app/telda-card.png
json_schemas:
- name: GetOpportunitiesOpportunityPanelsPanelResponse
  property_count: 14
  slug: telda-get-opportunities-opportunity-panels-panel-response
- name: PostRequest
  property_count: 12
  slug: telda-post-request
- name: PostResponse
  property_count: 18
  slug: telda-post-response
- name: PostV1RequisitionsResponse
  property_count: 20
  slug: telda-post-v1-requisitions-response
- name: PostV1Uploads083D56Ef40C6483A955120Ece8C4E776ResumePdfReques
  property_count: 5
  slug: telda-post-v1-uploads083-d56-ef40-c6483-a955120-ece8-c4-e776-resume-pdf-reques
- name: PutV1RequisitionsD918C5E654Cf4247A0548A02D575B993Response
  property_count: 22
  slug: telda-put-v1-requisitions-d918-c5-e654-cf4247-a0548-a02-d575-b993-response
jsonld:
- class_count: 120
  name: Telda Context
  property_count: 116
  slug: telda-context
layout: provider
modified: '2026-10-29'
name: Telda
nav: Providers
network: true
overview: 'Telda is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Mobile App, and Digital Banking.


  The Telda catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Telda''s developer surface includes authentication, documentation, and 13 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Telda API Rules
  rule_count: 41
  severity_counts:
    error: 35
    hint: 0
    info: 3
    warn: 3
  slug: telda-rules
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.8
    developer_ergonomics: 16.7
    discoverability: 67.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/telda/telda-2026-11-03T144409.png
security:
- kind: authentication
  name: Telda Authentication
  slug: telda-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Telda Domain Security
  slug: telda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telda
tags:
- Company
- Fintech
- Payments
- Mobile App
- Digital Banking
website: https://telda.app
---
