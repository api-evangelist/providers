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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Asynchronous REST API for asking natural-language analytics questions against connected data. Create a session, submit an inquiry, then poll or long-poll for a grounded answer with generated SQL, stru
  name: Jedify Data Intelligence API
  slug: jedify-data-intelligence-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://jedify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.jedify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jedify.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jedify.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jedify.com/getting-started/introduction
- group: start
  title: ''
  type: SignUp
  url: https://app.jedify.com/sign-up
- group: company
  title: ''
  type: Blog
  url: https://jedify.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jedify.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.jedify.com/changelog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jedify-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jedify-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/jedify-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/jedify-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jedify-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jedify-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jedify-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/jedify-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jedify-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jedify-domain-security.yml
created: '2026-07-17'
description: Jedify is an enterprise AI platform that fuses business context with multi-source data into an AI-ready contextual "context layer" (Semantic Fusion) so companies can run grounded, natural-language analytics and autonomous data agents across their data lakes, warehouses, BI tools, databases, CRMs, and documents. It exposes an asynchronous session/inquiry REST API at be.jedify.com/api (X-API-Key auth), a published Model Context Protocol (MCP) server with Asker, Editor, and Builder modes for connecting Claude, Cursor, and other agents, plus native data connectors (Snowflake, BigQuery, Redshift, Databricks, Athena, dbt, Looker, Tableau) and embedded surfaces for Looker and Slack. Jedify raised a $24M Series A and is backed by Norwest Venture Partners.
image: https://jedify.com/wp-content/uploads/logo01-1-1.svg
layout: provider
mcp_servers:
- description: ''
  name: Jedify MCP Server
  slug: jedify-mcp-server
modified: '2026-07-19'
name: Jedify
nav: Providers
network: true
overview: 'Jedify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data Analytics, Business Intelligence, and Semantic Layer.


  Jedify''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, changelog, authentication, and 13 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 22.6
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jedify/refs/heads/main/screenshots/jedify-2026-07-25T223116.png
security:
- kind: authentication
  name: Jedify Authentication
  slug: jedify-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Jedify Domain Security
  slug: jedify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jedify
tags:
- Company
- Artificial Intelligence
- Data Analytics
- Business Intelligence
- Semantic Layer
- Context Layer
- Data Agents
- MCP
- Enterprise AI
- Natural Language Query
website: https://jedify.com
---
