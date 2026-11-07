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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Ad Manager Agentic Access
  operation_count: 5
  slug: google-ad-manager-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://admanager.googleapis.com
  baseurl_source: declared
  description: The Companies API from Google Ad Manager — 1 operation(s) for companies.
  name: Google Ad Manager Companies API
  slug: google-ad-manager-companies-api
- baseURL: https://admanager.googleapis.com
  baseurl_source: declared
  description: The Networks API from Google Ad Manager — 1 operation(s) for networks.
  name: Google Ad Manager Networks API
  slug: google-ad-manager-networks-api
- baseURL: https://admanager.googleapis.com
  baseurl_source: declared
  description: The Orders API from Google Ad Manager — 1 operation(s) for orders.
  name: Google Ad Manager Orders API
  slug: google-ad-manager-orders-api
- baseURL: https://admanager.googleapis.com
  baseurl_source: declared
  description: The Reports:run API from Google Ad Manager — 1 operation(s) for reports:run.
  name: Google Ad Manager Reports:run API
  slug: google-ad-manager-reports-run-api
- baseURL: https://admanager.googleapis.com
  baseurl_source: declared
  description: The Ad Units API from Google Ad Manager — 1 operation(s) for ad units.
  name: Google Ad Manager Ad Units API
  slug: google-ad-manager-ad-units-api
artifact_total: 20
collections:
- collection_type: open
  name: Google Ad Manager adUnits API
  slug: open-google-ad-manager-adunits-api
- collection_type: open
  name: Google Ad Manager adUnits Companies API
  slug: open-google-ad-manager-companies-api
- collection_type: open
  name: Google Ad Manager adUnits Networks API
  slug: open-google-ad-manager-networks-api
- collection_type: open
  name: Google Ad Manager adUnits Orders API
  slug: open-google-ad-manager-orders-api
- collection_type: open
  name: Google Ad Manager adUnits Reports:run API
  slug: open-google-ad-manager-reports-run-api
- collection_type: open
  name: Google Ad Manager API
  slug: open-openapi
common:
- group: commercial
  href: https://artifacts.apis.io/google-ad-manager/plans/google-ad-manager-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-ad-manager-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-ad-manager/rate-limits/google-ad-manager-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-ad-manager-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-ad-manager/finops/google-ad-manager-finops.yml
  title: ''
  type: FinOps
  url: finops/google-ad-manager-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: agent
  href: https://artifacts.apis.io/google-ad-manager/agentic-access/google-ad-manager-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-ad-manager-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-ad-manager/security/google-ad-manager-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-ad-manager-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-ad-manager/security/google-ad-manager-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-ad-manager-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-ad-manager/authentication/google-ad-manager-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-ad-manager-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-ad-manager/scopes/google-ad-manager-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-ad-manager-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-ad-manager
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/ad-manager/api/beta/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://admanager.google.com/home/
- group: design
  href: https://artifacts.apis.io/google-ad-manager/json-ld/json-ld.yml
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Google Ad Manager API provides programmatic access to manage Ad Manager data including ad units, companies, orders, placements, line items, creatives, reports, and targeting. It enables publishers to automate their ad operations and integrate Ad Manager with other systems.
finops:
- has_sources: false
  method: generated
  name: Google Ad Manager Finops
  primary_unit: request
  service_category: API
  slug: google-ad-manager-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-ad-manager.png
layout: provider
modified: '2026-05-19'
name: Google Ad Manager
nav: Providers
network: true
overview: 'Google Ad Manager publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Networks API, Orders API, and 2 more. Tagged areas include Ad Manager, Ad Operations, Ad Serving, Creative, and Line Items.


  The Google Ad Manager catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Ad Manager''s developer surface includes authentication, getting-started guide, pricing, and 11 more developer resources.'
plans:
- name: Google Ad Manager Plans Pricing
  plan_count: 3
  slug: google-ad-manager-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Google Ad Manager Rate Limits
  slug: google-ad-manager-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Ad Manager — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-ad-manager-jsonschema-spectral-rules
scopes:
- name: Google Ad Manager Scopes
  scope_count: 1
  slug: google-ad-manager-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.7
    catalog_earned_first_party: 0.0
    catalog_gap: 63.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 9.8
    contract_quality: 52.7
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-ad-manager/google-ad-manager-2026-06-20T182001.png
security:
- kind: authentication
  name: Google Ad Manager Authentication
  slug: google-ad-manager-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Ad Manager Domain Security
  slug: google-ad-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Ad Manager Vulnerability Disclosure
  slug: google-ad-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-ad-manager
tags:
- Ad Manager
- Ad Operations
- Ad Serving
- Creative
- Line Items
- Order
- Publishers
- Targeting
website: https://www.google.com/
---
