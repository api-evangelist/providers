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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Embedded payments API documented on Nuvei developer portal.
  name: Payaut API
  slug: payaut-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/payaut/llms/payaut-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/payaut-llms.txt
- group: other
  href: https://artifacts.apis.io/payaut/hosts/payaut-hosts.yml
  title: ''
  type: Hosts
  url: hosts/payaut-hosts.yml
- group: other
  href: https://artifacts.apis.io/payaut/vendors/payaut-vendors.yml
  title: ''
  type: Vendors
  url: vendors/payaut-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nuvei.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuvei.com/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://www.nuvei.com/post-category/newsroom
- group: start
  title: ''
  type: Login
  url: https://www.nuvei.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nuvei.com/documentation/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://www.nuvei.com/post-category/blog
- group: auth
  href: https://artifacts.apis.io/payaut/security/payaut-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/payaut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payaut.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nuvei.com/documentation/home/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nuvei.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nuvei.com/documentation/online-payments/
coverage:
  checked: '2026-10-29'
  detail: Documentation is available but no OpenAPI/AsyncAPI/GraphQL spec could be retrieved.
  evidence:
  - status: 303
    url: https://api.payaut.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Payaut was a fintech company offering embedded payment solutions for platforms. The payaut.com domain now redirects to Nuvei’s embedded payments page, indicating that Payaut has been acquired or integrated into Nuvei. The company focused on seamless payment integration, supporting global payment methods, payouts, and real‑time transactions for marketplaces, SaaS platforms, and other digital services.
image: https://cdn.prod.website-files.com/69bbe852f53519cb6c89312c/69dcf015a4f8a55dc3098da6_OG-image.jpg
layout: provider
modified: '2026-10-29'
name: Payaut
nav: Providers
network: true
overview: 'Payaut is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Embedded Payments, Platforms, and APIs.


  The Payaut catalog on APIs.io includes 1 Spectral governance ruleset.


  Payaut''s developer surface includes changelog, engineering blog, documentation, getting-started guide, and 10 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Payaut API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: payaut-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 10.5
    developer_ergonomics: 33.3
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Payaut Authentication
  slug: payaut-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Payaut Domain Security
  slug: payaut-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payaut
tags:
- Fintech
- Payments
- Embedded Payments
- Platforms
- APIs
website: https://payaut.com/
---
