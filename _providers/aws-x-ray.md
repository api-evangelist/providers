---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Aws X Ray Agentic Access
  operation_count: 22
  slug: aws-x-ray-agentic-access
  summary_line: 22 operations · 22 acting
api_count: 9
apis:
- description: Manage encryption configuration
  name: AWS X-Ray Encryption API
  slug: aws-x-ray-encryption-api
- description: Manage trace groups
  name: AWS X-Ray Groups API
  slug: aws-x-ray-groups-api
- description: Automated anomaly detection insights
  name: AWS X-Ray Insights API
  slug: aws-x-ray-insights-api
- description: Manage sampling rules
  name: AWS X-Ray Sampling API
  slug: aws-x-ray-sampling-api
- description: Service map and statistics
  name: AWS X-Ray Service Graph API
  slug: aws-x-ray-service-graph-api
- description: The TagResource API from AWS X-Ray — 1 operation(s) for tagresource.
  name: AWS X-Ray TagResource API
  slug: aws-x-ray-tagresource-api
- description: The Tags API from AWS X-Ray — 1 operation(s) for tags.
  name: AWS X-Ray Tags API
  slug: aws-x-ray-tags-api
- description: Upload and retrieve trace data
  name: AWS X-Ray Traces API
  slug: aws-x-ray-traces-api
- description: The UntagResource API from AWS X-Ray — 1 operation(s) for untagresource.
  name: AWS X-Ray UntagResource API
  slug: aws-x-ray-untagresource-api
artifact_total: 101
collections:
- collection_type: postman
  name: AWS X-Ray Encryption API
  slug: postman-aws-x-ray-encryption-api
- collection_type: postman
  name: AWS X-Ray Encryption Groups API
  slug: postman-aws-x-ray-groups-api
- collection_type: postman
  name: AWS X-Ray Encryption Insights API
  slug: postman-aws-x-ray-insights-api
- collection_type: postman
  name: AWS X-Ray Encryption Sampling API
  slug: postman-aws-x-ray-sampling-api
- collection_type: postman
  name: AWS X-Ray Encryption Service Graph API
  slug: postman-aws-x-ray-service-graph-api
- collection_type: postman
  name: AWS X-Ray Encryption TagResource API
  slug: postman-aws-x-ray-tagresource-api
- collection_type: postman
  name: AWS X-Ray Encryption Tags API
  slug: postman-aws-x-ray-tags-api
- collection_type: postman
  name: AWS X-Ray Encryption Traces API
  slug: postman-aws-x-ray-traces-api
- collection_type: postman
  name: AWS X-Ray Encryption UntagResource API
  slug: postman-aws-x-ray-untagresource-api
- collection_type: open
  name: AWS X-Ray API
  slug: open-aws-x-ray
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aws-x-ray/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-x-ray-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-x-ray-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-x-ray-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-x-ray-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-x-ray-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/xray/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/xray/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/xray/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/xray/faqs/
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
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/category/management-tools/aws-x-ray/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: design
  title: ''
  type: SpectralRules
  url: rules/aws-x-ray-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aws-x-ray-vocabulary.yaml
created: '2026-03-26'
description: AWS X-Ray is a service that helps developers analyze and debug distributed applications by providing end-to-end tracing of requests as they travel through the application, identifying performance bottlenecks and errors. It is now part of Amazon CloudWatch Application Signals for unified observability.
examples:
- key_count: 3
  name: X Ray Batchgettracesresult Example
  slug: x-ray-batchgettracesresult-example
- key_count: 3
  name: X Ray Edgestatistics Example
  slug: x-ray-edgestatistics-example
- key_count: 3
  name: X Ray Encryptionconfig Example
  slug: x-ray-encryptionconfig-example
- key_count: 3
  name: X Ray Getservicegraphresult Example
  slug: x-ray-getservicegraphresult-example
- key_count: 3
  name: X Ray Gettracesummariesresult Example
  slug: x-ray-gettracesummariesresult-example
- key_count: 3
  name: X Ray Group Example
  slug: x-ray-group-example
- key_count: 3
  name: X Ray Groupsummary Example
  slug: x-ray-groupsummary-example
