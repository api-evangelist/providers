---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Defoorreport Com Agentic Access
  operation_count: 1
  slug: defoorreport-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: 'Remote Streamable HTTP MCP server at https://mcp.defoorreport.com/mcp with OAuth sign-in (scope news) using the reader''s DeFoor Report email. Documented tools: top_news, news_by_section, search_news, '
  name: DeFoor Report MCP Server
  slug: defoorreport-com-mcp-server
- baseURL: https://argolabs.us
  baseurl_source: declared
  description: The News API from DeFoor Report — 1 operation(s) for news.
  name: DeFoor Report News API
  slug: defoorreport-com-news-api
artifact_total: 12
common:
- group: build
  href: https://artifacts.apis.io/defoorreport-com/integrations/defoorreport-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/defoorreport-com-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/defoorreport-com/agentic-access/defoorreport-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/defoorreport-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/defoorreport-com/rate-limits/defoorreport-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/defoorreport-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/defoorreport-com/plans/defoorreport-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/defoorreport-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/defoorreport-com/rules/defoorreport-com-rules.yml
  title: ''
  type: Spectral
  url: rules/defoorreport-com-rules.yml
- group: design
  href: https://artifacts.apis.io/defoorreport-com/json-ld/defoorreport-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/defoorreport-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/defoorreport-com/vocabulary/defoorreport-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/defoorreport-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/defoorreport-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/defoorreport-com/data-model/defoorreport-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/defoorreport-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/defoorreport-com/conventions/defoorreport-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/defoorreport-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/defoorreport-com/errors/defoorreport-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/defoorreport-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/defoorreport-com/conformance/defoorreport-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/defoorreport-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/defoorreport-com/overlays/defoorreport-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/defoorreport-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/defoorreport-com/llms/defoorreport-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defoorreport-com-llms.txt
- group: build
  href: https://artifacts.apis.io/defoorreport-com/mcp/defoorreport-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/defoorreport-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/defoorreport-com/mcp/defoorreport-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/defoorreport-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/defoorreport-com/well-known/defoorreport-com-bsky-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/defoorreport-com-bsky-security.txt
- group: agent
  href: https://artifacts.apis.io/defoorreport-com/well-known/defoorreport-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/defoorreport-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/defoorreport-com/hosts/defoorreport-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/defoorreport-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/defoorreport-com/vendors/defoorreport-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/defoorreport-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://defoorreport.com/ai-directory/security
- group: company
  title: ''
  type: Newsroom
  url: https://defoorreport.com/ai-directory/media
- group: auth
  href: https://artifacts.apis.io/defoorreport-com/authentication/defoorreport-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/defoorreport-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/defoorreport-com/security/defoorreport-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defoorreport-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://defoorreport.com/
- group: company
  title: ''
  type: About
  url: https://defoorreport.com/about
- group: agent
  title: ''
  type: LLMsTxt
  url: https://defoorreport.com/llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://defoorreport.com/subscribe
- group: operate
  title: ''
  type: Support
  url: https://defoorreport.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://defoorreport.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://defoorreport.com/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/defoorreport
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/defoorreport.bsky.social
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@defoorreport
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/defoorreport/
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@defoorreport
created: '2026-11-05'
description: The DeFoor Report is an hourly, ranked AI and large-language-model news front page published by DeFoor Innovations (edited by Nathan DeFoor, based in Georgia, USA). It aggregates headlines on AI labs, the LLM race, agents, robotics, AI jobs, funding, policy, health, security breaches and crypto, linking each story to its original publisher, and runs an AI startup directory. Its llms.txt advertises a key-authenticated news index API (GET https://argolabs.us/v1/news) with an OpenAPI description, and a remote Streamable HTTP MCP server at mcp.defoorreport.com with OAuth sign-in and tools such as top_news, search_news and save_story.
image: https://defoorreport.com/og/defoor-report.png
json_schemas:
- name: Story
  property_count: 6
  slug: defoorreport-com-story
jsonld:
- class_count: 1
  name: Defoorreport Com Context
  property_count: 6
  slug: defoorreport-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.defoorreport.com over streamable HTTP requiring OAuth; 9 tools listed.
  name: DeFoor Report MCP Server
  slug: defoor-report-mcp-server
modified: '2026-11-05'
name: DeFoor Report
nav: Providers
network: true
overview: 'DeFoor Report publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including News API, and 1 more. Tagged areas include Company, News, Artificial Intelligence, Media, and News Aggregation.


  The DeFoor Report catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeFoor Report''s developer surface includes authentication, signup flow, support, YouTube channel, and 32 more developer resources.'
plans:
- name: Defoorreport Com Plans Pricing
  plan_count: 1
  slug: defoorreport-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Defoorreport Com Rate Limits
  slug: defoorreport-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: DeFoor Report API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: defoorreport-com-rules
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 69.2
    catalog_earned_first_party: 16.0
    catalog_gap: 45.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 56.1
    developer_ergonomics: 18.5
    discoverability: 73.3
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Defoorreport Com Authentication
  slug: defoorreport-com-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Defoorreport Com Domain Security
  slug: defoorreport-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: defoorreport-get-ai-news
  slug: defoorreport-com-get-ai-news
slug: defoorreport-com
tags:
- Company
- News
- Artificial Intelligence
- Media
- News Aggregation
- MCP
- LLM
website: https://defoorreport.com/
---
