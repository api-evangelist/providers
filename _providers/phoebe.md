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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.1
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/phoebe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/phoebe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phoebe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withcoral.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://withcoral.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://withcoral.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://withcoral.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://withcoral.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://withcoral.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withcoral
- group: operate
  title: ''
  type: Support
  url: https://withcoral.com/discord
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withcoral.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withcoral.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/phoebe-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/phoebe-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/phoebe-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/phoebe-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/phoebe-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/phoebe-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/phoebe-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/phoebe-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/phoebe-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/phoebe-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/phoebe-conformance.yml
created: '2026-07-17'
description: Coral is a local-first SQL runtime that gives AI agents governed, read-only access to data across any API, database, or file system using standard SQL — no custom integrations, ETL, or glue code required. Built by Phoebe Technology Limited (a GV / Google Ventures portfolio company incorporated in England and Wales, formerly branded Phoebe at phoebe.ai), Coral translates SQL into API calls or file reads and returns a single result set, handling authentication, authorization, pagination, rate limiting, and schema mapping automatically. It ships 25+ bundled sources (GitHub, GitLab, Slack, Datadog, Linear, Sentry, Jira, Stripe, PagerDuty, Notion, Grafana, Confluence and more), supports cross-source SQL JOINs executed locally, and exposes the same runtime over the Model Context Protocol (MCP) or a CLI. Coral is open-source (Apache-2.0), self-hosted so queries and data never leave your infrastructure, and ISO 27001:2022 certified / GDPR compliant.
image: https://withcoral.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: phoebe-mcp.yml
  slug: phoebe-mcpyml
modified: '2026-07-20'
name: Coral
nav: Providers
network: true
overview: 'Coral is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Agents, Model Context Protocol, and SQL.


  Coral''s developer surface includes documentation, getting-started guide, engineering blog, pricing, support, CLI, changelog, and 18 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 30.1
  delta: -0.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 30.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Phoebe Domain Security
  slug: phoebe-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Phoebe Vulnerability Disclosure
  slug: phoebe-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: phoebe
tags:
- Company
- Ai
- Agents
- Model Context Protocol
- SQL
- Data Access
- Data Integration
- Developer Tools
- Open Source
website: https://withcoral.com
---
