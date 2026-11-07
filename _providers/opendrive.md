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
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Programmatic access to OpenDrive storage, sharing, and file management.
  name: OpenDrive API
  slug: opendrive-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/opendrive/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.opendrive.com/security
- group: auth
  href: https://artifacts.apis.io/opendrive/authentication/opendrive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opendrive-authentication.yml
- group: design
  href: https://artifacts.apis.io/opendrive/lifecycle/opendrive-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opendrive-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/opendrive/conformance/opendrive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opendrive-conformance.yml
- group: other
  href: https://artifacts.apis.io/opendrive/overlays/opendrive-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/opendrive-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/opendrive/hosts/opendrive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opendrive-hosts.yml
- group: other
  href: https://artifacts.apis.io/opendrive/vendors/opendrive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opendrive-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.opendrive.com/wp-content/uploads/releases/api-samples/api-samples.zip
- group: auth
  href: https://artifacts.apis.io/opendrive/security/opendrive-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/opendrive-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/opendrive/security/opendrive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opendrive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendrive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.opendrive.com/api/explorer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.opendrive.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.opendrive.com/api
- group: company
  title: ''
  type: Blog
  url: https://www.opendrive.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.opendrive.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opendrive.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opendrive.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opendrive.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.opendrive.com/signup
created: '2026-10-28'
description: OpenDrive provides cloud‑based storage, backup, and collaboration services for personal, business, and enterprise users. The platform offers file synchronization across devices, secure sharing, note‑taking, task management, and an extensible API that enables developers to integrate storage capabilities into their applications. Founded in 2007, OpenDrive serves millions of users worldwide with features such as versioning, encryption, and automated backup scheduling.
image: https://www.opendrive.com/favicon.ico
layout: provider
modified: '2026-10-28'
name: OpenDrive
nav: Providers
network: true
overview: 'OpenDrive is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Storage, Backup, File Sync, and Collaboration.


  OpenDrive''s developer surface includes authentication, changelog, documentation, API reference, engineering blog, support, pricing, and 14 more developer resources.'
plans:
- name: Opendrive Plans Pricing
  plan_count: 4
  slug: opendrive-plans-pricing
random_paper: 12
scopes:
- name: Opendrive Scopes
  scope_count: 0
  slug: opendrive-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.0
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 43.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/opendrive/opendrive-2026-11-03T140636.png
security:
- kind: authentication
  name: Opendrive Authentication
  slug: opendrive-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Opendrive Domain Security
  slug: opendrive-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Opendrive Trust Center
  slug: opendrive-trust-center
  summary_line: SOC 2, HIPAA
skill_count: 2
skills:
- name: opendrive-branding
  slug: opendrive-branding
- name: file-management
  slug: opendrive-file-management
slug: opendrive
tags:
- Cloud Storage
- Backup
- File Sync
- Collaboration
website: https://opendrive.com/
---
