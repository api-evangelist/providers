---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Densify Agentic Access
  operation_count: 10
  slug: densify-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 7
apis:
- description: The Densify Public Cloud REST API exposes optimization analysis, recommendations, account and instance inventory, and systems data for AWS, Azure, and Google Cloud environments. The API uses JSON over
  name: Densify Public Cloud API
  slug: public-cloud-api
- description: The Densify Container Optimization REST API provides programmatic access to container right-sizing recommendations across Amazon EKS, AKS, GKE, OpenShift, and self-managed Kubernetes footprints. It ex
  name: Densify Container Optimization API
  slug: container-api
- description: The Authentication API from Densify — 1 operation(s) for authentication.
  name: Densify Authentication API
  slug: densify-authentication-api
- description: The Cloud Analysis API from Densify — 3 operation(s) for cloud analysis.
  name: Densify Cloud Analysis API
  slug: densify-cloud-analysis-api
- description: The Kubernetes API from Densify — 2 operation(s) for kubernetes.
  name: Densify Kubernetes API
  slug: densify-kubernetes-api
- description: The Recommendations API from Densify — 3 operation(s) for recommendations.
  name: Densify Recommendations API
  slug: densify-recommendations-api
- description: The System API from Densify — 1 operation(s) for system.
  name: Densify System API
  slug: densify-system-api
artifact_total: 16
collections:
- collection_type: open
  name: Densify / Kubex Public Cloud API
  slug: open-densify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/densify-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/densify-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/densify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/densify-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/densify
- group: company
  title: ''
  type: Website
  url: https://www.densify.com
- group: start
  title: ''
  type: Portal
  url: https://portal.densify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.densify.com
- group: other
  title: ''
  type: Developer Resources
  url: https://www.densify.com/dev
- group: docs
  title: ''
  type: Documentation Landing
  url: https://portal.densify.com/docs-landing/
- group: other
  title: ''
  type: Resources
  url: https://www.densify.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.densify.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.densify.com/pricing
- group: start
  title: ''
  type: Free Trial
  url: https://www.densify.com/free-trial
- group: operate
  title: ''
  type: Support
  url: https://www.densify.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/densify-dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.densify.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.densify.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.densify.com/contact
- group: design
  title: ''
  type: JSONLD
  url: json-ld/densify-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/densify-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/densify-capabilities.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://api.densify.com/llms.txt
created: '2026-03-16'
description: Densify (now Kubex) provides a machine learning powered cloud and container optimization platform that continuously right-sizes resources to reduce cost and improve performance across Kubernetes, public cloud, and virtualized environments. The Densify REST API exposes optimization analysis, recommendations, account and cluster inventory, and systems data so that optimization can be embedded into CI/CD pipelines, infrastructure as code templates, and FinOps workflows.
finops:
- name: Densify Finops
  service_category: API
  slug: densify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/densify.png
jsonld:
- class_count: 0
  name: Densify Context
  property_count: 6
  slug: densify-context
layout: provider
modified: '2026-04-28'
name: Densify
nav: Providers
network: true
overview: 'Densify publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Public Cloud API, Authentication API, Cloud Analysis API, and 3 more. Tagged areas include Cloud Cost, Container Optimization, FinOps, Kubernetes, and Machine Learning.


  The Densify catalog on APIs.io includes 1 JSON-LD context.


  Densify''s developer surface includes authentication, developer portal, documentation, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Densify Plans Pricing
  plan_count: 3
  slug: densify-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 5
  name: Densify Rate Limits
  slug: densify-rate-limits
score:
  band: developing
  composite: 52.1
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 63.7
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/densify/refs/heads/main/screenshots/densify-2026-06-20T175916.png
security:
- kind: authentication
  name: Densify Authentication
  slug: densify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Densify Domain Security
  slug: densify-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Densify Trust Center
  slug: densify-trust-center
  summary_line: SOC 2, ISO 27001
slug: densify
tags:
- Cloud Cost
- Container Optimization
- FinOps
- Kubernetes
- Machine Learning
- Recommendations
- Right-Sizing
website: https://www.densify.com
---
