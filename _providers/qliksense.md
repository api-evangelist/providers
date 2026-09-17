---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: templated
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.6
  scored_at: '2026-09-16'
api_count: 78
apis:
- description: JSON-RPC WebSocket API for interacting with the Qlik Associative Engine, creating and manipulating apps, and building visualizations.
  name: Qlik Engine API
  slug: engine-api
- description: gRPC/protobuf contract for extending the Qlik Associative Engine with external compute. A plugin implements the qlik.sse.Connector service and the engine calls out to it for scalar, aggregation and te
  name: Qlik Server-Side Extension Protocol
  slug: server-side-extension
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks
  baseurl_source: declared
  description: 'The Qlik Cloud tenant event surface: 29 AsyncAPI 3.0.0 documents covering 102 message definitions across apps, reloads, spaces, tenants, users, roles, licenses, quotas, OAuth clients, data-integration'
  name: Qlik Cloud System Events
  slug: system-events
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/ai/mcp
  baseurl_source: declared
  description: Qlik's first-party remote Model Context Protocol server, generally available since 2026-02-10 and included from the Starter plan up. It exposes Qlik Cloud analytics — datasets and data quality, data p
  name: Qlik MCP Server
  slug: mcp-server
- description: WebSocket-based API for interacting with the Qlik Associative Engine, including data modeling, selections, and visualizations.
  name: Qlik Sense Engine API
  slug: qlik-sense-engine-api
- description: REST API for managing Qlik Sense repository objects including apps, streams, users, and security rules.
  name: Qlik Sense Repository API
  slug: qlik-sense-repository-api
- description: REST API for session management and authentication through the Qlik Sense Proxy Service.
  name: Qlik Sense Proxy API
  slug: qlik-sense-proxy-api
- description: REST API for managing data integration tasks, connections, and data pipelines.
  name: Qlik Data Integration API
  slug: qlik-data-integration-api
