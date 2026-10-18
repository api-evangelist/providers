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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
api_count: 5
apis:
- baseURL: https://proxy-instance.float16.cloud
  baseurl_source: declared
  description: The Chat API from Float16 — 3 operation(s) for chat.
  name: Float16 Chat API
  slug: float16-chat-api
- baseURL: https://proxy-instance.float16.cloud
  baseurl_source: declared
  description: The Fact API from Float16 — 1 operation(s) for fact.
  name: Float16 Fact API
  slug: float16-fact-api
- baseURL: https://proxy-instance.float16.cloud
  baseurl_source: declared
  description: The Float16 API API from Float16 — 1 operation(s) for float16 api.
  name: Float16 Float16 API
  slug: float16-float16-api-api
- baseURL: https://proxy-instance.float16.cloud
  baseurl_source: declared
  description: The Ocr API from Float16 — 1 operation(s) for ocr.
  name: Float16 Ocr API
  slug: float16-ocr-api
- baseURL: https://proxy-instance.float16.cloud
  baseurl_source: declared
  description: The Task API from Float16 — 2 operation(s) for task.
  name: Float16 Task API
  slug: float16-task-api
artifact_total: 16
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/plans/float16-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/float16-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/rules/float16-rules.yml
  title: ''
  type: Spectral
  url: rules/float16-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/json-ld/float16-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/float16-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/vocabulary/float16-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/float16-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/data-model/float16-data-model.yml
  title: ''
  type: DataModel
  url: data-model/float16-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://float16.cloud/security/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/conformance/float16-conformance.yml
  title: ''
  type: Conformance
  url: conformance/float16-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/llms/float16-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/float16-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/well-known/float16-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/float16-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/hosts/float16-hosts.yml
  title: ''
  type: Hosts
  url: hosts/float16-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/vendors/float16-vendors.yml
  title: ''
  type: Vendors
  url: vendors/float16-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.float16.cloud/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://float16.cloud/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/float16
- group: docs
  title: ''
  type: APIReference
  url: https://float16.cloud/en-en/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.float16.cloud/getting-started/introduction
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/security/float16-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/float16-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/float16/refs/heads/main/security/float16-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/float16-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://float16.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://float16.cloud/en-en/docs
- group: company
  title: ''
  type: Blog
  url: https://float16.cloud/en-en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vultureprime.com/privacy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://float16.cloud/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Float16 provides a cloud‑based platform that simplifies high‑performance numeric computing by offering APIs for fast, low‑precision floating‑point operations. The service targets developers building AI, graphics, and scientific applications that can benefit from reduced memory bandwidth and accelerated throughput. Float16’s offering includes SDKs, detailed documentation, and support for multiple programming languages, enabling seamless integration into existing workflows. By focusing on the niche of half‑precision computation, Float16 helps lower infrastructure costs while maintaining acceptable accuracy for many modern workloads.
json_schemas:
- name: GetInstanceidIdV1Response
  property_count: 2
  slug: float16-get-instanceid-id-v1-response
- name: PostInstanceidIdV1ChatCompletionsRequest
  property_count: 2
  slug: float16-post-instanceid-id-v1-chat-completions-request
- name: PostInstanceidIdV1ChatCompletionsResponse
  property_count: 2
  slug: float16-post-instanceid-id-v1-chat-completions-response
- name: PostTaskRunServerX7X2Dfl8ZuChatRequest
  property_count: 1
  slug: float16-post-task-run-server-x7-x2-dfl8-zu-chat-request
- name: PostV1ChatCompletionsRequest
  property_count: 4
  slug: float16-post-v1-chat-completions-request
- name: PostV1ChatRequest
  property_count: 2
  slug: float16-post-v1-chat-request
jsonld:
- class_count: 7
  name: Float16 Context
  property_count: 5
  slug: float16-context
layout: provider
modified: '2026-10-16'
name: Float16
nav: Providers
network: true
overview: 'Float16 is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Fact API, Float16 API, and 2 more. Tagged areas include Company, Cloud, High Performance Computing, and Artificial Intelligence.


  The Float16 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Float16''s developer surface includes API reference, getting-started guide, documentation, engineering blog, and 18 more developer resources.'
plans:
- name: Float16 Plans Pricing
  plan_count: 4
  slug: float16-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Float16 API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: float16-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 23.7
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
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
  name: Float16 Domain Security
  slug: float16-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Float16 Trust Center
  slug: float16-trust-center
  summary_line: SOC 2, PCI DSS
slug: float16
tags:
- Company
- Cloud
- High Performance Computing
- Artificial Intelligence
website: https://float16.cloud/
---
