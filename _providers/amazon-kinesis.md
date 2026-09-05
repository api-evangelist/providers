---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 36
  human_in_the_loop: 2
  name: Amazon Kinesis Agentic Access
  operation_count: 39
  slug: amazon-kinesis-agentic-access
  summary_line: 39 operations · 36 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: Operations for describing and updating account-level settings and limits.
  name: Amazon Kinesis Account API
  slug: amazon-kinesis-account-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: Operations for registering, describing, listing, and deregistering enhanced fan-out consumers.
  name: Amazon Kinesis Consumers API
  slug: amazon-kinesis-consumers-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: Operations for starting and stopping server-side encryption on a stream.
  name: Amazon Kinesis Encryption API
  slug: amazon-kinesis-encryption-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: Operations for enabling and disabling enhanced shard-level monitoring.
  name: Amazon Kinesis Monitoring API
  slug: amazon-kinesis-monitoring-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: Operations for managing resource-based policies on streams.
  name: Amazon Kinesis Policies API
  slug: amazon-kinesis-policies-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: Operations for putting and getting data records to and from a stream.
  name: Amazon Kinesis Records API
  slug: amazon-kinesis-records-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: Operations for listing, splitting, merging, and managing shards within a stream.
  name: Amazon Kinesis Shards API
  slug: amazon-kinesis-shards-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: Operations for creating, describing, listing, and managing Kinesis data streams.
  name: Amazon Kinesis Streams API
  slug: amazon-kinesis-streams-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: 'The #X Amz Target=Kinesis 20131202.AddTagsToStream API from Amazon Kinesis — 1 operation(s) for #x amz target=kinesis 20131202.addtagstostream.'
  name: 'Amazon Kinesis #X Amz Target=Kinesis 20131202.AddTagsToStream API'
  slug: amazon-kinesis-x-amz-target-kinesis-20131202-addtagstostream-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: 'The #X Amz Target=Kinesis 20131202.ListTagsForStream API from Amazon Kinesis — 1 operation(s) for #x amz target=kinesis 20131202.listtagsforstream.'
  name: 'Amazon Kinesis #X Amz Target=Kinesis 20131202.ListTagsForStream API'
  slug: amazon-kinesis-x-amz-target-kinesis-20131202-listtagsforstream-api
- baseURL: https://kinesis.amazonaws.com
  baseurl_source: declared
  description: 'The #X Amz Target=Kinesis 20131202.RemoveTagsFromStream API from Amazon Kinesis — 1 operation(s) for #x amz target=kinesis 20131202.removetagsfromstream.'
  name: 'Amazon Kinesis #X Amz Target=Kinesis 20131202.RemoveTagsFromStream API'
  slug: amazon-kinesis-x-amz-target-kinesis-20131202-removetagsfromstream-api
arazzos:
- description: Create a Kinesis data stream and poll until it reaches ACTIVE status.
  name: Amazon Kinesis Create and Activate Stream
  slug: amazon-kinesis-create-and-activate-stream-workflow
- description: Create a stream, wait until it is ACTIVE, then write the first data record.
  name: Amazon Kinesis Create Stream and Put First Record
  slug: amazon-kinesis-create-stream-and-put-record-workflow
- description: Deregister an enhanced fan-out consumer, confirm the stream, then delete it.
  name: Amazon Kinesis Deregister Consumer and Delete Stream
  slug: amazon-kinesis-deregister-consumer-and-delete-stream-workflow
- description: List a stream's shards, then read from the first shard from the trim horizon.
  name: Amazon Kinesis List Shards and Read From First
  slug: amazon-kinesis-list-shards-and-read-from-first-workflow
- description: Write one record, then read it back starting at its exact sequence number.
  name: Amazon Kinesis Put Record and Read At Sequence
  slug: amazon-kinesis-put-record-and-read-at-sequence-workflow
