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
  scored_at: '2026-09-03'
api_count: 7
apis:
- description: Unified SaaS and Cloud FinOps platform offering app discovery, subscription management, user lifecycle automation, contract and renewal tracking, license optimization, chargeback, and policy-based gov
  name: CloudNuro SaaS Management Platform
  slug: cloudnuro-platform
- description: Dedicated management module for Microsoft 365 environments including license, group, and policy oversight.
  name: CloudNuro Microsoft 365 Custodian
  slug: cloudnuro-microsoft365-custodian
- description: Salesforce-specific governance, license optimization, and access control.
  name: CloudNuro Salesforce Custodian
  slug: cloudnuro-salesforce-custodian
- description: ServiceNow application management and license oversight.
  name: CloudNuro ServiceNow Custodian
  slug: cloudnuro-servicenow-custodian
- description: Cross-platform SaaS, PaaS, and IaaS management for AWS, Azure, GCP, and OCI under a single FinOps view.
  name: CloudNuro Unified Cloud Custodian
  slug: cloudnuro-unified-cloud-custodian
- description: AI workload oversight, governance, and cost allocation for enterprise AI usage.
  name: CloudNuro AI Custodian
  slug: cloudnuro-ai-custodian
- description: Financial accountability and SaaS/cloud cost allocation across departments and cost centers.
  name: CloudNuro Chargeback
  slug: cloudnuro-chargeback
artifact_total: 13
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudnuro-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudnuro-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudnuro
- group: company
  title: ''
  type: Website
  url: https://www.cloudnuro.ai
- group: other
  title: ''
  type: Product Overview
  url: https://www.cloudnuro.ai/product-overview
- group: company
  title: ''
  type: Blog
  url: https://www.cloudnuro.ai/blog
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.microsoft.com/en-us/product/web-apps/cloudnurocorp1684298468280.cloudnuro
- group: operate
  title: ''
  type: Contact
  url: https://www.cloudnuro.ai/contact-us
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudnuro-context.jsonld
created: '2026-03-27'
description: CloudNuro is an enterprise SaaS management and FinOps platform that combines SaaS discovery (shadow IT), SaaS subscription and license optimization, user lifecycle and compliance management, SaaS-Chargeback and cost allocation, and Cloud FinOps for AWS, Azure, GCP, and OCI. It offers 400+ pre-built connectors to leading SaaS, IaaS, IAM, ITSM, HR, and security platforms. CloudNuro is SOC 2 Type II certified and has been recognized by Gartner in the SaaS Management Platforms market guide.
finops:
- name: Cloudnuro Finops
  service_category: API
  slug: cloudnuro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudnuro.png
jsonld:
- class_count: 0
  name: Cloudnuro Context
  property_count: 5
  slug: cloudnuro-context
layout: provider
modified: '2026-04-26'
name: CloudNuro
nav: Providers
network: true
overview: 'CloudNuro publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud FinOps, Compliance, Cost Optimization, License Management, and SaaS Management.


  The CloudNuro catalog on APIs.io includes 1 JSON-LD context.


  CloudNuro''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Cloudnuro Plans Pricing
  plan_count: 3
  slug: cloudnuro-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Cloudnuro Rate Limits
  slug: cloudnuro-rate-limits
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 16.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudnuro/refs/heads/main/screenshots/cloudnuro-2026-06-20T174615.png
security:
- kind: domain-security
  name: Cloudnuro Domain Security
  slug: cloudnuro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: trust-center
  name: Cloudnuro Trust Center
  slug: cloudnuro-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR, CSA STAR
slug: cloudnuro
tags:
- Cloud FinOps
- Compliance
- Cost Optimization
- License Management
- SaaS Management
- Shadow IT
- SSPM
website: https://www.cloudnuro.ai
---
