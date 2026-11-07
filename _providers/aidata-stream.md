---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AI Data Stream provides a platform to interact via API for analytics data, AI chat and reports. Documentation is at https://aidata.stream/docs/.
  name: AI Data Stream API
  slug: ai-data-stream-api
- description: 'aidata-stream API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: aidata-stream API
  slug: aidata-stream-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/aidata-stream/plans/aidata-stream-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aidata-stream-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aidata-stream/rules/aidata-stream-rules.yml
  title: ''
  type: Spectral
  url: rules/aidata-stream-rules.yml
- group: design
  href: https://artifacts.apis.io/aidata-stream/vocabulary/aidata-stream-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aidata-stream-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/aidata-stream/changelog/aidata-stream-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aidata-stream-changelog.yml
- group: design
  href: https://artifacts.apis.io/aidata-stream/conformance/aidata-stream-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aidata-stream-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aidata-stream/llms/aidata-stream-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidata-stream-llms.txt
- group: agent
  href: https://artifacts.apis.io/aidata-stream/mcp/aidata-stream-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aidata-stream-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aidata-stream/well-known/aidata-stream-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aidata-stream-well-known.yml
- group: other
  href: https://artifacts.apis.io/aidata-stream/hosts/aidata-stream-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aidata-stream-hosts.yml
- group: other
  href: https://artifacts.apis.io/aidata-stream/vendors/aidata-stream-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aidata-stream-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.aidata.stream/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://aidata.stream/changelog/
- group: auth
  href: https://artifacts.apis.io/aidata-stream/security/aidata-stream-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidata-stream-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aidata.stream/
- group: docs
  title: ''
  type: Documentation
  url: https://aidata.stream/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://aidata.stream/docs/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://aidata.stream/pricing/
- group: company
  title: ''
  type: Blog
  url: https://aidata.stream/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aidata.stream/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aidata.stream/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aidata.stream/contact/
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://aidata.stream/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: AI Data Stream provides an AI-powered platform that explains analytics, advertising, and SEO data in plain English. Users can connect their analytics sources, ask natural language questions, and receive detailed explanations of traffic changes, content gaps, and performance metrics. The service offers a free 30‑day trial, supports custom AI keys with zero markup, and includes features like AI chat, annotations, and multi‑language support, aiming to make data-driven decisions accessible to marketers and analysts alike.
image: https://aidata.stream/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at aidata.stream.
  name: aidata-stream MCP Server
  slug: aidata-stream-mcp-yml
modified: '2026-10-29'
name: aidata-stream
nav: Providers
network: true
overview: 'aidata-stream is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, SEO, Marketing, and Data.


  The aidata-stream catalog on APIs.io includes 1 Spectral governance ruleset.


  aidata-stream''s developer surface includes changelog, documentation, getting-started guide, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Aidata Stream Plans Pricing
  plan_count: 4
  slug: aidata-stream-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: aidata-stream API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: aidata-stream-rules
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 14.3
    discoverability: 66.7
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aidata-stream/aidata-stream-2026-11-03T120452.png
security:
- kind: domain-security
  name: Aidata Stream Domain Security
  slug: aidata-stream-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aidata-stream
tags:
- Artificial Intelligence
- Analytics
- SEO
- Marketing
- Data
website: https://aidata.stream/
---
