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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for PartnerPage, covering partner directory operations and webhook integrations.
  name: PartnerPage API
  slug: partnerpage-api-2
- description: 'PartnerPage API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: PartnerPage API
  slug: partnerpage-api
artifact_total: 9
asyncapis:
- description: ''
  name: Partnerpage Webhooks
  slug: partnerpage-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/partnerpage/plans/partnerpage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/partnerpage-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/partnerpage/rules/partnerpage-rules.yml
  title: ''
  type: Spectral
  url: rules/partnerpage-rules.yml
- group: design
  href: https://artifacts.apis.io/partnerpage/json-ld/partnerpage-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/partnerpage-context.jsonld
- group: design
  href: https://artifacts.apis.io/partnerpage/vocabulary/partnerpage-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/partnerpage-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/partnerpage/asyncapi/partnerpage-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/partnerpage-webhooks.yml
- group: design
  href: https://artifacts.apis.io/partnerpage/data-model/partnerpage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/partnerpage-data-model.yml
- group: auth
  href: https://artifacts.apis.io/partnerpage/authentication/partnerpage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/partnerpage-authentication.yml
- group: design
  href: https://artifacts.apis.io/partnerpage/conformance/partnerpage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/partnerpage-conformance.yml
- group: agent
  href: https://artifacts.apis.io/partnerpage/llms/partnerpage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/partnerpage-llms.txt
- group: auth
  href: https://artifacts.apis.io/partnerpage/well-known/partnerpage-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/partnerpage-support-security.txt
- group: agent
  href: https://artifacts.apis.io/partnerpage/well-known/partnerpage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/partnerpage-well-known.yml
- group: other
  href: https://artifacts.apis.io/partnerpage/hosts/partnerpage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/partnerpage-hosts.yml
- group: other
  href: https://artifacts.apis.io/partnerpage/vendors/partnerpage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/partnerpage-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.partnerpage.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PartnerPage
- group: auth
  href: https://artifacts.apis.io/partnerpage/security/partnerpage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/partnerpage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.partnerpage.io
- group: operate
  title: ''
  type: Support
  url: https://support.partnerpage.io/en/
- group: company
  title: ''
  type: Blog
  url: https://www.partnerpage.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.partnerpage.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.partnerpage.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.partnerpage.io/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.partnerpage.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: PartnerPage provides a no‑code partner directory platform that helps B2B SaaS companies showcase, manage, and grow their partner ecosystems. The solution offers customizable branding, automated partner onboarding, referral tracking, and analytics, enabling teams to launch a partner directory in days without developer effort. It serves enterprises and startups alike, integrating with existing workflows and supporting both service and tech partner listings.
image: https://framerusercontent.com/images/ccFy6klsmOXaHUaHLuKWoHrb7g4.png
json_schemas:
- name: GetApiDirectoryPublicV1AlphaDirectoriesDirectoryidEntriesPar
  property_count: 8
  slug: partnerpage-get-api-directory-public-v1-alpha-directories-directoryid-entries-par
jsonld:
- class_count: 1
  name: Partnerpage Context
  property_count: 8
  slug: partnerpage-context
layout: provider
modified: '2026-10-29'
name: PartnerPage
nav: Providers
network: true
overview: 'PartnerPage is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Partners, Directory, Software-as-a-Service, B2B, and No-Code.


  The PartnerPage catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  PartnerPage''s developer surface includes authentication, documentation, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Partnerpage Plans Pricing
  plan_count: 3
  slug: partnerpage-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: PartnerPage API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: partnerpage-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 25.4
    developer_ergonomics: 20.2
    discoverability: 64.3
    operational_transparency: 21.1
  previous_composite: 38.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/partnerpage/partnerpage-2026-11-03T140951.png
security:
- kind: authentication
  name: Partnerpage Authentication
  slug: partnerpage-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Partnerpage Domain Security
  slug: partnerpage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: partnerpage
tags:
- Partners
- Directory
- Software-as-a-Service
- B2B
- No-Code
website: https://www.partnerpage.io
---
