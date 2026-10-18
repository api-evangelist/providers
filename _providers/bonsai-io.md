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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-10-17'
api_count: 4
apis:
- baseURL: https://api.bonsai.io
  baseurl_source: declared
  description: The Clusters API from Bonsai — 2 operation(s) for clusters.
  name: Bonsai Clusters API
  slug: bonsai-io-clusters-api
- baseURL: https://api.bonsai.io
  baseurl_source: declared
  description: The Plans API from Bonsai — 2 operation(s) for plans.
  name: Bonsai Plans API
  slug: bonsai-io-plans-api
- baseURL: https://api.bonsai.io
  baseurl_source: declared
  description: The Releases API from Bonsai — 2 operation(s) for releases.
  name: Bonsai Releases API
  slug: bonsai-io-releases-api
- baseURL: https://api.bonsai.io
  baseurl_source: declared
  description: The Spaces API from Bonsai — 2 operation(s) for spaces.
  name: Bonsai Spaces API
  slug: bonsai-io-spaces-api
artifact_total: 16
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/rate-limits/bonsai-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bonsai-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/plans/bonsai-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bonsai-io-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/rules/bonsai-io-rules.yml
  title: ''
  type: Spectral
  url: rules/bonsai-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/json-ld/bonsai-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bonsai-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/vocabulary/bonsai-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bonsai-io-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/data-model/bonsai-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bonsai-io-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/conventions/bonsai-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bonsai-io-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/authentication/bonsai-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bonsai-io-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/scopes/bonsai-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bonsai-io-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/lifecycle/bonsai-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bonsai-io-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/errors/bonsai-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bonsai-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/conformance/bonsai-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bonsai-io-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/well-known/bonsai-io-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bonsai-io-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/well-known/bonsai-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bonsai-io-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/hosts/bonsai-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonsai-io-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/vendors/bonsai-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonsai-io-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/packages/bonsai-io-packages.yml
  title: ''
  type: SDKs
  url: packages/bonsai-io-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/packages/bonsai-io-packages.yml
  title: ''
  type: Packages
  url: packages/bonsai-io-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bonsai.io/
- group: auth
  title: ''
  type: Security
  url: https://bonsai.io/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-io/refs/heads/main/security/bonsai-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonsai-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bonsai.io
- group: docs
  title: ''
  type: Documentation
  url: https://bonsai.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://bonsai.io/docs/api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://bonsai.io/docs/get-started/
- group: company
  title: ''
  type: Blog
  url: https://bonsai.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omc
- group: start
  title: ''
  type: Login
  url: https://app.bonsai.io/login
- group: start
  title: ''
  type: SignUp
  url: https://app.bonsai.io/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://bonsai.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bonsai.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bonsai.io/terms
- group: operate
  title: ''
  type: Support
  url: https://bonsai.io/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 403
    url: https://status.bonsai.io/mcp
  - status: 200
    url: https://bonsai.io
  reason: partner-login
  state: gated
created: '2026-10-13'
description: Bonsai, made by One More Cloud, is a fully managed hosted Elasticsearch and OpenSearch search service (managed or bring-your-own-cloud on AWS and Google Cloud), with vector search, a Heroku add-on and a Terraform provider. Its Bonsai Cloud REST API at https://api.bonsai.io (alpha) manages clusters and lists plans, releases (search engine versions) and spaces (regions), authenticated with Basic or Bearer API tokens.
image: https://cdn.prod.website-files.com/63c81e4decde60c281417feb/6807c033856de7919fd4ad83_opengraph-home.jpg
json_schemas:
- name: Cluster
  property_count: 9
  slug: bonsai-io-cluster
- name: Pagination
  property_count: 3
  slug: bonsai-io-pagination
- name: Plan
  property_count: 8
  slug: bonsai-io-plan
- name: Release
  property_count: 4
  slug: bonsai-io-release
- name: Space
  property_count: 3
  slug: bonsai-io-space
jsonld:
- class_count: 6
  name: Bonsai Io Context
  property_count: 24
  slug: bonsai-io-context
layout: provider
modified: '2026-10-14'
name: Bonsai
nav: Providers
network: true
overview: 'Bonsai is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Plans API, Releases API, and 1 more. Tagged areas include Company, Search, Elasticsearch, OpenSearch, and Managed Service.


  The Bonsai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bonsai''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, and 26 more developer resources.'
plans:
- name: Bonsai Io Plans Pricing
  plan_count: 12
  slug: bonsai-io-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Bonsai Io Rate Limits
  slug: bonsai-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Bonsai API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: bonsai-io-rules
scopes:
- name: Bonsai Io Scopes
  scope_count: 3
  slug: bonsai-io-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 30.3
    developer_ergonomics: 54.8
    discoverability: 71.4
    operational_transparency: 52.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bonsai Io Authentication
  slug: bonsai-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bonsai Io Domain Security
  slug: bonsai-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bonsai-io
tags:
- Company
- Search
- Elasticsearch
- OpenSearch
- Managed Service
- Vector Search
- Cloud Infrastructure
website: https://bonsai.io
---
