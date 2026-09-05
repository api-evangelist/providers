---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Alphasense Agentic Access
  operation_count: 5
  slug: alphasense-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 2
apis:
- description: Time-series operations for theme, keyword, and topic frequency across the document corpus - the back end behind AlphaSense's Trend visualisations and competitive-intelligence dashboards.
  name: AlphaSense Trends API
  slug: trends-api
- description: User and account management operations covering profile, preferences, session, and entitlement metadata for integrating the AlphaSense experience into a host application or single-sign-on flow.
  name: AlphaSense User API
  slug: user-api
- description: Bulk export and download operations for documents, search results, and report PDFs - used to push AlphaSense content into downstream data warehouses, vaults, and BI tools.
  name: AlphaSense Download / Export API
  slug: download-api
- description: Model Context Protocol surface that lets MCP-aware AI clients (Claude, Cursor, ChatGPT-style desktop hosts, in-house agent frameworks) call GenSearch, ThinkLonger, and Deep Research as tools without w
  name: AlphaSense MCP Server
  slug: mcp-server
- description: Go-based CLI (AlphaSense-Engineering/privatecloud-cli, Apache-2.0-ish "Other" license) used by Enterprise Intelligence Private Cloud customers to bootstrap and validate the Kubernetes cluster that hos
  name: AlphaSense Private Cloud CLI
  slug: privatecloud-cli
- baseURL: https://api.alpha-sense.com
  baseurl_source: declared
  description: OAuth 2.0 token exchange for the AlphaSense platform.
  name: AlphaSense Authentication API
  slug: alphasense-authentication-api
- baseURL: https://api.alpha-sense.com
  baseurl_source: declared
  description: Generative-search mutations and conversation polling for AlphaSense GenSearch.
  name: AlphaSense GenSearch API
  slug: alphasense-gensearch-api
- baseURL: https://api.alpha-sense.com
  baseurl_source: declared
  description: Push customer-owned content into Enterprise Intelligence.
  name: AlphaSense Ingestion API
  slug: alphasense-ingestion-api
- baseURL: https://api.alpha-sense.com
  baseurl_source: declared
  description: Document search across the AlphaSense corpus (500M+ documents).
  name: AlphaSense Search API
  slug: alphasense-search-api
artifact_total: 109
collections:
- collection_type: postman
  name: AlphaSense Agent Authentication API
  slug: postman-alphasense-authentication-api
- collection_type: postman
  name: AlphaSense Agent Authentication Brokers API
  slug: postman-alphasense-brokers-api
- collection_type: postman
  name: AlphaSense Agent Authentication Companies API
  slug: postman-alphasense-companies-api
- collection_type: postman
  name: AlphaSense Agent Authentication Deep Research API
  slug: postman-alphasense-deep-research-api
- collection_type: postman
  name: AlphaSense Agent Authentication Document Search API
  slug: postman-alphasense-document-search-api
- collection_type: postman
  name: AlphaSense Agent Authentication Download API
  slug: postman-alphasense-download-api
- collection_type: postman
  name: AlphaSense Agent Authentication GenSearch API
  slug: postman-alphasense-gensearch-api
- collection_type: postman
  name: AlphaSense Agent Authentication Ingestion API
  slug: postman-alphasense-ingestion-api
- collection_type: postman
  name: AlphaSense Agent Authentication Search API
  slug: postman-alphasense-search-api
- collection_type: postman
  name: AlphaSense Agent Authentication Trends API
  slug: postman-alphasense-trends-api
- collection_type: postman
  name: AlphaSense Agent Authentication User API
  slug: postman-alphasense-user-api
- collection_type: postman
  name: AlphaSense Agent Authentication Watchlist API
  slug: postman-alphasense-watchlist-api
- collection_type: postman
  name: AlphaSense Agent Authentication Workflow Agents API
  slug: postman-alphasense-workflow-agents-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AlphaSense Agent API
  slug: open-alphasense-agent-api
- collection_type: open
  name: AlphaSense Agent Authentication API
  slug: open-alphasense-authentication-api
- collection_type: open
  name: AlphaSense Agent Authentication Brokers API
  slug: open-alphasense-brokers-api
