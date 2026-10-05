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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.6
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Meltwater Agentic Access
  operation_count: 80
  slug: meltwater-agentic-access
  summary_line: 80 operations · 32 acting
api_count: 3
apis:
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Account Management API and Usage APIs
  name: Meltwater Account Management API
  phrasing_intents:
  - id: list_companies
    intent: List the companies on my account
    question: Which companies does my Meltwater account belong to?
  - id: list_workspaces
    intent: List the workspaces on my account
    question: What workspaces do I have set up?
  - id: list_tokens
    intent: List my API tokens
    question: Which API tokens have been issued on my account?
  - id: getV3UsageMeMetricsByMetric
    intent: Check usage of a feature metric
    question: How many documents have I exported through the API this period?
  - id: getV3UsageMeRequests
    intent: See how many API calls I have made
    question: How many API requests have I made this month?
  phrasing_ops: 5
  slug: meltwater-account-management-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Upload your own content into the Meltwater Platform.
  name: Meltwater Bring Your Own Content (BYOC) API
  phrasing_intents:
  - id: handleByocDocuments
    intent: Import my own documents into Meltwater
    question: How do I bring my own content into the Meltwater platform?
  - id: getV3ImportsBatches
    intent: List my content import batches
    question: Which of my content import batches failed last week?
  - id: getV3ImportsBatchesByBatchId
    intent: Check the status of one import batch
    question: Did my uploaded content batch finish importing, and how many documents made it?
  - id: getV3ImportsImportTagsByImportTag
    intent: Get statistics for an import tag
    question: How many documents have been imported under one of my import tags?
  phrasing_ops: 4
  slug: meltwater-bring-your-own-content-byoc-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Fetch analytics on data within your private index.
  name: Meltwater Explore+ Analytics API
  phrasing_intents:
  - id: postV3ExplorePlusAnalyticsCustom
    intent: Analyse earned media in my private index
    question: How do I run analytics over the earned coverage stored in my Explore+ private index?
  - id: getV3ExplorePlusAnalyticsCustomCatalog
    intent: List analytics options for my private index
    question: What analysis types can I run against my private index?
  phrasing_ops: 2
  slug: meltwater-explore-analytics-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Manage your Explore+ assets including searches and custom fields.
  name: Meltwater Explore+ Assets API
  phrasing_intents:
  - id: getV3ExplorePlusAssetsCustomFields
    intent: List custom fields
    question: What custom fields are set up in my workspace?
  - id: postV3ExplorePlusAssetsCustomFields
    intent: Create a custom field
    question: How do I add a new custom field for classifying content?
  - id: getV3ExplorePlusAssetsCustomFieldsByCustomFieldId
    intent: Get one custom field
    question: What is configured on a specific custom field?
  - id: putV3ExplorePlusAssetsCustomFieldsByCustomFieldId
    intent: Update a custom field
    question: How do I rename or change an existing custom field?
  - id: deleteV3ExplorePlusAssetsCustomFieldsByCustomFieldId
    intent: Delete a custom field
    question: How do I remove a custom field I no longer need?
  - id: postV3ExplorePlusAssetsCustomFieldsByCustomFieldIdValues
    intent: Add a value to a custom field
    question: How do I add a new option to an existing custom field?
  - id: getV3ExplorePlusAssetsCustomFieldsByCustomFieldIdValuesByValueId
    intent: Get one custom field value
    question: What does a particular value of a custom field contain?
  - id: putV3ExplorePlusAssetsCustomFieldsByCustomFieldIdValuesByValueId
    intent: Update a custom field value
    question: How do I rename one of the values in a custom field?
  phrasing_ops: 20
  slug: meltwater-explore-assets-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Export earned documents from your private index.
  name: Meltwater Explore+ Search API
  phrasing_intents:
  - id: postV3ExplorePlusSearch
    intent: Search documents in my private index
    question: How do I pull documents out of my Explore+ private index?
  phrasing_ops: 1
  slug: meltwater-explore-search-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Analyse multiple types of Meltwater data, run volume time series, top tags and sentiment counts.
  name: Meltwater Listening Analytics API
  phrasing_intents:
  - id: getV3Analytics-searchId-start-end-tz-source-country-language-company_id
    intent: Summarize analytics for a saved search
    question: How much coverage did my saved search get over a time range in Meltwater?
  - id: getV3AnalyticsTop_tags-searchId-start-end-tz-source-country-language-size-company_id
    intent: Rank the top tags and hashtags in a saved search
    question: Which hashtags show up most in the results of my saved search?
  - id: getV3AnalyticsTop_locations-searchId-start-end-tz-source-country-language-size-level-company_id
    intent: Rank the top locations in a saved search
    question: Where geographically is my saved search being talked about most?
  - id: getV3AnalyticsTop_shared-searchId-start-end-tz-source-country-language-size-sort_by-company_id
    intent: Rank the most shared documents in a saved search
    question: Which posts matching my saved search were shared the most?
  - id: getV3AnalyticsTop_entities-searchId-start-end-tz-source-country-language-size-sentiment-company_id
    intent: Rank the top named entities in a saved search
    question: Which people, brands and organizations are named most in my saved search?
  - id: getV3AnalyticsTop_sources-searchId-start-end-tz-source-country-language-size-min_authority-company_id
    intent: Rank the top sources and authors in a saved search
    question: Which outlets or authors produce the most results for my saved search?
  - id: getV3AnalyticsTop_keyphrases-searchId-start-end-tz-source-country-language-size-sentiment-company_id
    intent: Rank the top keyphrases in a saved search
    question: What phrases keep coming up in coverage matched by my saved search?
  - id: getV3AnalyticsTop_mentions-searchId-start-end-tz-source
    intent: Rank the top @mentions in a saved search
    question: Which accounts get @mentioned most in my saved search results?
  phrasing_ops: 12
  slug: meltwater-listening-analytics-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Data exports for onetime and recurring jobs.
  name: Meltwater Listening Exports API
  phrasing_intents:
  - id: create_onetime_export
    intent: Create a one-time export
    question: How do I export listening results once, without a schedule?
  - id: list_onetime_exports
    intent: List my one-time exports
    question: Which one-time exports have I created?
  - id: show_onetime_export
    intent: Get a one-time export's details
    question: Is my one-time export finished yet?
  - id: delete_onetime_export
    intent: Delete a one-time export
    question: How do I get rid of an old one-time export?
  - id: create_recurring_export
    intent: Create a recurring export
    question: How do I set up an export of listening data that repeats on a schedule?
  - id: list_recurring_exports
    intent: List my recurring exports
    question: Which recurring exports are currently scheduled?
  - id: show_recurring_export
    intent: Get a recurring export's details
    question: What schedule is a particular recurring export on?
  - id: delete_recurring_export
    intent: Delete a recurring export
    question: How do I stop a recurring export from running again?
  phrasing_ops: 8
  slug: meltwater-listening-exports-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Search Meltwater data using saved searches to integrate with your own API connectors and internal systems.
  name: Meltwater Listening Search API
  phrasing_intents:
  - id: create-earned-search
    intent: Search earned media results with a saved search
    question: How do I pull the actual earned media documents matching my saved search in Meltwater?
  phrasing_ops: 1
  slug: meltwater-listening-search-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Manage Saved Searches
  name: Meltwater Listening Search Management API
  phrasing_intents:
  - id: list_searches
    intent: List my saved searches
    question: Which saved searches do I have in Meltwater?
  - id: create_search
    intent: Create a saved search
    question: How do I create a new saved search to monitor a brand?
  - id: get_search
    intent: Get one saved search's definition
    question: What query is behind a particular saved search?
  - id: update_search
    intent: Update an existing saved search
    question: How do I change the keywords of a saved search I already have?
  - id: delete_search
    intent: Delete a saved search
    question: How do I remove a saved search I no longer use?
  - id: search_count
    intent: Estimate how many results a search returns
    question: Roughly how many results does my saved search match in a given period?
  - id: list_tags
    intent: List my document tags
    question: What tags have been created for labelling documents?
  - id: postV3Tags
    intent: Create a new document tag
    question: How do I define a brand-new tag before labelling any documents with it?
  phrasing_ops: 13
  slug: meltwater-listening-search-management-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Streaming of Meltwater data to integrate with your internal systems and workflows.
  name: Meltwater Listening Streaming API
  phrasing_intents:
  - id: getAllHooks
    intent: List my streaming hooks
    question: Which streaming hooks have I set up?
  - id: createHook
    intent: Stream a saved search's results to a URL
    question: How do I get Meltwater search results pushed to my own endpoint in real time?
  - id: deleteHook
    intent: Delete a streaming hook
    question: How do I stop search results being sent to my endpoint?
  - id: getHook
    intent: Get one streaming hook
    question: Which search and target URL is a particular hook tied to?
  phrasing_ops: 4
  slug: meltwater-listening-streaming-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: AI-powered chat completion and project listing features.
  name: Meltwater Mira API
  phrasing_intents:
  - id: postV3MiraChat
    intent: Ask Mira a question
    question: How do I send a single prompt to Meltwater's Mira assistant?
  - id: postV3MiraResponses
    intent: Send a multi-message conversation to Mira
    question: Can I pass a whole message history to Mira rather than one prompt?
  - id: getV3MiraProjects
    intent: List my Mira projects
    question: Which Mira projects do I have access to?
  phrasing_ops: 3
  slug: meltwater-mira-api-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Retrieve owned social metrics and analytics.
  name: Meltwater Owned Analytics API
  phrasing_intents:
  - id: getV3OwnedAccounts
    intent: List connected social accounts
    question: Which owned social accounts are connected to my company?
  - id: getV3OwnedAccountsMetricsBreakdown
    intent: Break down an owned account metric by category
    question: What countries does my Facebook page audience come from?
  - id: getV3OwnedAccountsMetricsHeatmap
    intent: Get a day-and-hour heatmap for an owned account
    question: When during the week is my page audience most active?
  - id: getV3OwnedAccountsMetricsNestedBreakdown
    intent: Break down an owned account metric two levels deep
    question: How is my page audience split by gender and then by age group?
  - id: getV3OwnedAccountsMetricsNumeric
    intent: Get simple numeric metrics for an owned account
    question: How many fans does my page have right now?
  - id: getV3OwnedAccountsPostsTopPosts
    intent: Find the top posts on owned social accounts
    question: Which of my own posts got the most engagement last month?
  - id: getV3OwnedSupportedMetrics
    intent: List supported owned social metrics
    question: Which metric IDs can I request for my owned social accounts?
  phrasing_ops: 7
  slug: meltwater-owned-analytics-api
