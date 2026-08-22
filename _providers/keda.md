---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Keda Agentic Access
  operation_count: 1
  slug: keda-agentic-access
  summary_line: 1 operation
api_count: 5
apis:
- description: External metrics API server that exposes event-driven metrics from configured scalers to the Kubernetes Horizontal Pod Autoscaler. It implements the Kubernetes external metrics API interface, allowing
  name: KEDA Metrics API
  slug: keda-metrics-api
- description: The ScaledObject custom resource defines the mapping between an event source and a Kubernetes Deployment, StatefulSet, or custom resource that should be scaled based on event metrics. It specifies tri
  name: KEDA ScaledObject API
  slug: keda-scaled-object-api
- description: 'The ScaledJob custom resource defines the mapping between an event source and Kubernetes Jobs that should be created in response to events. Unlike ScaledObject, ScaledJob creates new Job instances to '
  name: KEDA ScaledJob API
  slug: keda-scaled-job-api
- description: The TriggerAuthentication and ClusterTriggerAuthentication custom resources define authentication parameters for KEDA trigger scalers, allowing credentials to be sourced from Kubernetes Secrets, envir
  name: KEDA TriggerAuthentication API
  slug: keda-trigger-authentication-api
- description: 'The CloudEventSource and ClusterCloudEventSource custom resources define HTTP or Azure Event Grid destinations where KEDA delivers CloudEvents when scaling events occur. Events follow the CloudEvents '
  name: KEDA CloudEventSource API
  slug: keda-cloud-event-source-api
artifact_total: 19
asyncapis:
- description: 'KEDA emits CloudEvents to configured HTTP or Azure Event Grid destinations when scaling events occur. The CloudEventSource and ClusterCloudEventSource custom resources define the destination endpoint '
  name: KEDA CloudEvent Source
  slug: keda-cloud-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KEDA Metrics API
  slug: open-keda-metrics-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kedacore/keda/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/kedacore/keda/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/kedacore/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/kedacore/keda/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/kedacore/keda/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keda-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keda-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://keda.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://keda.sh/docs/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://keda.sh/docs/latest/deploy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kedacore
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kedacore/keda
- group: company
  title: ''
  type: Blog
  url: https://keda.sh/blog/
- group: operate
  title: ''
  type: Community
  url: https://keda.sh/community/
- group: operate
  title: ''
  type: Slack
  url: https://kubernetes.slack.com/archives/CKZJ36A5D
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/kedacore/keda/blob/main/CHANGELOG.md
- group: auth
  title: ''
  type: Security
  url: https://github.com/kedacore/keda/blob/main/SECURITY.md
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/keda
- group: design
  title: ''
  type: JSONLD
  url: keda-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/keda-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/keda-scaled-object-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/keda-cloud-event-schema.json
created: '2025-01-01'
description: KEDA (Kubernetes Event Driven Autoscaling) is a CNCF graduated application autoscaler that drives scaling of any container in Kubernetes based on the number of events needing to be processed. It extends Kubernetes with custom resources for defining scaling behavior and supports over 50 built-in scalers for event sources including Kafka, RabbitMQ, AWS SQS, Azure Service Bus, and Prometheus.
finops:
- name: Keda Finops
  service_category: Open-Source Kubernetes Autoscaling
  slug: keda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keda.png
json_schemas:
- name: KEDA CloudEvent
  property_count: 8
  slug: keda-cloud-event
- name: KEDA ScaledObject
  property_count: 5
  slug: keda-scaled-object
jsonld:
- class_count: 0
  name: Keda Context
  property_count: 27
  slug: keda-context
layout: provider
modified: '2026-05-19'
name: KEDA
nav: Providers
network: true
overview: 'KEDA publishes 2 APIs on the [APIs.io](https://apis.io/) network: Metrics API and CloudEventSource API. Tagged areas include Autoscaling, CNCF, Event-Driven, Graduated, and Kubernetes.


  The KEDA catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  KEDA''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, Stack Overflow tag, and 17 more developer resources.'
plans:
- name: Keda Plans Pricing
  plan_count: 1
  slug: keda-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Keda Rate Limits
  slug: keda-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: KEDA API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: keda-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: KEDA API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: keda-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.4
  delta: -4.8
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 11.4
    contract_quality: 75.3
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keda/refs/heads/main/screenshots/keda-2026-06-20T183939.png
security:
- kind: authentication
  name: Keda Authentication
  slug: keda-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Keda Domain Security
  slug: keda-domain-security
  summary_line: TLSv1.3 · HSTS
slug: keda
tags:
- Autoscaling
- CNCF
- Event-Driven
- Graduated
- Kubernetes
website: https://keda.sh/
---
