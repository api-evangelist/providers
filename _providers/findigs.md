---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Findigs Agentic Access
  operation_count: 8
  slug: findigs-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.client.findigs.com
  baseurl_source: declared
  description: The Applications API from Findigs — 2 operation(s) for applications.
  name: Findigs Applications API
  slug: findigs-applications-api
- baseURL: https://api.client.findigs.com
  baseurl_source: declared
  description: The Groups API from Findigs — 2 operation(s) for groups.
  name: Findigs Groups API
  slug: findigs-groups-api
- baseURL: https://api.client.findigs.com
  baseurl_source: declared
  description: The Listings API from Findigs — 2 operation(s) for listings.
  name: Findigs Listings API
  slug: findigs-listings-api
artifact_total: 16
asyncapis:
- description: ''
  name: Findigs Webhooks
  slug: findigs-webhooks
collections:
- collection_type: postman
  name: Findigs Client API
  slug: postman-findigs-client-api
- collection_type: open
  name: Findigs Client API
  slug: open-findigs-client-api
common:
- group: other
  href: https://artifacts.apis.io/findigs/capabilities/findigs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/findigs-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.findigs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getfindigs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getfindigs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getfindigs.com/
- group: build
  title: ''
  type: Postman
  url: https://docs.getfindigs.com/
- group: docs
  href: https://artifacts.apis.io/findigs/openapi/_original/findigs-client-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/findigs-client-api-openapi.yml
- group: company
  title: ''
  type: Blog
  url: https://www.findigs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Findigs
- group: operate
  title: ''
  type: Support
  url: https://www.findigs.com/renters
- group: start
  title: ''
  type: Login
  url: https://app.findigs.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.findigs.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.findigs.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.findigs.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.findigs.com/legal/responsible-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/findigs/security/findigs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/findigs-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/findigs/security/findigs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/findigs-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/findigs/authentication/findigs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/findigs-authentication.yml
- group: design
  href: https://artifacts.apis.io/findigs/conventions/findigs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/findigs-conventions.yml
- group: design
  href: https://artifacts.apis.io/findigs/conformance/findigs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/findigs-conformance.yml
- group: design
  href: https://artifacts.apis.io/findigs/errors/findigs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/findigs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/findigs/data-model/findigs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/findigs-data-model.yml
- group: design
  href: https://artifacts.apis.io/findigs/lifecycle/findigs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/findigs-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/findigs/asyncapi/findigs-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/findigs-webhooks.yml
- group: start
  href: https://artifacts.apis.io/findigs/sandbox/findigs-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/findigs-sandbox.yml
- group: build
  href: https://artifacts.apis.io/findigs/packages/findigs-packages.yml
  title: ''
  type: Packages
  url: packages/findigs-packages.yml
- group: commercial
  href: https://artifacts.apis.io/findigs/plans/findigs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/findigs-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/findigs/rate-limits/findigs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/findigs-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/findigs/examples/findigs-client-api-examples.yml
  title: ''
  type: Examples
  url: examples/findigs-client-api-examples.yml
- group: agent
  href: https://artifacts.apis.io/findigs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/findigs/agentic-access/findigs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/findigs-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/findigs/llms/findigs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/findigs-llms.txt
- group: other
  href: https://artifacts.apis.io/findigs/overlays/findigs-client-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/findigs-client-api-overlay.yaml
created: '2026-08-12'
description: Findigs is a New York City based residential real estate decisioning platform that screens rental applicants for identity, income, employment, credit, criminal history, eviction records, documents and pets, then applies automated underwriting against each operator's own written policy criteria to render a full yes/no decision on every rental application rather than handing back raw screening reports. The platform spans screening, underwriting, policy optimization and post-lease performance data, is backed by a contractual fraud guarantee, and reports a median decision time of 3.4 hours across 400K+ rental units. Findigs publishes a machine-readable Client API — an OpenAPI 3.1.0 contract served from api.client.findigs.com covering listings, applications and applicant groups, authenticated with a scoped X-API-KEY header and paired with a sandbox environment and a terse webhook event surface — though the company states the Client API is closed to new clients and existing integrators
  should contact integrations@findigs.com.
finops:
- has_sources: true
  method: derived
  name: Findigs Finops
  primary_unit: ''
  service_category: ''
  slug: findigs-finops
  template: true
image: https://www.findigs.com/opengraph-image?title=Resident%20screening%20and%20rental%20decisioning%20%7C%20Findigs&variant=home
layout: provider
modified: '2026-09-16'
name: Findigs
nav: Providers
network: true
overview: 'Findigs publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Applications API, Groups API, and Listings API. Tagged areas include rental-screening, Tenant Screening, Resident Screening, rental-application, and Underwriting.


  The Findigs catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Findigs'' developer surface includes documentation, API reference, engineering blog, support, pricing, authentication, sandbox, and 26 more developer resources.'
plans:
- name: Findigs Plans Pricing
  plan_count: 0
  slug: findigs-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Findigs Rate Limits
  slug: findigs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Findigs API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: findigs-rules
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 60.3
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 31.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/findigs/findigs-2026-08-17T080925.png
security:
- kind: authentication
  name: Findigs Authentication
  slug: findigs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Findigs Domain Security
  slug: findigs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Findigs Vulnerability Disclosure
  slug: findigs-vulnerability-disclosure
  summary_line: Hackerone · contact published
skill_count: 2
skills:
- name: Consume Findigs decision webhooks and reconcile state
  slug: findigs-consume-decision-webhooks
- name: Publish a Findigs listing and track its applications
  slug: findigs-publish-and-track-listing
slug: findigs
tags:
- rental-screening
- Tenant Screening
- Resident Screening
- rental-application
- Underwriting
- Decisioning
- Identity Verification
- Income Verification
- Credit Check
- Background Checks
- Fraud Prevention
- Property Management
- Real Estate
- PropTech
- FCRA
- Fair Housing
- Webhook
website: https://www.findigs.com/
---
