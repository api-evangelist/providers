---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.webflow.com
  baseurl_source: declared
  description: 'Jitty API as documented publicly: 26 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Jitty API
  slug: jitty-api
artifact_total: 13
common:
- group: auth
  href: https://artifacts.apis.io/jitty/well-known/jitty-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jitty-developers-security.txt
- group: design
  href: https://artifacts.apis.io/jitty/rules/jitty-rules.yml
  title: ''
  type: Spectral
  url: rules/jitty-rules.yml
- group: design
  href: https://artifacts.apis.io/jitty/json-ld/jitty-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jitty-context.jsonld
- group: design
  href: https://artifacts.apis.io/jitty/vocabulary/jitty-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jitty-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jitty/data-model/jitty-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jitty-data-model.yml
- group: design
  href: https://artifacts.apis.io/jitty/conformance/jitty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jitty-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jitty/well-known/jitty-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jitty-well-known.yml
- group: other
  href: https://artifacts.apis.io/jitty/hosts/jitty-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jitty-hosts.yml
- group: other
  href: https://artifacts.apis.io/jitty/vendors/jitty-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jitty-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.webflow.com/data/v2.0.0/reference/rest-introduction/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://developers.webflow.com/
- group: auth
  href: https://artifacts.apis.io/jitty/security/jitty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jitty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jitty.com/
- group: company
  title: ''
  type: Blog
  url: https://jitty.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uploads-ssl.webflow.com/64a29738a276228b93aec588/669e6bb8f183f79aa8fb3e63_Jitty%20-%20T%26Cs%20-%20July%202024%20(1).docx.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jitty.com/docs/PRIVACY-POLICY-0526.pdf
coverage:
  checked: '2026-10-29'
  detail: No public API documentation or machine‑readable contract was found on Jitty's website or associated hosts.
  evidence:
  - status: 404
    url: https://jitty.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Jitty is a home‑search platform that uses AI‑powered filters to help buyers find the exact home they want. Founded by three veterans frustrated with the stressful, slow, and guess‑driven home‑buying process, Jitty offers a clearer, smarter way to browse listings, compare commute times, and access detailed property information. The service provides tools for sharing favorites, organizing searches, and moving through the purchase process with transparency and control.
image: https://jitty.com/assets/logo-white-b9bc1ab4.svg
json_schemas:
- name: GetSitesSiteidWebhooksResponse
  property_count: 9
  slug: jitty-get-sites-siteid-webhooks-response
- name: GetV2WorkspacesWorkspaceidorslugAuditLogsResponse
  property_count: 2
  slug: jitty-get-v2-workspaces-workspaceidorslug-audit-logs-response
- name: PostOauthAccessTokenRequest
  property_count: 3
  slug: jitty-post-oauth-access-token-request
- name: PostV2SitesSiteidRegisteredScriptsHostedRequest
  property_count: 5
  slug: jitty-post-v2-sites-siteid-registered-scripts-hosted-request
- name: PostV2SitesSiteidRegisteredScriptsHostedResponse
  property_count: 4
  slug: jitty-post-v2-sites-siteid-registered-scripts-hosted-response
- name: PostV2SitesSiteidRegisteredScriptsInlineRequest
  property_count: 4
  slug: jitty-post-v2-sites-siteid-registered-scripts-inline-request
jsonld:
- class_count: 19
  name: Jitty Context
  property_count: 26
  slug: jitty-context
layout: provider
modified: '2026-10-29'
name: Jitty
nav: Providers
network: true
overview: 'Jitty is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Home Buying, Artificial Intelligence, and Search.


  The Jitty catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Jitty''s developer surface includes getting-started guide, documentation, engineering blog, and 13 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 0
  name: Jitty Rate Limits
  slug: jitty-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Jitty API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: jitty-rules
scopes:
- name: Jitty Scopes
  scope_count: 0
  slug: jitty-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.9
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jitty/jitty-2026-11-03T134148.png
security:
- kind: authentication
  name: Jitty Authentication
  slug: jitty-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Jitty Domain Security
  slug: jitty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jitty
tags:
- Company
- Real Estate
- Home Buying
- Artificial Intelligence
- Search
- Marketplace
website: https://jitty.com/
---
