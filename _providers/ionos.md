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
  trial: false
  try_now: false
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
  score: 10.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cloud API for managing IONOS resources
  name: IONOS Cloud API
  slug: ionos-cloud-api
artifact_total: 4
common:
- group: build
  href: https://artifacts.apis.io/ionos/integrations/ionos-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/ionos-integration-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://price-calculator.cloud.ionos.com/
- group: other
  href: https://artifacts.apis.io/ionos/vendors/ionos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ionos-vendors.yml
- group: operate
  href: https://artifacts.apis.io/ionos/changelog/ionos-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ionos-changelog.yml
- group: auth
  href: https://artifacts.apis.io/ionos/authentication/ionos-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ionos-authentication.yml
- group: design
  href: https://artifacts.apis.io/ionos/conformance/ionos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ionos-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ionos/llms/ionos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ionos-llms.txt
- group: auth
  href: https://artifacts.apis.io/ionos/well-known/ionos-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ionos-security.txt
- group: auth
  href: https://artifacts.apis.io/ionos/well-known/ionos-partnernetwork-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ionos-partnernetwork-security.txt
- group: auth
  href: https://artifacts.apis.io/ionos/well-known/ionos-id-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ionos-id-security.txt
- group: auth
  href: https://artifacts.apis.io/ionos/well-known/ionos-feedback-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ionos-feedback-security.txt
- group: auth
  href: https://artifacts.apis.io/ionos/well-known/ionos-dcd-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ionos-dcd-security.txt
- group: auth
  href: https://artifacts.apis.io/ionos/well-known/ionos-cloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ionos-cloud-security.txt
- group: auth
  href: https://artifacts.apis.io/ionos/well-known/ionos-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ionos-api-security.txt
- group: agent
  href: https://artifacts.apis.io/ionos/well-known/ionos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ionos-well-known.yml
- group: other
  href: https://artifacts.apis.io/ionos/hosts/ionos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ionos-hosts.yml
- group: build
  href: https://artifacts.apis.io/ionos/packages/ionos-packages.yml
  title: ''
  type: SDKs
  url: packages/ionos-packages.yml
- group: build
  href: https://artifacts.apis.io/ionos/packages/ionos-packages.yml
  title: ''
  type: Packages
  url: packages/ionos-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ionos.com/terms-gtc/terms-privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.ionos.com/help/
- group: auth
  title: ''
  type: Security
  url: https://www.ionos.com/security/ev-ssl
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ionos.com/terms-gtc/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.ionos.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.ionos.com/management
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ionos.com/cloud/release-notes/previous-releases/2026/august-2026
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ionos.com/cloud/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ionos.com/cloud/ai/mcp-server/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ionos.com/
- group: auth
  href: https://artifacts.apis.io/ionos/security/ionos-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ionos-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ionos/security/ionos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ionos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ionos.com
coverage:
  checked: '2026-10-13'
  detail: The IONOS Cloud API documentation provides only HTML pages without a downloadable OpenAPI or other machine‑readable contract.
  evidence:
  - status: 404
    url: https://api.ionos.com/openapi.json
  - status: 200
    url: https://docs.ionos.com/cloud/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: IONOS is a global cloud provider offering web hosting, domain registration, cloud servers, and AI-driven services. It serves businesses of all sizes with scalable infrastructure, managed services, and a suite of tools for website creation, e‑commerce, and digital transformation. IONOS emphasizes security, performance, and customer support, providing solutions ranging from shared hosting to dedicated servers and GPU‑accelerated cloud instances.
image: https://cs-us.uicdn.net/fileadmin/og_image/logo.png
layout: provider
modified: '2026-10-13'
name: IONOS
nav: Providers
network: true
overview: 'IONOS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Hosting, Domains, and Artificial Intelligence.


  IONOS''s developer surface includes pricing, changelog, authentication, support, API reference, getting-started guide, documentation, and 24 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 29.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ionos/ionos-2026-11-03T134023.png
security:
- kind: authentication
  name: Ionos Authentication
  slug: ionos-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Ionos Domain Security
  slug: ionos-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ionos Vulnerability Disclosure
  slug: ionos-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ionos
tags:
- Company
- Cloud
- Hosting
- Domains
- Artificial Intelligence
website: https://www.ionos.com
---