- description: JavaScript API for embedding Qlik Sense visualizations and mashups into web applications.
  name: Qlik Embedding API
  slug: qlik-embedding-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The alerting actions API from Qlik Sense — 2 operation(s) for alerting actions.
  name: Qlik Sense alerting actions API
  slug: qliksense-alerting-actions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The alerting settings API from Qlik Sense — 1 operation(s) for alerting settings.
  name: Qlik Sense alerting settings API
  slug: qliksense-alerting-settings-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The alerting tasks API from Qlik Sense — 4 operation(s) for alerting tasks.
  name: Qlik Sense alerting tasks API
  slug: qliksense-alerting-tasks-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The alerting tasks executions API from Qlik Sense — 4 operation(s) for alerting tasks executions.
  name: Qlik Sense alerting tasks executions API
  slug: qliksense-alerting-tasks-executions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The aliases API from Qlik Sense — 2 operation(s) for aliases.
  name: Qlik Sense Aliases API
  slug: qliksense-aliases-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Analytics API from Qlik Sense — 1 operation(s) for analytics.
  name: Qlik Sense Analytics API
  slug: qliksense-analytics-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The api-keys API from Qlik Sense — 2 operation(s) for api-keys.
  name: Qlik Sense API Keys API
  slug: qliksense-api-keys-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The api-keys configurations API from Qlik Sense — 1 operation(s) for api-keys configurations.
  name: Qlik Sense api-keys configurations API
  slug: qliksense-api-keys-configurations-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The api settings API from Qlik Sense — 1 operation(s) for api settings.
  name: Qlik Sense api settings API
  slug: qliksense-api-settings-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Apps API from Qlik Sense — 23 operation(s) for apps.
  name: Qlik Sense Apps API
  slug: qliksense-apps-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The assignments API from Qlik Sense — 2 operation(s) for assignments.
  name: Qlik Sense Assignments API
  slug: qliksense-assignments-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The assistants API from Qlik Sense — 4 operation(s) for assistants.
  name: Qlik Sense Assistants API
  slug: qliksense-assistants-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The async actions API from Qlik Sense — 1 operation(s) for async actions.
  name: Qlik Sense async actions API
  slug: qliksense-async-actions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The audits API from Qlik Sense — 7 operation(s) for audits.
  name: Qlik Sense Audits API
  slug: qliksense-audits-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The automation-connections API from Qlik Sense — 10 operation(s) for automation-connections.
  name: Qlik Sense Automation Connections API
  slug: qliksense-automation-connections-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The automation-connectors API from Qlik Sense — 4 operation(s) for automation-connectors.
  name: Qlik Sense Automation Connectors API
  slug: qliksense-automation-connectors-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The automations API from Qlik Sense — 30 operation(s) for automations.
  name: Qlik Sense Automations API
  slug: qliksense-automations-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The automl-deployments API from Qlik Sense — 1 operation(s) for automl-deployments.
  name: Qlik Sense Automl Deployments API
  slug: qliksense-automl-deployments-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The automl-predictions API from Qlik Sense — 6 operation(s) for automl-predictions.
  name: Qlik Sense Automl Predictions API
  slug: qliksense-automl-predictions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The banner API from Qlik Sense — 2 operation(s) for banner.
  name: Qlik Sense Banner API
  slug: qliksense-banner-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The brands API from Qlik Sense — 6 operation(s) for brands.
  name: Qlik Sense Brands API
  slug: qliksense-brands-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The categories API from Qlik Sense — 2 operation(s) for categories.
  name: Qlik Sense Categories API
  slug: qliksense-categories-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The change-stores API from Qlik Sense — 2 operation(s) for change-stores.
  name: Qlik Sense Change Stores API
  slug: qliksense-change-stores-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The changes API from Qlik Sense — 2 operation(s) for changes.
  name: Qlik Sense Changes API
  slug: qliksense-changes-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The chat API from Qlik Sense — 2 operation(s) for chat.
  name: Qlik Sense Chat API
  slug: qliksense-chat-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The collections API from Qlik Sense — 5 operation(s) for collections.
  name: Qlik Sense Collections API
  slug: qliksense-collections-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The computation API from Qlik Sense — 5 operation(s) for computation.
  name: Qlik Sense Computation API
  slug: qliksense-computation-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The condition preview API from Qlik Sense — 2 operation(s) for condition preview.
  name: Qlik Sense condition preview API
  slug: qliksense-condition-preview-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The conditions API from Qlik Sense — 2 operation(s) for conditions.
  name: Qlik Sense Conditions API
  slug: qliksense-conditions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Consumption API from Qlik Sense — 1 operation(s) for consumption.
  name: Qlik Sense Consumption API
  slug: qliksense-consumption-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The csp-origins API from Qlik Sense — 3 operation(s) for csp-origins.
  name: Qlik Sense Csp Origins API
  slug: qliksense-csp-origins-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The csrf API from Qlik Sense — 1 operation(s) for csrf.
  name: Qlik Sense Csrf API
  slug: qliksense-csrf-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-asset API from Qlik Sense — 2 operation(s) for data-asset.
  name: Qlik Sense Data Asset API
  slug: qliksense-data-asset-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-connections API from Qlik Sense — 5 operation(s) for data-connections.
  name: Qlik Sense Data Connections API
  slug: qliksense-data-connections-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-credentials API from Qlik Sense — 2 operation(s) for data-credentials.
  name: Qlik Sense Data Credentials API
  slug: qliksense-data-credentials-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-product-activation API from Qlik Sense — 2 operation(s) for data-product-activation.
  name: Qlik Sense Data Product Activation API
  slug: qliksense-data-product-activation-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-product API from Qlik Sense — 4 operation(s) for data-product.
  name: Qlik Sense Data Product API
  slug: qliksense-data-product-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-product-changelog API from Qlik Sense — 1 operation(s) for data-product-changelog.
  name: Qlik Sense Data Product Changelog API
  slug: qliksense-data-product-changelog-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-product-data-quality API from Qlik Sense — 1 operation(s) for data-product-data-quality.
  name: Qlik Sense Data Product Data Quality API
  slug: qliksense-data-product-data-quality-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-product-generate-provider-url API from Qlik Sense — 1 operation(s) for data-product-generate-provider-url.
  name: Qlik Sense Data Product Generate Provider URL API
  slug: qliksense-data-product-generate-provider-url-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data project actions API from Qlik Sense — 2 operation(s) for data project actions.
  name: Qlik Sense data project actions API
  slug: qliksense-data-project-actions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data project API from Qlik Sense — 2 operation(s) for data project.
  name: Qlik Sense data project API
  slug: qliksense-data-project-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data project deployment API from Qlik Sense — 5 operation(s) for data project deployment.
  name: Qlik Sense data project deployment API
  slug: qliksense-data-project-deployment-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-quality API from Qlik Sense — 4 operation(s) for data-quality.
  name: Qlik Sense Data Quality API
  slug: qliksense-data-quality-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data-sources API from Qlik Sense — 4 operation(s) for data-sources.
  name: Qlik Sense Data Sources API
  slug: qliksense-data-sources-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data task actions API from Qlik Sense — 4 operation(s) for data task actions.
  name: Qlik Sense data task actions API
  slug: qliksense-data-task-actions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data task API from Qlik Sense — 2 operation(s) for data task.
  name: Qlik Sense data task API
  slug: qliksense-data-task-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The data task runtime API from Qlik Sense — 4 operation(s) for data task runtime.
  name: Qlik Sense data task runtime API
  slug: qliksense-data-task-runtime-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The datafiles API from Qlik Sense — 9 operation(s) for datafiles.
  name: Qlik Sense Datafiles API
  slug: qliksense-datafiles-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The deliveries API from Qlik Sense — 3 operation(s) for deliveries.
  name: Qlik Sense Deliveries API
  slug: qliksense-deliveries-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The deployments API from Qlik Sense — 6 operation(s) for deployments.
  name: Qlik Sense Deployments API
  slug: qliksense-deployments-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The direct-access-agent-benchmarking API from Qlik Sense — 3 operation(s) for direct-access-agent-benchmarking.
  name: Qlik Sense Direct Access Agent Benchmarking API
  slug: qliksense-direct-access-agent-benchmarking-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The direct-access-agent-configuration API from Qlik Sense — 7 operation(s) for direct-access-agent-configuration.
  name: Qlik Sense Direct Access Agent Configuration API
  slug: qliksense-direct-access-agent-configuration-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The editable-columns API from Qlik Sense — 1 operation(s) for editable-columns.
  name: Qlik Sense Editable Columns API
  slug: qliksense-editable-columns-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The email-config-actions API from Qlik Sense — 3 operation(s) for email-config-actions.
  name: Qlik Sense Email Config Actions API
  slug: qliksense-email-config-actions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The email-config API from Qlik Sense — 1 operation(s) for email-config.
  name: Qlik Sense Email Config API
  slug: qliksense-email-config-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The evaluation API from Qlik Sense — 10 operation(s) for evaluation.
  name: Qlik Sense Evaluation API
  slug: qliksense-evaluation-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The evaluations API from Qlik Sense — 2 operation(s) for evaluations.
  name: Qlik Sense Evaluations API
  slug: qliksense-evaluations-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The experiments API from Qlik Sense — 7 operation(s) for experiments.
  name: Qlik Sense Experiments API
  slug: qliksense-experiments-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The extensions API from Qlik Sense — 4 operation(s) for extensions.
  name: Qlik Sense Extensions API
  slug: qliksense-extensions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The filters API from Qlik Sense — 3 operation(s) for filters.
  name: Qlik Sense Filters API
  slug: qliksense-filters-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The glossaries API from Qlik Sense — 4 operation(s) for glossaries.
  name: Qlik Sense Glossaries API
  slug: qliksense-glossaries-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The groups API from Qlik Sense — 3 operation(s) for groups.
  name: Qlik Sense Groups API
  slug: qliksense-groups-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The groups-settings API from Qlik Sense — 1 operation(s) for groups-settings.
  name: Qlik Sense Groups Settings API
  slug: qliksense-groups-settings-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The iam-resources API from Qlik Sense — 3 operation(s) for iam-resources.
  name: Qlik Sense Iam Resources API
  slug: qliksense-iam-resources-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The idp API from Qlik Sense — 5 operation(s) for idp.
  name: Qlik Sense Idp API
  slug: qliksense-idp-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The impact API from Qlik Sense — 4 operation(s) for impact.
  name: Qlik Sense Impact API
  slug: qliksense-impact-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The insight-analyses API from Qlik Sense — 3 operation(s) for insight-analyses.
  name: Qlik Sense Insight Analyses API
  slug: qliksense-insight-analyses-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The invite API from Qlik Sense — 1 operation(s) for invite.
  name: Qlik Sense Invite API
  slug: qliksense-invite-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The items API from Qlik Sense — 4 operation(s) for items.
  name: Qlik Sense Items API
  slug: qliksense-items-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The items-settings API from Qlik Sense — 1 operation(s) for items-settings.
  name: Qlik Sense Items Settings API
  slug: qliksense-items-settings-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The jobs API from Qlik Sense — 1 operation(s) for jobs.
  name: Qlik Sense Jobs API
  slug: qliksense-jobs-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The licenses API from Qlik Sense — 8 operation(s) for licenses.
  name: Qlik Sense Licenses API
  slug: qliksense-licenses-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The lineage-graphs API from Qlik Sense — 4 operation(s) for lineage-graphs.
  name: Qlik Sense Lineage Graphs API
  slug: qliksense-lineage-graphs-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Link API from Qlik Sense — 4 operation(s) for link.
  name: Qlik Sense Link API
  slug: qliksense-link-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The links API from Qlik Sense — 1 operation(s) for links.
  name: Qlik Sense Links API
  slug: qliksense-links-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The login API from Qlik Sense — 1 operation(s) for login.
  name: Qlik Sense Login API
  slug: qliksense-login-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The notifications API from Qlik Sense — 1 operation(s) for notifications.
  name: Qlik Sense Notifications API
  slug: qliksense-notifications-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The oauth-clients API from Qlik Sense — 6 operation(s) for oauth-clients.
  name: Qlik Sense OAUTH Clients API
  slug: qliksense-oauth-clients-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The oauth-tokens API from Qlik Sense — 2 operation(s) for oauth-tokens.
  name: Qlik Sense OAUTH Tokens API
  slug: qliksense-oauth-tokens-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The outputs API from Qlik Sense — 1 operation(s) for outputs.
  name: Qlik Sense Outputs API
  slug: qliksense-outputs-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The owl API from Qlik Sense — 1 operation(s) for owl.
  name: Qlik Sense Owl API
  slug: qliksense-owl-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The pinned links API from Qlik Sense — 4 operation(s) for pinned links.
  name: Qlik Sense pinned links API
  slug: qliksense-pinned-links-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The predictions API from Qlik Sense — 6 operation(s) for predictions.
  name: Qlik Sense Predictions API
  slug: qliksense-predictions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The profile API from Qlik Sense — 1 operation(s) for profile.
  name: Qlik Sense Profile API
  slug: qliksense-profile-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The profile-insights API from Qlik Sense — 2 operation(s) for profile-insights.
  name: Qlik Sense Profile Insights API
  slug: qliksense-profile-insights-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The questions API from Qlik Sense — 2 operation(s) for questions.
  name: Qlik Sense Questions API
  slug: qliksense-questions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The quotas API from Qlik Sense — 2 operation(s) for quotas.
  name: Qlik Sense Quotas API
  slug: qliksense-quotas-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The reload-tasks API from Qlik Sense — 2 operation(s) for reload-tasks.
  name: Qlik Sense Reload Tasks API
  slug: qliksense-reload-tasks-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The reloads API from Qlik Sense — 3 operation(s) for reloads.
  name: Qlik Sense Reloads API
  slug: qliksense-reloads-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The report-templates API from Qlik Sense — 3 operation(s) for report-templates.
  name: Qlik Sense Report Templates API
  slug: qliksense-report-templates-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The reports API from Qlik Sense — 1 operation(s) for reports.
  name: Qlik Sense Reports API
  slug: qliksense-reports-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Request API from Qlik Sense — 6 operation(s) for request.
  name: Qlik Sense Request API
  slug: qliksense-request-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The roles API from Qlik Sense — 2 operation(s) for roles.
  name: Qlik Sense Roles API
  slug: qliksense-roles-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The search API from Qlik Sense — 2 operation(s) for search.
  name: Qlik Sense Search API
  slug: qliksense-search-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The setting API from Qlik Sense — 1 operation(s) for setting.
  name: Qlik Sense Setting API
  slug: qliksense-setting-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Settings API from Qlik Sense — 2 operation(s) for settings.
  name: Qlik Sense Settings API
  slug: qliksense-settings-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The shares API from Qlik Sense — 2 operation(s) for shares.
  name: Qlik Sense Shares API
  slug: qliksense-shares-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The sharing settings API from Qlik Sense — 1 operation(s) for sharing settings.
  name: Qlik Sense sharing settings API
  slug: qliksense-sharing-settings-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The sharing tasks actions API from Qlik Sense — 2 operation(s) for sharing tasks actions.
  name: Qlik Sense sharing tasks actions API
  slug: qliksense-sharing-tasks-actions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The sharing tasks API from Qlik Sense — 2 operation(s) for sharing tasks.
  name: Qlik Sense sharing tasks API
  slug: qliksense-sharing-tasks-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The sharing tasks executions API from Qlik Sense — 3 operation(s) for sharing tasks executions.
  name: Qlik Sense sharing tasks executions API
  slug: qliksense-sharing-tasks-executions-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The spaces API from Qlik Sense — 3 operation(s) for spaces.
  name: Qlik Sense Spaces API
  slug: qliksense-spaces-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The starters API from Qlik Sense — 3 operation(s) for starters.
  name: Qlik Sense Starters API
  slug: qliksense-starters-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The status API from Qlik Sense — 1 operation(s) for status.
  name: Qlik Sense Status API
  slug: qliksense-status-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The task API from Qlik Sense — 14 operation(s) for task.
  name: Qlik Sense Task API
  slug: qliksense-task-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The task-graph API from Qlik Sense — 5 operation(s) for task-graph.
  name: Qlik Sense Task Graph API
  slug: qliksense-task-graph-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The task run history API from Qlik Sense — 3 operation(s) for task run history.
  name: Qlik Sense task run history API
  slug: qliksense-task-run-history-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Temporary contents API from Qlik Sense — 5 operation(s) for temporary contents.
  name: Qlik Sense Temporary contents API
  slug: qliksense-temporary-contents-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The tenant key migration information API from Qlik Sense — 1 operation(s) for tenant key migration information.
  name: Qlik Sense tenant key migration information API
  slug: qliksense-tenant-key-migration-information-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The tenant key provider management API from Qlik Sense — 3 operation(s) for tenant key provider management.
  name: Qlik Sense tenant key provider management API
  slug: qliksense-tenant-key-provider-management-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The tenant key provider operations API from Qlik Sense — 3 operation(s) for tenant key provider operations.
  name: Qlik Sense tenant key provider operations API
  slug: qliksense-tenant-key-provider-operations-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The tenant-settings API from Qlik Sense — 4 operation(s) for tenant-settings.
  name: Qlik Sense Tenant Settings API
  slug: qliksense-tenant-settings-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The tenants API from Qlik Sense — 5 operation(s) for tenants.
  name: Qlik Sense Tenants API
  slug: qliksense-tenants-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The terms API from Qlik Sense — 4 operation(s) for terms.
  name: Qlik Sense Terms API
  slug: qliksense-terms-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The themes API from Qlik Sense — 4 operation(s) for themes.
  name: Qlik Sense Themes API
  slug: qliksense-themes-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The threads API from Qlik Sense — 7 operation(s) for threads.
  name: Qlik Sense Threads API
  slug: qliksense-threads-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The tokens API from Qlik Sense — 1 operation(s) for tokens.
  name: Qlik Sense Tokens API
  slug: qliksense-tokens-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The trust-score-result API from Qlik Sense — 1 operation(s) for trust-score-result.
  name: Qlik Sense Trust Score Result API
  slug: qliksense-trust-score-result-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The users API from Qlik Sense — 5 operation(s) for users.
  name: Qlik Sense Users API
  slug: qliksense-users-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The web-integrations API from Qlik Sense — 2 operation(s) for web-integrations.
  name: Qlik Sense Web Integrations API
  slug: qliksense-web-integrations-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The web-notifications API from Qlik Sense — 3 operation(s) for web-notifications.
  name: Qlik Sense Web Notifications API
  slug: qliksense-web-notifications-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The webhooks API from Qlik Sense — 3 operation(s) for webhooks.
  name: Qlik Sense Webhooks API
  slug: qliksense-webhooks-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Dataset API from Qlik Sense — 2 operation(s) for dataset.
  name: Qlik Sense Dataset API
  slug: qliksense-dataset-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Datastore API from Qlik Sense — 4 operation(s) for datastore.
  name: Qlik Sense Datastore API
  slug: qliksense-datastore-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Knowledge Bases API from Qlik Sense — 11 operation(s) for knowledge bases.
  name: Qlik Sense Knowledge Bases API
  slug: qliksense-knowledge-bases-api
