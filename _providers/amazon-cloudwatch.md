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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Cloudwatch Agentic Access
  operation_count: 10
  slug: amazon-cloudwatch-agentic-access
  summary_line: 10 operations
api_count: 3
apis:
- description: Operations for creating, describing, and deleting metric alarms
  name: Amazon CloudWatch Alarms API
  slug: amazon-cloudwatch-alarms-api
- description: Operations for creating, retrieving, and listing CloudWatch dashboards
  name: Amazon CloudWatch Dashboards API
  slug: amazon-cloudwatch-dashboards-api
- description: Operations for publishing, retrieving, and listing CloudWatch metrics
  name: Amazon CloudWatch Metrics API
  slug: amazon-cloudwatch-metrics-api
artifact_total: 60
collections:
- collection_type: postman
  name: Amazon CloudWatch Alarms API
  slug: postman-amazon-cloudwatch-alarms-api
- collection_type: postman
  name: Amazon CloudWatch Alarms Dashboards API
  slug: postman-amazon-cloudwatch-dashboards-api
- collection_type: postman
  name: Amazon CloudWatch Alarms Metrics API
  slug: postman-amazon-cloudwatch-metrics-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-cloudwatch/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-cloudwatch-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-cloudwatch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloudwatch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-cloudwatch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-cloudwatch-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloudwatch/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/
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
  url: https://aws.amazon.com/blogs/mt/
- group: company
  title: ''
  type: BlogRSS
  url: https://aws.amazon.com/blogs/mt/tag/amazon-cloudwatch/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudwatch/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-cloudwatch
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-cloudwatch-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudwatch-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-cloudwatch-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-cloudwatch-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-cloudwatch-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-cloudwatch-llms.txt
created: '2024-01-15'
description: Amazon CloudWatch is an intelligent observability platform providing complete visibility into performance, availability, and security across your entire technology stack. Monitor applications, infrastructure, and workloads with unified metrics, logs, and traces plus AI-powered insights.
examples:
- key_count: 19
  name: Cloudwatch Alarm Example
  slug: cloudwatch-alarm-example
- key_count: 4
  name: Cloudwatch Dashboard Example
  slug: cloudwatch-dashboard-example
- key_count: 2
  name: Cloudwatch Describe Alarms Response Example
  slug: cloudwatch-describe-alarms-response-example
- key_count: 3
  name: Cloudwatch Get Dashboard Response Example
  slug: cloudwatch-get-dashboard-response-example
- key_count: 2
  name: Cloudwatch Get Metric Data Response Example
  slug: cloudwatch-get-metric-data-response-example
- key_count: 2
  name: Cloudwatch Get Metric Statistics Response Example
  slug: cloudwatch-get-metric-statistics-response-example
- key_count: 2
  name: Cloudwatch List Dashboards Response Example
  slug: cloudwatch-list-dashboards-response-example
- key_count: 2
  name: Cloudwatch List Metrics Response Example
  slug: cloudwatch-list-metrics-response-example
- key_count: 3
  name: Cloudwatch Metric Example
  slug: cloudwatch-metric-example
- key_count: 1
  name: Cloudwatch Put Dashboard Response Example
  slug: cloudwatch-put-dashboard-response-example
features:
- description: Monitor metrics, logs, and traces in one interface for complete system visibility.
  name: Unified Observability
- description: Detect anomalies and investigate issues using AI-powered CloudWatch Investigations.
  name: AI-Powered Insights
- description: Create custom dashboards with pre-built and customizable metric visualizations.
  name: Dashboards
- description: Set threshold-based alarms on any metric to trigger automated actions.
  name: Alarms
- description: Analyze log data with SQL and natural language queries using CloudWatch Logs Insights.
  name: Log Insights
- description: Ingest OpenTelemetry data alongside native AWS metrics and traces.
  name: OpenTelemetry Integration
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-cloudwatch.png
integrations:
- description: Monitor EC2 instance performance metrics including CPU, network, and disk.
  name: Amazon EC2
- description: Monitor Lambda invocations, errors, and duration metrics automatically.
  name: AWS Lambda
- description: Ingest Prometheus metrics into CloudWatch for unified monitoring.
  name: Amazon Prometheus
- description: Connect CloudWatch data sources to Grafana dashboards.
  name: Grafana
- description: Correlate traces from X-Ray with CloudWatch metrics and logs.
  name: AWS X-Ray
json_schemas:
- name: Amazon CloudWatch Alarm
  property_count: 25
  slug: amazon-cloudwatch-alarm
