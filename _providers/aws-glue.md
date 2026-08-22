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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aws Glue Agentic Access
  operation_count: 1
  slug: aws-glue-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The AWS Glue API API from AWS Glue — 1 operation(s) for aws glue api.
  name: AWS Glue AWS Glue API API
  slug: aws-glue-aws-glue-api-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Glue AWS Glue API API
  slug: open-aws-glue-aws-glue-api-api
- collection_type: open
  name: AWS Glue API
  slug: open-aws-glue
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-glue-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-glue-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-glue-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-glue-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-glue-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/glue/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/glue/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/glue/latest/webapi/WebAPI_Welcome.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/glue/pricing/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html
- group: other
  title: ''
  type: Endpoints
  url: https://docs.aws.amazon.com/general/latest/gr/glue.html
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/glue/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/feed/
created: '2026-05-11'
description: AWS Glue is a fully managed serverless extract, transform, and load (ETL) service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development. It provides a central data catalog, crawlers for automated metadata discovery, visual and code-based job authoring, and data quality capabilities. The Glue API uses AWS Signature Version 4 (SigV4) authentication and is accessed via SDKs, the AWS CLI, or direct HTTPS calls to regional service endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-glue.png
layout: provider
modified: '2026-05-11'
name: AWS Glue
nav: Providers
network: true
overview: 'AWS Glue publishes 1 API on the [APIs.io](https://apis.io/) network: AWS Glue API API. Tagged areas include Data, Data Catalog, ETL, Analytics, and Serverless.


  AWS Glue''s developer surface includes authentication, documentation, API reference, pricing, CLI, support, engineering blog, and 10 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 36.9
  delta: -0.4
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 55.9
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-glue/refs/heads/main/screenshots/aws-glue-2026-06-20T172756.png
security:
- kind: authentication
  name: Aws Glue Authentication
  slug: aws-glue-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Glue Domain Security
  slug: aws-glue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Glue Vulnerability Disclosure
  slug: aws-glue-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Glue Trust Center
  slug: aws-glue-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-glue
tags:
- Data
- Data Catalog
- ETL
- Analytics
- Serverless
website: https://aws.amazon.com/glue/
---
