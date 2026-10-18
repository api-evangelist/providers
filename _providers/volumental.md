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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-10-17'
api_count: 8
apis:
- baseURL: https://api.volumental.com
  baseurl_source: declared
  description: The Auth API from Volumental — 1 operation(s) for auth.
  name: Volumental Auth API
  slug: volumental-auth-api
- baseURL: https://api.volumental.com
  baseurl_source: declared
  description: The Oauth API from Volumental — 1 operation(s) for oauth.
  name: Volumental OAuth API
  slug: volumental-oauth-api
- baseURL: https://api.volumental.com
  baseurl_source: declared
  description: The Recommendations API from Volumental — 1 operation(s) for recommendations.
  name: Volumental Recommendations API
  slug: volumental-recommendations-api
- baseURL: https://api.volumental.com
  baseurl_source: declared
  description: The Scans API from Volumental — 3 operation(s) for scans.
  name: Volumental Scans API
  slug: volumental-scans-api
- baseURL: https://api.volumental.com
  baseurl_source: declared
  description: The Some Endpoint API from Volumental — 1 operation(s) for some endpoint.
  name: Volumental Some Endpoint API
  slug: volumental-some-endpoint-api
- baseURL: https://api.volumental.com
  baseurl_source: declared
  description: The V1Alpha API from Volumental — 2 operation(s) for v1alpha.
  name: Volumental V1Alpha API
  slug: volumental-v1alpha-api
- baseURL: https://api.volumental.com
  baseurl_source: declared
  description: The V1Beta API from Volumental — 2 operation(s) for v1beta.
  name: Volumental V1Beta API
  slug: volumental-v1beta-api
- baseURL: https://api.volumental.com
  baseurl_source: declared
  description: The Volumental API API from Volumental — 1 operation(s) for volumental api.
  name: Volumental Volumental API
  slug: volumental-volumental-api-api
artifact_total: 18
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/rules/volumental-rules.yml
  title: ''
  type: Spectral
  url: rules/volumental-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/json-ld/volumental-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/volumental-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/vocabulary/volumental-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/volumental-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/data-model/volumental-data-model.yml
  title: ''
  type: DataModel
  url: data-model/volumental-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/authentication/volumental-authentication.yml
  title: ''
  type: Authentication
  url: authentication/volumental-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/conformance/volumental-conformance.yml
  title: ''
  type: Conformance
  url: conformance/volumental-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/llms/volumental-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/volumental-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/well-known/volumental-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/volumental-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/hosts/volumental-hosts.yml
  title: ''
  type: Hosts
  url: hosts/volumental-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/vendors/volumental-vendors.yml
  title: ''
  type: Vendors
  url: vendors/volumental-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://volumental.com/press
- group: docs
  title: ''
  type: APIReference
  url: https://developer.volumental.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.volumental.com/docs/getting-started-recommendations
- group: docs
  title: ''
  type: Documentation
  url: https://developer.volumental.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Volumental
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/volumental/refs/heads/main/security/volumental-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/volumental-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://volumental.com/
- group: company
  title: ''
  type: Blog
  url: https://volumental.com/blog
- group: operate
  title: ''
  type: Support
  url: https://volumental.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://volumental.com/policy/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://volumental.com/policy/terms-of-service
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite accessible developer documentation.
  evidence:
  - status: 200
    url: https://developer.volumental.com/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Volumental provides 3D foot scanning and shoe fitting technology for retailers, enabling fast and accurate size recommendations both in‑store and online. Founded in 2012 by PhD researchers and a former NASA rocket scientist, the company leverages a large dataset of foot scans to power AI‑driven fit engines, omnichannel tools, and analytics that improve conversion and reduce returns. Their solutions integrate with Shopify, other e‑commerce platforms, and offer SDKs for mobile scanning, serving thousands of stores worldwide.
image: https://volumental.com/hubfs/Volumental_1554%20copy.jpg
json_schemas:
- name: GetApiV1ScansWebResponse
  property_count: 4
  slug: volumental-get-api-v1-scans-web-response
- name: GetApiV1SomeEndpointResponse
  property_count: 4
  slug: volumental-get-api-v1-some-endpoint-response
- name: GetV1BetaTenantnameInventoryResponse
  property_count: 4
  slug: volumental-get-v1-beta-tenantname-inventory-response
- name: GetV1BetaTenantnameResponse
  property_count: 4
  slug: volumental-get-v1-beta-tenantname-response
- name: PatchV1BetaTenantnameInventoryResponse
  property_count: 4
  slug: volumental-patch-v1-beta-tenantname-inventory-response
- name: PostApiV1RecommendationsResponse
  property_count: 3
  slug: volumental-post-api-v1-recommendations-response
jsonld:
- class_count: 13
  name: Volumental Context
  property_count: 13
  slug: volumental-context
layout: provider
modified: '2026-10-15'
name: Volumental
nav: Providers
network: true
overview: 'Volumental is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Auth API, OAuth API, Recommendations API, and 5 more. Tagged areas include Company, Retail, Footwear, 3DScanning, and Artificial Intelligence.


  The Volumental catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Volumental''s developer surface includes authentication, API reference, getting-started guide, documentation, engineering blog, support, and 15 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Volumental API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: volumental-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 47.6
    discoverability: 80.4
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Volumental Authentication
  slug: volumental-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Volumental Domain Security
  slug: volumental-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: volumental
tags:
- Company
- Retail
- Footwear
- 3DScanning
- Artificial Intelligence
website: https://volumental.com/
---
