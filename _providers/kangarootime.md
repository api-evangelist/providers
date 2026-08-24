---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.4
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://kangarootime.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.kangarootime.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://help.kangarootime.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://kangarootime.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kangarootime.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.kangarootime.com/hc/en-us/sections/42065337030932-Release-Notes
- group: start
  title: ''
  type: Login
  url: https://k2.kangarootime.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kangarootime.com/kangarootime-end-user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kangarootime.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kangarootime1
- group: design
  title: ''
  type: DataModel
  url: data-model/kangarootime-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kangarootime-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kangarootime-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kangarootime-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kangarootime-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kangarootime-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kangarootime-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kangarootime-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kangarootime-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Kangarootime runs no developer program at all - api., developer. and docs. subdomains are NXDOMAIN, the 311-URL sitemap contains no developer or API page, the help centre returns zero articles for "webhook", and six package registries return zero results; its only originating integration surface is Data Feeds, a daily bulk file export to a customer-owned S3/Azure/GCS bucket configured inside the app rather than any callable API.
  evidence:
  - status: 404
    url: https://kangarootime.com/openapi.json
  - status: 404
    url: https://kangarootime.com/.well-known/api-catalog
  - status: 404
    url: https://kangarootime.com/pricing
  - status: 200
    url: https://data-feed.kangarootime.com/
  - status: 200
    url: https://help.kangarootime.com/hc/en-us/articles/45717303390356-Kangarootime-Data-Feed-User-Guide
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: Kangarootime is a cloud-based childcare and early-education management platform for single-site and multi-location centers, franchises and after-school programs. The product covers enrollment and lead management, family and staff records, classroom and rooming, attendance and check-in/out kiosks, curriculum and lesson planning, parent communication, tuition billing, subsidy administration and integrated payment processing, plus reporting dashboards (Insights) and an educator training LMS. Kangarootime publishes no public REST, GraphQL or SOAP API and runs no developer program; its customer-facing data integration surface is "Data Feeds", a configurable daily bulk export of the platform's 63-table dimensional warehouse schema to a customer-owned AWS S3, Azure Blob or Google Cloud Storage bucket in CSV, JSON/NDJSON, Parquet or XLSX, with the table and domain-model reference published openly at data-feed.kangarootime.com.
image: https://kangarootime.com/wp-content/uploads/2023/03/kangarootime_vector_color_logo.svg
layout: provider
modified: '2026-08-23'
name: Kangarootime
nav: Providers
network: true
overview: 'Kangarootime is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Childcare, Early Childhood Education, Education, and Child Care Management.


  Kangarootime''s developer surface includes documentation, support, engineering blog, changelog, and 15 more developer resources.'
plans:
- name: Kangarootime Plans Pricing
  plan_count: 0
  slug: kangarootime-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Kangarootime Rate Limits
  slug: kangarootime-rate-limits
score:
  band: emerging
  composite: 23.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 36.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: domain-security
  name: Kangarootime Domain Security
  slug: kangarootime-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kangarootime
tags:
- Company
- Childcare
- Early Childhood Education
- Education
- Child Care Management
- Enrollment
- Billing
- Payments
- Attendance
- Parent Communication
- Staff Management
- Business Intelligence
- Data Feeds
- SaaS
website: https://kangarootime.com/
---
