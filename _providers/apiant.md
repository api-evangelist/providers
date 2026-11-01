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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/apiant/vendors/apiant-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apiant-vendors.yml
- group: operate
  href: https://artifacts.apis.io/apiant/rate-limits/apiant-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apiant-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/apiant/authentication/apiant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apiant-authentication.yml
- group: agent
  href: https://artifacts.apis.io/apiant/llms/apiant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiant-llms.txt
- group: agent
  href: https://artifacts.apis.io/apiant/well-known/apiant-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apiant-well-known.yml
- group: other
  href: https://artifacts.apis.io/apiant/hosts/apiant-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiant-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiant.com/tos
- group: operate
  title: ''
  type: Support
  url: https://help.apiant.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiant.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.apiant.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/APIANT
- group: auth
  href: https://artifacts.apis.io/apiant/security/apiant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apiant.com/platform/
- group: docs
  title: ''
  type: APIReference
  url: https://apiant.com/platform/automation-editor
- group: start
  title: ''
  type: GettingStarted
  url: https://apiant.com/for-saas
- group: company
  title: ''
  type: Blog
  url: https://apiant.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://apiant.com/compare/
- group: start
  title: ''
  type: SignUp
  url: https://app.apiant.ai/register
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.apiant.ai/mcp
  - status: 200
    url: https://apiant.com/
  reason: partner-login
  state: gated
created: '2026-10-20'
description: APIANT provides an AI‑driven integration platform that lets users build, test, and run API integrations automatically. The service offers a visual editor, automation and assembly tools, and a marketplace of pre‑built connectors for SaaS applications like Mindbody, Shopify, and many others. Users can start for free, connect their APIs, define workflows, and deploy them to production with monitoring and error handling. APIANT targets SaaS companies, system integrators, and enterprises seeking to accelerate integration development with AI assistance.
image: https://apiant.com/images/Apiant-iso1-02.png
layout: provider
modified: '2026-10-20'
name: APIANT
nav: Providers
network: true
overview: 'APIANT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, AI, Automation, and SaaS.


  APIANT''s developer surface includes authentication, support, documentation, API reference, getting-started guide, engineering blog, pricing, and 12 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 1
  name: Apiant Rate Limits
  slug: apiant-rate-limits
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apiant Authentication
  slug: apiant-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Apiant Domain Security
  slug: apiant-domain-security
  summary_line: TLSv1.2 · DMARC
slug: apiant
tags:
- Company
- Integration
- AI
- Automation
- SaaS
website: https://apiant.com/
---
