---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
  score: 19.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for sending transactional email, managing contacts and campaigns.
  name: Bottled Email API
  slug: bottled-email-api-2
- description: 'Bottled API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Bottled API
  slug: bottled-email-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/bottled-email/plans/bottled-email-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bottled-email-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bottled-email/rules/bottled-email-rules.yml
  title: ''
  type: Spectral
  url: rules/bottled-email-rules.yml
- group: design
  href: https://artifacts.apis.io/bottled-email/json-ld/bottled-email-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bottled-email-context.jsonld
- group: design
  href: https://artifacts.apis.io/bottled-email/vocabulary/bottled-email-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bottled-email-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bottled-email/data-model/bottled-email-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bottled-email-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://bottled.email/terms
- group: auth
  href: https://artifacts.apis.io/bottled-email/authentication/bottled-email-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bottled-email-authentication.yml
- group: design
  href: https://artifacts.apis.io/bottled-email/conformance/bottled-email-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bottled-email-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bottled-email/llms/bottled-email-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bottled-email-llms.txt
- group: auth
  href: https://artifacts.apis.io/bottled-email/well-known/bottled-email-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bottled-email-security.txt
- group: agent
  href: https://artifacts.apis.io/bottled-email/well-known/bottled-email-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bottled-email-well-known.yml
- group: other
  href: https://artifacts.apis.io/bottled-email/hosts/bottled-email-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bottled-email-hosts.yml
- group: other
  href: https://artifacts.apis.io/bottled-email/vendors/bottled-email-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bottled-email-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bottled.email/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bottled.email/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bottled.email/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://bottled.email/docs
- group: company
  title: ''
  type: Blog
  url: https://bottled.email/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://bottled.email/blog/setup-custom-domain-email
- group: auth
  href: https://artifacts.apis.io/bottled-email/security/bottled-email-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bottled-email-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bottled-email/security/bottled-email-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bottled-email-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bottled.email/
coverage:
  checked: '2026-11-02'
  detail: API documentation is rendered via a JavaScript SPA, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://bottled.email/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Bottled provides professional email addresses on custom domains, allowing users to cast messages across the digital ocean. The service offers free starter plans, integrates with Cloudflare email routing, and targets freelancers, developers, and businesses seeking affordable, reliable email hosting.
image: https://bottled.email/opengraph-image?ec17b6ba9621ed26
json_schemas:
- name: GetDomainsResponse
  property_count: 1
  slug: bottled-email-get-domains-response
- name: GetEmailsResponse
  property_count: 1
  slug: bottled-email-get-emails-response
- name: PostApiV1SendRequest
  property_count: 5
  slug: bottled-email-post-api-v1-send-request
- name: PostApiV1SendResponse
  property_count: 1
  slug: bottled-email-post-api-v1-send-response
- name: PostEmailsResponse
  property_count: 1
  slug: bottled-email-post-emails-response
- name: PostSendRequest
  property_count: 6
  slug: bottled-email-post-send-request
jsonld:
- class_count: 10
  name: Bottled Email Context
  property_count: 7
  slug: bottled-email-context
layout: provider
modified: '2026-11-02'
name: Bottled
nav: Providers
network: true
overview: 'Bottled is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Software-as-a-Service, Cloud, and Productivity.


  The Bottled catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bottled''s developer surface includes authentication, pricing, documentation, engineering blog, getting-started guide, and 17 more developer resources.'
plans:
- name: Bottled Email Plans Pricing
  plan_count: 3
  slug: bottled-email-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Bottled API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: bottled-email-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 22.7
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 5.3
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bottled Email Authentication
  slug: bottled-email-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bottled Email Domain Security
  slug: bottled-email-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bottled Email Vulnerability Disclosure
  slug: bottled-email-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bottled-email
tags:
- Company
- Email
- Software-as-a-Service
- Cloud
- Productivity
- CustomDomain
website: https://bottled.email/
---
