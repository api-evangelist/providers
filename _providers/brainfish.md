---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Brainfish Agentic Access
  operation_count: 27
  slug: brainfish-agentic-access
  summary_line: 27 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.brainfi.sh
  baseurl_source: declared
  description: AI agent operations for answer generation and streaming
  name: Brainfish Agents API
  slug: brainfish-agents-api
- baseURL: https://api.brainfi.sh
  baseurl_source: declared
  description: Conversation thread analytics with filtering and pagination
  name: Brainfish Analytics API
  slug: brainfish-analytics-api
- baseURL: https://api.brainfi.sh
  baseurl_source: declared
  description: Authentication and token validation operations
  name: Brainfish Authentication API
  slug: brainfish-authentication-api
- baseURL: https://api.brainfi.sh
  baseurl_source: declared
  description: Catalog management operations. Create catalogs and sync content programmatically via the API.
  name: Brainfish Catalogs API
  slug: brainfish-catalogs-api
- baseURL: https://api.brainfi.sh
  baseurl_source: declared
  description: Collection management operations including create, read, update, list, and delete
  name: Brainfish Collections API
  slug: brainfish-collections-api
- baseURL: https://api.brainfi.sh
  baseurl_source: declared
  description: Conversation operations including follow-up question generation
  name: Brainfish Conversations API
  slug: brainfish-conversations-api
- baseURL: https://api.brainfi.sh
  baseurl_source: declared
  description: Document management operations including create, read, update, list, and delete
  name: Brainfish Documents API
  slug: brainfish-documents-api
- baseURL: https://api.brainfi.sh
  baseurl_source: declared
  description: Chat session search, detail, timeline, and AI-powered insights. A "session" is a chat conversation keyed by conversationId.
  name: Brainfish Sessions API
  slug: brainfish-sessions-api
- baseURL: https://api.brainfi.sh
  baseurl_source: declared
  description: User-scoped operations. Generate answers personalized to a specific external/platform user with automatic attribute-based collection filtering.
  name: Brainfish Users API
  slug: brainfish-users-api
arazzos:
- description: Generate a cited AI answer for an end-user question, then generate suggested follow-up questions.
  name: Generate an answer and follow-up questions
  slug: brainfish-answer-and-followups
- description: Create a catalog, sync content into it, then read back its status.
  name: Create and sync an API catalog
  slug: brainfish-catalog-sync
- description: Validate the token, create a knowledge-base collection, then create a document inside it.
  name: Create a collection and add a document
  slug: brainfish-create-collection-and-document
artifact_total: 33
collections:
- collection_type: open
  name: Brainfish Public Agents API
  slug: open-brainfish-agents-api
- collection_type: open
  name: Brainfish Public Agents Analytics API
  slug: open-brainfish-analytics-api
- collection_type: open
  name: Brainfish Public Agents Authentication API
  slug: open-brainfish-authentication-api
- collection_type: open
  name: Brainfish Public Agents Catalogs API
  slug: open-brainfish-catalogs-api
- collection_type: open
  name: Brainfish Public Agents Collections API
  slug: open-brainfish-collections-api
- collection_type: open
  name: Brainfish Public Agents Conversations API
  slug: open-brainfish-conversations-api
- collection_type: open
  name: Brainfish Public Agents Documents API
  slug: open-brainfish-documents-api
- collection_type: open
  name: Brainfish Public Agents Sessions API
  slug: open-brainfish-sessions-api
- collection_type: open
  name: Brainfish Public Agents Users API
  slug: open-brainfish-users-api
common:
- group: operate
  href: https://artifacts.apis.io/brainfish/rate-limits/brainfish-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/brainfish-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/brainfish/plans/brainfish-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brainfish-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/brainfish/capabilities/brainfish-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/brainfish-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/brainfish/overlays/brainfish-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brainfish-public-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.brainfi.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brainfi.sh
- group: docs
  title: ''
  type: APIReference
  url: https://docs.brainfi.sh/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.brainfi.sh
- group: operate
  title: ''
  type: Support
  url: https://help.brainfi.sh