- description: Meltwater MCP is a single remote Model Context Protocol server that exposes a customer's Meltwater assets (saved searches, tags and other configured objects) and Meltwater data (news and social mentio
  name: Meltwater MCP
  slug: meltwater-mcp
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Analyze data with metrics and KPIs for LLM prompts
  name: Meltwater Analyze API
  phrasing_intents:
  - id: analyze
    intent: Run an analytics query with nested analyses
    question: How do I run an analytics query over a date range in Meltwater?
  phrasing_ops: 1
  slug: meltwater-analyze-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Export content and manage export jobs
  name: Meltwater Export API
  phrasing_intents:
  - id: listExports
    intent: List content export jobs
    question: Which content export jobs exist for a given data provider?
  - id: createExport
    intent: Create a content export job
    question: How do I export content from my saved searches to a file?
  - id: getExport
    intent: Get a content export job's details
    question: How do I check on a content export job I already started?
  - id: deleteExport
    intent: Delete a content export job
    question: How do I remove a content export job I no longer need?
  phrasing_ops: 4
  slug: meltwater-export-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Endpoints to list LLM prompts and folders available for analytics
  name: Meltwater LLM API
  phrasing_intents:
  - id: listLLMPrompts
    intent: List my LLM prompts
    question: Which LLM prompts do I have saved for LLM analytics?
  - id: listLLMFolders
    intent: List my LLM prompt folders
    question: How are my LLM prompts organized into folders?
  phrasing_ops: 2
  slug: meltwater-llm-api
