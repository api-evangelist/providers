---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Thanks Io Agentic Access
  operation_count: 52
  slug: thanks-io-agentic-access
  summary_line: 52 operations · 33 acting
api_count: 1
apis:
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: 'Your Creatives library: saved pairings of an image template and a message template. Sending one by `creative_id` is the recommended way to send. Creatives are designed in your dashboard; these endpoin'
  name: Thanks.io Creatives Library API
  slug: thanks-io-creatives-library-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Dynamic Images API from Thanks.io — 1 operation(s) for dynamic images.
  name: Thanks.io Dynamic Images API
  slug: thanks-io-dynamic-images-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Giftcards API from Thanks.io — 2 operation(s) for giftcards.
  name: Thanks.io Giftcards API
  slug: thanks-io-giftcards-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Handwriting Styles API from Thanks.io — 1 operation(s) for handwriting styles.
  name: Thanks.io Handwriting Styles API
  slug: thanks-io-handwriting-styles-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Image Templates API from Thanks.io — 1 operation(s) for image templates.
  name: Thanks.io Image Templates API
  slug: thanks-io-image-templates-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Mailing Lists API from Thanks.io — 5 operation(s) for mailing lists.
  name: Thanks.io Mailing Lists API
  slug: thanks-io-mailing-lists-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Message Templates API from Thanks.io — 2 operation(s) for message templates.
  name: Thanks.io Message Templates API
  slug: thanks-io-message-templates-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Order Estimates API from Thanks.io — 6 operation(s) for order estimates.
  name: Thanks.io Order Estimates API
  slug: thanks-io-order-estimates-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Orders API from Thanks.io — 6 operation(s) for orders.
  name: Thanks.io Orders API
  slug: thanks-io-orders-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Recipients API from Thanks.io — 4 operation(s) for recipients.
  name: Thanks.io Recipients API
  slug: thanks-io-recipients-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Send Mailer API from Thanks.io — 6 operation(s) for send mailer.
  name: Thanks.io Send Mailer API
  slug: thanks-io-send-mailer-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Webhook Events API from Thanks.io — 0 operation(s) for webhook events.
  name: Thanks.io Webhook Events API
  slug: thanks-io-webhook-events-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Webhooks API from Thanks.io — 2 operation(s) for webhooks.
  name: Thanks.io Webhooks API
  slug: thanks-io-webhooks-api
- baseURL: https://api.thanks.io/api/v2
  baseurl_source: declared
  description: The Subaccounts API from Thanks.io — 2 operation(s) for subaccounts.
  name: Thanks.io Subaccounts API
  slug: thanks-io-subaccounts-api
artifact_total: 34
asyncapis:
- description: ''
  name: Thanks Io Webhooks
  slug: thanks-io-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/thanks-io/agentic-access/thanks-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thanks-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/thanks-io/rate-limits/thanks-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thanks-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/thanks-io/plans/thanks-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thanks-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/thanks-io/rules/thanks-io-rules.yml
  title: ''
  type: Spectral
  url: rules/thanks-io-rules.yml
- group: design
  href: https://artifacts.apis.io/thanks-io/json-ld/thanks-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/thanks-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/thanks-io/vocabulary/thanks-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thanks-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/thanks-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/thanks-io/asyncapi/thanks-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/thanks-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/thanks-io/data-model/thanks-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thanks-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://thanks.io/security
- group: auth
  href: https://artifacts.apis.io/thanks-io/authentication/thanks-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thanks-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/thanks-io/errors/thanks-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thanks-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thanks-io/conformance/thanks-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thanks-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/thanks-io/llms/thanks-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thanks-io-llms.txt
- group: other
  href: https://artifacts.apis.io/thanks-io/a2a/thanks-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/thanks-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/thanks-io/well-known/thanks-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thanks-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/thanks-io/hosts/thanks-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thanks-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/thanks-io/vendors/thanks-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thanks-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/thanks-io/packages/thanks-io-packages.yml
  title: ''
  type: SDKs
  url: packages/thanks-io-packages.yml
- group: build
  href: https://artifacts.apis.io/thanks-io/packages/thanks-io-packages.yml
  title: ''
  type: Packages
  url: packages/thanks-io-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://thanks.io/security
- group: start
  title: ''
  type: Login
  url: https://api.thanks.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thanks-io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thanks.io/quickstart
- group: auth
  href: https://artifacts.apis.io/thanks-io/security/thanks-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/thanks-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/thanks-io/security/thanks-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thanks-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thanks.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thanks.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thanks.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://thanks.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thanks.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thanks.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://help.thanks.io
created: '2026-10-28'
description: Thanks.io provides AI‑powered direct‑mail automation, letting businesses send handwritten‑style postcards, letters and gift cards via an API. Users can design mail with AI, add QR tracking, and integrate with e‑commerce platforms. Free samples and a $10 credit are offered for new accounts.
image: https://thanks.io/og-image.jpg?v=2
json_schemas:
- name: Estimate Response
  property_count: 2
  slug: thanks-io-estimate-response
- name: order-item
  property_count: 9
  slug: thanks-io-order-item
- name: recipient-create
  property_count: 31
  slug: thanks-io-recipient-create
- name: recipient
  property_count: 28
  slug: thanks-io-recipient
- name: send-mailer-base
  property_count: 18
  slug: thanks-io-send-mailer-base
- name: Send Mailer Order Submitted Response
  property_count: 40
  slug: thanks-io-send-mailer-order-response
jsonld:
- class_count: 26
  name: Thanks Io Context
  property_count: 174
  slug: thanks-io-context
layout: provider
modified: '2026-10-28'
name: Thanks.io
nav: Providers
network: true
overview: 'Thanks.io publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Creatives Library API, Dynamic Images API, Giftcards API, and 11 more. Tagged areas include Company, Artificial Intelligence, Direct Mail, and Automation.


  The Thanks.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Thanks.io''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, support, and 27 more developer resources.'
plans:
- name: Thanks Io Plans Pricing
  plan_count: 3
  slug: thanks-io-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Thanks Io Rate Limits
  slug: thanks-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Thanks.io API Rules
  rule_count: 62
  severity_counts:
    error: 45
    hint: 0
    info: 7
    warn: 10
  slug: thanks-io-rules
score:
  band: strong
  composite: 55.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 76.4
    developer_ergonomics: 37.5
    discoverability: 64.3
    operational_transparency: 47.4
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/thanks-io/thanks-io-2026-11-03T144531.png
security:
- kind: authentication
  name: Thanks Io Authentication
  slug: thanks-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Thanks Io Domain Security
  slug: thanks-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Thanks Io Trust Center
  slug: thanks-io-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 5
skills:
- name: thanks-io-create-and-retrieve-message-template
  slug: thanks-io-create-and-retrieve-message-template
- name: thanks-io-create-and-retrieve-recipient
  slug: thanks-io-create-and-retrieve-recipient
- name: thanks-io-create-sub-account
  slug: thanks-io-create-sub-account
- name: thanks-io-manage-mailing-list
  slug: thanks-io-manage-mailing-list
- name: thanks-io-manage-webhook
  slug: thanks-io-manage-webhook
slug: thanks-io
tags:
- Company
- Artificial Intelligence
- Direct Mail
- Automation
website: https://thanks.io/
---
