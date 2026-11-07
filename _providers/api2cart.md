---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Api2Cart Agentic Access
  operation_count: 1
  slug: api2cart-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.api2cart.local.com/v1.1
  baseurl_source: spec
  description: The Account.failed Webhooks.json API from Lexy Mayko — 1 operation(s) for account.failed webhooks.json.
  name: Lexy Mayko Account.failed Webhooks.json API
  slug: api2cart-account-failed-webhooks-json-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/api2cart/vocabulary/api2cart-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/api2cart-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/api2cart/agentic-access/api2cart-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/api2cart-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/api2cart/plans/api2cart-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/api2cart-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/api2cart/rules/api2cart-rules.yml
  title: ''
  type: Spectral
  url: rules/api2cart-rules.yml
- group: operate
  href: https://artifacts.apis.io/api2cart/changelog/api2cart-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/api2cart-changelog.yml
- group: design
  href: https://artifacts.apis.io/api2cart/conventions/api2cart-conventions.yml
  title: ''
  type: Conventions
  url: conventions/api2cart-conventions.yml
- group: design
  href: https://artifacts.apis.io/api2cart/conformance/api2cart-conformance.yml
  title: ''
  type: Conformance
  url: conformance/api2cart-conformance.yml
- group: agent
  href: https://artifacts.apis.io/api2cart/llms/api2cart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/api2cart-llms.txt
- group: agent
  href: https://artifacts.apis.io/api2cart/well-known/api2cart-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/api2cart-well-known.yml
- group: other
  href: https://artifacts.apis.io/api2cart/hosts/api2cart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/api2cart-hosts.yml
- group: other
  href: https://artifacts.apis.io/api2cart/vendors/api2cart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/api2cart-vendors.yml
- group: build
  href: https://artifacts.apis.io/api2cart/packages/api2cart-packages.yml
  title: ''
  type: SDKs
  url: packages/api2cart-packages.yml
- group: build
  href: https://artifacts.apis.io/api2cart/packages/api2cart-packages.yml
  title: ''
  type: Packages
  url: packages/api2cart-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://api2cart.com/webhooks/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api2cart.com/terms-service/
- group: operate
  title: ''
  type: Support
  url: https://support.api2cart.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api2cart.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api2cart.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://api2cart.com/news/pos-api/
- group: operate
  title: ''
  type: ChangeLog
  url: https://api2cart.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://api2cart.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://api2cart.com/faqs/getting-started/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.api2cart.local.com/v1.1/webhook.create.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api2cart
- group: auth
  href: https://artifacts.apis.io/api2cart/security/api2cart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/api2cart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api2cart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api2cart.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://api2cart.com/price/
- group: company
  title: ''
  type: AboutUs
  url: https://api2cart.com/about-api2cart/
created: '2026-10-19'
description: API2Cart provides a unified eCommerce API integration solution, enabling developers to connect their applications with over 80 eCommerce platforms through a single API. It offers flexible pricing based on API call volume and store count, comprehensive documentation, SDKs, and webhook support to streamline multi‑store integrations and accelerate time‑to‑market.
image: https://d3g4zhtkdvou35.cloudfront.net/wp-content/uploads/2025/08/home-og.png
layout: provider
modified: '2026-10-19'
name: Lexy Mayko
nav: Providers
network: true
overview: 'Lexy Mayko publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Account.failed Webhooks.json API. Tagged areas include E-Commerce, Integration, Software-as-a-Service, and Marketplace.


  The Lexy Mayko catalog on APIs.io includes 1 Spectral governance ruleset.


  Lexy Mayko''s developer surface includes changelog, support, engineering blog, getting-started guide, documentation, pricing, and 23 more developer resources.'
plans:
- name: Api2Cart Plans Pricing
  plan_count: 5
  slug: api2cart-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Lexy Mayko API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: api2cart-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 44.8
    catalog_earned_first_party: 12.0
    catalog_gap: 70.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.5
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 38.1
    developer_ergonomics: 26.2
    discoverability: 56.3
    operational_transparency: 22.4
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/api2cart/api2cart-2026-11-03T120931.png
security:
- kind: domain-security
  name: Api2Cart Domain Security
  slug: api2cart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: api2cart
tags:
- E-Commerce
- Integration
- Software-as-a-Service
- Marketplace
website: https://api2cart.com/
---
