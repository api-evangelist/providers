---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Malt Agentic Access
  operation_count: 13
  slug: malt-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 2
apis:
- baseURL: https://api.malt.com
  baseurl_source: declared
  description: Operations related to freelancer service charge invoices
  name: Malt Fee Invoices API
  slug: malt-fee-invoices-api
- baseURL: https://api.malt.com
  baseurl_source: declared
  description: Operations related to freelancer invoices
  name: Malt Invoices API
  slug: malt-invoices-api
- baseURL: https://api.malt.com
  baseurl_source: declared
  description: Operations related to freelancer payments
  name: Malt Payments API
  slug: malt-payments-api
- baseURL: https://api.malt.com
  baseurl_source: declared
  description: Manage users
  name: Malt SCIM API
  slug: malt-scim-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/malt/capabilities/malt-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/malt-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.malt.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.malt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.malt.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.malt.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.malt.com/
- group: operate
  title: ''
  type: Support
  url: https://help.malt.com/kb/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.malt.com/kb/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.malt.engineering/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.malt.engineering/feed
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.malt.com/fr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Maltcommunity
- group: commercial
  title: ''
  type: Pricing
  url: https://www.malt.com/c/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.malt.com/who-are-you
- group: start
  title: ''
  type: Login
  url: https://www.malt.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.malt.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.malt.com/about/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.malt.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.malt.com/
- group: docs
  href: https://artifacts.apis.io/malt/openapi/_original/malt-exposed-apis-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/malt-exposed-apis-openapi.yml
- group: auth
  href: https://artifacts.apis.io/malt/authentication/malt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/malt-authentication.yml
- group: design
  href: https://artifacts.apis.io/malt/conventions/malt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/malt-conventions.yml
- group: design
  href: https://artifacts.apis.io/malt/data-model/malt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/malt-data-model.yml
- group: design
  href: https://artifacts.apis.io/malt/errors/malt-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/malt-problem-types.yml
- group: design
  href: https://artifacts.apis.io/malt/lifecycle/malt-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/malt-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/malt/conformance/malt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/malt-conformance.yml
- group: other
  href: https://artifacts.apis.io/malt/overlays/malt-exposed-apis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/malt-exposed-apis-overlay.yaml
- group: build
  href: https://artifacts.apis.io/malt/packages/malt-packages.yml
  title: ''
  type: Packages
  url: packages/malt-packages.yml
- group: design
  href: https://artifacts.apis.io/malt/components/malt-components.yml
  title: ''
  type: Components
  url: components/malt-components.yml
- group: commercial
  href: https://artifacts.apis.io/malt/plans/malt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/malt-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/malt/rate-limits/malt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/malt-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/malt/mcp/malt-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/malt-mcp.yml
- group: build
  href: https://artifacts.apis.io/malt/mcp/malt-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/malt-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/malt/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/malt/llms/malt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/malt-llms.txt
- group: agent
  href: https://artifacts.apis.io/malt/well-known/malt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/malt-well-known.yml
- group: auth
  href: https://artifacts.apis.io/malt/well-known/malt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/malt-security.txt
- group: auth
  href: https://artifacts.apis.io/malt/security/malt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/malt-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/malt/security/malt-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/malt-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/malt/security/malt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/malt-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/malt/agentic-access/malt-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/malt-agentic-access.yml
created: '2026-08-17'
description: 'Malt is a European freelance marketplace and Freelance Management System (FMS) founded in 2013 in Paris by Vincent Huguet and Hugo Lassiege, connecting more than a million independent consultants across tech, data, AI, design, marketing and management with enterprise buyers. Beyond matching, the platform handles the administrative spine of freelance engagement: quotes, automated contracts and NDAs, timesheets, invoicing, insured payments and compliance checks, plus an enterprise tier that consolidates an existing freelance roster (Malt Open) and plugs into 85+ ERP, procurement and HR systems including SAP Fieldglass, Coupa and Workday. Malt publishes a small, credential-gated public API surface at api.malt.com documented with Stoplight Elements: a freelancer billing API (invoices, service charge invoices, payments, invoice PDFs) and a SCIM 2.0 user-provisioning endpoint for enterprise identity lifecycle management.'
finops:
- has_sources: true
  method: derived
  name: Malt Finops
  primary_unit: ''
  service_category: ''
  slug: malt-finops
  template: true
image: https://dam.malt.com/rebranding2020/malt-logo/malt-brew-only
layout: provider
modified: '2026-09-16'
name: Malt
nav: Providers
network: true
overview: 'Malt publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Fee Invoices API, Invoices API, Payments API, and 1 more. Tagged areas include Company, Marketplace, Freelance Marketplace, Freelance Management System, and Talent Marketplace.


  The Malt catalog on APIs.io includes 1 Spectral governance ruleset.


  Malt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Malt Plans Pricing
  plan_count: 3
  slug: malt-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Malt Rate Limits
  slug: malt-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Malt API Rules
  rule_count: 67
  severity_counts:
    error: 55
    hint: 0
    info: 4
    warn: 8
  slug: malt-rules
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 58.9
    discoverability: 67.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/malt/malt-2026-09-02T150425.png
security:
- kind: authentication
  name: Malt Authentication
  slug: malt-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Malt Domain Security
  slug: malt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Malt Vulnerability Disclosure
  slug: malt-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Reconcile Malt freelancer revenue for a period
  slug: malt-freelancer-revenue-reconciliation
- name: Retrieve a Malt invoice document as a PDF
  slug: malt-invoice-document-retrieval
- name: Provision and offboard Malt users via SCIM 2.0
  slug: malt-scim-user-lifecycle
slug: malt
tags:
- Company
- Marketplace
- Freelance Marketplace
- Freelance Management System
- Talent Marketplace
- Workforce Management
- Contingent Workforce
- Invoicing
- Payments
- SCIM
- Identity Provisioning
- Procurement
- Future Of Work
- France
- Europe
website: https://www.malt.com/
---
