---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  - '{''url'': ''https://www.apperio.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.persuit.com/apperio-transfer — a different registrable domain (apperio.com -> persuit.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Apperio Agentic Access
  operation_count: 30
  slug: apperio-agentic-access
  summary_line: 30 operations · 16 acting
api_count: 1
apis:
- baseURL: https://app.apperio.com/api/v1
  baseurl_source: declared
  description: A set of non resource based endpoints that power various components within Apperio. These endpoints primarily support discovery and data investigation.
  name: Apperio Analytics API
  slug: apperio-analytics-api
- baseURL: https://app.apperio.com/api/v1
  baseurl_source: declared
  description: The e-billing endpoints provide access to the e-billing invoices in Apperio. They allow you to retrieve information about the invoices and the approval workflow, and also to approve and reject invoice
  name: Apperio E-billing API
  slug: apperio-e-billing-api
- baseURL: https://app.apperio.com/api/v1
  baseurl_source: declared
  description: 'The filter endpoints provide resource discovery in Apperio. This has two basic mechanisms. Firstly there are the resource discovery endpoints. These are: * `/api/v1/filter/engagements/` * `/api/v1/fil'
  name: Apperio Filter API
  slug: apperio-filter-api
- baseURL: https://app.apperio.com/api/v1
  baseurl_source: declared
  description: A set of endpoints returning information about a specific matter.
  name: Apperio Matter information API
  slug: apperio-matter-information-api
- baseURL: https://app.apperio.com/api/v1
  baseurl_source: declared
  description: The users endpoints allow you to manage your API tokens. Tokens are used to authenticate requests to the Apperio API. You can list your existing tokens, delete tokens that are no longer needed, and ac
  name: Apperio Users API
  slug: apperio-users-api
artifact_total: 18
collections:
- collection_type: open
  name: Apperio API Documentation Analytics API
  slug: open-apperio-analytics-api
- collection_type: open
  name: Apperio API Documentation Analytics E-billing API
  slug: open-apperio-e-billing-api
- collection_type: open
  name: Apperio API Documentation Analytics Filter API
  slug: open-apperio-filter-api
- collection_type: open
  name: Apperio API Documentation Analytics Matter information API
  slug: open-apperio-matter-information-api
- collection_type: open
  name: Apperio API Documentation Analytics Users API
  slug: open-apperio-users-api
common:
- group: other
  href: https://artifacts.apis.io/apperio/capabilities/apperio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/apperio-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/apperio/overlays/apperio-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apperio-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apperio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.apperio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.apperio.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.apperio.com/
- group: auth
  href: https://artifacts.apis.io/apperio/authentication/apperio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apperio-authentication.yml
- group: design
  href: https://artifacts.apis.io/apperio/conventions/apperio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apperio-conventions.yml
- group: operate
  href: https://artifacts.apis.io/apperio/rate-limits/apperio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apperio-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/apperio/errors/apperio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apperio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apperio/lifecycle/apperio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apperio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.apperio.com/
- group: operate
  href: https://artifacts.apis.io/apperio/changelog/apperio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apperio-changelog.yml
- group: start
  href: https://artifacts.apis.io/apperio/sandbox/apperio-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/apperio-sandbox.yml
- group: design
  href: https://artifacts.apis.io/apperio/data-model/apperio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apperio-data-model.yml
- group: design
  href: https://artifacts.apis.io/apperio/conformance/apperio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apperio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.apperio.com/information-security
- group: auth
  href: https://artifacts.apis.io/apperio/security/apperio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/apperio-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/apperio/security/apperio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apperio-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/apperio/mcp/apperio-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/apperio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/apperio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/apperio/agentic-access/apperio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apperio-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/apperio/llms/apperio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apperio-llms.txt
- group: start
  title: ''
  type: Login
  url: https://app.apperio.com/login/
- group: operate
  title: ''
  type: Support
  url: https://www.apperio.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.apperio.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apperio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apperio.com/privacy-notice
- group: company
  title: ''
  type: Website
  url: https://www.apperio.com
created: '2026-07-17'
description: Apperio is a legal spend management and matter management platform for in-house legal teams and the law firms they work with. It connects directly to law-firm time-and-billing systems to give continuous, real-time visibility into billed and unbilled ("work in progress") legal spend, benchmarking to negotiate rates, and AI-assisted e-billing review against Outside Counsel Guidelines. The Apperio REST API exposes the same secure data that powers the platform's analytics — legal-spend analytics, matter (engagement) and invoice discovery, matter tagging, and e-billing invoice approval workflows — across its two-sided business/law-firm model. Apperio is a Seedcamp portfolio company and is now part of Persuit.
image: https://developer.apperio.com/static/favicon-32x32.png
layout: provider
modified: '2026-07-17'
name: Apperio
nav: Providers
network: true
overview: 'Apperio publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, E-billing API, Filter API, and 2 more. Tagged areas include Legal, E-Billing, Legal Tech, Matter Management, and Legal Operations.


  Apperio''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 22 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 2
  name: Apperio Rate Limits
  slug: apperio-rate-limits
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 45.2
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 44.7
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/apperio/apperio-2026-07-25T200728.png
security:
- kind: authentication
  name: Apperio Authentication
  slug: apperio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apperio Domain Security
  slug: apperio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Apperio Trust Center
  slug: apperio-trust-center
  summary_line: ISO/IEC 27001, SOC 2 Type 2, Cyber Essentials
skill_count: 3
skills:
- name: Discover and analyze legal spend
  slug: apperio-discover-legal-spend
- name: Review and approve an e-billing invoice
  slug: apperio-ebilling-approval
- name: Organize matters with tags
  slug: apperio-matter-tagging
slug: apperio
tags:
- Legal
- E-Billing
- Legal Tech
- Matter Management
- Legal Operations
- Analytics
- Company
website: https://www.apperio.com
---
