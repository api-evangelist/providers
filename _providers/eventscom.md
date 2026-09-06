---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 598
  human_in_the_loop: 291
  name: Eventscom Agentic Access
  operation_count: 979
  slug: eventscom-agentic-access
  summary_line: 979 operations · 598 acting · 291 human-in-the-loop
api_count: 6
apis:
- description: Hosted Model Context Protocol server for the DataGol workbook surface, reachable at the /mcp, /sse and /messages transport paths. Connections are gated on workspace_id, workbook_id and token query par
  name: DataGol MCP Server
  slug: datagol-mcp-server
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The agent-config-controller API from Events.com — 3 operation(s) for agent-config-controller.
  name: Events.com Agent Config Controller API
  slug: eventscom-agent-config-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The agent-config-migration-controller API from Events.com — 1 operation(s) for agent-config-migration-controller.
  name: Events.com Agent Config Migration Controller API
  slug: eventscom-agent-config-migration-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The agent-email-controller API from Events.com — 1 operation(s) for agent-email-controller.
  name: Events.com Agent Email Controller API
  slug: eventscom-agent-email-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The agent-job-update-controller API from Events.com — 1 operation(s) for agent-job-update-controller.
  name: Events.com Agent Job Update Controller API
  slug: eventscom-agent-job-update-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: Manage company-level MCP servers for custom agents
  name: Events.com Agent MCP API
  slug: eventscom-agent-mcp-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The agent-mcp-config-controller API from Events.com — 2 operation(s) for agent-mcp-config-controller.
  name: Events.com Agent MCP Config Controller API
  slug: eventscom-agent-mcp-config-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Agent Memory API from Events.com — 4 operation(s) for agent memory.
  name: Events.com Agent Memory API
  slug: eventscom-agent-memory-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The agent-skill-controller API from Events.com — 6 operation(s) for agent-skill-controller.
  name: Events.com Agent Skill Controller API
  slug: eventscom-agent-skill-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The agent-template-controller API from Events.com — 3 operation(s) for agent-template-controller.
  name: Events.com Agent Template Controller API
  slug: eventscom-agent-template-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The ai-feedback-controller API from Events.com — 3 operation(s) for ai-feedback-controller.
  name: Events.com AI Feedback Controller API
  slug: eventscom-ai-feedback-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The ai-third-party-page-controller API from Events.com — 1 operation(s) for ai-third-party-page-controller.
  name: Events.com AI Third Party Page Controller API
  slug: eventscom-ai-third-party-page-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The alert-controller API from Events.com — 5 operation(s) for alert-controller.
  name: Events.com Alert Controller API
  slug: eventscom-alert-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: APIs for managing alert execution history
  name: Events.com Alert History API
  slug: eventscom-alert-history-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The alert-notification-history-controller API from Events.com — 16 operation(s) for alert-notification-history-controller.
  name: Events.com Alert Notification History Controller API
  slug: eventscom-alert-notification-history-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The api-post-workflow-test-controller API from Events.com — 4 operation(s) for api-post-workflow-test-controller.
  name: Events.com API Post Workflow Test Controller API
  slug: eventscom-api-post-workflow-test-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: Deploy and manage AppX apps in EKS
  name: Events.com AppX Deployment API
  slug: eventscom-appx-deployment-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The bi-page-controller API from Events.com — 9 operation(s) for bi-page-controller.
  name: Events.com Bi Page Controller API
  slug: eventscom-bi-page-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The bi_rag API from Events.com — 6 operation(s) for bi_rag.
  name: Events.com Bi Rag API
  slug: eventscom-bi-rag-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The biv-1-controller API from Events.com — 2 operation(s) for biv-1-controller.
  name: Events.com Biv 1 Controller API
  slug: eventscom-biv-1-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The biv-2-controller API from Events.com — 7 operation(s) for biv-2-controller.
  name: Events.com Biv 2 Controller API
  slug: eventscom-biv-2-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The cache-controller API from Events.com — 2 operation(s) for cache-controller.
  name: Events.com Cache Controller API
  slug: eventscom-cache-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The catalog-search-controller API from Events.com — 1 operation(s) for catalog-search-controller.
  name: Events.com Catalog Search Controller API
  slug: eventscom-catalog-search-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The chat-conversation-controller API from Events.com — 2 operation(s) for chat-conversation-controller.
  name: Events.com Chat Conversation Controller API
  slug: eventscom-chat-conversation-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The comment-controller API from Events.com — 4 operation(s) for comment-controller.
  name: Events.com Comment Controller API
  slug: eventscom-comment-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The company-ontology-controller API from Events.com — 3 operation(s) for company-ontology-controller.
  name: Events.com Company Ontology Controller API
  slug: eventscom-company-ontology-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The company-unstructured-data-controller API from Events.com — 1 operation(s) for company-unstructured-data-controller.
  name: Events.com Company Unstructured Data Controller API
  slug: eventscom-company-unstructured-data-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The config-controller API from Events.com — 3 operation(s) for config-controller.
  name: Events.com Config Controller API
  slug: eventscom-config-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The connector-controller API from Events.com — 17 operation(s) for connector-controller.
  name: Events.com Connector Controller API
  slug: eventscom-connector-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The conversation-controller API from Events.com — 3 operation(s) for conversation-controller.
  name: Events.com Conversation Controller API
  slug: eventscom-conversation-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Conversation File Upload API from Events.com — 6 operation(s) for conversation file upload.
  name: Events.com Conversation File Upload API
  slug: eventscom-conversation-file-upload-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Conversation Message V2 API from Events.com — 4 operation(s) for conversation message v2.
  name: Events.com Conversation Message V2 API
  slug: eventscom-conversation-message-v2-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Conversation V2 API from Events.com — 2 operation(s) for conversation v2.
  name: Events.com Conversation V2 API
  slug: eventscom-conversation-v2-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: Custom agent CRUD, runs, and schedule management
  name: Events.com Custom Agents API
  slug: eventscom-custom-agents-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Data Download API from Events.com — 1 operation(s) for data download.
  name: Events.com Data Download API
  slug: eventscom-data-download-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Data Extraction API from Events.com — 6 operation(s) for data extraction.
  name: Events.com Data Extraction API
  slug: eventscom-data-extraction-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The data-pipeline-controller API from Events.com — 13 operation(s) for data-pipeline-controller.
  name: Events.com Data Pipeline Controller API
  slug: eventscom-data-pipeline-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The data-pipeline-controller-v2 API from Events.com — 11 operation(s) for data-pipeline-controller-v2.
  name: Events.com Data Pipeline Controller V2 API
  slug: eventscom-data-pipeline-controller-v2-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The data-quality-controller API from Events.com — 7 operation(s) for data-quality-controller.
  name: Events.com Data Quality Controller API
  slug: eventscom-data-quality-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The data-source-migration-controller API from Events.com — 3 operation(s) for data-source-migration-controller.
  name: Events.com Data Source Migration Controller API
  slug: eventscom-data-source-migration-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Data Source Tables Controller API from Events.com — 2 operation(s) for data source tables controller.
  name: Events.com Data Source Tables Controller API
  slug: eventscom-data-source-tables-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The data-sources-controller API from Events.com — 55 operation(s) for data-sources-controller.
  name: Events.com Data Sources Controller API
  slug: eventscom-data-sources-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Document Validation Demo API from Events.com — 2 operation(s) for document validation demo.
  name: Events.com Document Validation Demo API
  slug: eventscom-document-validation-demo-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The element-link-controller API from Events.com — 6 operation(s) for element-link-controller.
  name: Events.com Element Link Controller API
  slug: eventscom-element-link-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: Operations for managing element permissions
  name: Events.com Element Permissions API
  slug: eventscom-element-permissions-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The etl-controller API from Events.com — 31 operation(s) for etl-controller.
  name: Events.com Etl Controller API
  slug: eventscom-etl-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The external-controller API from Events.com — 1 operation(s) for external-controller.
  name: Events.com External Controller API
  slug: eventscom-external-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The external-embedding-config-controller API from Events.com — 7 operation(s) for external-embedding-config-controller.
  name: Events.com External Embedding Config Controller API
  slug: eventscom-external-embedding-config-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The extraction-controller API from Events.com — 7 operation(s) for extraction-controller.
  name: Events.com Extraction Controller API
  slug: eventscom-extraction-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The file-controller API from Events.com — 6 operation(s) for file-controller.
  name: Events.com File Controller API
  slug: eventscom-file-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The folder-controller API from Events.com — 5 operation(s) for folder-controller.
  name: Events.com Folder Controller API
  slug: eventscom-folder-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The formula-processing-controller API from Events.com — 1 operation(s) for formula-processing-controller.
  name: Events.com Formula Processing Controller API
  slug: eventscom-formula-processing-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Gemini File Search (deprecated) API from Events.com — 3 operation(s) for gemini file search (deprecated).
  name: Events.com Gemini File Search (deprecated) API
  slug: eventscom-gemini-file-search-deprecated-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Global ID API from Events.com — 1 operation(s) for global id.
  name: Events.com Global ID API
  slug: eventscom-global-id-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The health check API from Events.com — 1 operation(s) for health check.
  name: Events.com health check API
  slug: eventscom-health-check-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The health-check-controller API from Events.com — 2 operation(s) for health-check-controller.
  name: Events.com Health Check Controller API
  slug: eventscom-health-check-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Home Chat Agent APIs API from Events.com — 11 operation(s) for home chat agent apis.
  name: Events.com Home Chat Agent APIs API
  slug: eventscom-home-chat-agent-apis-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The IDP API from Events.com — 65 operation(s) for idp.
  name: Events.com IDP API
  slug: eventscom-idp-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Internal API from Events.com — 5 operation(s) for internal.
  name: Events.com Internal API
  slug: eventscom-internal-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The internal-company-controller API from Events.com — 15 operation(s) for internal-company-controller.
  name: Events.com Internal Company Controller API
  slug: eventscom-internal-company-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The internal-login-and-registration-controller API from Events.com — 2 operation(s) for internal-login-and-registration-controller.
  name: Events.com Internal Login And Registration Controller API
  slug: eventscom-internal-login-and-registration-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The internal-table-controller API from Events.com — 4 operation(s) for internal-table-controller.
  name: Events.com Internal Table Controller API
  slug: eventscom-internal-table-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The invoice-controller API from Events.com — 2 operation(s) for invoice-controller.
  name: Events.com Invoice Controller API
  slug: eventscom-invoice-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The JIRA API from Events.com — 2 operation(s) for jira.
  name: Events.com JIRA API
  slug: eventscom-jira-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The KB Connectors API from Events.com — 25 operation(s) for kb connectors.
  name: Events.com KB Connectors API
  slug: eventscom-kb-connectors-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The KB Internal API from Events.com — 6 operation(s) for kb internal.
  name: Events.com KB Internal API
  slug: eventscom-kb-internal-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Knowledge Graph API from Events.com — 2 operation(s) for knowledge graph.
  name: Events.com Knowledge Graph API
  slug: eventscom-knowledge-graph-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The kyuubi-admin-controller API from Events.com — 1 operation(s) for kyuubi-admin-controller.
  name: Events.com Kyuubi Admin Controller API
  slug: eventscom-kyuubi-admin-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The lineages-controller API from Events.com — 8 operation(s) for lineages-controller.
  name: Events.com Lineages Controller API
  slug: eventscom-lineages-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: Unified connect-or-initiate flow for known connectors (Gmail, Google Drive, Calendar) via Composio, with per-company auth mapping and per-user connections.
  name: Events.com MCP Connector Auth API
  slug: eventscom-mcp-connector-auth-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: Register MCP server OAuth2 credentials via auto-discovery. Supports authorization_code (redirect) and client_credentials (immediate) flows.
  name: Events.com MCP Connectors API
  slug: eventscom-mcp-connectors-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Memories API from Events.com — 1 operation(s) for memories.
  name: Events.com Memories API
  slug: eventscom-memories-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Message Feedback API from Events.com — 1 operation(s) for message feedback.
  name: Events.com Message Feedback API
  slug: eventscom-message-feedback-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The ML-Dashboard API from Events.com — 6 operation(s) for ml-dashboard.
  name: Events.com ML Dashboard API
  slug: eventscom-ml-dashboard-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The NoCoDb API from Events.com — 18 operation(s) for nocodb.
  name: Events.com No Co Db API
  slug: eventscom-nocodb-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The NoCoDbV1 API from Events.com — 1 operation(s) for nocodbv1.
  name: Events.com No Co Db V1 API
  slug: eventscom-nocodbv1-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The NoCoDbV2 API from Events.com — 110 operation(s) for nocodbv2.
  name: Events.com No Co Db V2 API
  slug: eventscom-nocodbv2-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The NoCoDbV3 API from Events.com — 9 operation(s) for nocodbv3.
  name: Events.com No Co Db V3 API
  slug: eventscom-nocodbv3-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The node-group-config-controller API from Events.com — 3 operation(s) for node-group-config-controller.
  name: Events.com Node Group Config Controller API
  slug: eventscom-node-group-config-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The orchestration-controller API from Events.com — 15 operation(s) for orchestration-controller.
  name: Events.com Orchestration Controller API
  slug: eventscom-orchestration-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The orchestrator-controller API from Events.com — 4 operation(s) for orchestrator-controller.
  name: Events.com Orchestrator Controller API
  slug: eventscom-orchestrator-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The preference-controller API from Events.com — 2 operation(s) for preference-controller.
  name: Events.com Preference Controller API
  slug: eventscom-preference-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Python Agent API from Events.com — 9 operation(s) for python agent.
  name: Events.com Python Agent API
  slug: eventscom-python-agent-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Python Agent V2 API from Events.com — 4 operation(s) for python agent v2.
  name: Events.com Python Agent V2 API
  slug: eventscom-python-agent-v2-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The query-parser-controller API from Events.com — 3 operation(s) for query-parser-controller.
  name: Events.com Query Parser Controller API
  slug: eventscom-query-parser-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Research API from Events.com — 2 operation(s) for research.
  name: Events.com Research API
  slug: eventscom-research-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The search-controller API from Events.com — 1 operation(s) for search-controller.
  name: Events.com Search Controller API
  slug: eventscom-search-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The send-email-controller API from Events.com — 2 operation(s) for send-email-controller.
  name: Events.com Send Email Controller API
  slug: eventscom-send-email-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The shared-item-controller API from Events.com — 3 operation(s) for shared-item-controller.
  name: Events.com Shared Item Controller API
  slug: eventscom-shared-item-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The shared-item-email-controller API from Events.com — 1 operation(s) for shared-item-email-controller.
  name: Events.com Shared Item Email Controller API
  slug: eventscom-shared-item-email-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The shared-item-response-controller API from Events.com — 3 operation(s) for shared-item-response-controller.
  name: Events.com Shared Item Response Controller API
  slug: eventscom-shared-item-response-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The shared-permissions-controller API from Events.com — 3 operation(s) for shared-permissions-controller.
  name: Events.com Shared Permissions Controller API
  slug: eventscom-shared-permissions-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The slack-messaging-controller API from Events.com — 1 operation(s) for slack-messaging-controller.
  name: Events.com Slack Messaging Controller API
  slug: eventscom-slack-messaging-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The spark-job-controller API from Events.com — 4 operation(s) for spark-job-controller.
  name: Events.com Spark Job Controller API
  slug: eventscom-spark-job-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The SQL Parser APIs API from Events.com — 6 operation(s) for sql parser apis.
  name: Events.com SQL Parser APIs API
  slug: eventscom-sql-parser-apis-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The table-migration-controller API from Events.com — 6 operation(s) for table-migration-controller.
  name: Events.com Table Migration Controller API
  slug: eventscom-table-migration-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The third-party-page-admin-controller API from Events.com — 1 operation(s) for third-party-page-admin-controller.
  name: Events.com Third Party Page Admin Controller API
  slug: eventscom-third-party-page-admin-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: Resolve embedded page or agent config for third-party integrations
  name: Events.com Third Party Pages API
  slug: eventscom-third-party-pages-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The trigger-type-controller API from Events.com — 2 operation(s) for trigger-type-controller.
  name: Events.com Trigger Type Controller API
  slug: eventscom-trigger-type-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The unreal-engine-controller API from Events.com — 7 operation(s) for unreal-engine-controller.
  name: Events.com Unreal Engine Controller API
  slug: eventscom-unreal-engine-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The widget-controller API from Events.com — 4 operation(s) for widget-controller.
  name: Events.com Widget Controller API
  slug: eventscom-widget-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The WidgetV1 API from Events.com — 7 operation(s) for widgetv1.
  name: Events.com Widget V1 API
  slug: eventscom-widgetv1-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The work-flow-controller API from Events.com — 9 operation(s) for work-flow-controller.
  name: Events.com Work Flow Controller API
  slug: eventscom-work-flow-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The work-flow-v-2-controller API from Events.com — 6 operation(s) for work-flow-v-2-controller.
  name: Events.com Work Flow V 2 Controller API
  slug: eventscom-work-flow-v-2-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Workbook Agent API from Events.com — 6 operation(s) for workbook agent.
  name: Events.com Workbook Agent API
  slug: eventscom-workbook-agent-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Workbook AI Generate API from Events.com — 3 operation(s) for workbook ai generate.
  name: Events.com Workbook AI Generate API
  slug: eventscom-workbook-ai-generate-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: Configure and run AI enrichments on workbook table rows using Databar
  name: Events.com Workbook Enrichments API
  slug: eventscom-workbook-enrichments-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Workbook Generate Dashboard API from Events.com — 3 operation(s) for workbook generate dashboard.
  name: Events.com Workbook Generate Dashboard API
  slug: eventscom-workbook-generate-dashboard-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The Workflow Builder API from Events.com — 2 operation(s) for workflow builder.
  name: Events.com Workflow Builder API
  slug: eventscom-workflow-builder-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The workflow-job-scheduler-controller API from Events.com — 2 operation(s) for workflow-job-scheduler-controller.
  name: Events.com Workflow Job Scheduler Controller API
  slug: eventscom-workflow-job-scheduler-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The workflow-status-controller API from Events.com — 1 operation(s) for workflow-status-controller.
  name: Events.com Workflow Status Controller API
  slug: eventscom-workflow-status-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The workflow-template-controller API from Events.com — 5 operation(s) for workflow-template-controller.
  name: Events.com Workflow Template Controller API
  slug: eventscom-workflow-template-controller-api