- name: Alarm
  property_count: 19
  slug: cloudwatch-alarm
- name: Dashboard
  property_count: 4
  slug: cloudwatch-dashboard
- name: DescribeAlarmsResponse
  property_count: 2
  slug: cloudwatch-describe-alarms-response
- name: GetDashboardResponse
  property_count: 3
  slug: cloudwatch-get-dashboard-response
- name: GetMetricDataResponse
  property_count: 2
  slug: cloudwatch-get-metric-data-response
- name: GetMetricStatisticsResponse
  property_count: 2
  slug: cloudwatch-get-metric-statistics-response
- name: ListDashboardsResponse
  property_count: 2
  slug: cloudwatch-list-dashboards-response
- name: ListMetricsResponse
  property_count: 2
  slug: cloudwatch-list-metrics-response
- name: Metric
  property_count: 3
  slug: cloudwatch-metric
- name: PutDashboardResponse
  property_count: 1
  slug: cloudwatch-put-dashboard-response
json_structures:
- name: Cloudwatch Alarm Structure
  property_count: 19
  slug: cloudwatch-alarm-structure
- name: Cloudwatch Dashboard Structure
  property_count: 4
  slug: cloudwatch-dashboard-structure
- name: Cloudwatch Describe Alarms Response Structure
  property_count: 2
  slug: cloudwatch-describe-alarms-response-structure
- name: Cloudwatch Get Dashboard Response Structure
  property_count: 3
  slug: cloudwatch-get-dashboard-response-structure
- name: Cloudwatch Get Metric Data Response Structure
  property_count: 2
  slug: cloudwatch-get-metric-data-response-structure
- name: Cloudwatch Get Metric Statistics Response Structure
  property_count: 2
  slug: cloudwatch-get-metric-statistics-response-structure
- name: Cloudwatch List Dashboards Response Structure
  property_count: 2
  slug: cloudwatch-list-dashboards-response-structure
- name: Cloudwatch List Metrics Response Structure
  property_count: 2
  slug: cloudwatch-list-metrics-response-structure
- name: Cloudwatch Metric Structure
  property_count: 3
  slug: cloudwatch-metric-structure
- name: Cloudwatch Put Dashboard Response Structure
  property_count: 1
  slug: cloudwatch-put-dashboard-response-structure
jsonld:
- class_count: 10
  name: Amazon Cloudwatch Context
  property_count: 32
  slug: amazon-cloudwatch-context
layout: provider
modified: '2026-06-20'
name: Amazon CloudWatch
nav: Providers
network: true
overview: 'Amazon CloudWatch publishes 3 APIs on the [APIs.io](https://apis.io/) network: Alarms API, Dashboards API, and Metrics API. Tagged areas include CloudWatch, Monitoring, Observability, Metrics, and Logs.


  The Amazon CloudWatch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CloudWatch''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 21 more developer resources.'
random_paper: 23
rules:
- name: Amazon CloudWatch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-cloudwatch-jsonschema-spectral-rules
- name: Amazon CloudWatch API Rules
  rule_count: 25
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 10
  slug: amazon-cloudwatch-spectral-rules
score:
  band: strong
  composite: 60.7
  delta: -0.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 79.7
    developer_ergonomics: 45.7
    discoverability: 92.6
    governance: 80.2
    operational_transparency: 21.1
  previous_composite: 61.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-cloudwatch/refs/heads/main/screenshots/amazon-cloudwatch-2026-07-25T195951.png
security:
- kind: authentication
  name: Amazon Cloudwatch Authentication
  slug: amazon-cloudwatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Cloudwatch Domain Security
  slug: amazon-cloudwatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Cloudwatch Vulnerability Disclosure
  slug: amazon-cloudwatch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Cloudwatch Trust Center
  slug: amazon-cloudwatch-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-cloudwatch
tags:
- CloudWatch
- Monitoring
- Observability
- Metrics
- Logs
use_cases:
- description: Monitor EC2, RDS, Lambda, and other AWS resources with built-in metrics.
  name: Infrastructure Monitoring
- description: Track application performance metrics and detect latency or error rate spikes.
  name: Application Performance
- description: Aggregate and query application logs for troubleshooting and analytics.
  name: Log Analysis
- description: Trigger auto-scaling, Lambda functions, or SNS alerts based on metric alarms.
  name: Automated Remediation
website: https://aws.amazon.com/cloudwatch/
---
