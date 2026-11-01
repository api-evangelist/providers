---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Hello Audio does not document a public REST API. Programmatic access is through its Zapier app (listener and feed triggers and actions), outbound generic webhooks, Make/Integromat webhooks and native '
  name: Hello Audio API
  slug: hello-audio-api
artifact_total: 8
common:
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
- group: other
  href: https://artifacts.apis.io/hello-audio/a2a/hello-audio-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hello-audio-a2a.yml
- group: build
  href: https://artifacts.apis.io/hello-audio/integrations/hello-audio-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/hello-audio-integration-edges.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zapier.com/llms.txt
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
  href: https://artifacts.apis.io/hello-audio/hosts/hello-audio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hello-audio-hosts.yml
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
coverage:
  checked: '2026-10-28'
  detail: Hello Audio documents only a per-account Generic Webhook (a JSON body POSTed to a URL shown inside the app) and Zapier and Make actions in its Intercom help center, and app.helloaudio.fm answers every spec path with its single-page-app HTML shell.
  evidence:
  - status: 200
    url: https://app.helloaudio.fm/openapi.json
  - status: 404
    url: https://help.helloaudio.fm/openapi.json
  - status: 200
    url: https://help.helloaudio.fm/en/articles/10260478-generic-webhooks.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Hello Audio (helloaudio.fm) is a hosted platform for private and public podcasts. Creators, course builders and businesses turn existing content such as courses, videos and memberships into private audio feeds that listeners subscribe to through signup pages, with listener management, analytics and AI tooling. It has no public REST API; integration is documented through a Zapier app (triggers and actions), generic and Make/Integromat webhooks, and native connections to email services, course platforms, checkout carts, Stripe, Dropbox, Google Drive and Zoom.
image: https://helloaudio.fm/wp-content/uploads/2022/02/MainLogo.webp
jsonld:
- class_count: 32
  name: Hello Audio Context
  property_count: 37
  slug: hello-audio-context
layout: provider
modified: '2026-10-28'
name: Hello Audio
nav: Providers
network: true
overview: 'Hello Audio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audio, Podcast, SaaS, and Private.


  The Hello Audio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hello Audio''s developer surface includes authentication, API reference, documentation, getting-started guide, engineering blog, pricing, support, and 22 more developer resources.'
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
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Hello Audio API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 3
  slug: hello-audio-rules
scopes:
- name: Hello Audio Scopes
  scope_count: 0
  slug: hello-audio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hello Audio Authentication
  slug: hello-audio-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hello Audio Domain Security
  slug: hello-audio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hello-audio
tags:
- Company
- Audio
- Podcast
- SaaS
- Private
- Private Podcasts
- Webhooks
- Zapier
- Creator Economy
website: https://helloaudio.fm/
---
