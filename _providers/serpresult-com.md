---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Serpresult Com Agentic Access
  operation_count: 21
  slug: serpresult-com-agentic-access
  summary_line: 21 operations · 10 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: SerpResult Search API providing SERP results across multiple engines.
  name: SerpResult API
  slug: serpresult-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: The account behind the calling credential. Accepts an API key or a session cookie. Costs no credits.
  name: serpresult-com Account API
  slug: serpresult-com-account-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: Mint, list, rename, rotate and revoke secret keys. Session only.
  name: serpresult-com API keys API
  slug: serpresult-com-api-keys-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: The account's plan, where it stands against its quota, and buying or moving between plans through Polar. Session only.
  name: serpresult-com Billing API
  slug: serpresult-com-billing-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: Unauthenticated service endpoints.
  name: serpresult-com Meta API
  slug: serpresult-com-meta-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: The metered search endpoints. Accept an API key, a session cookie, the demo header or the marketplace proxy.
  name: serpresult-com Search API
  slug: serpresult-com-search-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: Account-wide reporting read off the query log. Session only.
  name: serpresult-com Usage API
  slug: serpresult-com-usage-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/serpresult-com/agentic-access/serpresult-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/serpresult-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/serpresult-com/rate-limits/serpresult-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/serpresult-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/serpresult-com/plans/serpresult-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/serpresult-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/rules/serpresult-com-rules.yml
  title: ''
  type: Spectral
  url: rules/serpresult-com-rules.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/json-ld/serpresult-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/serpresult-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/serpresult-com/vocabulary/serpresult-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/serpresult-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/serpresult-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/data-model/serpresult-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/serpresult-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/serpresult-com/authentication/serpresult-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/serpresult-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/errors/serpresult-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/serpresult-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/conformance/serpresult-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/serpresult-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/serpresult-com/llms/serpresult-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/serpresult-com-llms.txt
- group: other
  href: https://artifacts.apis.io/serpresult-com/hosts/serpresult-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/serpresult-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/serpresult-com/vendors/serpresult-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/serpresult-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/serpresult-com/packages/serpresult-com-packages.yml
  title: ''
  type: SDKs
  url: packages/serpresult-com-packages.yml
- group: build
  href: https://artifacts.apis.io/serpresult-com/packages/serpresult-com-packages.yml
  title: ''
  type: Packages
  url: packages/serpresult-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/serpresult-com/security/serpresult-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/serpresult-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://serpresult.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.serpresult.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.serpresult.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.serpresult.com/api/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.serpresult.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.serpresult.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.serpresult.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://www.serpresult.com/status
- group: operate
  title: ''
  type: Support
  url: https://www.serpresult.com/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.serpresult.com/openapi.json
  - status: null
    url: https://docs.serpresult.com/openapi.json
  - status: 401
    url: https://api.serpresult.com/mcp
  - status: 200
    url: https://serpresult.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: SerpResult provides a SERP API aggregating search results from Google, Bing, DuckDuckGo, Yahoo, Brave, and Yandex across 193 countries. It returns organic results in JSON with fields like position, title, URL, domain, and snippet. The service offers a simple GET endpoint for queries, a free demo limit, and paid plans. Documentation, pricing, and support are available on its website.
image: https://serpresult.com/og-image.png
jsonld:
- class_count: 44
  name: Serpresult Com Context
  property_count: 89
  slug: serpresult-com-context
layout: provider
modified: '2026-10-31'
name: serpresult-com
nav: Providers
network: true
overview: 'serpresult-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, API keys API, Billing API, and 4 more. Tagged areas include SERP, Search, API, Aggregator, and SEO.


  The serpresult-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  serpresult-com''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, and 20 more developer resources.'
plans:
- name: Serpresult Com Plans Pricing
  plan_count: 4
  slug: serpresult-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 7
  name: Serpresult Com Rate Limits
  slug: serpresult-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: serpresult-com API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: serpresult-com-rules
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 90.3
    catalog_earned_first_party: 0.0
    catalog_gap: 24.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 57.3
    developer_ergonomics: 58.8
    discoverability: 66.1
    operational_transparency: 44.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Serpresult Com Authentication
  slug: serpresult-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Serpresult Com Domain Security
  slug: serpresult-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: serpresult-com-billing-purchase
  slug: serpresult-com-billing-purchase
- name: serpresult-com-manage-api-keys
  slug: serpresult-com-manage-api-keys
- name: serpresult-com-search-multiple
  slug: serpresult-com-search-multiple
slug: serpresult-com
tags:
- SERP
- Search
- API
- Aggregator
- SEO
website: https://serpresult.com/
---
