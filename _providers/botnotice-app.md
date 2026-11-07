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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Botnotice App Agentic Access
  operation_count: 10
  slug: botnotice-app-agentic-access
  summary_line: 10 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://botnotice.app
  baseurl_source: declared
  description: 'Consent to AI phone calls: record, check before dialing, revoke. Token: the site''s voice token (bni_…).'
  name: BotNotice Consent API
  slug: botnotice-app-consent-api
- baseURL: https://botnotice.app
  baseurl_source: declared
  description: 'Register AI-generated media as it is created or uploaded. Token: the site''s content-register token.'
  name: BotNotice Content register API
  slug: botnotice-app-content-register-api
- baseURL: https://botnotice.app
  baseurl_source: declared
  description: No key needed.
  name: BotNotice Free tools API
  slug: botnotice-app-free-tools-api
- baseURL: https://botnotice.app
  baseurl_source: declared
  description: Open data, CC BY 4.0. https://botnotice.app/datasets/ai-disclosure-laws
  name: BotNotice Law dataset API
  slug: botnotice-app-law-dataset-api
- baseURL: https://botnotice.app
  baseurl_source: declared
  description: 'What an AI call must open with, and the receipt per call. Token: the site''s voice token (bni_…).'
  name: BotNotice Voice API
  slug: botnotice-app-voice-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/botnotice-app/agentic-access/botnotice-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/botnotice-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/botnotice-app/plans/botnotice-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botnotice-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/botnotice-app/rules/botnotice-app-rules.yml
  title: ''
  type: Spectral
  url: rules/botnotice-app-rules.yml
- group: design
  href: https://artifacts.apis.io/botnotice-app/json-ld/botnotice-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/botnotice-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/botnotice-app/vocabulary/botnotice-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/botnotice-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/botnotice-app/data-model/botnotice-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botnotice-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/botnotice-app/errors/botnotice-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botnotice-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/botnotice-app/conformance/botnotice-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botnotice-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botnotice-app/llms/botnotice-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botnotice-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/botnotice-app/mcp/botnotice-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/botnotice-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/botnotice-app/well-known/botnotice-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botnotice-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/botnotice-app/hosts/botnotice-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botnotice-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/botnotice-app/vendors/botnotice-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botnotice-app-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://botnotice.app/support
- group: start
  title: ''
  type: GettingStarted
  url: https://botnotice.app/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://botnotice.app/docs
- group: auth
  href: https://artifacts.apis.io/botnotice-app/authentication/botnotice-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botnotice-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/botnotice-app/security/botnotice-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botnotice-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botnotice.app/
- group: docs
  title: ''
  type: Documentation
  url: https://botnotice.app/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://botnotice.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://botnotice.app/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://botnotice.app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botnotice.app/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botnotice.app/legal/privacy
- group: other
  title: ''
  type: Disclaimer
  url: https://botnotice.app/legal/disclaimer
- group: agent
  title: ''
  type: LLMS
  url: https://botnotice.app/llms.txt
created: '2026-11-02'
description: BotNotice helps businesses comply with AI disclosure laws by adding clear notices to websites, providing timestamped records, and offering managed compliance plans. It supports major platforms like WordPress, Shopify, Wix, Squarespace, Webflow, and integrates via Google Tag Manager. Plans range from free scans to subscription services with record‑keeping and legal‑track updates.
image: https://botnotice.app/opengraph-image?8101c44379df9da1
json_schemas:
- name: ConsentCheck
  property_count: 6
  slug: botnotice-app-consent-check
- name: LawRecord
  property_count: 22
  slug: botnotice-app-law-record
- name: ScanResult
  property_count: 14
  slug: botnotice-app-scan-result
- name: VoicePolicy
  property_count: 10
  slug: botnotice-app-voice-policy
jsonld:
- class_count: 4
  name: Botnotice App Context
  property_count: 48
  slug: botnotice-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at botnotice.app.
  name: BotNotice MCP Server
  slug: botnotice-app-mcp-yml
modified: '2026-11-02'
name: BotNotice
nav: Providers
network: true
overview: 'BotNotice publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Consent API, Content register API, Free tools API, and 2 more. Tagged areas include AI disclosure, chatbot compliance, Recordkeeping, website widget, and managed compliance.


  The BotNotice catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BotNotice''s developer surface includes support, getting-started guide, API reference, authentication, documentation, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Botnotice App Plans Pricing
  plan_count: 3
  slug: botnotice-app-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: BotNotice API Rules
  rule_count: 65
  severity_counts:
    error: 60
    hint: 0
    info: 3
    warn: 2
  slug: botnotice-app-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 61.0
    developer_ergonomics: 29.8
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Botnotice App Authentication
  slug: botnotice-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Botnotice App Domain Security
  slug: botnotice-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: botnotice-app
tags:
- AI disclosure
- chatbot compliance
- Recordkeeping
- website widget
- managed compliance
- subscription pricing
website: https://botnotice.app/
---
