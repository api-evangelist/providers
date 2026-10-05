---
access_model:
  confidence: high
  label: Enterprise, on request
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.tryprofound.com/pricing
  - https://docs.tryprofound.com/rest-api/introduction
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.5
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 90
  human_in_the_loop: 0
  name: Profound Agentic Access
  operation_count: 125
  slug: profound-agentic-access
  summary_line: 125 operations · 90 acting
api_count: 2
apis:
- description: The inbound log-ingestion endpoint for Profound Agent Analytics. Customers POST batches of up to 1,000 web-request log entries as JSON (timestamp, method, host, path, status_code, ip, user_agent, plus
  name: Profound Agent Analytics Ingestion API
  slug: profound-agent-analytics-ingestion-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Agents API from Profound — 8 operation(s) for agents.
  name: Profound Agents API
  phrasing_intents:
  - id: list_agents_v1_agents_get
    intent: List the organization's agents
    question: Which agents does my organization have in Profound?
  - id: create_agent_v1_agents_post
    intent: Create a new draft agent
    question: How do I build a new agent from scratch for my organization?
  - id: publish_agent_v1_agents__agent_id__publish_post
    intent: Publish an agent's draft as live
    question: How do I take my agent's draft live?
  - id: list_node_types_v1_agents_node_types_get
    intent: List node types for building agents
    question: What building blocks can I use when designing an agent workflow?
  - id: get_node_type_schema_v1_agents_node_types__node_type__schema_get
    intent: Get the config schema for a node type
    question: What configuration fields does a particular agent node type accept?
  - id: get_agent_v1_agents__agent_id__get
    intent: Get an agent's details
    question: Can I look up one agent's details and status?
  - id: update_agent_v1_agents__agent_id__patch
    intent: Replace an agent's draft graph
    question: How do I fix my agent's workflow without creating a new agent?
  - id: get_agent_graph_v1_agents__agent_id__graph_get
    intent: Get an agent's workflow graph
    question: Can I export an agent's nodes and edges so I can copy it?
  phrasing_ops: 10
  slug: profound-agents-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The beta API from Profound — 2 operation(s) for beta.
  name: Profound Beta API
  phrasing_intents:
  - id: optimization_list_v1_content__asset_id__optimization_get
    intent: List content optimizations for an asset
    question: Which content optimization analyses exist for my brand asset?
  - id: optimization_analysis_v1_content__asset_id__optimization__content_id__get
    intent: Get one content optimization analysis
    question: What does the optimization analysis say about a specific piece of content?
  phrasing_ops: 2
  slug: profound-beta-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Bot Traffic Reports API from Profound — 2 operation(s) for bot traffic reports.
  name: Profound Bot Traffic Reports API
  phrasing_intents:
  - id: get_bots_report_v1_v1_reports_bots_post
    intent: Report daily AI bot traffic to a domain
    question: How many AI crawler visits did my site get each day?
  - id: get_bots_report_v2_v2_reports_bots_post
    intent: Report hourly AI bot traffic to a domain
    question: Which AI bots hit my site hour by hour, and on which paths?
  phrasing_ops: 2
  slug: profound-bot-traffic-reports-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Categories API from Profound — 10 operation(s) for categories.
  name: Profound Categories API
  phrasing_intents:
  - id: get_categories_v1_org_categories_get
    intent: List the organization's categories
    question: Which tracking categories are set up for my organization?
  - id: get_category_topics_v1_org_categories__category_id__topics_get
    intent: List the topics in a category
    question: What topics are defined under one of my categories?
  - id: get_category_tags_v1_org_categories__category_id__tags_get
    intent: List the prompt tags in a category
    question: What tags are used to label prompts in my category?
  - id: get_category_regions_v1_org_categories__category_id__regions_get
    intent: List the regions tracked in a category
    question: Which geographic regions does one of my categories track?
  - id: get_category_citation_categories_v1_org_categories__category_id__citation_categories_get
    intent: List citation buckets for a category
    question: How are cited sources grouped into buckets in my category?
  - id: get_category_citation_tags_v1_org_categories__category_id__citation_tags_get
    intent: List custom citation tags for a category
    question: What custom labels have we defined for cited sources in a category?
  - id: get_category_prompts_v1_org_categories__category_id__prompts_get
    intent: List prompts tracked in a category
    question: Which prompts are we tracking in a category?
  - id: create_category_prompts_v1_org_categories__category_id__prompts_post
    intent: Add new prompts to a category
    question: How do I start tracking new prompts in a category?
  phrasing_ops: 12
  slug: profound-categories-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Content API from Profound — 2 operation(s) for content.
  name: Profound Content API
  phrasing_intents:
  - id: optimization_list_v1_content__asset_id__optimization_get
    intent: List content optimizations for an asset
    question: Which content optimization analyses exist for my brand asset?
  - id: optimization_analysis_v1_content__asset_id__optimization__content_id__get
    intent: Get one content optimization analysis
    question: What does the optimization analysis say about a specific piece of content?
  phrasing_ops: 2
  slug: profound-content-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Content optimization API from Profound — 2 operation(s) for content optimization.
  name: Profound Content optimization API
  phrasing_intents:
  - id: optimization_list_v1_content__asset_id__optimization_get
    intent: List content optimizations for an asset
    question: Which content optimization analyses exist for my brand asset?
  - id: optimization_analysis_v1_content__asset_id__optimization__content_id__get
    intent: Get one content optimization analysis
    question: What does the optimization analysis say about a specific piece of content?
  phrasing_ops: 2
  slug: profound-content-optimization-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Documents API from Profound — 3 operation(s) for documents.
  name: Profound Documents API
  phrasing_intents:
  - id: list_documents_v1_documents_get
    intent: List the organization's documents
    question: Which Profound documents can my organization see, most recently edited first?
  - id: create_document_v1_documents_post
    intent: Create a markdown document
    question: How do I create a new document from markdown?
  - id: read_document_v1_documents__document_id__get
    intent: Read a document with tabs and comments
    question: Can I read the full text and comments of a document?
  - id: patch_document_v1_documents__document_id__patch
    intent: Rename a document or change its visibility
    question: How do I rename a document?
  - id: delete_document_v1_documents__document_id__delete
    intent: Delete a document created via the API
    question: Can I delete a document that was created through the API?
  - id: replace_document_content_v1_documents__document_id__content_post
    intent: Overwrite a document's entire body
    question: How do I replace all the text in a document with new markdown?
  phrasing_ops: 6
  slug: profound-documents-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Human Referrals API from Profound — 2 operation(s) for human referrals.
  name: Profound Human Referrals API
  phrasing_intents:
  - id: get_referrals_report_v1_v1_reports_referrals_post
    intent: Report daily human referrals from AI
    question: How much daily referral traffic are AI assistants sending to my site?
  - id: get_referrals_report_v2_v2_reports_referrals_post
    intent: Report hourly human referrals from AI
    question: Which hours of the day bring the most AI-referred visitors to my site?
  phrasing_ops: 2
  slug: profound-human-referrals-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Integrations API from Profound — 1 operation(s) for integrations.
  name: Profound Integrations API
  phrasing_intents:
  - id: list_integrations_v1_integrations_get
    intent: List connected integrations
    question: Which integrations has my organization connected?
  phrasing_ops: 1
  slug: profound-integrations-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Knowledge bases API from Profound — 4 operation(s) for knowledge bases.
  name: Profound Knowledge bases API
  phrasing_intents:
  - id: list_knowledge_bases_v1_knowledge_bases_get
    intent: List knowledge bases
    question: Which knowledge bases can my API key access?
  - id: search_knowledge_base_v1_knowledge_bases__knowledge_base_id__search_post
    intent: Search a knowledge base
    question: How do I find passages in my knowledge base that answer a question?
  - id: add_document_v1_knowledge_bases__knowledge_base_id__documents_post
    intent: Add a document to a knowledge base
    question: How do I add a new document to my knowledge base?
  - id: update_document_v1_knowledge_bases__knowledge_base_id__documents_put
    intent: Overwrite a knowledge base document
    question: How do I update the contents of a document that's already in my knowledge base?
  - id: delete_document_v1_knowledge_bases__knowledge_base_id__documents_delete
    intent: Delete a document from a knowledge base
    question: How do I remove a document from my knowledge base?
  - id: add_folder_v1_knowledge_bases__knowledge_base_id__folders_post
    intent: Create a folder in a knowledge base
    question: Can I organize my knowledge base into folders?
  - id: delete_folder_v1_knowledge_bases__knowledge_base_id__folders_delete
    intent: Delete a folder from a knowledge base
    question: How do I remove a folder and everything in it from my knowledge base?
  phrasing_ops: 7
  slug: profound-knowledge-bases-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The OpenAI Ads API from Profound — 1 operation(s) for openai ads.
  name: Profound OpenAI Ads API
  phrasing_intents:
  - id: get_account_insights_v1_ads_openai_ads_ad_account_insights_get
    intent: Get OpenAI Ads account insights
    question: How are my OpenAI Ads campaigns performing?
  phrasing_ops: 1
  slug: profound-openai-ads-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Organization API from Profound — 16 operation(s) for organization.
  name: Profound Organization API
  phrasing_intents:
  - id: list_organizations_v1_org_get
    intent: List organizations my API key can access
    question: Which organizations does my API key give me access to?
  - id: get_regions_v1_org_regions_get
    intent: List the organization's regions
    question: What regions are configured across my whole organization?
  - id: get_models_v1_org_models_get
    intent: List the AI models the organization tracks
    question: Which AI models or answer engines does my organization monitor?
  - id: get_domains_v1_org_domains_get
    intent: List the organization's domains
    question: Which website domains are registered to my organization?
  - id: get_assets_v1_org_assets_get
    intent: List assets across the organization
    question: What brands and assets exist across all of my organization's categories?
  - id: get_personas_v1_org_personas_get
    intent: List personas across the organization
    question: What personas are defined anywhere in my organization?
  - id: get_categories_v1_org_categories_get
    intent: List the organization's categories
    question: Which tracking categories are set up for my organization?
  - id: get_category_topics_v1_org_categories__category_id__topics_get
    intent: List the topics in a category
    question: What topics are defined under one of my categories?
  phrasing_ops: 18
  slug: profound-organization-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Projects API from Profound — 10 operation(s) for projects.
  name: Profound Projects API
  phrasing_intents:
  - id: list_projects_v1_projects_get
    intent: List content projects in a category
    question: What content projects exist for one of my categories?
  - id: create_project_v1_projects_post
    intent: Create a content project
    question: How do I start a new content project for a category?
  - id: list_project_generations_v1_projects_generations_get
    intent: List project generation runs
    question: Which project generation jobs have run in my category?
  - id: get_project_generation_status_v1_projects_generations__run_id__get
    intent: Check a project generation run
    question: Is my project generation job finished yet?
  - id: get_project_v1_projects__project_id__get
    intent: Get a content project
    question: Can I view the full details of one content project?
  - id: delete_project_v1_projects__project_id__delete
    intent: Delete a content project
    question: How do I permanently remove a content project?
  - id: get_project_status_v1_projects__project_id__status_get
    intent: Get a content project's status
    question: What state is my content project in right now?
  - id: archive_project_v1_projects__project_id__archive_post
    intent: Archive a content project
    question: Can I put a finished project away without deleting it?
  phrasing_ops: 15
  slug: profound-projects-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Prompts API from Profound — 3 operation(s) for prompts.
  name: Profound Prompts API
  phrasing_intents:
  - id: get_answers_v1_prompts_answers_post
    intent: Get AI answers to tracked prompts
    question: What did AI assistants actually answer to the prompts we track?
  - id: query_answers_v2_v2_prompts_answers_post
    intent: Query prompt answers with cursor paging
    question: Is there a newer answers query that pages with a cursor?
  - id: stream_answers_v2_v2_prompts_answers_stream_post
    intent: Stream prompt answers
    question: Can I stream a large set of AI answers instead of paging?
  phrasing_ops: 3
  slug: profound-prompts-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Reports API from Profound — 62 operation(s) for reports.
  name: Profound Reports API
  phrasing_intents:
  - id: query_citations_v1_reports_citations_post
    intent: Report which sources AI answers cite
    question: Which websites do AI answers cite most in my category?
  - id: stream_citations_v1_reports_citations_stream_post
    intent: Stream the v1 citations report
    question: Can I stream a big citations report row by row rather than paginate it?
  - id: query_visibility_v1_reports_visibility_post
    intent: Report brand visibility in AI answers
    question: How visible is my brand in AI-generated answers compared with competitors?
  - id: stream_visibility_v1_reports_visibility_stream_post
    intent: Stream the v1 visibility report
    question: Is there a streaming version of the original visibility report?
  - id: query_sentiment_v1_reports_sentiment_post
    intent: Report sentiment toward brands in AI answers
    question: Do AI answers talk about my brand positively or negatively?
  - id: stream_sentiment_v1_reports_sentiment_stream_post
    intent: Stream the v1 sentiment report
    question: Can I stream the original sentiment report rather than wait for one big response?
  - id: query_sentiment_v2_v1_reports_sentiment_v2_post
    intent: Report sentiment for one named brand
    question: What's the sentiment toward one specific brand by name, compared with a prior period?
  - id: query_web_search_results_v1_reports_web_search_results_post
    intent: Report web search results behind AI answers
    question: Which web search results do AI engines pull up for my category's prompts?
  phrasing_ops: 62
  slug: profound-reports-api
artifact_total: 25
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/capabilities/profound-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/profound-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/agentic-access/profound-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/profound-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.tryprofound.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryprofound.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryprofound.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryprofound.com/api-reference/organization/get-categories
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryprofound.com/rest-api/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.tryprofound.com
- group: company
  title: ''
  type: Blog
  url: https://www.tryprofound.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cooper-square-technologies
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryprofound.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.tryprofound.com/rest-api/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryprofound.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.tryprofound.com/signup
- group: start
  title: ''
  type: Login
  url: https://platform.tryprofound.com/welcome
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tryprofound.com/legal/privacy-policy
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/openapi/_original/profound-external-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/profound-external-api-openapi.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/overlays/profound-external-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/profound-external-api-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/packages/profound-packages.yml
  title: ''
  type: Packages
  url: packages/profound-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/packages/profound-packages.yml
  title: ''
  type: SDKs
  url: packages/profound-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/profound/
- group: build
  title: ''
  type: JavaScript SDK
  url: https://www.npmjs.com/package/@profoundai/client
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/mcp/profound-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/profound-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/mcp/profound-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/profound-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/a2a/profound-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/profound-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/authentication/profound-authentication.yml
  title: ''
  type: Authentication
  url: authentication/profound-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/scopes/profound-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/profound-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/conventions/profound-conventions.yml
  title: ''
  type: Conventions
  url: conventions/profound-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/errors/profound-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/profound-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/data-model/profound-data-model.yml
  title: ''
  type: DataModel
  url: data-model/profound-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/conformance/profound-conformance.yml
  title: ''
  type: Conformance
  url: conformance/profound-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/changelog/profound-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/profound-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/rate-limits/profound-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/profound-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/plans/profound-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/profound-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/lifecycle/profound-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/profound-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/llms/profound-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/profound-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/well-known/profound-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/profound-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/well-known/profound-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/profound-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/security/profound-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/profound-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/security/profound-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/profound-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tryprofound.com/vulnerability-reporting
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/security/profound-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/profound-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tryprofound.com
- group: operate
  title: ''
  type: Contact
  url: mailto:team@tryprofound.com
created: '2026-07-17'
description: Profound is a marketing platform for the AI era and a leading platform for Answer Engine Optimization (AEO). Operated by Cooper Square Technologies Inc. (dba Profound) in New York, it helps brands measure and improve how they are represented across AI answer engines and assistants — ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews and AI Mode, Copilot, and Grok — through answer-engine insights, agent analytics, prompt volumes, shopping visibility, and content optimization. Profound publishes a 125-operation OpenAPI 3.1 for its External API at api.tryprofound.com, runs a separate Agent Analytics Ingestion API, ships official Python and TypeScript SDKs, and operates a hosted remote MCP server at mcp.tryprofound.com with OAuth 2.1 and a conformant A2A agent card. API access is included on the Enterprise plan on request. Profound is SOC 2 and HIPAA aligned and publishes a responsible-disclosure policy. Backed by Kleiner Perkins.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/profound.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.tryprofound.com over HTTP requiring OAuth.
  name: Profound MCP Server
  slug: profound-mcp
modified: '2026-09-16'
name: Profound
nav: Providers
network: true
overview: 'Profound publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Beta API, Bot Traffic Reports API, and 13 more. Tagged areas include Company, Artificial Intelligence, Answer Engine Optimization, AEO, and AI Search.


  Profound''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 38 more developer resources.'
plans:
- name: Profound Plans Pricing
  plan_count: 3
  slug: profound-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Profound Rate Limits
  slug: profound-rate-limits
scopes:
- name: Profound Scopes
  scope_count: 4
  slug: profound-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode/refreshToken
score:
  band: exemplar
  composite: 66.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 75.0
    contract_governance: 4.5
    contract_quality: 49.3
    developer_ergonomics: 81.0
    discoverability: 75.0
    operational_transparency: 65.8
  previous_composite: 66.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/screenshots/profound-2026-08-17T080414.png
security:
- kind: authentication
  name: Profound Authentication
  slug: profound-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Profound Domain Security
  slug: profound-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Profound Vulnerability Disclosure
  slug: profound-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Profound Trust Center
  slug: profound-trust-center
  summary_line: SOC 2, HIPAA
slug: profound
tags:
- Company
- Artificial Intelligence
- Answer Engine Optimization
- AEO
- AI Search
- Generative Engine Optimization
- Marketing
- Analytics
- Agent Analytics
- Brand Visibility
- Citations
- MCP
- A2A
website: https://www.tryprofound.com
---