- baseURL: https://datagol-be.events.com/
  baseurl_source: declared
  description: The workspace-template-controller API from Events.com — 2 operation(s) for workspace-template-controller.
  name: Events.com Workspace Template Controller API
  slug: eventscom-workspace-template-controller-api
artifact_total: 234
asyncapis:
- description: ''
  name: Eventscom Webhooks
  slug: eventscom-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Saasxl-api doc Agent Config Controller API
  slug: open-eventscom-agent-config-controller-api
- collection_type: open
  name: Saasxl-api doc Agent Config Migration Controller API
  slug: open-eventscom-agent-config-migration-controller-api
- collection_type: open
  name: Saasxl-api doc Agent Email Controller API
  slug: open-eventscom-agent-email-controller-api
- collection_type: open
  name: Saasxl-api doc Agent Job Update Controller API
  slug: open-eventscom-agent-job-update-controller-api
- collection_type: open
  name: Saasxl-api doc Agent MCP API
  slug: open-eventscom-agent-mcp-api
- collection_type: open
  name: Saasxl-api doc Agent MCP Config Controller API
  slug: open-eventscom-agent-mcp-config-controller-api
- collection_type: open
  name: DataGol AI Agent Memory API
  slug: open-eventscom-agent-memory-api
- collection_type: open
  name: Saasxl-api doc Agent Skill Controller API
  slug: open-eventscom-agent-skill-controller-api
