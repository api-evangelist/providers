---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: false
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.cincel.digital
  baseurl_source: declared
  description: 'CINCEL API as documented publicly: 58 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: CINCEL API
  slug: cincel-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/cincel/plans/cincel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cincel-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cincel/rules/cincel-rules.yml
  title: ''
  type: Spectral
  url: rules/cincel-rules.yml
- group: design
  href: https://artifacts.apis.io/cincel/json-ld/cincel-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cincel-context.jsonld
- group: design
  href: https://artifacts.apis.io/cincel/vocabulary/cincel-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cincel-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cincel/data-model/cincel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cincel-data-model.yml
- group: design
  href: https://artifacts.apis.io/cincel/conformance/cincel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cincel-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cincel/well-known/cincel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cincel-well-known.yml
- group: other
  href: https://artifacts.apis.io/cincel/hosts/cincel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cincel-hosts.yml
- group: other
  href: https://artifacts.apis.io/cincel/vendors/cincel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cincel-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cincel.digital/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cincel.digital/en/quick-start-guide-3-minute-initial-setup-in-cincel
- group: auth
  href: https://artifacts.apis.io/cincel/security/cincel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cincel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cincel.digital/
- group: docs
  title: ''
  type: Documentation
  url: https://help.cincel.digital/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cincel.digital/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cincel.digital/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cincel.digital/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cincel.digital/
created: '2026-10-20'
description: CINCEL provides a digital signature platform tailored for Latin America, offering electronic signing, timestamping, identity verification, and contract lifecycle management. The SaaS solution ensures legal compliance with regional regulations such as NOM151, integrates with existing systems via APIs, and supports biometric verification, OCR, and blockchain-backed timestamps. It serves sectors including sales, legal, HR, and procurement, aiming to reduce administrative overhead and accelerate digital transformation.
image: https://cdn.prod.website-files.com/6851b0a597e0ad8a6388960f/68b51691d3bd0eef7fbdb565_Cincel%20software%20de%20firma%20digital%20OG.png
json_schemas:
- name: GetV3TeamsTeamFoldersFolderDocumentsDocumentInvitesInviteRes
  property_count: 23
  slug: cincel-get-v3-teams-team-folders-folder-documents-document-invites-invite-res
- name: GetV3TeamsTeamFoldersFolderDocumentsResponse
  property_count: 22
  slug: cincel-get-v3-teams-team-folders-folder-documents-response
- name: GetV3UsersResponse
  property_count: 11
  slug: cincel-get-v3-users-response
- name: GetV3UsersUserLimitsResponse
  property_count: 10
  slug: cincel-get-v3-users-user-limits-response
- name: PatchV3TeamsTeamFoldersFolderDocumentsDocumentResponse
  property_count: 22
  slug: cincel-patch-v3-teams-team-folders-folder-documents-document-response
- name: PostV3TeamsTeamFoldersFolderDocumentsDocumentInvitesResponse
  property_count: 23
  slug: cincel-post-v3-teams-team-folders-folder-documents-document-invites-response
jsonld:
- class_count: 20
  name: Cincel Context
  property_count: 39
  slug: cincel-context
layout: provider
modified: '2026-10-20'
name: CINCEL
nav: Providers
network: true
overview: 'CINCEL is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Signature, Software-as-a-Service, Latin America, and Compliance.


  The CINCEL catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CINCEL''s developer surface includes engineering blog, getting-started guide, documentation, pricing, and 14 more developer resources.'
plans:
- name: Cincel Plans Pricing
  plan_count: 5
  slug: cincel-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: CINCEL API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: cincel-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.6
  provenance:
    conformance: first-party
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cincel/cincel-2026-11-03T124143.png
security:
- kind: domain-security
  name: Cincel Domain Security
  slug: cincel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cincel
tags:
- Company
- Digital Signature
- Software-as-a-Service
- Latin America
- Compliance
website: https://cincel.digital/
---
