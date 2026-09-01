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
- description: Vertice Cloud Cost Optimization integrates with AWS, GCP, and Azure accounts to provide cloud visibility, cost analytics, and optimization recommendations. The integration uses cross-account IAM roles
  name: Vertice Cloud Cost Optimization API
  slug: cloud-cost-optimization-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vertice-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vertice-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verticeone
- group: company
  title: ''
  type: Website
  url: https://www.vertice.one/
- group: operate
  title: ''
  type: Support
  url: https://help.vertice.one/hc/en-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vertice.one/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.vertice.one/blog
- group: company
  title: ''
  type: Partners
  url: https://www.vertice.one/partners
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VerticeOne
- group: other
  title: ''
  type: TerraformModule
  url: https://github.com/VerticeOne/terraform-aws-vertice-integration
- group: other
  title: ''
  type: CloudFormationTemplate
  url: https://github.com/VerticeOne/cloudformation-aws-vertice-cco-integration
- group: build
  title: ''
  type: CloudIntegration
  url: https://www.vertice.one/platform/cloud-cost-optimization
- group: other
  title: ''
  type: Dashboard
  url: https://app.vertice.one/
created: '2026-05-03'
description: Vertice is an intelligent procurement platform built for the modern enterprise with agentic workflows, AI insights, and expert buyers that empower finance and procurement teams across 30+ countries to buy smarter and scale faster. The platform covers SaaS purchasing and contract management, cloud spend optimization (AWS, GCP, Azure), and integrates with ERPs, CLMs, ticketing platforms, communication tools, TPRM systems, and SSOs to centralize procurement workflows. Vertice processes over $30B in spend with proven 20%+ savings for customers including ARM, Blackberry, Factorial, and Santander.
finops:
- name: Vertice Finops
  service_category: API
  slug: vertice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vertice.png
layout: provider
modified: '2026-07-25'
name: Vertice
nav: Providers
network: true
overview: 'Vertice publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Cost Optimization, Contract Management, Procurement, SaaS Management, and Spend Management.


  Vertice''s developer surface includes support, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Vertice Plans Pricing
  plan_count: 3
  slug: vertice-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Vertice Rate Limits
  slug: vertice-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Vertice Domain Security
  slug: vertice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Vertice Trust Center
  slug: vertice-trust-center
  summary_line: SOC 2, ISO 27001
slug: vertice
tags:
- Cloud Cost Optimization
- Contract Management
- Procurement
- SaaS Management
- Spend Management
website: https://www.vertice.one/
---
