---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Dust Tt Agentic Access
  operation_count: 64
  slug: dust-tt-agentic-access
  summary_line: 64 operations · 32 acting · 1 human-in-the-loop
api_count: 9
apis:
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Agent configurations
  name: Dust Agents API
  slug: dust-tt-agents-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Dust apps
  name: Dust Apps API
  slug: dust-tt-apps-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Conversations
  name: Dust Conversations API
  slug: dust-tt-conversations-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Data sources
  name: Dust Datasources API
  slug: dust-tt-datasources-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Data source views
  name: Dust DatasourceViews API
  slug: dust-tt-datasourceviews-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Message feedbacks
  name: Dust Feedbacks API
  slug: dust-tt-feedbacks-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: MCP servers
  name: Dust MCP API
  slug: dust-tt-mcp-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Mentions
  name: Dust Mentions API
  slug: dust-tt-mentions-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Search
  name: Dust Search API
  slug: dust-tt-search-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Skills
  name: Dust Skills API
  slug: dust-tt-skills-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Spaces
  name: Dust Spaces API
  slug: dust-tt-spaces-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Tools
  name: Dust Tools API
  slug: dust-tt-tools-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Triggers
  name: Dust Triggers API
  slug: dust-tt-triggers-api
- baseURL: https://dust.tt/api/v1
  baseurl_source: declared
  description: Workspace
  name: Dust Workspace API
  slug: dust-tt-workspace-api
arazzos:
- description: Start a conversation, wait for the agent to request a tool action, then approve or reject it.
  name: Dust Approve a Pending Agent Tool Action
  slug: dust-tt-approve-agent-action-workflow
- description: Reserve a file upload URL, attach the file as a content fragment, then ask an agent about it.
  name: Dust Attach a File and Ask an Agent
  slug: dust-tt-attach-file-and-ask-workflow
- description: Start a conversation, mention an agent, and poll the conversation until the agent answers.
  name: Dust Converse with an Agent
  slug: dust-tt-converse-with-agent-workflow
- description: Upsert a structured table into a data source, then load rows into it and read one back.
  name: Dust Create a Table and Upsert Rows
  slug: dust-tt-create-table-and-upsert-rows-workflow
- description: List the workspace's accessible spaces, then enumerate the data sources within a chosen space.
  name: Dust Discover Spaces and Data Sources
  slug: dust-tt-discover-spaces-and-data-sources-workflow
- description: Search for an agent by name, resolve its full configuration, then open a conversation mentioning it.
  name: Dust Find Agent and Start a Conversation
  slug: dust-tt-find-agent-and-start-conversation-workflow
- description: Create a new agent configuration from a JSON definition, then open a conversation that mentions it.
  name: Dust Import an Agent and Start a Conversation
  slug: dust-tt-import-agent-and-converse-workflow
- description: Post a message into a conversation, wait for the agent reply, then submit thumbs feedback on it.
  name: Dust Message an Agent and Submit Feedback
  slug: dust-tt-message-and-submit-feedback-workflow
- description: Post a follow-up message into an existing conversation and poll the conversation for the agent reply.
  name: Dust Post Follow-up Message and Poll
  slug: dust-tt-post-message-and-poll-workflow
- description: Trigger a non-blocking Dust app run and poll the run until its status succeeds or errors.
  name: Dust Run an App and Poll for Completion
  slug: dust-tt-run-app-and-poll-workflow
- description: Resolve a mention query into an agent suggestion, then open a conversation that mentions it.
  name: Dust Suggest a Mention and Start a Conversation
  slug: dust-tt-suggest-mention-and-converse-workflow
- description: Upsert a document into a data source, wait for the upsert queue to drain, then search for it.
  name: Dust Upsert a Document and Search the Data Source
  slug: dust-tt-upsert-document-and-search-workflow
artifact_total: 72
collections:
- collection_type: postman
  name: Dust Agents API
  slug: postman-dust-agents-api
- collection_type: postman
  name: Dust Apps API
  slug: postman-dust-apps-api
- collection_type: postman
  name: Dust Conversations API
  slug: postman-dust-conversations-api
- collection_type: postman
  name: Dust Data Sources API
  slug: postman-dust-datasources-api
- collection_type: postman
  name: Dust MCP API
  slug: postman-dust-mcp-api
- collection_type: postman
  name: Dust Search API
  slug: postman-dust-search-api
