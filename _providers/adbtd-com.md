---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'adbtd API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: adbtd API
  slug: adbtd-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/adbtd-com/plans/adbtd-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adbtd-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adbtd-com/rules/adbtd-com-rules.yml
  title: ''
  type: Spectral
  url: rules/adbtd-com-rules.yml
- group: design
  href: https://artifacts.apis.io/adbtd-com/json-ld/adbtd-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adbtd-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/adbtd-com/vocabulary/adbtd-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adbtd-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/adbtd-com/data-model/adbtd-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adbtd-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/adbtd-com/security/adbtd-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/adbtd-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adbtd-com/authentication/adbtd-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adbtd-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/adbtd-com/conformance/adbtd-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adbtd-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adbtd-com/llms/adbtd-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adbtd-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/adbtd-com/well-known/adbtd-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adbtd-com-security.txt
- group: agent
  href: https://artifacts.apis.io/adbtd-com/well-known/adbtd-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adbtd-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adbtd-com/hosts/adbtd-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adbtd-com-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://adbtd.com/dashboard/webhooks
- group: start
  title: ''
  type: Login
  url: https://adbtd.com/login
- group: company
  title: ''
  type: Blog
  url: https://adbtd.com/blog/mail-tester-alternative
- group: auth
  href: https://artifacts.apis.io/adbtd-com/security/adbtd-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adbtd-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adbtd-com/security/adbtd-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adbtd-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adbtd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://adbtd.com/en/docs
- group: docs
  title: ''
  type: Documentation
  url: https://adbtd.com/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://adbtd.com/en/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://adbtd.com/signup
- group: operate
  title: ''
  type: Support
  url: https://adbtd.com/status
- group: commercial
  title: ''
  type: Pricing
  url: https://adbtd.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adbtd.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adbtd.com/en/privacy
coverage:
  checked: '2026-10-31'
  detail: Provider documentation pages contain no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract files.
  evidence:
  - status: 200
    url: https://adbtd.com/en/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: adbtd provides email infrastructure as a service, offering dedicated SMTP and IMAP servers, dedicated IP addresses, and full deliverability tools. It targets resellers and businesses needing white‑label email sending without exposing the underlying provider infrastructure. The platform includes a web dashboard, API, webhooks, and pricing plans starting at $20.99 per month, with features like domain‑level DKIM signing, bounce handling, and real‑time analytics.
image: https://adbtd.com/en/opengraph-image?e19519f2691cbcc7
json_schemas:
- name: PostApiV1MeResponse
  property_count: 1
  slug: adbtd-com-post-api-v1-me-response
- name: PostV1CheckRequest
  property_count: 6
  slug: adbtd-com-post-v1-check-request
- name: PostV1CheckResponse
  property_count: 6
  slug: adbtd-com-post-v1-check-response
- name: PostV1DomainsRequest
  property_count: 4
  slug: adbtd-com-post-v1-domains-request
- name: PostV1MailboxesIdSendRequest
  property_count: 8
  slug: adbtd-com-post-v1-mailboxes-id-send-request
- name: PostV1MailboxesRequest
  property_count: 1
  slug: adbtd-com-post-v1-mailboxes-request
jsonld:
- class_count: 18
  name: Adbtd Com Context
  property_count: 26
  slug: adbtd-com-context
layout: provider
modified: '2026-10-31'
name: adbtd
nav: Providers
network: true
overview: 'adbtd is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Infrastructure, SMTP, IMAP, Dedicated IP, and Deliverability.


  The adbtd catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  adbtd''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 19 more developer resources.'
plans:
- name: Adbtd Com Plans Pricing
  plan_count: 2
  slug: adbtd-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: adbtd API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: adbtd-com-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 65.0
    catalog_earned_first_party: 8.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 43.4
    contract_governance: 19.7
    contract_quality: 24.4
    developer_ergonomics: 34.5
    discoverability: 57.1
    operational_transparency: 14.5
  previous_composite: 43.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adbtd Com Authentication
  slug: adbtd-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adbtd Com Domain Security
  slug: adbtd-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adbtd Com Vulnerability Disclosure
  slug: adbtd-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: adbtd-com
tags:
- Email Infrastructure
- SMTP
- IMAP
- Dedicated IP
- Deliverability
- Webhook
- MCP
website: https://adbtd.com/
---
