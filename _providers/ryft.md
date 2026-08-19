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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Push query-execution telemetry to Ryft.
  name: Ryft Ingest API
  slug: ryft-ingest-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ryft Ingest API
  slug: open-ryft-ingest-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ryft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ryft.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ryft.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ryft.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ryft.io/integrations/custom-engine
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ryft.io/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.ryft.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ryft.io/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ryft.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ryft.io/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.ryft.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ryft-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ryft-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ryft-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ryft-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ryft-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ryft-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.ryft.io/administration/security-and-privacy
- group: other
  title: ''
  type: Overlay
  url: overlays/ryft-ingest-overlay.yaml
created: '2026-07-17'
description: Ryft is the intelligent Apache Iceberg management platform - a data lakehouse optimization layer that continuously monitors, manages, and optimizes Iceberg tables across query engines and clouds. It provides automated table compaction, snapshot and data lifecycle management, orphan-file and compliance cleanup (GDPR/CCPA), an Asset and Query Explorer, and usage-based self-tuning that reduces lakehouse TCO and speeds up queries. Ryft integrates with AWS (Athena, Glue, Redshift, S3 Tables), Google Cloud/BigLake, Azure, Microsoft OneLake, Databricks, Snowflake, Starburst, Trino, StarRocks, and any Iceberg REST Catalog. For engines it does not natively support, the Ryft Ingest API accepts query telemetry directly, and the Ryft MCP server enriches AI agents with live lakehouse context. Backed by Bessemer Venture Partners and Index Ventures; acquired by Cyera in 2026.
image: https://cdn.ryft.io/static/assets/icon_full_new.png
layout: provider
mcp_servers:
- description: ''
  name: ryft-mcp.yml
  slug: ryft-mcpyml
modified: '2026-07-21'
name: Ryft
nav: Providers
network: true
overview: 'Ryft publishes 1 API on the [APIs.io](https://apis.io/) network: Ingest API. Tagged areas include Company, Data, Data Lake, Lakehouse, and Apache Iceberg.


  Ryft''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 13 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 45.9
  delta: -1.9
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 58.7
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 47.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ryft/refs/heads/main/screenshots/ryft-2026-08-17T081702.png
security:
- kind: authentication
  name: Ryft Authentication
  slug: ryft-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Ryft Domain Security
  slug: ryft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ryft
tags:
- Company
- Data
- Data Lake
- Lakehouse
- Apache Iceberg
- Data Management
- Analytics
- Query Optimization
- AI
- MCP
website: https://www.ryft.io/
---