- collection_type: postman
  name: Dust Skills API
  slug: postman-dust-skills-api
- collection_type: postman
  name: Dust Triggers API
  slug: postman-dust-triggers-api
- collection_type: postman
  name: Dust Workspace API
  slug: postman-dust-workspace-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dust Agents API
  slug: open-dust-agents-api
- collection_type: open
  name: Dust Apps API
  slug: open-dust-apps-api
- collection_type: open
  name: Dust Conversations API
  slug: open-dust-conversations-api
- collection_type: open
  name: Dust Data Sources API
  slug: open-dust-datasources-api
- collection_type: open
  name: Dust MCP API
  slug: open-dust-mcp-api
- collection_type: open
  name: Dust Search API
  slug: open-dust-search-api
- collection_type: open
  name: Dust Skills API
  slug: open-dust-skills-api
- collection_type: open
  name: Dust Triggers API
  slug: open-dust-triggers-api
- collection_type: open
  name: Dust Agents API
  slug: open-dust-tt-agents-api
- collection_type: open
  name: Dust Agents Apps API
  slug: open-dust-tt-apps-api
- collection_type: open
  name: Dust Agents Conversations API
  slug: open-dust-tt-conversations-api
- collection_type: open
  name: Dust Agents Datasources API
  slug: open-dust-tt-datasources-api
- collection_type: open
  name: Dust Agents DatasourceViews API
  slug: open-dust-tt-datasourceviews-api
- collection_type: open
  name: Dust Agents Feedbacks API
  slug: open-dust-tt-feedbacks-api
- collection_type: open
  name: Dust Agents MCP API
  slug: open-dust-tt-mcp-api
- collection_type: open
  name: Dust Agents Mentions API
  slug: open-dust-tt-mentions-api
- collection_type: open
  name: Dust Agents Search API
  slug: open-dust-tt-search-api
- collection_type: open
  name: Dust Agents Skills API
  slug: open-dust-tt-skills-api
- collection_type: open
  name: Dust Agents Spaces API
  slug: open-dust-tt-spaces-api
- collection_type: open
  name: Dust Agents Tools API
  slug: open-dust-tt-tools-api
- collection_type: open
  name: Dust Agents Triggers API
  slug: open-dust-tt-triggers-api
- collection_type: open
  name: Dust Agents Workspace API
  slug: open-dust-tt-workspace-api
- collection_type: open
  name: Dust Workspace API
  slug: open-dust-workspace-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dust-tt/dust/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/dust-tt/dust/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/dust-tt/dust/blob/main/SECURITY.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dust-tt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dust-tt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dust-tt-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dust/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-approve-agent-action-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-attach-file-and-ask-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-converse-with-agent-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-create-table-and-upsert-rows-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-discover-spaces-and-data-sources-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-find-agent-and-start-conversation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-import-agent-and-converse-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-message-and-submit-feedback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-post-message-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-run-app-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-suggest-mention-and-converse-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dust-tt-upsert-document-and-search-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://dust.tt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dust.tt
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dust.tt/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dust.tt/docs/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dust.tt/docs/programmatic-usage
- group: commercial
  title: ''
  type: Pricing
  url: https://dust.tt/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dust-tt
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/dust-tt/dust
- group: commercial
  title: ''
  type: License
  url: https://github.com/dust-tt/dust/blob/main/LICENSE
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dust.tt/changelog
- group: start
  title: ''
  type: Signup
  url: https://dust.tt/sign-up
- group: operate
  title: ''
  type: ContactSales
  url: https://dust.tt/home/contact
- group: auth
  title: ''
  type: Security
  url: https://dust.tt/home/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.dust.tt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dust.tt/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dust.tt/website-privacy
- group: auth
  title: ''
  type: Compliance
  url: https://dust.tt/home/security
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dust-tt/dust-sdk-js
- group: build
  title: ''
  type: SDKs
  url: https://docs.dust.tt/reference/javascript-sdk
- group: build
  title: ''
  type: CLI
  url: https://docs.dust.tt/reference/cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/dust-tt/dust-labs
- group: build
  title: ''
  type: Tools
  url: https://github.com/dust-tt/dust-github-action
- group: build
  title: ''
  type: Tools
  url: https://github.com/dust-tt/dust-n8n-node
- group: build
  title: ''
  type: Tools
  url: https://github.com/dust-tt/raycast-extension
- group: build
  title: ''
  type: Tools
  url: https://github.com/dust-tt/browse
