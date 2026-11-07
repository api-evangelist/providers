---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Fiix CMMS API provides programmatic access to maintenance management data including assets, work orders, purchase orders, parts inventory, users, and maintenance schedules. Supports CRUD operation
  name: Fiix CMMS API
  slug: fiix-cmms-api
artifact_total: 5
common:
- group: docs
  title: ''
  type: Documentation
  url: https://fiixlabs.github.io/api-documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fiixlabs
- group: company
  title: ''
  type: Blog
  url: https://fiixsoftware.com/blog/
- group: start
  title: ''
  type: Login
  url: https://fiixsoftware.com/cmms-login/
- group: commercial
  title: ''
  type: Pricing
  url: https://fiixsoftware.com/cmms/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fiixsoftware.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.fiixsoftware.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.fiixsoftware.com/site/terms
- group: design
  href: https://artifacts.apis.io/fiix-software/json-ld/fiix-software-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fiix-software-context.jsonld
- group: design
  href: https://artifacts.apis.io/fiix-software/vocabulary/fiix-software-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fiix-software-vocabulary.yml
- group: start
  href: https://artifacts.apis.io/fiix-software/sandbox/fiix-software-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fiix-software-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://fiixsoftware.com/security/
- group: auth
  href: https://artifacts.apis.io/fiix-software/authentication/fiix-software-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fiix-software-authentication.yml
- group: agent
  href: https://artifacts.apis.io/fiix-software/llms/fiix-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fiix-software-llms.txt
- group: auth
  href: https://artifacts.apis.io/fiix-software/well-known/fiix-software-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fiix-software-status-security.txt
- group: agent
  href: https://artifacts.apis.io/fiix-software/well-known/fiix-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fiix-software-well-known.yml
- group: other
  href: https://artifacts.apis.io/fiix-software/hosts/fiix-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fiix-software-hosts.yml
- group: other
  href: https://artifacts.apis.io/fiix-software/vendors/fiix-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fiix-software-vendors.yml
- group: build
  href: https://artifacts.apis.io/fiix-software/packages/fiix-software-packages.yml
  title: ''
  type: SDKs
  url: packages/fiix-software-packages.yml
- group: build
  href: https://artifacts.apis.io/fiix-software/packages/fiix-software-packages.yml
  title: ''
  type: Packages
  url: packages/fiix-software-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fiixsoftware.com/
- group: company
  title: ''
  type: Newsroom
  url: https://fiixsoftware.com/about-us/news/
- group: auth
  href: https://artifacts.apis.io/fiix-software/security/fiix-software-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fiix-software-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fiix-software/security/fiix-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fiix-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fiixsoftware.com
- group: docs
  title: ''
  type: Documentation
  url: https://fiixlabs.github.io/api-documentation/
- group: company
  title: ''
  type: Blog
  url: https://fiixsoftware.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fiixlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fiix-software
- group: commercial
  title: ''
  type: Pricing
  url: https://fiixsoftware.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.fiixsoftware.com/
coverage:
  checked: '2026-10-20'
  detail: Fiix documents its CMMS API only as an HTML guide on fiixlabs.github.io for an RPC-style JSON endpoint at https://{subdomain}.macmms.com/api reached through Java/JS client SDKs, with no OpenAPI or other contract published; api.fiixsoftware.com does not resolve.
  evidence:
  - status: 200
    url: https://fiixlabs.github.io/api-documentation/guide.html
  - status: 404
    url: https://fiixlabs.github.io/api-documentation/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-06-05'
description: Fiix (by Rockwell Automation) is a cloud-based CMMS (Computerized Maintenance Management System) platform for maintenance and reliability teams in manufacturing, facilities, and utilities. The Fiix API provides programmatic access to assets, work orders, purchase orders, parts, users, and maintenance data through custom client libraries, with integration support for ERP and industrial automation systems including FactoryTalk Optix.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fiix-software.png
jsonld:
- class_count: 0
  name: Fiix Software Context
  property_count: 9
  slug: fiix-software-context
layout: provider
modified: '2026-10-20'
name: Fiix Software
nav: Providers
network: true
overview: 'Fiix Software is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CMMS, Maintenance Management, Asset Management, Manufacturing, and Reliability.


  The Fiix Software catalog on APIs.io includes 1 JSON-LD context.


  Fiix Software''s developer surface includes documentation, engineering blog, pricing, support, sandbox, authentication, and 25 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 43.3
    catalog_earned_first_party: 0.0
    catalog_gap: 71.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 39.5
    contract_governance: 3.8
    contract_quality: 6.7
    developer_ergonomics: 54.8
    discoverability: 74.1
    operational_transparency: 21.1
  previous_composite: 38.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fiix-software/fiix-software-2026-06-20T181200.png
security:
- kind: authentication
  name: Fiix Software Authentication
  slug: fiix-software-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fiix Software Domain Security
  slug: fiix-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fiix Software Trust Center
  slug: fiix-software-trust-center
  summary_line: SOC 2, ISO 27001
slug: fiix-software
tags:
- CMMS
- Maintenance Management
- Asset Management
- Manufacturing
- Reliability
- Work Orders
- Software-as-a-Service
website: https://fiixsoftware.com
---
