---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Similarweb Agentic Access
  operation_count: 27
  slug: similarweb-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 14
apis:
- description: The SimilarWeb Batch API is optimized for large-scale bulk data extraction, supporting jobs of up to one million domains per request. It delivers data asynchronously to cloud storage destinations incl
  name: SimilarWeb Batch API
  slug: similarweb-batch-api
- description: Account credits, capabilities, and usage information
  name: SimilarWeb Account API
  slug: similarweb-account-api
- description: Mobile app downloads, active users, sessions, and demographics
  name: SimilarWeb App Intelligence API
  slug: similarweb-app-intelligence-api
- description: Batch API credit management
  name: SimilarWeb Credits API
  slug: similarweb-credits-api
- description: Geographic distribution of website traffic
  name: SimilarWeb Geography API
  slug: similarweb-geography-api
- description: Manage cloud storage integrations (S3, GCS, Snowflake)
  name: SimilarWeb Integrations API
  slug: similarweb-integrations-api
- description: Keyword analytics including organic and paid keyword data
  name: SimilarWeb Keywords API
  slug: similarweb-keywords-api
- description: Lead enrichment combining firmographics and web analytics
  name: SimilarWeb Lead Enrichment API
  slug: similarweb-lead-enrichment-api
- description: Global, country, and industry rank data
  name: SimilarWeb Rankings API
  slug: similarweb-rankings-api
- description: Submit, track, and retrieve bulk data report requests
  name: SimilarWeb Reports API
  slug: similarweb-reports-api
- description: Similar website discovery
  name: SimilarWeb Similar Sites API
  slug: similarweb-similar-sites-api
- description: Website traffic visits, bounce rate, pages per visit, visit duration
  name: SimilarWeb Traffic and Engagement API
  slug: similarweb-traffic-and-engagement-api
- description: Marketing channel traffic breakdown including organic, paid, referral, social, and display
  name: SimilarWeb Traffic Sources API
  slug: similarweb-traffic-sources-api
- description: Webhook subscription management for data-ready notifications
  name: SimilarWeb Webhooks API
  slug: similarweb-webhooks-api
artifact_total: 45
asyncapis:
- description: ''
  name: Similarweb Webhooks
  slug: similarweb-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SimilarWeb Batch Account API
  slug: open-similarweb-account-api
- collection_type: open
  name: SimilarWeb Batch Account App Intelligence API
  slug: open-similarweb-app-intelligence-api
- collection_type: open
  name: SimilarWeb Batch Account Credits API
  slug: open-similarweb-credits-api
- collection_type: open
  name: SimilarWeb Batch Account Geography API
  slug: open-similarweb-geography-api
- collection_type: open
  name: SimilarWeb Batch Account Integrations API
  slug: open-similarweb-integrations-api
- collection_type: open
  name: SimilarWeb Batch Account Keywords API
  slug: open-similarweb-keywords-api
- collection_type: open
  name: SimilarWeb Batch Account Lead Enrichment API
  slug: open-similarweb-lead-enrichment-api
- collection_type: open
  name: SimilarWeb Batch Account Rankings API
  slug: open-similarweb-rankings-api
- collection_type: open
  name: SimilarWeb Batch Account Reports API
  slug: open-similarweb-reports-api
- collection_type: open
  name: SimilarWeb Batch Account Similar Sites API
  slug: open-similarweb-similar-sites-api
- collection_type: open
  name: SimilarWeb Batch Account Traffic and Engagement API
  slug: open-similarweb-traffic-and-engagement-api
- collection_type: open
  name: SimilarWeb Batch Account Traffic Sources API
  slug: open-similarweb-traffic-sources-api
- collection_type: open
  name: SimilarWeb Batch Account Webhooks API
  slug: open-similarweb-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/similarweb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/similarweb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/similarweb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.similarweb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.similarweb.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/similarweb
- group: company
  title: ''
  type: Blog
  url: https://www.similarweb.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.similarweb.com/corp/daas/api/
- group: other
  title: ''
  type: X
  url: https://x.com/similarweb