- collection_type: open
  name: AlphaSense Agent Authentication Companies API
  slug: open-alphasense-companies-api
- collection_type: open
  name: AlphaSense Agent Authentication Deep Research API
  slug: open-alphasense-deep-research-api
- collection_type: open
  name: AlphaSense Agent Authentication Document Search API
  slug: open-alphasense-document-search-api
- collection_type: open
  name: AlphaSense Agent Authentication Download API
  slug: open-alphasense-download-api
- collection_type: open
  name: AlphaSense Agent Authentication GenSearch API
  slug: open-alphasense-gensearch-api
- collection_type: open
  name: AlphaSense Agent Authentication Ingestion API
  slug: open-alphasense-ingestion-api
- collection_type: open
  name: AlphaSense Agent Authentication Search API
  slug: open-alphasense-search-api
- collection_type: open
  name: AlphaSense Agent Authentication Trends API
  slug: open-alphasense-trends-api
- collection_type: open
  name: AlphaSense Agent Authentication User API
  slug: open-alphasense-user-api
- collection_type: open
  name: AlphaSense Utility APIs
  slug: open-alphasense-utility-api
- collection_type: open
  name: AlphaSense Agent Authentication Watchlist API
  slug: open-alphasense-watchlist-api
- collection_type: open
  name: AlphaSense Agent Authentication Workflow Agents API
  slug: open-alphasense-workflow-agents-api
common:
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/AlphaSense-Engineering/privatecloud-cli/blob/main/CONTRIBUTING.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/alphasense/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alphasense-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/alphasense-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alphasense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alphasense-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.alpha-sense.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.alpha-sense.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.alpha-sense.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.alpha-sense.com/api/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.alpha-sense.com/agent-api/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://developer.alpha-sense.com/api/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlphaSense-Engineering
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.alpha-sense.com/
- group: operate
  title: ''
  type: Support
  url: https://help.alpha-sense.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alphasense
- group: commercial
  title: ''
  type: Plans
  url: plans/alphasense-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alphasense-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alphasense-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/alphasense-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/alphasense-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/alphasense-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.alpha-sense.com/llms.txt
created: '2026-05-23'
description: 'AlphaSense is an AI-powered market intelligence and search platform used by hedge funds, banks, corporates, consulting firms, and law firms to accelerate research and decision-making. The platform unifies 500M+ public and private documents - SEC filings, broker research from 1,500+ firms, news, earnings call transcripts, internal company content, and 260,000+ Tegus expert call transcripts (Tegus was acquired in December 2023 for ~$930M) - behind a generative search and agent layer (GenSearch, Deep Research, Workflow Agents). The developer surface is gated, enterprise-only, and is split across two contracts: an Agent API for embedding GenSearch / Deep Research / MCP tools into customer AI agents, and a set of Utility APIs (Search, Brokers, Companies, Watchlist, Trends, User, Download, Ingestion) for direct programmatic access. Both are exposed over a single OAuth 2.0-protected GraphQL endpoint at https://api.alpha-sense.com/gql, with a companion REST Ingestion API for Enterprise
  Intelligence customers. AlphaSense Enterprise Intelligence Private Cloud ships with a public Go CLI (AlphaSense-Engineering/privatecloud-cli) for installing and validating the Kubernetes-hosted environment in a customer''s own VPC.'
examples:
- key_count: 4
  name: Alphasense Auth Token Example
  slug: alphasense-auth-token-example
- key_count: 4
  name: Alphasense Broker Example
  slug: alphasense-broker-example
- key_count: 5
  name: Alphasense Citation Example
  slug: alphasense-citation-example
- key_count: 7
  name: Alphasense Company Example
  slug: alphasense-company-example
- key_count: 6
  name: Alphasense Document Example
  slug: alphasense-document-example
- key_count: 5
  name: Alphasense Gensearch Conversation Example
  slug: alphasense-gensearch-conversation-example
- key_count: 4
  name: Alphasense Ingestion Job Example
  slug: alphasense-ingestion-job-example
- key_count: 6
  name: Alphasense Tegus Document Example
  slug: alphasense-tegus-document-example
- key_count: 3
  name: Alphasense Watchlist Example
  slug: alphasense-watchlist-example
