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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 389
  human_in_the_loop: 15
  name: Kibana Agentic Access
  operation_count: 612
  slug: kibana-agentic-access
  summary_line: 612 operations · 389 acting · 15 human-in-the-loop
api_count: 60
apis:
- description: The Actions API from Kibana — 1 operation(s) for actions.
  name: Kibana Actions API
  slug: kibana-actions-api
- description: Agent Builder is a set of AI-powered capabilities for developing and interacting with agents that work with your Elasticsearch data. Most users will probably want to integrate with Agent Builder using
  name: Kibana agent builder API
  slug: kibana-agent-builder-api
- description: Alerting enables you to define rules, which detect complex conditions within your data. When a condition is met, the rule tracks it as an alert and runs the actions that are defined in the rule. Actio
  name: Kibana alerting API
  slug: kibana-alerting-api
- description: Adjust APM agent configuration without need to redeploy your application.
  name: Kibana APM agent configuration API
  slug: kibana-apm-agent-configuration-api
- description: Configure APM agent keys to authorize requests from APM agents to the APM Server.
  name: Kibana APM agent keys API
  slug: kibana-apm-agent-keys-api
- description: Annotate visualizations in the APM app with significant events. Annotations enable you to easily see how events are impacting the performance of your applications.
  name: Kibana APM annotations API
  slug: kibana-apm-annotations-api
- description: Create APM fleet server schema.
  name: Kibana APM server schema API
  slug: kibana-apm-server-schema-api
- description: Configure APM source maps. A source map allows minified files to be mapped back to original source code--allowing you to maintain the speed advantage of minified code, without losing the ability to qu
  name: Kibana APM sourcemaps API
  slug: kibana-apm-sourcemaps-api
- description: 'Cases are used to open and track issues. You can add assignees and tags to your cases, set their severity and status, and add alerts, comments, and visualizations. You can also send cases to external '
  name: Kibana cases API
  slug: kibana-cases-api
- description: Connectors provide a central place to store connection information for services and integrations with Elastic or third party systems. Alerting rules can use connectors to run actions when rule conditi
  name: Kibana connectors API
  slug: kibana-connectors-api
- description: Data stream APIs enable you to manage data streams, which are collections of indices that share the same index template and are managed as a single unit for time-series data.
  name: Kibana Data streams API
  slug: kibana-data-streams-api
- description: Data view APIs enable you to manage data views, formerly known as Kibana index patterns.
  name: Kibana data views API
  slug: kibana-data-views-api
- description: Elastic Agent actions APIs enable you to manage actions performed on Elastic Agents, including agent reassignment, diagnostics collection, enrollment management, upgrades, and bulk operations for agen
  name: Kibana Elastic Agent actions API
  slug: kibana-elastic-agent-actions-api
- description: Elastic Agent binary download sources APIs enable you to manage download sources for Elastic Agent binaries, including creating, updating, and deleting custom download sources for agent binaries.
  name: Kibana Elastic Agent binary download sources API
  slug: kibana-elastic-agent-binary-download-sources-api
- description: Elastic Agent policies APIs enable you to manage agent policies, including creating, updating, and deleting policies, as well as to retrieve agent policy outputs, manifests, and auto-upgrade status in
  name: Kibana Elastic Agent policies API
  slug: kibana-elastic-agent-policies-api
- description: Enables you to retrieve status information about Elastic Agents, including health summaries and operational status.
  name: Kibana Elastic Agent status API
  slug: kibana-elastic-agent-status-api
- description: Elastic Agents APIs enable you to manage Elastic Agents, including retrieving agent information, managing agent lifecycle, handling file uploads, and initiating agent setup.
  name: Kibana Elastic Agents API
  slug: kibana-elastic-agents-api
- description: Elastic Package Manager (EPM) APIs enable you to manage packages and integrations, including installing, updating, and uninstalling packages, managing custom integrations, and handling package assets.
  name: Kibana Elastic Package Manager (EPM) API
  slug: kibana-elastic-package-manager-epm-api
- description: The Fleet agentless policies API from Kibana — 2 operation(s) for fleet agentless policies.
  name: Kibana Fleet agentless policies API
  slug: kibana-fleet-agentless-policies-api
- description: The Fleet API from Kibana — 1 operation(s) for fleet.
  name: Kibana Fleet API
  slug: kibana-fleet-api