- collection_type: open
  name: Saasxl-api doc Agent Template Controller API
  slug: open-eventscom-agent-template-controller-api
- collection_type: open
  name: Saasxl-api doc AI Feedback Controller API
  slug: open-eventscom-ai-feedback-controller-api
- collection_type: open
  name: Saasxl-api doc AI Third Party Page Controller API
  slug: open-eventscom-ai-third-party-page-controller-api
- collection_type: open
  name: Saasxl-api doc Alert Controller API
  slug: open-eventscom-alert-controller-api
- collection_type: open
  name: Saasxl-api doc Alert History API
  slug: open-eventscom-alert-history-api
- collection_type: open
  name: Saasxl-api doc Alert Notification History Controller API
  slug: open-eventscom-alert-notification-history-controller-api
- collection_type: open
  name: Saasxl-api doc API Post Workflow Test Controller API
  slug: open-eventscom-api-post-workflow-test-controller-api
- collection_type: open
  name: Saasxl-api doc AppX Deployment API
  slug: open-eventscom-appx-deployment-api
- collection_type: open
  name: Saasxl-api doc Bi Page Controller API
  slug: open-eventscom-bi-page-controller-api
- collection_type: open
  name: DataGol AI Bi Rag API
  slug: open-eventscom-bi-rag-api
