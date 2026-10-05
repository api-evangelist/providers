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
  scored_at: '2026-10-04'
api_count: 2
apis:
- description: Public API reference for Tencent Cloud services
  name: Tencent Cloud API
  slug: tencent-cloud-api
- description: The Exampleobject API from Tencent Cloud — 1 operation(s) for exampleobject.
  name: Tencent Cloud Exampleobject API
  slug: tencentcloud-exampleobject-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tencentcloud/refs/heads/main/plans/tencentcloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tencentcloud-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tencentcloud/refs/heads/main/rules/tencentcloud-rules.yml
  title: ''
  type: Spectral
  url: rules/tencentcloud-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tencentcloud/refs/heads/main/conformance/tencentcloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tencentcloud-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tencentcloud/refs/heads/main/llms/tencentcloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tencentcloud-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tencentcloud/refs/heads/main/hosts/tencentcloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tencentcloud-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tencentcloud/refs/heads/main/vendors/tencentcloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tencentcloud-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tencentcloud/refs/heads/main/packages/tencentcloud-packages.yml
  title: ''
  type: SDKs
  url: packages/tencentcloud-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tencentcloud/refs/heads/main/packages/tencentcloud-packages.yml
  title: ''
  type: Packages
  url: packages/tencentcloud-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tencentcloud.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tencentcloud/refs/heads/main/security/tencentcloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tencentcloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tencentcloud.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.tencent.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.tencent.com/document/product
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.tencent.com/document/api
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.tencent.com/guide
- group: operate
  title: ''
  type: Support
  url: https://cloud.tencent.com/act
- group: company
  title: ''
  type: Blog
  url: https://cloud.tencent.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://buy.cloud.tencent.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.tencent.com/register
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/tencentcloud/workspace
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on discovered hosts.
  evidence:
  - status: 404
    url: https://api.tencentcloud.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Tencent Cloud provides a comprehensive suite of cloud computing services, including compute, storage, database, AI, and networking solutions for enterprises and developers worldwide. It offers a global infrastructure, advanced security, and integrated AI capabilities, supporting a wide range of industries and enabling digital transformation.
layout: provider
modified: '2026-10-03'
name: Tencent Cloud
nav: Providers
network: true
overview: 'Tencent Cloud publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Exampleobject API, and 1 more. Tagged areas include Cloud, Computing, Artificial Intelligence, Infrastructure, and Services.


  The Tencent Cloud catalog on APIs.io includes 1 Spectral governance ruleset.


  Tencent Cloud''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Tencentcloud Plans Pricing
  plan_count: 3
  slug: tencentcloud-plans-pricing
random_paper: 12
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Tencent Cloud API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: tencentcloud-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.5
    catalog_earned_first_party: 12.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 57.1
    discoverability: 60.7
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Tencentcloud Domain Security
  slug: tencentcloud-domain-security
  summary_line: TLSv1.3
slug: tencentcloud
tags:
- Cloud
- Computing
- Artificial Intelligence
- Infrastructure
- Services
- Tencent
website: https://www.tencentcloud.com
---