- description: Batch-write records, get a shard iterator, then read the records back.
  name: Amazon Kinesis Put Records and Read Back
  slug: amazon-kinesis-put-records-and-read-back-workflow
- description: Register an enhanced fan-out consumer and poll until it becomes ACTIVE.
  name: Amazon Kinesis Register Consumer and Confirm
  slug: amazon-kinesis-register-consumer-and-confirm-workflow
- description: Resize a provisioned stream's shard count, wait for ACTIVE, then list shards.
  name: Amazon Kinesis Scale Stream Shard Count
  slug: amazon-kinesis-scale-stream-shard-count-workflow
artifact_total: 56
asyncapis:
- description: Amazon Kinesis Data Streams is a massively scalable and durable real-time data streaming service. This AsyncAPI specification describes the event-driven consumer patterns for Kinesis Data Streams, inc
  name: Amazon Kinesis Data Streams
  slug: amazon-kinesis-streams-asyncapi
collections:
- collection_type: postman
  name: Amazon Kinesis Data Streams API
  slug: postman-amazon-kinesis-data-streams
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Kinesis Data Streams Account API
  slug: open-amazon-kinesis-account-api
- collection_type: open
  name: Amazon Kinesis Data Streams Account Consumers API
  slug: open-amazon-kinesis-consumers-api
- collection_type: open
  name: Amazon Kinesis Data Streams API
  slug: open-amazon-kinesis-data-streams
- collection_type: open
  name: Amazon Kinesis Data Streams Account Encryption API
  slug: open-amazon-kinesis-encryption-api
- collection_type: open
  name: Amazon Kinesis Data Streams Account Monitoring API
  slug: open-amazon-kinesis-monitoring-api
- collection_type: open
  name: Amazon Kinesis Data Streams Account Policies API
  slug: open-amazon-kinesis-policies-api
- collection_type: open
  name: Amazon Kinesis Data Streams Account Records API
  slug: open-amazon-kinesis-records-api
- collection_type: open
  name: Amazon Kinesis Data Streams Account Shards API
  slug: open-amazon-kinesis-shards-api
- collection_type: open
  name: Amazon Kinesis Data Account Streams API
  slug: open-amazon-kinesis-streams-api
- collection_type: open
  name: 'Amazon Kinesis Data Streams Account #X Amz Target=Kinesis 20131202.AddTagsToStream API'
  slug: open-amazon-kinesis-x-amz-target-kinesis-20131202-addtagstostream-api
- collection_type: open
  name: 'Amazon Kinesis Data Streams Account #X Amz Target=Kinesis 20131202.ListTagsForStream API'
  slug: open-amazon-kinesis-x-amz-target-kinesis-20131202-listtagsforstream-api
- collection_type: open
  name: 'Amazon Kinesis Data Streams Account #X Amz Target=Kinesis 20131202.RemoveTagsFromStream API'
  slug: open-amazon-kinesis-x-amz-target-kinesis-20131202-removetagsfromstream-api
- collection_type: open
  name: Amazon Kinesis API
  slug: open-amazon-kinesis
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-kinesis-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-kinesis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-kinesis-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-kinesis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-kinesis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-kinesis-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-kinesis/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kinesis-create-and-activate-stream-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kinesis-create-stream-and-put-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kinesis-deregister-consumer-and-delete-stream-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kinesis-list-shards-and-read-from-first-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kinesis-put-record-and-read-at-sequence-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kinesis-put-records-and-read-back-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kinesis-register-consumer-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kinesis-scale-stream-shard-count-workflow.yml
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/kinesis/data-streams/faqs/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis/
- group: other
  title: ''
  type: Customers
  url: https://aws.amazon.com/kinesis/customers/
- group: other
  title: ''
  type: Resources
  url: https://aws.amazon.com/kinesis/resources/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/kinesis/
- group: build
  title: ''
  type: SDK & Tools
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/kinesis/
- group: company
  title: ''
  type: Firehose Blog
  url: https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis/kinesis-data-firehose/