- key_count: 3
  name: X Ray Histogramentry Example
  slug: x-ray-histogramentry-example
- key_count: 3
  name: X Ray Insight Example
  slug: x-ray-insight-example
- key_count: 3
  name: X Ray Insightsummary Example
  slug: x-ray-insightsummary-example
- key_count: 3
  name: X Ray Samplingrule Example
  slug: x-ray-samplingrule-example
- key_count: 3
  name: X Ray Samplingrulerecord Example
  slug: x-ray-samplingrulerecord-example
- key_count: 3
  name: X Ray Service Example
  slug: x-ray-service-example
- key_count: 3
  name: X Ray Serviceid Example
  slug: x-ray-serviceid-example
- key_count: 3
  name: X Ray Servicestatistics Example
  slug: x-ray-servicestatistics-example
- key_count: 3
  name: X Ray Tag Example
  slug: x-ray-tag-example
- key_count: 3
  name: X Ray Timeseriesservicestatistics Example
  slug: x-ray-timeseriesservicestatistics-example
- key_count: 3
  name: X Ray Trace Example
  slug: x-ray-trace-example
- key_count: 3
  name: X Ray Tracesummary Example
  slug: x-ray-tracesummary-example
features:
- description: Trace requests from client to backend across all services in your distributed application.
  name: End-to-End Tracing
- description: Visualize service dependencies and real-time health indicators in an interactive map.
  name: Service Map
- description: Filter, search, and analyze traces using filter expressions and groups.
  name: Trace Analytics
- description: Control trace collection rates with dynamic sampling rules to manage cost and volume.
  name: Sampling Rules
- description: Add indexed annotations and non-indexed metadata to traces for custom filtering and context.
  name: Annotations and Metadata
- description: Identify and analyze errors, faults, and throttling across distributed services.
  name: Error Analysis
- description: Identify performance bottlenecks with detailed latency histograms and percentile data.
  name: Latency Analysis
- description: Integrated with CloudWatch Application Signals for unified observability and alerting.
  name: CloudWatch Integration
- description: Instrument applications with X-Ray SDKs for Java, Python, Go, Node.js, Ruby, and .NET.
  name: SDK Support
finops:
- name: Aws X Ray Finops
  service_category: API
  slug: aws-x-ray-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-x-ray.png
json_schemas:
- name: BatchGetTracesResult
  property_count: 3
  slug: x-ray-batchgettracesresult
- name: EdgeStatistics
  property_count: 5
  slug: x-ray-edgestatistics
- name: EncryptionConfig
  property_count: 3
  slug: x-ray-encryptionconfig
- name: GetServiceGraphResult
  property_count: 5
  slug: x-ray-getservicegraphresult
- name: GetTraceSummariesResult
  property_count: 4
  slug: x-ray-gettracesummariesresult
- name: Group
  property_count: 4
  slug: x-ray-group
- name: GroupSummary
  property_count: 4
  slug: x-ray-groupsummary
- name: HistogramEntry
  property_count: 2
  slug: x-ray-histogramentry
- name: Insight
  property_count: 12
  slug: x-ray-insight
- name: InsightSummary
  property_count: 13
  slug: x-ray-insightsummary
- name: SamplingRule
  property_count: 13
  slug: x-ray-samplingrule
- name: SamplingRuleRecord
  property_count: 3
  slug: x-ray-samplingrulerecord
- name: Service
  property_count: 13
  slug: x-ray-service
- name: ServiceId
  property_count: 4
  slug: x-ray-serviceid
- name: ServiceStatistics
  property_count: 5
  slug: x-ray-servicestatistics
- name: Tag
  property_count: 2
  slug: x-ray-tag
- name: TimeSeriesServiceStatistics
  property_count: 5
  slug: x-ray-timeseriesservicestatistics
- name: Trace
  property_count: 4
  slug: x-ray-trace
- name: TraceSummary
  property_count: 13
  slug: x-ray-tracesummary
json_structures:
- name: X Ray Batchgettracesresult Structure
  property_count: 0
  slug: x-ray-batchgettracesresult-structure