artifact_total: 44
asyncapis:
- description: ''
  name: Meltwater Webhooks
  slug: meltwater-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Meltwater Account Management API
  slug: open-meltwater-account-management-api
- collection_type: open
  name: Meltwater Account Management Bring Your Own Content (BYOC) API
  slug: open-meltwater-bring-your-own-content-byoc-api
- collection_type: open
  name: Meltwater Account Management Explore+ Analytics API
  slug: open-meltwater-explore-analytics-api
- collection_type: open
  name: Meltwater Account Management Explore+ Assets API
  slug: open-meltwater-explore-assets-api
- collection_type: open
  name: Meltwater Account Management Explore+ Search API
  slug: open-meltwater-explore-search-api
- collection_type: open
  name: Meltwater Account Management Listening Analytics API
  slug: open-meltwater-listening-analytics-api
- collection_type: open
  name: Meltwater Account Management Listening Exports API
  slug: open-meltwater-listening-exports-api
- collection_type: open
  name: Meltwater Account Management Listening Search API
  slug: open-meltwater-listening-search-api
- collection_type: open
  name: Meltwater Account Management Listening Search Management API
  slug: open-meltwater-listening-search-management-api
- collection_type: open
  name: Meltwater Account Management Listening Streaming API
  slug: open-meltwater-listening-streaming-api
- collection_type: open
  name: Meltwater Account Management Mira API API
  slug: open-meltwater-mira-api-api
