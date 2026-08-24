---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Api Evangelist Agentic Access
  operation_count: 92
  slug: api-evangelist-agentic-access
  summary_line: 92 operations · 22 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: The whole network behind one REST API — unified search, 5,100+ posts, 77 topic areas, 2,400+ governance building blocks, conversations, papers, services, vocabulary, and newsletters from a single base
  name: API Evangelist Network API
  slug: api-evangelist-api
- description: 'Governance and discovery compute over the API Evangelist rule catalog — lint an OpenAPI against 461 curated rules or your own ruleset, score it, measure rule coverage, classify fields, diff versions, '
  name: API Evangelist Governance & Discovery API
  slug: api-evangelist-governance
- description: Model Context Protocol server over the same network — concierge tools (get_overview, guide_topic) plus find/get tools for every resource type, served over Streamable HTTP for AI agents.
  name: API Evangelist MCP Server
  slug: api-evangelist-mcp
- description: Individual API resources tracked across the API Evangelist network, drawn from many providers and business sectors and accompanied by OpenAPI reviews.
  name: API Evangelist APIs
  slug: api-evangelist-apis
- description: Over 4,000 stories on the API Evangelist blog since 2010 — the technology, business, and politics of how APIs are changing the way we live and work.
  name: API Evangelist Posts
  slug: api-evangelist-posts
- description: Regular conversations with API producers, consumers, and service providers about how they see APIs and what their biggest challenges are.
  name: API Evangelist Conversations
  slug: api-evangelist-conversations
- description: An alphabetical listing of every company tracked across the API Evangelist network, operating in almost every business sector.
  name: API Evangelist Companies
  slug: api-evangelist-companies
- description: The real-world human experience across teams producing APIs and the consumers who are applying and integrating them as part of business.
  name: API Evangelist Experiences
  slug: api-evangelist-experiences
- description: Modular guidance for teams producing and consuming APIs — snackable real-time guidance for keeping API operations moving forward.
  name: API Evangelist Guidance
  slug: api-evangelist-guidance
- description: The business reasons behind why we govern API operations — aligning the engineering side of operations with the business side of things.
  name: API Evangelist Policies
  slug: api-evangelist-policies
- description: Individual properties of API operations that can be linked to strategy, experience, and policies — and then governed to standardize how things work.
  name: API Evangelist Properties
  slug: api-evangelist-properties
- description: Technical details of API operations that can be automated and enforced, used to align policies with strategy to deliver the desired experience.
  name: API Evangelist Rules
  slug: api-evangelist-rules
- description: The naming and structure of the digital objects we pass back and forth via APIs within the business and personal applications we use.
  name: API Evangelist Schema
  slug: api-evangelist-schema
- description: Common Internet or industry standards used to consistently define API operations and keep the API factory floor well-defined and interoperable.
  name: API Evangelist Standards
  slug: api-evangelist-standards
- description: High-level approaches to shifting the direction of API operations — aligning policies and experiences across the platform.
  name: API Evangelist Strategies
  slug: api-evangelist-strategies
- description: Video content covering API topics, interviews, and walkthroughs of API concepts and technologies.
  name: API Evangelist Videos
  slug: api-evangelist-videos
- description: Organizing the words we use to describe API resources and capabilities — controlled vocabularies that help us get on the same page.
  name: API Evangelist Vocabularies
  slug: api-evangelist-vocabularies
artifact_total: 26
collections:
- collection_type: open
  name: API Evangelist Governance & Discovery API
  slug: open-apievangelist-governance
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/api-evangelist/posts/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/api-evangelist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-evangelist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/api-evangelist-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apievangelist.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.apievangelist.com
- group: company
  title: ''
  type: Blog
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.apievangelist.com/mcp
- group: agent
  title: ''
  type: MCPServerCard
  url: https://apievangelist.com/.well-known/mcp/server-card.json
- group: docs
  title: ''
  type: APIReference
  url: https://developer.apievangelist.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.apievangelist.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://apievangelist.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.apievangelist.com/plans/
- group: start
  title: ''
  type: SignUp
  url: https://api.apievangelist.com/v1/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apievangelist.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apievangelist.com/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/api-evangelist-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://developer.apievangelist.com/.well-known/api-catalog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/api-evangelist-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/api-evangelist-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/api-evangelist-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/api-evangelist-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/api-evangelist-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/api-evangelist-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/api-evangelist-data-model.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/api-evangelist-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://vocabularies.apievangelist.com
- group: commercial
  title: ''
  type: Plans
  url: plans/api-evangelist-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/api-evangelist-rate-limits.yml
- group: build
  title: ''
  type: Postman
  url: collections/apievangelist-v1.postman_collection.json
- group: build
  title: ''
  type: Postman
  url: collections/apievangelist-governance.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/apievangelist-governance.opencollection.json
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.apievangelist.com/changelog
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.apievangelist.com/deprecation
- group: auth
  title: ''
  type: Security
  url: https://developer.apievangelist.com/security
- group: auth
  title: ''
  type: SecurityTxt
  url: https://developer.apievangelist.com/.well-known/security.txt
- group: operate
  title: ''
  type: RoadMap
  url: https://developer.apievangelist.com/roadmap
created: '2024-10-14'
description: The index of everything available via the API Evangelist developer portal at developer.apievangelist.com — sixteen years of API research served as one REST API, an MCP server for agents, and the static JSON feeds behind each network collection.
image: https://kinlane-images.s3.amazonaws.com/shared/api-evangelist-logos/api-evangelist-butterfly-vertical.png
layout: provider
mcp_servers:
- description: ''
  name: API Evangelist MCP Server
  slug: api-evangelist-mcp-server
- description: ''
  name: API Evangelist MCP Server
  slug: api-evangelist-mcp-server-2
modified: '2026-08-10'
name: API Evangelist
nav: Providers
network: true
overview: 'API Evangelist publishes 2 APIs on the [APIs.io](https://apis.io/) network: Network API and Governance & Discovery API. Tagged areas include API Evangelist, Developer Portal, API Research, API Governance, and API Discovery.


  The API Evangelist catalog on APIs.io includes 1 Spectral governance ruleset.


  API Evangelist''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, pricing, and 32 more developer resources.'
plans:
- name: Api Evangelist Plans Pricing
  plan_count: 4
  slug: api-evangelist-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Api Evangelist Rate Limits
  slug: api-evangelist-rate-limits
rules:
- effective_rule_count: 88
  extends:
  - spectral:oas
  name: API Evangelist API Rules
  rule_count: 47
  severity_counts:
    error: 8
    hint: 0
    info: 8
    warn: 31
  slug: api-evangelist-spectral-rules
score:
  band: exemplar
  composite: 70.2
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 59.1
    contract_quality: 65.1
    developer_ergonomics: 63.7
    discoverability: 92.6
    governance: 59.1
    operational_transparency: 73.7
  previous_composite: 70.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-evangelist/refs/heads/main/screenshots/api-evangelist-2026-08-17T080558.png
security:
- kind: authentication
  name: Api Evangelist Authentication
  slug: api-evangelist-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Api Evangelist Domain Security
  slug: api-evangelist-domain-security
  summary_line: TLSv1.3
slug: api-evangelist
tags:
- API Evangelist
- Developer Portal
- API Research
- API Governance
- API Discovery
- MCP
- Agents
- API Standards
- API Vocabulary
website: https://developer.apievangelist.com
---