- description: Fleet cloud connectors APIs enable you to manage Fleet cloud connectors, including creating, updating, and deleting cloud connector configurations for Fleet integrations.
  name: Kibana Fleet cloud connectors API
  slug: kibana-fleet-cloud-connectors-api
- description: Fleet enrollment API keys APIs enable you to manage enrollment API keys for Fleet, including creating, retrieving, and revoking API keys used for agent enrollment.
  name: Kibana Fleet enrollment API keys API
  slug: kibana-fleet-enrollment-api-keys-api
- description: Fleet internals APIs enable you to manage Fleet internal operations, including checking permissions, monitoring Fleet Server health, managing settings, and initiating Fleet setup.
  name: Kibana Fleet internals API
  slug: kibana-fleet-internals-api
- description: Fleet outputs APIs enable you to manage Fleet outputs, including creating, updating, and deleting output configurations, generating Logstash API keys, and monitoring output health.
  name: Kibana Fleet outputs API
  slug: kibana-fleet-outputs-api
- description: Fleet package policies APIs enable you to manage Fleet package policies, including creating, updating, and deleting policies, performing bulk operations, and managing policy upgrades.
  name: Kibana Fleet package policies API
  slug: kibana-fleet-package-policies-api
- description: Fleet proxies APIs enable you to manage Fleet proxies, including creating, updating, and deleting proxy configurations for Fleet agent communication.
  name: Kibana Fleet proxies API
  slug: kibana-fleet-proxies-api
- description: 'Use the Fleet remote synced integrations API to check the status of the automatic integrations synchronization on a remote cluster: * Use the `/api/fleet/remote_synced_integrations/{outputId}/remote_s'
  name: Kibana Fleet remote synced integrations API
  slug: kibana-fleet-remote-synced-integrations-api
- description: Fleet Server hosts APIs enable you to manage Fleet Server hosts, including creating, updating, and deleting Fleet Server host configurations.
  name: Kibana Fleet Server hosts API
  slug: kibana-fleet-server-hosts-api
- description: Enables you to create tokens for Fleet service authentication and authorization.
  name: Kibana Fleet service tokens API
  slug: kibana-fleet-service-tokens-api
- description: Fleet uninstall tokens APIs enable you to manage Fleet uninstall tokens, including retrieving metadata and decrypted tokens for agent uninstallation.
  name: Kibana Fleet uninstall tokens API
  slug: kibana-fleet-uninstall-tokens-api
- description: Programmatically integrate with Logstash configuration management. > warn > Do not directly access the `.logstash` index. The structure of the `.logstash` index is subject to change, which could cause
  name: Kibana logstash API
  slug: kibana-logstash-api
- description: You can schedule single or recurring maintenance windows to temporarily reduce rule notifications. For example, a maintenance window prevents false alarms during planned outages.
  name: Kibana maintenance-window API
  slug: kibana-maintenance-window-api
- description: Enables you to rotate message signing key pairs for secure Fleet communication.
  name: Kibana Message Signing Service API
  slug: kibana-message-signing-service-api
- description: Enables you to synchronize machine learning saved objects.
  name: Kibana ml API
  slug: kibana-ml-api
- description: Interact with the Observability AI Assistant resources.
  name: Kibana observability_ai_assistant API
  slug: kibana-observability-ai-assistant-api
- description: Manage the roles that grant Elasticsearch and Kibana privileges.
  name: Kibana roles API
  slug: kibana-roles-api
- description: Export sets of saved objects that you want to import into Kibana, resolve import errors, and rotate an encryption key for encrypted saved objects with the saved objects APIs. To manage a specific type
  name: Kibana saved objects API
  slug: kibana-saved-objects-api
- description: Manage and interact with Security Assistant resources.
  name: Kibana Security AI Assistant API API
  slug: kibana-security-ai-assistant-api-api
- description: The Security API from Kibana — 1 operation(s) for security.
  name: Kibana Security API
  slug: kibana-security-api
- description: Use the Attack discovery APIs to generate and manage Attack discoveries. Attack Discovery leverages large language models (LLMs) to analyze alerts in your environment and identify threats. Each "disco
  name: Kibana Security Attack discovery API API
  slug: kibana-security-attack-discovery-api-api
- description: Use the detections APIs to create and manage detection rules. Detection rules search events and external alerts sent to Elastic Security and generate detection alerts from any hits. Alerts are display
  name: Kibana Security Detections API API
  slug: kibana-security-detections-api-api
