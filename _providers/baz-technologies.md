---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/baz-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baz.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://baz.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://baz.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://baz.ai/docs/basics/getting-started
- group: company
  title: ''
  type: Blog
  url: https://baz.ai/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/baz-scm
- group: commercial
  title: ''
  type: Pricing
  url: https://baz.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://baz.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://baz.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://baz.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://baz.ai/contact
- group: operate
  title: ''
  type: ChangeLog
  url: https://baz.ai/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/baz-technologies-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/baz-technologies-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/baz-technologies-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/baz-technologies-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/baz-technologies-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/baz-technologies-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://baz.ai/docs/account/security-privacy-and-compliance
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/baz-technologies-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://baz.ai/docs/account/security-privacy-and-compliance
created: '2026-07-17'
description: Baz Technologies (Baz) is a Tel Aviv-based engineering review platform that uses purpose-built AI agents — code review, spec review, advanced security, SRE, and an automated fixer — to review implementation plans, pull requests, security findings, and merge decisions across the whole software development lifecycle. Baz reads the entire codebase alongside production telemetry to catch bugs and vulnerabilities before they ship, integrating with GitHub, GitLab, and Azure DevOps and issue/observability tools (Jira, Linear, Datadog, Sentry). It exposes its context-aware reviews to AI-native IDEs and CLIs (Cursor, Claude, VS Code) through a hosted Model Context Protocol (MCP) server, an npm-distributed CLI, and a coding-agent plugin. Backed by Battery Ventures and boldstart ventures with $17M in seed funding.
image: https://baz.ai/seo.jpg
layout: provider
mcp_servers:
- description: Baz exposes a hosted, remote MCP server that delivers context-aware, org-configured code reviews directly inside any MCP-enabled IDE, CLI, or agent (Cursor, Claude Code / Desktop, VS Code). Review pri
  name: Baz Technologies MCP Server
  slug: baz-technologies-mcp-server
modified: '2026-07-18'
name: Baz Technologies
nav: Providers
network: true
overview: 'Baz Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Code Review, Developer Tools, AI Agents, and Application Security.


  Baz Technologies'' developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 16 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 32.1
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/baz-technologies/refs/heads/main/screenshots/baz-technologies-2026-07-25T202451.png
security:
- kind: domain-security
  name: Baz Technologies Domain Security
  slug: baz-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Baz Technologies Vulnerability Disclosure
  slug: baz-technologies-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Baz Technologies Trust Center
  slug: baz-technologies-trust-center
  summary_line: SOC 2
slug: baz-technologies
tags:
- Company
- Code Review
- Developer Tools
- AI Agents
- Application Security
- Agentic Coding
- DevOps
- MCP
- Software Engineering
website: https://baz.ai
---