artifact_total: 202
asyncapis:
- description: ''
  name: Qliksense Asyncapi Index
  slug: qliksense-asyncapi-index
- description: ''
  name: Qliksense Webhooks
  slug: qliksense-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-analytics-apps-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-apps-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-analytics-change-stores-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-change-stores-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-analytics-discovery-agent-adaptive-cards-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-discovery-agent-adaptive-cards-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-analytics-odag-apps-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-odag-apps-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-analytics-odag-links-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-odag-links-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-analytics-odag-requests-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-odag-requests-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-analytics-odag-settings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-odag-settings-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-api-keys-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-api-keys-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-apps-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-apps-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-assistants-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-assistants-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-audits-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-audits-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-automation-connections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automation-connections-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-automation-connectors-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automation-connectors-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-automations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-automl-deployments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automl-deployments-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-automl-predictions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automl-predictions-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-banners-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-banners-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-brands-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-brands-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-collections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-collections-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-conditions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-conditions-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-consumption-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-consumption-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-core-auth-settings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-core-auth-settings-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-core-ip-policies-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-core-ip-policies-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-csp-origins-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-csp-origins-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-csrf-token-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-csrf-token-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-alerts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-alerts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-assets-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-assets-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-connections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-connections-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-credentials-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-credentials-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-files-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-files-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-governance-data-products-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-governance-data-products-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-governance-data-qualities-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-governance-data-qualities-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-governance-trust-scores-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-governance-trust-scores-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-qualities-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-qualities-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-sets-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-sets-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-sources-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-sources-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-data-stores-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-stores-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-di-projects-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-di-projects-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-direct-access-agents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-direct-access-agents-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-encryption-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-encryption-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-extensions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-extensions-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-glossaries-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-glossaries-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-groups-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-groups-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-identity-providers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-identity-providers-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-items-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-items-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-knowledgebases-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-knowledgebases-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-licenses-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-licenses-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-lineage-graphs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-lineage-graphs-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-login-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-login-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-ml-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-ml-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-notes-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-notes-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-notifications-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-oauth-clients-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-oauth-clients-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-oauth-tokens-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-oauth-tokens-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-questions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-questions-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-quotas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-quotas-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-reload-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-reload-tasks-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-reloads-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-reloads-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-report-templates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-report-templates-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-reports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-reports-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-roles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-roles-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-scheduling-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-scheduling-tasks-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-sharing-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-sharing-tasks-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-spaces-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-spaces-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-tasks-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-temp-contents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-temp-contents-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-tenant-settings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-tenant-settings-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-tenants-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-tenants-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-themes-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-themes-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-transports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-transports-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-ui-config-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-ui-config-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-users-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-users-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-web-integrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-web-integrations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-web-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-web-notifications-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-webhooks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-webhooks-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-workflows-automation-connections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-workflows-automation-connections-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-workflows-automation-connectors-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-workflows-automation-connectors-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/overlays/qliksense-workflows-automations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-workflows-automations-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/qlik-oss/server-side-extension/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.qlik.com/us/products/qlik-sense
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qlik.dev/
- group: start
  title: ''
  type: Portal
  url: https://qlik.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://qlik.dev/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://qlik.dev/apis/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://qlik.dev/manage/get-started-first-api-call/
