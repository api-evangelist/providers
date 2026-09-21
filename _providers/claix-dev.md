---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-09-20'
api_count: 1
apis:
- baseURL: https://claix.dev/api
  baseurl_source: declared
  description: 'REST API (Claix API 1.8.2) with 20 operations: six schema-driven conversions (Excel/CSV, PDF, Word/text, image and raw text to JSON; JSON to Excel), five Agent-mode variants that add a reasoning layer'
  name: Claix Document Intelligence API
  slug: claix-document-intelligence-api
- description: Hosted, remote Model Context Protocol server (Streamable HTTP and legacy SSE) exposing the REST contract as dot-named tools - claix.schemas.*, claix.extract.*, claix.agent.*, claix.convert.json_to_exc
  name: Claix MCP Server
  slug: claix-mcp-server
- description: Native Agent-to-Agent (A2A 0.3) JSON-RPC agent at /a2a with a public agent card at /.well-known/agent-card.json declaring 20 skills, each bound by the provider to its OpenAPI operation. message/send w
  name: Claix A2A Agent
  slug: claix-a2a-agent
artifact_total: 9
asyncapis:
- description: ''
  name: Claix Dev Webhooks
  slug: claix-dev-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/security/claix-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claix-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.claix.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.claix.dev/documentation/excel-to-json
- group: docs
  title: ''
  type: APIReference
  url: https://www.claix.dev/documentation/excel-to-json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.claix.dev/documentation/sdks
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.claix.dev/dashboard
- group: start
  title: ''
  type: SignUp
  url: https://www.claix.dev/register
- group: start
  title: ''
  type: Login
  url: https://www.claix.dev/login
- group: company
  title: ''
  type: Blog
  url: https://www.claix.dev/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claix.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claix.dev/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/llms/claix-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claix-dev-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/well-known/claix-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claix-dev-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/packages/claix-dev-packages.yml
  title: ''
  type: Packages
  url: packages/claix-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/packages/claix-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/claix-dev-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/conformance/claix-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claix-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/lifecycle/claix-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/claix-dev-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/components/claix-dev-components.yml
  title: ''
  type: Components
  url: components/claix-dev-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/claix-dev/refs/heads/main/regulatory/claix-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/claix-dev-regulatory-posture.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://www.claix.dev/dpa
- group: operate
  title: ''
  type: IncidentNotification
  url: https://www.claix.dev/dpa
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.claix.dev/privacy
created: '2026-09-19'
description: 'Claix is a Madrid-based B2B document intelligence API that converts PDFs, Excel/CSV, Word and text documents and images into strictly typed JSON against customer-defined schemas, keeps extracted documents as queryable context for AI agents (single-document and knowledge-space Q&A with deterministic nulls), and exposes one 20-operation contract three ways: REST (OpenAPI 3.0.3), a hosted MCP server at /mcp, and a native A2A agent at /a2a with a published, conformant agent card. Pay-as-you-go in euros after 100 free calls, with a free BYOK mode; official Python SDK and n8n node.'
image: https://www.claix.dev/claix-logo.png
layout: provider
mcp_servers:
- description: 'Claix ships a hosted, remote MCP server on its own domain. The documented URL is https://claix.dev/mcp; the apex answers 308 to https://www.claix.dev/mcp, which is the URL an MCP client actually ends '
  name: Claix MCP Server
  slug: claix-mcp-server
modified: '2026-09-19'
name: Claix
nav: Providers
network: true
overview: 'Claix publishes 1 API on the [APIs.io](https://apis.io/) network: Document Intelligence API. Tagged areas include Document Processing, Data Extraction, Document Intelligence, PDF, and Excel.


  The Claix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Claix''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, and 18 more developer resources.'
plans:
- name: Claix Dev Plans Pricing
  plan_count: 2
  slug: claix-dev-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Claix Dev Rate Limits
  slug: claix-dev-rate-limits
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 49.1
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 63.0
    developer_ergonomics: 61.3
    discoverability: 75.9
    operational_transparency: 28.9
  previous_composite: 2.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Claix Dev Authentication
  slug: claix-dev-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Claix Dev Domain Security
  slug: claix-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: claix-dev
tags:
- Document Processing
- Data Extraction
- Document Intelligence
- PDF
- Excel
- OCR
- Structured Data
- AI Agents
- MCP
- A2A
- Spain
- Company
website: https://www.claix.dev/
---
