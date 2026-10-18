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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 21
apis:
- description: Workspace API provides programmatic access to Curiosity's enterprise knowledge graph, enabling data ingestion, search, embeddings, and AI agent operations.
  name: Curiosity Workspace API
  slug: curiosity-workspace-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Admin Agent API from Curiosity — 2 operation(s) for admin agent.
  name: Curiosity Admin Agent API
  slug: curiosity-admin-agent-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Build API from Curiosity — 1 operation(s) for build.
  name: Curiosity Build API
  slug: curiosity-build-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Cce API from Curiosity — 1 operation(s) for cce.
  name: Curiosity Cce API
  slug: curiosity-cce-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Chatai API from Curiosity — 4 operation(s) for chatai.
  name: Curiosity Chatai API
  slug: curiosity-chatai-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Code API from Curiosity — 1 operation(s) for code.
  name: Curiosity Code API
  slug: curiosity-code-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Config API from Curiosity — 1 operation(s) for config.
  name: Curiosity Config API
  slug: curiosity-config-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Curiosity API API from Curiosity — 1 operation(s) for curiosity api.
  name: Curiosity Curiosity API
  slug: curiosity-curiosity-api-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Embeddings API from Curiosity — 1 operation(s) for embeddings.
  name: Curiosity Embeddings API
  slug: curiosity-embeddings-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Endpoints API from Curiosity — 4 operation(s) for endpoints.
  name: Curiosity Endpoints API
  slug: curiosity-endpoints-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Graph API from Curiosity — 3 operation(s) for graph.
  name: Curiosity Graph API
  slug: curiosity-graph-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Groups API from Curiosity — 4 operation(s) for groups.
  name: Curiosity Groups API
  slug: curiosity-groups-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Install API from Curiosity — 1 operation(s) for install.
  name: Curiosity Install API
  slug: curiosity-install-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Login API from Curiosity — 3 operation(s) for login.
  name: Curiosity Login API
  slug: curiosity-login-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Messages API from Curiosity — 2 operation(s) for messages.
  name: Curiosity Messages API
  slug: curiosity-messages-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Migrations API from Curiosity — 1 operation(s) for migrations.
  name: Curiosity Migrations API
  slug: curiosity-migrations-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Models API from Curiosity — 3 operation(s) for models.
  name: Curiosity Models API
  slug: curiosity-models-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Node API from Curiosity — 5 operation(s) for node.
  name: Curiosity Node API
  slug: curiosity-node-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Saml API from Curiosity — 2 operation(s) for saml.
  name: Curiosity SAML API
  slug: curiosity-saml-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Search API from Curiosity — 3 operation(s) for search.
  name: Curiosity Search API
  slug: curiosity-search-api
- baseURL: https://<your-workspace-host>/api
  baseurl_source: declared
  description: The Chat Completions API from Curiosity — 1 operation(s) for chat completions.
  name: Curiosity Chat Completions API
  slug: curiosity-chat-completions-api
artifact_total: 33
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/plans/curiosity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/curiosity-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/rules/curiosity-rules.yml
  title: ''
  type: Spectral
  url: rules/curiosity-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/json-ld/curiosity-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/curiosity-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/vocabulary/curiosity-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/curiosity-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/data-model/curiosity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/curiosity-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/cli/curiosity-cli.yml
  title: ''
  type: CLI
  url: cli/curiosity-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.curiosity.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/authentication/curiosity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/curiosity-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/lifecycle/curiosity-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/curiosity-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/lifecycle/curiosity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/curiosity-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/conformance/curiosity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/curiosity-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/llms/curiosity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/curiosity-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/hosts/curiosity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curiosity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/vendors/curiosity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curiosity-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/packages/curiosity-packages.yml
  title: ''
  type: SDKs
  url: packages/curiosity-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/packages/curiosity-packages.yml
  title: ''
  type: Packages
  url: packages/curiosity-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.curiosity.ai/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.curiosity.ai/workspace/getting-started/build-your-first-enterprise-ai-app
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/security/curiosity-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/curiosity-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curiosity/refs/heads/main/security/curiosity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curiosity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curiosity.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.curiosity.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://curiosity.ai/developers/
- group: company
  title: ''
  type: Blog
  url: https://blog.curiosity.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://curiosity.ai/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.curiosity.ai/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found on the documented API host despite accessible documentation.
  evidence:
  - status: 200
    url: https://docs.curiosity.ai/workspace-api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curiosity provides an AI‑powered enterprise knowledge graph platform that lets organizations connect, enrich, and query their data across systems. Built for on‑premises or private‑cloud deployment, Curiosity Studio enables users to build custom AI‑driven tools, search, embeddings, and agents while keeping data within their own infrastructure. The platform supports a REST API, SDKs for C# and Python, and extensive developer documentation covering data ingestion, security, and extensibility.
image: https://curiosity.ai/assets/social/home.png
json_schemas:
- name: PostApiEmbeddingsEmbeddingidRequest
  property_count: 3
  slug: curiosity-post-api-embeddings-embeddingid-request
- name: PostApiLoginPasswordPasswordidRequest
  property_count: 2
  slug: curiosity-post-api-login-password-passwordid-request
- name: PostChatCompletionsRequest
  property_count: 3
  slug: curiosity-post-chat-completions-request
- name: PostV1MessagesRequest
  property_count: 4
  slug: curiosity-post-v1-messages-request
- name: PutApiSearchSettingsLlmRequest
  property_count: 2
  slug: curiosity-put-api-search-settings-llm-request
- name: PutApiSearchSynonymsForRequest
  property_count: 3
  slug: curiosity-put-api-search-synonyms-for-request
jsonld:
- class_count: 11
  name: Curiosity Context
  property_count: 21
  slug: curiosity-context
layout: provider
modified: '2026-10-12'
name: Curiosity
nav: Providers
network: true
overview: 'Curiosity is listed with 21 APIs on the [APIs.io](https://apis.io/) network, including Admin Agent API, Build API, Cce API, and 18 more. Tagged areas include Artificial Intelligence, Knowledge-Graph, Enterprise, Data-Integration, and On-Premises.


  The Curiosity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Curiosity''s developer surface includes CLI, authentication, changelog, getting-started guide, documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Curiosity Plans Pricing
  plan_count: 2
  slug: curiosity-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Curiosity API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: curiosity-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 68.0
    catalog_earned_first_party: 8.0
    catalog_gap: 47.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 24.8
    developer_ergonomics: 64.3
    discoverability: 69.6
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 21
      marker_coverage: 100.0
      total: 21
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Curiosity Authentication
  slug: curiosity-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Curiosity Domain Security
  slug: curiosity-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Curiosity Trust Center
  slug: curiosity-trust-center
  summary_line: SOC 2, ISO 27001
slug: curiosity
tags:
- Artificial Intelligence
- Knowledge-Graph
- Enterprise
- Data-Integration
- On-Premises
- Company
website: https://curiosity.ai
---
