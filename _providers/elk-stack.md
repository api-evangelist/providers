---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · Free trial
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: true
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1137
  human_in_the_loop: 57
  name: Elk Stack Agentic Access
  operation_count: 1873
  slug: elk-stack-agentic-access
  summary_line: 1873 operations · 1137 acting · 57 human-in-the-loop
api_count: 3
apis:
- description: The Elastic Cloud control-plane API creates, scales, upgrades and deletes Elasticsearch and Kibana deployments, and manages accounts, organizations, IAM, traffic filters, extensions, deployment templa
  name: Elastic Cloud API
  slug: elastic-cloud-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Accounts API from Elastic Stack (ELK Stack) — 1 operation(s) for accounts.
  name: Elastic Stack (ELK Stack) Accounts API
  slug: elk-stack-accounts-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Actions API from Elastic Stack (ELK Stack) — 1 operation(s) for actions.
  name: Elastic Stack (ELK Stack) Actions API
  slug: elk-stack-actions-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Agent Builder is a set of AI-powered capabilities for developing and interacting with agents that work with your Elasticsearch data. Most users will probably want to integrate with Agent Builder using
  name: Elastic Stack (ELK Stack) agent builder API
  slug: elk-stack-agent-builder-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Alerting enables you to define rules, which detect complex conditions within your data. When a condition is met, the rule tracks it as an alert and runs the actions that are defined in the rule. Actio
  name: Elastic Stack (ELK Stack) Alerting API
  slug: elk-stack-alerting-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Alerting V2 is an ES|QL-first alerting API for managing rules, alert actions, and action policies. Use these endpoints to create and manage detection rules, act on alerts, and control when and how not
  name: Elastic Stack (ELK Stack) Alerting V2 API
  slug: elk-stack-alerting-v2-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The analytics API from Elastic Stack (ELK Stack) — 3 operation(s) for analytics.
  name: Elastic Stack (ELK Stack) Analytics API
  slug: elk-stack-analytics-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Adjust APM agent configuration without need to redeploy your application.
  name: Elastic Stack (ELK Stack) APM agent configuration API
  slug: elk-stack-apm-agent-configuration-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Configure APM agent keys to authorize requests from APM agents to the APM Server.
  name: Elastic Stack (ELK Stack) APM agent keys API
  slug: elk-stack-apm-agent-keys-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Annotate visualizations in the APM app with significant events. Annotations enable you to easily see how events are impacting the performance of your applications.
  name: Elastic Stack (ELK Stack) APM annotations API
  slug: elk-stack-apm-annotations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Create APM fleet server schema.
  name: Elastic Stack (ELK Stack) APM server schema API
  slug: elk-stack-apm-server-schema-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Configure APM source maps. A source map allows minified files to be mapped back to original source code--allowing you to maintain the speed advantage of minified code, without losing the ability to qu
  name: Elastic Stack (ELK Stack) APM sourcemaps API
  slug: elk-stack-apm-sourcemaps-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Authentication API from Elastic Stack (ELK Stack) — 12 operation(s) for authentication.
  name: Elastic Stack (ELK Stack) Authentication API
  slug: elk-stack-authentication-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The BillingCostsAnalysis API from Elastic Stack (ELK Stack) — 6 operation(s) for billingcostsanalysis.
  name: Elastic Stack (ELK Stack) Billing Costs Analysis API
  slug: elk-stack-billingcostsanalysis-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: 'Cases are used to open and track issues. You can add assignees and tags to your cases, set their severity and status, and add alerts, comments, and visualizations. You can also send cases to external '
  name: Elastic Stack (ELK Stack) Cases API
  slug: elk-stack-cases-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The cat API from Elastic Stack (ELK Stack) — 45 operation(s) for cat.
  name: Elastic Stack (ELK Stack) Cat API
  slug: elk-stack-cat-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ccr API from Elastic Stack (ELK Stack) — 12 operation(s) for ccr.
  name: Elastic Stack (ELK Stack) Ccr API
  slug: elk-stack-ccr-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The cluster API from Elastic Stack (ELK Stack) — 35 operation(s) for cluster.
  name: Elastic Stack (ELK Stack) Cluster API
  slug: elk-stack-cluster-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Comments API from Elastic Stack (ELK Stack) — 2 operation(s) for comments.
  name: Elastic Stack (ELK Stack) Comments API
  slug: elk-stack-comments-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The connector API from Elastic Stack (ELK Stack) — 24 operation(s) for connector.
  name: Elastic Stack (ELK Stack) Connector API
  slug: elk-stack-connector-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Connectors provide a central place to store connection information for services and integrations with Elastic or third party systems. Alerting rules can use connectors to run actions when rule conditi
  name: Elastic Stack (ELK Stack) Connectors API
  slug: elk-stack-connectors-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: '> This documentation is temporarily hosted at a separate location. > > **[View the full Dashboards API reference →](https://elastic.github.io/dashboards-api-spec/dashboards#tag/Dashboards)**'
  name: Elastic Stack (ELK Stack) Dashboards API
  slug: elk-stack-dashboards-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The data stream API from Elastic Stack (ELK Stack) — 14 operation(s) for data stream.
  name: Elastic Stack (ELK Stack) data stream API
  slug: elk-stack-data-stream-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Data stream APIs enable you to manage data streams, which are collections of indices that share the same index template and are managed as a single unit for time-series data.
  name: Elastic Stack (ELK Stack) Data streams API
  slug: elk-stack-data-streams-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Data view APIs enable you to manage data views, formerly known as Kibana index patterns.
  name: Elastic Stack (ELK Stack) data views API
  slug: elk-stack-data-views-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Deployments API from Elastic Stack (ELK Stack) — 58 operation(s) for deployments.
  name: Elastic Stack (ELK Stack) Deployments API
  slug: elk-stack-deployments-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The DeploymentsTrafficFilter API from Elastic Stack (ELK Stack) — 8 operation(s) for deploymentstrafficfilter.
  name: Elastic Stack (ELK Stack) Deployments Traffic Filter API
  slug: elk-stack-deploymentstrafficfilter-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The DeploymentTemplates API from Elastic Stack (ELK Stack) — 2 operation(s) for deploymenttemplates.
  name: Elastic Stack (ELK Stack) Deployment Templates API
  slug: elk-stack-deploymenttemplates-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The document API from Elastic Stack (ELK Stack) — 19 operation(s) for document.
  name: Elastic Stack (ELK Stack) Document API
  slug: elk-stack-document-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Agent actions APIs enable you to manage actions performed on Elastic Agents, including agent reassignment, diagnostics collection, enrollment management, upgrades, and bulk operations for agen
  name: Elastic Stack (ELK Stack) Elastic Agent actions API
  slug: elk-stack-elastic-agent-actions-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Agent binary download sources APIs enable you to manage download sources for Elastic Agent binaries, including creating, updating, and deleting custom download sources for agent binaries.
  name: Elastic Stack (ELK Stack) Elastic Agent binary download sources API
  slug: elk-stack-elastic-agent-binary-download-sources-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Agent policies APIs enable you to manage agent policies, including creating, updating, and deleting policies, as well as to retrieve agent policy outputs, manifests, and auto-upgrade status in
  name: Elastic Stack (ELK Stack) Elastic Agent policies API
  slug: elk-stack-elastic-agent-policies-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Enables you to retrieve status information about Elastic Agents, including health summaries and operational status.
  name: Elastic Stack (ELK Stack) Elastic Agent status API
  slug: elk-stack-elastic-agent-status-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Agents APIs enable you to manage Elastic Agents, including retrieving agent information, managing agent lifecycle, handling file uploads, and initiating agent setup.
  name: Elastic Stack (ELK Stack) Elastic Agents API
  slug: elk-stack-elastic-agents-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Package Manager (EPM) APIs enable you to manage packages and integrations, including installing, updating, and uninstalling packages, managing custom integrations, and handling package assets.
  name: Elastic Stack (ELK Stack) Elastic Package Manager (EPM) API
  slug: elk-stack-elastic-package-manager-epm-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The enrich API from Elastic Stack (ELK Stack) — 4 operation(s) for enrich.
  name: Elastic Stack (ELK Stack) Enrich API
  slug: elk-stack-enrich-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The eql API from Elastic Stack (ELK Stack) — 3 operation(s) for eql.
  name: Elastic Stack (ELK Stack) Eql API
  slug: elk-stack-eql-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The esql API from Elastic Stack (ELK Stack) — 12 operation(s) for esql.
  name: Elastic Stack (ELK Stack) Esql API
  slug: elk-stack-esql-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Extensions API from Elastic Stack (ELK Stack) — 2 operation(s) for extensions.
  name: Elastic Stack (ELK Stack) Extensions API
  slug: elk-stack-extensions-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The features API from Elastic Stack (ELK Stack) — 2 operation(s) for features.
  name: Elastic Stack (ELK Stack) Features API
  slug: elk-stack-features-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Fleet agentless policies API from Elastic Stack (ELK Stack) — 4 operation(s) for fleet agentless policies.
  name: Elastic Stack (ELK Stack) Fleet agentless policies API
  slug: elk-stack-fleet-agentless-policies-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The fleet API from Elastic Stack (ELK Stack) — 4 operation(s) for fleet.
  name: Elastic Stack (ELK Stack) Fleet API
  slug: elk-stack-fleet-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet cloud connectors APIs enable you to manage Fleet cloud connectors, including creating, updating, and deleting cloud connector configurations for Fleet integrations.
  name: Elastic Stack (ELK Stack) Fleet cloud connectors API
  slug: elk-stack-fleet-cloud-connectors-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet enrollment API keys APIs enable you to manage enrollment API keys for Fleet, including creating, retrieving, and revoking API keys used for agent enrollment.
  name: Elastic Stack (ELK Stack) Fleet enrollment API keys API
  slug: elk-stack-fleet-enrollment-api-keys-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet internals APIs enable you to manage Fleet internal operations, including checking permissions, monitoring Fleet Server health, managing settings, and initiating Fleet setup.
  name: Elastic Stack (ELK Stack) Fleet internals API
  slug: elk-stack-fleet-internals-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Fleet managed integrations API from Elastic Stack (ELK Stack) — 4 operation(s) for fleet managed integrations.
  name: Elastic Stack (ELK Stack) Fleet managed integrations API
  slug: elk-stack-fleet-managed-integrations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet outputs APIs enable you to manage Fleet outputs, including creating, updating, and deleting output configurations, generating Logstash API keys, and monitoring output health.
  name: Elastic Stack (ELK Stack) Fleet outputs API
  slug: elk-stack-fleet-outputs-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet package policies APIs enable you to manage Fleet package policies, including creating, updating, and deleting policies, performing bulk operations, and managing policy upgrades.
  name: Elastic Stack (ELK Stack) Fleet package policies API
  slug: elk-stack-fleet-package-policies-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet proxies APIs enable you to manage Fleet proxies, including creating, updating, and deleting proxy configurations for Fleet agent communication.
  name: Elastic Stack (ELK Stack) Fleet proxies API
  slug: elk-stack-fleet-proxies-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: 'Use the Fleet remote synced integrations API to check the status of the automatic integrations synchronization on a remote cluster: * Use the `/api/fleet/remote_synced_integrations/{outputId}/remote_s'
  name: Elastic Stack (ELK Stack) Fleet remote synced integrations API
  slug: elk-stack-fleet-remote-synced-integrations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet Server hosts APIs enable you to manage Fleet Server hosts, including creating, updating, and deleting Fleet Server host configurations.
  name: Elastic Stack (ELK Stack) Fleet Server hosts API
  slug: elk-stack-fleet-server-hosts-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Enables you to create tokens for Fleet service authentication and authorization.
  name: Elastic Stack (ELK Stack) Fleet service tokens API
  slug: elk-stack-fleet-service-tokens-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet uninstall tokens APIs enable you to manage Fleet uninstall tokens, including retrieving metadata and decrypted tokens for agent uninstallation.
  name: Elastic Stack (ELK Stack) Fleet uninstall tokens API
  slug: elk-stack-fleet-uninstall-tokens-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The graph API from Elastic Stack (ELK Stack) — 1 operation(s) for graph.
  name: Elastic Stack (ELK Stack) Graph API
  slug: elk-stack-graph-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The health_report API from Elastic Stack (ELK Stack) — 2 operation(s) for health_report.
  name: Elastic Stack (ELK Stack) Health Report API
  slug: elk-stack-health-report-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The IamService API from Elastic Stack (ELK Stack) — 31 operation(s) for iamservice.
  name: Elastic Stack (ELK Stack) Iam Service API
  slug: elk-stack-iamservice-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ilm API from Elastic Stack (ELK Stack) — 10 operation(s) for ilm.
  name: Elastic Stack (ELK Stack) Ilm API
  slug: elk-stack-ilm-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The indices API from Elastic Stack (ELK Stack) — 63 operation(s) for indices.
  name: Elastic Stack (ELK Stack) Indices API
  slug: elk-stack-indices-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The inference API from Elastic Stack (ELK Stack) — 40 operation(s) for inference.
  name: Elastic Stack (ELK Stack) Inference API
  slug: elk-stack-inference-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The info API from Elastic Stack (ELK Stack) — 1 operation(s) for info.
  name: Elastic Stack (ELK Stack) Info API
  slug: elk-stack-info-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ingest API from Elastic Stack (ELK Stack) — 12 operation(s) for ingest.
  name: Elastic Stack (ELK Stack) Ingest API
  slug: elk-stack-ingest-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The license API from Elastic Stack (ELK Stack) — 5 operation(s) for license.
  name: Elastic Stack (ELK Stack) License API
  slug: elk-stack-license-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Links API from Elastic Stack (ELK Stack) — 2 operation(s) for links.
  name: Elastic Stack (ELK Stack) Links API
  slug: elk-stack-links-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The logstash API from Elastic Stack (ELK Stack) — 4 operation(s) for logstash.
  name: Elastic Stack (ELK Stack) Logstash API
  slug: elk-stack-logstash-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: You can schedule single or recurring maintenance windows to temporarily reduce rule notifications. For example, a maintenance window prevents false alarms during planned outages.
  name: Elastic Stack (ELK Stack) Maintenance Window API
  slug: elk-stack-maintenance-window-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Markdowns API from Elastic Stack (ELK Stack) — 2 operation(s) for markdowns.
  name: Elastic Stack (ELK Stack) Markdowns API
  slug: elk-stack-markdowns-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Enables you to rotate message signing key pairs for secure Fleet communication.
  name: Elastic Stack (ELK Stack) Message Signing Service API
  slug: elk-stack-message-signing-service-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The migration API from Elastic Stack (ELK Stack) — 7 operation(s) for migration.
  name: Elastic Stack (ELK Stack) Migration API
  slug: elk-stack-migration-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ml anomaly API from Elastic Stack (ELK Stack) — 45 operation(s) for ml anomaly.
  name: Elastic Stack (ELK Stack) ml anomaly API
  slug: elk-stack-ml-anomaly-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ml API from Elastic Stack (ELK Stack) — 7 operation(s) for ml.
  name: Elastic Stack (ELK Stack) Ml API
  slug: elk-stack-ml-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ml data frame API from Elastic Stack (ELK Stack) — 12 operation(s) for ml data frame.
  name: Elastic Stack (ELK Stack) ml data frame API
  slug: elk-stack-ml-data-frame-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ml trained model API from Elastic Stack (ELK Stack) — 12 operation(s) for ml trained model.
  name: Elastic Stack (ELK Stack) ml trained model API
  slug: elk-stack-ml-trained-model-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Interact with the Observability AI Assistant resources.
  name: Elastic Stack (ELK Stack) Observability AI Assistant API
  slug: elk-stack-observability-ai-assistant-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Organizations API from Elastic Stack (ELK Stack) — 15 operation(s) for organizations.
  name: Elastic Stack (ELK Stack) Organizations API
  slug: elk-stack-organizations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Platform API from Elastic Stack (ELK Stack) — 3 operation(s) for platform.
  name: Elastic Stack (ELK Stack) Platform API
  slug: elk-stack-platform-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationInstances API from Elastic Stack (ELK Stack) — 2 operation(s) for platformconfigurationinstances.
  name: Elastic Stack (ELK Stack) Platform Configuration Instances API
  slug: elk-stack-platformconfigurationinstances-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationNetworking API from Elastic Stack (ELK Stack) — 2 operation(s) for platformconfigurationnetworking.
  name: Elastic Stack (ELK Stack) Platform Configuration Networking API
  slug: elk-stack-platformconfigurationnetworking-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationSecurity API from Elastic Stack (ELK Stack) — 12 operation(s) for platformconfigurationsecurity.
  name: Elastic Stack (ELK Stack) Platform Configuration Security API
  slug: elk-stack-platformconfigurationsecurity-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationSnapshots API from Elastic Stack (ELK Stack) — 2 operation(s) for platformconfigurationsnapshots.
  name: Elastic Stack (ELK Stack) Platform Configuration Snapshots API
  slug: elk-stack-platformconfigurationsnapshots-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationTemplates API from Elastic Stack (ELK Stack) — 1 operation(s) for platformconfigurationtemplates.
  name: Elastic Stack (ELK Stack) Platform Configuration Templates API
  slug: elk-stack-platformconfigurationtemplates-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationTrustRelationships API from Elastic Stack (ELK Stack) — 2 operation(s) for platformconfigurationtrustrelationships.
  name: Elastic Stack (ELK Stack) Platform Configuration Trust Relationships API
  slug: elk-stack-platformconfigurationtrustrelationships-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformInfrastructure API from Elastic Stack (ELK Stack) — 51 operation(s) for platforminfrastructure.
  name: Elastic Stack (ELK Stack) Platform Infrastructure API
  slug: elk-stack-platforminfrastructure-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The query_rules API from Elastic Stack (ELK Stack) — 4 operation(s) for query_rules.
  name: Elastic Stack (ELK Stack) Query Rules API
  slug: elk-stack-query-rules-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The reindex API from Elastic Stack (ELK Stack) — 3 operation(s) for reindex.
  name: Elastic Stack (ELK Stack) Reindex API
  slug: elk-stack-reindex-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Manage the roles that grant Elasticsearch and Kibana privileges.
  name: Elastic Stack (ELK Stack) Roles API
  slug: elk-stack-roles-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The rollup API from Elastic Stack (ELK Stack) — 8 operation(s) for rollup.
  name: Elastic Stack (ELK Stack) Rollup API
  slug: elk-stack-rollup-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Export sets of saved objects that you want to import into Kibana, resolve import errors, and rotate an encryption key for encrypted saved objects with the saved objects APIs. To manage a specific type
  name: Elastic Stack (ELK Stack) saved objects API
  slug: elk-stack-saved-objects-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The script API from Elastic Stack (ELK Stack) — 5 operation(s) for script.
  name: Elastic Stack (ELK Stack) Script API
  slug: elk-stack-script-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The search API from Elastic Stack (ELK Stack) — 29 operation(s) for search.
  name: Elastic Stack (ELK Stack) Search API
  slug: elk-stack-search-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The search_application API from Elastic Stack (ELK Stack) — 4 operation(s) for search_application.
  name: Elastic Stack (ELK Stack) Search Application API
  slug: elk-stack-search-application-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The searchable_snapshots API from Elastic Stack (ELK Stack) — 7 operation(s) for searchable_snapshots.
  name: Elastic Stack (ELK Stack) Searchable Snapshots API
  slug: elk-stack-searchable-snapshots-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Manage and interact with Security Assistant resources.
  name: Elastic Stack (ELK Stack) Security AI Assistant API
  slug: elk-stack-security-ai-assistant-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The security API from Elastic Stack (ELK Stack) — 64 operation(s) for security.
  name: Elastic Stack (ELK Stack) Security API
  slug: elk-stack-security-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Use the Attack discovery APIs to generate and manage Attack discoveries. Attack Discovery leverages large language models (LLMs) to analyze alerts in your environment and identify threats. Each "disco
  name: Elastic Stack (ELK Stack) Security Attack discovery API
  slug: elk-stack-security-attack-discovery-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Use the detections APIs to create and manage detection rules. Detection rules search events and external alerts sent to Elastic Security and generate detection alerts from any hits. Alerts are display
  name: Elastic Stack (ELK Stack) Security Detections API
  slug: elk-stack-security-detections-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Endpoint Exceptions API allows you to manage detection rule endpoint exceptions to prevent a rule from generating an alert from incoming events even when the rule's other criteria are met.
  name: Elastic Stack (ELK Stack) Security Endpoint Exceptions API
  slug: elk-stack-security-endpoint-exceptions-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Interact with and manage endpoints running the Elastic Defend integration.
  name: Elastic Stack (ELK Stack) Security Endpoint Management API
  slug: elk-stack-security-endpoint-management-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Use the Security entity analytics APIs to manage entity analytics and risk scoring, including asset criticality, privileged user monitoring, and entity engines.
  name: Elastic Stack (ELK Stack) Security Entity Analytics API
  slug: elk-stack-security-entity-analytics-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Security entity store API from Elastic Stack (ELK Stack) — 16 operation(s) for security entity store.
  name: Elastic Stack (ELK Stack) Security entity store API
  slug: elk-stack-security-entity-store-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Exceptions are associated with detection and endpoint rules, and are used to prevent a rule from generating an alert from incoming events, even when the rule's other criteria are met. They can help re
  name: Elastic Stack (ELK Stack) Security Exceptions API
  slug: elk-stack-security-exceptions-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: 'Lists can be used with detection rule exceptions to define values that prevent a rule from generating alerts. Lists are made up of: * **List containers**: A container for values of the same Elasticsea'
  name: Elastic Stack (ELK Stack) Security Lists API
  slug: elk-stack-security-lists-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Run live queries, manage packs and saved queries.
  name: Elastic Stack (ELK Stack) Security Osquery API
  slug: elk-stack-security-osquery-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Use the initialization API to set up the assets Elastic Security needs to operate in a Kibana space. A single request can run one or more initialization flows. Each flow provisions a specific set of a
  name: Elastic Stack (ELK Stack) Security Solution Initialization API
  slug: elk-stack-security-solution-initialization-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: You can create Timelines and Timeline templates via the API, as well as import new Timelines from an ndjson file.
  name: Elastic Stack (ELK Stack) Security Timeline API
  slug: elk-stack-security-timeline-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Manage Kibana short URLs.
  name: Elastic Stack (ELK Stack) short url API
  slug: elk-stack-short-url-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The significant_events API from Elastic Stack (ELK Stack) — 4 operation(s) for significant_events.
  name: Elastic Stack (ELK Stack) Significant Events API
  slug: elk-stack-significant-events-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The slm API from Elastic Stack (ELK Stack) — 8 operation(s) for slm.
  name: Elastic Stack (ELK Stack) Slm API
  slug: elk-stack-slm-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: SLO APIs enable you to define, manage and track service-level objectives
  name: Elastic Stack (ELK Stack) Slo API
  slug: elk-stack-slo-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The snapshot API from Elastic Stack (ELK Stack) — 12 operation(s) for snapshot.
  name: Elastic Stack (ELK Stack) Snapshot API
  slug: elk-stack-snapshot-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Spaces API from Elastic Stack (ELK Stack) — 7 operation(s) for spaces.
  name: Elastic Stack (ELK Stack) Spaces API
  slug: elk-stack-spaces-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The sql API from Elastic Stack (ELK Stack) — 6 operation(s) for sql.
  name: Elastic Stack (ELK Stack) Sql API
  slug: elk-stack-sql-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Stack API from Elastic Stack (ELK Stack) — 3 operation(s) for stack.
  name: Elastic Stack (ELK Stack) Stack API
  slug: elk-stack-stack-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The streams API from Elastic Stack (ELK Stack) — 16 operation(s) for streams.
  name: Elastic Stack (ELK Stack) Streams API
  slug: elk-stack-streams-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The synonyms API from Elastic Stack (ELK Stack) — 3 operation(s) for synonyms.
  name: Elastic Stack (ELK Stack) Synonyms API
  slug: elk-stack-synonyms-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Synthetics APIs enable you to check the status of your services and applications.
  name: Elastic Stack (ELK Stack) Synthetics API
  slug: elk-stack-synthetics-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Get information about the system status, resource usage, features, and installed plugins.
  name: Elastic Stack (ELK Stack) System API
  slug: elk-stack-system-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Tags API from Elastic Stack (ELK Stack) — 2 operation(s) for tags.
  name: Elastic Stack (ELK Stack) Tags API
  slug: elk-stack-tags-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Task manager APIs enable you to check the health of the Kibana task manager, which is used by features such as alerting, actions, and reporting to run mission critical work as persistent background ta
  name: Elastic Stack (ELK Stack) task manager API
  slug: elk-stack-task-manager-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The tasks API from Elastic Stack (ELK Stack) — 4 operation(s) for tasks.
  name: Elastic Stack (ELK Stack) Tasks API
  slug: elk-stack-tasks-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Telemetry API from Elastic Stack (ELK Stack) — 1 operation(s) for telemetry.
  name: Elastic Stack (ELK Stack) Telemetry API
  slug: elk-stack-telemetry-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The text_structure API from Elastic Stack (ELK Stack) — 4 operation(s) for text_structure.
  name: Elastic Stack (ELK Stack) Text Structure API
  slug: elk-stack-text-structure-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The transform API from Elastic Stack (ELK Stack) — 13 operation(s) for transform.
  name: Elastic Stack (ELK Stack) Transform API
  slug: elk-stack-transform-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The TrustedEnvironments API from Elastic Stack (ELK Stack) — 1 operation(s) for trustedenvironments.
  name: Elastic Stack (ELK Stack) Trusted Environments API
  slug: elk-stack-trustedenvironments-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: 'The Kibana Upgrade Assistant API helps you prepare for the next major Elasticsearch release. > warn > This is a Kibana REST API (not an Elasticsearch API) and requests must target your Kibana URL: > *'
  name: Elastic Stack (ELK Stack) Upgrade API
  slug: elk-stack-upgrade-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Uptime APIs enable you to view and update uptime monitoring settings.
  name: Elastic Stack (ELK Stack) Uptime API
  slug: elk-stack-uptime-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Enables you to invalidate user sessions for security and session management purposes.
  name: Elastic Stack (ELK Stack) user session API
  slug: elk-stack-user-session-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The UserRoleAssignments API from Elastic Stack (ELK Stack) — 1 operation(s) for userroleassignments.
  name: Elastic Stack (ELK Stack) User Role Assignments API
  slug: elk-stack-userroleassignments-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Users API from Elastic Stack (ELK Stack) — 3 operation(s) for users.
  name: Elastic Stack (ELK Stack) Users API
  slug: elk-stack-users-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: '> This documentation is temporarily hosted at a separate location. > > **[View the full Visualizations API reference →](https://elastic.github.io/dashboards-api-spec/visualizations#tag/Visualizations)'
  name: Elastic Stack (ELK Stack) Visualizations API
  slug: elk-stack-visualizations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The watcher API from Elastic Stack (ELK Stack) — 13 operation(s) for watcher.
  name: Elastic Stack (ELK Stack) Watcher API
  slug: elk-stack-watcher-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Workflows enable you to automate multi-step processes directly in Kibana. Define sequences of steps in YAML to transform data insights into automated actions and outcomes, without needing external aut
  name: Elastic Stack (ELK Stack) Workflows API
  slug: elk-stack-workflows-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The xpack API from Elastic Stack (ELK Stack) — 2 operation(s) for xpack.
  name: Elastic Stack (ELK Stack) Xpack API
  slug: elk-stack-xpack-api