- key_count: 5
  name: Alphasense Workflow Agent Example
  slug: alphasense-workflow-agent-example
features:
- description: Multi-agent search-and-answer layer over 500M+ documents with auto, fast, ThinkLonger, and Deep Research reasoning modes.
  name: Generative Search (GenSearch)
- description: Long-horizon agent that decomposes a research question, plans steps, searches across filings / transcripts / broker research / Tegus expert calls, and returns a markdown report with inline citations.
  name: Deep Research
- description: Pre-built and custom agents addressable by ID for repeatable research tasks (earnings prep, competitor scan, KOL mapping, etc.).
  name: Workflow Agents
- description: 260,000+ private expert-call transcripts, on-demand expert interviews, and the Tegus expert network - integrated into search and Deep Research after the December 2023 acquisition.
  name: Tegus Expert Insights
- description: Search the same generative layer over a customer's internal documents (decks, CRM, notes) alongside the external AlphaSense corpus.
  name: Enterprise Intelligence
- description: Customer-hosted Kubernetes deployment for regulated buyers; managed via the public privatecloud-cli.
  name: Enterprise Intelligence Private Cloud
- description: Structured financial datasets, 4,000+ pre-built financial models, and analyst-grade fundamentals integrated with the search layer.
  name: Financial Data
- description: Domain-tuned query expansion that maps tickers, business jargon, and industry terms to the right document language.
  name: Smart Synonyms
- description: Every GenSearch / Deep Research answer ships with traceable citations back to the underlying document, page, and span.
  name: Inline Citations
finops:
- name: Alphasense Finops
  service_category: Market Intelligence
  slug: alphasense-finops
graphqls:
- description: GraphQL surface for embedding AlphaSense intelligence into customer AI agents. Wraps GenSearch (auto / fast / thinkLonger / deepResearch modes), Workflow Agents (pre-built and custom), and the Documen
  name: AlphaSense GraphQL API
  slug: alphasense-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alphasense.png
integrations:
- description: Push and query AlphaSense-derived content alongside the customer's warehouse via Enterprise Intelligence ingestion + export.
  name: Snowflake
- description: Pull internal documents from SharePoint and Microsoft 365 into Enterprise Intelligence for unified search.
  name: Microsoft 365 / SharePoint
- description: Native integration with Tegus's expert-call transcript library and on-demand expert services (post-acquisition).
  name: Tegus Expert Network
- description: SEC filing search and analytics (acquired) folded into the unified search index.
  name: BamSEC
- description: Pre-built financial models and equity datasets (acquired) used in financial analysis.
  name: Canalyst
- description: Document search and financial workflow (acquired) consolidated into the AlphaSense platform.
  name: Sentieo
- description: 2025 partnership accelerating inference for AlphaSense's generative-AI layer.
  name: Cerebras Systems
- description: Any MCP-aware host (Claude, Cursor, in-house agent frameworks) can call GenSearch / ThinkLonger / Deep Research as tools.
  name: Model Context Protocol (MCP) Clients
- description: Customer-managed Kubernetes (EKS / GKE / AKS) provisioned via the privatecloud-cli for regulated and air-gapped buyers.
  name: Kubernetes (Private Cloud)
json_schemas:
- name: Broker
  property_count: 4
  slug: alphasense-broker
- name: Citation
  property_count: 5
  slug: alphasense-citation
- name: Company
  property_count: 7
  slug: alphasense-company
- name: Document
  property_count: 6
  slug: alphasense-document
- name: GenSearchConversation
  property_count: 5
  slug: alphasense-gensearch-conversation
- name: IngestionJob
  property_count: 4
  slug: alphasense-ingestion-job
- name: Watchlist
  property_count: 3
  slug: alphasense-watchlist
- name: WorkflowAgent
  property_count: 5
  slug: alphasense-workflow-agent
json_structures:
- name: Alphasense Broker Structure
  property_count: 4
  slug: alphasense-broker-structure
- name: Alphasense Citation Structure
  property_count: 5
  slug: alphasense-citation-structure
- name: Alphasense Company Structure
  property_count: 7
  slug: alphasense-company-structure
