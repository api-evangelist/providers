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
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aws Elastic Beanstalk Agentic Access
  operation_count: 1
  slug: aws-elastic-beanstalk-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Query API for creating and managing Elastic Beanstalk applications, versions, environments, configuration templates, and deployments. Requests are authenticated with AWS Signature Version 4 (SigV4) us
  name: AWS Elastic Beanstalk API
  slug: management-api
- description: The AWS Elastic Beanstalk API API from AWS Elastic Beanstalk — 1 operation(s) for aws elastic beanstalk api.
  name: AWS Elastic Beanstalk AWS Elastic Beanstalk API API
  slug: aws-elastic-beanstalk-aws-elastic-beanstalk-api-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Elastic Beanstalk AWS Elastic Beanstalk API API
  slug: open-aws-elastic-beanstalk-aws-elastic-beanstalk-api-api
- collection_type: open
  name: AWS Elastic Beanstalk API
  slug: open-aws-elastic-beanstalk
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-elastic-beanstalk-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-elastic-beanstalk-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-elastic-beanstalk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-elastic-beanstalk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-elastic-beanstalk-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/elasticbeanstalk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/elasticbeanstalk/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/elasticbeanstalk/pricing/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/feed/
created: '2026-05-11'
description: AWS Elastic Beanstalk is a Platform-as-a-Service offering that makes it easy to deploy, scale, and manage web applications and services developed in Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar AWS infrastructure. It automatically handles capacity provisioning, load balancing, auto-scaling, and health monitoring. The Elastic Beanstalk API and AWS SDKs provide programmatic access to applications, environments, and deployments using AWS Signature Version 4 authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-elastic-beanstalk.png
layout: provider
modified: '2026-05-11'
name: AWS Elastic Beanstalk
nav: Providers
network: true
overview: 'AWS Elastic Beanstalk publishes 1 API on the [APIs.io](https://apis.io/) network: AWS Elastic Beanstalk API API. Tagged areas include Platform-as-a-Service, Application Deployment, Auto-Scaling, Cloud, and DevOps.


  AWS Elastic Beanstalk''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-elastic-beanstalk/refs/heads/main/screenshots/aws-elastic-beanstalk-2026-06-20T172748.png
security:
- kind: authentication
  name: Aws Elastic Beanstalk Authentication
  slug: aws-elastic-beanstalk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Elastic Beanstalk Domain Security
  slug: aws-elastic-beanstalk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Elastic Beanstalk Vulnerability Disclosure
  slug: aws-elastic-beanstalk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Elastic Beanstalk Trust Center
  slug: aws-elastic-beanstalk-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-elastic-beanstalk
tags:
- Platform-as-a-Service
- Application Deployment
- Auto-Scaling
- Cloud
- DevOps
website: https://aws.amazon.com/elasticbeanstalk/
---
