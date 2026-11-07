---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for Jitterbit integration platform
  name: Jitterbit API
  slug: jitterbit-api
- baseURL: https://na-east.jitterbit.com
  baseurl_source: declared
  description: 'Jitterbit API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Jitterbit API
  slug: ebridgeconnections-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/ebridgeconnections/rules/ebridgeconnections-rules.yml
  title: ''
  type: Spectral
  url: rules/ebridgeconnections-rules.yml
- group: design
  href: https://artifacts.apis.io/ebridgeconnections/json-ld/ebridgeconnections-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ebridgeconnections-context.jsonld
- group: design
  href: https://artifacts.apis.io/ebridgeconnections/vocabulary/ebridgeconnections-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ebridgeconnections-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ebridgeconnections/data-model/ebridgeconnections-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ebridgeconnections-data-model.yml
- group: build
  href: https://artifacts.apis.io/ebridgeconnections/cli/ebridgeconnections-cli.yml
  title: ''
  type: CLI
  url: cli/ebridgeconnections-cli.yml
- group: design
  href: https://artifacts.apis.io/ebridgeconnections/conformance/ebridgeconnections-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ebridgeconnections-conformance.yml
- group: other
  href: https://artifacts.apis.io/ebridgeconnections/hosts/ebridgeconnections-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ebridgeconnections-hosts.yml
- group: other
  href: https://artifacts.apis.io/ebridgeconnections/vendors/ebridgeconnections-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ebridgeconnections-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jitterbit.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.jitterbit.com/support/
- group: auth
  title: ''
  type: Security
  url: https://www.jitterbit.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jitterbit.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jitterbit.com/harmony/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.jitterbit.com/resources/type/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.jitterbit.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.jitterbit.com/blog/ai-roi/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jitterbit.com/api-manager/quickstart-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jitterbit.com/
- group: auth
  href: https://artifacts.apis.io/ebridgeconnections/security/ebridgeconnections-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ebridgeconnections-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ebridgeconnections.com/
coverage:
  checked: '2026-10-20'
  detail: Documentation at https://docs.jitterbit.com/ provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://docs.jitterbit.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Jitterbit provides an AI‑powered integration platform that enables enterprises to connect applications, data, and devices with low‑code tools, API management, and managed file transfer. The company offers solutions for iPaaS, EDI, API management, and a Managed Cloud Platform, supporting automation, orchestration, and AI‑driven workflows across industries. Jitterbit’s platform is used by thousands of organizations worldwide to accelerate digital transformation and streamline business processes.
image: https://www.jitterbit.com/wp-content/uploads/jitterbit-social-banner.jpg
json_schemas:
- name: DeleteRestV1SalesCustomers9Ce3347486904A75Ab9065Caa6C3C24ERe
  property_count: 4
  slug: ebridgeconnections-delete-rest-v1-sales-customers9-ce3347486904-a75-ab9065-caa6-c3-c24-ere
- name: GetRestV1VinylDeployMetadataResponse
  property_count: 6
  slug: ebridgeconnections-get-rest-v1-vinyl-deploy-metadata-response
- name: PostRestV1SalesCustomersResponse
  property_count: 4
  slug: ebridgeconnections-post-rest-v1-sales-customers-response
- name: PostRestV1VinylDeployReleaseQueueRequest
  property_count: 3
  slug: ebridgeconnections-post-rest-v1-vinyl-deploy-release-queue-request
- name: PostRestV1VinylDeployReleaseRequest
  property_count: 3
  slug: ebridgeconnections-post-rest-v1-vinyl-deploy-release-request
- name: PutJitterbitCloudRestfulServiceUserLoginResponse
  property_count: 8
  slug: ebridgeconnections-put-jitterbit-cloud-restful-service-user-login-response
jsonld:
- class_count: 15
  name: Ebridgeconnections Context
  property_count: 30
  slug: ebridgeconnections-context
layout: provider
modified: '2026-10-20'
name: Jitterbit
nav: Providers
network: true
overview: 'Jitterbit is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Automation, API Management, iPaaS, and Enterprise.


  The Jitterbit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Jitterbit''s developer surface includes CLI, support, pricing, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Jitterbit API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ebridgeconnections-rules
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 21.4
    discoverability: 58.9
    operational_transparency: 5.3
  previous_composite: 29.8
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
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ebridgeconnections/ebridgeconnections-2026-11-03T131249.png
security:
- kind: domain-security
  name: Ebridgeconnections Domain Security
  slug: ebridgeconnections-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: ebridgeconnections
tags:
- Integration
- Automation
- API Management
- iPaaS
- Enterprise
website: https://ebridgeconnections.com/
---
