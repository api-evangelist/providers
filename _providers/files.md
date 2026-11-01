---
agent_readiness:
  band: agent-aware
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
  score: 21.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Files.com provides a REST API for file orchestration and automation.
  name: Files.com API
  slug: files-com-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.files.com/compliance
- group: agent
  href: https://artifacts.apis.io/files/llms/files-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/files-llms.txt
- group: auth
  href: https://artifacts.apis.io/files/well-known/files-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/files-status-security.txt
- group: agent
  href: https://artifacts.apis.io/files/well-known/files-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/files-well-known.yml
- group: other
  href: https://artifacts.apis.io/files/hosts/files-hosts.yml
  title: ''
  type: Hosts
  url: hosts/files-hosts.yml
- group: other
  href: https://artifacts.apis.io/files/vendors/files-vendors.yml
  title: ''
  type: Vendors
  url: vendors/files-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.files.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://www.files.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.files.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.files.com/legal/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.files.com/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Files-com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.files.com/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://www.files.com/five-days-to-onboarding
- group: auth
  href: https://artifacts.apis.io/files/security/files-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/files-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/files/security/files-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/files-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://files.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.files.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.files.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.files.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.files.com/signup
coverage:
  checked: '2026-10-20'
  detail: API requires an API key, returning an authentication error.
  evidence:
  - status: 200
    url: https://api.files.com/v1/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-20'
description: Files.com provides a secure, cloud‑based managed file transfer (MFT) platform that enables businesses to move, store, and share files across a variety of protocols and integrations. The service offers features such as SFTP, FTP, AS2, automation workflows, granular permissions, audit logging, and compliance tools, serving over 4,000 organizations worldwide. Its web‑based interface and API allow for seamless integration with cloud storage providers, enterprise applications, and custom workflows, positioning Files.com as a comprehensive solution for modern file orchestration and secure data exchange.
image: https://www.files.com/opengraph-image?2bd704c175272096
layout: provider
modified: '2026-10-20'
name: Files.com
nav: Providers
network: true
overview: 'Files.com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, File Transfer, Cloud Storage, Automation, and Security.


  Files.com''s developer surface includes support, changelog, getting-started guide, documentation, pricing, engineering blog, signup flow, and 14 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 47.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Files Domain Security
  slug: files-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Files Trust Center
  slug: files-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP, GDPR
slug: files
tags:
- Company
- File Transfer
- Cloud Storage
- Automation
- Security
website: https://files.com/
---