- collection_type: open
  name: Meltwater Account Management Owned Analytics API
  slug: open-meltwater-owned-analytics-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/overlays/meltwater-api-v4-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/meltwater-api-v4-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/agentic-access/meltwater-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/meltwater-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/security/meltwater-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/meltwater-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/security/meltwater-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meltwater-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/authentication/meltwater-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meltwater-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.meltwater.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.meltwater.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/meltwater
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meltwater
- group: company
  title: ''
  type: Blog
  url: https://www.meltwater.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meltwater.com/en/suite/data-api-integration
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.meltwater.com
- group: other
  title: ''
  type: X
  url: https://x.com/Meltwater
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/plans/meltwater-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meltwater-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/rate-limits/meltwater-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/meltwater-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/finops/meltwater-finops.yml
  title: ''
  type: FinOps
  url: finops/meltwater-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/well-known/meltwater-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meltwater-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/well-known/meltwater-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/meltwater-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.meltwater.com/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/security/meltwater-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/meltwater-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/mcp/meltwater-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/meltwater-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/mcp/meltwater-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/meltwater-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/llms/meltwater-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meltwater-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/scopes/meltwater-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/meltwater-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/conformance/meltwater-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meltwater-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/errors/meltwater-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meltwater-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/lifecycle/meltwater-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/meltwater-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/conventions/meltwater-conventions.yml
  title: ''
  type: Conventions
  url: conventions/meltwater-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/changelog/meltwater-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/meltwater-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/data-model/meltwater-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meltwater-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/asyncapi/meltwater-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/meltwater-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/sandbox/meltwater-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/meltwater-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/packages/meltwater-packages.yml
  title: ''
  type: Packages
  url: packages/meltwater-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/examples/meltwater-api-examples.json
  title: ''
  type: Examples
  url: examples/meltwater-api-examples.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/vocabulary/meltwater-vocabulary.json
  title: ''
  type: Vocabulary
  url: vocabulary/meltwater-vocabulary.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/json-schema/meltwater-schemas.json
  title: ''
  type: JSONSchema
  url: json-schema/meltwater-schemas.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/rules/meltwater-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/meltwater-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/json-ld/meltwater-api.jsonld
  title: ''
  type: JSONLD
  url: json-ld/meltwater-api.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.meltwater.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.meltwater.com/api-reference/api-reference-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.meltwater.com/guides/getting-started/overview
- group: operate
  title: ''
  type: Support
  url: https://developer.meltwater.com/help/support
- group: operate
  title: ''
  type: FAQ
  url: https://developer.meltwater.com/help/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meltwater.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meltwater.com/en/privacy
- group: start
  title: ''
  type: Login
  url: https://app.meltwater.com/
- group: start
  title: ''
  type: Console
  url: https://developer.meltwater.com/tools/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meltwater
created: '2026-06-13'
description: Meltwater is a media intelligence platform providing REST APIs for media monitoring, social listening, journalist outreach, PR analytics, and brand reputation management. The API enables programmatic access to billions of editorial, blog, and social media conversations across news sources and social networks, with capabilities for searching, exporting, streaming, and analyzing mentions, as well as fetching owned social account analytics.
examples:
- key_count: 80
  name: Meltwater Api Examples
  slug: meltwater-api-examples
finops:
- name: Meltwater Finops
  service_category: ''
  slug: meltwater-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meltwater.png
json_schemas:
- name: Meltwater API Schemas
  property_count: 0
  slug: meltwater-schemas
jsonld:
- class_count: 52
  name: Meltwater Api Context
  property_count: 1
  slug: meltwater-api
layout: provider
mcp_servers:
- description: Remote MCP server at api.meltwater.com requiring an API key.
  name: Meltwater MCP Server
  slug: meltwater-mcp-yml
modified: '2026-09-16'
name: Meltwater
nav: Providers
network: true
overview: 'Meltwater publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account Management API, Bring Your Own Content (BYOC) API, Explore+ Analytics API, and 13 more. Tagged areas include Media Monitoring, Social Listening, PR Analytics, Brand Intelligence, and News API.


  The Meltwater catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Meltwater''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, sandbox, code examples, and 42 more developer resources.'
plans:
- name: Meltwater Plans Pricing
  plan_count: 3
  slug: meltwater-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 7
  name: Meltwater Rate Limits
  slug: meltwater-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Meltwater API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: meltwater-jsonschema-spectral-rules
scopes:
- name: Meltwater Scopes
  scope_count: 5
  slug: meltwater-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 82.8
    catalog_earned_first_party: 24.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 28.0
    contract_quality: 67.6
    developer_ergonomics: 66.1
    discoverability: 80.0
    operational_transparency: 84.2
  previous_composite: 73.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/screenshots/meltwater-2026-06-20T185137.png
security:
- kind: authentication
  name: Meltwater Authentication
  slug: meltwater-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Meltwater Domain Security
  slug: meltwater-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meltwater Vulnerability Disclosure
  slug: meltwater-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Meltwater Trust Center
  slug: meltwater-trust-center
  summary_line: trust center published
slug: meltwater
tags:
- Media Monitoring
- Social Listening
- PR Analytics
- Brand Intelligence
- News API
- Social Analytics
- Media Intelligence
website: https://www.meltwater.com
---