- name: X Ray Edgestatistics Structure
  property_count: 0
  slug: x-ray-edgestatistics-structure
- name: X Ray Encryptionconfig Structure
  property_count: 0
  slug: x-ray-encryptionconfig-structure
- name: X Ray Getservicegraphresult Structure
  property_count: 0
  slug: x-ray-getservicegraphresult-structure
- name: X Ray Gettracesummariesresult Structure
  property_count: 0
  slug: x-ray-gettracesummariesresult-structure
- name: X Ray Group Structure
  property_count: 0
  slug: x-ray-group-structure
- name: X Ray Groupsummary Structure
  property_count: 0
  slug: x-ray-groupsummary-structure
- name: X Ray Histogramentry Structure
  property_count: 0
  slug: x-ray-histogramentry-structure
- name: X Ray Insight Structure
  property_count: 0
  slug: x-ray-insight-structure
- name: X Ray Insightsummary Structure
  property_count: 0
  slug: x-ray-insightsummary-structure
- name: X Ray Samplingrule Structure
  property_count: 0
  slug: x-ray-samplingrule-structure
- name: X Ray Samplingrulerecord Structure
  property_count: 0
  slug: x-ray-samplingrulerecord-structure
- name: X Ray Service Structure
  property_count: 0
  slug: x-ray-service-structure
- name: X Ray Serviceid Structure
  property_count: 0
  slug: x-ray-serviceid-structure
- name: X Ray Servicestatistics Structure
  property_count: 0
  slug: x-ray-servicestatistics-structure
- name: X Ray Tag Structure
  property_count: 0
  slug: x-ray-tag-structure
- name: X Ray Timeseriesservicestatistics Structure
  property_count: 0
  slug: x-ray-timeseriesservicestatistics-structure
- name: X Ray Trace Structure
  property_count: 0
  slug: x-ray-trace-structure
- name: X Ray Tracesummary Structure
  property_count: 0
  slug: x-ray-tracesummary-structure
jsonld:
- class_count: 19
  name: Aws X Ray Context
  property_count: 0
  slug: aws-x-ray-context
layout: provider
modified: '2026-05-19'
name: AWS X-Ray
nav: Providers
network: true
overview: 'AWS X-Ray publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Encryption API, Groups API, Insights API, and 6 more. Tagged areas include Debugging, Distributed Tracing, Microservices, and Observability.


  The AWS X-Ray catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AWS X-Ray''s developer surface includes authentication, documentation, getting-started guide, pricing, FAQ, support, engineering blog, and 11 more developer resources.'
plans:
- name: Aws X Ray Plans Pricing
  plan_count: 3
  slug: aws-x-ray-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Aws X Ray Rate Limits
  slug: aws-x-ray-rate-limits
rules:
- name: AWS X-Ray API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aws-x-ray-jsonschema-spectral-rules
- name: AWS X-Ray API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 7
  slug: aws-x-ray-spectral-rules
score:
  band: developing
  composite: 54.7
  delta: -8.5
  facets:
    commercial_clarity: 55.3
    contract_quality: 70.1
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 23.7
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-x-ray/refs/heads/main/screenshots/aws-x-ray-2026-06-20T172820.png
security:
- kind: authentication
  name: Aws X Ray Authentication
  slug: aws-x-ray-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws X Ray Domain Security
  slug: aws-x-ray-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws X Ray Vulnerability Disclosure
  slug: aws-x-ray-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws X Ray Trust Center
  slug: aws-x-ray-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-x-ray
tags:
- Debugging
- Distributed Tracing
- Microservices
- Observability
use_cases:
- description: Identify and resolve latency bottlenecks in distributed microservices applications.
  name: Performance Optimization
- description: Trace errors and exceptions to their root cause across service boundaries.
  name: Error Debugging
- description: Understand service dependencies and the impact of downstream failures.
  name: Dependency Analysis
- description: Monitor request latency and error rates against service level agreements.
  name: SLA Monitoring
- description: Gain observability into complex microservices architectures and their interactions.
  name: Microservices Visibility
website: https://aws.amazon.com/xray/
---
