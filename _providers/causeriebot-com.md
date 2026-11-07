---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Causeriebot Com Agentic Access
  operation_count: 4
  slug: causeriebot-com-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://dashboard.causeriebot.com/api/public
  baseurl_source: declared
  description: The Chatbots API from Causerie — 1 operation(s) for chatbots.
  name: Causerie Chatbots API
  slug: causeriebot-com-chatbots-api
- baseURL: https://dashboard.causeriebot.com/api/public
  baseurl_source: declared
  description: Conversations between visitors and the chatbots. Pro and Business plans.
  name: Causerie Conversations API
  slug: causeriebot-com-conversations-api
- baseURL: https://dashboard.causeriebot.com/api/public
  baseurl_source: declared
  description: Contacts collected by the chatbots. Pro and Business plans.
  name: Causerie Leads API
  slug: causeriebot-com-leads-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/causeriebot-com/agentic-access/causeriebot-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/causeriebot-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/causeriebot-com/plans/causeriebot-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/causeriebot-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/causeriebot-com/rules/causeriebot-com-rules.yml
  title: ''
  type: Spectral
  url: rules/causeriebot-com-rules.yml
- group: design
  href: https://artifacts.apis.io/causeriebot-com/json-ld/causeriebot-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/causeriebot-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/causeriebot-com/vocabulary/causeriebot-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/causeriebot-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/causeriebot-com/data-model/causeriebot-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/causeriebot-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/causeriebot-com/authentication/causeriebot-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/causeriebot-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/causeriebot-com/errors/causeriebot-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/causeriebot-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/causeriebot-com/conformance/causeriebot-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/causeriebot-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/causeriebot-com/llms/causeriebot-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/causeriebot-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/causeriebot-com/mcp/causeriebot-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/causeriebot-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/causeriebot-com/well-known/causeriebot-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/causeriebot-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/causeriebot-com/hosts/causeriebot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/causeriebot-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dashboard.causeriebot.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dashboard.causeriebot.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://causeriebot.com/en/pricing/
- group: start
  title: ''
  type: Login
  url: https://dashboard.causeriebot.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://causeriebot.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://causeriebot.com/blog/
- group: auth
  href: https://artifacts.apis.io/causeriebot-com/security/causeriebot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/causeriebot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://causeriebot.com/
created: '2026-11-04'
description: Causerie is a French AI-powered chatbot platform that integrates with websites, PDFs and other content to provide 24/7 customer support, lead qualification and sales assistance. It offers native RAG, nine AI models, European hosting, and a free tier for businesses seeking automated conversational experiences.
image: https://causeriebot.com/opengraph-image?740280cf6b043a1e
json_schemas:
- name: Chatbot
  property_count: 7
  slug: causeriebot-com-chatbot
- name: ConversationPage
  property_count: 2
  slug: causeriebot-com-conversation-page
- name: Conversation
  property_count: 9
  slug: causeriebot-com-conversation
- name: LeadPage
  property_count: 2
  slug: causeriebot-com-lead-page
jsonld:
- class_count: 10
  name: Causeriebot Com Context
  property_count: 30
  slug: causeriebot-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at chat.causeriebot.com.
  name: Causerie MCP Server
  slug: causeriebot-com-mcp-yml
modified: '2026-11-04'
name: Causerie
nav: Providers
network: true
overview: 'Causerie publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Chatbots API, Conversations API, and Leads API. Tagged areas include Artificial Intelligence, Chatbots, Customer Service, Lead Qualification, and French.


  The Causerie catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Causerie''s developer surface includes authentication, pricing, documentation, engineering blog, and 17 more developer resources.'
plans:
- name: Causeriebot Com Plans Pricing
  plan_count: 4
  slug: causeriebot-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Causerie API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: causeriebot-com-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 68.1
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Causeriebot Com Authentication
  slug: causeriebot-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Causeriebot Com Domain Security
  slug: causeriebot-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: causeriebot-com
tags:
- Artificial Intelligence
- Chatbots
- Customer Service
- Lead Qualification
- French
website: https://causeriebot.com/
---