- description: Endpoint Exceptions API allows you to manage detection rule endpoint exceptions to prevent a rule from generating an alert from incoming events even when the rule's other criteria are met.
  name: Kibana Security Endpoint Exceptions API API
  slug: kibana-security-endpoint-exceptions-api-api
- description: Interact with and manage endpoints running the Elastic Defend integration.
  name: Kibana Security Endpoint Management API API
  slug: kibana-security-endpoint-management-api-api
- description: Use the Security entity analytics APIs to manage entity analytics and risk scoring, including asset criticality, privileged user monitoring, and entity engines.
  name: Kibana Security Entity Analytics API API
  slug: kibana-security-entity-analytics-api-api
- description: The Security entity store API from Kibana — 13 operation(s) for security entity store.
  name: Kibana Security entity store API
  slug: kibana-security-entity-store-api
- description: Exceptions are associated with detection and endpoint rules, and are used to prevent a rule from generating an alert from incoming events, even when the rule's other criteria are met. They can help re
  name: Kibana Security Exceptions API API
  slug: kibana-security-exceptions-api-api
- description: 'Lists can be used with detection rule exceptions to define values that prevent a rule from generating alerts. Lists are made up of: * **List containers**: A container for values of the same Elasticsea'
  name: Kibana Security Lists API API
  slug: kibana-security-lists-api-api
- description: Run live queries, manage packs and saved queries.
  name: Kibana Security Osquery API API
  slug: kibana-security-osquery-api-api
- description: You can create Timelines and Timeline templates via the API, as well as import new Timelines from an ndjson file.
  name: Kibana Security Timeline API API
  slug: kibana-security-timeline-api-api
- description: Manage Kibana short URLs.
  name: Kibana short url API
  slug: kibana-short-url-api
- description: SLO APIs enable you to define, manage and track service-level objectives
  name: Kibana slo API
  slug: kibana-slo-api
- description: The Spaces API from Kibana — 7 operation(s) for spaces.
  name: Kibana Spaces API
  slug: kibana-spaces-api
- description: 'Streams provide a unified data management layer for ingestion, routing, and processing. There are three stream types: * **Wired** streams are managed by Kibana. They route documents to child streams b'
  name: Kibana streams API
  slug: kibana-streams-api
- description: Synthetics APIs enable you to check the status of your services and applications.
  name: Kibana synthetics API
  slug: kibana-synthetics-api
- description: Get information about the system status, resource usage, features, and installed plugins.
  name: Kibana system API
  slug: kibana-system-api
- description: Task manager APIs enable you to check the health of the Kibana task manager, which is used by features such as alerting, actions, and reporting to run mission critical work as persistent background ta
  name: Kibana task manager API
  slug: kibana-task-manager-api
- description: 'The Kibana Upgrade Assistant API helps you prepare for the next major Elasticsearch release. > warn > This is a Kibana REST API (not an Elasticsearch API) and requests must target your Kibana URL: > *'
  name: Kibana upgrade API
  slug: kibana-upgrade-api
- description: Uptime APIs enable you to view and update uptime monitoring settings.
  name: Kibana uptime API
  slug: kibana-uptime-api
- description: Enables you to invalidate user sessions for security and session management purposes.
  name: Kibana user session API
  slug: kibana-user-session-api
- description: Workflows enable you to automate multi-step processes directly in Kibana. Define sequences of steps in YAML to transform data insights into automated actions and outcomes, without needing external aut
  name: Kibana workflows API
  slug: kibana-workflows-api
artifact_total: 128
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kibana APIs Actions API
  slug: open-kibana-actions-api
- collection_type: open
  name: Kibana APIs Actions agent builder API
  slug: open-kibana-agent-builder-api
- collection_type: open
  name: Kibana APIs Actions alerting API
  slug: open-kibana-alerting-api
- collection_type: open
  name: Kibana APIs Actions APM agent configuration API
  slug: open-kibana-apm-agent-configuration-api
- collection_type: open
  name: Kibana APIs Actions APM agent keys API
  slug: open-kibana-apm-agent-keys-api
- collection_type: open
  name: Kibana APIs Actions APM annotations API
  slug: open-kibana-apm-annotations-api
- collection_type: open
  name: Kibana APIs Actions APM server schema API
  slug: open-kibana-apm-server-schema-api
