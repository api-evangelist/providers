---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: GraphQL-based Cloud API for the Engagement Platform.
  name: Cloud API
  slug: cloud-api
- baseURL: https://api.sentiance.com
  baseurl_source: declared
  description: 'Sentiance API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Sentiance API
  slug: sentiance-api
artifact_total: 12
common:
- group: other
  href: https://artifacts.apis.io/sentiance/vendors/sentiance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sentiance-vendors.yml
- group: design
  href: https://artifacts.apis.io/sentiance/rules/sentiance-rules.yml
  title: ''
  type: Spectral
  url: rules/sentiance-rules.yml
- group: design
  href: https://artifacts.apis.io/sentiance/json-ld/sentiance-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sentiance-context.jsonld
- group: design
  href: https://artifacts.apis.io/sentiance/vocabulary/sentiance-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sentiance-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sentiance/data-model/sentiance-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sentiance-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sentiance.com/trust
- group: design
  href: https://artifacts.apis.io/sentiance/conformance/sentiance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sentiance-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sentiance/llms/sentiance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sentiance-llms.txt
- group: agent
  href: https://artifacts.apis.io/sentiance/well-known/sentiance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sentiance-well-known.yml
- group: other
  href: https://artifacts.apis.io/sentiance/hosts/sentiance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sentiance-hosts.yml
- group: build
  href: https://artifacts.apis.io/sentiance/packages/sentiance-packages.yml
  title: ''
  type: SDKs
  url: packages/sentiance-packages.yml
- group: build
  href: https://artifacts.apis.io/sentiance/packages/sentiance-packages.yml
  title: ''
  type: Packages
  url: packages/sentiance-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://sentiance.com/security
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sentiance.com/sdk/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sentiance.com/getting-started/readme
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sentiance.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sentiance
- group: auth
  href: https://artifacts.apis.io/sentiance/security/sentiance-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sentiance-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sentiance/security/sentiance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sentiance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sentiance.com/
- group: company
  title: ''
  type: Blog
  url: https://sentiance.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sentiance.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sentiance.com/sdk-license-terms
- group: operate
  title: ''
  type: Support
  url: https://sentiance.com/contact
coverage:
  checked: '2026-11-01'
  detail: Documentation provides a GraphQL endpoint but no publicly accessible machine‑readable contract.
  evidence:
  - status: 401
    url: https://api.sentiance.com/v4/gql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Sentiance delivers AI-native, on-device behavioral intelligence for mobile apps. We turn sensor data into real-time insights about how people move, drive, and live, enabling safer journeys, smarter experiences, and deeper engagement, all with privacy built in.
image: https://sentiance.com/wp-content/uploads/2026/09/sentiance-meta-1200x675-1.png
json_schemas:
- name: PostUsersAuthCodeRequest
  property_count: 1
  slug: sentiance-post-users-auth-code-request
- name: PostUsersAuthCodeResponse
  property_count: 1
  slug: sentiance-post-users-auth-code-response
jsonld:
- class_count: 2
  name: Sentiance Context
  property_count: 2
  slug: sentiance-context
layout: provider
modified: '2026-11-01'
name: Sentiance
nav: Providers
network: true
overview: 'Sentiance is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Behavioral-Intelligence, Mobile, Privacy, and On-Device.


  The Sentiance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sentiance''s developer surface includes API reference, getting-started guide, documentation, engineering blog, support, and 19 more developer resources.'
plans:
- name: Sentiance Plans Pricing
  plan_count: 0
  slug: sentiance-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Sentiance Rate Limits
  slug: sentiance-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Sentiance API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: sentiance-rules
scopes:
- name: Sentiance Scopes
  scope_count: 0
  slug: sentiance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 22.4
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 35.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sentiance Authentication
  slug: sentiance-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sentiance Domain Security
  slug: sentiance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sentiance Trust Center
  slug: sentiance-trust-center
  summary_line: ISO 27001, GDPR
slug: sentiance
tags:
- Artificial Intelligence
- Behavioral-Intelligence
- Mobile
- Privacy
- On-Device
website: https://sentiance.com/
---
