---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 130
  human_in_the_loop: 2
  name: Blawgy Com Agentic Access
  operation_count: 202
  slug: blawgy-com-agentic-access
  summary_line: 202 operations · 130 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: The caller, their sites, async jobs and the tool escape hatch.
  name: blawgy-com Account API
  slug: blawgy-com-account-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: 'Articles on a site: list, read, write now, edit, schedule, publish and record live URLs.'
  name: blawgy-com Articles API
  slug: blawgy-com-articles-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: 'The article builder: titles, outlines, sections, remixes and drafts.'
  name: blawgy-com Builder API
  slug: blawgy-com-builder-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: The inventory of pages that already exist on the site.
  name: blawgy-com Existing pages API
  slug: blawgy-com-existing-pages-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Article images, the photo bank and brand colors.
  name: blawgy-com Images API
  slug: blawgy-com-images-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: The publishing platform and search-engine connections.
  name: blawgy-com Integrations API
  slug: blawgy-com-integrations-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Keyword research, the research brief, your own keywords and exclusions.
  name: blawgy-com Keywords API
  slug: blawgy-com-keywords-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Business locations and location pages.
  name: blawgy-com Location pages API
  slug: blawgy-com-location-pages-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Overview, traffic, rankings, AI mentions, indexing and on-site behavior.
  name: blawgy-com Metrics API
  slug: blawgy-com-metrics-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: White-label partner owners managing clients. Needs a partner-scoped key.
  name: blawgy-com Partner API
  slug: blawgy-com-partner-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: 'The content plan: entries, cadence, autopilot and suggestions.'
  name: blawgy-com Plan API
  slug: blawgy-com-plan-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Products the articles can feature, and the Dutchie inventory link.
  name: blawgy-com Products API
  slug: blawgy-com-products-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Published posts for headless frontends and static builds. No key; callable from browsers; cacheable.
  name: blawgy-com Public content API
  slug: blawgy-com-public-content-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Refresh requests for existing pages (sites with existing-content checks on).
  name: blawgy-com Refresh API
  slug: blawgy-com-refresh-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Site settings, guardrails, draft mode and the pixel.
  name: blawgy-com Settings API
  slug: blawgy-com-settings-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Help search and support requests.
  name: blawgy-com Support API
  slug: blawgy-com-support-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Teammates, invites and billing.
  name: blawgy-com Team and billing API
  slug: blawgy-com-team-and-billing-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Smart updates to published articles (Pro+).
  name: blawgy-com Updates API
  slug: blawgy-com-updates-api
- baseURL: https://app.blawgy.com/v1
  baseurl_source: declared
  description: Outbound webhooks and their deliveries.
  name: blawgy-com Webhooks API
  slug: blawgy-com-webhooks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Blawgy Com Webhooks
  slug: blawgy-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/blawgy-com/agentic-access/blawgy-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blawgy-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/blawgy-com/rate-limits/blawgy-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blawgy-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/blawgy-com/plans/blawgy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blawgy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blawgy-com/rules/blawgy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blawgy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blawgy-com/json-ld/blawgy-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blawgy-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/blawgy-com/vocabulary/blawgy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blawgy-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/blawgy-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blawgy-com/asyncapi/blawgy-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/blawgy-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/blawgy-com/data-model/blawgy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blawgy-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/blawgy-com/changelog/blawgy-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blawgy-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/blawgy-com/conventions/blawgy-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blawgy-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/blawgy-com/conventions/blawgy-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blawgy-com-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://blawgy.com/developers/versioning
- group: design
  href: https://artifacts.apis.io/blawgy-com/lifecycle/blawgy-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/blawgy-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/blawgy-com/errors/blawgy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blawgy-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blawgy-com/conformance/blawgy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blawgy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blawgy-com/llms/blawgy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blawgy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/blawgy-com/well-known/blawgy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blawgy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blawgy-com/hosts/blawgy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blawgy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blawgy-com/vendors/blawgy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blawgy-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://blawgy.com/help/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blawgy.com/terms
- group: operate
  title: ''
  type: Support
  url: https://blawgy.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blawgy.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://blawgy.com/help/plans-and-pricing
- group: docs
  title: ''
  type: Documentation
  url: https://blawgy.com/developers/guides/partners
- group: start
  title: ''
  type: DeveloperPortal
  url: https://blawgy.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://blawgy.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://blawgy.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://blawgy.com/help#getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://blawgy.com/developers/reference
- group: auth
  href: https://artifacts.apis.io/blawgy-com/authentication/blawgy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blawgy-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/blawgy-com/security/blawgy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blawgy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blawgy.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://app.blawgy.com/v1/openapi.json
  - status: 401
    url: https://app.blawgy.com/mcp
  - status: 200
    url: https://blawgy.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Blawgy offers an AI‑driven content platform that writes, publishes, and continuously updates blog articles for businesses to appear in ChatGPT and Google AI search results. It targets high‑intent keywords, integrates with web platforms such as WordPress, Shopify, and Webflow, and provides analytics through Search Console and a cookieless pixel. The service is sold to agencies and direct business customers seeking automated SEO‑focused content.
image: https://blawgy.com/og-image.png
json_schemas:
- name: PublicPost
  property_count: 19
  slug: blawgy-com-public-post
jsonld:
- class_count: 2
  name: Blawgy Com Context
  property_count: 20
  slug: blawgy-com-context
layout: provider
modified: '2026-11-02'
name: blawgy-com
nav: Providers
network: true
overview: 'blawgy-com publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Articles API, Builder API, and 16 more. Tagged areas include Content AI, SEO, Blog Publishing, AI Search, and Agency Tools.


  The blawgy-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  blawgy-com''s developer surface includes changelog, support, pricing, documentation, engineering blog, getting-started guide, API reference, and 27 more developer resources.'
plans:
- name: Blawgy Com Plans Pricing
  plan_count: 2
  slug: blawgy-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Blawgy Com Rate Limits
  slug: blawgy-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: blawgy-com API Rules
  rule_count: 68
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 12
  slug: blawgy-com-rules
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 76.2
    catalog_earned_first_party: 20.0
    catalog_gap: 38.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 67.9
    developer_ergonomics: 36.3
    discoverability: 66.1
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
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
  name: Blawgy Com Authentication
  slug: blawgy-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Blawgy Com Domain Security
  slug: blawgy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: blawgy-com-connect-gsc-property
  slug: blawgy-com-connect-gsc-property
- name: blawgy-com-create-configure-webhook
  slug: blawgy-com-create-configure-webhook
- name: blawgy-com-manage-sites
  slug: blawgy-com-manage-sites
- name: blawgy-com-run-seo-scan
  slug: blawgy-com-run-seo-scan
slug: blawgy-com
tags:
- Content AI
- SEO
- Blog Publishing
- AI Search
- Agency Tools
website: https://blawgy.com/
---