- collection_type: open
  name: Saasxl-api doc Biv 1 Controller API
  slug: open-eventscom-biv-1-controller-api
- collection_type: open
  name: Saasxl-api doc Biv 2 Controller API
  slug: open-eventscom-biv-2-controller-api
- collection_type: open
  name: Saasxl-api doc Cache Controller API
  slug: open-eventscom-cache-controller-api
- collection_type: open
  name: Saasxl-api doc Catalog Search Controller API
  slug: open-eventscom-catalog-search-controller-api
- collection_type: open
  name: Saasxl-api doc Chat Conversation Controller API
  slug: open-eventscom-chat-conversation-controller-api
- collection_type: open
  name: Saasxl-api doc Comment Controller API
  slug: open-eventscom-comment-controller-api
- collection_type: open
  name: Saasxl-api doc Company Ontology Controller API
  slug: open-eventscom-company-ontology-controller-api
- collection_type: open
  name: Saasxl-api doc Company Unstructured Data Controller API
  slug: open-eventscom-company-unstructured-data-controller-api
- collection_type: open
  name: Saasxl-api doc Config Controller API
  slug: open-eventscom-config-controller-api
- collection_type: open
  name: Saasxl-api doc Connector Controller API
  slug: open-eventscom-connector-controller-api
- collection_type: open
  name: Saasxl-api doc Conversation Controller API
  slug: open-eventscom-conversation-controller-api
