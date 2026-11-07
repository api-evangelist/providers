---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Cloudwatch Agentic Access
  operation_count: 10
  slug: amazon-cloudwatch-agentic-access
  summary_line: 10 operations
api_count: 2
apis:
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for creating, describing, and deleting metric alarms
  name: Amazon CloudWatch Alarms API
  slug: amazon-cloudwatch-alarms-api
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for creating, retrieving, and listing CloudWatch dashboards
  name: Amazon CloudWatch Dashboards API
  slug: amazon-cloudwatch-dashboards-api
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for publishing, retrieving, and listing CloudWatch metrics
  name: Amazon CloudWatch Metrics API
  slug: amazon-cloudwatch-metrics-api
- description: Query API for publishing and retrieving metrics, managing alarms, and configuring dashboards in Amazon CloudWatch. Requests are authenticated with AWS Signature Version 4 (SigV4) using AWS access keys
  name: Amazon CloudWatch API
  slug: monitoring-api
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Amazon CloudWatch API API from Amazon CloudWatch — 1 operation(s) for amazon cloudwatch api.
  name: Amazon CloudWatch Amazon CloudWatch API
  slug: amazon-cloudwatch-amazon-cloudwatch-api-api
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudwatch Alarm Mute Rule API from Amazon CloudWatch — 4 operation(s) for cloudwatch alarm mute rule.
  name: Amazon CloudWatch Cloudwatch Alarm Mute Rule API
  slug: amazon-cloudwatch-alarm-mute-rule-api
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudwatch Anomaly Detector API from Amazon CloudWatch — 3 operation(s) for cloudwatch anomaly detector.
  name: Amazon CloudWatch Cloudwatch Anomaly Detector API
  slug: amazon-cloudwatch-anomaly-detector-api
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudwatch Insight Rule API from Amazon CloudWatch — 5 operation(s) for cloudwatch insight rule.
  name: Amazon CloudWatch Cloudwatch Insight Rule API
  slug: amazon-cloudwatch-insight-rule-api
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudwatch Metric Stream API from Amazon CloudWatch — 6 operation(s) for cloudwatch metric stream.
  name: Amazon CloudWatch Cloudwatch Metric Stream API
  slug: amazon-cloudwatch-metric-stream-api
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudwatch O Tel Enrichment API from Amazon CloudWatch — 4 operation(s) for cloudwatch o tel enrichment.
  name: Amazon CloudWatch Cloudwatch O Tel Enrichment API
  slug: amazon-cloudwatch-o-tel-enrichment-api
- baseURL: https://monitoring.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudwatch Resource Metrics Configuration API from Amazon CloudWatch — 4 operation(s) for cloudwatch resource metrics configuration.
  name: Amazon CloudWatch Cloudwatch Resource Metrics Configuration API
  slug: amazon-cloudwatch-resource-metrics-configuration-api
artifact_total: 74
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
- collection_type: open
  name: Amazon CloudWatch Alarms API
  slug: open-amazon-cloudwatch-alarms-api
- collection_type: open
  name: Amazon CloudWatch Alarms Dashboards API
  slug: open-amazon-cloudwatch-dashboards-api
- collection_type: open
  name: Amazon CloudWatch Alarms Metrics API
  slug: open-amazon-cloudwatch-metrics-api
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-cloudwatch/plans/amazon-cloudwatch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-cloudwatch-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/amazon-cloudwatch/capabilities/amazon-cloudwatch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-cloudwatch-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/amazon-cloudwatch/mcp/amazon-cloudwatch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amazon-cloudwatch-mcp.yml
- group: other
  href: https://artifacts.apis.io/amazon-cloudwatch/overlays/amazon-cloudwatch-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amazon-cloudwatch-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-cloudwatch/overview
- group: agent
  href: https://artifacts.apis.io/amazon-cloudwatch/agentic-access/amazon-cloudwatch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-cloudwatch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudwatch/security/amazon-cloudwatch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-cloudwatch-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudwatch/security/amazon-cloudwatch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloudwatch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudwatch/security/amazon-cloudwatch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-cloudwatch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudwatch/authentication/amazon-cloudwatch-authentication.yml
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
  href: https://artifacts.apis.io/amazon-cloudwatch/rules/amazon-cloudwatch-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-cloudwatch-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-cloudwatch/vocabulary/amazon-cloudwatch-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudwatch-vocabulary.yaml
- group: build
  href: https://artifacts.apis.io/amazon-cloudwatch/packages/amazon-cloudwatch-packages.yml
  title: ''
  type: Packages
  url: packages/amazon-cloudwatch-packages.yml
- group: agent
  href: https://artifacts.apis.io/amazon-cloudwatch/well-known/amazon-cloudwatch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-cloudwatch-well-known.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudwatch/well-known/amazon-cloudwatch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-cloudwatch-security.txt
- group: agent
  href: https://artifacts.apis.io/amazon-cloudwatch/llms/amazon-cloudwatch-llms.txt
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
finops:
- has_sources: true
  method: derived
  name: Amazon Cloudwatch Finops
  primary_unit: gb ingested
  service_category: ''
  slug: amazon-cloudwatch-finops
  template: false
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
mcp_servers:
- description: Official AWS Labs CloudWatch MCP server. Runs locally (stdio) on the same host as the LLM client and uses the caller's AWS credentials to expose CloudWatch metrics, PromQL, alarms, and Logs Insights f
  name: Amazon CloudWatch MCP Server
  slug: awslabs-cloudwatch-mcp-server
modified: '2026-09-16'
name: Amazon CloudWatch
nav: Providers
network: true
overview: 'Amazon CloudWatch publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alarms API, Dashboards API, Metrics API, and 8 more. Tagged areas include Amazon Web Services, CloudWatch, Monitoring, Observability, and Metrics.


  The Amazon CloudWatch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CloudWatch''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 25 more developer resources.'
plans:
- name: Amazon Cloudwatch Plans Pricing
  plan_count: 16
  slug: amazon-cloudwatch-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon CloudWatch — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-cloudwatch-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Amazon CloudWatch API Rules
  rule_count: 25
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 10
  slug: amazon-cloudwatch-spectral-rules
score:
  band: exemplar
  composite: 71.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 81.0
    catalog_earned_first_party: 12.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 73.4
    developer_ergonomics: 72.6
    discoverability: 71.7
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 70.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 60.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/amazon-cloudwatch/amazon-cloudwatch-2026-07-25T195951.png
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
- Amazon Web Services
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