- group: commercial
  title: ''
  type: Plans
  url: plans/similarweb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/similarweb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/similarweb-finops.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/similarweb-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/similarweb-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/similarweb-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/similarweb-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/similarweb-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/similarweb-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/similarweb-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/similarweb-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.similarweb.com/api-v5/guides/rest-api-data-version-migration
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/similarweb-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/similarweb-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.similarweb.com/corp/privacy-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/similarweb-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/similarweb-scopes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/similarweb-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/similarweb-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/similarweb-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/similarweb-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/similarweb-batch-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.similarweb.com/api-v5/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.similarweb.com/api-v5/api-reference/website-analysis-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.similarweb.com/api-v5/getting-started/making-your-first-request
- group: auth
  title: ''
  type: Authentication
  url: https://docs.similarweb.com/api-v5/getting-started/authentication
- group: operate
  title: ''
  type: Support
  url: https://support.similarweb.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://developers.similarweb.com/docs/getting-help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/similarweb
- group: start
  title: ''
  type: SignUp
  url: https://account.similarweb.com/standard-api
- group: start
  title: ''
  type: Login
  url: https://pro.similarweb.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.similarweb.com/corp/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.similarweb.com/corp/legal/privacy-policy/
created: '2026-06-13'
description: SimilarWeb is a digital intelligence platform offering a REST API for accessing website traffic estimates, audience demographics, keyword analytics, competitive benchmarking, app intelligence data, and lead generation insights. The API provides real-time and historical data covering traffic sources, search behavior, technographics, e-commerce shopper intelligence, and firmographic company data, enabling developers to integrate market intelligence into applications, dashboards, and data pipelines. The current generation is API V5, launched March 2026, which unified the REST and Batch API keys, added multi-metric requests, and shipped a first-party hosted MCP server at mcp.similarweb.com for AI agents; legacy v1-v4 REST endpoints carry a published sunset date of 2026-10-06.
examples:
- key_count: 2
  name: Similarweb Batch Request Example
  slug: similarweb-batch-request-example
- key_count: 2
  name: Similarweb Geography Example
  slug: similarweb-geography-example
- key_count: 2
  name: Similarweb Visits Desktop Example
  slug: similarweb-visits-desktop-example
finops:
- name: Similarweb Finops
  service_category: ''
  slug: similarweb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/similarweb.png
json_schemas:
- name: SimilarWeb Geography Response
  property_count: 2
  slug: similarweb-geography
- name: SimilarWeb Traffic and Engagement Response
  property_count: 6
  slug: similarweb-traffic-engagement
jsonld:
- class_count: 7
  name: Similarweb Context
  property_count: 49
  slug: similarweb-context
layout: provider
mcp_servers:
- description: Similarweb operates a first-party hosted (remote) MCP server at https://mcp.similarweb.com that exposes its Web, Search and App intelligence datasets as MCP tools. It is not an npm or PyPI package — t
  name: SimilarWeb MCP Server
  slug: similarweb-mcp-server
modified: '2026-08-13'
name: SimilarWeb
nav: Providers
network: true
overview: 'SimilarWeb publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, App Intelligence API, Credits API, and 10 more. Tagged areas include Digital Intelligence, Web Analytics, Traffic Analytics, Competitive Intelligence, and Keyword Analytics.


  The SimilarWeb catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SimilarWeb''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 36 more developer resources.'
plans:
- name: Similarweb Plans Pricing
  plan_count: 3
  slug: similarweb-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Similarweb Rate Limits
  slug: similarweb-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: SimilarWeb API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: similarweb-jsonschema-spectral-rules
scopes:
- name: Similarweb Scopes
  scope_count: 1
  slug: similarweb-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 71.5
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 40.2
    contract_quality: 73.8
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 40.2
    operational_transparency: 65.8
  previous_composite: 71.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/screenshots/similarweb-2026-06-20T193927.png
security:
- kind: authentication
  name: Similarweb Authentication
  slug: similarweb-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Similarweb Domain Security
  slug: similarweb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Similarweb Trust Center
  slug: similarweb-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: similarweb
tags:
- Digital Intelligence
- Web Analytics
- Traffic Analytics
- Competitive Intelligence
- Keyword Analytics
- Audience Demographics
- App Intelligence
- Market Research
- E-Commerce
- SEO
website: https://www.similarweb.com/
---