- group: auth
  title: ''
  type: Authentication
  url: https://qlik.dev/authenticate
- group: operate
  title: ''
  type: Support
  url: https://support.qlik.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.qlik.com/
- group: company
  title: ''
  type: Blog
  url: https://www.qlik.com/us/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qlik.com/us/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.qlik.com/us/trial/qlik-cloud-analytics
- group: start
  title: ''
  type: Login
  url: https://login.qlik.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qlikcloud.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://qlik.dev/changelog/
- group: other
  title: ''
  type: RSS
  url: https://qlik.dev/rss.xml
- group: build
  title: ''
  type: CLI
  url: https://qlik.dev/toolkits/qlik-cli/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/packages/qliksense-packages.yml
  title: ''
  type: SDKs
  url: packages/qliksense-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/packages/qliksense-packages.yml
  title: ''
  type: Packages
  url: packages/qliksense-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/mcp/qliksense-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/qliksense-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/mcp/qliksense-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/qliksense-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/llms/qliksense-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qliksense-llms.txt
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/asyncapi/qliksense-asyncapi-index.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/qliksense-asyncapi-index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/asyncapi/qliksense-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/qliksense-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/grpc/qliksense-server-side-extension.proto
  title: ''
  type: Protobuf
  url: grpc/qliksense-server-side-extension.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/json-rpc/qliksense-qix-openrpc.json
  title: ''
  type: OpenRPC
  url: json-rpc/qliksense-qix-openrpc.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/json-schema/qliksense-qtcp-project.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/qliksense-qtcp-project.schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/conformance/qliksense-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qliksense-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/security/qliksense-trust-center.yml
  title: ''
  type: Compliance
  url: security/qliksense-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/security/qliksense-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/qliksense-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/security/qliksense-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/qliksense-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/security/qliksense-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/qliksense-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/security/qliksense-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qliksense-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/errors/qliksense-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qliksense-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/lifecycle/qliksense-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qliksense-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/lifecycle/qliksense-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/qliksense-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/scopes/qliksense-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/qliksense-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/authentication/qliksense-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qliksense-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/conventions/qliksense-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qliksense-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/changelog/qliksense-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/qliksense-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/cli/qliksense-cli.yml
  title: ''
  type: CLI
  url: cli/qliksense-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/components/qliksense-components.yml
  title: ''
  type: Components
  url: components/qliksense-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/data-model/qliksense-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qliksense-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/plans/qliksense-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qliksense-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/rate-limits/qliksense-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qliksense-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/finops/qliksense-finops.yml
  title: ''
  type: FinOps
  url: finops/qliksense-finops.yml
