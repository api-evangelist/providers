---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Socially Run Agentic Access
  operation_count: 30
  slug: socially-run-agentic-access
  summary_line: 30 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: The open-source datasets behind username search and what their licenses ask of you.
  name: socially-run Attributions API
  slug: socially-run-attributions-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: 'The deep run: a full username sweep with the details each site exposes, delivered as one report.'
  name: socially-run Dossiers API
  slug: socially-run-dossiers-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: Find which services an email address is registered on. Paid plans, after accepting the acceptable-use policy.
  name: socially-run Emails API
  slug: socially-run-emails-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: Follow, page through, stream and cancel the asynchronous searches.
  name: socially-run Jobs API
  slug: socially-run-jobs-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: Which platforms and strategies are healthy, degraded or down at this moment.
  name: socially-run Platforms API
  slug: socially-run-platforms-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: 'Read one public post by URL: caption, media type, counts where the platform shows them.'
  name: socially-run Posts API
  slug: socially-run-posts-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: Read a public profile on Instagram, TikTok, YouTube, LinkedIn, X, Facebook, GitHub or a website, one at a time or in a batch, and aggregate the batch into one intelligence report.
  name: socially-run Profiles API
  slug: socially-run-profiles-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: Turn a URL or @handle into a platform and a canonical handle. Free, no lookup happens.
  name: socially-run Resolve API
  slug: socially-run-resolve-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: Find videos, popular reels, hashtag posts and news about a subject.
  name: socially-run Search API
  slug: socially-run-search-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: What is trending right now on Google and YouTube, by country.
  name: socially-run Trending API
  slug: socially-run-trending-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: Credits charged this month, split by kind and by API key.
  name: socially-run Usage API
  slug: socially-run-usage-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: Search one username across thousands of sites (a fast top-200 pass or the full database) and browse the site list.
  name: socially-run Usernames API
  slug: socially-run-usernames-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: Read a web page as clean text and structured data, or fetch its Open Graph card.
  name: socially-run Web API
  slug: socially-run-web-api
- baseURL: https://api.socially.run/v1
  baseurl_source: declared
  description: 'One signed-event endpoint per account: set it, test-fire it, rotate its secret, read its delivery log.'
  name: socially-run Webhooks API
  slug: socially-run-webhooks-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/socially-run/agentic-access/socially-run-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/socially-run-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/socially-run/rate-limits/socially-run-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/socially-run-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/socially-run/plans/socially-run-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/socially-run-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/socially-run/rules/socially-run-rules.yml
  title: ''
  type: Spectral
  url: rules/socially-run-rules.yml
- group: design
  href: https://artifacts.apis.io/socially-run/json-ld/socially-run-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/socially-run-context.jsonld
- group: design
  href: https://artifacts.apis.io/socially-run/vocabulary/socially-run-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/socially-run-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/socially-run/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/socially-run/data-model/socially-run-data-model.yml
  title: ''
  type: DataModel
  url: data-model/socially-run-data-model.yml
- group: auth
  href: https://artifacts.apis.io/socially-run/authentication/socially-run-authentication.yml
  title: ''
  type: Authentication
  url: authentication/socially-run-authentication.yml
- group: design
  href: https://artifacts.apis.io/socially-run/errors/socially-run-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/socially-run-problem-types.yml
- group: design
  href: https://artifacts.apis.io/socially-run/conformance/socially-run-conformance.yml
  title: ''
  type: Conformance
  url: conformance/socially-run-conformance.yml
- group: agent
  href: https://artifacts.apis.io/socially-run/llms/socially-run-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/socially-run-llms.txt
- group: agent
  href: https://artifacts.apis.io/socially-run/well-known/socially-run-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/socially-run-well-known.yml
- group: other
  href: https://artifacts.apis.io/socially-run/hosts/socially-run-hosts.yml
  title: ''
  type: Hosts
  url: hosts/socially-run-hosts.yml
- group: other
  href: https://artifacts.apis.io/socially-run/vendors/socially-run-vendors.yml
  title: ''
  type: Vendors
  url: vendors/socially-run-vendors.yml
- group: build
  href: https://artifacts.apis.io/socially-run/packages/socially-run-packages.yml
  title: ''
  type: SDKs
  url: packages/socially-run-packages.yml
- group: build
  href: https://artifacts.apis.io/socially-run/packages/socially-run-packages.yml
  title: ''
  type: Packages
  url: packages/socially-run-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.yourapp.com/hooks/socially
- group: auth
  href: https://artifacts.apis.io/socially-run/security/socially-run-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socially-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socially.run/
- group: docs
  title: ''
  type: Documentation
  url: https://socially.run/docs/en
- group: docs
  title: ''
  type: APIReference
  url: https://socially.run/docs/en
- group: start
  title: ''
  type: GettingStarted
  url: https://socially.run/en/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://socially.run/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socially.run/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socially.run/en/privacy
created: '2026-10-31'
description: Entregue ao seu agente de IA ou ao seu backend os dados públicos de Instagram, TikTok, YouTube, LinkedIn, X, Facebook, GitHub e qualquer página da web em JSON. Uma chave para MCP, SDK, REST e console.
image: https://socially.run/og/home.png
jsonld:
- class_count: 1
  name: Socially Run Context
  property_count: 1
  slug: socially-run-context
layout: provider
modified: '2026-10-31'
name: socially-run
nav: Providers
network: true
overview: 'socially-run publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attributions API, Dossiers API, Emails API, and 11 more. Tagged areas include Social Media, Data API, JSON, MCP, and AI-Agent.


  The socially-run catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  socially-run''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 21 more developer resources.'
plans:
- name: Socially Run Plans Pricing
  plan_count: 4
  slug: socially-run-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Socially Run Rate Limits
  slug: socially-run-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: socially-run API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: socially-run-rules
scopes:
- name: Socially Run Scopes
  scope_count: 0
  slug: socially-run-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 84.3
    catalog_earned_first_party: 0.0
    catalog_gap: 30.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 49.2
    developer_ergonomics: 63.6
    discoverability: 66.1
    operational_transparency: 28.4
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
  name: Socially Run Authentication
  slug: socially-run-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Socially Run Domain Security
  slug: socially-run-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: resolve
  slug: socially-run-resolve
slug: socially-run
tags:
- Social Media
- Data API
- JSON
- MCP
- AI-Agent
website: https://socially.run/
---
