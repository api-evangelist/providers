---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 20.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Amazon Cloudtrail Agentic Access
  operation_count: 6
  slug: amazon-cloudtrail-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://cloudtrail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing CloudTrail Lake event data stores
  name: Amazon CloudTrail Event Data Stores API
  slug: amazon-cloudtrail-event-data-stores-api
- baseURL: https://cloudtrail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for looking up and querying events
  name: Amazon CloudTrail Events API
  slug: amazon-cloudtrail-events-api
- baseURL: https://cloudtrail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for creating and managing CloudTrail trails
  name: Amazon CloudTrail Trails API
  slug: amazon-cloudtrail-trails-api
artifact_total: 54
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon CloudTrail Event Data Stores API
  slug: open-amazon-cloudtrail-event-data-stores-api
- collection_type: open
  name: Amazon CloudTrail Event Data Stores Events API
  slug: open-amazon-cloudtrail-events-api
- collection_type: open
  name: Amazon CloudTrail Event Data Stores Trails API
  slug: open-amazon-cloudtrail-trails-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-cloudtrail-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-cloudtrail-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-cloudtrail-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloudtrail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-cloudtrail-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloudtrail/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/
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
  url: https://aws.amazon.com/blogs/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudtrail/
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
  url: https://stackoverflow.com/questions/tagged/aws-cloudtrail
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
  url: rules/amazon-cloudtrail-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudtrail-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-cloudtrail-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-cloudtrail-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-cloudtrail-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-cloudtrail-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-cloudtrail-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-cloudtrail-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-cloudtrail-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-cloudtrail-lifecycle.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/mt/tag/aws-cloudtrail/feed/
created: '2024-01-15'
description: AWS CloudTrail enables governance, compliance, operational auditing, and risk auditing of your AWS account by tracking user activity and API usage across AWS environments, hybrid setups, and multicloud deployments with immutable audit trails.
examples:
- key_count: 3
  name: Cloudtrail Create Event Data Store Request Example
  slug: cloudtrail-create-event-data-store-request-example
- key_count: 5
  name: Cloudtrail Create Event Data Store Response Example
  slug: cloudtrail-create-event-data-store-response-example
- key_count: 7
  name: Cloudtrail Create Trail Request Example
  slug: cloudtrail-create-trail-request-example
- key_count: 5
  name: Cloudtrail Create Trail Response Example
  slug: cloudtrail-create-trail-response-example
- key_count: 1
  name: Cloudtrail Describe Trails Response Example
  slug: cloudtrail-describe-trails-response-example
- key_count: 2
  name: Cloudtrail List Event Data Stores Response Example
  slug: cloudtrail-list-event-data-stores-response-example
- key_count: 5
  name: Cloudtrail Lookup Events Request Example
  slug: cloudtrail-lookup-events-request-example
- key_count: 2
  name: Cloudtrail Lookup Events Response Example
  slug: cloudtrail-lookup-events-response-example
features:
- description: Consolidate activity events from AWS, external providers, on-premises, and SaaS into a unified audit trail.
  name: Event Aggregation
- description: Store audit-worthy events immutably to ensure tamper-proof compliance records.
  name: Immutable Audit Logs
- description: Detect unusual API activity patterns with anomaly detection on management and data events.
  name: CloudTrail Insights
- description: Investigate issues using SQL queries or natural language with Amazon Athena integration.
  name: SQL Query Support
- description: Create trails that capture events from all AWS regions in a single S3 bucket.
  name: Multi-Region Trails
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-cloudtrail.png
integrations:
- description: Store CloudTrail logs in S3 buckets with lifecycle management.
  name: Amazon S3
- description: Query CloudTrail logs using SQL via Athena integration.
  name: Amazon Athena
- description: Stream CloudTrail events to CloudWatch Logs for real-time monitoring.
  name: Amazon CloudWatch
- description: Trigger Lambda functions based on CloudTrail events for automated response.
  name: AWS Lambda
- description: Send CloudTrail findings to Security Hub for centralized security management.
  name: AWS Security Hub
