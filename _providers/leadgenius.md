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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Leadgenius Agentic Access
  operation_count: 11
  slug: leadgenius-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 5
apis:
- description: Create, update and inspect enrichment campaigns.
  name: LeadGenius Campaigns API
  slug: leadgenius-campaigns-api
- description: Submit accounts and contacts that should be excluded from enrichment.
  name: LeadGenius Exclusion API
  slug: leadgenius-exclusion-api
- description: Real-time single-record account/contact enrichment and contact append.
  name: LeadGenius Rapid Enrichment API
  slug: leadgenius-rapid-enrichment-api
- description: Upload records to a campaign and retrieve enriched results.
  name: LeadGenius Records API
  slug: leadgenius-records-api
- description: Subscription usage and enrichment request statistics.
  name: LeadGenius Usage API
  slug: leadgenius-usage-api
artifact_total: 18
asyncapis:
- description: ''
  name: Leadgenius Enrichment Webhooks
  slug: leadgenius-enrichment-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LeadGenius Enrichment Campaigns API
  slug: open-leadgenius-campaigns-api
- collection_type: open
  name: LeadGenius Enrichment Campaigns Exclusion API
  slug: open-leadgenius-exclusion-api
- collection_type: open
  name: LeadGenius Enrichment Campaigns Rapid Enrichment API
  slug: open-leadgenius-rapid-enrichment-api
- collection_type: open
  name: LeadGenius Enrichment Campaigns Records API
  slug: open-leadgenius-records-api
- collection_type: open
  name: LeadGenius Enrichment Campaigns Usage API
  slug: open-leadgenius-usage-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leadgenius-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leadgenius-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://leadgenius.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.leadgenius.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leadgenius.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.leadgenius.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.leadgenius.com/#leadgenius-api-docs
- group: start
  title: ''
  type: SignUp
  url: https://app.leadgenius.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.leadgenius.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://support.leadgenius.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.leadgenius.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leadgenius.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leadgenius.com/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.leadgenius.com/legal/ccpa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leadgenius
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leadgenius/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/leadgenius
- group: other
  title: ''
  type: CaseStudies
  url: https://www.leadgenius.com/customers
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/leadgenius-enrichment-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/leadgenius-enrichment-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leadgenius-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leadgenius-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leadgenius-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leadgenius-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leadgenius-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leadgenius-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leadgenius-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leadgenius-enrichment-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leadgenius-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leadgenius-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/leadgenius-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leadgenius-plans-pricing.yml
created: '2026-07-17'
description: LeadGenius provides precision B2B contact and account intelligence for go-to-market teams, combining machine learning with a global team of human researchers so every contact and account is human-verified before delivery. The company reports 400+ customers, coverage across 42 countries and 3 billion+ data records served, with products spanning contact behavioral intelligence, advanced contact tags, contact monitoring, social tracking, buying-committee coverage and privacy compliance. Its developer surface is the LeadGenius Enrichment API — a RESTful, API-key authenticated service documented at docs.leadgenius.com that supports company enrichment, contact enrichment and contact append, offered both as asynchronous Campaigns (create a campaign, upload up to 200 records per request, receive a record-finalized webhook, retrieve the enriched results) and as real-time "rapid enrichment" requests submitted and collected by id.
image: https://cdn.prod.website-files.com/688ff1b200d9d4cf5019d518/68906378722ec3a7e64df624_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: leadgenius-mcp.yml
  slug: leadgenius-mcpyml
modified: '2026-08-13'
name: LeadGenius
nav: Providers
network: true
overview: 'LeadGenius publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Exclusion API, Rapid Enrichment API, and 2 more. Tagged areas include Company, Data Enrichment, Lead Generation, Sales, and Marketing.


  The LeadGenius catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LeadGenius'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: Leadgenius Plans Pricing
  plan_count: 0
  slug: leadgenius-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Leadgenius Rate Limits
  slug: leadgenius-rate-limits
score:
  band: developing
  composite: 40.7
  delta: -12.3
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 16.7
    contract_quality: 69.7
    developer_ergonomics: 8.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/leadgenius/refs/heads/main/screenshots/leadgenius-2026-07-25T224714.png
security:
- kind: authentication
  name: Leadgenius Authentication
  slug: leadgenius-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Leadgenius Domain Security
  slug: leadgenius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leadgenius
tags:
- Company
- Data Enrichment
- Lead Generation
- Sales
- Marketing
- B2B Data
- Contact Data
- Firmographics
- Go To Market
- Account Based Marketing
website: https://leadgenius.com
---