created: '2024-01-15'
description: 'Qlik Sense and Qlik Cloud from Qlik Parent, Inc. — a business intelligence, data integration and AI analytics platform. Qlik publishes one of the broadest machine-readable API surfaces in the analytics market: 78 OpenAPI 3.0.0 documents covering 681 REST operations, 29 AsyncAPI 3.0.0 event documents carrying CloudEvents 1.0 payloads, an OpenRPC 1.0.0 document for the QIX Associative Engine WebSocket API, 39 JSON Schemas for Qlik Talend Cloud declarative pipelines, and a proto3 gRPC contract for the engine''s Server-Side Extension protocol. It also ships a generally-available remote MCP server at <tenant>/api/ai/mcp and maintains a public Agent Skills hub. Every API is tenant-scoped to https://{tenant}.{region}.qlikcloud.com and authenticated with an API key, an OAuth 2.0 token or a signed JWT.'
features:
- description: Qlik's unique Associative Engine enables dynamic data exploration without predefined queries or drill paths.
  name: Associative Engine
- description: Comprehensive REST API coverage for all Qlik Cloud resources including apps, data, users, and automation.
  name: 50+ REST APIs
- description: AutoML, natural language queries, and AI assistants for data-driven insights.
  name: AI-Powered Analytics
- description: Build automation workflows connecting Qlik with external applications without coding.
  name: No-Code Automation
