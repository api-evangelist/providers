---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Unblocked Agentic Access
  operation_count: 12
  slug: unblocked-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 3
apis:
- description: Ask Unblocked questions and retrieve answers asynchronously. Submit a question using the PUT endpoint and poll for the response using the GET endpoint.
  name: Unblocked Answers API
  slug: unblocked-answers-api
- description: A collection in Unblocked allows you to organize related documents from various data sources, such as customer support tools, knowledge bases, and internal wikis, which are not natively supported by U
  name: Unblocked Collections API
  slug: unblocked-collections-api
- description: A document contains content that Unblocked uses to answer questions. Each document is associated with a collection, so you must create a collection before adding documents. Documents used to provide a
  name: Unblocked Documents API
  slug: unblocked-documents-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unblocked Public API Reference Answers API
  slug: open-unblocked-answers-api
- collection_type: open
  name: Unblocked Public API Reference Answers Collections API
  slug: open-unblocked-collections-api
- collection_type: open
  name: Unblocked Public API Reference Answers Documents API
  slug: open-unblocked-documents-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/unblocked-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://getunblocked.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getunblocked.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getunblocked.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getunblocked.com/api-reference/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getunblocked.com/api-reference/quickstart
- group: company
  title: ''
  type: Blog
  url: https://getunblocked.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unblocked
- group: commercial
  title: ''
  type: Pricing
  url: https://getunblocked.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://getunblocked.com/dashboard/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getunblocked.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getunblocked.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getunblocked.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unblocked-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unblocked-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unblocked-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/unblocked-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/unblocked-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unblocked-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unblocked-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unblocked-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unblocked-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/unblocked-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unblocked-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unblocked-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unblocked-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.getunblocked.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/unblocked-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unblocked-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unblocked-agentic-access.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unblocked-data-model.yml
- group: operate
  title: ''
  type: Support
  url: https://getunblocked.com/dashboard?showIntercom=true
created: '2026-07-17'
description: Unblocked is an AI context engine for engineering teams that consolidates code, documentation, tickets, and conversations from sources like GitHub, Slack, Jira, Confluence, Notion, and Google Drive into grounded, cited answers for engineers and AI coding agents. The product spans developer Q&A, AI code review with risk assessment, a CI failure agent, an official MCP server (local via the Unblocked CLI and hosted remote), open-source Agent Skills, and a Public API for ingesting custom documents and asking questions programmatically. Built by Next Chapter Software Inc and backed by Amplify Partners.
image: https://avatars.githubusercontent.com/u/91906527?s=300
layout: provider
mcp_servers:
- description: ''
  name: unblocked-mcp.yml
  slug: unblocked-mcpyml
modified: '2026-07-21'
name: Unblocked
nav: Providers
network: true
overview: 'Unblocked publishes 3 APIs on the [APIs.io](https://apis.io/) network: Answers API, Collections API, and Documents API. Tagged areas include Company, Developer Tools, AI, Developer Experience, and Knowledge Management.


  Unblocked''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 26 more developer resources.'
random_paper: 6
score:
  band: strong
  composite: 58.3
  delta: -0.7
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 65.0
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 18.4
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unblocked/refs/heads/main/screenshots/unblocked-2026-08-17T082549.png
security:
- kind: authentication
  name: Unblocked Authentication
  slug: unblocked-authentication
  summary_line: http-bearer/oauth2 · 2 schemes
- kind: domain-security
  name: Unblocked Domain Security
  slug: unblocked-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Unblocked Trust Center
  slug: unblocked-trust-center
  summary_line: SOC 2 Type II, SOC 3, CASA Tier 2, GDPR
slug: unblocked
tags:
- Company
- Developer Tools
- AI
- Developer Experience
- Knowledge Management
- Code Review
- MCP
- AI Agents
- Context Engineering
- Search
website: https://getunblocked.com
---
