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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/put-io/plans/put-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/put-io-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/put-io/authentication/put-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/put-io-authentication.yml
- group: agent
  href: https://artifacts.apis.io/put-io/llms/put-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/put-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/put-io/well-known/put-io-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/put-io-status-security.txt
- group: auth
  href: https://artifacts.apis.io/put-io/well-known/put-io-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/put-io-help-security.txt
- group: agent
  href: https://artifacts.apis.io/put-io/well-known/put-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/put-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/put-io/hosts/put-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/put-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/put-io/vendors/put-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/put-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/put-io/packages/put-io-packages.yml
  title: ''
  type: SDKs
  url: packages/put-io-packages.yml
- group: build
  href: https://artifacts.apis.io/put-io/packages/put-io-packages.yml
  title: ''
  type: Packages
  url: packages/put-io-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.put.io
- group: auth
  href: https://artifacts.apis.io/put-io/security/put-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/put-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://put.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.put.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://put.io/about
- group: operate
  title: ''
  type: Support
  url: https://help.put.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/putdotio
- group: commercial
  title: ''
  type: Pricing
  url: https://put.io/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://put.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://put.io/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's documented API hosts.
  evidence:
  - status: 404
    url: https://api.put.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: put.io is a cloud storage service that lets users download files from public sources such as torrents, direct links, and video sites, storing them in a personal cloud. Users can stream media on various devices, manage files via web, apps, or CLI, and automate actions with IFTTT, FTP/WebDAV, and other integrations. The service emphasizes privacy, offering private storage without public sharing, and provides a RESTful API for programmatic access to file management, transfers, and account information.
image: https://put.io/_astro/og.DFwNIy47.png
layout: provider
modified: '2026-10-28'
name: put.io
nav: Providers
network: true
overview: 'put.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Storage, Media Streaming, File Management, API, and Automation.


  put.io''s developer surface includes authentication, getting-started guide, support, pricing, and 16 more developer resources.'
plans:
- name: Put Io Plans Pricing
  plan_count: 1
  slug: put-io-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 48.2
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Put Io Authentication
  slug: put-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Put Io Domain Security
  slug: put-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: put-io
tags:
- Cloud Storage
- Media Streaming
- File Management
- API
- Automation
website: https://put.io/
---
