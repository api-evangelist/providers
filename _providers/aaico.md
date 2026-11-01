---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The Opus REST API. Generate a workflow from a natural-language prompt, run a workflow as a "case" with populated inputs, upload files as case inputs through a presigned-URL flow, poll or receive a cal
  name: Opus Platform API
  slug: opus-platform-api
- description: 'A first-party remote MCP server over the Opus developer documentation, reachable anonymously at https://developer.opus.com/mcp over streamable HTTP. Three tools: semantic search across the docs, a rea'
  name: Opus Docs MCP Server
  slug: opus-docs-mcp
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.aaico.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.opus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.opus.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.opus.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.opus.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.opus.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.opus.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opus.com/legal-docs/Opus-Subscriber-Agreement.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opus.com/legal-docs/Opus-Privacy-Policy.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opus.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.opus.com/
- group: auth
  href: https://artifacts.apis.io/aaico/conformance/aaico-conformance.yml
  title: ''
  type: Compliance
  url: conformance/aaico-conformance.yml
- group: operate
  href: https://artifacts.apis.io/aaico/changelog/aaico-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aaico-changelog.yml
- group: design
  href: https://artifacts.apis.io/aaico/lifecycle/aaico-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aaico-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/aaico/mcp/aaico-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aaico-mcp.yml
- group: other
  href: https://artifacts.apis.io/aaico/a2a/aaico-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aaico-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aaico/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aaico/llms/aaico-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aaico-llms.txt
- group: agent
  href: https://artifacts.apis.io/aaico/well-known/aaico-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aaico-well-known.yml
- group: auth
  href: https://artifacts.apis.io/aaico/authentication/aaico-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aaico-authentication.yml
- group: design
  href: https://artifacts.apis.io/aaico/conventions/aaico-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aaico-conventions.yml
- group: design
  href: https://artifacts.apis.io/aaico/errors/aaico-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aaico-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/aaico/rate-limits/aaico-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aaico-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aaico/plans/aaico-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aaico-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/aaico/packages/aaico-packages.yml
  title: ''
  type: Packages
  url: packages/aaico-packages.yml
- group: design
  href: https://artifacts.apis.io/aaico/conformance/aaico-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aaico-conformance.yml
- group: auth
  href: https://artifacts.apis.io/aaico/security/aaico-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aaico-domain-security.yml
- group: build
  title: ''
  type: Postman
  url: https://developer.opus.com/api-reference/v0-jobs/postman-collection
- group: design
  href: https://artifacts.apis.io/aaico/conventions/aaico-conventions.yml
  title: ''
  type: Webhooks
  url: conventions/aaico-conventions.yml
created: '2026-09-05'
description: 'AppliedAI — The Applied AI Company, or AAICO — is an Abu Dhabi headquartered company, founded in 2021, that builds AI-native workflow systems for heavily regulated industries: banking, fintech, insurance, healthcare, life sciences and government. Its platform, Opus, lets organizations discover an existing business process, build it as an auditable workflow of AI agents and human review steps, run it, and optimize it — automating document-heavy back-office and mid-office operations while keeping governance, audit trails and human oversight intact. Opus is built on a proprietary Large Work Model and Work Knowledge Graph that encode procedural knowledge. The company publishes a developer hub at developer.opus.com with a REST platform API for generating workflows, running them as cases, uploading files, reading discovered processes and authoring custom integrations, plus a remote MCP server over its documentation, an A2A agent card and a published Agent Skill. AAICO raised a $55M
  Series A led by G42 with Palantir, Bessemer Venture Partners, McKinsey, e& and Accrete Capital participating.'
image: https://www.aaico.com/images/built-for-momentum.jpg
layout: provider
mcp_servers:
- description: 'A first-party, publicly reachable MCP server over the Opus developer documentation. It is a READ-ONLY documentation surface: it searches and reads published docs pages and lets a client file docs feed'
  name: Opus Docs MCP Server
  slug: opus-docs-mcp-server
modified: '2026-09-05'
name: AppliedAI (AAICO)
nav: Providers
network: true
overview: 'AppliedAI (AAICO) is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Opus Platform API, and 1 more. Tagged areas include Company, Artificial Intelligence, Workflow Automation, Agents, and Enterprise.


  AppliedAI (AAICO)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 22 more developer resources.'
plans:
- name: Aaico Plans Pricing
  plan_count: 0
  slug: aaico-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Aaico Rate Limits
  slug: aaico-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 65.0
    operational_transparency: 71.1
  previous_composite: 40.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 24.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aaico/aaico-2026-10-11T092340.png
security:
- kind: authentication
  name: Aaico Authentication
  slug: aaico-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aaico Domain Security
  slug: aaico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aaico Vulnerability Disclosure
  slug: aaico-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Aaico Trust Center
  slug: aaico-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 42001, HIPAA, GDPR, EU AI Act
skill_count: 1
skills:
- name: Opus Developer Documentation
  slug: aaico-opus-developer-documentation
slug: aaico
tags:
- Company
- Artificial Intelligence
- Workflow Automation
- Agents
- Enterprise
- Document Processing
- Regulated Industries
- Business Process Automation
- Banking
- Insurance
- Healthcare
- MCP
- A2A
website: https://www.aaico.com/
---
