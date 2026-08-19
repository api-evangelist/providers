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
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 7
apis:
- description: The Cloudability v3 API is the modern REST interface for the platform. It exposes resource-oriented endpoints for reporting, dimensions and metrics, business mappings, anomalies, rightsizing recommend
  name: Cloudability API v3
  slug: api-v3
- description: The legacy v1 API remains available for older integrations covering cost reporting and dimensions. Apptio recommends migrating to v3 for new integrations. v1 uses an api_key query parameter for authen
  name: Cloudability API v1 (Legacy)
  slug: api-v1
- description: The Reporting endpoints under v3 build cost-and-usage queries against Cloudability's normalized billing dataset. Callers select metrics (unblended cost, amortized cost, usage_quantity), dimensions (ve
  name: Cloudability Reporting API
  slug: reporting
- description: 'Business Mappings define rule-based dimensions that allocate spend to cost centers, products, environments, or applications. The API lets callers list, create, update and delete mappings, manage rule '
  name: Cloudability Business Mappings API
  slug: business-mappings
- description: The Rightsizing API surfaces machine-learning generated downsizing, modernization and termination recommendations for AWS EC2, RDS, EBS, Azure VMs and disks, and Google Compute Engine instances, inclu
  name: Cloudability Rightsizing Recommendations API
  slug: rightsizing
- description: The Anomalies API exposes detected cost anomalies on dimensions such as service, account, and business mapping. Callers can query open anomalies, retrieve baseline / actual cost deltas, classify anoma
  name: Cloudability Anomaly Detection API
  slug: anomalies
- description: The Vendor Credentials API manages connections to AWS payer accounts, Azure billing scopes, GCP billing projects, OCI tenancies and other cloud vendors. It supports listing existing credentials, valid
  name: Cloudability Vendor Credentials API
  slug: vendor-credentials
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudability-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apptio.com/products/cloudability/
- group: start
  title: ''
  type: Portal
  url: https://www.ibm.com/products/cloudability
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudability
- group: learn
  title: ''
  type: Training
  url: https://education.apptio.com/courses/ibm-cloudability-api
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudability-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudability-rules.yml
created: '2026-03-27'
description: Cloudability (an IBM Apptio product) is a cloud cost management and FinOps platform providing cost visibility, optimization recommendations, anomaly detection, and governance across AWS, Azure, Google Cloud, and other multi-cloud environments. The Cloudability API v3 is REST-oriented with JSON responses, HTTP basic authentication using an API token, cursor-style limit/offset pagination, and operations for reporting, business mappings, rightsizing recommendations, anomalies, vendor credentials, and views.
finops:
- name: Cloudability Finops
  service_category: API
  slug: cloudability-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudability.png
jsonld:
- class_count: 0
  name: Cloudability Context
  property_count: 7
  slug: cloudability-context
layout: provider
modified: '2026-04-23'
name: Cloudability
nav: Providers
network: true
overview: 'Cloudability publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Cost Management, Cost Optimization, FinOps, Multi-Cloud, and Recommendations.


  The Cloudability catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudability''s developer surface includes developer portal, documentation, GitHub presence, training material, and 4 more developer resources.'
plans:
- name: Cloudability Plans Pricing
  plan_count: 3
  slug: cloudability-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 5
  name: Cloudability Rate Limits
  slug: cloudability-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Cloudability API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 6
  slug: cloudability-rules
score:
  band: emerging
  composite: 24.4
  delta: 3.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 54.5
    contract_quality: 7.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 54.5
    operational_transparency: 13.2
  previous_composite: 21.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudability/refs/heads/main/screenshots/cloudability-2026-06-20T174542.png
security:
- kind: domain-security
  name: Cloudability Domain Security
  slug: cloudability-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cloudability
tags:
- Cloud Cost Management
- Cost Optimization
- FinOps
- Multi-Cloud
- Recommendations
- Reporting
website: https://www.apptio.com/products/cloudability/
---
