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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://{tenant}.phosphorus.io
  baseurl_source: declared
  description: The Alerts API from Phosphorus — 1 operation(s) for alerts.
  name: Phosphorus Alerts API
  slug: phosphorus-alerts-api
- baseURL: https://{tenant}.phosphorus.io
  baseurl_source: declared
  description: The Device API from Phosphorus — 8 operation(s) for device.
  name: Phosphorus Device API
  slug: phosphorus-device-api
- baseURL: https://{tenant}.phosphorus.io
  baseurl_source: declared
  description: The Devices API from Phosphorus — 1 operation(s) for devices.
  name: Phosphorus Devices API
  slug: phosphorus-devices-api
- baseURL: https://{tenant}.phosphorus.io
  baseurl_source: declared
  description: The Dynamic Scans API from Phosphorus — 5 operation(s) for dynamic scans.
  name: Phosphorus Dynamic Scans API
  slug: phosphorus-dynamic-scans-api
- baseURL: https://{tenant}.phosphorus.io
  baseurl_source: declared
  description: The Providers API from Phosphorus — 5 operation(s) for providers.
  name: Phosphorus Providers API
  slug: phosphorus-providers-api
- baseURL: https://{tenant}.phosphorus.io
  baseurl_source: declared
  description: The Search API from Phosphorus — 1 operation(s) for search.
  name: Phosphorus Search API
  slug: phosphorus-search-api
- baseURL: https://{tenant}.phosphorus.io
  baseurl_source: declared
  description: The Sites API from Phosphorus — 1 operation(s) for sites.
  name: Phosphorus Sites API
  slug: phosphorus-sites-api
- baseURL: https://{tenant}.phosphorus.io
  baseurl_source: declared
  description: The Vault API from Phosphorus — 2 operation(s) for vault.
  name: Phosphorus Vault API
  slug: phosphorus-vault-api
artifact_total: 13
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/phosphorus-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://phosphorus.io/
- group: operate
  title: ''
  type: Support
  url: https://phosphorus.io/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.phosphorus.io/
- group: company
  title: ''
  type: Blog
  url: https://phosphorus.io/resource-center/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phosphorusinc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phosphorus.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phosphorus.io/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://partners.phosphorus.io/login
- group: operate
  title: ''
  type: Contact
  url: https://phosphorus.io/contact-us/
- group: build
  title: ''
  type: Packages
  url: packages/phosphorus-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/phosphorus-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/phosphorus-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phosphorus-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/phosphorus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/phosphorus-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/phosphorus-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/phosphorus-plans-pricing.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/phosphorus_stock/
created: '2026-08-26'
description: Phosphorus Cybersecurity is a Nashville, Tennessee cyber-physical systems (CPS) security company founded in 2017 by Chris Rouland, Earle Ady and Rebecca Rouland, and acquired by Dragos on 1 June 2026. Its agentless xIoT platform discovers, assesses, hardens and remediates IoT, OT, IIoT and IoMT devices across enterprise and critical infrastructure networks, automating credential rotation, firmware updates, certificate management, and vulnerability assessment at scale without additional hardware or endpoint agents. The platform exposes a customer-facing REST API (v2 and v3) described by an OpenAPI 3.0.0 contract that Phosphorus serves from each tenant instance at /api/swagger/public/swagger.json, covering devices, alerts, firmware, certificates, credentials, sites, search, dynamic scans, integration providers, and the Phosphorus Vault, authenticated with an X-API-KEY request header.
image: https://phosphorus.io/wp-content/uploads/2026/01/300x300.jpg
layout: provider
modified: '2026-08-26'
name: Phosphorus
nav: Providers
network: true
overview: 'Phosphorus publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Device API, Devices API, and 5 more. Tagged areas include Cybersecurity, xIoT Security, IoT Security, OT Security, and IoMT.


  Phosphorus'' developer surface includes support, engineering blog, and 18 more developer resources.'
plans:
- name: Phosphorus Plans Pricing
  plan_count: 0
  slug: phosphorus-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Phosphorus Rate Limits
  slug: phosphorus-rate-limits
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 48.9
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 32.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phosphorus/refs/heads/main/screenshots/phosphorus-2026-09-02T151153.png
security:
- kind: authentication
  name: Phosphorus Authentication
  slug: phosphorus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Phosphorus Domain Security
  slug: phosphorus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Phosphorus Vulnerability Disclosure
  slug: phosphorus-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: phosphorus
tags:
- Cybersecurity
- xIoT Security
- IoT Security
- OT Security
- IoMT
- Asset Discovery
- Vulnerability Management
- Firmware Management
- Certificate Management
- Credential Management
- Critical Infrastructure
- Device Management
website: https://phosphorus.io/
---
