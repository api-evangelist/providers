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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Exa Ai Agentic Access
  operation_count: 66
  slug: exa-ai-agentic-access
  summary_line: 66 operations · 36 acting · 1 human-in-the-loop
api_count: 19
apis:
- description: The Agent API from Exa — 4 operation(s) for agent.
  name: Exa Agent API
  slug: exa-ai-agent-api
- description: The Answer API from Exa — 1 operation(s) for answer.
  name: Exa Answer API
  slug: exa-ai-answer-api
- description: The Contents API from Exa — 1 operation(s) for contents.
  name: Exa Contents API
  slug: exa-ai-contents-api
- description: The Enrichments API from Exa — 3 operation(s) for enrichments.
  name: Exa Enrichments API
  slug: exa-ai-enrichments-api
- description: The Events API from Exa — 2 operation(s) for events.
  name: Exa Events API
  slug: exa-ai-events-api
- description: The Imports API from Exa — 2 operation(s) for imports.
  name: Exa Imports API
  slug: exa-ai-imports-api
- description: The Items API from Exa — 2 operation(s) for items.
  name: Exa Items API
  slug: exa-ai-items-api
- description: The Monitors API from Exa — 6 operation(s) for monitors.
  name: Exa Monitors API
  slug: exa-ai-monitors-api
- description: The Monitors Runs API from Exa — 2 operation(s) for monitors runs.
  name: Exa Monitors Runs API
  slug: exa-ai-monitors-runs-api
- description: The Research API from Exa — 2 operation(s) for research.
  name: Exa Research API
  slug: exa-ai-research-api
- description: The Runs API from Exa — 2 operation(s) for runs.
  name: Exa Runs API
  slug: exa-ai-runs-api
- description: The Search API from Exa — 1 operation(s) for search.
  name: Exa Search API
  slug: exa-ai-search-api
- description: The Searches API from Exa — 3 operation(s) for searches.
  name: Exa Searches API
  slug: exa-ai-searches-api
- description: The Team Management API from Exa — 3 operation(s) for team management.
  name: Exa Team Management API
  slug: exa-ai-team-management-api
- description: The Teams API from Exa — 1 operation(s) for teams.
  name: Exa Teams API
  slug: exa-ai-teams-api
- description: The Webhooks API from Exa — 2 operation(s) for webhooks.
  name: Exa Webhooks API
  slug: exa-ai-webhooks-api
- description: The Webhooks Attempts API from Exa — 1 operation(s) for webhooks attempts.
  name: Exa Webhooks Attempts API
  slug: exa-ai-webhooks-attempts-api
- description: The Websets API from Exa — 3 operation(s) for websets.
  name: Exa Websets API
  slug: exa-ai-websets-api
- description: The Websets Preview API from Exa — 1 operation(s) for websets preview.
  name: Exa Websets Preview API
  slug: exa-ai-websets-preview-api
arazzos:
- description: Get a cited answer to a question, then deep-fetch the top citation.
  name: Exa Answer with Deep Sources
  slug: exa-ai-answer-with-deep-sources-workflow
- description: Kick off an Exa research task and poll until it completes, then read output.
  name: Exa Create and Poll Research
  slug: exa-ai-create-and-poll-research-workflow
- description: Create a Webset from a search, poll until it settles, then list its items.
  name: Exa Create Webset and List Items
  slug: exa-ai-create-webset-and-list-items-workflow
- description: Build a Webset, then add an enrichment column and poll until it completes.
  name: Exa Enrich Webset and Poll
  slug: exa-ai-enrich-webset-and-poll-workflow
- description: Build a Webset, add a follow-up search, and poll it to completion.
  name: Exa Expand Webset Search
  slug: exa-ai-expand-webset-search-workflow
- description: Find pages similar to a seed result, then fetch their full contents.
  name: Exa Find Similar and Fetch Contents
  slug: exa-ai-find-similar-and-fetch-contents-workflow
- description: Preview how a query decomposes, then commit it to a real Webset.
  name: Exa Preview then Create Webset
  slug: exa-ai-preview-then-create-webset-workflow
