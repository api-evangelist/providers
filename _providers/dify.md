---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - pricing
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 50
  human_in_the_loop: 3
  name: Dify Agentic Access
  operation_count: 82
  slug: dify-agentic-access
  summary_line: 82 operations · 50 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Dify is an open-source platform for building AI applications, combining Backend-as-a-Service and LLMOps. Every app published in Dify doubles as a REST API, and so does every knowledge base. The Dify S
  name: Dify
  slug: dify
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to chat messages and interactions. 3 operation(s) from the Dify Service API.
  name: Dify Chat Messages API
  slug: dify-chat-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to text generation and completion. 2 operation(s) from the Dify Service API.
  name: Dify Completion Messages API
  slug: dify-completion-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to managing conversations. 6 operation(s) from the Dify Service API.
  name: Dify Conversations API
  slug: dify-conversations-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing knowledge bases, including creation, configuration, and retrieval. 6 operation(s) from the Dify Service API.
  name: Dify Knowledge Bases API
  slug: dify-datasets-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: File upload and preview operations. 2 operation(s) from the Dify Service API.
  name: Dify Files API
  slug: dify-files-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for executing and managing workflows. 6 operation(s) from the Dify Service API.
  name: Dify Workflow Runs API
  slug: dify-workflows-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations to retrieve application settings and information. 4 operation(s) from the Dify Service API.
  name: Dify Applications API
  slug: dify-applications-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to managing annotations for direct replies. 6 operation(s) from the Dify Service API.
  name: Dify Annotations API
  slug: dify-annotations-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Text-to-Speech and Speech-to-Text operations. 2 operation(s) from the Dify Service API.
  name: Dify Audio API
  slug: dify-audio-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: User feedback operations. 2 operation(s) from the Dify Service API.
  name: Dify Feedback API
  slug: dify-feedback-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to end user information. 1 operation(s) from the Dify Service API.
  name: Dify End Users API
  slug: dify-end-users-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Endpoints for resuming paused workflows that require human input. 2 operation(s) from the Dify Service API.
  name: Dify Human Input API
  slug: dify-human-input-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for creating, updating, and managing documents within a knowledge base. 12 operation(s) from the Dify Service API.
  name: Dify Documents API
  slug: dify-documents-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing document chunks and child chunks. 9 operation(s) from the Dify Service API.
  name: Dify Chunks API
  slug: dify-chunks-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing knowledge base tags and tag bindings. 7 operation(s) from the Dify Service API.
  name: Dify Knowledge Tags API
  slug: dify-tags-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing knowledge base metadata fields and document metadata values. 7 operation(s) from the Dify Service API.
  name: Dify Metadata API
  slug: dify-metadata-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for retrieving available models. 1 operation(s) from the Dify Service API.
  name: Dify Models API
  slug: dify-models-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing and running knowledge pipelines, including datasource plugins and pipeline execution. 4 operation(s) from the Dify Service API.
  name: Dify Knowledge Pipeline API
  slug: dify-knowledge-pipeline-api
artifact_total: 37
asyncapis:
- description: ''
  name: Dify Events
  slug: dify-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dify Chat API
  slug: open-dify-chat-api
- collection_type: open
  name: Dify Chat Completion API
  slug: open-dify-completion-api
- collection_type: open
  name: Dify Chat Conversations API
  slug: open-dify-conversations-api
- collection_type: open
  name: Dify Chat Datasets API
  slug: open-dify-datasets-api
- collection_type: open
  name: Dify Chat Files API
  slug: open-dify-files-api
- collection_type: open
  name: Dify Chat Workflows API
  slug: open-dify-workflows-api
- collection_type: open
  name: Dify API
  slug: open-dify
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/dify-service-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/dify-service-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dify-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dify-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dify-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dify-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dify-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dify-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dify.ai/
- group: design
  title: ''
  type: Conformance
  url: conformance/dify-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/dify-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dify-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/dify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dify-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/dify-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dify-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dify-cli.yml
- group: design
  title: ''
  type: Components
  url: components/dify-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dify-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dify-finops.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dify-events.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dify-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dify-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/dify-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dify-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dify-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dify-llms.txt
- group: company
  title: ''
  type: Website
  url: https://dify.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dify.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dify.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dify.ai/en/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dify.ai/en/api-reference/guides/get-started
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dify.ai/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://dify.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.dify.ai/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.dify.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dify.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dify.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/FngNHpbcY7
- group: operate
  title: ''
  type: Community
  url: https://github.com/langgenius/dify/discussions
- group: company
  title: ''
  type: Blog
  url: https://dify.ai/blog
- group: operate
  title: ''
  type: RoadMap
  url: https://roadmap.dify.ai/roadmap
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.dify.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/langgenius
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/langgenius
- group: company
  title: ''
  type: Twitter
  url: https://x.com/dify_ai
created: '2025-02-08'
description: Dify is an open-source platform for building AI applications, combining Backend-as-a-Service and LLMOps to streamline the development of generative AI solutions for developers and non-technical innovators alike. Teams build agentic workflows, chatflows, agents and RAG knowledge pipelines on a visual canvas, then publish each one as a web app, an embeddable widget, a REST API or an MCP server. Dify is operated by Langgenius, Inc. and ships as Dify Cloud, a self-hosted Community Edition and a commercial Enterprise edition.
finops:
- name: Dify Finops
  service_category: API
  slug: dify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dify.png
layout: provider
mcp_servers:
- description: Dify's MCP posture has two distinct surfaces. (1) A live, anonymous, remote documentation MCP server at https://docs.dify.ai/mcp, confirmed by an unauthenticated tools/list call that returned three re
  name: Dify Docs MCP
  slug: dify-docs-mcp
modified: '2026-09-06'
name: Dify
nav: Providers
network: true
overview: 'Dify publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Dify, Chat Messages API, Completion Messages API, and 16 more. Tagged areas include Artificial Intelligence, LLMOps, Backend-as-a-Service, Agents, and Workflows.


  The Dify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dify''s developer surface includes authentication, changelog, CLI, sandbox, documentation, API reference, getting-started guide, and 43 more developer resources.'
plans:
- name: Dify Plans Pricing
  plan_count: 5
  slug: dify-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Dify Rate Limits
  slug: dify-rate-limits
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 24.5
    developer_ergonomics: 85.7
    discoverability: 75.9
    operational_transparency: 89.5
  previous_composite: 64.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 18
      marker_coverage: 94.7
      total: 19
    mcp: first-party
    skills: unknown
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/dify/refs/heads/main/screenshots/dify-2026-06-20T180051.png
security:
- kind: authentication
  name: Dify Authentication
  slug: dify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dify Domain Security
  slug: dify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dify Vulnerability Disclosure
  slug: dify-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Dify Trust Center
  slug: dify-trust-center
  summary_line: SOC 2
slug: dify
tags:
- Artificial Intelligence
- LLMOps
- Backend-as-a-Service
- Agents
- Workflows
- Knowledge Management
- RAG
- Model Context Protocol
- Low Code
- Open Source
website: https://dify.ai/
---
