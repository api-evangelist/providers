---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for accessing and administrating all Chatmeter platform data including location listings, review management, social monitoring, surveys, and user administration. Uses JSON Web Token (JWT) aut
  name: Chatmeter API
  slug: chatmeter-api
artifact_total: 7
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://help.alchemer.com/help/getting-started
- group: design
  href: https://artifacts.apis.io/chatmeter/json-ld/chatmeter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chatmeter-context.jsonld
- group: operate
  href: https://artifacts.apis.io/chatmeter/lifecycle/chatmeter-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/chatmeter-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/chatmeter/hosts/chatmeter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatmeter-hosts.yml
- group: other
  href: https://artifacts.apis.io/chatmeter/vendors/chatmeter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chatmeter-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.chatmeter.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.chatmeter.com/about-us/leadership/
- group: auth
  href: https://artifacts.apis.io/chatmeter/security/chatmeter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatmeter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chatmeter.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.chatmeter.com/hc/en-us/categories/4465860037275-Chatmeter-API
- group: company
  title: ''
  type: Blog
  url: https://www.chatmeter.com/category/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chatmeter.com/pricing/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chatmeter
- group: other
  title: ''
  type: X
  url: https://x.com/chatmeter
- group: commercial
  href: https://artifacts.apis.io/chatmeter/plans/chatmeter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chatmeter-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/chatmeter/finops/chatmeter-finops.yml
  title: ''
  type: FinOps
  url: finops/chatmeter-finops.yml
- group: design
  href: https://artifacts.apis.io/chatmeter/conventions/chatmeter-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chatmeter-conventions.yml
- group: design
  href: https://artifacts.apis.io/chatmeter/lifecycle/chatmeter-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/chatmeter-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/chatmeter/conformance/chatmeter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chatmeter-conformance.yml
- group: auth
  href: https://artifacts.apis.io/chatmeter/conformance/chatmeter-conformance.yml
  title: ''
  type: Compliance
  url: conformance/chatmeter-conformance.yml
- group: design
  href: https://artifacts.apis.io/chatmeter/data-model/chatmeter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chatmeter-data-model.yml
- group: agent
  href: https://artifacts.apis.io/chatmeter/mcp/chatmeter-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/chatmeter-mcp.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chatmeter
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.alchemer.com/help/chatmeter
- group: operate
  title: ''
  type: Support
  url: https://www.chatmeter.com/contactsupport/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chatmeter.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chatmeter.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://live.chatmeter.com/
coverage:
  checked: '2026-10-20'
  detail: The Chatmeter API reference lives in a Zendesk category on support.chatmeter.com that answers 401 and redirects to a customer login, live.chatmeter.com/v5 302s to sign-in, and the public Alchemer help hub carries only end-user Chatmeter articles with no API reference.
  evidence:
  - status: 401
    url: https://support.chatmeter.com/hc/en-us/categories/4465860037275-Chatmeter-API
  - status: 302
    url: https://live.chatmeter.com/v5/openapi.json
  - status: 200
    url: https://help.alchemer.com/help/chatmeter
  reason: customer-only-docs
  state: gated
created: '2026-06-13'
description: Chatmeter is an AI-powered multi-location intelligence platform offering a REST API for managing business listings, monitoring and responding to reviews, tracking social mentions, running surveys, and benchmarking competitive performance across locations.
finops:
- has_sources: false
  method: generated
  name: Chatmeter Finops
  primary_unit: ''
  service_category: ''
  slug: chatmeter-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chatmeter.png
jsonld:
- class_count: 0
  name: Chatmeter Context
  property_count: 0
  slug: chatmeter-context
layout: provider
modified: '2026-08-13'
name: Chatmeter
nav: Providers
network: true
overview: 'Chatmeter is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Reputation Management, Local SEO, Listings Management, Review Management, and Social Media.


  The Chatmeter catalog on APIs.io includes 1 JSON-LD context.


  Chatmeter''s developer surface includes getting-started guide, documentation, engineering blog, pricing, support, and 23 more developer resources.'
plans:
- name: Chatmeter Plans Pricing
  plan_count: 3
  slug: chatmeter-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Chatmeter Rate Limits
  slug: chatmeter-rate-limits
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 54.0
    catalog_earned_first_party: 12.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 17.9
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 34.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chatmeter/chatmeter-2026-06-20T174238.png
security:
- kind: authentication
  name: Chatmeter Authentication
  slug: chatmeter-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chatmeter Domain Security
  slug: chatmeter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chatmeter
tags:
- Reputation Management
- Local SEO
- Listings Management
- Review Management
- Social Media
- Multi-Location
- Competitive Intelligence
website: https://www.chatmeter.com
---