- collection_type: open
  name: DataGol AI Conversation File Upload API
  slug: open-eventscom-conversation-file-upload-api
- collection_type: open
  name: DataGol AI Conversation Message V2 API
  slug: open-eventscom-conversation-message-v2-api
- collection_type: open
  name: DataGol AI Conversation V2 API
  slug: open-eventscom-conversation-v2-api
- collection_type: open
  name: Saasxl-api doc Custom Agents API
  slug: open-eventscom-custom-agents-api
- collection_type: open
  name: DataGol AI Data Download API
  slug: open-eventscom-data-download-api
- collection_type: open
  name: DataGol AI Data Extraction API
  slug: open-eventscom-data-extraction-api
- collection_type: open
  name: Saasxl-api doc Data Pipeline Controller API
  slug: open-eventscom-data-pipeline-controller-api
- collection_type: open
  name: Saasxl-api doc Data Pipeline Controller V2 API
  slug: open-eventscom-data-pipeline-controller-v2-api
- collection_type: open
  name: Saasxl-api doc Data Quality Controller API
  slug: open-eventscom-data-quality-controller-api
- collection_type: open
  name: Saasxl-api doc Data Source Migration Controller API
  slug: open-eventscom-data-source-migration-controller-api
- collection_type: open
  name: DataGol AI Data Source Tables Controller API
  slug: open-eventscom-data-source-tables-controller-api
