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
api_count: 3
apis:
- description: The Axflow platform provides AI tooling and workflow APIs as documented.
  name: Axflow API
  slug: axflow-api-2
- description: The Chat API from Axflow — 1 operation(s) for chat.
  name: Axflow Chat API
  slug: axflow-chat-api
- description: The Openai API from Axflow — 1 operation(s) for openai.
  name: Axflow Openai API
  slug: axflow-openai-api
artifact_total: 10
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/rules/axflow-rules.yml
  title: ''
  type: Spectral
  url: rules/axflow-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/json-ld/axflow-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/axflow-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/vocabulary/axflow-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/axflow-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/data-model/axflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/axflow-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/conformance/axflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axflow-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/hosts/axflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axflow-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/vendors/axflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axflow-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/packages/axflow-packages.yml
  title: ''
  type: SDKs
  url: packages/axflow-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/packages/axflow-packages.yml
  title: ''
  type: Packages
  url: packages/axflow-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axflow
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axflow/refs/heads/main/security/axflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axflow.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://studio.axflow.dev
- group: docs
  title: ''
  type: Documentation
  url: https://studio.axflow.dev
- group: company
  title: ''
  type: Blog
  url: https://axflow.dev/blog/
- group: start
  title: ''
  type: SignUp
  url: https://studio.axflow.dev
coverage:
  checked: '2026-10-16'
  detail: Documentation site renders via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.axflow.dev/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Axflow provides AI tooling for the future, offering a platform that integrates large language models, agents, and AI-driven workflows. The service focuses on enabling developers and enterprises to build, deploy, and manage AI-powered applications with ease, featuring customizable pipelines, tool integrations, and collaborative features.
image: https://axflow.dev/OG.png
json_schemas:
- name: PostApiChatRequest
  property_count: 1
  slug: axflow-post-api-chat-request
- name: PostApiChatResponse
  property_count: 1
  slug: axflow-post-api-chat-response
- name: PostApiOpenaiChatRequest
  property_count: 1
  slug: axflow-post-api-openai-chat-request
- name: PostApiOpenaiChatResponse
  property_count: 1
  slug: axflow-post-api-openai-chat-response
jsonld:
- class_count: 4
  name: Axflow Context
  property_count: 3
  slug: axflow-context
layout: provider
modified: '2026-10-16'
name: Axflow
nav: Providers
network: true
overview: 'Axflow is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Openai API, and 1 more. Tagged areas include Company, Artificial Intelligence, Tooling, Platform, and LLM.


  The Axflow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Axflow''s developer surface includes documentation, engineering blog, signup flow, and 13 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Axflow API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: axflow-rules
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 19.4
    developer_ergonomics: 28.6
    discoverability: 62.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Axflow Domain Security
  slug: axflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axflow
tags:
- Company
- Artificial Intelligence
- Tooling
- Platform
- LLM
website: https://axflow.dev/
---
