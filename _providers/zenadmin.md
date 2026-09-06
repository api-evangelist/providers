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
  band: agent-ready
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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://console.zenadmin.ai/api/external
  baseurl_source: declared
  description: The Catalog API from ZenAdmin — 3 operation(s) for catalog.
  name: ZenAdmin Catalog API
  slug: zenadmin-catalog-api
- baseURL: https://console.zenadmin.ai/api/external
  baseurl_source: declared
  description: The Context API from ZenAdmin — 1 operation(s) for context.
  name: ZenAdmin Context API
  slug: zenadmin-context-api
- baseURL: https://console.zenadmin.ai/api/external
  baseurl_source: declared
  description: The Devices API from ZenAdmin — 2 operation(s) for devices.
  name: ZenAdmin Devices API
  slug: zenadmin-devices-api
- baseURL: https://console.zenadmin.ai/api/external
  baseurl_source: declared
  description: The Employees API from ZenAdmin — 2 operation(s) for employees.
  name: ZenAdmin Employees API
  slug: zenadmin-employees-api
- baseURL: https://console.zenadmin.ai/api/external
  baseurl_source: declared
  description: The Orders API from ZenAdmin — 3 operation(s) for orders.
  name: ZenAdmin Orders API
  slug: zenadmin-orders-api
- baseURL: https://console.zenadmin.ai/api/external
  baseurl_source: declared
  description: The Webhooks API from ZenAdmin — 4 operation(s) for webhooks.
  name: ZenAdmin Webhooks API
  slug: zenadmin-webhooks-api
artifact_total: 16
asyncapis:
- description: ''
  name: Zenadmin Webhooks
  slug: zenadmin-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ZenAdmin External Catalog API
  slug: open-zenadmin-catalog-api
- collection_type: open
  name: ZenAdmin External Catalog Context API
  slug: open-zenadmin-context-api
- collection_type: open
  name: ZenAdmin External Catalog Devices API
  slug: open-zenadmin-devices-api
- collection_type: open
  name: ZenAdmin External Catalog Employees API
  slug: open-zenadmin-employees-api
- collection_type: open
  name: ZenAdmin External Catalog Orders API
  slug: open-zenadmin-orders-api
- collection_type: open
  name: ZenAdmin External Catalog Webhooks API
  slug: open-zenadmin-webhooks-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zenadmin-inventory-devices-employees.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zenadmin-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zenadmin-external-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://zenadmin.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zenadmin.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenadmin.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zenadmin.ai
- group: start
  title: ''
  type: Login
  url: https://console.zenadmin.ai
- group: company
  title: ''
  type: Blog
  url: https://www.zenadmin.ai/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zenadmin.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zenadmin.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenadmin-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenadmin-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zenadmin-well-known.yml
created: '2026-07-17'
description: 'ZenAdmin is an all-in-one IT management platform for global teams, covering the full device and employee lifecycle: IT procurement, device lifecycle management, asset and inventory tracking, mobile device management (MDM), identity and access management, SaaS/app management, IT helpdesk, and 24/7 IT support across 150+ countries. ZenAdmin publishes an External API v1 (documented at docs.zenadmin.ai) for programmatic access to devices, hardware orders, a hardware catalog, employees, and outbound webhooks. Authentication is a per-key API key sent via the x-api-key header. This profile was originally surfaced as a 500 Global portfolio company and has been enriched from the live developer documentation.'
image: https://www.zenadmin.ai/favicon.ico
layout: provider
modified: '2026-07-21'
name: ZenAdmin
nav: Providers
network: true
overview: 'ZenAdmin publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Context API, Devices API, and 3 more. Tagged areas include Company, IT Management, Device Management, Mobile Device Management, and IT Asset Management.


  The ZenAdmin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZenAdmin''s developer surface includes documentation, API reference, engineering blog, and 11 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 24.9
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 29.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenadmin/refs/heads/main/screenshots/zenadmin-2026-09-02T171553.png
security:
- kind: authentication
  name: Zenadmin Authentication
  slug: zenadmin-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Zenadmin Domain Security
  slug: zenadmin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zenadmin
tags:
- Company
- IT Management
- Device Management
- Mobile Device Management
- IT Asset Management
- SaaS Management
- Identity and Access Management
- IT Procurement
- Employee Lifecycle
- Webhook
website: https://zenadmin.ai
---
