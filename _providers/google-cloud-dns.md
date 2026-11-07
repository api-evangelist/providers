---
access_model:
  confidence: high
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
  - rate-limits
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Dns Agentic Access
  operation_count: 10
  slug: google-cloud-dns-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL: https://dns.googleapis.com
  baseurl_source: declared
  description: Manage DNS changes
  name: Google Cloud DNS Changes API
  slug: google-cloud-dns-changes-api
- baseURL: https://dns.googleapis.com
  baseurl_source: declared
  description: Manage DNS zones
  name: Google Cloud DNS ManagedZones API
  slug: google-cloud-dns-managedzones-api
- baseURL: https://dns.googleapis.com
  baseurl_source: declared
  description: Manage DNS policies
  name: Google Cloud DNS Policies API
  slug: google-cloud-dns-policies-api
- baseURL: https://dns.googleapis.com
  baseurl_source: declared
  description: Manage DNS resource record sets
  name: Google Cloud DNS Resource Record Sets API
  slug: google-cloud-dns-resource-record-sets-api
artifact_total: 25
collections:
- collection_type: postman
  name: Google Cloud DNS Changes API
  slug: postman-google-cloud-dns-changes-api
- collection_type: postman
  name: Google Cloud DNS Changes ManagedZones API
  slug: postman-google-cloud-dns-managedzones-api
- collection_type: postman
  name: Google Cloud DNS Changes Policies API
  slug: postman-google-cloud-dns-policies-api
- collection_type: postman
  name: Google Cloud DNS Changes ResourceRecordSets API
  slug: postman-google-cloud-dns-resourcerecordsets-api
- collection_type: open
  name: Google Cloud DNS API
  slug: open-dns
- collection_type: open
  name: Google Cloud DNS Changes API
  slug: open-google-cloud-dns-changes-api
- collection_type: open
  name: Google Cloud DNS Changes ManagedZones API
  slug: open-google-cloud-dns-managedzones-api
- collection_type: open
  name: Google Cloud DNS Changes Policies API
  slug: open-google-cloud-dns-policies-api
- collection_type: open
  name: Google Cloud DNS Changes ResourceRecordSets API
  slug: open-google-cloud-dns-resourcerecordsets-api
common:
- group: commercial
  href: https://artifacts.apis.io/google-cloud-dns/finops/google-cloud-dns-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-dns-finops.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-dns/rate-limits/google-cloud-dns-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-dns-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-dns/plans/google-cloud-dns-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-dns-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: other
  href: https://artifacts.apis.io/google-cloud-dns/capabilities/google-cloud-dns-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-dns-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-dns/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-dns/agentic-access/google-cloud-dns-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-dns-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-dns/security/google-cloud-dns-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-dns-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-dns/security/google-cloud-dns-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-dns-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-dns/authentication/google-cloud-dns-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-dns-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-dns/scopes/google-cloud-dns-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-dns-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/dns
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/dns/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/dns/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/dns/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/dns/docs/support
- group: design
  href: https://artifacts.apis.io/google-cloud-dns/json-ld/dns-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dns-context.jsonld
created: '2026-03-13'
description: Google Cloud DNS is a scalable, reliable, and managed authoritative Domain Name System (DNS) service running on the same infrastructure as Google. It provides low-latency, high-availability DNS serving with 100% uptime SLA, supporting both public and private DNS zones for domain name resolution.
finops:
- has_sources: true
  method: derived
  name: Google Cloud Dns Finops
  primary_unit: 1,000,000 queries
  service_category: ''
  slug: google-cloud-dns-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-dns.png
json_schemas:
- name: Google Cloud DNS Managed Zone
  property_count: 8
  slug: dns-managedzone
jsonld:
- class_count: 11
  name: Dns Context
  property_count: 3
  slug: dns-context
layout: provider
modified: '2026-05-19'
name: Google Cloud DNS
nav: Providers
network: true
overview: 'Google Cloud DNS publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Changes API, ManagedZones API, Policies API, and 1 more. Tagged areas include DNS, Domain Names, Google Cloud, Name Resolution, and Networking.


  The Google Cloud DNS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud DNS''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Google Cloud Dns Plans Pricing
  plan_count: 14
  slug: google-cloud-dns-plans-pricing
- name: Google Cloud Dns Price Estimates
  plan_count: 0
  slug: google-cloud-dns-price-estimates
random_paper: 3
rate_limits:
- limit_count: 3
  name: Google Cloud Dns Rate Limits
  slug: google-cloud-dns-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud DNS — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-dns-jsonschema-spectral-rules
scopes:
- name: Google Cloud Dns Scopes
  scope_count: 2
  slug: google-cloud-dns-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 80.7
    catalog_earned_first_party: 24.0
    catalog_gap: 34.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 58.1
    developer_ergonomics: 48.8
    discoverability: 66.1
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-cloud-dns/google-cloud-dns-2026-06-20T182106.png
security:
- kind: authentication
  name: Google Cloud Dns Authentication
  slug: google-cloud-dns-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Dns Domain Security
  slug: google-cloud-dns-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Dns Vulnerability Disclosure
  slug: google-cloud-dns-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-dns
tags:
- DNS
- Domain Names
- Google Cloud
- Name Resolution
- Networking
website: https://www.google.com/
---
