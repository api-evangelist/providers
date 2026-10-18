---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: Developer portal for PAR Technology APIs and integrations.
  name: PAR Developer Portal
  slug: par-developer-portal
- baseURL: https://SERVER_NAME_GOES_HERE.punchh.com
  baseurl_source: declared
  description: The Auth API from PAR Technology — 5 operation(s) for auth.
  name: PAR Technology Auth API
  slug: par-technology-auth-api
- baseURL: https://SERVER_NAME_GOES_HERE.punchh.com
  baseurl_source: declared
  description: The Discounts API from PAR Technology — 3 operation(s) for discounts.
  name: PAR Technology Discounts API
  slug: par-technology-discounts-api
- baseURL: https://SERVER_NAME_GOES_HERE.punchh.com
  baseurl_source: declared
  description: The Pos API from PAR Technology — 7 operation(s) for pos.
  name: PAR Technology Pos API
  slug: par-technology-pos-api
- baseURL: https://SERVER_NAME_GOES_HERE.punchh.com
  baseurl_source: declared
  description: The Redemptions API from PAR Technology — 2 operation(s) for redemptions.
  name: PAR Technology Redemptions API
  slug: par-technology-redemptions-api
artifact_total: 23
asyncapis:
- description: ''
  name: Par Technology Webhooks
  slug: par-technology-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/rules/par-technology-rules.yml
  title: ''
  type: Spectral
  url: rules/par-technology-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/json-ld/par-technology-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/par-technology-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/vocabulary/par-technology-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/par-technology-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/asyncapi/par-technology-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/par-technology-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/data-model/par-technology-data-model.yml
  title: ''
  type: DataModel
  url: data-model/par-technology-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.partech.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/authentication/par-technology-authentication.yml
  title: ''
  type: Authentication
  url: authentication/par-technology-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/conformance/par-technology-conformance.yml
  title: ''
  type: Conformance
  url: conformance/par-technology-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/llms/par-technology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/par-technology-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/well-known/par-technology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/par-technology-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/hosts/par-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/par-technology-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/vendors/par-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/par-technology-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://partech.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://partech.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://partech.com/newsroom/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.partech.com/docs/dev-portal-developer-resources/getting-started/kiosk
- group: docs
  title: ''
  type: Documentation
  url: https://developers.partech.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/security/par-technology-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/par-technology-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/par-technology/refs/heads/main/security/par-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/par-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://partech.com
- group: company
  title: ''
  type: Blog
  url: https://partech.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.partech.com
- group: operate
  title: ''
  type: Support
  url: https://support.partech.com
- group: company
  title: ''
  type: Blog
  url: https://partech.com/blog
coverage:
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://developers.partech.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: PAR Technology provides a comprehensive hospitality management platform offering solutions for restaurants, convenience stores, fuel retail, and loyalty programs. Their services include cloud POS, back‑office operations, guest engagement, digital experiences, payment services, and data‑driven insights, helping businesses streamline operations and enhance customer experiences across multiple channels.
image: https://partech.com/wp-content/uploads/2026/04/par-intelligence-demo.webp
json_schemas:
- name: DeleteApiPosRedemptionsMultipleDestroyRequest
  property_count: 2
  slug: par-technology-delete-api-pos-redemptions-multiple-destroy-request
- name: GetApiAuthRedemptionsApplicableOffersResponse
  property_count: 4
  slug: par-technology-get-api-auth-redemptions-applicable-offers-response
- name: GetApiPosUsersFindResponse
  property_count: 12
  slug: par-technology-get-api-pos-users-find-response
- name: PostApiApiidRedemptionsApplicableOffersRequest
  property_count: 8
  slug: par-technology-post-api-apiid-redemptions-applicable-offers-request
- name: PostApiAuthAuthidRequest
  property_count: 9
  slug: par-technology-post-api-auth-authid-request
- name: PostApiAuthAuthidResponse
  property_count: 3
  slug: par-technology-post-api-auth-authid-response
- name: PostApiAuthRedemptionsRedemptionidRequest
  property_count: 22
  slug: par-technology-post-api-auth-redemptions-redemptionid-request
- name: PostApiAuthRedemptionsRedemptionidResponse
  property_count: 9
  slug: par-technology-post-api-auth-redemptions-redemptionid-response
- name: PostApiPosPoidRequest
  property_count: 9
  slug: par-technology-post-api-pos-poid-request
- name: PostApiPosPoidResponse
  property_count: 9
  slug: par-technology-post-api-pos-poid-response
- name: PostApiPosRedemptionsRedemptionidRequest
  property_count: 7
  slug: par-technology-post-api-pos-redemptions-redemptionid-request
- name: PostApiPosRedemptionsRedemptionidResponse
  property_count: 3
  slug: par-technology-post-api-pos-redemptions-redemptionid-response
jsonld:
- class_count: 22
  name: Par Technology Context
  property_count: 57
  slug: par-technology-context
layout: provider
modified: '2026-10-13'
name: PAR Technology
nav: Providers
network: true
overview: 'PAR Technology is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Discounts API, Pos API, and 2 more. Tagged areas include Company, Hospitality, Point-of-Sale, Loyalty, and Retail.


  The PAR Technology catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  PAR Technology''s developer surface includes authentication, getting-started guide, documentation, engineering blog, support, and 19 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: PAR Technology API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: par-technology-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 19.7
    contract_quality: 32.7
    developer_ergonomics: 40.5
    discoverability: 71.4
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Par Technology Authentication
  slug: par-technology-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Par Technology Domain Security
  slug: par-technology-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Par Technology Trust Center
  slug: par-technology-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: par-technology
tags:
- Company
- Hospitality
- Point-of-Sale
- Loyalty
- Retail
website: https://partech.com
---