- group: build
  title: ''
  type: Tools
  url: https://github.com/dust-tt/srchd
- group: build
  title: ''
  type: BrowserExtension
  url: https://dust.tt/home/chrome-extension
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/34241185-c7e0fdbe-b2c5-47d5-a923-8244d45cd95e
- group: docs
  title: ''
  type: OpenAPI
  url: https://dust.tt/swagger.json
- group: learn
  title: ''
  type: AcademyMode
  url: https://dust.tt/academy
- group: company
  title: ''
  type: Blog
  url: https://blog.dust.tt
- group: operate
  title: ''
  type: Forums
  url: https://dust-community.tightknit.community/join
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dust.tt
- group: start
  title: ''
  type: Industry
  url: https://dust.tt/home/industry/b2b-saas
- group: start
  title: ''
  type: Industry
  url: https://dust.tt/home/industry/financial-services
- group: start
  title: ''
  type: Industry
  url: https://dust.tt/home/industry/consulting
- group: start
  title: ''
  type: Industry
  url: https://dust.tt/home/industry/insurance
- group: start
  title: ''
  type: Industry
  url: https://dust.tt/home/industry/marketplace
- group: start
  title: ''
  type: Industry
  url: https://dust.tt/home/industry/retail-ecommerce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dust-tt
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/dust4ai
- group: commercial
  title: ''
  type: Plans
  url: plans/dust-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dust-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dust-finops.yml
created: '2026-05-24'
description: Dust is a Paris-based enterprise AI platform for building, deploying, and operating teams of AI agents that have shared context across a company's knowledge and tools. Dust positions itself as the platform for "AI Operators" — the people who design, govern, and continuously improve agentic workflows across Sales, Customer Support, Marketing, Engineering, Data & Analytics, IT, Legal, Recruiting, and Knowledge teams. Agents in Dust are model-agnostic (OpenAI, Anthropic, Google, Mistral), grounded on company data through 100+ connectors (Slack, Notion, GitHub, Google Drive, Salesforce, Zendesk, Jira, Confluence, HubSpot, BigQuery, Snowflake), exposed via a REST API, MCP servers (client- and server-side), webhooks, and OAuth2, and reachable from a multiplayer conversation UI, Slack, a Chrome extension, a Raycast extension, and a CLI. The Dust core platform is open source under the MIT license at github.com/dust-tt/dust. The hosted service is available on a per-seat Pro plan (29
  EUR / user / month) and a custom Enterprise tier (100+ seats) with SSO, SCIM, dedicated environments, EU residency, and SOC 2 Type II / GDPR / HIPAA-ready compliance.
finops:
- name: Dust Finops
  service_category: ''
  slug: dust-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dust-tt.png
json_schemas:
- name: Dust Agent Configuration
  property_count: 16
  slug: dust-agent-configuration
- name: Dust Conversation
  property_count: 1
  slug: dust-conversation
- name: Dust Data Source
  property_count: 8
  slug: dust-datasource
- name: Dust Document
  property_count: 16
  slug: dust-document
- name: Dust Skill
  property_count: 22
  slug: dust-skill
jsonld:
- class_count: 17
  name: Dust Context
  property_count: 17
  slug: dust-context
layout: provider
modified: '2026-05-24'
name: Dust
nav: Providers
network: true
overview: 'Dust publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Apps API, Conversations API, and 11 more. Tagged areas include Agents, Artificial Intelligence, Custom Workflows, Data Sources, and Dust.


  The Dust catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dust''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, pricing, changelog, and 56 more developer resources.'
plans:
- name: Dust Plans Pricing
  plan_count: 2
  slug: dust-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Dust Rate Limits
  slug: dust-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Dust API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: dust-tt-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 66.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 27.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 9.8
    contract_quality: 67.0
    developer_ergonomics: 76.2
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 76.3
  open_source:
    applies: true
    score: 60.0
  previous_composite: 66.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dust-tt/refs/heads/main/screenshots/dust-tt-2026-06-20T180330.png
security:
- kind: authentication
  name: Dust Tt Authentication
  slug: dust-tt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dust Tt Domain Security
  slug: dust-tt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dust-tt
tags:
- Agents
- Artificial Intelligence
- Custom Workflows
- Data Sources
- Dust
- Enterprise AI
- Knowledge-Management
- LLM
- MCP
- Multi-Model
- RAG
website: https://dust.tt
---
