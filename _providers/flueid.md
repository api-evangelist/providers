---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 81
  human_in_the_loop: 1
  name: Flueid Agentic Access
  operation_count: 132
  slug: flueid-agentic-access
  summary_line: 132 operations · 81 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Account API from Flueid — 24 operation(s) for account.
  name: Flueid Account API
  slug: flueid-account-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The AccountPartner API from Flueid — 2 operation(s) for accountpartner.
  name: Flueid Account Partner API
  slug: flueid-accountpartner-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The ClientCompanies API from Flueid — 5 operation(s) for clientcompanies.
  name: Flueid Client Companies API
  slug: flueid-clientcompanies-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Documents API from Flueid — 1 operation(s) for documents.
  name: Flueid Documents API
  slug: flueid-documents-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Farms API from Flueid — 18 operation(s) for farms.
  name: Flueid Farms API
  slug: flueid-farms-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The NewOrders API from Flueid — 15 operation(s) for neworders.
  name: Flueid New Orders API
  slug: flueid-neworders-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The OrderDocumentSettings API from Flueid — 5 operation(s) for orderdocumentsettings.
  name: Flueid Order Document Settings API
  slug: flueid-orderdocumentsettings-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The OrderEvents API from Flueid — 2 operation(s) for orderevents.
  name: Flueid Order Events API
  slug: flueid-orderevents-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The OrderOptions API from Flueid — 2 operation(s) for orderoptions.
  name: Flueid Order Options API
  slug: flueid-orderoptions-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Orders API from Flueid — 10 operation(s) for orders.
  name: Flueid Orders API
  slug: flueid-orders-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The PartnerOrderSettings API from Flueid — 10 operation(s) for partnerordersettings.
  name: Flueid Partner Order Settings API
  slug: flueid-partnerordersettings-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Partners API from Flueid — 11 operation(s) for partners.
  name: Flueid Partners API
  slug: flueid-partners-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Permissions API from Flueid — 3 operation(s) for permissions.
  name: Flueid Permissions API
  slug: flueid-permissions-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The PropertyData API from Flueid — 22 operation(s) for propertydata.
  name: Flueid Property Data API
  slug: flueid-propertydata-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Public API from Flueid — 1 operation(s) for public.
  name: Flueid Public API
  slug: flueid-public-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Settings API from Flueid — 1 operation(s) for settings.
  name: Flueid Settings API
  slug: flueid-settings-api
artifact_total: 22
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/flueid-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/flueid-pro-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flueid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flueid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flueid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.pro.flueid.com/swagger
- group: docs
  title: ''
  type: APIReference
  url: https://api.pro.flueid.com/swagger
- group: start
  title: ''
  type: SignUp
  url: https://pro.flueid.com/
- group: operate
  title: ''
  type: Support
  url: https://www.flueid.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.flueid.com/media
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flueid.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flueid.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.flueid.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/flueid-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flueid-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flueid-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flueid-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flueid-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flueid-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flueid-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flueid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flueid-rate-limits.yml
created: '2026-08-16'
description: Flueid is an Austin, Texas real estate technology company, founded in 2017, that built the Verification of Title (VOT) category — digitizing the legacy title search, examination and underwriting risk process so title status can be returned as data rather than a manual report. Its platform spans Flueid Decision (the patented VOT decisioning engine used by mortgage lenders, servicers, title underwriters and secondary-market investors), Flueid Transact (workflow and settlement orchestration) and Flueid Pro (a property research, data and lead-discovery workspace for real estate agents, loan officers and title agents). Flueid Pro exposes a public OpenAPI 3.0.1 contract at api.pro.flueid.com covering orders, property data, farms, partners, documents and account management; the Decision and Transact platform APIs are token-based partner integrations negotiated under contract rather than self-service.
image: https://www.flueid.com/favicons/android-chrome-192x192.png
layout: provider
modified: '2026-08-16'
name: Flueid
nav: Providers
network: true
overview: 'Flueid publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account API, Account Partner API, Client Companies API, and 13 more. Tagged areas include Company, Real-Estate, Title Insurance, Mortgage, and Property Data.


  Flueid''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Flueid Plans Pricing
  plan_count: 0
  slug: flueid-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Flueid Rate Limits
  slug: flueid-rate-limits
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 40.1
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flueid/refs/heads/main/screenshots/flueid-2026-09-02T145527.png
security:
- kind: authentication
  name: Flueid Authentication
  slug: flueid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Flueid Domain Security
  slug: flueid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flueid Trust Center
  slug: flueid-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, FIPS 140-2 Level 3 (AWS KMS HSM), NIST CSF alignment
slug: flueid
tags:
- Company
- Real-Estate
- Title Insurance
- Mortgage
- Property Data
- Verification of Title
- Financial-Services
- Lending
- PropTech
- Settlement Services
website: https://www.flueid.com/
---
