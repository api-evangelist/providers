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
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/deluge/well-known/deluge-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deluge-blog-security.txt
- group: auth
  title: ''
  type: Security
  url: https://bugbounty.zohocorp.com/bb/info
- group: auth
  href: https://artifacts.apis.io/deluge/authentication/deluge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deluge-authentication.yml
- group: agent
  href: https://artifacts.apis.io/deluge/llms/deluge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deluge-llms.txt
- group: auth
  href: https://artifacts.apis.io/deluge/well-known/deluge-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deluge-security.txt
- group: auth
  href: https://artifacts.apis.io/deluge/well-known/deluge-blogsint-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deluge-blogsint-security.txt
- group: auth
  href: https://artifacts.apis.io/deluge/well-known/deluge-blogs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deluge-blogs-security.txt
- group: agent
  href: https://artifacts.apis.io/deluge/well-known/deluge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deluge-well-known.yml
- group: other
  href: https://artifacts.apis.io/deluge/hosts/deluge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deluge-hosts.yml
- group: other
  href: https://artifacts.apis.io/deluge/vendors/deluge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deluge-vendors.yml
- group: build
  href: https://artifacts.apis.io/deluge/packages/deluge-packages.yml
  title: ''
  type: SDKs
  url: packages/deluge-packages.yml
- group: build
  href: https://artifacts.apis.io/deluge/packages/deluge-packages.yml
  title: ''
  type: Packages
  url: packages/deluge-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoho.com/terms.html
- group: operate
  title: ''
  type: Support
  url: https://help.zoho.com/portal/en/home
- group: start
  title: ''
  type: SignUp
  url: https://www.zoho.com/signup.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoho.com/privacy.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zoho.com/zia/developers/
- group: company
  title: ''
  type: Blog
  url: https://blog.zoho.com/
- group: auth
  href: https://artifacts.apis.io/deluge/security/deluge-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deluge-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deluge/security/deluge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deluge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/deluge/
- group: docs
  title: ''
  type: Documentation
  url: https://deluge.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://deluge.readthedocs.io/en/latest/reference/webapi.html
coverage:
  checked: '2026-10-28'
  detail: Documentation exists at readthedocs but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://deluge.readthedocs.io/en/latest/reference/webapi.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Deluge is Zoho’s low-code scripting language and platform that enables developers to create, automate, and integrate applications across the Zoho suite. It provides a serverless environment, AI‑assisted code generation, and a rich set of built‑in functions for data access, email automation, and API integration, serving millions of developers worldwide.
image: https://zohowebstatic.com/sites/zweb/images/deluge/og/deluge-og.png
layout: provider
modified: '2026-10-28'
name: Deluge
nav: Providers
network: true
overview: 'Deluge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Low-code, Scripting, Automation, and Zoho.


  Deluge''s developer surface includes authentication, support, signup flow, engineering blog, documentation, API reference, and 17 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deluge Authentication
  slug: deluge-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Deluge Domain Security
  slug: deluge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deluge Vulnerability Disclosure
  slug: deluge-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deluge
tags:
- Company
- Low-code
- Scripting
- Automation
- Zoho
- Serverless
website: https://www.zoho.com/deluge/
---