- collection_type: open
  name: Saasxl-api doc Data Sources Controller API
  slug: open-eventscom-data-sources-controller-api
- collection_type: open
  name: DataGol AI
  slug: open-eventscom-datagol-ai
- collection_type: open
  name: Saasxl-api doc
  slug: open-eventscom-datagol-platform
- collection_type: open
  name: DataGol AI
  slug: open-eventscom-datagol-python-agent
- collection_type: open
  name: DataGol AI Document Validation Demo API
  slug: open-eventscom-document-validation-demo-api
- collection_type: open
  name: Saasxl-api doc Element Link Controller API
  slug: open-eventscom-element-link-controller-api
- collection_type: open
  name: Saasxl-api doc Element Permissions API
  slug: open-eventscom-element-permissions-api
- collection_type: open
  name: Saasxl-api doc Etl Controller API
  slug: open-eventscom-etl-controller-api
- collection_type: open
  name: Saasxl-api doc External Controller API
  slug: open-eventscom-external-controller-api
- collection_type: open
  name: Saasxl-api doc External Embedding Config Controller API
  slug: open-eventscom-external-embedding-config-controller-api
- collection_type: open
  name: Saasxl-api doc Extraction Controller API
  slug: open-eventscom-extraction-controller-api
- collection_type: open
  name: Saasxl-api doc File Controller API
  slug: open-eventscom-file-controller-api
- collection_type: open
  name: Saasxl-api doc Folder Controller API
  slug: open-eventscom-folder-controller-api
- collection_type: open
  name: Saasxl-api doc Formula Processing Controller API
  slug: open-eventscom-formula-processing-controller-api
- collection_type: open
  name: DataGol AI Gemini File Search (deprecated) Gemini File Search (deprecated) API
  slug: open-eventscom-gemini-file-search-deprecated-api
- collection_type: open
  name: DataGol AI Global ID API
  slug: open-eventscom-global-id-api
- collection_type: open
  name: Eventscom health check API
  slug: open-eventscom-health-check-api
- collection_type: open
  name: Saasxl-api doc Health Check Controller API
  slug: open-eventscom-health-check-controller-api
- collection_type: open
  name: DataGol AI Home Chat Agent APIs API
  slug: open-eventscom-home-chat-agent-apis-api
- collection_type: open
  name: Saasxl-api doc IDP API
  slug: open-eventscom-idp-api
- collection_type: open
  name: DataGol AI Internal API
  slug: open-eventscom-internal-api
- collection_type: open
  name: Saasxl-api doc Internal Company Controller API
  slug: open-eventscom-internal-company-controller-api
- collection_type: open
  name: Saasxl-api doc Internal Login And Registration Controller API
  slug: open-eventscom-internal-login-and-registration-controller-api
- collection_type: open
  name: Saasxl-api doc Internal Table Controller API
  slug: open-eventscom-internal-table-controller-api
