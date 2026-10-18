---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: verified
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 78
  human_in_the_loop: 7
  name: Tale Dev Agentic Access
  operation_count: 143
  slug: tale-dev-agentic-access
  summary_line: 143 operations · 78 acting · 7 human-in-the-loop
api_count: 2
apis:
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Agents belonging to one project.
  name: Tale Agents API
  slug: tale-dev-agents-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: 'Versioned automations, their runs and triggers — list, read, install, bind, run, cancel and delete. Authoring (save, validate, test, deploy) is not on this surface: it lives on `POST /api/v1/mcp` (`sa'
  name: Tale Automations API
  slug: tale-dev-automations-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: The warmed browser-session pool behind video-link ingestion.
  name: Tale Browser sessions API
  slug: tale-dev-browser-sessions-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Contact records.
  name: Tale Contacts API
  slug: tale-dev-contacts-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Mirroring external conversations into Inbox — versioned snapshots, reply claims, delivery receipts and staged uploads.
  name: Tale Conversations API
  slug: tale-dev-conversations-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Documents in the knowledge base.
  name: Tale Documents API
  slug: tale-dev-documents-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Knowledge entries and semantic search.
  name: Tale Knowledge API
  slug: tale-dev-knowledge-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: The platform MCP endpoint (JSON-RPC over HTTP).
  name: Tale MCP API
  slug: tale-dev-mcp-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: The organization’s approved models over two vendor wires — OpenAI Chat Completions under `/api/v1/openai` and Anthropic Messages under `/api/v1/anthropic` — for the OpenAI and Anthropic SDKs, opencode
  name: Tale Model endpoints API
  slug: tale-dev-model-endpoints-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Read-only, recipient-scoped notification exports for connected applications.
  name: Tale Notifications API
  slug: tale-dev-notifications-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: The key holder and the organizations it may act in — where a multi-organization client learns the slug to send.
  name: Tale Organization API
  slug: tale-dev-organization-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Product catalog entries.
  name: Tale Products API
  slug: tale-dev-products-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Projects, their folders, and their files — the machine door for external systems that mirror client work into the platform. Multi-org keys must send X-Organization-Slug on every call.
  name: Tale Projects API
  slug: tale-dev-projects-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Durable automation runs.
  name: Tale Runs API
  slug: tale-dev-runs-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: The organization’s skills.
  name: Tale Skills API
  slug: tale-dev-skills-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Tasks on the project boards — the machine door for external workers that materialize items as tasks, start their workflows, and report back. Multi-org keys must send X-Organization-Slug on every call.
  name: Tale Tasks API
  slug: tale-dev-tasks-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Chat threads of the key holder.
  name: Tale Threads API
  slug: tale-dev-threads-api
- baseURL: https://your-host.example.com/api/v1
  baseurl_source: declared
  description: Crawled website sources.
  name: Tale Websites API
  slug: tale-dev-websites-api
artifact_total: 32
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/agentic-access/tale-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tale-dev-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/rate-limits/tale-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tale-dev-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/plans/tale-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tale-dev-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/rules/tale-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/tale-dev-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/json-ld/tale-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tale-dev-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/vocabulary/tale-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tale-dev-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/data-model/tale-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tale-dev-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/conventions/tale-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tale-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/conventions/tale-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tale-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/errors/tale-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tale-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/conformance/tale-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tale-dev-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/llms/tale-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tale-dev-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/mcp/tale-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tale-dev-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/mcp/tale-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tale-dev-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/hosts/tale-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tale-dev-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/vendors/tale-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tale-dev-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/authentication/tale-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tale-dev-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/security/tale-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tale-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tale.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tale.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tale.dev/develop/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tale.dev/get-started/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://tale.dev/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://tale.dev/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tale.dev/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tale.dev/legal/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tale-project
- group: design
  title: ''
  type: Webhooks
  url: https://docs.tale.dev/develop/webhooks
created: '2026-10-09'
description: Tale is an open-source (MIT) AI platform from Ruler GmbH (Spiez, Switzerland) for knowledge, chat, agents, skills and automations, self-hosted or run as Tale Enterprise in CH/EU clouds. Each deployment exposes the Tale Platform API (REST under /api/v1 with Bearer organization API keys), an MCP endpoint at /api/v1/mcp with 22 documented tools, webhook triggers and OpenAI/Anthropic-compatible model endpoints.
image: https://tale.dev/og.png
json_schemas:
- name: Document
  property_count: 16
  slug: tale-dev-document
- name: Me
  property_count: 5
  slug: tale-dev-me
- name: Message
  property_count: 13
  slug: tale-dev-message
- name: RunProjection
  property_count: 25
  slug: tale-dev-run-projection
- name: Run
  property_count: 25
  slug: tale-dev-run
- name: RunSummary
  property_count: 23
  slug: tale-dev-run-summary
jsonld:
- class_count: 68
  name: Tale Dev Context
  property_count: 260
  slug: tale-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at your-host.example.com requiring an API key; 22 tools listed.
  name: Tale Platform MCP Endpoint
  slug: tale-platform-mcp-endpoint
modified: '2026-10-09'
name: Tale
nav: Providers
network: true
overview: 'Tale publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Automations API, Browser sessions API, and 15 more. Tagged areas include Company, Artificial Intelligence, Agents, Automation, and Knowledge Management.


  The Tale catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tale''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, and 23 more developer resources.'
plans:
- name: Tale Dev Plans Pricing
  plan_count: 2
  slug: tale-dev-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 6
  name: Tale Dev Rate Limits
  slug: tale-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Tale API Rules
  rule_count: 19
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 2
  slug: tale-dev-rules
score:
  band: strong
  composite: 61.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.4
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 64.2
    developer_ergonomics: 42.3
    discoverability: 68.3
    operational_transparency: 60.5
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 88.9
screenshot: https://raw.githubusercontent.com/api-evangelist/tale-dev/refs/heads/main/screenshots/tale-dev-2026-10-11T130636.png
security:
- kind: authentication
  name: Tale Dev Authentication
  slug: tale-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tale Dev Domain Security
  slug: tale-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tale-dev
tags:
- Company
- Artificial Intelligence
- Agents
- Automation
- Knowledge Management
- MCP
- Open Source
- Self-Hosted
website: https://tale.dev
---
