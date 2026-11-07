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
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Deployment.io platform, providing access to AI agent management and deployment operations.
  name: Deployment.io API
  slug: deployment-io-api-2
- description: 'Deployment AI Inc. API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Deployment AI Inc. API
  slug: deployment-io-api
artifact_total: 9
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://deployment.io/docs/runner-installation/aws-setup
- group: design
  href: https://artifacts.apis.io/deployment-io/rules/deployment-io-rules.yml
  title: ''
  type: Spectral
  url: rules/deployment-io-rules.yml
- group: design
  href: https://artifacts.apis.io/deployment-io/json-ld/deployment-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deployment-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/deployment-io/vocabulary/deployment-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deployment-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deployment-io/data-model/deployment-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deployment-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/deployment-io/conformance/deployment-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deployment-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deployment-io/llms/deployment-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deployment-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/deployment-io/well-known/deployment-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deployment-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/deployment-io/hosts/deployment-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deployment-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/deployment-io/vendors/deployment-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deployment-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deployment.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deployment.io/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deployment-io
- group: auth
  href: https://artifacts.apis.io/deployment-io/security/deployment-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deployment-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deployment.io/
- group: docs
  title: ''
  type: Documentation
  url: https://deployment.io/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://deployment.io/pricing/
- group: auth
  title: ''
  type: Security
  url: https://deployment.io/security/
- group: company
  title: ''
  type: Blog
  url: https://deployment.io/blog/
coverage:
  checked: '2026-11-05'
  detail: Documentation is public but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract is published.
  evidence:
  - status: 200
    url: https://deployment.io/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Deployment AI Inc. provides senior engineers and AI agents to take software from specification to production, offering modernisation, remediation, and managed engineering delivery across cloud environments. Their platform enables customers to define specifications, approve deployments, and benefit from security, compliance, and migration services, all powered by AI-driven coding agents and expert engineering capacity.
image: https://deployment.io/images/how-deployment-io-works.png
json_schemas:
- name: GetOldResponse
  property_count: 1
  slug: deployment-io-get-old-response
- name: GetVersionResponse
  property_count: 1
  slug: deployment-io-get-version-response
- name: PostItemsRequest
  property_count: 1
  slug: deployment-io-post-items-request
jsonld:
- class_count: 3
  name: Deployment Io Context
  property_count: 3
  slug: deployment-io-context
layout: provider
modified: '2026-11-05'
name: Deployment AI Inc.
nav: Providers
network: true
overview: 'Deployment AI Inc. is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Engineering, Cloud, Automation, and Deployment.


  The Deployment AI Inc. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Deployment AI Inc.''s developer surface includes getting-started guide, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Deployment Io Plans Pricing
  plan_count: 0
  slug: deployment-io-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Deployment AI Inc. API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: deployment-io-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deployment Io Domain Security
  slug: deployment-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: deployment-io
tags:
- Artificial Intelligence
- Engineering
- Cloud
- Automation
- Deployment
website: https://deployment.io/
---
