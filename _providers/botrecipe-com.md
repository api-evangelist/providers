---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Botrecipe Com Agentic Access
  operation_count: 17
  slug: botrecipe-com-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 2
apis:
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Agent Auth API from botrecipe-com — 1 operation(s) for agent auth.
  name: botrecipe-com Agent Auth API
  slug: botrecipe-com-agent-auth-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Board API from botrecipe-com — 1 operation(s) for board.
  name: botrecipe-com Board API
  slug: botrecipe-com-board-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Comment API from botrecipe-com — 1 operation(s) for comment.
  name: botrecipe-com Comment API
  slug: botrecipe-com-comment-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Comments API from botrecipe-com — 1 operation(s) for comments.
  name: botrecipe-com Comments API
  slug: botrecipe-com-comments-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Feedback API from botrecipe-com — 1 operation(s) for feedback.
  name: botrecipe-com Feedback API
  slug: botrecipe-com-feedback-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Hub API from botrecipe-com — 1 operation(s) for hub.
  name: botrecipe-com Hub API
  slug: botrecipe-com-hub-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Market API from botrecipe-com — 1 operation(s) for market.
  name: botrecipe-com Market API
  slug: botrecipe-com-market-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Premium API from botrecipe-com — 1 operation(s) for premium.
  name: botrecipe-com Premium API
  slug: botrecipe-com-premium-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Pricing.json API from botrecipe-com — 1 operation(s) for pricing.json.
  name: botrecipe-com Pricing.json API
  slug: botrecipe-com-pricing-json-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Recipes.json API from botrecipe-com — 1 operation(s) for recipes.json.
  name: botrecipe-com Recipes.json API
  slug: botrecipe-com-recipes-json-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Search API from botrecipe-com — 1 operation(s) for search.
  name: botrecipe-com Search API
  slug: botrecipe-com-search-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Stats API from botrecipe-com — 1 operation(s) for stats.
  name: botrecipe-com Stats API
  slug: botrecipe-com-stats-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Submit API from botrecipe-com — 1 operation(s) for submit.
  name: botrecipe-com Submit API
  slug: botrecipe-com-submit-api
- baseURL: https://botrecipe.com
  baseurl_source: declared
  description: The Top Up API from botrecipe-com — 1 operation(s) for top up.
  name: botrecipe-com Top Up API
  slug: botrecipe-com-top-up-api
artifact_total: 23
asyncapis:
- description: ''
  name: Botrecipe Com Webhooks
  slug: botrecipe-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/botrecipe-com/agentic-access/botrecipe-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/botrecipe-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/botrecipe-com/plans/botrecipe-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botrecipe-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/botrecipe-com/rules/botrecipe-com-rules.yml
  title: ''
  type: Spectral
  url: rules/botrecipe-com-rules.yml
- group: design
  href: https://artifacts.apis.io/botrecipe-com/asyncapi/botrecipe-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/botrecipe-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/botrecipe-com/changelog/botrecipe-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/botrecipe-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/botrecipe-com/errors/botrecipe-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botrecipe-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/botrecipe-com/conformance/botrecipe-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botrecipe-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botrecipe-com/llms/botrecipe-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botrecipe-com-llms.txt
- group: build
  href: https://artifacts.apis.io/botrecipe-com/mcp/botrecipe-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/botrecipe-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/botrecipe-com/mcp/botrecipe-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/botrecipe-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/botrecipe-com/hosts/botrecipe-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botrecipe-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/botrecipe-com/vendors/botrecipe-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botrecipe-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://botrecipe.com/recipes/signup-research-card/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botrecipe.com/recipes/privacy-friendly-analytics/
- group: commercial
  title: ''
  type: Pricing
  url: https://botrecipe.com/recipes/pricing-objection-faq/
- group: start
  title: ''
  type: GettingStarted
  url: https://botrecipe.com/recipes/onboarding-drop-off-email/
- group: docs
  title: ''
  type: APIReference
  url: https://botrecipe.com/changelog/
- group: auth
  href: https://artifacts.apis.io/botrecipe-com/security/botrecipe-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botrecipe-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botrecipe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://botrecipe.com/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://botrecipe.com/topics/support/
created: '2026-10-29'
description: BotRecipe.com is a platform that enables developers and businesses to create, share, and manage chatbot recipes for various messaging services. It provides a catalog of pre-built chatbot workflows, integration guides, and API endpoints to programmatically retrieve and deploy chatbot configurations. The service aims to simplify the development of conversational agents by offering reusable components, versioning, and documentation for each recipe, supporting platforms such as Slack, Microsoft Teams, and Facebook Messenger.
image: https://botrecipe.com/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at botrecipe.com.
  name: botrecipe-com MCP Server
  slug: botrecipe-com-mcp-yml
modified: '2026-10-29'
name: botrecipe-com
nav: Providers
network: true
overview: 'botrecipe-com publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Auth API, Board API, Comment API, and 11 more. Tagged areas include Company, Bot, Chatbots, Recipes, and Automation.


  The botrecipe-com catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  botrecipe-com''s developer surface includes changelog, signup flow, pricing, getting-started guide, API reference, documentation, support, and 14 more developer resources.'
plans:
- name: Botrecipe Com Plans Pricing
  plan_count: 6
  slug: botrecipe-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: botrecipe-com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: botrecipe-com-rules
scopes:
- name: Botrecipe Com Scopes
  scope_count: 0
  slug: botrecipe-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 48.7
    contract_governance: 18.2
    contract_quality: 43.3
    developer_ergonomics: 16.7
    discoverability: 75.0
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 87.5
      derived: 2
      marker_coverage: 12.5
      total: 16
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/botrecipe-com/botrecipe-com-2026-11-03T122340.png
security:
- kind: authentication
  name: Botrecipe Com Authentication
  slug: botrecipe-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Botrecipe Com Domain Security
  slug: botrecipe-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: list-recipes
  slug: botrecipe-com-list-recipes
slug: botrecipe-com
tags:
- Company
- Bot
- Chatbots
- Recipes
- Automation
- Integration
website: https://botrecipe.com/
---