- name: Alphasense Document Structure
  property_count: 6
  slug: alphasense-document-structure
- name: Alphasense Gensearch Conversation Structure
  property_count: 5
  slug: alphasense-gensearch-conversation-structure
- name: Alphasense Ingestion Job Structure
  property_count: 4
  slug: alphasense-ingestion-job-structure
- name: Alphasense Watchlist Structure
  property_count: 3
  slug: alphasense-watchlist-structure
- name: Alphasense Workflow Agent Structure
  property_count: 5
  slug: alphasense-workflow-agent-structure
jsonld:
- class_count: 0
  name: Alphasense Context
  property_count: 8
  slug: alphasense-context
layout: provider
modified: '2026-05-23'
name: AlphaSense
nav: Providers
network: true
overview: 'AlphaSense publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, GenSearch API, Ingestion API, and 1 more. Tagged areas include Market Intelligence, Financial Research, Search, Generative AI, and AI Agents.


  The AlphaSense catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AlphaSense''s developer surface includes authentication, documentation, getting-started guide, support, and 19 more developer resources.'
plans:
- name: Alphasense Plans Pricing
  plan_count: 6
  slug: alphasense-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Alphasense Rate Limits
  slug: alphasense-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AlphaSense API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: alphasense-jsonschema-spectral-rules
- effective_rule_count: 17
  extends: []
  name: AlphaSense API Rules
  rule_count: 17
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 8
  slug: alphasense-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 87.3
    catalog_earned_first_party: 0.0
    catalog_gap: 27.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 25.0
    contract_quality: 70.7
    developer_ergonomics: 48.8
    discoverability: 75.9
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alphasense/refs/heads/main/screenshots/alphasense-2026-06-20T171557.png
security:
- kind: authentication
  name: Alphasense Authentication
  slug: alphasense-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Alphasense Domain Security
  slug: alphasense-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Alphasense Trust Center
  slug: alphasense-trust-center
  summary_line: SOC 2, ISO 27001
slug: alphasense
solutions:
- description: Core SaaS search and intelligence product for the full customer base.
  name: AlphaSense Platform
- description: Search + GenSearch across both AlphaSense's external corpus and the customer's internal documents.
  name: Enterprise Intelligence
- description: Same product, deployed into the customer's own Kubernetes cluster for compliance-bound buyers.
  name: Enterprise Intelligence Private Cloud
- description: Expert-call transcript library and on-demand expert services from the Tegus side of the business.
  name: Tegus Expert Insights
- description: Concierge sourcing and scheduling of one-off expert interviews on behalf of the customer.
  name: Tegus Expert Call Services
- description: GenSearch + Deep Research + Workflow Agents bundle aimed at AI-led research workflows.
  name: Generative Search Suite
- description: Embedding contract for customers building their own agents on top of the AlphaSense corpus.
  name: Agent API + MCP
tags:
- Market Intelligence
- Financial Research
- Search
- Generative AI
- AI Agents
- Expert Calls
- Document Intelligence
- Enterprise Intelligence
- MCP
- GraphQL
use_cases:
- description: Pitch prep, comparables analysis, M&A target screening, and earnings-call review for bankers.
  name: Sell-Side Investment Banking
- description: Idea generation, thesis monitoring, and competitive tracking across public filings, broker research, and Tegus expert calls.
  name: Hedge Fund Research
- description: Industry primers, KOL identification, and management-quality assessment via expert interviews.
  name: Private Equity Diligence
- description: Coverage scaling for analysts who must monitor a long tail of names and themes.
  name: Asset Management
- description: Market sizing, founder background, and category-comp scans for early-stage diligence.
  name: Venture Capital
- description: Competitor surveillance, market-trend tracking, and board-pack preparation for in-house strategy teams.
  name: Corporate Strategy & CI
- description: Engagement primers, hypothesis testing, and expert sourcing across McKinsey-style project workflows.
  name: Consulting Engagements
- description: Litigation research, regulatory landscape mapping, and matter intelligence.
  name: Law Firm Research
- description: Programmatic GenSearch / Deep Research calls from customer-built agents over the Agent API or MCP server.
  name: Agentic Research Automation
website: https://www.alpha-sense.com/
---
