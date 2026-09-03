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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Aws Batch Agentic Access
  operation_count: 24
  slug: aws-batch-agentic-access
  summary_line: 24 operations · 23 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: REST API for managing AWS Batch compute environments, job queues, job definitions, scheduling policies, consumable resources, and jobs. Operations are exposed as POST endpoints under /v1/ paths with J
  name: AWS Batch API
  slug: api
- baseURL: https://batch.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Compute Environments API from AWS Batch — 4 operation(s) for compute environments.
  name: AWS Batch Compute Environments API
  slug: aws-batch-compute-environments-api
- baseURL: https://batch.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Job Definitions API from AWS Batch — 3 operation(s) for job definitions.
  name: AWS Batch Job Definitions API
  slug: aws-batch-job-definitions-api
- baseURL: https://batch.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Job Queues API from AWS Batch — 4 operation(s) for job queues.
  name: AWS Batch Job Queues API
  slug: aws-batch-job-queues-api
- baseURL: https://batch.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Jobs API from AWS Batch — 5 operation(s) for jobs.
  name: AWS Batch Jobs API
  slug: aws-batch-jobs-api
- baseURL: https://batch.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Scheduling Policies API from AWS Batch — 5 operation(s) for scheduling policies.
  name: AWS Batch Scheduling Policies API
  slug: aws-batch-scheduling-policies-api
- baseURL: https://batch.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Tags API from AWS Batch — 1 operation(s) for tags.
  name: AWS Batch Tags API
  slug: aws-batch-tags-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Batch Compute Environments API
  slug: open-aws-batch-compute-environments-api
- collection_type: open
  name: AWS Batch Compute Environments Job Definitions API
  slug: open-aws-batch-job-definitions-api
- collection_type: open
  name: AWS Batch Compute Environments Job Queues API
  slug: open-aws-batch-job-queues-api
- collection_type: open
  name: AWS Batch Compute Environments Jobs API
  slug: open-aws-batch-jobs-api
- collection_type: open
  name: AWS Batch Compute Environments Scheduling Policies API
  slug: open-aws-batch-scheduling-policies-api
- collection_type: open
  name: AWS Batch Compute Environments Tags API
  slug: open-aws-batch-tags-api
- collection_type: open
  name: AWS Batch API
  slug: open-aws-batch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-batch-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-batch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-batch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-batch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-batch-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/batch/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/batch/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/batch/pricing/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
created: '2026-05-11'
description: AWS Batch is a fully managed batch computing service that enables developers, scientists, and engineers to run hundreds of thousands of batch and machine learning compute jobs efficiently on AWS by dynamically provisioning the optimal quantity and type of compute resources based on job volume and resource requirements. The AWS Batch API provides programmatic management of compute environments, job queues, job definitions, scheduling policies, and job submission and lifecycle operations, authenticated with AWS Signature Version 4 (SigV4).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-batch.png
layout: provider
modified: '2026-05-11'
name: AWS Batch
nav: Providers
network: true
overview: 'AWS Batch publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Compute Environments API, Job Definitions API, Job Queues API, and 3 more. Tagged areas include Batch Computing, Compute, HPC, Job Scheduling, and Containers.


  AWS Batch''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 29.4
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
    contract_quality: 47.6
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-batch/refs/heads/main/screenshots/aws-batch-2026-06-20T172748.png
security:
- kind: authentication
  name: Aws Batch Authentication
  slug: aws-batch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Batch Domain Security
  slug: aws-batch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Batch Vulnerability Disclosure
  slug: aws-batch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Batch Trust Center
  slug: aws-batch-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-batch
tags:
- Batch Computing
- Compute
- HPC
- Job Scheduling
- Containers
- Managed Service
website: https://aws.amazon.com/batch/
---
