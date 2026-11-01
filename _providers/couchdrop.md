---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/couchdrop/plans/couchdrop-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/couchdrop-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.couchdrop.io/privacy
- group: auth
  href: https://artifacts.apis.io/couchdrop/authentication/couchdrop-authentication.yml
  title: ''
  type: Authentication
  url: authentication/couchdrop-authentication.yml
- group: agent
  href: https://artifacts.apis.io/couchdrop/llms/couchdrop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/couchdrop-llms.txt
- group: agent
  href: https://artifacts.apis.io/couchdrop/well-known/couchdrop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/couchdrop-well-known.yml
- group: other
  href: https://artifacts.apis.io/couchdrop/hosts/couchdrop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/couchdrop-hosts.yml
- group: other
  href: https://artifacts.apis.io/couchdrop/vendors/couchdrop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/couchdrop-vendors.yml
- group: auth
  href: https://artifacts.apis.io/couchdrop/security/couchdrop-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/couchdrop-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/couchdrop/security/couchdrop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/couchdrop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.couchdrop.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.couchdrop.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.couchdrop.io/
- group: docs
  title: ''
  type: APIReference
  url: https://www.couchdrop.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.couchdrop.io/
- group: operate
  title: ''
  type: Support
  url: https://www.couchdrop.io/support?hsLang=en
- group: company
  title: ''
  type: Blog
  url: https://www.couchdrop.io/updates
- group: commercial
  title: ''
  type: Pricing
  url: https://www.couchdrop.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.couchdrop.io/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.couchdrop.io/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/couchdrop/workspace
coverage:
  checked: '2026-10-19'
  detail: Docs are public HTML without a machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://docs.couchdrop.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Couchdrop provides cloud-based SFTP, FTP, and managed file transfer solutions, enabling businesses to send and receive files securely across platforms. Their platform offers file automation workflows without code, integration with popular services, transfer shield for data loss prevention, and support for webhooks, AS2 messaging, and B2B connections. Targeted at data, HR, support, and engineering teams, Couchdrop aims to simplify secure data exchange and integration in the cloud.
image: https://www.couchdrop.io/hubfs/Feaure%20Image%20-%20Logo%20with%20text-2.png
layout: provider
modified: '2026-10-19'
name: Couchdrop
nav: Providers
network: true
overview: 'Couchdrop is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include File Transfer, SFTP, Automation, Integration, and Cloud.


  Couchdrop''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Couchdrop Plans Pricing
  plan_count: 1
  slug: couchdrop-plans-pricing
random_paper: 7
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Couchdrop Authentication
  slug: couchdrop-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Couchdrop Domain Security
  slug: couchdrop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Couchdrop Trust Center
  slug: couchdrop-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: couchdrop
tags:
- File Transfer
- SFTP
- Automation
- Integration
- Cloud
website: https://www.couchdrop.io/
---
