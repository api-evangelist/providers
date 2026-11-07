---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Asynchronous REST API for asking natural-language analytics questions against connected data. Create a session, submit an inquiry, then poll or long-poll for a grounded answer with generated SQL, stru
  name: Jedify Data Intelligence API
  slug: jedify-data-intelligence-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Blog
  url: https://jedify.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://jedify.com/feed/
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
  href: https://artifacts.apis.io/jedify/mcp/jedify-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jedify-mcp.yml
- group: agent
  href: https://artifacts.apis.io/jedify/llms/jedify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jedify-llms.txt
- group: auth
  href: https://artifacts.apis.io/jedify/authentication/jedify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jedify-authentication.yml
- group: build
  href: https://artifacts.apis.io/jedify/packages/jedify-packages.yml
  title: ''
  type: Packages
  url: packages/jedify-packages.yml
- group: design
  href: https://artifacts.apis.io/jedify/conventions/jedify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jedify-conventions.yml
- group: design
  href: https://artifacts.apis.io/jedify/errors/jedify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jedify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jedify/data-model/jedify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jedify-data-model.yml
- group: design
  href: https://artifacts.apis.io/jedify/components/jedify-components.yml
  title: ''
  type: Components
  url: components/jedify-components.yml
- group: agent
  href: https://artifacts.apis.io/jedify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/jedify/changelog/jedify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jedify-changelog.yml
- group: auth
  href: https://artifacts.apis.io/jedify/security/jedify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jedify-domain-security.yml
created: '2026-07-17'
description: Jedify is an enterprise AI platform that fuses business context with multi-source data into an AI-ready contextual "context layer" (Semantic Fusion) so companies can run grounded, natural-language analytics and autonomous data agents across their data lakes, warehouses, BI tools, databases, CRMs, and documents. It exposes an asynchronous session/inquiry REST API at be.jedify.com/api (X-API-Key auth), a published Model Context Protocol (MCP) server with Asker, Editor, and Builder modes for connecting Claude, Cursor, and other agents, plus native data connectors (Snowflake, BigQuery, Redshift, Databricks, Athena, dbt, Looker, Tableau) and embedded surfaces for Looker and Slack. Jedify raised a $24M Series A and is backed by Norwest Venture Partners.
image: https://jedify.com/wp-content/uploads/logo01-1-1.svg
layout: provider
mcp_servers:
- description: Remote MCP server at be.jedify.com over HTTP; 16 tools listed.
  name: Jedify MCP Server
  slug: jedify
modified: '2026-10-06'
name: Jedify
nav: Providers
network: true
overview: 'Jedify is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data Analytics, Business Intelligence, and Semantic Layer.


  Jedify''s developer surface includes engineering blog, documentation, API reference, getting-started guide, signup flow, changelog, authentication, and 15 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 15.8
  previous_composite: 22.4
  provenance:
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jedify/jedify-2026-07-25T223116.png
security:
- kind: authentication
  name: Jedify Authentication
  slug: jedify-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Jedify Domain Security
  slug: jedify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Ask Jedify a question and get the answer
  slug: jedify-ask-a-question
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
