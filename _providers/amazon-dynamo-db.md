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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Dynamo Db Agentic Access
  operation_count: 1
  slug: amazon-dynamo-db-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: Low-level HTTPS JSON API for Amazon DynamoDB that supports table management, item-level CRUD, queries, scans, transactions, global tables, streams, and backup and restore operations. Requests are POST
  name: Amazon DynamoDB API
  slug: api
- description: The Amazon DynamoDB API API from Amazon DynamoDB — 1 operation(s) for amazon dynamodb api.
  name: Amazon DynamoDB Amazon DynamoDB API API
  slug: amazon-dynamo-db-amazon-dynamodb-api-api
artifact_total: 8
collections:
- collection_type: open
  name: Amazon DynamoDB API
  slug: open-amazon-dynamo-db
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-dynamo-db-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-dynamo-db-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-dynamo-db-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-dynamo-db-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-dynamo-db-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/dynamodb/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/dynamodb/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/dynamodb/pricing/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
created: '2026-05-11'
description: Amazon DynamoDB is a fully managed NoSQL key-value and document database service from Amazon Web Services that delivers single-digit millisecond performance at any scale with built-in security, continuous backups, automated multi-region replication, in-memory caching, and data export capabilities. DynamoDB exposes a low-level HTTPS JSON API used by the AWS SDKs and CLI to perform table management, item CRUD, query, scan, transaction, and streams operations, all authenticated with AWS Signature Version 4 (SigV4).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-dynamo-db.png
layout: provider
modified: '2026-05-11'
name: Amazon DynamoDB
nav: Providers
network: true
overview: 'Amazon DynamoDB publishes 1 API on the [APIs.io](https://apis.io/) network: Amazon DynamoDB API API. Tagged areas include NoSQL, Database, Key-Value Store, Document Database, and Serverless.


  Amazon DynamoDB''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 74
score:
  band: thin
  composite: 32.8
  delta: 2.1
  facets:
    commercial_clarity: 31.6
    contract_quality: 62.7
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-dynamo-db/refs/heads/main/screenshots/amazon-dynamo-db-2026-06-20T171631.png
security:
- kind: authentication
  name: Amazon Dynamo Db Authentication
  slug: amazon-dynamo-db-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Dynamo Db Domain Security
  slug: amazon-dynamo-db-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Dynamo Db Vulnerability Disclosure
  slug: amazon-dynamo-db-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Dynamo Db Trust Center
  slug: amazon-dynamo-db-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-dynamo-db
tags:
- NoSQL
- Database
- Key-Value Store
- Document Database
- Serverless
- Managed Database
website: https://aws.amazon.com/dynamodb/
---
