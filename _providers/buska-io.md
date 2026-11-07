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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Buska's public REST API for social listening and B2B lead generation.
  name: Buska Public API
  slug: buska-public-api
artifact_total: 5
asyncapis:
- description: ''
  name: Buska Io Webhooks
  slug: buska-io-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/buska-io/plans/buska-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buska-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buska-io/asyncapi/buska-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/buska-io-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/buska-io/authentication/buska-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buska-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/buska-io/conformance/buska-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buska-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buska-io/llms/buska-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buska-io-llms.txt
- group: other
  href: https://artifacts.apis.io/buska-io/a2a/buska-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/buska-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/buska-io/well-known/buska-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buska-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/buska-io/hosts/buska-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buska-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/buska-io/vendors/buska-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buska-io-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.buska.io/integrations/webhook
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buska.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buska.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buska.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.buska.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.buska.io/docs/what-is-buska
- group: docs
  title: ''
  type: Documentation
  url: https://developers.buska.io/
- group: docs
  title: ''
  type: APIReference
  url: https://www.buska.io/docs
- group: auth
  href: https://artifacts.apis.io/buska-io/security/buska-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buska-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.buska.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://buska.io/openapi.json
  - status: null
    url: https://buska.io/mcp
  - status: 401
    url: https://api.buska.io/mcp
  - status: 200
    url: https://buska.io/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Buska provides a social listening platform that monitors over 30 online platforms to detect buying intent signals. Using AI scoring, it turns social mentions into qualified B2B leads, integrates with CRM tools, and offers tiered pricing plans for businesses seeking to capture sales opportunities from social media.
image: https://www.buska.io/images/og-default.png
layout: provider
modified: '2026-11-03'
name: Buska
nav: Providers
network: true
overview: 'Buska is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Listening, Lead Generation, Artificial Intelligence, B2B, and Marketing.


  The Buska catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Buska''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 13 more developer resources.'
plans:
- name: Buska Io Plans Pricing
  plan_count: 3
  slug: buska-io-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 27.4
    discoverability: 66.1
    operational_transparency: 3.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Buska Io Authentication
  slug: buska-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Buska Io Domain Security
  slug: buska-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buska-io
tags:
- Social Listening
- Lead Generation
- Artificial Intelligence
- B2B
- Marketing
website: https://www.buska.io/
---
