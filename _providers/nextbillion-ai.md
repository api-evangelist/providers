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
  scored_at: '2026-10-17'
api_count: 8
apis:
- description: Location‑based routing and optimization APIs as described in the developer documentation.
  name: NextBillion AI API
  slug: nextbillion-ai-api-2
- baseURL: https://api.nextbillion.io
  baseurl_source: declared
  description: The Directions API from NextBillion.ai — 1 operation(s) for directions.
  name: NextBillion.ai Directions API
  slug: nextbillion-ai-directions-api
- baseURL: https://api.nextbillion.io
  baseurl_source: declared
  description: The Distancematrix API from NextBillion.ai — 1 operation(s) for distancematrix.
  name: NextBillion.ai Distancematrix API
  slug: nextbillion-ai-distancematrix-api
- baseURL: https://api.nextbillion.io
  baseurl_source: declared
  description: The Hos API from NextBillion.ai — 1 operation(s) for hos.
  name: NextBillion.ai Hos API
  slug: nextbillion-ai-hos-api
- baseURL: https://api.nextbillion.io
  baseurl_source: declared
  description: The Isochrone API from NextBillion.ai — 1 operation(s) for isochrone.
  name: NextBillion.ai Isochrone API
  slug: nextbillion-ai-isochrone-api
- baseURL: https://api.nextbillion.io
  baseurl_source: declared
  description: The Mdm API from NextBillion.ai — 2 operation(s) for mdm.
  name: NextBillion.ai Mdm API
  slug: nextbillion-ai-mdm-api
- baseURL: https://api.nextbillion.io
  baseurl_source: declared
  description: The Navigation API from NextBillion.ai — 2 operation(s) for navigation.
  name: NextBillion.ai Navigation API
  slug: nextbillion-ai-navigation-api
- baseURL: https://api.nextbillion.io
  baseurl_source: declared
  description: The Optimization API from NextBillion.ai — 5 operation(s) for optimization.
  name: NextBillion.ai Optimization API
  slug: nextbillion-ai-optimization-api
artifact_total: 16
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/rules/nextbillion-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/nextbillion-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/json-ld/nextbillion-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nextbillion-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/vocabulary/nextbillion-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nextbillion-ai-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/data-model/nextbillion-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nextbillion-ai-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/changelog/nextbillion-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nextbillion-ai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/conformance/nextbillion-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nextbillion-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/llms/nextbillion-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nextbillion-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/hosts/nextbillion-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nextbillion-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/vendors/nextbillion-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nextbillion-ai-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/packages/nextbillion-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/nextbillion-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/packages/nextbillion-ai-packages.yml
  title: ''
  type: Packages
  url: packages/nextbillion-ai-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://nextbillion.ai/trust-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nextbillion.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nextbillion.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://nextbillion.ai/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://nextbillion.ai/get-started
- group: company
  title: ''
  type: Blog
  url: https://nextbillion.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nextbillion.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.nextbillion.io/optimization/v2?key={your_api_key}</p
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nextbillion-ai/refs/heads/main/security/nextbillion-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nextbillion-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nextbillion.ai/
coverage:
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.nextbillion.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: NextBillion.ai provides a suite of location‑based routing and optimization APIs, including Route Optimization, Distance Matrix, Directions, Driver Assignment, and Navigation SDKs. Their platform leverages AI to deliver accurate ETAs, dynamic routing, and fleet management solutions for logistics, delivery, and field service operations. The company offers on‑premise deployment and extensive documentation for developers.
image: https://nextbillion.ai/wp-content/uploads/2025/01/Home-OG-V2.png
json_schemas:
- name: GetMdmStatusResponse
  property_count: 3
  slug: nextbillion-ai-get-mdm-status-response
- name: GetNavigationJsonResponse
  property_count: 2
  slug: nextbillion-ai-get-navigation-json-response
- name: GetNavigationResponse
  property_count: 2
  slug: nextbillion-ai-get-navigation-response
- name: PostNavigationRequest
  property_count: 6
  slug: nextbillion-ai-post-navigation-request
- name: PostNavigationResponse
  property_count: 2
  slug: nextbillion-ai-post-navigation-response
jsonld:
- class_count: 5
  name: Nextbillion Ai Context
  property_count: 10
  slug: nextbillion-ai-context
layout: provider
modified: '2026-10-13'
name: NextBillion.ai
nav: Providers
network: true
overview: 'NextBillion.ai is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Directions API, Distancematrix API, Hos API, and 5 more. Tagged areas include Company, Routing, Logistics, Artificial Intelligence, and Mapping.


  The NextBillion.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NextBillion.ai''s developer surface includes changelog, pricing, getting-started guide, engineering blog, documentation, and 16 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: NextBillion.ai API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: nextbillion-ai-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 24.6
    developer_ergonomics: 40.5
    discoverability: 69.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Nextbillion Ai Domain Security
  slug: nextbillion-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nextbillion-ai
tags:
- Company
- Routing
- Logistics
- Artificial Intelligence
- Mapping
website: https://nextbillion.ai/
---
