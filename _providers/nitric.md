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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-03'
api_count: 11
apis:
- description: SDK resource for declaring HTTP APIs and routes in code. Nitric provisions the API gateway (e.g. AWS API Gateway, GCP API Gateway, Azure API Management) and wires routes to your handlers. This is a fr
  name: Nitric API Resource
  slug: nitric-api-resource
- description: SDK resource for declaring time-based and cron schedules in code. Nitric provisions the underlying scheduler in your target cloud and triggers your handler on the defined cadence. Framework primitive,
  name: Nitric Schedule Resource
  slug: nitric-schedule-resource
- description: SDK resource for declaring durable message queues for batch and deferred processing. Nitric maps it to a cloud queue service (e.g. AWS SQS) with enqueue and dequeue semantics. Framework primitive, not
  name: Nitric Queue Resource
  slug: nitric-queue-resource
- description: SDK resource for declaring publish/subscribe topics for event-driven architectures. Nitric provisions the cloud pub/sub service (e.g. AWS SNS, GCP Pub/Sub) and wires subscribers to handlers. Framework
  name: Nitric Topic Resource
  slug: nitric-topic-resource
- description: SDK resource for declaring object/file storage buckets with read, write, delete, signed URLs, and bucket-event triggers. Nitric maps it to cloud storage (e.g. AWS S3, GCS, Azure Blob). Framework primi
  name: Nitric Bucket Resource
  slug: nitric-bucket-resource
- description: SDK resource for declaring key-value stores with get, set, delete, and query operations. Nitric maps it to a cloud key-value service (e.g. AWS DynamoDB). Framework primitive, not a hosted API.
  name: Nitric Key-Value Resource
  slug: nitric-keyvalue-resource
- description: SDK resource for declaring and accessing secrets with versioning. Nitric maps it to a cloud secrets manager (e.g. AWS Secrets Manager). Framework primitive, not a hosted API.
  name: Nitric Secret Resource
  slug: nitric-secret-resource
- description: SDK resource for declaring realtime bidirectional websocket endpoints with connect, disconnect, and message handlers. Nitric provisions the cloud websocket service. Framework primitive, not a hosted A
  name: Nitric Websocket Resource
  slug: nitric-websocket-resource
- description: SDK resource for declaring managed relational (Postgres) databases with migrations. Nitric provisions the cloud database (e.g. AWS RDS, GCP Cloud SQL). Framework primitive, not a hosted API.
  name: Nitric SQL Database Resource
  slug: nitric-sql-resource
- description: The Nitric command-line tool (nitric new, nitric start, nitric stack new, nitric up, nitric down) that scaffolds projects, runs local emulation with a dashboard, and deploys or tears down infrastructu
  name: Nitric CLI
  slug: nitric-cli
- description: Pluggable provider implementations that translate declared Nitric resources into cloud infrastructure on AWS, Google Cloud, or Azure using Pulumi (direct deploy) or Terraform (generated config). Custo
  name: Nitric Provider Plugins
  slug: nitric-provider-plugins
artifact_total: 16
collections:
- collection_type: open
  name: Nitric Framework
  slug: open-nitric
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nitric-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nitrictech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nitric
- group: company
  title: ''
  type: Website
  url: https://nitric.io/
- group: docs
  title: ''
  type: Documentation
  url: https://nitric.io/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/nitric-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nitric-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nitric-finops.yml
created: '2026-06-20'
description: Nitric is an open-source cloud framework and infrastructure-from-code SDK plus CLI for building cloud applications in TypeScript, Python, Go, or Dart. You declare resources - APIs, schedules, queues, topics, buckets, key-value stores, secrets, and websockets - directly in your application code, and Nitric provisions them across AWS, Google Cloud, or Azure via pluggable Pulumi or Terraform providers. Nitric is a framework / IaC tool, not a hosted REST API - the APIs you build are deployed to your own cloud.
finops:
- name: Nitric Finops
  service_category: Developer Tools and Infrastructure
  slug: nitric-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nitric.png
layout: provider
modified: '2026-06-20'
name: Nitric
nav: Providers
network: true
overview: 'Nitric publishes 11 APIs on the [APIs.io](https://apis.io/) network, including API Resource, Schedule Resource, Queue Resource, and 8 more. Tagged areas include Infrastructure from Code, Cloud Framework, SDK, CLI, and Serverless.


  Nitric''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Nitric Plans Pricing
  plan_count: 2
  slug: nitric-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 2
  name: Nitric Rate Limits
  slug: nitric-rate-limits
score:
  band: emerging
  composite: 26.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 26.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nitric/refs/heads/main/screenshots/nitric-2026-06-20T190332.png
security:
- kind: domain-security
  name: Nitric Domain Security
  slug: nitric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nitric
tags:
- Infrastructure from Code
- Cloud Framework
- SDK
- CLI
- Serverless
- Multi-Cloud
website: https://nitric.io/
---