- collection_type: open
  name: Kibana APIs Actions APM sourcemaps API
  slug: open-kibana-apm-sourcemaps-api
- collection_type: open
  name: Kibana APIs Actions cases API
  slug: open-kibana-cases-api
- collection_type: open
  name: Kibana APIs Actions connectors API
  slug: open-kibana-connectors-api
- collection_type: open
  name: Kibana APIs Actions Data streams API
  slug: open-kibana-data-streams-api
- collection_type: open
  name: Kibana APIs Actions data views API
  slug: open-kibana-data-views-api
- collection_type: open
  name: Kibana APIs Actions Elastic Agent actions API
  slug: open-kibana-elastic-agent-actions-api
- collection_type: open
  name: Kibana APIs Actions Elastic Agent binary download sources API
  slug: open-kibana-elastic-agent-binary-download-sources-api
- collection_type: open
  name: Kibana APIs Actions Elastic Agent policies API
  slug: open-kibana-elastic-agent-policies-api
- collection_type: open
  name: Kibana APIs Actions Elastic Agent status API
  slug: open-kibana-elastic-agent-status-api
- collection_type: open
  name: Kibana APIs Actions Elastic Agents API
  slug: open-kibana-elastic-agents-api
- collection_type: open
  name: Kibana APIs Actions Elastic Package Manager (EPM) API
  slug: open-kibana-elastic-package-manager-epm-api
- collection_type: open
  name: Kibana APIs Actions Fleet agentless policies API
  slug: open-kibana-fleet-agentless-policies-api
- collection_type: open
  name: Kibana APIs Actions Fleet API
  slug: open-kibana-fleet-api
- collection_type: open
  name: Kibana APIs Actions Fleet cloud connectors API
  slug: open-kibana-fleet-cloud-connectors-api
- collection_type: open
  name: Kibana APIs Actions Fleet enrollment API keys API
  slug: open-kibana-fleet-enrollment-api-keys-api
- collection_type: open
  name: Kibana APIs Actions Fleet internals API
  slug: open-kibana-fleet-internals-api
- collection_type: open
  name: Kibana APIs Actions Fleet outputs API
  slug: open-kibana-fleet-outputs-api
- collection_type: open
  name: Kibana APIs Actions Fleet package policies API
  slug: open-kibana-fleet-package-policies-api
- collection_type: open
  name: Kibana APIs Actions Fleet proxies API
  slug: open-kibana-fleet-proxies-api
- collection_type: open
  name: Kibana APIs Actions Fleet remote synced integrations API
  slug: open-kibana-fleet-remote-synced-integrations-api
- collection_type: open
  name: Kibana APIs Actions Fleet Server hosts API
  slug: open-kibana-fleet-server-hosts-api
- collection_type: open
  name: Kibana APIs Actions Fleet service tokens API
  slug: open-kibana-fleet-service-tokens-api
- collection_type: open
  name: Kibana APIs Actions Fleet uninstall tokens API
  slug: open-kibana-fleet-uninstall-tokens-api
- collection_type: open
  name: Kibana APIs Actions logstash API
  slug: open-kibana-logstash-api
- collection_type: open
  name: Kibana APIs Actions maintenance-window API
  slug: open-kibana-maintenance-window-api
- collection_type: open
  name: Kibana APIs Actions Message Signing Service API
  slug: open-kibana-message-signing-service-api
- collection_type: open
  name: Kibana APIs Actions ml API
  slug: open-kibana-ml-api
- collection_type: open
  name: Kibana APIs Actions observability_ai_assistant API
  slug: open-kibana-observability-ai-assistant-api
- collection_type: open
  name: Kibana APIs Actions roles API
  slug: open-kibana-roles-api
- collection_type: open
  name: Kibana APIs Actions saved objects API
  slug: open-kibana-saved-objects-api
- collection_type: open
  name: Kibana APIs Actions Security AI Assistant API API
  slug: open-kibana-security-ai-assistant-api-api
- collection_type: open
  name: Kibana APIs Actions Security API
  slug: open-kibana-security-api
- collection_type: open
  name: Kibana APIs Actions Security Attack discovery API API
  slug: open-kibana-security-attack-discovery-api-api
- collection_type: open
  name: Kibana APIs Actions Security Detections API API
  slug: open-kibana-security-detections-api-api
