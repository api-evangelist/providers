---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sync Labs Agentic Access
  operation_count: 10
  slug: sync-labs-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- description: Official Python SDK for integrating the Sync Labs lip-sync API into Python applications. Supports Python 3.8+. Install via pip install syncsdk.
  name: Sync Labs Python SDK
  slug: sync-labs-python-sdk
- description: Official TypeScript/Node.js SDK for integrating the Sync Labs API. Supports Node.js 18+. Install via npm install @sync.so/sdk.
  name: Sync Labs TypeScript SDK
  slug: sync-labs-typescript-sdk
- baseURL: https://api.sync.so/v2
  baseurl_source: declared
  description: Uploaded asset management
  name: Sync Labs Assets API
  slug: sync-labs-assets-api
- baseURL: https://api.sync.so/v2
  baseurl_source: declared
  description: Batch processing multiple videos
  name: Sync Labs Batch API
  slug: sync-labs-batch-api
- baseURL: https://api.sync.so/v2
  baseurl_source: declared
  description: Lip-sync video generation operations
  name: Sync Labs Generate API
  slug: sync-labs-generate-api
- baseURL: https://api.sync.so/v2
  baseurl_source: declared
  description: Available AI model listing
  name: Sync Labs Models API
  slug: sync-labs-models-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sync Labs Assets API
  slug: open-sync-labs-assets-api
- collection_type: open
  name: Sync Labs Assets Batch API
  slug: open-sync-labs-batch-api
- collection_type: open
  name: Sync Labs Assets Generate API
  slug: open-sync-labs-generate-api
- collection_type: open
  name: Sync Labs Assets Models API
  slug: open-sync-labs-models-api
- collection_type: open
  name: Sync Labs API
  slug: open-sync-labs
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sync-labs-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sync-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sync-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sync-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synchronicity-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synclabs-ai
- group: company
  title: ''
  type: Website
  url: https://sync.so
- group: docs
  title: ''
  type: Documentation
  url: https://sync.so/docs/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://sync.so/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://sync.so/pricing
- group: auth
  title: ''
  type: API Keys
  url: https://sync.so/settings/api-keys
- group: start
  title: ''
  type: Signup
  url: https://sync.so/sign-up
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@sync.so
- group: other
  title: ''
  type: Y Combinator
  url: https://www.ycombinator.com/companies/sync-2
- group: agent
  title: ''
  type: LlmsText
  url: https://sync.so/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://sync.so/blog/rss.xml
created: '2026-05-03'
description: Sync Labs (sync.so) provides a suite of studio-grade AI lip-sync and visual dubbing APIs. Their technology synchronizes video lip movements with any audio track using state-of-the-art models, enabling professional video dubbing, content localization, and personalized video generation at scale. Models include sync-3, lipsync-2-pro, lipsync-2, lipsync-1.9, and react-1, with support for batch processing (up to 500 videos), webhooks, Python and TypeScript SDKs, Adobe Premiere plugin, and ComfyUI integration. Backed by Y Combinator.
examples:
- key_count: 6
  name: Sync Labs Create Generation Example
  slug: sync-labs-create-generation-example
finops:
- name: Sync Labs Finops
  service_category: AI Infrastructure / Media Generation
  slug: sync-labs-finops
image: https://sync.so/favicon.ico
json_schemas:
- name: Sync Labs Generation
  property_count: 9
  slug: sync-labs-generation
json_structures:
- name: Sync Labs Generation Structure
  property_count: 0
  slug: sync-labs-generation-structure
jsonld:
- class_count: 0
  name: Sync Labs Context
  property_count: 22
  slug: sync-labs-context
layout: provider
modified: '2026-05-19'
name: Sync Labs
nav: Providers
network: true
overview: 'Sync Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Batch API, Generate API, and 1 more. Tagged areas include Artificial Intelligence, Content Localization, Dubbing, Lip Sync, and Media.


  The Sync Labs catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sync Labs'' developer surface includes authentication, documentation, getting-started guide, pricing, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Sync Labs Plans Pricing
  plan_count: 5
  slug: sync-labs-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 7
  name: Sync Labs Rate Limits
  slug: sync-labs-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sync Labs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sync-labs-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Sync Labs API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 1
    info: 1
    warn: 5
  slug: sync-labs-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 61.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 61.7
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sync-labs/refs/heads/main/screenshots/sync-labs-2026-06-20T194835.png
security:
- kind: authentication
  name: Sync Labs Authentication
  slug: sync-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sync Labs Domain Security
  slug: sync-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sync-labs
tags:
- Artificial Intelligence
- Content Localization
- Dubbing
- Lip Sync
- Media
- Video
- Visual AI
website: https://sync.so
---
