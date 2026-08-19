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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Owler Agentic Access
  operation_count: 6
  slug: owler-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: 'Read-only REST API over Owler''s company graph. Three products in one OpenAPI 3.0.1 definition: Company Premium (complete firmographics, funding, acquisitions, stock and CEO data for a company looked u'
  name: Owler Enterprise API
  slug: owler-enterprise-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/owler-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://corp.owler.com
- group: other
  title: ''
  type: DataLicensing
  url: https://corp.owler.com/data-licensing
- group: company
  title: ''
  type: Blog
  url: https://corp.owler.com/blog
- group: operate
  title: ''
  type: Support
  url: https://owlerinc.happyfox.com/home/
- group: operate
  title: ''
  type: HelpCenter
  url: https://owlerinc.happyfox.com/kb/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.owler.com/checkout/owlerpro
- group: start
  title: ''
  type: Login
  url: https://www.owler.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corp.owler.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corp.owler.com/privacy-notice
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.owler.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.owler.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.owler.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.owler.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/owler-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/owler-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/owler-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/owler-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/owler-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/owler-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/owler-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/owler-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/owler-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/owler-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/owler-domain-security.yml
created: '2026-07-17'
description: 'Owler is a crowdsourced competitive- and business-intelligence platform that maintains real-time profiles on more than 20 million public and private companies, tracking firmographics, funding, and news across 45M+ competitive relationships contributed and validated by a community of 5M+ business professionals. It is delivered as web and mobile apps (Owler Community, Pro, and Max), a Chrome extension, and CRM and collaboration integrations (Salesforce, HubSpot, Slack, Microsoft Teams, ChatGPT). The Owler Enterprise API is a real, publicly documented REST API: a Swagger UI developer portal at developers.owler.com renders an OpenAPI 3.0.1 definition (six read operations across Company Premium, Competitor Premium and Feed, served from https://apiv2.owler.com, authenticated with an x-api-key header) that is fetchable at https://developers-v3.owler.com/apis/api3-swagger.json. Access to the data itself is sold through the data-licensing sales motion rather than self-serve signup,
  and Owler ships no first-party SDKs, CLI or MCP server. Owler was acquired by Meltwater in 2021. Added to the API Evangelist network from the Norwest Venture Partners portfolio.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/owler.png
layout: provider
mcp_servers:
- description: ''
  name: owler-mcp.yml
  slug: owler-mcpyml
modified: '2026-08-14'
name: Owler
nav: Providers
network: true
overview: 'Owler publishes 1 API on the [APIs.io](https://apis.io/) network: Enterprise API. Tagged areas include Company, Company Intelligence, Sales Intelligence, Competitive Intelligence, and Business Data.


  Owler''s developer surface includes engineering blog, support, pricing, documentation, API reference, and 21 more developer resources.'
plans:
- name: Owler Plans Pricing
  plan_count: 0
  slug: owler-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 0
  name: Owler Rate Limits
  slug: owler-rate-limits
score:
  band: developing
  composite: 40.1
  delta: -4.5
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 16.7
    contract_quality: 59.4
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/owler/refs/heads/main/screenshots/owler-2026-08-07T191152.png
security:
- kind: authentication
  name: Owler Authentication
  slug: owler-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Owler Domain Security
  slug: owler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: owler
tags:
- Company
- Company Intelligence
- Sales Intelligence
- Competitive Intelligence
- Business Data
- Data Licensing
- News Monitoring
- Market Research
- Firmographics
- Company Search
- Funding Data
website: https://corp.owler.com
---
