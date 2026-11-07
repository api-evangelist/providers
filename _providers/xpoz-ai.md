---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Xpoz Ai Agentic Access
  operation_count: 80
  slug: xpoz-ai-agentic-access
  summary_line: 80 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: Access keys, plan, and usage of the signed-in user.
  name: xpoz-ai Account API
  slug: xpoz-ai-account-api
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: Stripe checkout, subscription changes, and add-on purchases.
  name: xpoz-ai Billing API
  slug: xpoz-ai-billing-api
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: Tracked items collected on a schedule.
  name: xpoz-ai Crawl Settings API
  slug: xpoz-ai-crawl-settings-api
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: On-demand Instagram fetches straight from the platform, cursor-paginated. Not available for trial access keys.
  name: xpoz-ai Instagram (live) API
  slug: xpoz-ai-instagram-live-api
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: Polling for background operations started with `responseType=paging`.
  name: xpoz-ai Operations API
  slug: xpoz-ai-operations-api
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: Health, metrics, and this spec.
  name: xpoz-ai Platform API
  slug: xpoz-ai-platform-api
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: On-demand Reddit fetches straight from the platform, cursor-paginated. Not available for trial access keys.
  name: xpoz-ai Reddit (live) API
  slug: xpoz-ai-reddit-live-api
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: Platform status page and notifications.
  name: xpoz-ai System Status API
  slug: xpoz-ai-system-status-api
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: On-demand TikTok fetches straight from the platform, cursor-paginated. Not available for trial access keys.
  name: xpoz-ai TikTok (live) API
  slug: xpoz-ai-tiktok-live-api
- baseURL: https://api.xpoz.ai
  baseurl_source: declared
  description: On-demand Twitter/X fetches straight from the platform, cursor-paginated. Not available for trial access keys.
  name: xpoz-ai Twitter (live) API
  slug: xpoz-ai-twitter-live-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/xpoz-ai/agentic-access/xpoz-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xpoz-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/xpoz-ai/rules/xpoz-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/xpoz-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/xpoz-ai/json-ld/xpoz-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/xpoz-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/xpoz-ai/vocabulary/xpoz-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xpoz-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/xpoz-ai/data-model/xpoz-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xpoz-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/xpoz-ai/errors/xpoz-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xpoz-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xpoz-ai/conformance/xpoz-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xpoz-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/xpoz-ai/llms/xpoz-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xpoz-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/xpoz-ai/a2a/xpoz-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/xpoz-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/xpoz-ai/well-known/xpoz-ai-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xpoz-ai-help-security.txt
- group: agent
  href: https://artifacts.apis.io/xpoz-ai/well-known/xpoz-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xpoz-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/xpoz-ai/hosts/xpoz-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xpoz-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/xpoz-ai/vendors/xpoz-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xpoz-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/xpoz-ai/packages/xpoz-ai-packages.yml
  title: ''
  type: Packages
  url: packages/xpoz-ai-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.xpoz.ai/webhooks/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xpoz.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://help.xpoz.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.xpoz.ai/use-cases/security/
- group: build
  title: ''
  type: SDKs
  url: https://www.xpoz.ai/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xpoz.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XPOZpublic
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.xpoz.ai\
- group: auth
  href: https://artifacts.apis.io/xpoz-ai/authentication/xpoz-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xpoz-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/xpoz-ai/security/xpoz-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xpoz-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xpoz.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xpoz.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api.xpoz.ai/api-docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xpoz.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.xpoz.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.xpoz.ai/en/collections/16124756-getting-started
created: '2026-10-31'
description: XPOZ AI provides a Social Data API for AI agents, enabling brand monitoring, social listening, lead generation, and competitive intelligence across platforms like Twitter/X, Instagram, TikTok, and Reddit. The service offers typed SDKs, a MCP server, and a CLI, with a free tier and extensive documentation for developers to integrate social data into AI workflows.
image: https://www.xpoz.ai/og-image.png
json_schemas:
- name: AccessKeyCreated
  property_count: 4
  slug: xpoz-ai-access-key-created
- name: AccessKeyRecord
  property_count: 15
  slug: xpoz-ai-access-key-record
- name: CrawlSettings
  property_count: 4
  slug: xpoz-ai-crawl-settings
- name: CursorResponse
  property_count: 5
  slug: xpoz-ai-cursor-response
- name: OperationState
  property_count: 6
  slug: xpoz-ai-operation-state
- name: PurchaseResult
  property_count: 0
  slug: xpoz-ai-purchase-result
jsonld:
- class_count: 40
  name: Xpoz Ai Context
  property_count: 100
  slug: xpoz-ai-context
layout: provider
modified: '2026-10-31'
name: xpoz-ai
nav: Providers
network: true
overview: 'xpoz-ai publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Crawl Settings API, and 7 more. Tagged areas include Company, Social Data, Artificial Intelligence, Monitoring, and Analytics.


  The xpoz-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  xpoz-ai''s developer surface includes support, authentication, documentation, API reference, pricing, engineering blog, getting-started guide, and 23 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: xpoz-ai API Rules
  rule_count: 16
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 6
  slug: xpoz-ai-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 59.7
    developer_ergonomics: 41.7
    discoverability: 66.1
    operational_transparency: 11.8
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: unknown
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Xpoz Ai Authentication
  slug: xpoz-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Xpoz Ai Domain Security
  slug: xpoz-ai-domain-security
  summary_line: TLSv1.3
slug: xpoz-ai
tags:
- Company
- Social Data
- Artificial Intelligence
- Monitoring
- Analytics
- SDK
website: https://www.xpoz.ai/
---
