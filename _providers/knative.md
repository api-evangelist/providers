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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Knative Agentic Access
  operation_count: 42
  slug: knative-agentic-access
  summary_line: 42 operations · 20 acting
api_count: 13
apis:
- description: Knative Functions enables developers to create, build, and deploy stateless, event-driven functions as Knative Services using the func CLI or the kn func plugin. Functions can be written in multiple l
  name: Knative Functions
  slug: knative-functions
- description: The Knative CLI (kn) provides a command-line interface for creating and managing Knative resources including Services, Revisions, Routes, event sources, and Brokers. It simplifies tasks like traffic s
  name: Knative CLI (kn)
  slug: knative-cli
- description: The Apis API from Knative — 2 operation(s) for apis.
  name: Knative Apis API
  slug: knative-apis-api
- description: Knative Broker resources collect pools of events that can be consumed using Triggers. Brokers provide event routing with filtering, guaranteed delivery, and dead-letter sink support. The default broke
  name: Knative Brokers API
  slug: knative-brokers-api
- description: Knative Channel resources represent a generic pub/sub messaging channel. Channels receive events and fan them out to all Subscriptions. The default channel implementation uses an in-memory channel.
  name: Knative Channels API
  slug: knative-channels-api
- description: Knative Configuration resources maintain the desired state for a deployment by capturing container templates. Each update to a Configuration creates a new immutable Revision.
  name: Knative Configurations API
  slug: knative-configurations-api
- description: Knative DomainMapping resources map a custom domain name to a Knative Service, enabling services to be served under custom hostnames with automatic TLS certificate provisioning.
  name: Knative DomainMappings API
  slug: knative-domainmappings-api
- description: Knative event source resources connect external event producers to the eventing mesh. Built-in sources include ApiServerSource for Kubernetes API events, PingSource for scheduled events, and SinkBindi
  name: Knative EventSources API
  slug: knative-eventsources-api
- description: Knative EventType resources maintain a catalog of event types that can be consumed from Brokers. EventTypes help consumers discover what events are available without inspecting Broker contents directl
  name: Knative EventTypes API
  slug: knative-eventtypes-api
- description: Knative Revision resources are immutable snapshots of application code and configuration at a point in time. Revisions are created by Configuration updates and are the actual units that are scaled.
  name: Knative Revisions API
  slug: knative-revisions-api
- description: Knative Route resources manage the network endpoints and traffic distribution across Revisions. Routes support percentage-based traffic splitting for canary deployments and named route targets.
  name: Knative Routes API
  slug: knative-routes-api
- description: Knative Subscription resources define a delivery destination for events sent to a Channel. Each Subscription routes events from a Channel to a subscriber destination with optional reply and dead-lette
  name: Knative Subscriptions API
  slug: knative-subscriptions-api
- description: 'Knative Trigger resources define filtered delivery options for events arriving at a Broker. A Trigger selects events by attribute filters and routes matching events to a destination such as a Knative '
  name: Knative Triggers API
  slug: knative-triggers-api
artifact_total: 38
asyncapis:
- description: Knative Eventing uses HTTP POST requests conforming to the CloudEvents specification to deliver events between event sources, Brokers, Triggers, Channels, and Subscriptions. Events can carry structure
  name: Knative Eventing CloudEvents
  slug: knative-cloudevents-asyncapi
collections:
- collection_type: postman
  name: Knative Eventing Apis API
  slug: postman-knative-apis-api
- collection_type: postman
  name: Knative Eventing Apis Brokers API
  slug: postman-knative-brokers-api
- collection_type: postman
  name: Knative Eventing Apis Channels API
  slug: postman-knative-channels-api
- collection_type: postman
  name: Knative Eventing Apis Configurations API
  slug: postman-knative-configurations-api
- collection_type: postman
  name: Knative Eventing Apis DomainMappings API
  slug: postman-knative-domainmappings-api
- collection_type: postman
  name: Knative Eventing Apis EventSources API
  slug: postman-knative-eventsources-api
- collection_type: postman
  name: Knative Eventing Apis EventTypes API
  slug: postman-knative-eventtypes-api
- collection_type: postman
  name: Knative Eventing Apis Revisions API
  slug: postman-knative-revisions-api
- collection_type: postman
  name: Knative Eventing Apis Routes API
  slug: postman-knative-routes-api
- collection_type: postman
  name: Knative Eventing Apis Subscriptions API
  slug: postman-knative-subscriptions-api
- collection_type: postman
  name: Knative Eventing Apis Triggers API
  slug: postman-knative-triggers-api
- collection_type: open
  name: Knative Eventing API
  slug: open-knative-eventing-api
- collection_type: open
  name: Knative Serving API
  slug: open-knative-serving-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/knative/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knative-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knative-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knative-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/knative
- group: design
  title: ''
  type: JSONLD
  url: json-ld/knative-context.jsonld
- group: company
  title: ''
  type: Website
  url: https://knative.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://knative.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://knative.dev/docs/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://knative.dev/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://knative.dev/docs/reference/relnotes/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knative
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/knative/docs
- group: operate
  title: ''
  type: Community
  url: https://knative.dev/community/
created: '2026-03-16'
description: Knative is a CNCF graduated platform that extends Kubernetes to provide serverless capabilities. It consists of Serving for deploying and scaling serverless workloads with automatic scale-to-zero, and Eventing for building event-driven architectures with declarative event routing and delivery. Knative abstracts away infrastructure complexity so developers can focus on writing code.
finops:
- name: Knative Finops
  service_category: API
  slug: knative-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knative.png
json_schemas:
- name: Knative Eventing Resources
  property_count: 0
  slug: knative-eventing
- name: Knative Serving Resources
  property_count: 0
  slug: knative-serving
jsonld:
- class_count: 2
  name: Knative Context
  property_count: 21
  slug: knative-context
layout: provider
modified: '2026-05-19'
name: Knative
nav: Providers
network: true
overview: 'Knative publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Apis API, Brokers API, Channels API, and 8 more. Tagged areas include Auto-Scaling, Cloud Native, Event-Driven, Graduated, and Kubernetes.


  The Knative catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Knative''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, and 9 more developer resources.'
plans:
- name: Knative Plans Pricing
  plan_count: 3
  slug: knative-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Knative Rate Limits
  slug: knative-rate-limits
rules:
- name: Knative API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 7
  slug: knative-asyncapi-spectral-rules
- name: Knative API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: knative-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.0
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 87.3
    developer_ergonomics: 41.3
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knative/refs/heads/main/screenshots/knative-2026-06-20T184106.png
security:
- kind: authentication
  name: Knative Authentication
  slug: knative-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Knative Domain Security
  slug: knative-domain-security
  summary_line: TLSv1.3 · HSTS
slug: knative
tags:
- Auto-Scaling
- Cloud Native
- Event-Driven
- Graduated
- Kubernetes
- Serverless
website: https://knative.dev/
---
