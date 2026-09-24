---
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/less-annoying-crm/refs/heads/main/plans/less-annoying-crm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/less-annoying-crm-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/less-annoying-crm/refs/heads/main/changelog/less-annoying-crm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/less-annoying-crm-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/less-annoying-crm/refs/heads/main/authentication/less-annoying-crm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/less-annoying-crm-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/less-annoying-crm/refs/heads/main/llms/less-annoying-crm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/less-annoying-crm-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/less-annoying-crm/refs/heads/main/hosts/less-annoying-crm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/less-annoying-crm-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/less-annoying-crm/refs/heads/main/vendors/less-annoying-crm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/less-annoying-crm-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lessannoyingcrm.com/
- group: auth
  title: ''
  type: Security
  url: https://lessannoyingcrm.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://lessannoyingcrm.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/less-annoying-crm/refs/heads/main/security/less-annoying-crm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/less-annoying-crm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lessannoyingcrm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://account.lessannoyingcrm.com/api_docs/v2/Getting_Started/Introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://lessannoyingcrm.com/tour
- group: commercial
  title: ''
  type: Pricing
  url: https://lessannoyingcrm.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://lessannoyingcrm.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://lessannoyingcrm.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lessannoyingcrm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lessannoyingcrm.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://account.lessannoyingcrm.com/signup
- group: start
  title: ''
  type: Login
  url: https://account.lessannoyingcrm.com/login
coverage:
  checked: 2026-09-22
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on api.lessannoyingcrm.com.
  evidence:
  - status: 404
    url: https://api.lessannoyingcrm.com/openapi.json
  - status: 404
    url: https://api.lessannoyingcrm.com/openapi.yaml
  - status: 404
    url: https://api.lessannoyingcrm.com/swagger.json
  - status: 404
    url: https://api.lessannoyingcrm.com/v1/openapi.json
  - status: 404
    url: https://api.lessannoyingcrm.com/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-22'
description: Less Annoying CRM provides simple, affordable contact management software tailored for small businesses. Founded in 2009, it remains family‑owned and self‑funded, offering a single‑price tier with no contracts, upgrades, or hidden fees. The platform includes task reminders, email syncing, calendar integration, and collaborative notes, all without the complexity of enterprise CRMs. Users can start a free trial, view live demos, and access extensive resources such as pricing, product tours, integrations, testimonials, blog posts, and a help center. The service emphasizes data ownership, easy export to Excel, and responsive human support, positioning itself as a straightforward alternative to spreadsheet‑based tracking and larger CRM solutions.
image: https://account.lessannoyingcrm.com/i/social_logo.png
layout: provider
modified: '2026-09-22'
name: Less Annoying CRM
nav: Providers
network: true
overview: 'Less Annoying CRM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Small Business, Contact Management, and Software-as-a-Service.


  Less Annoying CRM''s developer surface includes changelog, authentication, documentation, getting-started guide, pricing, engineering blog, support, and 13 more developer resources.'
plans:
- name: Less Annoying Crm Plans Pricing
  plan_count: 1
  slug: less-annoying-crm-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.4
    operational_transparency: 42.1
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Less Annoying Crm Authentication
  slug: less-annoying-crm-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Less Annoying Crm Domain Security
  slug: less-annoying-crm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: less-annoying-crm
tags:
- Company
- CRM
- Small Business
- Contact Management
- Software-as-a-Service
website: https://lessannoyingcrm.com/
---
