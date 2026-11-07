---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MeshArc API providing clean content extraction and change tracking.
  name: MeshArc API
  slug: mesharc-api
artifact_total: 5
asyncapis:
- description: ''
  name: Mesharc Dev Webhooks
  slug: mesharc-dev-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/mesharc-dev/plans/mesharc-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mesharc-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mesharc-dev/asyncapi/mesharc-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mesharc-dev-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/mesharc-dev/changelog/mesharc-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mesharc-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/mesharc-dev/authentication/mesharc-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mesharc-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/mesharc-dev/conformance/mesharc-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mesharc-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mesharc-dev/llms/mesharc-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mesharc-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/mesharc-dev/well-known/mesharc-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mesharc-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/mesharc-dev/hosts/mesharc-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mesharc-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/mesharc-dev/vendors/mesharc-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mesharc-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mesharc.dev/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://mesharc.dev/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mesharc.dev/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://mesharc.dev/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://mesharc.dev/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mesharc.dev/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://mesharc.dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://mesharc.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://mesharc.dev/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/mesharc-dev/security/mesharc-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mesharc-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mesharc.dev/
created: '2026-10-30'
description: mesharc-dev is a developer-focused platform that provides tools and services for managing and sharing medical imaging data. The company offers secure storage, advanced metadata handling, and integration capabilities with existing healthcare systems, enabling clinicians and researchers to efficiently access and analyze imaging datasets. Their solutions emphasize compliance with healthcare regulations, scalability for large datasets, and user-friendly interfaces for both technical and non-technical users.
image: https://mesharc.dev/opengraph-image
layout: provider
modified: '2026-10-30'
name: mesharc-dev
nav: Providers
network: true
overview: 'mesharc-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Imaging, Data Management, Healthcare, and Developer Tools.


  The mesharc-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  mesharc-dev''s developer surface includes changelog, authentication, pricing, documentation, engineering blog, getting-started guide, and 14 more developer resources.'
plans:
- name: Mesharc Dev Plans Pricing
  plan_count: 5
  slug: mesharc-dev-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 45.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mesharc-dev/mesharc-dev-2026-11-03T135512.png
security:
- kind: authentication
  name: Mesharc Dev Authentication
  slug: mesharc-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mesharc Dev Domain Security
  slug: mesharc-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: mesharc-dev
tags:
- Company
- Medical Imaging
- Data Management
- Healthcare
- Developer Tools
website: https://mesharc.dev/
---