artifact_total: 151
asyncapis:
- description: ''
  name: Elk Stack Webhooks
  slug: elk-stack-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elasticsearch REST Cat API
  slug: open-elk-stack-cat-api
- collection_type: open
  name: Elasticsearch REST Cat Cluster API
  slug: open-elk-stack-cluster-api
- collection_type: open
  name: Elasticsearch REST Cat Document API
  slug: open-elk-stack-document-api
- collection_type: open
  name: Elasticsearch REST Cat Index API
  slug: open-elk-stack-index-api
- collection_type: open
  name: Elasticsearch REST Cat Ingest API
  slug: open-elk-stack-ingest-api
- collection_type: open
  name: Elasticsearch REST Cat Search API
  slug: open-elk-stack-search-api
- collection_type: open
  name: Elasticsearch REST Cat Snapshot API
  slug: open-elk-stack-snapshot-api
- collection_type: open
  name: Elasticsearch REST API
  slug: open-elk-stack
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/elastic/elasticsearch-specification/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/elk-stack-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/elk-stack-elasticsearch-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/elk-stack-kibana-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co/elastic-stack/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.elastic.co/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.elastic.co/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.elastic.co/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.elastic.co/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://discuss.elastic.co/
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elastic
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.elastic.co/cloud/elasticsearch-service/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elastic.co/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elastic.co/legal/privacy-statement
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elastic-co
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elastic.co/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elk-stack-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/elk-stack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/elk-stack-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/elk-stack-cli.yml
- group: design
  title: ''
  type: Components
  url: components/elk-stack-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elk-stack-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/elk-stack-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elk-stack-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/elk-stack-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/elk-stack-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elk-stack-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/elk-stack-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elk-stack-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elk-stack-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/elk-stack-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elk-stack-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elk-stack-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/elk-stack-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elk-stack-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/elk-stack-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elk-stack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elk-stack-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elk-stack-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elk-stack-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elk-stack-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/elk-stack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/elk-stack-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elk-stack-agentic-access.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elk-stack-finops.yml
