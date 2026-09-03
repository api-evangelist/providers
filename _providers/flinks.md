---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Flinks Agentic Access
  operation_count: 12
  slug: flinks-agentic-access
  summary_line: 12 operations · 11 acting
api_count: 1
apis:
- baseURL: https://{instance}-api.private.fin.ag/v3/{customerId}/BankingServices
  baseurl_source: declared
  description: The Authorize API from Flinks — 1 operation(s) for authorize.
  name: Flinks Authorize API
  slug: flinks-authorize-api
- baseURL: https://{instance}-api.private.fin.ag/v3/{customerId}/BankingServices
  baseurl_source: declared
  description: The Connect API from Flinks — 5 operation(s) for connect.
  name: Flinks Connect API
  slug: flinks-connect-api
- baseURL: https://{instance}-api.private.fin.ag/v3/{customerId}/BankingServices
  baseurl_source: declared
  description: The Enrich API from Flinks — 1 operation(s) for enrich.
  name: Flinks Enrich API
  slug: flinks-enrich-api
- baseURL: https://{instance}-api.private.fin.ag/v3/{customerId}/BankingServices
  baseurl_source: declared
  description: The Fraud API from Flinks — 2 operation(s) for fraud.
  name: Flinks Fraud API
  slug: flinks-fraud-api
- baseURL: https://{instance}-api.private.fin.ag/v3/{customerId}/BankingServices
  baseurl_source: declared
  description: The Identity API from Flinks — 1 operation(s) for identity.
  name: Flinks Identity API
  slug: flinks-identity-api
- baseURL: https://{instance}-api.private.fin.ag/v3/{customerId}/BankingServices
  baseurl_source: declared
  description: The Score API from Flinks — 2 operation(s) for score.
  name: Flinks Score API
  slug: flinks-score-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flinks Authorize API
  slug: open-flinks-authorize-api
- collection_type: open
  name: Flinks Authorize Connect API
  slug: open-flinks-connect-api
- collection_type: open
  name: Flinks Authorize Enrich API
  slug: open-flinks-enrich-api
- collection_type: open
  name: Flinks Authorize Fraud API
  slug: open-flinks-fraud-api
- collection_type: open
  name: Flinks Authorize Identity API
  slug: open-flinks-identity-api
- collection_type: open
  name: Flinks Authorize Score API
  slug: open-flinks-score-api
- collection_type: open
  name: Flinks API
  slug: open-flinks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/flinks-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flinks-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/flinks-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flinks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flinks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flinks-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flinks
- group: company
  title: ''
  type: Website
  url: https://flinks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flinks.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/flinks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flinks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/flinks-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://flinks.com/blog/
created: '2026-07-01'
description: Flinks is a Canadian financial data platform (owned by National Bank of Canada) that lets businesses connect to consumer and business bank accounts to aggregate account, transaction, and statement data, verify identity, and derive income, credit-risk, and fraud analytics. Access begins with a Flinks Connect authentication session and a multi-step /Authorize (MFA) call, after which banking, enrichment, and analytics endpoints are invoked with the returned RequestId.
finops:
- name: Flinks Finops
  service_category: Financial Data and Analytics
  slug: flinks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flinks.png
layout: provider
modified: '2026-07-01'
name: Flinks
nav: Providers
network: true
overview: 'Flinks publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authorize API, Connect API, Enrich API, and 3 more. Tagged areas include Financial Data, Open Banking, Bank Aggregation, Fintech, and Canada.


  Flinks'' developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Flinks Plans Pricing
  plan_count: 2
  slug: flinks-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Flinks Rate Limits
  slug: flinks-rate-limits
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 52.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flinks/refs/heads/main/screenshots/flinks-2026-07-25T214800.png
security:
- kind: authentication
  name: Flinks Authentication
  slug: flinks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flinks Domain Security
  slug: flinks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flinks Vulnerability Disclosure
  slug: flinks-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Flinks Trust Center
  slug: flinks-trust-center
  summary_line: SOC 2, PCI DSS
slug: flinks
tags:
- Financial Data
- Open Banking
- Bank Aggregation
- Fintech
- Canada
website: https://flinks.com/
---
