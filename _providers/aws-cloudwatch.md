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
  name: Aws Cloudwatch Agentic Access
  operation_count: 1
  slug: aws-cloudwatch-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Query API for publishing and retrieving metrics, managing alarms, and configuring dashboards in Amazon CloudWatch. Requests are authenticated with AWS Signature Version 4 (SigV4) using AWS access keys
  name: Amazon CloudWatch API
  slug: monitoring-api
- description: The Amazon CloudWatch API API from Amazon CloudWatch — 1 operation(s) for amazon cloudwatch api.
  name: Amazon CloudWatch Amazon CloudWatch API API
  slug: aws-cloudwatch-amazon-cloudwatch-api-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon CloudWatch Amazon CloudWatch API API
  slug: open-aws-cloudwatch-amazon-cloudwatch-api-api
- collection_type: open
  name: Amazon CloudWatch API
  slug: open-aws-cloudwatch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-cloudwatch-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-cloudwatch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-cloudwatch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-cloudwatch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-cloudwatch-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloudwatch/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudwatch/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/cloudwatch/pricing/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
created: '2026-05-11'
description: Amazon CloudWatch is a monitoring and observability service from AWS that collects metrics, logs, and events from AWS resources, applications, and on-premises services. It enables operators to set alarms, visualize dashboards, automate responses, and troubleshoot performance across cloud workloads. The CloudWatch Query API and AWS SDKs expose programmatic access to metrics, alarms, dashboards, and Logs via AWS Signature Version 4 authenticated HTTPS requests.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-cloudwatch.png
layout: provider
modified: '2026-05-11'
name: Amazon CloudWatch
nav: Providers
network: true
overview: 'Amazon CloudWatch publishes 1 API on the [APIs.io](https://apis.io/) network: Amazon CloudWatch API API. Tagged areas include Monitoring, Observability, Metrics, Logs, and Alarms.


  Amazon CloudWatch''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 31.1
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
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-cloudwatch/refs/heads/main/screenshots/aws-cloudwatch-2026-06-20T172757.png
security:
- kind: authentication
  name: Aws Cloudwatch Authentication
  slug: aws-cloudwatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Cloudwatch Domain Security
  slug: aws-cloudwatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Cloudwatch Vulnerability Disclosure
  slug: aws-cloudwatch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Cloudwatch Trust Center
  slug: aws-cloudwatch-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-cloudwatch
tags:
- Monitoring
- Observability
- Metrics
- Logs
- Alarms
- Cloud
website: https://aws.amazon.com/cloudwatch/
---
