---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Deck Agentic Access
  operation_count: 23
  slug: deck-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 1
apis:
- baseURL: https://sandbox.deck.co/api/v1
  baseurl_source: spec
  description: Manage connections
  name: Deck Connection API
  slug: deck-connection-api
- baseURL: https://sandbox.deck.co/api/v1
  baseurl_source: spec
  description: Endpoints related to jobs.
  name: Deck Jobs API
  slug: deck-jobs-api
- baseURL: https://sandbox.deck.co/api/v1
  baseurl_source: spec
  description: These endpoints are used by the Link widget. They can also be used for creating your own UX experience and connecting data from utility data sources.
  name: Deck Link API
  slug: deck-link-api
artifact_total: 13
asyncapis:
- description: ''
  name: Deck Webhooks
  slug: deck-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/deck/agentic-access/deck-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deck-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/deck/rate-limits/deck-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deck-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/deck/plans/deck-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deck-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deck/rules/deck-rules.yml
  title: ''
  type: Spectral
  url: rules/deck-rules.yml
- group: design
  href: https://artifacts.apis.io/deck/json-ld/deck-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deck-context.jsonld
- group: design
  href: https://artifacts.apis.io/deck/vocabulary/deck-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deck-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deck/asyncapi/deck-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/deck-webhooks.yml
- group: design
  href: https://artifacts.apis.io/deck/data-model/deck-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deck-data-model.yml
- group: design
  href: https://artifacts.apis.io/deck/conventions/deck-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deck-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.deck.co/
- group: auth
  href: https://artifacts.apis.io/deck/security/deck-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/deck-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deck/authentication/deck-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deck-authentication.yml
- group: design
  href: https://artifacts.apis.io/deck/errors/deck-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deck-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deck/conformance/deck-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deck-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deck/llms/deck-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deck-llms.txt
- group: other
  href: https://artifacts.apis.io/deck/a2a/deck-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deck-a2a.yml
- group: agent
  href: https://artifacts.apis.io/deck/well-known/deck-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deck-well-known.yml
- group: other
  href: https://artifacts.apis.io/deck/hosts/deck-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deck-hosts.yml
- group: other
  href: https://artifacts.apis.io/deck/vendors/deck-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deck-vendors.yml
- group: auth
  href: https://artifacts.apis.io/deck/security/deck-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deck-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/deck/security/deck-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deck-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deck/security/deck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deck.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://deck.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deck.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.deck.co/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.deck.co/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://deck.co/contact
- group: company
  title: ''
  type: Blog
  url: https://deck.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buildwithdeck
- group: commercial
  title: ''
  type: Pricing
  url: https://deck.co/pricing
created: '2026-10-20'
description: Deck provides a platform that enables agents to access and automate interactions with websites that lack public APIs. By securely handling user credentials, including 2FA and captchas, Deck’s agents can fetch bills, submit claims, make payments, and perform other workflows across a wide range of services such as utilities, insurance, and subscription platforms. The solution offers audit trails, compliance with SOC 2 Type II and PCI DSS, and customizable automation for enterprises seeking to integrate legacy web portals into their digital processes.
image: https://deck.co/og/og-home.png
jsonld:
- class_count: 54
  name: Deck Context
  property_count: 76
  slug: deck-context
layout: provider
modified: '2026-10-20'
name: Deck
nav: Providers
network: true
overview: 'Deck publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Connection API, Jobs API, and Link API. Tagged areas include Company, Automation, API Integration, Enterprise, and Security.


  The Deck catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Deck''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Deck Plans Pricing
  plan_count: 4
  slug: deck-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Deck Rate Limits
  slug: deck-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Deck API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: deck-rules
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 63.0
    catalog_earned_first_party: 20.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 19.7
    contract_quality: 65.8
    developer_ergonomics: 57.1
    discoverability: 48.2
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deck Authentication
  slug: deck-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Deck Domain Security
  slug: deck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deck Vulnerability Disclosure
  slug: deck-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Deck Trust Center
  slug: deck-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, FedRAMP, GDPR
slug: deck
tags:
- Company
- Automation
- API Integration
- Enterprise
- Security
website: https://deck.co/
---
