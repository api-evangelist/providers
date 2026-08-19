---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The CloudHealth Platform REST API programmatically retrieves and manages data from the CloudHealth Platform — AWS/Azure/GCP accounts, assets, perspectives, billing rules, metrics, OLAP reports, polici
  name: CloudHealth Platform API
  slug: cloudhealth-platform-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudhealth-technologies-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.cloudhealthtech.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.cloudhealthtech.com/
- group: company
  title: ''
  type: Website
  url: https://www.broadcom.com/products/software/finops/cloudhealth
- group: commercial
  title: ''
  type: Pricing
  url: https://www.broadcom.com/products/software/finops/cloudhealth
- group: start
  title: ''
  type: GettingStarted
  url: https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/tnz-cloudhealth/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloudHealth
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudhealth-technologies-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudhealth-technologies-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudhealth-technologies-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudhealth-technologies-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudhealth-technologies-llms.txt
created: '2026-07-17'
description: 'CloudHealth Technologies is a cloud financial management (FinOps) and multi-cloud governance platform, founded in Boston and backed by Kleiner Perkins before being acquired by VMware in 2018 and now sold as CloudHealth by Broadcom. The platform helps organizations analyze and optimize cloud cost, usage, security, and governance across AWS, Microsoft Azure, and Google Cloud. It exposes a public developer surface: a REST API (organized around resource-oriented URLs, JSON responses, and standard HTTP status codes) and a GraphQL API for programmatically retrieving and managing accounts, assets, perspectives, billing rules, metrics, reporting (OLAP reports), policies, tagging, SSO, and partner/organization administration. Authentication is via a per-user API Key presented as a bearer token or api_key query parameter, enforcing the same role and organization scoping as the platform UI.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudhealth-technologies.png
layout: provider
modified: '2026-07-18'
name: CloudHealth Technologies
nav: Providers
network: true
overview: 'CloudHealth Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Cloud Cost Management, FinOps, and Cloud Governance.


  CloudHealth Technologies'' developer surface includes documentation, API reference, pricing, getting-started guide, authentication, and 7 more developer resources.'
random_paper: 110
score:
  band: emerging
  composite: 18.5
  delta: 0.7
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 17.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudhealth-technologies/refs/heads/main/screenshots/cloudhealth-technologies-2026-07-25T205700.png
security:
- kind: authentication
  name: Cloudhealth Technologies Authentication
  slug: cloudhealth-technologies-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cloudhealth Technologies Domain Security
  slug: cloudhealth-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cloudhealth-technologies
tags:
- Company
- Enterprise
- Cloud Cost Management
- FinOps
- Cloud Governance
- Multi-Cloud
- Cloud Management Platform
website: https://www.broadcom.com/products/software/finops/cloudhealth
---