- collection_type: open
  name: Saasxl-api doc Invoice Controller API
  slug: open-eventscom-invoice-controller-api
- collection_type: open
  name: DataGol AI JIRA API
  slug: open-eventscom-jira-api
- collection_type: open
  name: Saasxl-api doc KB Connectors API
  slug: open-eventscom-kb-connectors-api
- collection_type: open
  name: Saasxl-api doc KB Internal API
  slug: open-eventscom-kb-internal-api
- collection_type: open
  name: DataGol AI Knowledge Graph API
  slug: open-eventscom-knowledge-graph-api
- collection_type: open
  name: Saasxl-api doc Kyuubi Admin Controller API
  slug: open-eventscom-kyuubi-admin-controller-api
- collection_type: open
  name: Saasxl-api doc Lineages Controller API
  slug: open-eventscom-lineages-controller-api
- collection_type: open
  name: Saasxl-api doc MCP Connector Auth API
  slug: open-eventscom-mcp-connector-auth-api
- collection_type: open
  name: Saasxl-api doc MCP Connectors API
  slug: open-eventscom-mcp-connectors-api
- collection_type: open
  name: DataGol AI Memories API
  slug: open-eventscom-memories-api
- collection_type: open
  name: DataGol AI Message Feedback API
  slug: open-eventscom-message-feedback-api
- collection_type: open
  name: DataGol AI ML Dashboard API
  slug: open-eventscom-ml-dashboard-api
- collection_type: open
  name: Saasxl-api doc No Co Db API
  slug: open-eventscom-nocodb-api
- collection_type: open
  name: Saasxl-api doc No Co Db V1 API
  slug: open-eventscom-nocodbv1-api
- collection_type: open
  name: Saasxl-api doc No Co Db V2 API
  slug: open-eventscom-nocodbv2-api
- collection_type: open
  name: Saasxl-api doc No Co Db V3 API
  slug: open-eventscom-nocodbv3-api
- collection_type: open
  name: Saasxl-api doc Node Group Config Controller API
  slug: open-eventscom-node-group-config-controller-api
- collection_type: open
  name: Saasxl-api doc Orchestration Controller API
  slug: open-eventscom-orchestration-controller-api
- collection_type: open
  name: Saasxl-api doc Orchestrator Controller API
  slug: open-eventscom-orchestrator-controller-api
- collection_type: open
  name: Saasxl-api doc Preference Controller API
  slug: open-eventscom-preference-controller-api
- collection_type: open
  name: DataGol AI Python Agent API
  slug: open-eventscom-python-agent-api
- collection_type: open
  name: DataGol AI Python Agent V2 API
  slug: open-eventscom-python-agent-v2-api
- collection_type: open
  name: Saasxl-api doc Query Parser Controller API
  slug: open-eventscom-query-parser-controller-api
- collection_type: open
  name: DataGol AI Research API
  slug: open-eventscom-research-api
- collection_type: open
  name: Saasxl-api doc Search Controller API
  slug: open-eventscom-search-controller-api
- collection_type: open
  name: Saasxl-api doc Send Email Controller API
  slug: open-eventscom-send-email-controller-api
- collection_type: open
  name: Saasxl-api doc Shared Item Controller API
  slug: open-eventscom-shared-item-controller-api
- collection_type: open
  name: Saasxl-api doc Shared Item Email Controller API
  slug: open-eventscom-shared-item-email-controller-api
- collection_type: open
  name: Saasxl-api doc Shared Item Response Controller API
  slug: open-eventscom-shared-item-response-controller-api
- collection_type: open
  name: Saasxl-api doc Shared Permissions Controller API
  slug: open-eventscom-shared-permissions-controller-api
- collection_type: open
  name: Saasxl-api doc Slack Messaging Controller API
  slug: open-eventscom-slack-messaging-controller-api
- collection_type: open
  name: Saasxl-api doc Spark Job Controller API
  slug: open-eventscom-spark-job-controller-api
- collection_type: open
  name: DataGol AI SQL Parser APIs API
  slug: open-eventscom-sql-parser-apis-api
- collection_type: open
  name: Saasxl-api doc Table Migration Controller API
  slug: open-eventscom-table-migration-controller-api
- collection_type: open
  name: Saasxl-api doc Third Party Page Admin Controller API
  slug: open-eventscom-third-party-page-admin-controller-api
- collection_type: open
  name: Saasxl-api doc Third Party Pages API
  slug: open-eventscom-third-party-pages-api
- collection_type: open
  name: Saasxl-api doc Trigger Type Controller API
  slug: open-eventscom-trigger-type-controller-api
