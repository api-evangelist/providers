---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.precision.dext.com
  baseurl_source: declared
  description: Practice client data-health metrics and activity statistics
  name: Dext Clients API
  slug: dext-clients-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dext Data Health & Insights Clients API
  slug: open-dext-clients-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/dext-data-health-overlay.yaml
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/dext-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/dext-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dext-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dext-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dext-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dext-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dext-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dext-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dext-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/dext-data-health-openapi.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dext-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dext-vulnerability-disclosure.yml
created: '2026-07-17'
description: Dext is bookkeeping automation software for businesses, accountants and bookkeepers (formerly Receipt Bank / Dext Precision / Dext Commerce). It captures receipts, invoices and bank statements, extracts and validates the data with high accuracy, and publishes it into accounting software such as Xero, QuickBooks, Sage, Zoho and MYOB. Dext serves over 700,000 customers worldwide across the UK, US, Canada, Australia, France and South Africa. For accounting practices, Dext exposes a read-only Data Health & Insights REST API that returns client data-health metrics and rolling activity statistics, authenticated with practice-scoped bearer tokens and rate limited to 60 requests per minute.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dext.png
layout: provider
modified: '2026-07-18'
name: Dext
nav: Providers
network: true
overview: 'Dext publishes 1 API on the [APIs.io](https://apis.io/) network: Clients API. Tagged areas include Company, Accounting, Bookkeeping, Receipts, and Expense Management.


  Dext''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Dext Rate Limits
  slug: dext-rate-limits
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 54.5
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
    score: 45.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dext/refs/heads/main/screenshots/dext-2026-07-25T211838.png
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
