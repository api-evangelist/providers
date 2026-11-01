---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Zeotap Agentic Access
  operation_count: 3
  slug: zeotap-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- baseURL: https://api.zeotap.com
  baseurl_source: declared
  description: Zeotap CDP Profile API for writing and searching user profiles.
  name: Zeotap Profile API
  slug: zeotap-profile-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/zeotap/changelog/zeotap-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zeotap-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.zeotap.com/
- group: design
  href: https://artifacts.apis.io/zeotap/conformance/zeotap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zeotap-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zeotap/llms/zeotap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zeotap-llms.txt
- group: other
  href: https://artifacts.apis.io/zeotap/a2a/zeotap-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/zeotap-a2a.yml
- group: auth
  href: https://artifacts.apis.io/zeotap/well-known/zeotap-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zeotap-status-security.txt
- group: agent
  href: https://artifacts.apis.io/zeotap/well-known/zeotap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zeotap-well-known.yml
- group: other
  href: https://artifacts.apis.io/zeotap/hosts/zeotap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zeotap-hosts.yml
- group: other
  href: https://artifacts.apis.io/zeotap/vendors/zeotap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zeotap-vendors.yml
- group: build
  href: https://artifacts.apis.io/zeotap/packages/zeotap-packages.yml
  title: ''
  type: SDKs
  url: packages/zeotap-packages.yml
- group: build
  href: https://artifacts.apis.io/zeotap/packages/zeotap-packages.yml
  title: ''
  type: Packages
  url: packages/zeotap-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.zeotap.com`
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zeotap
- group: auth
  href: https://artifacts.apis.io/zeotap/security/zeotap-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zeotap-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zeotap/security/zeotap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zeotap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zeotap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zeotap.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zeotap.com/api-reference/profile/write-user-profile-data.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zeotap.com/articles/get-started-guide/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://zeotap.com/support/
- group: company
  title: ''
  type: Blog
  url: https://zeotap.com/about-us/newsroom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zeotap.com/legal-hub/master-services-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zeotap.com/product-privacy-policy
created: '2026-10-28'
description: Zeotap provides an AI-powered Customer Data Platform that helps enterprise brands unify first-party data, resolve identities at scale, and activate audiences across clouds and stacks. The platform includes data ingestion, identity resolution, audience building, omnichannel activation, and an AI layer (ZeoAI) for automated data mapping and predictive modeling. It emphasizes privacy, compliance, and flexible deployment options (managed or composable).
json_schemas:
- name: ProfileRequest
  property_count: 3
  slug: zeotap-profile-request
- name: ProfileResponseArray
  property_count: 0
  slug: zeotap-profile-response-array
jsonld:
- class_count: 2
  name: Zeotap Context
  property_count: 4
  slug: zeotap-context
layout: provider
modified: '2026-10-28'
name: Zeotap
nav: Providers
network: true
overview: 'Zeotap publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Profile API. Tagged areas include Company, AI, Customer-Data-Platform, Data-Integration, and Identity-Resolution.


  The Zeotap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zeotap''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, and 17 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 2
  name: Zeotap Rate Limits
  slug: zeotap-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Zeotap API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: zeotap-rules
scopes:
- name: Zeotap Scopes
  scope_count: 3
  slug: zeotap-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 55.5
    catalog_earned_first_party: 8.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 52.4
    discoverability: 67.9
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zeotap Authentication
  slug: zeotap-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zeotap Domain Security
  slug: zeotap-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Zeotap Trust Center
  slug: zeotap-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, CSA STAR
skill_count: 3
skills:
- name: delete-profiles
  slug: zeotap-delete-profiles
- name: search-profiles
  slug: zeotap-search-profiles
- name: write-profile
  slug: zeotap-write-profile
slug: zeotap
tags:
- Company
- AI
- Customer-Data-Platform
- Data-Integration
- Identity-Resolution
website: https://zeotap.com/
---
