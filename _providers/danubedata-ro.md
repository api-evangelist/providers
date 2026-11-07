---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Danube Data API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Danube Data API
  slug: danubedata-ro-api
artifact_total: 15
asyncapis:
- description: ''
  name: Danubedata Ro Webhooks
  slug: danubedata-ro-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/danubedata-ro/rate-limits/danubedata-ro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/danubedata-ro-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/danubedata-ro/plans/danubedata-ro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/danubedata-ro-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/danubedata-ro/rules/danubedata-ro-rules.yml
  title: ''
  type: Spectral
  url: rules/danubedata-ro-rules.yml
- group: design
  href: https://artifacts.apis.io/danubedata-ro/json-ld/danubedata-ro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/danubedata-ro-context.jsonld
- group: design
  href: https://artifacts.apis.io/danubedata-ro/vocabulary/danubedata-ro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/danubedata-ro-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/danubedata-ro/asyncapi/danubedata-ro-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/danubedata-ro-webhooks.yml
- group: design
  href: https://artifacts.apis.io/danubedata-ro/data-model/danubedata-ro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/danubedata-ro-data-model.yml
- group: build
  href: https://artifacts.apis.io/danubedata-ro/cli/danubedata-ro-cli.yml
  title: ''
  type: CLI
  url: cli/danubedata-ro-cli.yml
- group: operate
  href: https://artifacts.apis.io/danubedata-ro/changelog/danubedata-ro-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/danubedata-ro-changelog.yml
- group: auth
  href: https://artifacts.apis.io/danubedata-ro/authentication/danubedata-ro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/danubedata-ro-authentication.yml
- group: design
  href: https://artifacts.apis.io/danubedata-ro/conformance/danubedata-ro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/danubedata-ro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/danubedata-ro/llms/danubedata-ro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/danubedata-ro-llms.txt
- group: auth
  href: https://artifacts.apis.io/danubedata-ro/well-known/danubedata-ro-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/danubedata-ro-status-security.txt
- group: auth
  href: https://artifacts.apis.io/danubedata-ro/well-known/danubedata-ro-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/danubedata-ro-security.txt
- group: auth
  href: https://artifacts.apis.io/danubedata-ro/well-known/danubedata-ro-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/danubedata-ro-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/danubedata-ro/well-known/danubedata-ro-console-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/danubedata-ro-console-security.txt
- group: agent
  href: https://artifacts.apis.io/danubedata-ro/well-known/danubedata-ro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/danubedata-ro-well-known.yml
- group: other
  href: https://artifacts.apis.io/danubedata-ro/hosts/danubedata-ro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/danubedata-ro-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://danubedata.ro/terms
- group: operate
  title: ''
  type: Support
  url: https://danubedata.ro/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.danubedata.ro
- group: auth
  title: ''
  type: Security
  url: https://danubedata.ro/blog/category/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://danubedata.ro/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://danubedata.ro/pricing
- group: start
  title: ''
  type: Login
  url: https://console.danubedata.ro/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://danubedata.ro/changelog
- group: company
  title: ''
  type: Blog
  url: https://danubedata.ro/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.danubedata.ro/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.danubedata.ro/
- group: auth
  href: https://artifacts.apis.io/danubedata-ro/security/danubedata-ro-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/danubedata-ro-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/danubedata-ro/security/danubedata-ro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/danubedata-ro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://danubedata.ro/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are JavaScript-rendered SPAs with no machine-readable spec.
  evidence:
  - status: 200
    url: https://docs.danubedata.ro
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: DanubeData provides managed EU cloud infrastructure, offering virtual machines, managed databases, in‑memory caches, object storage and serverless containers to developers and businesses. The platform includes a CLI, Terraform and Pulumi providers, and a managed Kubernetes control plane, all hosted in German GDPR‑compliant data centres.
image: https://danubedata.ro/images/danubedata_logo.png
json_schemas:
- name: GetApiV1StorageBucketsResponse
  property_count: 2
  slug: danubedata-ro-get-api-v1-storage-buckets-response
- name: PostApiV1ServerlessContaineridRunsResponse
  property_count: 4
  slug: danubedata-ro-post-api-v1-serverless-containerid-runs-response
- name: PostApiV1StorageAccessKeysRequest
  property_count: 4
  slug: danubedata-ro-post-api-v1-storage-access-keys-request
- name: PostApiV1StorageBucketsIdPolicyFolderGrantsRequest
  property_count: 4
  slug: danubedata-ro-post-api-v1-storage-buckets-id-policy-folder-grants-request
- name: PostApiV1StorageBucketsIdPolicyFolderGrantsResponse
  property_count: 5
  slug: danubedata-ro-post-api-v1-storage-buckets-id-policy-folder-grants-response
- name: PostApiV1StorageBucketsRequest
  property_count: 7
  slug: danubedata-ro-post-api-v1-storage-buckets-request
jsonld:
- class_count: 20
  name: Danubedata Ro Context
  property_count: 36
  slug: danubedata-ro-context
layout: provider
modified: '2026-11-04'
name: Danube Data
nav: Providers
network: true
overview: 'Danube Data is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Virtual Machines, Managed Database, Object Storage, and Serverless.


  The Danube Data catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Danube Data''s developer surface includes CLI, changelog, authentication, support, pricing, engineering blog, getting-started guide, and 25 more developer resources.'
plans:
- name: Danubedata Ro Plans Pricing
  plan_count: 29
  slug: danubedata-ro-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 12
  name: Danubedata Ro Rate Limits
  slug: danubedata-ro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Danube Data API Rules
  rule_count: 42
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 2
  slug: danubedata-ro-rules
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 32.8
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 81.6
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
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Danubedata Ro Authentication
  slug: danubedata-ro-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Danubedata Ro Domain Security
  slug: danubedata-ro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Danubedata Ro Vulnerability Disclosure
  slug: danubedata-ro-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: danubedata-ro
tags:
- Cloud
- Virtual Machines
- Managed Database
- Object Storage
- Serverless
- Kubernetes
- Caching
- Developer Tools
website: https://danubedata.ro/
---
