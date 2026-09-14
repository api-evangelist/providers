---
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
  title: ''
  type: OpenAPI
  url: openapi/ai-squared-openapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ai-squared-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ai-squared-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ai-squared-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/ai-squared-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/ai-squared-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ai-squared-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ai-squared-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ai-squared-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ai-squared-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ai-squared-plans-pricing.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ai-squared-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ai-squared-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ai-squared-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ai-squared-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ai-squared-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ai-squared-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ai-squared-vulnerability-disclosure.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ai-squared-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ai-squared-openapi-overlay.yaml
- group: design
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
overview: 'AI Squared publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, Reverse ETL, Artificial Intelligence, Machine Learning, and Customer Data Platform.


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
- Machine Learning
- Customer Data Platform
- Data Activation
- Workflow Automation
- Open Source
- MCP
- Enterprise
website: https://aisquared.ai/
---
