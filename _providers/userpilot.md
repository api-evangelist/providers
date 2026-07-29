---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Userpilot Agentic Access
  operation_count: 23
  slug: userpilot-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 6
apis:
- description: The Analytics API from Userpilot — 15 operation(s) for analytics.
  name: Userpilot Analytics API
  slug: userpilot-analytics-api
- description: The Background Jobs API from Userpilot — 2 operation(s) for background jobs.
  name: Userpilot Background Jobs API
  slug: userpilot-background-jobs-api
- description: The Companies API from Userpilot — 2 operation(s) for companies.
  name: Userpilot Companies API
  slug: userpilot-companies-api
- description: The Imports API from Userpilot — 1 operation(s) for imports.
  name: Userpilot Imports API
  slug: userpilot-imports-api
- description: The Real-time API from Userpilot — 2 operation(s) for real-time.
  name: Userpilot Real-time API
  slug: userpilot-real-time-api
- description: The Track API from Userpilot — 1 operation(s) for track.
  name: Userpilot Track API
  slug: userpilot-track-api
artifact_total: 36
collections:
- collection_type: open
  name: Userpilot API
  slug: open-userpilot-analytex
- collection_type: open
  name: Userpilot API
  slug: open-userpilot-appex
- collection_type: open
  name: Userpilot API
  slug: open-userpilot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/userpilot-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/userpilot-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/userpilot-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Userpilot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teamuserpilot
- group: company
  title: ''
  type: Website
  url: https://userpilot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.userpilot.com/api-references/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/userpilot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/userpilot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/userpilot-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.userpilot.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://userpilot.com/blog/
created: '2026-05-08'
description: Userpilot is a product growth platform for in-app onboarding, user engagement, surveys, and product analytics — without code.
examples:
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupsbanners Example
  slug: userpilot-get-apiv1analyticsexportslookupsbanners-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupschecklists Example
  slug: userpilot-get-apiv1analyticsexportslookupschecklists-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupscompany Properties Example
  slug: userpilot-get-apiv1analyticsexportslookupscompany-properties-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupsembeds Example
  slug: userpilot-get-apiv1analyticsexportslookupsembeds-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupsevents Properties Example
  slug: userpilot-get-apiv1analyticsexportslookupsevents-properties-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupsfeatures Events Example
  slug: userpilot-get-apiv1analyticsexportslookupsfeatures-events-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupsflows Example
  slug: userpilot-get-apiv1analyticsexportslookupsflows-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupsresource Center Modules Example
  slug: userpilot-get-apiv1analyticsexportslookupsresource-center-modules-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupssegments Example
  slug: userpilot-get-apiv1analyticsexportslookupssegments-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupsspotlights Example
  slug: userpilot-get-apiv1analyticsexportslookupsspotlights-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupssurveys Example
  slug: userpilot-get-apiv1analyticsexportslookupssurveys-example
- key_count: 6
  name: Userpilot Get Apiv1Analyticsexportslookupsuser Properties Example
  slug: userpilot-get-apiv1analyticsexportslookupsuser-properties-example
- key_count: 6
  name: Userpilot Post V1Companiesbulk Identify Example
  slug: userpilot-post-v1companiesbulk-identify-example
- key_count: 6
  name: Userpilot Post V1Companiesidentify Example
  slug: userpilot-post-v1companiesidentify-example
- key_count: 6
  name: Userpilot Post V1Imports Example
  slug: userpilot-post-v1imports-example
- key_count: 6
  name: Userpilot Post V1Track Example
  slug: userpilot-post-v1track-example
- key_count: 6
  name: Userpilot Post V1Usersbulk Identify Example
  slug: userpilot-post-v1usersbulk-identify-example
finops:
- name: Userpilot Finops
  service_category: Product
  slug: userpilot-finops
graphqls:
- description: This GraphQL schema provides a conceptual representation of the Userpilot product growth platform. Userpilot enables teams to build in-app onboarding experiences, product tours, checklists, surveys, a
  name: Userpilot GraphQL Schema
  slug: userpilot-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/userpilot.png
json_schemas:
- name: ErrorResponse
  property_count: 1
  slug: userpilot-errorresponse
json_structures:
- name: Userpilot Structure
  property_count: 0
  slug: userpilot-structure
layout: provider
modified: '2026-05-19'
name: Userpilot
nav: Providers
network: true
overview: 'Userpilot publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Background Jobs API, Companies API, and 3 more. Tagged areas include Product, Onboarding, In-App Guidance, Analytics, and Customer Success.


  The Userpilot catalog on APIs.io includes 1 Spectral governance ruleset.


  Userpilot''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Userpilot Plans Pricing
  plan_count: 1
  slug: userpilot-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Userpilot Rate Limits
  slug: userpilot-rate-limits
rules:
- name: Userpilot API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: userpilot-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.3
  delta: -1.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 55.4
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/userpilot/refs/heads/main/screenshots/userpilot-2026-06-20T200701.png
security:
- kind: domain-security
  name: Userpilot Domain Security
  slug: userpilot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Userpilot Trust Center
  slug: userpilot-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: userpilot
tags:
- Product
- Onboarding
- In-App Guidance
- Analytics
- Customer Success
website: https://userpilot.com/
---
