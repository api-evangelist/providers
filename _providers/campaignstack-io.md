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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: CampaignStack API provides endpoints for managing campaigns, leads, and workflows as documented.
  name: CampaignStack API
  slug: campaignstack-api
- baseURL: https://mcp.campaignstack.io
  baseurl_source: declared
  description: 'CampaignStack API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CampaignStack API
  slug: campaignstack-io-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/campaignstack-io/plans/campaignstack-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/campaignstack-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/campaignstack-io/rules/campaignstack-io-rules.yml
  title: ''
  type: Spectral
  url: rules/campaignstack-io-rules.yml
- group: design
  href: https://artifacts.apis.io/campaignstack-io/json-ld/campaignstack-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/campaignstack-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/campaignstack-io/vocabulary/campaignstack-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/campaignstack-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/campaignstack-io/data-model/campaignstack-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/campaignstack-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/campaignstack-io/changelog/campaignstack-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/campaignstack-io-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://campaignstack.io/security
- group: auth
  href: https://artifacts.apis.io/campaignstack-io/authentication/campaignstack-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/campaignstack-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/campaignstack-io/conformance/campaignstack-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/campaignstack-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/campaignstack-io/llms/campaignstack-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/campaignstack-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/campaignstack-io/well-known/campaignstack-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campaignstack-io-security.txt
- group: agent
  href: https://artifacts.apis.io/campaignstack-io/well-known/campaignstack-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/campaignstack-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/campaignstack-io/hosts/campaignstack-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/campaignstack-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/campaignstack-io/vendors/campaignstack-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/campaignstack-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://campaignstack.io/security
- group: start
  title: ''
  type: Login
  url: https://campaignstack.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://campaignstack.io/changelog
- group: auth
  href: https://artifacts.apis.io/campaignstack-io/security/campaignstack-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/campaignstack-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/campaignstack-io/security/campaignstack-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/campaignstack-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/campaignstack-io/security/campaignstack-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/campaignstack-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://campaignstack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.campaignstack.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://campaignstack.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://campaignstack.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://campaignstack.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://campaignstack.io/help
- group: company
  title: ''
  type: Blog
  url: https://campaignstack.io/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.campaignstack.io/getting-started/introduction/
created: '2026-11-04'
description: CampaignStack provides a safety product for LinkedIn outreach, offering AI‑driven lead generation, intent detection, and automated meeting booking. It aggregates signals from LinkedIn, Apollo, Clay and CSV sources, scores leads in real time, and automates outreach workflows with content drafting, scheduling, and inbox management. The platform targets lead‑gen agencies, founders, sales operators, and consultants, offering a free tier for one LinkedIn account and paid plans for larger teams.
image: https://campaignstack.io/images/og-image.png
json_schemas:
- name: PostMcpResponse
  property_count: 5
  slug: campaignstack-io-post-mcp-response
jsonld:
- class_count: 1
  name: Campaignstack Io Context
  property_count: 5
  slug: campaignstack-io-context
layout: provider
modified: '2026-11-04'
name: CampaignStack
nav: Providers
network: true
overview: 'CampaignStack is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Outbound outreach, LinkedIn sourcing, and B2B SaaS.


  The CampaignStack catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CampaignStack''s developer surface includes changelog, authentication, documentation, pricing, support, engineering blog, getting-started guide, and 21 more developer resources.'
plans:
- name: Campaignstack Io Plans Pricing
  plan_count: 3
  slug: campaignstack-io-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: CampaignStack API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: campaignstack-io-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 19.3
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 13.2
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
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Campaignstack Io Authentication
  slug: campaignstack-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Campaignstack Io Domain Security
  slug: campaignstack-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Campaignstack Io Vulnerability Disclosure
  slug: campaignstack-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Campaignstack Io Trust Center
  slug: campaignstack-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: campaignstack-io
tags:
- Outbound outreach
- LinkedIn sourcing
- B2B SaaS
website: https://campaignstack.io/
---
