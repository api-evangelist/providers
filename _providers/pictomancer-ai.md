---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: 'REST API for image transformation: get_format_info, estimate_cost, analyze_image, resize_image, compress_image, convert_image, crop_image, optimize_for_vision, optimize_generated_image and image_pipel'
  name: Pictomancer.ai Image API
  slug: pictomancer-ai-image-api
- description: Official hosted Model Context Protocol server at https://api.pictomancer.ai/mcp (Streamable HTTP, protocol revision 2025-06-18, no authentication required, 120 requests/minute). Anonymous tools/list r
  name: Pictomancer.ai MCP Server
  slug: pictomancer-ai-mcp-server
- description: Agent-to-Agent endpoint at https://api.pictomancer.ai/a2a (JSON-RPC) described by a published agent card — canonical /.well-known/agent-card.json on api.pictomancer.ai (protocolVersion 0.3, graded con
  name: Pictomancer.ai A2A Agent
  slug: pictomancer-ai-a2a-agent
artifact_total: 10
asyncapis:
- description: ''
  name: Pictomancer Ai Webhooks
  slug: pictomancer-ai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://pictomancer.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.pictomancer.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.pictomancer.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.pictomancer.ai/
- group: start
  title: ''
  type: Login
  url: https://app.pictomancer.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.pictomancer.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://pictomancer.ai/#pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/plans/pictomancer-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pictomancer-ai-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://pictomancer.ai/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/changelog/pictomancer-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pictomancer-ai-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://pictomancer.ai/status
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/lifecycle/pictomancer-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pictomancer-ai-lifecycle.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pictomancer.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pictomancer.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pictomancer
- group: agent
  title: ''
  type: LLMsTxt
  url: https://pictomancer.ai/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/llms/pictomancer-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pictomancer-ai-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/packages/pictomancer-ai-packages.yml
  title: ''
  type: Packages
  url: packages/pictomancer-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/packages/pictomancer-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/pictomancer-ai-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/well-known/pictomancer-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pictomancer-ai-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/conformance/pictomancer-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pictomancer-ai-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/security/pictomancer-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pictomancer-ai-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pictomancer-ai/refs/heads/main/regulatory/pictomancer-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/pictomancer-ai-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://pictomancer.ai/privacy
created: '2026-09-19'
description: 'Pictomancer.ai is a Spain-registered image-optimization API built for agents: resize, compress, convert, crop, optimize-for-vision and one-call optimization of AI-generated images, processed in under 50 ms and priced per request ($0.001-$0.03, analyze free). The same ten operations are published three ways — an OpenAPI 3.1 REST API, a hosted MCP server (Streamable HTTP, listed in the official MCP Registry) and an A2A agent card — and are paid for anonymously with USDC on Base via x402 (HTTP 402 -> pay -> retry), with an API key, or free for the first 50 requests per identity. Results return inline, PUT to the caller''s own bucket, or POST to a callback endpoint. First-party SDKs ship for Python, Node, PHP and Go plus an n8n node and a WordPress plugin.'
image: https://pictomancer.ai/apple-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Pictomancer.ai
  slug: pictomancerai
- description: ''
  name: Pictomancer.ai MCP Server
  slug: pictomancerai-mcp-server
modified: '2026-09-19'
name: Pictomancer.ai
nav: Providers
network: true
overview: 'Pictomancer.ai publishes 1 API on the [APIs.io](https://apis.io/) network: Image API. Tagged areas include Company, Image, Image Optimization, Image Processing, and Media.


  The Pictomancer.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pictomancer.ai''s developer surface includes documentation, API reference, signup flow, pricing, changelog, and 19 more developer resources.'
plans:
- name: Pictomancer Ai Plans Pricing
  plan_count: 5
  slug: pictomancer-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Pictomancer Ai Rate Limits
  slug: pictomancer-ai-rate-limits
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 33.9
    discoverability: 75.9
    operational_transparency: 63.2
  previous_composite: 48.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Pictomancer Ai Authentication
  slug: pictomancer-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Pictomancer Ai Domain Security
  slug: pictomancer-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: pictomancer-ai
tags:
- Company
- Image
- Image Optimization
- Image Processing
- Media
- Agents
- MCP
- A2A
- x402
- Micropayments
- Developer Tools
website: https://pictomancer.ai/
---