- description: Find the most recent research task and poll it until it completes.
  name: Exa Resume Latest Research
  slug: exa-ai-resume-latest-research-workflow
- description: Scout sources with a quick search, then launch and poll a deep research task.
  name: Exa Scout then Research
  slug: exa-ai-scout-then-research-workflow
- description: Run an Exa neural search and pull full page contents for the top result.
  name: Exa Search and Fetch Contents
  slug: exa-ai-search-and-fetch-contents-workflow
- description: Build a Webset, list its items, and deep-fetch the top item's contents.
  name: Exa Webset Item Deep Contents
  slug: exa-ai-webset-item-deep-contents-workflow
artifact_total: 76
collections:
- collection_type: postman
  name: Exa Agent API
  slug: postman-exa-agent-api
- collection_type: postman
  name: Exa Monitors API
  slug: postman-exa-monitors-api
- collection_type: postman
  name: Exa Research API
  slug: postman-exa-research-api
- collection_type: postman
  name: Exa Search API
  slug: postman-exa-search-api
- collection_type: postman
  name: Exa Team API
  slug: postman-exa-team-api
- collection_type: postman
  name: Team Management API
  slug: postman-exa-team-management-api
- collection_type: postman
  name: Exa Websets API
  slug: postman-exa-websets-api
- collection_type: open
  name: Exa Agent API
  slug: open-exa-agent-api
- collection_type: open
  name: Exa Monitors API
  slug: open-exa-monitors-api
- collection_type: open
  name: Exa Research API
  slug: open-exa-research-api
- collection_type: open
  name: Exa Search API
  slug: open-exa-search-api
- collection_type: open
  name: Exa Team API
  slug: open-exa-team-api
- collection_type: open
  name: Team Management API
  slug: open-exa-team-management-api
- collection_type: open
  name: Exa Websets API
  slug: open-exa-websets-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exa-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/exa-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exa-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exa-ai-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/exa-ai-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/exa-ai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/exa-ai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/exa-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exa-ai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/exa-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/exa-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exa-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/exa-ai-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/exa-ai-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/exa-ai-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/exa-ai-search-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/exa-ai-research-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/exa-ai-monitors-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/exa-ai-agent-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/exa-ai-websets-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/exa-ai-team-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/exa-ai-team-management-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/exa/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-answer-with-deep-sources-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-create-and-poll-research-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-create-webset-and-list-items-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-enrich-webset-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-expand-webset-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-find-similar-and-fetch-contents-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-preview-then-create-webset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-resume-latest-research-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-scout-then-research-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-search-and-fetch-contents-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exa-ai-webset-item-deep-contents-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://exa.ai
- group: docs
  title: ''
  type: Documentation
  url: https://exa.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://exa.ai/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://exa.ai/docs/reference/search-api-guide
- group: start
  title: ''
  type: Signup
  url: https://dashboard.exa.ai
- group: start
  title: ''
  type: Sandbox
  url: https://dashboard.exa.ai/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://exa.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://exa.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://exa.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.exa.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exa.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exa.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://exa.ai/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exa-ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exa-labs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/exa-labs/exa-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/exa-labs/exa-js
- group: build
  title: ''
  type: Tools
  url: https://github.com/exa-labs/exa-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/exa-labs/websets-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/exa-labs/zed-exa-mcp-extension
- group: build
  title: ''
  type: Tools
  url: https://github.com/exa-labs/exa-for-sheets
- group: build
  title: ''
  type: Tools
  url: https://github.com/exa-labs/n8n-integration
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/exa-labs/exa-hallucination-detector
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/exa-labs/company-researcher
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/exa-labs/exa-deepseek-chat
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/exa-labs/exa-o3mini-chat
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/exa-labs/answer-chat-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/exa-labs/jfk-files-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/exa-labs/research-paper-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/exa-labs/websets-news-monitor
- group: auth
  title: ''
  type: Authentication
  url: https://exa.ai/docs/getting-started/authentication