- collection_type: open
  name: Saasxl-api doc Unreal Engine Controller API
  slug: open-eventscom-unreal-engine-controller-api
- collection_type: open
  name: Saasxl-api doc Widget Controller API
  slug: open-eventscom-widget-controller-api
- collection_type: open
  name: Saasxl-api doc Widget V1 API
  slug: open-eventscom-widgetv1-api
- collection_type: open
  name: Saasxl-api doc Work Flow Controller API
  slug: open-eventscom-work-flow-controller-api
- collection_type: open
  name: Saasxl-api doc Work Flow V 2 Controller API
  slug: open-eventscom-work-flow-v-2-controller-api
- collection_type: open
  name: DataGol AI Workbook Agent API
  slug: open-eventscom-workbook-agent-api
- collection_type: open
  name: DataGol AI Workbook AI Generate API
  slug: open-eventscom-workbook-ai-generate-api
- collection_type: open
  name: Saasxl-api doc Workbook Enrichments API
  slug: open-eventscom-workbook-enrichments-api
- collection_type: open
  name: DataGol AI Workbook Generate Dashboard API
  slug: open-eventscom-workbook-generate-dashboard-api
- collection_type: open
  name: DataGol AI Workflow Builder API
  slug: open-eventscom-workflow-builder-api
- collection_type: open
  name: Saasxl-api doc Workflow Job Scheduler Controller API
  slug: open-eventscom-workflow-job-scheduler-controller-api
- collection_type: open
  name: Saasxl-api doc Workflow Status Controller API
  slug: open-eventscom-workflow-status-controller-api
- collection_type: open
  name: Saasxl-api doc Workflow Template Controller API
  slug: open-eventscom-workflow-template-controller-api
- collection_type: open
  name: Saasxl-api doc Workspace Template Controller API
  slug: open-eventscom-workspace-template-controller-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/eventscom-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/eventscom-datagol-ai-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://events.com/
- group: docs
  title: ''
  type: APIReference
  url: https://datagol-be.events.com/swagger-ui/index.html
- group: operate
  title: ''
  type: Support
  url: https://events.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://events.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edc-core
- group: commercial
  title: ''
  type: Pricing
  url: https://events.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://org.events.com/#/en_US/events/create
- group: start
  title: ''
  type: Login
  url: https://org.events.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://events.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://events.com/privacy/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eventscom-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eventscom-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eventscom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eventscom-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eventscom-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eventscom-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eventscom-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eventscom-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/eventscom-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eventscom-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eventscom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eventscom-domain-security.yml
created: '2026-08-04'
description: Events.com is a La Jolla, California event-technology company founded by Mitch Thrower (co-founder of Active.com / The Active Network) that operates an end-to-end platform for creating, promoting, selling, and discovering events. Its organizer-facing products span ticketing and registration (Sell), digital event marketing (Promote), sponsorship management (Sponsor), on-site check-in and execution (Execute), analytics (Insights), virtual and hybrid events (Virtual), and an embeddable event calendar, alongside a consumer event-discovery destination. Events.com does not publish a public developer program, but its internal DataGol / Saasxl AI and data platform exposes three anonymously reachable OpenAPI 3.x contracts and a hosted Model Context Protocol server on production hosts, covering no-code data tables, ETL and orchestration, BI dashboards, knowledge graphs, custom agents, agent skills, and MCP connectors.
image: https://events.com/wp-content/uploads/2023/09/events-featured-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Events.com MCP Server
  slug: eventscom-mcp-server
modified: '2026-08-04'
name: Events.com
nav: Providers
network: true
overview: 'Events.com publishes 112 APIs on the [APIs.io](https://apis.io/) network, including Agent Config Controller API, Agent Config Migration Controller API, Agent Email Controller API, and 109 more. Tagged areas include Event Management, Ticketing, Event Registration, Event Marketing, and Sponsorship.


  The Events.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Events.com''s developer surface includes API reference, support, engineering blog, pricing, signup flow, authentication, and 19 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 58.4
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 112
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eventscom/refs/heads/main/screenshots/eventscom-2026-08-07T165031.png
security:
- kind: authentication
  name: Eventscom Authentication
  slug: eventscom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eventscom Domain Security
  slug: eventscom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eventscom
tags:
- Event Management
- Ticketing
- Event Registration
- Event Marketing
- Sponsorship
- Event Discovery
- Data Platform
- Business Intelligence
- Artificial Intelligence
- MCP
- agent-native
- No-Code
website: https://events.com/
---
