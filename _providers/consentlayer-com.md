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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: ConsentLayer provides a consent management API as documented in the API Reference.
  name: ConsentLayer API
  slug: consentlayer-api
- baseURL: https://api.consentlayer.com
  baseurl_source: declared
  description: 'ConsentLayer API as documented publicly: 33 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ConsentLayer API
  slug: consentlayer-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/consentlayer-com/plans/consentlayer-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consentlayer-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/consentlayer-com/rules/consentlayer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/consentlayer-com-rules.yml
- group: design
  href: https://artifacts.apis.io/consentlayer-com/json-ld/consentlayer-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/consentlayer-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/consentlayer-com/vocabulary/consentlayer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/consentlayer-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/consentlayer-com/data-model/consentlayer-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/consentlayer-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/consentlayer-com/authentication/consentlayer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/consentlayer-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/consentlayer-com/conformance/consentlayer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consentlayer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/consentlayer-com/llms/consentlayer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/consentlayer-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/consentlayer-com/well-known/consentlayer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/consentlayer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/consentlayer-com/hosts/consentlayer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/consentlayer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/consentlayer-com/vendors/consentlayer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/consentlayer-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/consentlayer-com/packages/consentlayer-com-packages.yml
  title: ''
  type: SDKs
  url: packages/consentlayer-com-packages.yml
- group: build
  href: https://artifacts.apis.io/consentlayer-com/packages/consentlayer-com-packages.yml
  title: ''
  type: Packages
  url: packages/consentlayer-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://consentlayer.com/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://app.consentlayer.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://consentlayer.com/privacy-policy/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.consentlayer.com/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.consentlayer.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/consentlayer-com/security/consentlayer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consentlayer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://consentlayer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.consentlayer.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://consentlayer.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://consentlayer.com/blog/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.consentlayer.com/mcp
  - status: 200
    url: https://consentlayer.com/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: ConsentLayer offers a cookie‑consent solution that lets web professionals manage consent across any site by prompting an AI agent such as Claude or ChatGPT. The agent creates the site entry, scans pages for trackers, categorises them, inserts a script tag, and returns a compliance score with open items. The service includes a scanner, consent logging and region‑specific rules for GDPR, CCPA and other privacy regimes, and is sold on a free‑forever plan and paid tiers for solo, studio and agency users.
image: https://consentlayer.com/wp-content/uploads/2026/07/consentlayer-og.png
json_schemas:
- name: GetSitesIdBannerResponse
  property_count: 14
  slug: consentlayer-com-get-sites-id-banner-response
- name: PatchApiV1SitesE1A2B3C4D5E67F890A1B2C3D4E5F6789BannerRespons
  property_count: 17
  slug: consentlayer-com-patch-api-v1-sites-e1-a2-b3-c4-d5-e67-f890-a1-b2-c3-d4-e5-f6789-banner-respons
- name: PatchApiV1SitesSiteidBannerResponse
  property_count: 17
  slug: consentlayer-com-patch-api-v1-sites-siteid-banner-response
- name: PatchSitesIdBannerRequest
  property_count: 8
  slug: consentlayer-com-patch-sites-id-banner-request
- name: PatchSitesIdBannerResponse
  property_count: 14
  slug: consentlayer-com-patch-sites-id-banner-response
- name: PostSitesIdScanResponse
  property_count: 8
  slug: consentlayer-com-post-sites-id-scan-response
jsonld:
- class_count: 30
  name: Consentlayer Com Context
  property_count: 40
  slug: consentlayer-com-context
layout: provider
modified: '2026-11-04'
name: ConsentLayer
nav: Providers
network: true
overview: 'ConsentLayer is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cookie Consent, AI Integration, Tracker Blocking, Privacy Compliance, and Consent Logging.


  The ConsentLayer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ConsentLayer''s developer surface includes authentication, signup flow, API reference, getting-started guide, documentation, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Consentlayer Com Plans Pricing
  plan_count: 4
  slug: consentlayer-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: ConsentLayer API Rules
  rule_count: 46
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 4
  slug: consentlayer-com-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 0.0
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Consentlayer Com Authentication
  slug: consentlayer-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Consentlayer Com Domain Security
  slug: consentlayer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: consentlayer-com
tags:
- Cookie Consent
- AI Integration
- Tracker Blocking
- Privacy Compliance
- Consent Logging
website: https://consentlayer.com/
---
