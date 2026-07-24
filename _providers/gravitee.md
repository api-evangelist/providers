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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 193
  human_in_the_loop: 11
  name: Gravitee Agentic Access
  operation_count: 381
  slug: gravitee-agentic-access
  summary_line: 381 operations · 193 acting · 11 human-in-the-loop
api_count: 55
apis:
- description: Gravitee Cockpit is the multi-environment, multi-installation control plane for Gravitee. It centralizes management of multiple APIM and AM installations (dev, staging, prod, regions) into one console
  name: Gravitee Cockpit
  slug: gravitee-cockpit
- description: Gravitee Alert Engine (AE) is a real-time API monitoring solution that tracks performance, availability, errors, quota approach, and security events across all Gravitee gateways. It evaluates conditio
  name: Gravitee Alert Engine
  slug: gravitee-alert-engine
- description: Gravitee AI Agent Management brings the API management discipline to agentic AI ecosystems. It is delivered as an Enterprise add-on package and includes an LLM Proxy (model routing, prompt-token track
  name: Gravitee AI Agent Management
  slug: gravitee-ai-agent-management
- description: The Gravitee Kafka Gateway brings full API management discipline to Apache Kafka. It sits in front of one or more Kafka clusters and applies authentication mediation, ACLs, quotas, message filtering a
  name: Gravitee Kafka Gateway
  slug: gravitee-kafka-gateway
- description: The Gravitee Kubernetes Operator (GKO) is a Go-based Kubernetes operator that lets platform teams declare Gravitee APIs, applications, subscriptions, shared policy groups, and management contexts as K
  name: Gravitee Kubernetes Operator
  slug: gravitee-kubernetes-operator
- description: The alerts API from Gravitee — 3 operation(s) for alerts.
  name: Gravitee alerts API
  slug: gravitee-alerts-api
- description: Query analytics, time-series, and dashboards
  name: Gravitee Analytics API
  slug: gravitee-analytics-api
- description: Bundle one or more APIs into a publishable API product
  name: Gravitee API Products API
  slug: gravitee-api-products-api
- description: Manage APIs (v2 and v4 message-oriented APIs)
  name: Gravitee APIs API
  slug: gravitee-apis-api
- description: The application API from Gravitee — 22 operation(s) for application.
  name: Gravitee application API
  slug: gravitee-application-api
- description: Manage consumer applications
  name: Gravitee Applications API
  slug: gravitee-applications-api
- description: The audit API from Gravitee — 4 operation(s) for audit.
  name: Gravitee audit API
  slug: gravitee-audit-api
- description: The Authentication Device Notifier API from Gravitee — 5 operation(s) for authentication device notifier.
  name: Gravitee Authentication Device Notifier API
  slug: gravitee-authentication-device-notifier-api
- description: The Authorization Engine API from Gravitee — 5 operation(s) for authorization engine.
  name: Gravitee Authorization Engine API
  slug: gravitee-authorization-engine-api
- description: The Bot Detection API from Gravitee — 5 operation(s) for bot detection.
  name: Gravitee Bot Detection API
  slug: gravitee-bot-detection-api
- description: The Certificate API from Gravitee — 8 operation(s) for certificate.
  name: Gravitee Certificate API
  slug: gravitee-certificate-api
- description: The data-sources API from Gravitee — 1 operation(s) for data-sources.
  name: Gravitee data-sources API
  slug: gravitee-data-sources-api
- description: The dataPlane API from Gravitee — 1 operation(s) for dataplane.
  name: Gravitee dataPlane API
  slug: gravitee-dataplane-api
- description: The Device Identifier API from Gravitee — 3 operation(s) for device identifier.
  name: Gravitee Device Identifier API
  slug: gravitee-device-identifier-api
- description: The device identifiers API from Gravitee — 2 operation(s) for device identifiers.
  name: Gravitee device identifiers API
  slug: gravitee-device-identifiers-api
- description: The devices API from Gravitee — 2 operation(s) for devices.
  name: Gravitee devices API
  slug: gravitee-devices-api
- description: The dictionary API from Gravitee — 3 operation(s) for dictionary.
  name: Gravitee dictionary API
  slug: gravitee-dictionary-api
- description: The domain API from Gravitee — 120 operation(s) for domain.
  name: Gravitee domain API
  slug: gravitee-domain-api
- description: The email API from Gravitee — 4 operation(s) for email.
  name: Gravitee email API
  slug: gravitee-email-api
- description: The entrypoints API from Gravitee — 2 operation(s) for entrypoints.
  name: Gravitee entrypoints API
  slug: gravitee-entrypoints-api
- description: The Extension Grant API from Gravitee — 5 operation(s) for extension grant.
  name: Gravitee Extension Grant API
  slug: gravitee-extension-grant-api
- description: The Factor API from Gravitee — 5 operation(s) for factor.
  name: Gravitee Factor API
  slug: gravitee-factor-api
- description: The flow API from Gravitee — 2 operation(s) for flow.
  name: Gravitee flow API
  slug: gravitee-flow-api
- description: The form API from Gravitee — 7 operation(s) for form.
  name: Gravitee form API
  slug: gravitee-form-api
- description: The group API from Gravitee — 10 operation(s) for group.
  name: Gravitee group API
  slug: gravitee-group-api
- description: The Identity Provider API from Gravitee — 8 operation(s) for identity provider.
  name: Gravitee Identity Provider API
  slug: gravitee-identity-provider-api
- description: Manage organizations, environments, and platform installation
  name: Gravitee Installation API
  slug: gravitee-installation-api
- description: Search request and error logs
  name: Gravitee Logs API
  slug: gravitee-logs-api
- description: The Newsletter API from Gravitee — 2 operation(s) for newsletter.
  name: Gravitee Newsletter API
  slug: gravitee-newsletter-api
- description: The Notifier API from Gravitee — 3 operation(s) for notifier.
  name: Gravitee Notifier API
  slug: gravitee-notifier-api
- description: The Organizations API from Gravitee — 5 operation(s) for organizations.
  name: Gravitee Organizations API
  slug: gravitee-organizations-api
- description: The Password Policy API from Gravitee — 5 operation(s) for password policy.
  name: Gravitee Password Policy API
  slug: gravitee-password-policy-api
- description: Manage plans (Keyless, API Key, OAuth2, JWT, mTLS, Push)
  name: Gravitee Plans API
  slug: gravitee-plans-api
- description: The platform API from Gravitee — 45 operation(s) for platform.
  name: Gravitee platform API
  slug: gravitee-platform-api
- description: The Plugin API from Gravitee — 37 operation(s) for plugin.
  name: Gravitee Plugin API
  slug: gravitee-plugin-api
- description: Discover policies, endpoints, entrypoints, and resources installed in the gateway
  name: Gravitee Plugins API
  slug: gravitee-plugins-api
- description: The Policy API from Gravitee — 4 operation(s) for policy.
  name: Gravitee Policy API
  slug: gravitee-policy-api
- description: The preview API from Gravitee — 1 operation(s) for preview.
  name: Gravitee preview API
  slug: gravitee-preview-api
- description: The protected-resource API from Gravitee — 8 operation(s) for protected-resource.
  name: Gravitee protected-resource API
  slug: gravitee-protected-resource-api
- description: The Reporter API from Gravitee — 7 operation(s) for reporter.
  name: Gravitee Reporter API
  slug: gravitee-reporter-api
- description: The Resource API from Gravitee — 5 operation(s) for resource.
  name: Gravitee Resource API
  slug: gravitee-resource-api
- description: The role API from Gravitee — 4 operation(s) for role.
  name: Gravitee role API
  slug: gravitee-role-api
- description: The scope API from Gravitee — 2 operation(s) for scope.
  name: Gravitee scope API
  slug: gravitee-scope-api
- description: The sharding-tags API from Gravitee — 2 operation(s) for sharding-tags.
  name: Gravitee sharding-tags API
  slug: gravitee-sharding-tags-api
- description: Manage subscriptions between applications and plans
  name: Gravitee Subscriptions API
  slug: gravitee-subscriptions-api
- description: The theme API from Gravitee — 2 operation(s) for theme.
  name: Gravitee theme API
  slug: gravitee-theme-api
- description: Customize developer portal and console themes
  name: Gravitee UI API
  slug: gravitee-ui-api
- description: The user API from Gravitee — 38 operation(s) for user.
  name: Gravitee user API
  slug: gravitee-user-api
- description: The user notifications API from Gravitee — 2 operation(s) for user notifications.
  name: Gravitee user notifications API
  slug: gravitee-user-notifications-api
- description: Manage Gravitee users
  name: Gravitee Users API
  slug: gravitee-users-api
artifact_total: 78
collections:
- collection_type: open
  name: Gravitee.io - Access Management API
  slug: open-gravitee-am
- collection_type: open
  name: Gravitee.io APIM Management API
  slug: open-gravitee-apim
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gravitee-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gravitee-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gravitee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gravitee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gravitee-io
- group: company
  title: ''
  type: Website
  url: https://www.gravitee.io/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.gravitee.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.gravitee.io/apim/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.gravitee.io/blog/all
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gravitee.io/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://documentation.gravitee.io/apim/release-information/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gravitee-io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/gravitee-io/gravitee-api-management
- group: operate
  title: ''
  type: Community
  url: https://community.gravitee.io/
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/gravitee-io/gravitee-api-management/issues
- group: company
  title: ''
  type: Partners
  url: https://www.gravitee.io/partners
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/gravitee-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gravitee-api-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gravitee-plan-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gravitee-domain-schema.json
- group: commercial
  title: ''
  type: Plans
  url: plans/gravitee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gravitee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gravitee-finops.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/api-gateway-operations.yaml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/traffic-observability.yaml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/mcp-publishing.yaml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/api-management.yaml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/access-management.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/gravitee-io/gravitee-apim-mcp-server
crds:
- name: gravitee.io apidefinitions
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_apidefinitions.yaml
- name: gravitee.io apiresources
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_apiresources.yaml
- name: gravitee.io apiv4definitions
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_apiv4definitions.yaml
- name: gravitee.io applications
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_applications.yaml
- name: gravitee.io groups
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_groups.yaml
- name: gravitee.io kafkaroutes
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_kafkaroutes.yaml
- name: gravitee.io managementcontexts
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_managementcontexts.yaml
- name: gravitee.io notifications
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_notifications.yaml
- name: gravitee.io sharedpolicygroups
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_sharedpolicygroups.yaml
- name: gravitee.io subscriptions
  url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/crd/gravitee.io_subscriptions.yaml
created: '2026-03-18'
description: Gravitee.io is an open-source API management platform from GraviteeSource, combining a high-performance API Gateway, full-lifecycle API Management, Access Management (IAM), Cockpit (multi-environment control plane), an Alert Engine, a Kubernetes Operator, and a new AI Agent Management suite with native MCP and LLM-proxy capabilities. The core projects are Apache 2.0 OSS, with an Enterprise commercial offering and a managed Gravitee Cloud SaaS. The platform supports synchronous and asynchronous APIs across REST, GraphQL, WebSocket, gRPC, SSE, Webhooks, Kafka, MQTT, AMQP, and Model Context Protocol (MCP).
examples:
- key_count: 5
  name: Gravitee Am Create Application Example
  slug: gravitee-am-create-application-example
- key_count: 5
  name: Gravitee Am Create Domain Example
  slug: gravitee-am-create-domain-example
- key_count: 5
  name: Gravitee Apim Create Api Example
  slug: gravitee-apim-create-api-example
- key_count: 6
  name: Gravitee Apim Create Plan Example
  slug: gravitee-apim-create-plan-example
- key_count: 3
  name: Gravitee Apim Create Subscription Example
  slug: gravitee-apim-create-subscription-example
- key_count: 14
  name: Gravitee Apim Get Api Example
  slug: gravitee-apim-get-api-example
finops:
- name: Gravitee Finops
  service_category: API Management
  slug: gravitee-finops
graphqls:
- description: ''
  name: Gravitee GraphQL API
  slug: gravitee-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gravitee.png
json_schemas:
- name: Gravitee API
  property_count: 16
  slug: gravitee-api
- name: Gravitee Security Domain
  property_count: 10
  slug: gravitee-domain
- name: Gravitee Plan
  property_count: 6
  slug: gravitee-plan
json_structures:
- name: Gravitee Api Structure
  property_count: 18
  slug: gravitee-api-structure
jsonld:
- class_count: 0
  name: Gravitee Context
  property_count: 10
  slug: gravitee-context
layout: provider
modified: '2026-05-21'
name: Gravitee
nav: Providers
network: true
overview: 'Gravitee publishes 50 APIs on the [APIs.io](https://apis.io/) network, including alerts API, Analytics API, API Products API, and 47 more. Tagged areas include API Gateway, API Management, Access Management, Identity, and Event-Driven.


  The Gravitee catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Gravitee''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, changelog, and 24 more developer resources.'
plans:
- name: Gravitee Plans Pricing
  plan_count: 9
  slug: gravitee-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 5
  name: Gravitee Rate Limits
  slug: gravitee-rate-limits
rules:
- name: Gravitee API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gravitee-jsonschema-spectral-rules
- name: Gravitee API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 1
    info: 0
    warn: 3
  slug: gravitee-rules
score:
  band: developing
  composite: 57.0
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 55.2
    developer_ergonomics: 45.7
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 57.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/screenshots/gravitee-2026-06-20T182344.png
security:
- kind: authentication
  name: Gravitee Authentication
  slug: gravitee-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Gravitee Domain Security
  slug: gravitee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gravitee Trust Center
  slug: gravitee-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: gravitee
tags:
- API Gateway
- API Management
- Access Management
- Identity
- Event-Driven
- Event Management
- Kafka Gateway
- Kafka
- MQTT
- GraphQL
- gRPC
- AI Gateway
- MCP
- A2A
- LLM Proxy
- Multi-Gateway Federation
- Developer Portal
- Open Source
- Apache 2.0
website: https://www.gravitee.io/
---