created: '2024-01-01'
description: 'The Elastic Stack (formerly known as the ELK Stack) is the collection of open-source products from Elastic — Elasticsearch, Logstash, Kibana, and Beats/Elastic Agent — designed for taking data from any source, in any format, and searching, analyzing, and visualizing it in real time. It is widely used for log management, observability, security analytics (SIEM), and increasingly as a vector database and retrieval layer for RAG and agentic AI applications. Elastic publishes machine-readable OpenAPI descriptions for all three of its programmable surfaces: the Elasticsearch REST API, the Kibana APIs, and the Elastic Cloud control-plane API. The stack is deployment-hosted — self-managed, Elastic Cloud Hosted, or Elastic Cloud Serverless — so the Elasticsearch and Kibana base URLs are always specific to the customer''s own cluster or project.'
finops:
- name: Elk Stack Finops
  service_category: API
  slug: elk-stack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elk-stack.png
layout: provider
mcp_servers:
- description: ''
  name: Elastic Stack (ELK Stack) MCP Server
  slug: elastic-stack-elk-stack-mcp-server
modified: '2026-08-27'
name: Elastic Stack (ELK Stack)
nav: Providers
network: true
overview: 'Elastic Stack (ELK Stack) publishes 132 APIs on the [APIs.io](https://apis.io/) network, including Elastic Cloud API, Accounts API, Actions API, and 129 more. Tagged areas include Analytics, Logging, Monitoring, Observability, and Search.


  The Elastic Stack (ELK Stack) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Elastic Stack (ELK Stack)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 42 more developer resources.'
plans:
- name: Elk Stack Plans Pricing
  plan_count: 4
  slug: elk-stack-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Elk Stack Rate Limits
  slug: elk-stack-rate-limits
score:
  band: exemplar
  composite: 67.4
  coverage:
    artifact_dirs: 28
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.4
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 58.5
    developer_ergonomics: 80.4
    discoverability: 83.3
    governance: 4.5
    operational_transparency: 60.5
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 131
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/screenshots/elk-stack-2026-06-20T180610.png
security:
- kind: authentication
  name: Elk Stack Authentication
  slug: elk-stack-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Elk Stack Domain Security
  slug: elk-stack-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Elk Stack Vulnerability Disclosure
  slug: elk-stack-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Elk Stack Trust Center
  slug: elk-stack-trust-center
  summary_line: FedRAMP High, FedRAMP Moderate, PCI DSS (Level 1 Service Provider), CSA STAR, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, SOC 2, SOC 3, TISAX, HIPAA, Cyber Essentials Plus, IRAP Assessed — Protected B, GDPR
slug: elk-stack
tags:
- Analytics
- Logging
- Monitoring
- Observability
- Search
- Security
- Vector Database
- SIEM
- Machine-Learning
website: https://www.elastic.co/elastic-stack/
---
