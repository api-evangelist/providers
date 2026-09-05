---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Kinesis Firehose Agentic Access
  operation_count: 7
  slug: amazon-kinesis-firehose-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: https://firehose.amazonaws.com
  baseurl_source: declared
  description: Firehose delivery stream management
  name: Amazon Kinesis Data Firehose Delivery Streams API
  slug: amazon-kinesis-firehose-delivery-streams-api
artifact_total: 33
collections:
- collection_type: postman
  name: Amazon Kinesis Data Firehose Delivery Streams API
  slug: postman-amazon-kinesis-firehose-delivery-streams-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Kinesis Data Firehose Delivery Streams API
  slug: open-amazon-kinesis-firehose-delivery-streams-api
- collection_type: open
  name: Amazon Kinesis Data Firehose API
  slug: open-amazon-kinesis-firehose
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-kinesis-data-firehose/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-kinesis-firehose-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-kinesis-firehose-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-kinesis-firehose-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-kinesis-firehose-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-kinesis-firehose-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/kinesis/data-firehose/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/firehose/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/firehose/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-kinesis-firehose-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-kinesis-firehose-vocabulary.yaml
created: '2024-01-15'
description: Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. It can capture, transform, and deliver streaming data to Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Splunk, and any custom HTTP endpoint. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration.
examples:
- key_count: 6
  name: Amazon Kinesis Firehose Delivery Stream Example
  slug: amazon-kinesis-firehose-delivery-stream-example
features:
- description: Fully managed service that automatically scales to match data throughput with no ongoing administration.
  name: Zero Administration
- description: Transform streaming data using AWS Lambda before delivering to destinations.
  name: Data Transformation
- description: Deliver data to Amazon S3, Redshift, OpenSearch Service, Splunk, Datadog, and custom HTTP endpoints.
  name: Multiple Destinations
- description: Automatically convert data formats such as JSON to Apache Parquet or Apache ORC before storing in S3.
  name: Format Conversion
- description: Compress data using GZIP, ZIP, or Snappy before delivering to S3 to reduce storage costs.
  name: Data Compression
finops:
- name: Amazon Kinesis Firehose Finops
  service_category: API
  slug: amazon-kinesis-firehose-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Deliver streaming data to S3 buckets as the primary data lake destination.
  name: Amazon S3
- description: Load streaming data into Redshift data warehouse for SQL analytics.
  name: Amazon Redshift
- description: Index streaming data in OpenSearch for real-time search and visualization.
  name: Amazon OpenSearch Service
- description: Transform and enrich streaming data using Lambda functions before delivery.
  name: AWS Lambda
- description: Send streaming data to Splunk for security and operational analytics.
  name: Splunk
json_schemas:
- name: DeliveryStream
  property_count: 6
  slug: amazon-kinesis-firehose-delivery-stream
json_structures:
- name: Amazon Kinesis Firehose Delivery Stream Structure
  property_count: 6
  slug: amazon-kinesis-firehose-delivery-stream-structure
jsonld:
- class_count: 1
  name: Amazon Kinesis Firehose Context
  property_count: 7
  slug: amazon-kinesis-firehose-context
layout: provider
modified: '2026-05-19'
name: Amazon Kinesis Data Firehose
nav: Providers
network: true
overview: 'Amazon Kinesis Data Firehose publishes 1 API on the [APIs.io](https://apis.io/) network: Delivery Streams API. Tagged areas include Analytics, Data Delivery, and Streaming.


  The Amazon Kinesis Data Firehose catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Kinesis Data Firehose''s developer surface includes authentication, developer portal, documentation, support, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon Kinesis Firehose Plans Pricing
  plan_count: 3
  slug: amazon-kinesis-firehose-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Amazon Kinesis Firehose Rate Limits
  slug: amazon-kinesis-firehose-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Amazon Kinesis Data Firehose API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-kinesis-firehose-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Amazon Kinesis Data Firehose API Rules
  rule_count: 23
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 14
  slug: amazon-kinesis-firehose-spectral-rules
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 64.6
    developer_ergonomics: 56.0
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-kinesis-firehose/refs/heads/main/screenshots/amazon-kinesis-firehose-2026-06-20T171717.png
security:
- kind: authentication
  name: Amazon Kinesis Firehose Authentication
  slug: amazon-kinesis-firehose-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Kinesis Firehose Domain Security
  slug: amazon-kinesis-firehose-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Kinesis Firehose Vulnerability Disclosure
  slug: amazon-kinesis-firehose-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Kinesis Firehose Trust Center
  slug: amazon-kinesis-firehose-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-kinesis-firehose
tags:
- Analytics
- Data Delivery
- Streaming
use_cases:
- description: Stream application and infrastructure logs to Amazon OpenSearch Service for real-time analysis.
  name: Log Analytics
- description: Capture website clickstream data and deliver to data lakes for behavioral analysis.
  name: Clickstream Analytics
- description: Ingest IoT device telemetry into S3 or Redshift for analytics and reporting.
  name: IoT Data Ingestion
- description: Stream security events and logs to SIEM systems like Splunk for threat detection.
  name: Security Analytics
website: https://aws.amazon.com/
---
