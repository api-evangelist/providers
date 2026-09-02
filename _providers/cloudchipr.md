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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'CloudChipr publishes a developer API Reference at docs.cloudchipr.com/reference covering the same multi-cloud cost-management capabilities as the web app: connecting cloud provider accounts, viewing i'
  name: CloudChipr API
  slug: cloudchipr-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudchipr-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudchipr
- group: company
  title: ''
  type: Website
  url: https://cloudchipr.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.cloudchipr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudchipr.com/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://cloudchipr.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://cloudchipr.com/blog
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cloudchipr
- group: commercial
  title: ''
  type: FinOpsMember
  url: https://www.finops.org/members/cloudchipr/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cloudchipr.com/llms.txt
created: '2026-03-27'
description: CloudChipr is a cloud cost-management and FinOps platform that consolidates AWS, Azure, and GCP spend in a single console and automates resource cleanup, rightsizing, and cost governance. The product surface centres on dashboards, automated workflows, budget alerts, and integrations with email, Slack, Microsoft Teams, Jira, and webhooks. CloudChipr exposes an API Reference at docs.cloudchipr.com/reference for programmatic access; specific endpoints, base URL, and authentication mechanism are documented in that portal.
finops:
- name: Cloudchipr Finops
  service_category: API
  slug: cloudchipr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudchipr.png
layout: provider
modified: '2026-04-27'
name: CloudChipr
nav: Providers
network: true
overview: 'CloudChipr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Azure, Cloud Cost Management, Cost Optimization, FinOps, and GCP.


  CloudChipr''s developer surface includes developer portal, documentation, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Cloudchipr Plans Pricing
  plan_count: 3
  slug: cloudchipr-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Cloudchipr Rate Limits
  slug: cloudchipr-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 20.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudchipr/refs/heads/main/screenshots/cloudchipr-2026-06-20T174545.png
security:
- kind: domain-security
  name: Cloudchipr Domain Security
  slug: cloudchipr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudchipr
tags:
- Azure
- Cloud Cost Management
- Cost Optimization
- FinOps
- GCP
- Multi-Cloud
- Resource Cleanup
- Rightsizing
website: https://cloudchipr.com/
---
