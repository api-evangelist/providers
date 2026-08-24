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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: HTTP REST API to interact with a Secoda workspace — CRUD over catalog resources (databases, schemas, tables, columns, dashboards, charts, collections, documents, glossary/terms, tags, custom propertie
  name: Secoda API
  slug: secoda-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://secoda.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.secoda.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.secoda.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.secoda.co/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.secoda.co/api/reference/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.secoda.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.secoda.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.secoda.co/auth
- group: operate
  title: ''
  type: Support
  url: mailto:support@secoda.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.secoda.co/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.secoda.co/policies/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.secoda.co/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.secoda.co
- group: auth
  title: ''
  type: Authentication
  url: authentication/secoda-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/secoda-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/secoda-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/secoda-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/secoda-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/secoda-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/secoda-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/secoda-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.secoda.co/policies/security-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.secoda.co
- group: auth
  title: ''
  type: Security
  url: https://docs.secoda.co/policies/security-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/secoda-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secoda-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/secoda-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/secoda-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/secoda-llms.txt
created: '2026-07-17'
description: Secoda is an AI-powered data catalog, governance, and observability platform that acts as a metadata control plane for data teams. It unifies discovery, documentation, lineage, data-quality monitoring, and access governance across 70+ integrations (Snowflake, BigQuery, Databricks, dbt, Tableau, and more), and exposes a REST API plus a Model Context Protocol (MCP) server so agents and automation can search assets, run SQL, retrieve lineage, and manage users, tags, and metadata programmatically. Backed by Craft Ventures.
image: https://cdn.prod.website-files.com/61ddd0b42c51f86c96e1e90e/683a14fafd2295179b0ab954_Open%20graph%20image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Secoda MCP Server
  slug: secoda-mcp-server
modified: '2026-07-21'
name: Secoda
nav: Providers
network: true
overview: 'Secoda publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Data Catalog, Data Governance, and Metadata.


  Secoda''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 23 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 1
  name: Secoda Rate Limits
  slug: secoda-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 36.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Secoda Authentication
  slug: secoda-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Secoda Domain Security
  slug: secoda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Secoda Vulnerability Disclosure
  slug: secoda-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Secoda Trust Center
  slug: secoda-trust-center
  summary_line: SOC 2
slug: secoda
tags:
- Company
- Developer Tools
- Data Catalog
- Data Governance
- Metadata
- Data Lineage
- Data Quality
- Data Discovery
- Observability
- AI Agents
website: https://secoda.co
---
