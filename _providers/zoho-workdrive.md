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
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Zoho WorkDrive provides file management and collaboration features, but no public developer API is documented.
  name: WorkDrive API
  slug: workdrive-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/zoho-workdrive/well-known/zoho-workdrive-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zoho-workdrive-blog-security.txt
- group: auth
  title: ''
  type: Security
  url: https://bugbounty.zohocorp.com/bb/info
- group: auth
  href: https://artifacts.apis.io/zoho-workdrive/authentication/zoho-workdrive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zoho-workdrive-authentication.yml
- group: agent
  href: https://artifacts.apis.io/zoho-workdrive/llms/zoho-workdrive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zoho-workdrive-llms.txt
- group: auth
  href: https://artifacts.apis.io/zoho-workdrive/well-known/zoho-workdrive-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zoho-workdrive-security.txt
- group: agent
  href: https://artifacts.apis.io/zoho-workdrive/well-known/zoho-workdrive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zoho-workdrive-well-known.yml
- group: other
  href: https://artifacts.apis.io/zoho-workdrive/hosts/zoho-workdrive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zoho-workdrive-hosts.yml
- group: other
  href: https://artifacts.apis.io/zoho-workdrive/vendors/zoho-workdrive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zoho-workdrive-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.zoho.com/portal/en/home
- group: start
  title: ''
  type: SignUp
  url: https://www.zoho.com/workdrive/signup.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoho.com/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/workdrive/pricing.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zoho.com/developer/
- group: company
  title: ''
  type: Blog
  url: https://blog.zoho.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.zoho.com/
- group: auth
  href: https://artifacts.apis.io/zoho-workdrive/security/zoho-workdrive-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-workdrive-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zoho-workdrive/security/zoho-workdrive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zoho-workdrive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/workdrive/
created: '2026-10-27'
description: Zoho WorkDrive is an online file management and content collaboration platform designed for teams to store, share, manage, and work together on files of any size. It provides secure cloud storage, real-time collaboration, and integration with other Zoho applications, enabling businesses to streamline document workflows and improve productivity across the organization.
image: https://www.zohowebstatic.com/sites/zweb/images/ogimage/workdrive-logo.png
layout: provider
modified: '2026-10-27'
name: Zoho Docs
nav: Providers
network: true
overview: 'Zoho Docs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Storage, Collaboration, File Management, Zoho, and SaaS.


  Zoho Docs'' developer surface includes authentication, support, signup flow, pricing, engineering blog, documentation, and 12 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zoho Workdrive Authentication
  slug: zoho-workdrive-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zoho Workdrive Domain Security
  slug: zoho-workdrive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Workdrive Vulnerability Disclosure
  slug: zoho-workdrive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-workdrive
tags:
- Cloud Storage
- Collaboration
- File Management
- Zoho
- SaaS
website: https://www.zoho.com/workdrive/
---