- group: learn
  title: ''
  type: Video Streams FAQs
  url: https://aws.amazon.com/kinesis/video-streams/faqs/
- group: operate
  title: ''
  type: Firehose FAQs
  url: https://aws.amazon.com/firehose/faqs/
- group: operate
  title: ''
  type: Managed Flink FAQs
  url: https://aws.amazon.com/managed-service-apache-flink/faqs/
- group: learn
  title: ''
  type: Video Streams Resources
  url: https://aws.amazon.com/kinesis/video-streams/resources/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/kinesis/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/kinesis/data-streams/pricing/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-iam.html
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-kinesis
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-kinesis-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-kinesis-vocabulary.yaml
created: 2024-01-01 00:00:00+00:00
description: Amazon Kinesis makes it easy to collect, process, and analyze real-time streaming data so you can get timely insights and react quickly to new information. Amazon Kinesis offers key capabilities to cost-effectively process streaming data at any scale, along with the flexibility to choose the tools that best suit the requirements of your application.
examples:
- key_count: 4
  name: Amazon Kinesis Record Example
  slug: amazon-kinesis-record-example
- key_count: 5
  name: Amazon Kinesis Stream Example
  slug: amazon-kinesis-stream-example
finops:
- name: Amazon Kinesis Finops
  service_category: Analytics / Streaming
  slug: amazon-kinesis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-kinesis.png
json_schemas:
- name: Record
  property_count: 4
  slug: amazon-kinesis-record
- name: Stream
  property_count: 5
  slug: amazon-kinesis-stream
json_structures:
- name: Amazon Kinesis Record Structure
  property_count: 4
  slug: amazon-kinesis-record-structure
- name: Amazon Kinesis Stream Structure
  property_count: 5
  slug: amazon-kinesis-stream-structure
jsonld:
- class_count: 2
  name: Amazon Kinesis Context
  property_count: 7
  slug: amazon-kinesis-context
layout: provider
modified: '2026-05-19'
name: Amazon Kinesis
nav: Providers
network: true
overview: 'Amazon Kinesis publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Consumers API, Encryption API, and 8 more. Tagged areas include Analytics, Big Data, Data Processing, Real-Time, and Streaming.


  The Amazon Kinesis catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Amazon Kinesis'' developer surface includes authentication, FAQ, engineering blog, documentation, support, developer console, developer portal, and 32 more developer resources.'
plans:
- name: Amazon Kinesis Plans Pricing
  plan_count: 3
  slug: amazon-kinesis-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Amazon Kinesis Rate Limits
  slug: amazon-kinesis-rate-limits
rules:
- effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: Amazon Kinesis API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: amazon-kinesis-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Amazon Kinesis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-kinesis-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon Kinesis API Rules
  rule_count: 24
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 15
  slug: amazon-kinesis-spectral-rules
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 67.5
    catalog_earned_first_party: 0.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 75.5
    developer_ergonomics: 65.5
    discoverability: 63.0
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-kinesis/refs/heads/main/screenshots/amazon-kinesis-2026-06-20T171718.png
security:
- kind: authentication
  name: Amazon Kinesis Authentication
  slug: amazon-kinesis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Kinesis Domain Security
  slug: amazon-kinesis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Kinesis Vulnerability Disclosure
  slug: amazon-kinesis-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Kinesis Trust Center
  slug: amazon-kinesis-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-kinesis
tags:
- Analytics
- Big Data
- Data Processing
- Real-Time
- Streaming
use_cases:
- description: Analyze streaming data for operational metrics and business intelligence.
  name: Real-Time Analytics
- description: Build event-driven microservices that react to real-time data streams.
  name: Event-Driven Architectures
- description: Feed real-time data into ML models for online training and inference.
  name: Machine Learning
website: https://aws.amazon.com/kinesis/
---
