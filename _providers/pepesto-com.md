---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Real-time product catalogs, live pricing, promotions and nutrition data across 28 European supermarkets.
  name: Grocery Data API
  slug: grocery-data-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/pepesto-com/plans/pepesto-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pepesto-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pepesto-com/components/pepesto-com-components.yml
  title: ''
  type: Components
  url: components/pepesto-com-components.yml
- group: design
  href: https://artifacts.apis.io/pepesto-com/conventions/pepesto-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pepesto-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/pepesto-com/authentication/pepesto-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pepesto-com-authentication.yml
- group: other
  href: https://artifacts.apis.io/pepesto-com/hosts/pepesto-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pepesto-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pepesto-com/vendors/pepesto-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pepesto-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/pepesto-com/security/pepesto-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pepesto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pepesto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pepesto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pepesto.com/supermarkets/
- group: docs
  title: ''
  type: APIReference
  url: https://www.pepesto.com/ai-grocery-shopping-agent/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pepesto.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.pepesto.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.pepesto.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pepesto.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pepesto.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pepesto.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pepesto-solutions/
coverage:
  checked: '2026-10-31'
  detail: The provider's public documentation pages describe the API but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://www.pepesto.com/ai-grocery-shopping-agent/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Pepesto offers a unified API that aggregates live grocery pricing and product data across Europe. Covering 28 supermarket chains in 13 countries, the platform provides real‑time catalog information, price comparisons, and dietary filters. Developers can quickly integrate up‑to‑date grocery data into apps, agents, and AI services, enabling seamless shopping experiences and market analytics. The service includes instant API key provisioning, flexible credit packs, and comprehensive documentation for rapid onboarding.
image: https://www.pepesto.com/images/logo.svg
layout: provider
modified: '2026-10-30'
name: pepesto-com
nav: Providers
network: true
overview: 'pepesto-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Grocery, API, European, and Pricing.


  pepesto-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Pepesto Com Plans Pricing
  plan_count: 3
  slug: pepesto-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Pepesto Com Rate Limits
  slug: pepesto-com-rate-limits
scopes:
- name: Pepesto Com Scopes
  scope_count: 0
  slug: pepesto-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pepesto Com Authentication
  slug: pepesto-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pepesto Com Domain Security
  slug: pepesto-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pepesto-com
tags:
- Company
- Grocery
- API
- European
- Pricing
website: https://pepesto.com/
---
