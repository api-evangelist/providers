---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Prosperstack Agentic Access
  operation_count: 29
  slug: prosperstack-agentic-access
  summary_line: 29 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: The [customer portal](https://docs.prosperstack.com/customer-portal/enabling-the-customer-portal) allows customers to self-manage their subscriptions and billing details. Creating a portal session cre
  name: ProsperStack Customer Portal API
  slug: prosperstack-customer-portal-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: An event represents a ProsperStack event that occurred in your account. These are the same events that are delivered via configured webhooks. The events endpoints can be used as an alternative or in a
  name: ProsperStack Events API
  slug: prosperstack-events-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: A flow session represents the session a cancelling subscriber took when going through the ProsperStack cancellation flow, including answers to survey questions and any offers presented or accepted.
  name: ProsperStack Flow Sessions API
  slug: prosperstack-flow-sessions-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: A flow represents a ProsperStack cancellation flow.
  name: ProsperStack Flows API
  slug: prosperstack-flows-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: An offer link is a unique URL associating a landing page offer with a particular subscription. [Learn more.](https://docs.prosperstack.com/offers/offer-links)
  name: ProsperStack Offer Links API
  slug: prosperstack-offer-links-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: An offer represents a [ProsperStack offer](https://docs.prosperstack.com/offers/creating-an-offer). Offers can be of type `coupon`, `pause_subscription`, `trial_extension`, `change_plan` or `custom`.
  name: ProsperStack Offers API
  slug: prosperstack-offers-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: A payment represents a retained payment made by a saved or deflected subscriber. Payments can be of type `saved` or `deflected`.
  name: ProsperStack Payments API
  slug: prosperstack-payments-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: A property represents a [ProsperStack custom property](https://prosperstack.com/docs/custom-properties/) defined for subscribers or subscriptions. Properties can be used to store custom data with your
  name: ProsperStack Properties API
  slug: prosperstack-properties-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: A subscriber represents a customer of your product.
  name: ProsperStack Subscribers API
  slug: prosperstack-subscribers-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: A subscription represents a subscription belonging to a customer of your product.
  name: ProsperStack Subscriptions API
  slug: prosperstack-subscriptions-api
- baseURL: https://api.prosperstack.com/v1
  baseurl_source: declared
  description: A webhook represents a [ProsperStack webhook](https://prosperstack.com/docs/webhooks/) that delivers events to a specified endpoint. Supported events are `flow_session_started` and `flow_session_compl
  name: ProsperStack Webhooks API
  slug: prosperstack-webhooks-api
artifact_total: 26
asyncapis:
- description: ''
  name: Prosperstack Webhooks
  slug: prosperstack-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/prosperstack/agentic-access/prosperstack-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/prosperstack-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/prosperstack/plans/prosperstack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prosperstack-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/prosperstack/rules/prosperstack-rules.yml
  title: ''
  type: Spectral
  url: rules/prosperstack-rules.yml
- group: design
  href: https://artifacts.apis.io/prosperstack/json-ld/prosperstack-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/prosperstack-context.jsonld
- group: design
  href: https://artifacts.apis.io/prosperstack/vocabulary/prosperstack-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/prosperstack-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/prosperstack/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/prosperstack/asyncapi/prosperstack-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/prosperstack-webhooks.yml
- group: design
  href: https://artifacts.apis.io/prosperstack/data-model/prosperstack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prosperstack-data-model.yml
- group: design
  href: https://artifacts.apis.io/prosperstack/errors/prosperstack-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prosperstack-problem-types.yml
- group: design
  href: https://artifacts.apis.io/prosperstack/conformance/prosperstack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prosperstack-conformance.yml
- group: other
  href: https://artifacts.apis.io/prosperstack/overlays/prosperstack-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/prosperstack-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/prosperstack/llms/prosperstack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prosperstack-llms.txt
- group: other
  href: https://artifacts.apis.io/prosperstack/hosts/prosperstack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prosperstack-hosts.yml
- group: other
  href: https://artifacts.apis.io/prosperstack/vendors/prosperstack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prosperstack-vendors.yml
- group: build
  href: https://artifacts.apis.io/prosperstack/packages/prosperstack-packages.yml
  title: ''
  type: SDKs
  url: packages/prosperstack-packages.yml
- group: build
  href: https://artifacts.apis.io/prosperstack/packages/prosperstack-packages.yml
  title: ''
  type: Packages
  url: packages/prosperstack-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prosperstack.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prosperstack.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://prosperstack.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://prosperstack.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.prosperstack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prosperstack
- group: auth
  href: https://artifacts.apis.io/prosperstack/authentication/prosperstack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prosperstack-authentication.yml
- group: auth
  href: https://artifacts.apis.io/prosperstack/security/prosperstack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prosperstack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prosperstack.com/
created: '2026-10-26'
description: ProsperStack provides a customer retention platform for subscription businesses, offering tools to measure, test, and optimize retention performance. The service includes analytics, automated experiments, and actionable insights to help businesses reduce churn and increase revenue.
image: https://prosperstack.com/logo.png
json_schemas:
- name: FlowSession
  property_count: 18
  slug: prosperstack-flow-session
- name: OfferLink
  property_count: 8
  slug: prosperstack-offer-link
- name: Offer
  property_count: 9
  slug: prosperstack-offer
- name: Payment
  property_count: 10
  slug: prosperstack-payment
- name: Subscriber
  property_count: 9
  slug: prosperstack-subscriber
- name: Subscription
  property_count: 9
  slug: prosperstack-subscription
jsonld:
- class_count: 50
  name: Prosperstack Context
  property_count: 77
  slug: prosperstack-context
layout: provider
modified: '2026-10-26'
name: ProsperStack
nav: Providers
network: true
overview: 'ProsperStack publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Customer Portal API, Events API, Flow Sessions API, and 8 more. Tagged areas include Company, Retention, Subscription, Analytics, and SaaS.


  The ProsperStack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ProsperStack''s developer surface includes pricing, engineering blog, documentation, authentication, and 21 more developer resources.'
plans:
- name: Prosperstack Plans Pricing
  plan_count: 3
  slug: prosperstack-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: ProsperStack API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: prosperstack-rules
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 67.0
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
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
  name: Prosperstack Authentication
  slug: prosperstack-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Prosperstack Domain Security
  slug: prosperstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: prosperstack-offer-links-create-and-retrieve
  slug: prosperstack-offer-links-create-and-retrieve
- name: prosperstack-webhook-management
  slug: prosperstack-webhook-management
slug: prosperstack
tags:
- Company
- Retention
- Subscription
- Analytics
- SaaS
website: https://prosperstack.com/
---