- description: Event-driven architecture with webhooks for real-time notifications on platform events.
  name: Real-Time Webhooks
- description: Deploy Qlik Cloud across AWS, Azure, and GCP regions with global availability.
  name: Multi-Cloud Deployment
finops:
- name: Qliksense Finops
  service_category: API
  slug: qliksense-finops
image: /assets/icons/qliksense.png
integrations:
- description: Direct connectivity for analytics on Snowflake cloud data warehouse.
  name: Snowflake
- description: Integration with Databricks lakehouse for large-scale analytics workloads.
  name: Databricks
- description: Enterprise data connectivity for SAP ERP, BW, and HANA data sources.
  name: SAP
- description: CRM data integration for sales analytics and pipeline management.
  name: Salesforce
- description: Collaboration integration for sharing analytics insights and alerts in Slack.
  name: Slack
- description: Embed analytics and receive notifications within Microsoft Teams.
  name: Microsoft Teams
json_schemas:
- name: New Task Defaults Configuration
  property_count: 14
  slug: qliksense-qtcp-newtaskdefaults.schema
- name: Common Task Settings Definitions
  property_count: 0
  slug: qliksense-qtcp-newtaskdefaults.settings.common.schema
- name: Defaults for new Datamart Task
  property_count: 8
  slug: qliksense-qtcp-newtaskdefaults.settings.datamart.schema