- group: agent
  href: https://artifacts.apis.io/brainfish/mcp/brainfish-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brainfish-mcp.yml
- group: agent
  href: https://artifacts.apis.io/brainfish/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/brainfish/packages/brainfish-packages.yml
  title: ''
  type: Packages
  url: packages/brainfish-packages.yml
- group: build
  href: https://artifacts.apis.io/brainfish/packages/brainfish-packages.yml
  title: ''
  type: SDKs
  url: packages/brainfish-packages.yml
- group: design
  href: https://artifacts.apis.io/brainfish/components/brainfish-components.yml
  title: ''
  type: Components
  url: components/brainfish-components.yml
- group: agent
  href: https://artifacts.apis.io/brainfish/well-known/brainfish-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brainfish-well-known.yml
- group: agent
  href: https://artifacts.apis.io/brainfish/llms/brainfish-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brainfish-llms.txt
- group: operate
  href: https://artifacts.apis.io/brainfish/changelog/brainfish-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brainfish-changelog.yml
- group: design
  href: https://artifacts.apis.io/brainfish/lifecycle/brainfish-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brainfish-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brainfi.sh
- group: auth
  href: https://artifacts.apis.io/brainfish/security/brainfish-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/brainfish-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.brainfi.sh/
- group: auth
  href: https://artifacts.apis.io/brainfish/security/brainfish-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainfish-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brainfish-ai
- group: company
  title: ''
  type: Blog
  url: https://www.brainfishai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brainfishai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.brainfi.sh
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brainfishai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brainfishai.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.brainfishai.com
created: '2026-07-17'
description: Brainfish is an AI product-support platform for B2B SaaS companies, built in Sydney and deployed globally with US/EU/AU data residency. Its AI support agents resolve customer tickets across chat, email, in-product, Slack and Teams, grounding every answer in the company's real product knowledge rather than training on customer data. Brainfish exposes a REST Public API (https://api.brainfi.sh) to programmatically manage the knowledge base (collections, documents, catalogs), generate cited AI answers and follow-up questions, and pull session analytics, plus a remote Model Context Protocol (MCP) server and an embeddable browser widget suite. Backed by Prosus Ventures.
finops:
- has_sources: true
  method: derived
  name: Brainfish Finops
  primary_unit: ''
  service_category: ''
  slug: brainfish-finops
  template: true
image: https://www.brainfishai.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.brainfi.sh over HTTP; 23 tools listed.
  name: Brainfish MCP Server
  slug: brainfish
modified: '2026-07-18'
name: Brainfish
nav: Providers
network: true
overview: 'Brainfish publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Analytics API, Authentication API, and 6 more. Tagged areas include Company, Artificial Intelligence, Customer Service, Knowledge Base, and Help Desk.


  The Brainfish catalog on APIs.io includes 1 Spectral governance ruleset.


  Brainfish''s developer surface includes documentation, API reference, getting-started guide, support, changelog, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Brainfish Plans Pricing
  plan_count: 3
  slug: brainfish-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Brainfish Rate Limits
  slug: brainfish-rate-limits
rules:
- authorship: generated
  effective_rule_count: 114
  extends:
  - spectral:oas
  name: Brainfish API Rules
  rule_count: 73
  severity_counts:
    error: 64
    hint: 0
    info: 3
    warn: 6
  slug: brainfish-rules
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 31.8
    contract_quality: 49.5
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 47.4
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/brainfish/brainfish-2026-07-25T203705.png
security:
- kind: authentication
  name: Brainfish Authentication
  slug: brainfish-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Brainfish Domain Security
  slug: brainfish-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Brainfish Trust Center
  slug: brainfish-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 3
skills:
- name: Generate an AI answer with Brainfish
  slug: brainfish-generate-ai-answer
- name: Manage a Brainfish knowledge base
  slug: brainfish-manage-knowledge-base
- name: Sync an API catalog into Brainfish
  slug: brainfish-sync-api-catalog
slug: brainfish
tags:
- Company
- Artificial Intelligence
- Customer Service
- Knowledge Base
- Help Desk
- Agents
- Support Automation
- Software-as-a-Service
website: https://www.brainfishai.com
---
