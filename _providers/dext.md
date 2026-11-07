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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.precision.dext.com
  baseurl_source: declared
  description: Practice client data-health metrics and activity statistics
  name: Dext Clients API
  slug: dext-clients-api
artifact_total: 12
collections:
- collection_type: open
  name: Dext Data Health & Insights Clients API
  slug: open-dext-clients-api
common:
- group: commercial
  href: https://artifacts.apis.io/dext/plans/dext-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dext-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/dext/overlays/dext-data-health-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dext-data-health-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/dext/security/dext-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dext-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://dext.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.dext.com/en/articles/272702-data-health-insights-api
- group: docs
  title: ''
  type: APIReference
  url: https://help.dext.com/en/articles/272702-data-health-insights-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.dext.com/en/articles/272702-data-health-insights-api
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.dext.com/
- group: operate
  title: ''
  type: Support
  url: https://help.dext.com/
- group: company
  title: ''
  type: Blog
  url: https://dext.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dext.com/en/business/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dext.com/us/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dext.com/us/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.dext.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dext
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dext.com/
- group: auth
  title: ''
  type: Security
  url: https://dext.com/us/security
- group: auth
  title: ''
  type: Compliance
  url: https://dext.com/us/security
- group: agent
  href: https://artifacts.apis.io/dext/llms/dext-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dext-llms.txt
- group: auth
  href: https://artifacts.apis.io/dext/authentication/dext-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dext-authentication.yml
- group: operate
  href: https://artifacts.apis.io/dext/rate-limits/dext-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dext-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/dext/conventions/dext-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dext-conventions.yml
- group: design
  href: https://artifacts.apis.io/dext/lifecycle/dext-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dext-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dext/errors/dext-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dext-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dext/conformance/dext-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dext-conformance.yml
- group: design
  href: https://artifacts.apis.io/dext/data-model/dext-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dext-data-model.yml
- group: agent
  href: https://artifacts.apis.io/dext/mcp/dext-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dext-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dext/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/dext/openapi/_original/dext-data-health-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/dext-data-health-openapi.yml
- group: auth
  href: https://artifacts.apis.io/dext/security/dext-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dext-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dext/security/dext-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dext-vulnerability-disclosure.yml
created: '2026-07-17'
description: Dext is bookkeeping automation software for businesses, accountants and bookkeepers (formerly Receipt Bank / Dext Precision / Dext Commerce). It captures receipts, invoices and bank statements, extracts and validates the data with high accuracy, and publishes it into accounting software such as Xero, QuickBooks, Sage, Zoho and MYOB. Dext serves over 700,000 customers worldwide across the UK, US, Canada, Australia, France and South Africa. For accounting practices, Dext exposes a read-only Data Health & Insights REST API that returns client data-health metrics and rolling activity statistics, authenticated with practice-scoped bearer tokens and rate limited to 60 requests per minute.
finops:
- has_sources: true
  method: derived
  name: Dext Finops
  primary_unit: add-on
  service_category: ''
  slug: dext-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dext.png
layout: provider
modified: '2026-07-18'
name: Dext
nav: Providers
network: true
overview: 'Dext publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Clients API. Tagged areas include Company, Accounting, Bookkeeping, Receipts, and Expense Management.


  The Dext catalog on APIs.io includes 1 Spectral governance ruleset.


  Dext''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Dext Plans Pricing
  plan_count: 9
  slug: dext-plans-pricing
- name: Dext Price Estimates
  plan_count: 0
  slug: dext-price-estimates
random_paper: 5
rate_limits:
- limit_count: 1
  name: Dext Rate Limits
  slug: dext-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Dext API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: dext-rules
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 50.2
    developer_ergonomics: 49.4
    discoverability: 73.2
    operational_transparency: 50.0
  previous_composite: 60.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/dext/dext-2026-07-25T211838.png
security:
- kind: authentication
  name: Dext Authentication
  slug: dext-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dext Domain Security
  slug: dext-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dext Vulnerability Disclosure
  slug: dext-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Dext Trust Center
  slug: dext-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
skill_count: 1
skills:
- name: Pull client data-health and activity stats from Dext
  slug: dext-client-data-health
slug: dext
tags:
- Company
- Accounting
- Bookkeeping
- Receipts
- Expense Management
- Financial Automation
- Data Health
- OCR
website: https://dext.com/
---
