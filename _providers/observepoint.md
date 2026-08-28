---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: The current, preferred ObservePoint REST API. 283 operations covering web audits and their runs, page/tag/cookie/ variable/browser-log/privacy reports, exports and scheduled exports, alerts, consent c
  name: ObservePoint V3 API
  slug: observepoint-v3-api
- description: The fastest and most flexible way to read ObservePoint results data. A single POST endpoint per grid entity type returns report data in row/column form with filters, operators, multi-column sorting, g
  name: ObservePoint Grid Reporting API
  slug: observepoint-grid-reporting-api
- description: The legacy but fully supported v2 REST API, served from https://api.observepoint.com/v2. 88 operations covering account, users, folders and sub-folders (domains), labels, tag and variable rules, tag d
  name: ObservePoint V2 API
  slug: observepoint-v2-api
artifact_total: 9
asyncapis:
- description: ''
  name: Observepoint Webhooks
  slug: observepoint-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/observepoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/observepoint-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.observepoint.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.observepoint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.observepoint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.observepoint.com/sections/v3-index
- group: start
  title: ''
  type: GettingStarted
  url: https://help.observepoint.com/en/articles/9106323-getting-started-with-the-observepoint-api
- group: operate
  title: ''
  type: Support
  url: https://help.observepoint.com/
- group: company
  title: ''
  type: Blog
  url: https://www.observepoint.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/observepoint
- group: commercial
  title: ''
  type: Pricing
  url: https://www.observepoint.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.observepoint.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.observepoint.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.observepoint.com/service-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.observepoint.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://news.observepoint.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.observepoint.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/observepoint-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/observepoint-site-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/observepoint-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/observepoint-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/observepoint-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/observepoint-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/observepoint-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/observepoint-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/observepoint-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/observepoint-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/observepoint-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/observepoint-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/observepoint-data-dictionary-schemas.json
created: '2026-08-26'
description: ObservePoint is a web governance and digital data-quality platform that automatically scans websites, mobile web properties and email links to validate analytics tags, marketing pixels, cookies, consent banners, link integrity and WCAG accessibility. Customers configure Audits (large-scale crawls of a site) and Web Journeys (scripted multi-step user paths), run them on a schedule or on demand, and get back structured reports on tags, variables, cookies, network requests, browser logs, privacy exposure and accessibility issues. Everything in the product is available through a public REST API at api.observepoint.com across two supported versions (v2 and v3) plus a Grid Reporting API that returns any report as rows and columns with filtering, sorting, grouping, pagination and export. API access is included with every ObservePoint subscription at no additional cost, and audits and journeys can push completion webhooks (HMAC-SHA256 signed) into CI/CD pipelines, BI tools and ticketing
  systems.
image: https://www.observepoint.com/wp-content/themes/observepoint/assets/images/op-fallback-img.png
json_schemas:
- name: Data Dictionary API by Observepoint
  property_count: 0
  slug: observepoint-data-dictionary-schemas
layout: provider
modified: '2026-08-26'
name: ObservePoint
nav: Providers
network: true
overview: 'ObservePoint publishes 3 APIs on the [APIs.io](https://apis.io/) network: V3 API, Grid Reporting API, and V2 API. Tagged areas include Company, Web Governance, Tag Management, Analytics Validation, and Privacy Compliance.


  The ObservePoint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ObservePoint''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Observepoint Plans Pricing
  plan_count: 0
  slug: observepoint-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Observepoint Rate Limits
  slug: observepoint-rate-limits
score:
  band: developing
  composite: 53.3
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 64.6
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 57.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Observepoint Authentication
  slug: observepoint-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Observepoint Domain Security
  slug: observepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: observepoint
tags:
- Company
- Web Governance
- Tag Management
- Analytics Validation
- Privacy Compliance
- Consent Management
- Web Accessibility
- Data Quality
- Marketing Technology
- Website Auditing
- Digital Analytics
- Webhooks
website: https://www.observepoint.com/
---
