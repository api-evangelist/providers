---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-09-14'
api_count: 29
apis:
- baseURL: https://api.squared.ai/api/v1/
  baseurl_source: declared
  description: REST API for the AI Squared platform covering connectors (data and AI/ML sources and destinations), connector definitions and connection checks, models, catalogs, syncs, scheduled/manual sync triggers
  name: AI Squared API
  slug: ai-squared-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://aisquared.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.squared.ai/home/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.squared.ai/home/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.squared.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.squared.ai/getting-started/introduction
- group: operate
  title: ''
  type: Support
  url: https://docs.squared.ai/open-source/community-support/overview
- group: company
  title: ''
  type: Blog
  url: https://aisquared.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://aisquared.ai/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Multiwoven
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AISquaredInc
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Multiwoven/multiwoven
- group: commercial
  title: ''
  type: Pricing
  url: https://aisquared.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.squared.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aisquared.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aisquared.ai/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://docs.squared.ai/deployment-and-security/security-and-compliance/overview
- group: auth
  title: ''
  type: Compliance
  url: https://docs.squared.ai/deployment-and-security/security-and-compliance/overview
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/openapi/ai-squared-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/ai-squared-openapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/llms/ai-squared-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-squared-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/mcp/ai-squared-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ai-squared-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/mcp/ai-squared-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ai-squared-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/a2a/ai-squared-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ai-squared-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/packages/ai-squared-packages.yml
  title: ''
  type: Packages
  url: packages/ai-squared-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/packages/ai-squared-packages.yml
  title: ''
  type: SDKs
  url: packages/ai-squared-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/well-known/ai-squared-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai-squared-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/conventions/ai-squared-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ai-squared-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/rate-limits/ai-squared-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ai-squared-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/plans/ai-squared-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ai-squared-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/authentication/ai-squared-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ai-squared-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/errors/ai-squared-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ai-squared-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/lifecycle/ai-squared-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ai-squared-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/changelog/ai-squared-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ai-squared-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/conformance/ai-squared-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-squared-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/security/ai-squared-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-squared-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/security/ai-squared-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ai-squared-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/data-model/ai-squared-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ai-squared-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/overlays/ai-squared-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ai-squared-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-squared/refs/heads/main/components/ai-squared-components.yml
  title: ''
  type: Components
  url: components/ai-squared-components.yml
created: '2026-09-13'
description: AI Squared is an enterprise data-and-AI integration platform that connects data sources (Snowflake, BigQuery, Databricks, Redshift, PostgreSQL, S3, Salesforce and more) to AI/ML model endpoints (OpenAI, Anthropic, Google Vertex, AWS Bedrock, SageMaker, WatsonX) and then pushes the resulting insights back into the business applications where work happens. The company acquired Multiwoven, the open-source Reverse ETL / composable CDP project, in 2024 and now develops it as the open core of the platform under AGPL-3.0. Its public REST API at api.squared.ai covers connectors, connector definitions, models, catalogs, syncs, sync runs and sync records, authenticated with a JWT bearer token. AI Squared is SOC 2 Type II certified and ships SaaS, cloud, on-premise and air-gapped federal deployments.
image: https://i0.wp.com/aisquared.ai/wp-content/uploads/2026/06/screenshot.png
layout: provider
mcp_servers:
- description: An anonymous, read-mostly MCP server over the AI Squared documentation corpus, advertised by AI Squared at /.well-known/mcp.json on its own documentation host. It exposes documentation search, a read-
  name: AI Squared Documentation MCP Server
  slug: ai-squared-documentation-mcp-server
modified: '2026-09-13'
name: AI Squared
nav: Providers
network: true
overview: 'AI Squared publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, Reverse ETL, Artificial Intelligence, Machine-Learning, and Customer Data Platform.


  AI Squared''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Ai Squared Plans Pricing
  plan_count: 3
  slug: ai-squared-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Ai Squared Rate Limits
  slug: ai-squared-rate-limits
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 47.7
    developer_ergonomics: 71.4
    discoverability: 81.5
    operational_transparency: 52.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Ai Squared Authentication
  slug: ai-squared-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ai Squared Domain Security
  slug: ai-squared-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ai Squared Vulnerability Disclosure
  slug: ai-squared-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Ai Squared Trust Center
  slug: ai-squared-trust-center
  summary_line: SOC 2 Type II, HIPAA, CCPA
slug: ai-squared
tags:
- Data Integration
- Reverse ETL
- Artificial Intelligence
- Machine-Learning
- Customer Data Platform
- Data Activation
- Workflow-Automation
- Open-Source
- MCP
- Enterprise
website: https://aisquared.ai/
---
