---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'FileFlows API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: FileFlows API
  slug: fileflows-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/fileflows/plans/fileflows-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fileflows-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fileflows/rules/fileflows-rules.yml
  title: ''
  type: Spectral
  url: rules/fileflows-rules.yml
- group: design
  href: https://artifacts.apis.io/fileflows/json-ld/fileflows-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fileflows-context.jsonld
- group: design
  href: https://artifacts.apis.io/fileflows/vocabulary/fileflows-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fileflows-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fileflows/data-model/fileflows-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fileflows-data-model.yml
- group: design
  href: https://artifacts.apis.io/fileflows/conformance/fileflows-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fileflows-conformance.yml
- group: other
  href: https://artifacts.apis.io/fileflows/hosts/fileflows-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fileflows-hosts.yml
- group: other
  href: https://artifacts.apis.io/fileflows/vendors/fileflows-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fileflows-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://fileflows.com/Vb497vM386w2f38Dg47D/repo/webhook
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fileflows.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://fileflows.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fileflows
- group: auth
  href: https://artifacts.apis.io/fileflows/security/fileflows-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fileflows-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fileflows.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fileflows.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://fileflows.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://fileflows.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://fileflows.com/docs/api/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered by Docusaurus JavaScript and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://fileflows.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: FileFlows provides an automated file processing platform that lets users design, schedule, and run pipelines for tasks like video transcoding, audio processing, image conversion, and ebook handling. It supports self‑hosted deployments on single servers or distributed clusters, offering a visual drag‑and‑drop flow editor, real‑time monitoring, extensible plugins, and cloud‑ready Docker installations. The platform targets home labs, enterprises, and developers needing flexible, scalable automation of file workflows.
image: https://fileflows.com/images/social-card-2.jpg
json_schemas:
- name: PostWebhookProcessFileRequest
  property_count: 1
  slug: fileflows-post-webhook-process-file-request
jsonld:
- class_count: 1
  name: Fileflows Context
  property_count: 1
  slug: fileflows-context
layout: provider
modified: '2026-10-28'
name: FileFlows
nav: Providers
network: true
overview: 'FileFlows is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, File Processing, Self-Hosted, and Docker.


  The FileFlows catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FileFlows'' developer surface includes documentation, pricing, getting-started guide, API reference, and 14 more developer resources.'
plans:
- name: Fileflows Plans Pricing
  plan_count: 3
  slug: fileflows-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: FileFlows API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: fileflows-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 16.5
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 6.6
  previous_composite: 32.3
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
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fileflows/fileflows-2026-11-03T131957.png
security:
- kind: domain-security
  name: Fileflows Domain Security
  slug: fileflows-domain-security
  summary_line: TLSv1.3
slug: fileflows
tags:
- Company
- Automation
- File Processing
- Self-Hosted
- Docker
- Open Source
website: https://fileflows.com/
---