- collection_type: open
  name: Kibana APIs Actions Security Endpoint Exceptions API API
  slug: open-kibana-security-endpoint-exceptions-api-api
- collection_type: open
  name: Kibana APIs Actions Security Endpoint Management API API
  slug: open-kibana-security-endpoint-management-api-api
- collection_type: open
  name: Kibana APIs Actions Security Entity Analytics API API
  slug: open-kibana-security-entity-analytics-api-api
- collection_type: open
  name: Kibana APIs Actions Security entity store API
  slug: open-kibana-security-entity-store-api
- collection_type: open
  name: Kibana APIs Actions Security Exceptions API API
  slug: open-kibana-security-exceptions-api-api
- collection_type: open
  name: Kibana APIs Actions Security Lists API API
  slug: open-kibana-security-lists-api-api
- collection_type: open
  name: Kibana APIs Actions Security Osquery API API
  slug: open-kibana-security-osquery-api-api
- collection_type: open
  name: Kibana APIs Actions Security Timeline API API
  slug: open-kibana-security-timeline-api-api
- collection_type: open
  name: Kibana APIs Actions short url API
  slug: open-kibana-short-url-api
- collection_type: open
  name: Kibana APIs Actions slo API
  slug: open-kibana-slo-api
- collection_type: open
  name: Kibana APIs Actions Spaces API
  slug: open-kibana-spaces-api
- collection_type: open
  name: Kibana APIs Actions streams API
  slug: open-kibana-streams-api
- collection_type: open
  name: Kibana APIs Actions synthetics API
  slug: open-kibana-synthetics-api
- collection_type: open
  name: Kibana APIs Actions system API
  slug: open-kibana-system-api
- collection_type: open
  name: Kibana APIs Actions task manager API
  slug: open-kibana-task-manager-api
- collection_type: open
  name: Kibana APIs Actions upgrade API
  slug: open-kibana-upgrade-api
- collection_type: open
  name: Kibana APIs Actions uptime API
  slug: open-kibana-uptime-api
- collection_type: open
  name: Kibana APIs Actions user session API
  slug: open-kibana-user-session-api
- collection_type: open
  name: Kibana APIs Actions workflows API
  slug: open-kibana-workflows-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kibana-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kibana-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kibana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kibana-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co/kibana
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/guide/en/kibana/current/index.html
- group: docs
  title: ''
  type: APIDocumentation
  url: https://www.elastic.co/guide/en/kibana/current/api.html
- group: other
  title: ''
  type: Downloads
  url: https://www.elastic.co/downloads/kibana
- group: build
  title: ''
  type: GitHub
  url: https://github.com/elastic/kibana
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/blog/category/kibana
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.elastic.co/support
- group: operate
  title: ''
  type: Forums
  url: https://discuss.elastic.co/c/kibana
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elastic.co/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elastic.co/legal/privacy-statement
created: '2024-01-15'
description: Kibana is an open-source data visualization and exploration tool used for log and time-series analytics, application monitoring, and operational intelligence. Kibana provides histograms, line graphs, pie charts, heat maps, geospatial visualizations, dashboards, alerting, and management of saved objects across spaces, exposing a comprehensive REST API for programmatic configuration and automation.
finops:
- name: Kibana Finops
  service_category: API
  slug: kibana-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kibana.png
layout: provider
modified: '2026-05-19'
name: Kibana
nav: Providers
network: true
overview: 'Kibana publishes 60 APIs on the [APIs.io](https://apis.io/) network, including Actions API, agent builder API, alerting API, and 57 more. Tagged areas include Alerting, Analytics, Dashboards, Elastic Stack, and Logging.


  Kibana''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Kibana Plans Pricing
  plan_count: 3
  slug: kibana-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Kibana Rate Limits
  slug: kibana-rate-limits
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 58.7
    developer_ergonomics: 32.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 60
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kibana/refs/heads/main/screenshots/kibana-2026-06-20T184031.png
security:
- kind: authentication
  name: Kibana Authentication
  slug: kibana-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Kibana Domain Security
  slug: kibana-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Kibana Trust Center
  slug: kibana-trust-center
  summary_line: GDPR
slug: kibana
tags:
- Alerting
- Analytics
- Dashboards
- Elastic Stack
- Logging
- Monitoring
- Observability
- Visualization
website: https://www.elastic.co/kibana
---
