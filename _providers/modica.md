---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/modica/well-known/modica-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/modica-status-security.txt
- group: auth
  href: https://artifacts.apis.io/modica/well-known/modica-modicagroup-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/modica-modicagroup-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.modicagroup.com/company/reporting-a-vulnerability
- group: auth
  href: https://artifacts.apis.io/modica/well-known/modica-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/modica-www-security.txt
- group: auth
  href: https://artifacts.apis.io/modica/well-known/modica-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/modica-security.txt
- group: agent
  href: https://artifacts.apis.io/modica/well-known/modica-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/modica-well-known.yml
- group: other
  href: https://artifacts.apis.io/modica/hosts/modica-hosts.yml
  title: ''
  type: Hosts
  url: hosts/modica-hosts.yml
- group: other
  href: https://artifacts.apis.io/modica/vendors/modica-vendors.yml
  title: ''
  type: Vendors
  url: vendors/modica-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.modicagroup.com/platform/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.modicagroup.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modicagroup.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://omni.modicagroup.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.modicagroup.com/blog
- group: auth
  href: https://artifacts.apis.io/modica/security/modica-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/modica-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/modica/security/modica-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/modica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modicagroup.com/
coverage:
  checked: '2026-10-27'
  detail: The Modica website provides no discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.modicagroup.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Modica Group provides a comprehensive Communications Platform as a Service (CPaaS) for enterprises, offering a wide range of messaging channels including SMS, MMS, Email, WhatsApp Business, and voice, video, and chat capabilities. Their platform supports payments, IoT, push notifications, and two‑factor authentication, alongside robust reporting, billing, and security features. Targeted industries span logistics, retail, insurance, public sector, education, healthcare, and utilities, with solutions for alerts, customer service, marketing, and business continuity. Modica enables white‑labelled platforms for mobile network operators and delivers enterprise‑grade reliability and compliance.
layout: provider
modified: '2026-10-26'
name: Modica
nav: Providers
network: true
overview: 'Modica is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CPaaS, Communications, Enterprise, Messaging, and Platform.


  Modica''s developer surface includes support, engineering blog, and 14 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 44.6
    operational_transparency: 13.2
  previous_composite: 13.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/modica/modica-2026-11-03T135759.png
security:
- kind: domain-security
  name: Modica Domain Security
  slug: modica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Modica Vulnerability Disclosure
  slug: modica-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: modica
tags:
- CPaaS
- Communications
- Enterprise
- Messaging
- Platform
website: https://modicagroup.com/
---
