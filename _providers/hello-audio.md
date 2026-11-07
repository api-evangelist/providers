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
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Hello Audio does not document a public REST API. Programmatic access is through its Zapier app (listener and feed triggers and actions), outbound generic webhooks, Make/Integromat webhooks and native '
  name: Hello Audio API
  slug: hello-audio-api
- description: Remote Model Context Protocol server that gives an AI assistant read-only access to the feeds on a signed-in Hello Audio account (downloads, listeners, retention and similar figures); it cannot upload
  name: Hello Audio MCP Server
  slug: hello-audio-mcp-server
artifact_total: 10
common:
- group: other
  href: https://artifacts.apis.io/hello-audio/a2a/hello-audio-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hello-audio-a2a.yml
- group: other
  href: https://artifacts.apis.io/hello-audio/hosts/hello-audio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hello-audio-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zapier.com/llms.txt
- group: design
  href: https://artifacts.apis.io/hello-audio/rules/hello-audio-rules.yml
  title: ''
  type: Spectral
  url: rules/hello-audio-rules.yml
- group: design
  href: https://artifacts.apis.io/hello-audio/json-ld/hello-audio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hello-audio-context.jsonld
- group: design
  href: https://artifacts.apis.io/hello-audio/vocabulary/hello-audio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hello-audio-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hello-audio/data-model/hello-audio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hello-audio-data-model.yml
- group: design
  href: https://artifacts.apis.io/hello-audio/conventions/hello-audio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hello-audio-conventions.yml
- group: auth
  href: https://artifacts.apis.io/hello-audio/authentication/hello-audio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hello-audio-authentication.yml
- group: operate
  href: https://artifacts.apis.io/hello-audio/lifecycle/hello-audio-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hello-audio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hello-audio/lifecycle/hello-audio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hello-audio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hello-audio/conformance/hello-audio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hello-audio-conformance.yml
- group: build
  href: https://artifacts.apis.io/hello-audio/integrations/hello-audio-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/hello-audio-integration-edges.yml
- group: commercial
  href: https://artifacts.apis.io/hello-audio/plans/hello-audio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hello-audio-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/hello-audio/llms/hello-audio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hello-audio-llms.txt
- group: auth
  href: https://artifacts.apis.io/hello-audio/well-known/hello-audio-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hello-audio-help-security.txt
- group: agent
  href: https://artifacts.apis.io/hello-audio/well-known/hello-audio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hello-audio-well-known.yml
- group: other
  href: https://artifacts.apis.io/hello-audio/vendors/hello-audio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hello-audio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hello-audio/security/hello-audio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hello-audio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://helloaudio.fm/
- group: docs
  title: ''
  type: Documentation
  url: https://help.helloaudio.fm/en/collections/14938214-zapier-webhooks
- group: start
  title: ''
  type: GettingStarted
  url: https://help.helloaudio.fm/en/collections/14937853-getting-started
- group: other
  title: ''
  type: Zapier
  url: https://zapier.com/apps/hello-audio/integrations
- group: company
  title: ''
  type: Blog
  url: https://helloaudio.fm/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://helloaudio.fm/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://helloaudio.fm/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://helloaudio.fm/privacy/
- group: start
  title: ''
  type: Login
  url: https://app.helloaudio.fm/login
- group: operate
  title: ''
  type: Support
  url: https://help.helloaudio.fm/en/
- group: company
  title: ''
  type: About
  url: https://helloaudio.fm/about/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@helloaudiofm
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/helloaudiofm/
coverage:
  checked: '2026-11-04'
  detail: Hello Audio publishes no REST, GraphQL or AsyncAPI contract; its one machine interface, the remote MCP server at mcp.helloaudio.fm/mcp, answers initialize and tools/list with 401 'Missing bearer token' and points to OAuth at auth.helloaudio.fm, so tool schemas are readable only after signing in to a Hello Audio account.
  evidence:
  - status: 401
    url: https://mcp.helloaudio.fm/mcp
  - status: 200
    url: https://mcp.helloaudio.fm/.well-known/oauth-protected-resource/mcp
  - status: 200
    url: https://help.helloaudio.fm/en/articles/17761552-how-do-i-connect-hello-audio-to-claude-with-the-mcp-connector.md
  reason: auth-required
  state: gated
created: '2026-10-28'
description: Hello Audio (helloaudio.fm) is a hosted platform for private and public podcasts. Creators, course builders and businesses turn existing content such as courses, videos and memberships into private audio feeds that listeners subscribe to through signup pages, with listener management, analytics and AI tooling. It has no public REST API; integration is documented through a Zapier app (triggers and actions), generic and Make/Integromat webhooks, and native connections to email services, course platforms, checkout carts, Stripe, Dropbox, Google Drive and Zoom.
image: https://helloaudio.fm/wp-content/uploads/2022/02/MainLogo.webp
jsonld:
- class_count: 32
  name: Hello Audio Context
  property_count: 37
  slug: hello-audio-context
layout: provider
mcp_servers:
- description: ''
  name: Hello Audio MCP Server
  slug: mcp
modified: '2026-11-04'
name: Hello Audio
nav: Providers
network: true
overview: 'Hello Audio is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audio, Podcasts, Software-as-a-Service, and Private.


  The Hello Audio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hello Audio''s developer surface includes API reference, authentication, documentation, getting-started guide, engineering blog, pricing, support, and 25 more developer resources.'
plans:
- name: Hello Audio Plans Pricing
  plan_count: 7
  slug: hello-audio-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Hello Audio Rate Limits
  slug: hello-audio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Hello Audio API Rules
  rule_count: 44
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 4
  slug: hello-audio-rules
scopes:
- name: Hello Audio Scopes
  scope_count: 0
  slug: hello-audio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 20.4
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 43.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hello-audio/hello-audio-2026-11-03T133339.png
security:
- kind: authentication
  name: Hello Audio Authentication
  slug: hello-audio-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Hello Audio Domain Security
  slug: hello-audio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hello-audio
tags:
- Company
- Audio
- Podcasts
- Software-as-a-Service
- Private
- Private Podcasts
- Webhook
- Zapier
- Creator Economy
website: https://helloaudio.fm/
---
