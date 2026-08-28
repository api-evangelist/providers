---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-26'
api_count: 7
apis:
- description: Synchronize employee records and organizational unit (OU) structures between external systems and Cornerstone. Supports create, read, update, and deactivate operations for users and organizational hie
  name: Cornerstone Employee and OU API
  slug: cornerstone-employee-and-ou-api
- description: Programmatically assign training courses to user transcripts asynchronously. Track assignment status and search for existing assignments across the enterprise.
  name: Cornerstone Learning Assignment API
  slug: cornerstone-learning-assignment-api
- description: Manage the full recruiting lifecycle including job requisitions, candidate profiles, applications, and offer management. Supports applicant tracking system (ATS) integrations.
  name: Cornerstone Recruiting API
  slug: cornerstone-recruiting-api
- description: Access workforce analytics and reporting data using an OData-compatible interface with server-driven paging. Supports BI tool integrations including Power BI.
  name: Cornerstone Reporting API
  slug: cornerstone-reporting-api
- description: Reliably import large volumes of data into Cornerstone either as a one-time load or recurring system-to-system synchronization. Supports asynchronous job submission, status tracking, and error reporti
  name: Cornerstone Bulk API
  slug: cornerstone-bulk-api
- description: Access and manage performance review cycles, goals, competencies, ratings, and succession planning data for enterprise workforce development workflows.
  name: Cornerstone Performance API
  slug: cornerstone-performance-api
- description: Subscribe to near real-time HTTP event notifications for critical Cornerstone business events including learner enrollment, course completion, candidate creation, account creation, and session attenda
  name: Cornerstone Webhooks
  slug: cornerstone-webhooks
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cornerstone-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://csod.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://csod.dev/guides/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://csod.dev/guides/getting-started/authentication.html
- group: operate
  title: ''
  type: RateLimits
  url: https://csod.dev/guides/getting-started/throttling.html
- group: operate
  title: ''
  type: Status
  url: https://status.csod.com/
- group: docs
  title: ''
  type: HelpDocumentation
  url: https://help.csod.com/help/csod_0/Content/User/Edge/Overview_Topics_-_Edge/APIs_Overview.htm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cornerstoneondemand
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.csod.com/
- group: company
  title: ''
  type: Website
  url: https://www.cornerstoneondemand.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cornerstoneondemand.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cornerstoneondemand.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.cornerstoneondemand.com/company/security
- group: commercial
  title: ''
  type: Plans
  url: plans/cornerstone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cornerstone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cornerstone-finops.yml
created: '2026-06-13'
description: Cornerstone OnDemand is an enterprise talent management platform offering REST APIs for learning management, performance reviews, succession planning, recruiting, and workforce analytics. The APIs are RESTful, support OAuth 2.0 Client Credentials authentication, and return JSON (with some XML support). Developers can integrate with modules including Core HR, Learning, Performance, Recruiting, Reporting, Bulk data import, Connectors, and Webhooks through the Cornerstone Developer Portal at csod.dev.
finops:
- name: Cornerstone Finops
  service_category: ''
  slug: cornerstone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cornerstone.png
jsonld:
- class_count: 45
  name: Cornerstone Context
  property_count: 8
  slug: cornerstone-context
layout: provider
modified: '2026-06-13'
name: Cornerstone OnDemand
nav: Providers
network: true
overview: 'Cornerstone OnDemand publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Talent Management, Learning Management, Performance Management, Recruiting, and HR.


  The Cornerstone OnDemand catalog on APIs.io includes 1 JSON-LD context.


  Cornerstone OnDemand''s developer surface includes developer portal, documentation, authentication, status page, and 12 more developer resources.'
plans:
- name: Cornerstone Plans Pricing
  plan_count: 5
  slug: cornerstone-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Cornerstone Rate Limits
  slug: cornerstone-rate-limits
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 32.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cornerstone/refs/heads/main/screenshots/cornerstone-2026-06-20T175031.png
security:
- kind: domain-security
  name: Cornerstone Domain Security
  slug: cornerstone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cornerstone
tags:
- Talent Management
- Learning Management
- Performance Management
- Recruiting
- HR
- Workforce Analytics
- Succession Planning
- Enterprise
website: https://www.cornerstoneondemand.com/
---
