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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.4
  scored_at: '2026-10-17'
api_count: 3
apis:
- baseURL: https://api.cloudploy.com
  baseurl_source: declared
  description: The Apps API from CloudPloy — 3 operation(s) for apps.
  name: CloudPloy Apps API
  slug: cloudploy-apps-api
- baseURL: https://api.cloudploy.com
  baseurl_source: declared
  description: The Deployments API from CloudPloy — 2 operation(s) for deployments.
  name: CloudPloy Deployments API
  slug: cloudploy-deployments-api
- baseURL: https://api.cloudploy.com
  baseurl_source: declared
  description: The Rollback API from CloudPloy — 1 operation(s) for rollback.
  name: CloudPloy Rollback API
  slug: cloudploy-rollback-api
artifact_total: 10
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/plans/cloudploy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudploy-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/rules/cloudploy-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudploy-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/json-ld/cloudploy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudploy-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/vocabulary/cloudploy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudploy-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/data-model/cloudploy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudploy-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/conformance/cloudploy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudploy-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/llms/cloudploy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudploy-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/well-known/cloudploy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudploy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/hosts/cloudploy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudploy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/vendors/cloudploy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudploy-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cloudploy.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloudploy.com/for/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudploy/refs/heads/main/security/cloudploy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudploy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudploy.com
- group: docs
  title: ''
  type: Documentation
  url: https://cloudploy.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cloudploy.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://cloudploy.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cloudploy.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloudploy.com
- group: operate
  title: ''
  type: Support
  url: https://cloudploy.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudploy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudploy.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://cloudploy.com/blog
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cloudploy/workspace
coverage:
  checked: '2026-10-15'
  detail: API documentation page https://cloudploy.com/docs/api returns HTML with no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://cloudploy.com/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: CloudPloy provides a platform that lets developers deploy applications to any cloud or VPS using AI agents. Through its MCP (Machine Control Plane), users can manage servers, apps, and deployments via a RESTful API, enabling automation of the full lifecycle from provisioning to scaling. The service offers a free tier with limited resources and paid plans for larger workloads, focusing on ease of use, security, and integration with existing CI/CD pipelines.
image: https://cloudploy.com/cloudploy-share-light-2026.png
json_schemas:
- name: PostAppsRequest
  property_count: 1
  slug: cloudploy-post-apps-request
- name: PostDeploymentsRequest
  property_count: 3
  slug: cloudploy-post-deployments-request
- name: PostV1AppsRequest
  property_count: 1
  slug: cloudploy-post-v1-apps-request
jsonld:
- class_count: 3
  name: Cloudploy Context
  property_count: 4
  slug: cloudploy-context
layout: provider
modified: '2026-10-15'
name: CloudPloy
nav: Providers
network: true
overview: 'CloudPloy is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Apps API, Deployments API, and Rollback API. Tagged areas include Company, Deployment, Artificial Intelligence, Cloud, and Automation.


  The CloudPloy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CloudPloy''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 17 more developer resources.'
plans:
- name: Cloudploy Plans Pricing
  plan_count: 4
  slug: cloudploy-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: CloudPloy API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: cloudploy-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 50.0
    discoverability: 78.6
    operational_transparency: 10.5
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
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Cloudploy Domain Security
  slug: cloudploy-domain-security
  summary_line: TLSv1.3
slug: cloudploy
tags:
- Company
- Deployment
- Artificial Intelligence
- Cloud
- Automation
website: https://cloudploy.com
---