- name: Defaults for new File Based Knowledge Mart Task
  property_count: 7
  slug: qliksense-qtcp-newtaskdefaults.settings.filebasedknowledgemart.schema
- name: Defaults for new Knowledge Mart Task
  property_count: 9
  slug: qliksense-qtcp-newtaskdefaults.settings.knowledgemart.schema
- name: Defaults for new Lakehouse Storage Task
  property_count: 5
  slug: qliksense-qtcp-newtaskdefaults.settings.lakehousestorage.schema
- name: Defaults for new Lake Landing Task
  property_count: 3
  slug: qliksense-qtcp-newtaskdefaults.settings.lakelanding.schema
- name: Defaults for new Landing Task
  property_count: 5
  slug: qliksense-qtcp-newtaskdefaults.settings.landing.schema
- name: Defaults for new QVD Storage Task
  property_count: 2
  slug: qliksense-qtcp-newtaskdefaults.settings.qvdstorage.schema
- name: Defaults for new Registered Data Task
  property_count: 4
  slug: qliksense-qtcp-newtaskdefaults.settings.registereddata.schema
- name: Defaults for new Replicate Landing Task
  property_count: 3
  slug: qliksense-qtcp-newtaskdefaults.settings.replicatelanding.schema
- name: Defaults for new Storage Task
  property_count: 8
  slug: qliksense-qtcp-newtaskdefaults.settings.storage.schema
- name: Defaults for new Streaming Lake Landing Task
  property_count: 4
  slug: qliksense-qtcp-newtaskdefaults.settings.streaminglakelanding.schema
- name: Defaults for new Streaming Transform Task
  property_count: 5
  slug: qliksense-qtcp-newtaskdefaults.settings.streamingtransform.schema
- name: Defaults for new Transform Task
  property_count: 9
  slug: qliksense-qtcp-newtaskdefaults.settings.transform.schema
- name: Project Configuration
  property_count: 2
  slug: qliksense-qtcp-project.schema
- name: Task Dataset Configuration
  property_count: 4
  slug: qliksense-qtcp-task.dataset.schema
- name: Task Model Configuration
  property_count: 2
  slug: qliksense-qtcp-task.model.schema
- name: Task Schedule Configuration
  property_count: 2
  slug: qliksense-qtcp-task.schedule.schema
- name: Task Configuration
  property_count: 0
  slug: qliksense-qtcp-task.schema
- name: Common Task Settings Definitions
  property_count: 0
  slug: qliksense-qtcp-task.settings.common.schema
- name: Datamart Task Settings
  property_count: 7
  slug: qliksense-qtcp-task.settings.datamart.schema
