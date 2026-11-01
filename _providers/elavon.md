---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Elavon provides a payment gateway API documented at the developer portal, but no machine‑readable OpenAPI spec was found.
  name: Elavon Payment Gateway API
  slug: elavon-payment-gateway-api
artifact_total: 4
asyncapis:
- description: ''
  name: Elavon Webhooks
  slug: elavon-webhooks
common:
- group: design
  href: https://artifacts.apis.io/elavon/asyncapi/elavon-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/elavon-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/elavon/changelog/elavon-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elavon-changelog.yml
- group: auth
  href: https://artifacts.apis.io/elavon/authentication/elavon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elavon-authentication.yml
- group: agent
  href: https://artifacts.apis.io/elavon/llms/elavon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elavon-llms.txt
- group: agent
  href: https://artifacts.apis.io/elavon/well-known/elavon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elavon-well-known.yml
- group: other
  href: https://artifacts.apis.io/elavon/hosts/elavon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elavon-hosts.yml
- group: other
  href: https://artifacts.apis.io/elavon/vendors/elavon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elavon-vendors.yml
- group: build
  href: https://artifacts.apis.io/elavon/packages/elavon-packages.yml
  title: ''
  type: SDKs
  url: packages/elavon-packages.yml
- group: build
  href: https://artifacts.apis.io/elavon/packages/elavon-packages.yml
  title: ''
  type: Packages
  url: packages/elavon-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.elavon.com/s/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elavon.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elavon
- group: auth
  href: https://artifacts.apis.io/elavon/security/elavon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elavon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elavon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.elavon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.elavon.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elavon.com/privacy-policy.html
- group: operate
  title: ''
  type: SupportCenter
  url: https://www.elavon.com/support-center.html
coverage:
  checked: '2026-10-26'
  detail: Developer portal pages are JavaScript-rendered and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://developer.elavon.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Elavon provides merchant services and payment processing solutions for businesses of all sizes, offering secure, reliable, and scalable transaction handling across multiple channels including in‑store, online, and mobile. Their platform supports a wide range of payment methods, fraud detection tools, and reporting features, helping merchants improve cash flow and customer experience. Elavon serves enterprises worldwide and integrates with numerous point‑of‑sale systems and e‑commerce platforms.
image: https://www.elavon.com/content/dam/elavon/en-us/refresh/images/solutions/cafe-payment-using-talech-register.jpg
layout: provider
modified: '2026-10-26'
name: Elavon
nav: Providers
network: true
overview: 'Elavon is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Merchant Services, FinTech, and API.


  The Elavon catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Elavon''s developer surface includes changelog, authentication, support, documentation, and 14 more developer resources.'
random_paper: 21
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 44.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Elavon Authentication
  slug: elavon-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Elavon Domain Security
  slug: elavon-domain-security
  summary_line: TLSv1.3 · DMARC
slug: elavon
tags:
- Company
- Payments
- Merchant Services
- FinTech
- API
website: https://www.elavon.com/
---
