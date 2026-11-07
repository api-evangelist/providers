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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Adsense Agentic Access
  operation_count: 5
  slug: google-adsense-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://adsense.googleapis.com
  baseurl_source: declared
  description: The Accounts API from Google AdSense Management — 1 operation(s) for accounts.
  name: Google AdSense Management Accounts API
  slug: google-adsense-accounts-api
- baseURL: https://adsense.googleapis.com
  baseurl_source: declared
  description: The Adclients API from Google AdSense Management — 1 operation(s) for adclients.
  name: Google AdSense Management Adclients API
  slug: google-adsense-adclients-api
- baseURL: https://adsense.googleapis.com
  baseurl_source: declared
  description: The Payments API from Google AdSense Management — 1 operation(s) for payments.
  name: Google AdSense Management Payments API
  slug: google-adsense-payments-api
- baseURL: https://adsense.googleapis.com
  baseurl_source: declared
  description: The Reports:generate API from Google AdSense Management — 1 operation(s) for reports:generate.
  name: Google AdSense Management Reports:generate API
  slug: google-adsense-reports-generate-api
- baseURL: https://adsense.googleapis.com
  baseurl_source: declared
  description: The Ad Units API from Google AdSense Management — 1 operation(s) for ad units.
  name: Google AdSense Management Ad Units API
  slug: google-adsense-ad-units-api
artifact_total: 20
collections:
- collection_type: open
  name: Google AdSense Management Accounts API
  slug: open-google-adsense-accounts-api
- collection_type: open
  name: Google AdSense Management Accounts Adclients API
  slug: open-google-adsense-adclients-api
- collection_type: open
  name: Google AdSense Management Accounts Adunits API
  slug: open-google-adsense-adunits-api
- collection_type: open
  name: Google AdSense Management Accounts Payments API
  slug: open-google-adsense-payments-api
- collection_type: open
  name: Google AdSense Management Accounts Reports:generate API
  slug: open-google-adsense-reports-generate-api
- collection_type: open
  name: Google AdSense Management API
  slug: open-openapi
common:
- group: commercial
  href: https://artifacts.apis.io/google-adsense/plans/google-adsense-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-adsense-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-adsense/rate-limits/google-adsense-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-adsense-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-adsense/finops/google-adsense-finops.yml
  title: ''
  type: FinOps
  url: finops/google-adsense-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: agent
  href: https://artifacts.apis.io/google-adsense/agentic-access/google-adsense-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-adsense-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-adsense/security/google-adsense-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-adsense-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-adsense/security/google-adsense-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-adsense-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-adsense/authentication/google-adsense-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-adsense-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-adsense/scopes/google-adsense-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-adsense-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/google-adsense
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/adsense/management/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://support.google.com/adsense/answer/180195
- group: design
  href: https://artifacts.apis.io/google-adsense/json-ld/json-ld.yml
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Google AdSense Management API allows publishers to access their inventory and run earnings and performance reports. Publishers can manage ad clients, ad units, custom channels, URL channels, and access payment and policy information programmatically.
finops:
- has_sources: false
  method: generated
  name: Google Adsense Finops
  primary_unit: request
  service_category: API
  slug: google-adsense-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-adsense.png
layout: provider
modified: '2026-05-19'
name: Google AdSense Management
nav: Providers
network: true
overview: 'Google AdSense Management publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Adclients API, Payments API, and 2 more. Tagged areas include Ad Units, AdSense, Advertising, Monetization, and Publishers.


  The Google AdSense Management catalog on APIs.io includes 1 Spectral governance ruleset.


  Google AdSense Management''s developer surface includes authentication, getting-started guide, pricing, and 11 more developer resources.'
plans:
- name: Google Adsense Plans Pricing
  plan_count: 3
  slug: google-adsense-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Google Adsense Rate Limits
  slug: google-adsense-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google AdSense Management — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-adsense-jsonschema-spectral-rules
scopes:
- name: Google Adsense Scopes
  scope_count: 2
  slug: google-adsense-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 51.7
    catalog_earned_first_party: 0.0
    catalog_gap: 63.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 52.7
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 31.9
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
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/google-adsense/google-adsense-2026-06-20T182008.png
security:
- kind: authentication
  name: Google Adsense Authentication
  slug: google-adsense-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Adsense Domain Security
  slug: google-adsense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Adsense Vulnerability Disclosure
  slug: google-adsense-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-adsense
tags:
- Ad Units
- AdSense
- Advertising
- Monetization
- Publishers
- Reports
- Revenue
website: https://www.google.com/
---