- name: File Based Knowledge Mart Task Settings
  property_count: 14
  slug: qliksense-qtcp-task.settings.filebasedknowledgemart.schema
- name: Knowledge Mart Task Settings
  property_count: 15
  slug: qliksense-qtcp-task.settings.knowledgemart.schema
- name: Lakehouse Mirror Task Settings
  property_count: 6
  slug: qliksense-qtcp-task.settings.lakehousemirror.schema
- name: Lakehouse Storage Task Settings
  property_count: 6
  slug: qliksense-qtcp-task.settings.lakehousestorage.schema
- name: Lake Landing Task Configuration (Replication)
  property_count: 21
  slug: qliksense-qtcp-task.settings.lakelanding.schema
- name: Landing Task Settings
  property_count: 19
  slug: qliksense-qtcp-task.settings.landing.schema
- name: QVD Storage Task Settings
  property_count: 3
  slug: qliksense-qtcp-task.settings.qvdstorage.schema
- name: Registered Data Task Settings
  property_count: 9
  slug: qliksense-qtcp-task.settings.registereddata.schema
- name: Replicate Landing Task Settings
  property_count: 2
  slug: qliksense-qtcp-task.settings.replicatelanding.schema
- name: Replication Task Configuration (Replication)
  property_count: 17
  slug: qliksense-qtcp-task.settings.replication.schema
- name: Storage Task Settings
  property_count: 8
  slug: qliksense-qtcp-task.settings.storage.schema
- name: Streaming Lake Landing Task Settings
  property_count: 3
  slug: qliksense-qtcp-task.settings.streaminglakelanding.schema
- name: Streaming Transform Task Settings
  property_count: 5
  slug: qliksense-qtcp-task.settings.streamingtransform.schema
- name: Transform Task Settings
  property_count: 7
  slug: qliksense-qtcp-task.settings.transform.schema
- name: Task SourceSelection Configuration
  property_count: 6
  slug: qliksense-qtcp-task.sourceselection.schema
- name: Task transformation data flow Configuration
  property_count: 6
  slug: qliksense-qtcp-task.transformationdataflow.schema
- name: Task transformation Configuration
  property_count: 2
  slug: qliksense-qtcp-task.transformationrules.schema
layout: provider
mcp_servers:
- description: Qlik ships a first-party REMOTE MCP server as part of Qlik Cloud. It reached general availability on 2026-02-10 and is listed as an included capability from the Starter plan upward on https://www.qlik
  name: Qlik MCP Server
  slug: qlik-mcp-server
modified: '2026-09-15'
name: Qlik Sense
nav: Providers
network: true
overview: 'Qlik Sense publishes 128 APIs on the [APIs.io](https://apis.io/) network, including Qlik Cloud System Events, Qlik MCP Server, alerting actions API, and 125 more. Tagged areas include Agents, Analytics, Artificial Intelligence, Business Intelligence, and Cloud.


  The Qlik Sense catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Qlik Sense''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, support, engineering blog, and 122 more developer resources.'
plans:
- name: Qliksense Plans Pricing
  plan_count: 5
  slug: qliksense-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Qliksense Rate Limits
  slug: qliksense-rate-limits
scopes:
- name: Qliksense Scopes
  scope_count: 0
  slug: qliksense-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 69.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 78.6
    discoverability: 59.3
    operational_transparency: 84.2
  previous_composite: 70.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 126
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/screenshots/qliksense-2026-06-20T192343.png
security:
- kind: authentication
  name: Qliksense Authentication
  slug: qliksense-authentication
  summary_line: 8 schemes
- kind: domain-security
  name: Qliksense Domain Security
  slug: qliksense-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Qliksense Vulnerability Disclosure
  slug: qliksense-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Qliksense Trust Center
  slug: qliksense-trust-center
  summary_line: qlik, qlik_cloud_government, talend_cloud
slug: qliksense
tags:
- Agents
- Analytics
- Artificial Intelligence
- Business Intelligence
- Cloud
- Data Integration
- Data Visualization
- Embedded Analytics
- Enterprise
- Machine-Learning
use_cases:
- description: Embed interactive Qlik visualizations and dashboards in custom web applications.
  name: Embedded Analytics
- description: Automate data integration and transformation workflows using APIs and automation connectors.
  name: Data Pipeline Automation
- description: Enable business users to create and share analytics apps through the platform APIs.
  name: Self-Service BI
- description: Generate predictive analytics and natural language insights using ML and NLP APIs.
  name: AI-Powered Insights
- description: Manage multiple Qlik Cloud tenants programmatically for SaaS and enterprise deployments.
  name: Multi-Tenant Management
website: https://www.qlik.com/us/products/qlik-sense
---
