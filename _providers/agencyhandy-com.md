---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_server: false
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
  score: 44.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AgencyHandy REST API for leads, clients, orders etc.
  name: AgencyHandy API
  slug: agencyhandy-api
artifact_total: 5
asyncapis:
- description: ''
  name: Agencyhandy Com Webhooks
  slug: agencyhandy-com-webhooks
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agencyhandy.com/terms-conditions/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agencyhandy.com/getting-started/introduction
- group: commercial
  href: https://artifacts.apis.io/agencyhandy-com/plans/agencyhandy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agencyhandy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agencyhandy-com/asyncapi/agencyhandy-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agencyhandy-com-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/agencyhandy-com/authentication/agencyhandy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agencyhandy-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/agencyhandy-com/llms/agencyhandy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agencyhandy-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agencyhandy-com/a2a/agencyhandy-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agencyhandy-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agencyhandy-com/well-known/agencyhandy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agencyhandy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agencyhandy-com/hosts/agencyhandy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agencyhandy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agencyhandy-com/vendors/agencyhandy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agencyhandy-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgencyHandy
- group: auth
  href: https://artifacts.apis.io/agencyhandy-com/security/agencyhandy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agencyhandy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agencyhandy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agencyhandy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agencyhandy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agencyhandy.com/
- group: operate
  title: ''
  type: Support
  url: https://www.agencyhandy.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.agencyhandy.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agencyhandy.com/pricing-plan/
- group: start
  title: ''
  type: SignUp
  url: https://app.agencyhandy.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agencyhandy.com/privacy-policy/
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.agencyhandy.com/
coverage:
  detail: No OpenAPI/AsyncAPI/GraphQL spec found; attempts to fetch common spec URLs returned 404.
  evidence:
  - status: 404
    url: https://docs.agencyhandy.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Agency Handy provides client portal software for agencies, enabling management of clients, projects, invoices, and payments from a single platform. The service offers features such as client management, agency management, productized services, subscription management, and integrates with pricing plans, roadmaps, and a blog. It targets agencies seeking streamlined operations and offers a free trial and demo options.
image: https://dtscwu3g38rxp.cloudfront.net/wp-content/uploads/2026/06/24193910/agency-handy-og.jpg
layout: provider
modified: '2026-10-31'
name: Agency Handy
nav: Providers
network: true
overview: 'Agency Handy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agency, Software-as-a-Service, Client Portal, Project Management, and Invoicing.


  The Agency Handy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agency Handy''s developer surface includes getting-started guide, authentication, documentation, API reference, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Agencyhandy Com Plans Pricing
  plan_count: 9
  slug: agencyhandy-com-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 34.5
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 45.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agencyhandy Com Authentication
  slug: agencyhandy-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agencyhandy Com Domain Security
  slug: agencyhandy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agencyhandy-com
tags:
- Agency
- Software-as-a-Service
- Client Portal
- Project Management
- Invoicing
website: https://agencyhandy.com/
---