json_schemas:
- name: Amazon CloudTrail Event
  property_count: 16
  slug: amazon-cloudtrail-event
- name: CreateEventDataStoreRequest
  property_count: 3
  slug: cloudtrail-create-event-data-store-request
- name: CreateEventDataStoreResponse
  property_count: 5
  slug: cloudtrail-create-event-data-store-response
- name: CreateTrailRequest
  property_count: 7
  slug: cloudtrail-create-trail-request
- name: CreateTrailResponse
  property_count: 5
  slug: cloudtrail-create-trail-response
- name: DescribeTrailsResponse
  property_count: 1
  slug: cloudtrail-describe-trails-response
- name: ListEventDataStoresResponse
  property_count: 2
  slug: cloudtrail-list-event-data-stores-response
- name: LookupEventsRequest
  property_count: 5
  slug: cloudtrail-lookup-events-request
- name: LookupEventsResponse
  property_count: 2
  slug: cloudtrail-lookup-events-response
json_structures:
- name: Cloudtrail Create Event Data Store Request Structure
  property_count: 3
  slug: cloudtrail-create-event-data-store-request-structure
- name: Cloudtrail Create Event Data Store Response Structure
  property_count: 5
  slug: cloudtrail-create-event-data-store-response-structure
- name: Cloudtrail Create Trail Request Structure
  property_count: 7
  slug: cloudtrail-create-trail-request-structure
- name: Cloudtrail Create Trail Response Structure
  property_count: 5
  slug: cloudtrail-create-trail-response-structure
- name: Cloudtrail Describe Trails Response Structure
  property_count: 1
  slug: cloudtrail-describe-trails-response-structure
- name: Cloudtrail List Event Data Stores Response Structure
  property_count: 2
  slug: cloudtrail-list-event-data-stores-response-structure
- name: Cloudtrail Lookup Events Request Structure
  property_count: 5
  slug: cloudtrail-lookup-events-request-structure
- name: Cloudtrail Lookup Events Response Structure
  property_count: 2
  slug: cloudtrail-lookup-events-response-structure
jsonld:
- class_count: 9
  name: Amazon Cloudtrail Context
  property_count: 21
  slug: amazon-cloudtrail-context
layout: provider
mcp_servers:
- description: ''
  name: Amazon CloudTrail MCP Server
  slug: amazon-cloudtrail-mcp-server
modified: '2026-06-20'
name: Amazon CloudTrail
nav: Providers
network: true
overview: 'Amazon CloudTrail publishes 3 APIs on the [APIs.io](https://apis.io/) network: Event Data Stores API, Events API, and Trails API. Tagged areas include CloudTrail, Audit, Compliance, Governance, and Security.


  The Amazon CloudTrail catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CloudTrail''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, YouTube channel, and 24 more developer resources.'
random_paper: 2
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon CloudTrail API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-cloudtrail-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon CloudTrail API Rules
  rule_count: 24
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 10
  slug: amazon-cloudtrail-spectral-rules
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 67.5
    catalog_earned_first_party: 0.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 33.3
    contract_quality: 68.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 18.4
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-cloudtrail/refs/heads/main/screenshots/amazon-cloudtrail-2026-07-25T195952.png
security:
- kind: domain-security
  name: Amazon Cloudtrail Domain Security
  slug: amazon-cloudtrail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Cloudtrail Vulnerability Disclosure
  slug: amazon-cloudtrail-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Cloudtrail Trust Center
  slug: amazon-cloudtrail-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-cloudtrail
tags:
- CloudTrail
- Audit
- Compliance
- Governance
- Security
use_cases:
- description: Demonstrate adherence to SOC, PCI DSS, and HIPAA regulations with audit logs.
  name: Compliance Auditing
- description: Record and monitor user and API activity for security incident detection.
  name: Security Monitoring
- description: Investigate operational issues by querying historical API activity.
  name: Operational Debugging
- description: Track who made changes to AWS resources and when for governance accountability.
  name: Governance
website: https://aws.amazon.com/cloudtrail/
---
