---
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Titus Agentic Access
  operation_count: 34
  slug: titus-agentic-access
  summary_line: 34 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Titus provides payment orchestration APIs.
  name: Titus API
  slug: titus-api
- baseURL: https://api.gotitus.com
  baseurl_source: declared
  description: The Authorizations API from Titus — 4 operation(s) for authorizations.
  name: Titus Authorizations API
  slug: titus-authorizations-api
- baseURL: https://api.gotitus.com
  baseurl_source: declared
  description: The BusinessConnections API from Titus — 4 operation(s) for businessconnections.
  name: Titus Business Connections API
  slug: titus-businessconnections-api
- baseURL: https://api.gotitus.com
  baseurl_source: declared
  description: The Checkouts API from Titus — 6 operation(s) for checkouts.
  name: Titus Checkouts API
  slug: titus-checkouts-api
- baseURL: https://api.gotitus.com
  baseurl_source: declared
  description: The Customers API from Titus — 6 operation(s) for customers.
  name: Titus Customers API
  slug: titus-customers-api
- baseURL: https://api.gotitus.com
  baseurl_source: declared
  description: The Listings API from Titus — 1 operation(s) for listings.
  name: Titus Listings API
  slug: titus-listings-api
- baseURL: https://api.gotitus.com
  baseurl_source: declared
  description: The PlatformPayouts API from Titus — 4 operation(s) for platformpayouts.
  name: Titus Platform Payouts API
  slug: titus-platformpayouts-api
- baseURL: https://api.gotitus.com
  baseurl_source: declared
  description: The Refunds API from Titus — 1 operation(s) for refunds.
  name: Titus Refunds API
  slug: titus-refunds-api
- baseURL: https://api.gotitus.com
  baseurl_source: declared
  description: The Titus API API from Titus — 0 operation(s) for titus api.
  name: Titus Titus API
  slug: titus-titus-api-api
artifact_total: 15
asyncapis:
- description: ''
  name: Titus Webhooks
  slug: titus-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/titus/agentic-access/titus-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/titus-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/titus/plans/titus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/titus-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/titus/rules/titus-rules.yml
  title: ''
  type: Spectral
  url: rules/titus-rules.yml
- group: design
  href: https://artifacts.apis.io/titus/vocabulary/titus-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/titus-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/titus/asyncapi/titus-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/titus-webhooks.yml
- group: design
  href: https://artifacts.apis.io/titus/conventions/titus-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/titus-conventions.yml
- group: design
  href: https://artifacts.apis.io/titus/conventions/titus-conventions.yml
  title: ''
  type: Conventions
  url: conventions/titus-conventions.yml
- group: design
  href: https://artifacts.apis.io/titus/errors/titus-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/titus-problem-types.yml
- group: design
  href: https://artifacts.apis.io/titus/conformance/titus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/titus-conformance.yml
- group: agent
  href: https://artifacts.apis.io/titus/llms/titus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/titus-llms.txt
- group: agent
  href: https://artifacts.apis.io/titus/well-known/titus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/titus-well-known.yml
- group: other
  href: https://artifacts.apis.io/titus/hosts/titus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/titus-hosts.yml
- group: other
  href: https://artifacts.apis.io/titus/vendors/titus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/titus-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.gotitus.com`
- group: auth
  href: https://artifacts.apis.io/titus/authentication/titus-authentication.yml
  title: ''
  type: Authentication
  url: authentication/titus-authentication.yml
- group: auth
  href: https://artifacts.apis.io/titus/security/titus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/titus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gotitus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gotitus.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gotitus.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.gotitus.com/get-started
- group: start
  title: ''
  type: Login
  url: https://www.gotitus.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gotitus.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gotitus.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.gotitus.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gotitus.com/terms
created: '2026-10-29'
description: Titus provides a flexible payment orchestration platform enabling businesses to integrate multiple payment methods, manage risk, and streamline checkout experiences. Founded with backing from Sequoia Capital, Titus offers APIs for payments, refunds, subscriptions, and reporting, targeting B2B SaaS and e‑commerce companies. The platform emphasizes developer-friendly documentation, robust security, and scalable infrastructure, supporting global merchants across various industries.
image: https://www.gotitus.com/titus-business-og-image-v2.png
layout: provider
modified: '2026-10-29'
name: Titus
nav: Providers
network: true
overview: 'Titus publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorizations API, Business Connections API, Checkouts API, and 6 more. Tagged areas include Company, Payments, FinTech, Orchestration, and API.


  The Titus catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Titus'' developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, and 19 more developer resources.'
plans:
- name: Titus Plans Pricing
  plan_count: 3
  slug: titus-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Titus API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: titus-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 53.8
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Titus Authentication
  slug: titus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Titus Domain Security
  slug: titus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: titus
tags:
- Company
- Payments
- FinTech
- Orchestration
- API
- B2B
website: https://www.gotitus.com/
---