- group: docs
  title: ''
  type: OpenAPI
  url: https://exa.ai/docs/exa-spec.json
- group: docs
  title: ''
  type: OpenAPI
  url: https://exa.ai/docs/team-management-spec.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/exa-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/exa-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/exa-ai-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Exa is a web search API and AI research platform built specifically for LLMs and agents — semantic and keyword search across the open web with token-efficient highlights, structured outputs, sub-200ms latency tiers, and verticals for code, companies, news, people, research, and financials. The platform pairs the core Search, Contents, and Answer endpoints with Research (asynchronous deep research), Agent (managed multi-step agents at four effort modes), Monitors (scheduled searches with webhooks), and Websets (curated, enrichable result collections). Customers include Cognition (Devin), HubSpot, Monday, Databricks, AWS, and Cursor; Exa raised a $250M Series C to build the search engine for AIs. Open SDKs in Python and JavaScript, an MCP server, Google Sheets and n8n integrations, and a free tier of 1,000 requests/month round out the surface.
features:
- Neural and keyword web search built specifically for LLMs and agents
- Token-efficient highlights — claimed ~90% reduction in LLM context cost vs full page text
- Latency tiers — fast (~180ms), auto (~1s), deep (~10s)
- Verticals — Code, Companies, News, People, Research, Financials
- Structured outputs with web-grounded citations
- Contents API for full-page text, summaries, highlights, and subpages
- Answer endpoint — LLM-grounded answers with sources, streaming optional
- Research API — asynchronous deep-research tasks
- Agent API — managed research agents with low/medium/high/x-high effort modes
- Monitors API — scheduled searches with webhook notifications
- Websets — curated, enrichable result collections with imports and webhooks
- Webhooks for Webset events, enrichments, monitor runs, and agent runs
- Team Management API with per-key rate limits, budgets, and usage reporting
- Official SDKs in Python (exa-py) and JavaScript / TypeScript (exa-js)
- Exa MCP server and Websets MCP server for agent tool integration
- n8n node, Google Sheets extension, Zed editor extension
- Free tier — 1,000 requests/month
- Pay-as-you-go from $7 per 1,000 search requests; $1 per 1,000 content pages
- $1,000 startup/education grant program
finops:
- name: Exa Ai Finops
  service_category: AI and Machine Learning
  slug: exa-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exa-ai.png
json_schemas:
- name: Exa Search Result
  property_count: 13
  slug: exa-search-result
- name: Exa Webset Item
  property_count: 9
  slug: exa-webset-item
jsonld:
- class_count: 0
  name: Exa Ai Context
  property_count: 12
  slug: exa-ai-context
layout: provider
mcp_servers:
- description: ''
  name: exa-ai-mcp.yml
  slug: exa-ai-mcpyml
modified: '2026-06-20'
name: Exa
nav: Providers
network: true
overview: 'Exa publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Answer API, Contents API, and 16 more. Tagged areas include AI, Search, Web Search, Neural Search, and LLM.


  The Exa catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Exa''s developer surface includes authentication, changelog, developer portal, documentation, getting-started guide, signup flow, sandbox, and 63 more developer resources.'
plans:
- name: Exa Ai Plans Pricing
  plan_count: 8
  slug: exa-ai-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 6
  name: Exa Ai Rate Limits
  slug: exa-ai-rate-limits
rules:
- name: Exa API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: exa-ai-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 76.9
  delta: 2.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 72.5
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 69.8
    operational_transparency: 68.4
  previous_composite: 74.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exa-ai/refs/heads/main/screenshots/exa-ai-2026-06-20T180928.png
security:
- kind: authentication
  name: Exa Ai Authentication
  slug: exa-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Exa Ai Domain Security
  slug: exa-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Exa Ai Vulnerability Disclosure
  slug: exa-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Exa Ai Trust Center
  slug: exa-ai-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR
slug: exa-ai
tags:
- AI
- Search
- Web Search
- Neural Search
- LLM
- Agents
- Research
- Websets
website: https://exa.ai
---
