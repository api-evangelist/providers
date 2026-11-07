---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - finops
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Kustomer Agentic Access
  operation_count: 2
  slug: kustomer-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.kustomerapp.com
  baseurl_source: declared
  description: Conversation threads with customers
  name: Kustomer Conversations API
  slug: kustomer-conversations-api
- baseURL: https://api.kustomerapp.com
  baseurl_source: declared
  description: Customer records in Kustomer
  name: Kustomer Customers API
  slug: kustomer-customers-api
artifact_total: 13
asyncapis:
- description: Kustomer's outbound webhook surface delivers event notifications when resources in a Kustomer organization are created or updated. Apps subscribe to a configured array of event names in their app defi
  name: Kustomer Outbound Webhook Events
  slug: kustomer-webhooks-asyncapi
collections:
- collection_type: open
  name: Kustomer REST Conversations API
  slug: open-kustomer-conversations-api
- collection_type: open
  name: Kustomer REST Conversations Customers API
  slug: open-kustomer-customers-api
- collection_type: open
  name: Kustomer REST API
  slug: open-kustomer
common:
- group: other
  href: https://artifacts.apis.io/kustomer/vendor-facets/kustomer-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/kustomer-vendor-facets.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kustomer.com/pricing/
- group: other
  href: https://artifacts.apis.io/kustomer/capabilities/kustomer-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kustomer-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/kustomer/agentic-access/kustomer-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kustomer-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kustomer/security/kustomer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kustomer-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kustomer/authentication/kustomer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kustomer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kustomer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kustomer
- group: company
  title: ''
  type: Website
  url: https://www.kustomer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kustomer.com/kustomer-api-docs/reference
- group: commercial
  href: https://artifacts.apis.io/kustomer/plans/kustomer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kustomer-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kustomer/rate-limits/kustomer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kustomer-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kustomer/finops/kustomer-finops.yml
  title: ''
  type: FinOps
  url: finops/kustomer-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.kustomer.com/resources/blog/
created: '2026-05-08'
description: Kustomer is an AI-powered customer service CRM that unifies conversations, customer data, automation, and reporting across channels.
finops:
- has_sources: true
  method: generated
  name: Kustomer Finops
  primary_unit: ''
  service_category: Customer Support
  slug: kustomer-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kustomer.png
layout: provider
modified: '2026-05-30'
name: Kustomer
nav: Providers
network: true
overview: 'Kustomer publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Conversations API and Customers API. Tagged areas include Customer Service, CRM, Help Desk, Messaging, and Artificial Intelligence.


  The Kustomer catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kustomer''s developer surface includes pricing, authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Kustomer Plans Pricing
  plan_count: 0
  slug: kustomer-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Kustomer Rate Limits
  slug: kustomer-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Kustomer — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: kustomer-asyncapi-spectral-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 38.5
    catalog_earned_first_party: 0.0
    catalog_gap: 76.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 58.8
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/kustomer/kustomer-2026-06-20T184221.png
security:
- kind: authentication
  name: Kustomer Authentication
  slug: kustomer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kustomer Domain Security
  slug: kustomer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kustomer
tags:
- Customer Service
- CRM
- Help Desk
- Messaging
- Artificial Intelligence
- Conversational AI
website: https://www.kustomer.com/
---
