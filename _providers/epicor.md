---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Epicor Kinetic Open REST API exposes all ERP capabilities through OData v4 compliant endpoints covering business objects, processes, reports, Business Activity Queries (BAQs), and custom Epicor Fu
  name: Epicor Kinetic Open REST API
  slug: epicor-kinetic-rest-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/epicor/json-ld/epicor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/epicor-context.jsonld
- group: design
  href: https://artifacts.apis.io/epicor/vocabulary/epicor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/epicor-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/epicor/authentication/epicor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/epicor-authentication.yml
- group: design
  href: https://artifacts.apis.io/epicor/conformance/epicor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/epicor-conformance.yml
- group: agent
  href: https://artifacts.apis.io/epicor/llms/epicor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/epicor-llms.txt
- group: auth
  href: https://artifacts.apis.io/epicor/well-known/epicor-learncenter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/epicor-learncenter-security.txt
- group: agent
  href: https://artifacts.apis.io/epicor/well-known/epicor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/epicor-well-known.yml
- group: other
  href: https://artifacts.apis.io/epicor/hosts/epicor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/epicor-hosts.yml
- group: build
  href: https://artifacts.apis.io/epicor/integrations/epicor-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/epicor-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/epicor/vendors/epicor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/epicor-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.epicor.com/en-us/company/compliance/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.epicor.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.epicor.com/en-us/company/compliance/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.epicor.com/en-us/newsroom/
- group: auth
  href: https://artifacts.apis.io/epicor/security/epicor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/epicor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.epicor.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.epicor.com/en/products/enterprise-resource-planning-erp/epicor-kinetic/tools-and-technology/open-rest-api/
- group: company
  title: ''
  type: Blog
  url: https://www.epicor.com/en-us/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/epicor
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@epicor
coverage:
  checked: '2026-10-20'
  detail: Epicor publishes no OpenAPI or public reference; the Kinetic Open REST API is documented only in each customer tenant's built-in REST help, and developer.epicor.com redirects to the partners marketing page.
  evidence:
  - status: 200
    url: https://www.epicor.com/en/products/enterprise-resource-planning-erp/epicor-kinetic/tools-and-technology/open-rest-api/
  - status: 200
    url: https://developer.epicor.com/
  - status: 401
    url: https://epiccare.epicor.com/api/mcp
  reason: customer-only-docs
  state: gated
created: '2026-06-05'
description: Epicor Software Corporation provides industry-specific enterprise resource planning software for manufacturing, distribution, retail, and service industries. Epicor Kinetic, the flagship ERP platform, exposes an Open REST API built on OData v4 that gives developers service-based access to all business objects, processes, reports, BAQs, and Epicor Functions using standard HTTP methods and API key authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epicor.png
jsonld:
- class_count: 23
  name: Epicor Context
  property_count: 9
  slug: epicor-context
layout: provider
modified: '2026-10-20'
name: Epicor
nav: Providers
network: true
overview: 'Epicor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, Manufacturing, Distribution, Enterprise, and REST.


  The Epicor catalog on APIs.io includes 1 JSON-LD context.


  Epicor''s developer surface includes authentication, documentation, engineering blog, YouTube channel, and 16 more developer resources.'
plans:
- name: Epicor Plans Pricing
  plan_count: 0
  slug: epicor-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Epicor Rate Limits
  slug: epicor-rate-limits
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.3
    catalog_earned_first_party: 0.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 23.8
    discoverability: 67.9
    operational_transparency: 31.6
  previous_composite: 26.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/epicor/epicor-2026-06-20T180754.png
security:
- kind: authentication
  name: Epicor Authentication
  slug: epicor-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Epicor Domain Security
  slug: epicor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: epicor
tags:
- ERP
- Manufacturing
- Distribution
- Enterprise
- REST
- Fortune 500
website: https://www.epicor.com
---
