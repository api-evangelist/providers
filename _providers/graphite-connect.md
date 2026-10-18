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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: Supplier management platform API (details not publicly documented)
  name: Graphite Connect API
  slug: graphite-connect-api-2
- baseURL: https://poc.projectgraphite.com
  baseurl_source: declared
  description: The Oauth API from Graphite Connect — 2 operation(s) for oauth.
  name: Graphite Connect OAuth API
  slug: graphite-connect-oauth-api
- baseURL: https://poc.projectgraphite.com
  baseurl_source: declared
  description: The Profile API from Graphite Connect — 1 operation(s) for profile.
  name: Graphite Connect Profile API
  slug: graphite-connect-profile-api
- baseURL: https://poc.projectgraphite.com
  baseurl_source: declared
  description: The Search API from Graphite Connect — 1 operation(s) for search.
  name: Graphite Connect Search API
  slug: graphite-connect-search-api
artifact_total: 13
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/rules/graphite-connect-rules.yml
  title: ''
  type: Spectral
  url: rules/graphite-connect-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/json-ld/graphite-connect-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/graphite-connect-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/vocabulary/graphite-connect-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/graphite-connect-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/data-model/graphite-connect-data-model.yml
  title: ''
  type: DataModel
  url: data-model/graphite-connect-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/changelog/graphite-connect-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/graphite-connect-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/conventions/graphite-connect-conventions.yml
  title: ''
  type: Conventions
  url: conventions/graphite-connect-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/authentication/graphite-connect-authentication.yml
  title: ''
  type: Authentication
  url: authentication/graphite-connect-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/conformance/graphite-connect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/graphite-connect-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/llms/graphite-connect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/graphite-connect-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/well-known/graphite-connect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/graphite-connect-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/hosts/graphite-connect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/graphite-connect-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/vendors/graphite-connect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/graphite-connect-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.graphiteconnect.com/
- group: auth
  title: ''
  type: Security
  url: https://www.graphiteconnect.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.graphiteconnect.com/legal/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.graphiteconnect.com/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.graphiteconnect.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.graphiteconnect.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.graphiteconnect.com/docs/netsuite-suiteapp-1
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/scopes/graphite-connect-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/graphite-connect-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/graphite-connect/refs/heads/main/security/graphite-connect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/graphite-connect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.graphiteconnect.com
- group: company
  title: ''
  type: Blog
  url: https://www.graphiteconnect.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.graphiteconnect.com/product
- group: commercial
  title: ''
  type: Pricing
  url: https://www.graphiteconnect.com/solutions
- group: operate
  title: ''
  type: Support
  url: https://www.graphiteconnect.com/press
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://apidocs.graphiteconnect.com/mcp
  - status: 401
    url: https://app.graphiteconnect.com/mcp
  - status: 200
    url: https://www.graphiteconnect.com
  reason: partner-login
  state: gated
created: '2026-10-13'
description: Graphite Connect provides a supplier management platform that automates procurement workflows, offers AI‑driven validation, risk assessments, and a patented network approach to consolidate supplier data. The solution helps global procurement teams onboard suppliers faster, improve data quality, and gain visibility across the supply chain, addressing the chaos of bad supplier data with integrated compliance, risk, and relationship management tools.
image: https://cdn.prod.website-files.com/691cd35f19ecbb108803b3a7/697ae1b53f8e0b2511a8f48b_og.jpg
json_schemas:
- name: PatchProfilePublicidRequest
  property_count: 1
  slug: graphite-connect-patch-profile-publicid-request
- name: PatchProfilePublicidResponse
  property_count: 1
  slug: graphite-connect-patch-profile-publicid-response
- name: PostApiOauthTokenRequest
  property_count: 3
  slug: graphite-connect-post-api-oauth-token-request
- name: PostOauthTokenRequest
  property_count: 3
  slug: graphite-connect-post-oauth-token-request
jsonld:
- class_count: 4
  name: Graphite Connect Context
  property_count: 3
  slug: graphite-connect-context
layout: provider
modified: '2026-10-13'
name: Graphite Connect
nav: Providers
network: true
overview: 'Graphite Connect is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including OAuth API, Profile API, Search API, and 1 more. Tagged areas include Company, Supplier Management, Procurement, Artificial Intelligence, and Risk Management.


  The Graphite Connect catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Graphite Connect''s developer surface includes changelog, authentication, API reference, getting-started guide, engineering blog, documentation, pricing, and 19 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Graphite Connect API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: graphite-connect-rules
scopes:
- name: Graphite Connect Scopes
  scope_count: 1
  slug: graphite-connect-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 47.6
    discoverability: 71.4
    operational_transparency: 42.1
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
    score: 28.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Graphite Connect Authentication
  slug: graphite-connect-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Graphite Connect Domain Security
  slug: graphite-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: graphite-connect
tags:
- Company
- Supplier Management
- Procurement
- Artificial Intelligence
- Risk Management
website: https://www.graphiteconnect.com
---
