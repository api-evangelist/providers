---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Duck.ai is DuckDuckGo's anonymizing proxy in front of third-party LLMs. Free tier currently includes Anthropic Claude 4.5 Haiku, Meta Llama 4 Scout, Mistral Small 3 24B, OpenAI GPT-4o mini / GPT-5 min
  name: Duck.ai Anonymous AI Chat
  slug: duck-ai
- description: Tracker Radar is the open dataset that powers DuckDuckGo's tracker and fingerprinting protection. It is a JSON corpus of the most common third-party domains on the web, with metadata covering behavior
  name: DuckDuckGo Tracker Radar Dataset
  slug: tracker-radar
- description: 'The !bang system - in place since 2008 and now spanning thousands of destinations - lets a query like "!w filter bubble" 302-redirect to the destination site''s own search (Wikipedia in that example). '
  name: DuckDuckGo !Bang Redirector
  slug: bang-redirector
- description: Resolve !bang queries to redirect URLs.
  name: DuckDuckGo Bangs API
  slug: duckduckgo-bangs-api
- description: Zero-click answers, abstracts, definitions and disambiguations.
  name: DuckDuckGo Instant Answers API
  slug: duckduckgo-instant-answers-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DuckDuckGo Instant Answer Bangs API
  slug: open-duckduckgo-bangs-api
- collection_type: open
  name: DuckDuckGo Instant Answer Instant Answers API
  slug: open-duckduckgo-instant-answers-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/duckduckgo/tracker-radar/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/duckduckgo/tracker-radar/releases
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/duckduckgo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duckduckgo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duckduckgo.com/
- group: start
  title: ''
  type: Portal
  url: https://duckduckgo.com/duckduckgo-help-pages/
- group: company
  title: ''
  type: Blog
  url: https://spreadprivacy.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://spreadprivacy.com/rss/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duckduckgo
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/duckduckgo
- group: other
  title: DuckDuckGo Browser
  type: Browser
  url: https://duckduckgo.com/app
- group: other
  title: Duck.ai
  type: AIChat
  url: https://duck.ai/
- group: other
  title: ''
  type: EmailProtection
  url: https://duckduckgo.com/email/
- group: commercial
  title: ''
  type: PrivacyPro
  url: https://duckduckgo.com/privacy-pro
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://duckduckgo.com/privacy
- group: commercial
  title: ''
  type: Plans
  url: plans/duckduckgo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/duckduckgo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/duckduckgo-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/duckduckgo-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/duckduckgo-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://duck.ai/llms.txt
created: '2026-05-23'
description: DuckDuckGo is an independent online-privacy company best known for its tracker-free search engine and the DuckDuckGo Browser (iOS, Android, macOS, Windows). It operates the public Instant Answer API at api.duckduckgo.com (free, JSON/XML), the Duck.ai anonymous AI-chat proxy at duck.ai (routes to Anthropic Claude, OpenAI GPT, Meta Llama, Mistral models without storing or training on prompts), the Tracker Radar open dataset (CC BY-NC-SA), Email Protection (@duck.com forwarding addresses), and Privacy Pro (VPN + Personal Information Removal + Identity Theft Restoration).
examples:
- key_count: 2
  name: Instant Answer Bang Example
  slug: instant-answer-bang-example
- key_count: 2
  name: Instant Answer Calc Example
  slug: instant-answer-calc-example
- key_count: 2
  name: Instant Answer Topic Example
  slug: instant-answer-topic-example
- key_count: 14
  name: Tracker Radar Domain Example
  slug: tracker-radar-domain-example
finops:
- name: Duckduckgo Finops
  service_category: ''
  slug: duckduckgo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/duckduckgo.png
json_schemas:
- name: DuckDuckGo Instant Answer Response
  property_count: 21
  slug: instant-answer-response
- name: DuckDuckGo Tracker Radar Domain Record
  property_count: 14
  slug: tracker-radar-domain
json_structures:
- name: Instant Answer Response Structure
  property_count: 0
  slug: instant-answer-response-structure
jsonld:
- class_count: 22
  name: Duckduckgo Context
  property_count: 5
  slug: duckduckgo-context
layout: provider
modified: '2026-05-23'
name: DuckDuckGo
nav: Providers
network: true
overview: 'DuckDuckGo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bangs API and Instant Answers API. Tagged areas include Search, Privacy, Browser, AI Chat, and Email Protection.


  The DuckDuckGo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  DuckDuckGo''s developer surface includes developer portal, engineering blog, and 19 more developer resources.'
plans:
- name: Duckduckgo Plans Pricing
  plan_count: 6
  slug: duckduckgo-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Duckduckgo Rate Limits
  slug: duckduckgo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: DuckDuckGo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: duckduckgo-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: DuckDuckGo API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: instant-answer-rules
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 27.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -3.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 28.8
    contract_quality: 63.3
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 25.0
  previous_composite: 50.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duckduckgo/refs/heads/main/screenshots/duckduckgo-2026-06-20T180307.png
security:
- kind: domain-security
  name: Duckduckgo Domain Security
  slug: duckduckgo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Duckduckgo Vulnerability Disclosure
  slug: duckduckgo-vulnerability-disclosure
  summary_line: disclosure policy published
slug: duckduckgo
tags:
- Search
- Privacy
- Browser
- AI Chat
- Email Protection
- VPN
- Trackers
- Identity
website: https://duckduckgo.com/
---
