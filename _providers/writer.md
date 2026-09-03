---
access_model:
  confidence: high
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Writer Agentic Access
  operation_count: 30
  slug: writer-agentic-access
  summary_line: 30 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.writer.com/v1
  baseurl_source: declared
  description: The File API API from Writer — 4 operation(s) for file api.
  name: Writer File API API
  slug: writer-file-api-api
- baseURL: https://api.writer.com/v1
  baseurl_source: declared
  description: The Generation API API from Writer — 5 operation(s) for generation api.
  name: Writer Generation API API
  slug: writer-generation-api-api
- baseURL: https://api.writer.com/v1
  baseurl_source: declared
  description: The KG API API from Writer — 5 operation(s) for kg api.
  name: Writer KG API API
  slug: writer-kg-api-api
- baseURL: https://api.writer.com/v1
  baseurl_source: declared
  description: The template API from Writer — 4 operation(s) for template.
  name: Writer template API
  slug: writer-template-api
- baseURL: https://api.writer.com/v1
  baseurl_source: declared
  description: The Tools API API from Writer — 2 operation(s) for tools api.
  name: Writer Tools API API
  slug: writer-tools-api-api
- baseURL: https://api.writer.com/v1
  baseurl_source: declared
  description: The Translation API from Writer — 1 operation(s) for translation.
  name: Writer Translation API
  slug: writer-translation-api
- baseURL: https://api.writer.com/v1
  baseurl_source: declared
  description: The Vision API from Writer — 1 operation(s) for vision.
  name: Writer Vision API
  slug: writer-vision-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: File API API
  slug: open-writer-file-api-api
- collection_type: open
  name: File API Generation API API
  slug: open-writer-generation-api-api
- collection_type: open
  name: File API KG API API
  slug: open-writer-kg-api-api
- collection_type: open
  name: File API template API
  slug: open-writer-template-api
- collection_type: open
  name: File API Tools API API
  slug: open-writer-tools-api-api
- collection_type: open
  name: File API Translation API
  slug: open-writer-translation-api
- collection_type: open
  name: File API Vision API
  slug: open-writer-vision-api
- collection_type: open
  name: API
  slug: open-writer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/writer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/writer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/writer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/writer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getwriter
- group: company
  title: ''
  type: Website
  url: https://writer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.writer.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/writer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/writer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/writer-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://api.writer.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://writer.com/blog/feed/
created: '2026-05-08'
description: Writer is a generative AI platform purpose-built for the enterprise. The Writer AI Studio Platform API exposes the proprietary Palmyra family of LLMs, knowledge-graph retrieval, no-code Application invocation, tool calling, vision, translation, and content guardrails for enterprise content, summarization, and process-automation workflows.
finops:
- name: Writer Finops
  service_category: AI and Machine Learning
  slug: writer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/writer.png
layout: provider
modified: '2026-05-19'
name: Writer
nav: Providers
network: true
overview: 'Writer publishes 7 APIs on the [APIs.io](https://apis.io/) network, including File API API, Generation API API, KG API API, and 4 more. Tagged areas include Artificial Intelligence, LLM, Enterprise, Content Generation, and Palmyra.


  Writer''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Writer Plans Pricing
  plan_count: 3
  slug: writer-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Writer Rate Limits
  slug: writer-rate-limits
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 52.9
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/writer/refs/heads/main/screenshots/writer-2026-06-20T201632.png
security:
- kind: authentication
  name: Writer Authentication
  slug: writer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Writer Domain Security
  slug: writer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: writer
tags:
- Artificial Intelligence
- LLM
- Enterprise
- Content Generation
- Palmyra
- Agents
website: https://writer.com/
---
