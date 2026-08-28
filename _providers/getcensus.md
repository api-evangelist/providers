---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Census Management REST API allows developers to programmatically manage syncs, connections, models, segments, and destinations within Census workspaces and organizations. Supports both workspace-l
  name: Census Management API
  slug: census-management-api
artifact_total: 8
asyncapis:
- description: ''
  name: Getcensus Sync Lifecycle Webhooks
  slug: getcensus-sync-lifecycle-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/getcensus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getcensus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getcensus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fivetran.com/docs/activations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sutrolabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getcensus
- group: company
  title: ''
  type: Blog
  url: https://www.getcensus.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fivetran.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getcensus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/getcensus
- group: commercial
  title: ''
  type: Plans
  url: plans/getcensus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/getcensus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/getcensus-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://whatsnew.getcensus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/getcensus-changelog.yml
- group: other
  title: ''
  type: Terraform
  url: https://fivetran.com/docs/activations/rest-api/terraform
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fivetran.com/docs/activations/rest-api
- group: docs
  title: ''
  type: APIReference
  url: https://fivetran.com/docs/activations/rest-api/api-reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://support.fivetran.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.getcensus.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fivetran.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fivetran.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/getcensus/workspace/census-api/overview
- group: auth
  title: ''
  type: Compliance
  url: https://www.fivetran.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/getcensus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/getcensus-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/getcensus-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/getcensus-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/getcensus-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/getcensus-sync-lifecycle-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/getcensus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/getcensus-packages.yml
- group: design
  title: ''
  type: Components
  url: components/getcensus-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getcensus-llms.txt
created: '2026-06-13'
description: Census (now Fivetran Activations) is a reverse ETL platform that syncs data from data warehouses to CRM, marketing, advertising, and other business destinations. It enables data teams to define SQL-based models and segments, then automatically activate that data to over 200 destinations including Salesforce, HubSpot, Facebook Ads, and Google Ads without writing custom integrations.
finops:
- name: Getcensus Finops
  service_category: ''
  slug: getcensus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getcensus.png
layout: provider
modified: '2026-08-13'
name: Census
nav: Providers
network: true
overview: 'Census publishes 1 API on the [APIs.io](https://apis.io/) network: Management API. Tagged areas include Reverse ETL, Data Activation, Data Warehouse, CRM, and Marketing Automation.


  The Census catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Census'' developer surface includes documentation, engineering blog, pricing, changelog, API reference, support, signup flow, and 27 more developer resources.'
plans:
- name: Getcensus Plans Pricing
  plan_count: 4
  slug: getcensus-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Getcensus Rate Limits
  slug: getcensus-rate-limits
score:
  band: strong
  composite: 56.1
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 52.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 56.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getcensus/refs/heads/main/screenshots/getcensus-2026-06-20T181807.png
security:
- kind: authentication
  name: Getcensus Authentication
  slug: getcensus-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Getcensus Domain Security
  slug: getcensus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getcensus Trust Center
  slug: getcensus-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: getcensus
tags:
- Reverse ETL
- Data Activation
- Data Warehouse
- CRM
- Marketing Automation
- Segments
- Syncs
- SQL
website: https://www.getcensus.com/
---
