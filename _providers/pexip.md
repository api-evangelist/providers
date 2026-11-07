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
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/pexip/well-known/pexip-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pexip-status-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.pexip.com/trust-center
- group: auth
  title: ''
  type: Security
  url: https://www.pexip.com/trust-center/vulnerability-disclosure
- group: agent
  href: https://artifacts.apis.io/pexip/llms/pexip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pexip-llms.txt
- group: auth
  href: https://artifacts.apis.io/pexip/well-known/pexip-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pexip-security.txt
- group: auth
  href: https://artifacts.apis.io/pexip/well-known/pexip-pexip-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pexip-pexip-security.txt
- group: agent
  href: https://artifacts.apis.io/pexip/well-known/pexip-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pexip-well-known.yml
- group: other
  href: https://artifacts.apis.io/pexip/hosts/pexip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pexip-hosts.yml
- group: other
  href: https://artifacts.apis.io/pexip/vendors/pexip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pexip-vendors.yml
- group: build
  href: https://artifacts.apis.io/pexip/packages/pexip-packages.yml
  title: ''
  type: SDKs
  url: packages/pexip-packages.yml
- group: build
  href: https://artifacts.apis.io/pexip/packages/pexip-packages.yml
  title: ''
  type: Packages
  url: packages/pexip-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pexip.com/?utm_source=website&utm_medium=menu
- group: company
  title: ''
  type: Newsroom
  url: https://www.pexip.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://help.pexip.com/service/home-starting.htm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pexip
- group: auth
  href: https://artifacts.apis.io/pexip/security/pexip-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pexip-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pexip/security/pexip-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pexip-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pexip/security/pexip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pexip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pexip.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.pexip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pexip.com/
- group: operate
  title: ''
  type: Support
  url: https://support.pexip.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pexip.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pexip.com/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pexip.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pexip.com/privacy
coverage:
  checked: '2026-10-27'
  detail: Provider documentation is HTML only with no OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications.
  evidence:
  - status: 404
    url: https://developer.pexip.com/openapi.json
  - status: 404
    url: https://developer.pexip.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Pexip provides a secure video communications platform enabling organizations to host, join, and manage virtual meetings across any device or conference system. Their solutions include Pexip Connect, a cloud‑based service that integrates with Microsoft Teams, Zoom, Google Meet, and SIP/H.323 endpoints, offering interoperability, recording, and AI‑enhanced features. Pexip serves sectors such as enterprise, government, healthcare, and education, delivering scalable, high‑quality video conferencing with robust security and compliance controls.
layout: provider
modified: '2026-10-26'
name: Pexip
nav: Providers
network: true
overview: 'Pexip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Communications, Cloud, Security, and Enterprise.


  Pexip''s developer surface includes getting-started guide, documentation, support, engineering blog, pricing, and 21 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 52.7
    operational_transparency: 15.8
  previous_composite: 29.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pexip/pexip-2026-11-03T141142.png
security:
- kind: domain-security
  name: Pexip Domain Security
  slug: pexip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pexip Vulnerability Disclosure
  slug: pexip-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Pexip Trust Center
  slug: pexip-trust-center
  summary_line: ISO 27001, GDPR
slug: pexip
tags:
- Video
- Communications
- Cloud
- Security
- Enterprise
website: https://pexip.com/
---
