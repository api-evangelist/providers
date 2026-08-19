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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: GraphQL API for programmatic access to Labelbox platform resources including datasets, projects, labels, ontologies, and model evaluation workflows. Labelbox recommends using the Python SDK as a wrapp
  name: Labelbox GraphQL API
  slug: labelbox-graphql-api
- description: REST API providing access to Labelbox platform resources. Available at https://api.labelbox.com/api/v1, this endpoint complements the GraphQL API for operations that benefit from RESTful conventions.
  name: Labelbox REST API
  slug: labelbox-rest-api
artifact_total: 10
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Labelbox/labelbox-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Labelbox/labelbox-python/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Labelbox/labelbox-python/blob/develop/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Labelbox/labelbox-python/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Labelbox/labelbox-python/blob/develop/LICENSE
- group: auth
  title: ''
  type: TrustCenter
  url: security/labelbox-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/labelbox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/labelbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://labelbox.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.labelbox.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Labelbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/labelbox
- group: other
  title: ''
  type: X
  url: https://x.com/labelbox
- group: company
  title: ''
  type: Blog
  url: https://labelbox.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://labelbox.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.labelbox.com
- group: docs
  title: ''
  type: PythonSDKDocumentation
  url: https://labelbox-python.readthedocs.io/en/latest/
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/labelbox/
- group: commercial
  title: ''
  type: Plans
  url: plans/labelbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/labelbox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/labelbox-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/labelbox-context.jsonld
created: 2026-06-12
description: 'Labelbox is an enterprise-grade data labeling and AI training data platform that enables teams to build, manage, and evaluate machine learning models. The platform provides a REST API and a GraphQL API (endpoint: https://api.labelbox.com/graphql) for programmatic access to datasets, annotation projects, labels, ontologies, and model evaluation workflows. Labelbox strongly recommends using its official Python SDK rather than querying the GraphQL API directly, as GraphQL endpoints may change without notice. The platform also supports JavaScript/TypeScript through a Node.js SDK and offers notebook-based examples via its GitHub organization.'
finops:
- name: Labelbox Finops
  service_category: ''
  slug: labelbox-finops
graphqls:
- description: The Labelbox GraphQL API provides programmatic access to the full range of Labelbox platform resources, including projects, datasets, data rows, labels, ontologies, model runs, and annotation imports.
  name: Labelbox GraphQL API
  slug: labelbox-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/labelbox.png
jsonld:
- class_count: 0
  name: Labelbox Context
  property_count: 29
  slug: labelbox-context
layout: provider
modified: 2026-06-12
name: Labelbox
nav: Providers
network: true
overview: 'Labelbox publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Labeling, AI Training, Machine Learning, Annotation, and Computer Vision.


  The Labelbox catalog on APIs.io includes 1 JSON-LD context.


  Labelbox''s developer surface includes documentation, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Labelbox Plans Pricing
  plan_count: 2
  slug: labelbox-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 2
  name: Labelbox Rate Limits
  slug: labelbox-rate-limits
score:
  band: thin
  composite: 37.1
  delta: -3.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 47.8
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 65.8
  previous_composite: 40.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/labelbox/refs/heads/main/screenshots/labelbox-2026-06-20T184245.png
security:
- kind: domain-security
  name: Labelbox Domain Security
  slug: labelbox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Labelbox Vulnerability Disclosure
  slug: labelbox-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Labelbox Trust Center
  slug: labelbox-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: labelbox
tags:
- Data Labeling
- AI Training
- Machine Learning
- Annotation
- Computer Vision
- RLHF
- Model Evaluation
- Dataset Management
- GraphQL
- Python SDK
website: https://labelbox.com
---
