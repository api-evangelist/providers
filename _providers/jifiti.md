---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Jifiti's Buy Now Pay Later API enables merchants and lenders to offer split payment and consumer financing options, including one-time loans and revolving lines of credit.
  name: Jifiti Buy Now Pay Later API
  slug: bnpl-api
- description: Jifiti's Embedded Lending API for banks and lenders provides detailed guides and component diagrams to help map lending solutions with the Jifiti platform.
  name: Jifiti Embedded Lending API
  slug: lending-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/jifiti-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.jifiti.com/compliance/
- group: design
  title: ''
  type: Conformance
  url: conformance/jifiti-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jifiti-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jifiti-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jifiti.com
- group: commercial
  title: ''
  type: Plans
  url: plans/jifiti-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jifiti-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jifiti-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jifiti-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jifiti
- group: company
  title: ''
  type: Website
  url: https://www.jifiti.com
- group: start
  title: ''
  type: Portal
  url: https://www.jifiti.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jifiti.com/api/
- group: operate
  title: ''
  type: Support
  url: https://www.jifiti.com/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jifiti.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jifiti.com/privacy-notice/
- group: company
  title: ''
  type: Blog
  url: https://www.jifiti.com/news/feed/
coverage:
  checked: '2026-08-27'
  detail: Both Jifiti developer hubs are ReadMe.io sites behind a site-wide password — developers.jifiti.com ("CRED API") and lenders.jifiti.com ("jifiti4lenders") 302 every path, including /openapi.json and /llms.txt, to /password?redirect=... — and the only way to the password is a "Developer Access Request" form on www.jifiti.com/api/ that asks for company name and job title before granting one of "API for Lenders", "API for Merchants" or "Lending MCP (Alpha)".
  evidence:
  - status: 302
    url: https://developers.jifiti.com/openapi.json
  - status: 302
    url: https://lenders.jifiti.com/reference
  - status: 403
    url: https://api.jifiti.com/openapi.json
  - status: 200
    url: https://www.jifiti.com/api/
  reason: partner-login
  state: gated
created: '2025-02-24'
description: Through our white-labeled platform, banks and lenders embed their loans at any point of sale, giving merchants access to the most competitive business and consumer loan programs from lenders their customers trust. Jifiti provides a fast, secure, and stable API for embedded lending and Buy Now Pay Later solutions.
finops:
- name: Jifiti Finops
  service_category: API
  slug: jifiti-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jifiti.png
layout: provider
modified: '2026-08-27'
name: Jifiti
nav: Providers
network: true
overview: 'Jifiti publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Buy Now Pay Later, Embedded Finance, Embedded Lending, and Fintech.


  Jifiti''s developer surface includes developer portal, documentation, support, engineering blog, and 14 more developer resources.'
plans:
- name: Jifiti Plans Pricing
  plan_count: 0
  slug: jifiti-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Jifiti Rate Limits
  slug: jifiti-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 25.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: dora
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 30.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jifiti/refs/heads/main/screenshots/jifiti-2026-06-20T183731.png
security:
- kind: domain-security
  name: Jifiti Domain Security
  slug: jifiti-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Jifiti Trust Center
  slug: jifiti-trust-center
  summary_line: ISO/IEC 27001, PCI DSS, SOC 1 Type II, SOC 2 Type II, DORA, EU-US Data Privacy Framework (incl. UK Extension), GDPR
slug: jifiti
tags:
- Banking
- Buy Now Pay Later
- Embedded Finance
- Embedded Lending
- Fintech
- Lending
- Payments
- POS Financing
- White Label
website: https://www.jifiti.com
---
