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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: The current MadKudu API (MadAPI) exposes account and person lookup, full account/person details and activities, company hiring/job-posting enrichment, person contact enrichment, advanced account and p
  name: MadKudu API (MadAPI)
  slug: madkudu-api-madapi
- description: 'The legacy MadKudu Scoring API returns customer-fit, likelihood-to-buy and lead-grade scores for accounts and persons. Authentication is HTTP Basic (API key as username); rate limited to 600 requests '
  name: MadKudu Legacy Scoring API
  slug: madkudu-legacy-scoring-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://madkudu.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.madkudu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.madkudu.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.madkudu.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.madkudu.com/getting-started
- group: agent
  title: ''
  type: MCPServer
  url: mcp/madkudu-mcp.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MadKudu
- group: operate
  title: ''
  type: Support
  url: mailto:support@madkudu.com
- group: start
  title: ''
  type: Login
  url: https://msi.madkudu.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/madkudu-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/madkudu-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/madkudu-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/madkudu-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/madkudu-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/madkudu-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/madkudu-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/madkudu-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/madkudu-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/madkudu-llms.txt
created: '2026-07-17'
description: MadKudu is a predictive lead scoring and account intelligence platform for B2B sales and marketing teams, using AI-driven propensity modeling and dynamic scoring across fit, intent, and engagement signals to surface high-propensity accounts and people. Its developer surface (MadAPI) programmatically exposes account and person lookup, enrichment, activity, search, discovery, and organisation endpoints, plus a hosted Model Context Protocol (MCP) server for AI agents. MadKudu is now part of HG Insights (HG Sales Copilot). Originally backed by Partech and Techstars.
image: https://developers.madkudu.com/~gitbook/image
layout: provider
mcp_servers:
- description: ''
  name: madkudu-mcp.yml
  slug: madkudu-mcpyml
modified: '2026-07-20'
name: MadKudu
nav: Providers
network: true
overview: 'MadKudu publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Applicative Saas, Sales Intelligence, Lead Scoring, and Predictive Analytics.


  MadKudu''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 14 more developer resources.'
random_paper: 27
score:
  band: emerging
  composite: 24.7
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 66.8
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 24.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/screenshots/madkudu-2026-07-25T225833.png
security:
- kind: authentication
  name: Madkudu Authentication
  slug: madkudu-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Madkudu Domain Security
  slug: madkudu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: madkudu
tags:
- Company
- Applicative Saas
- Sales Intelligence
- Lead Scoring
- Predictive Analytics
- Account Intelligence
- Data Enrichment
- MCP
website: https://madkudu.com/
---
