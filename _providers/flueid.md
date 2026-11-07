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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 79
  human_in_the_loop: 1
  name: Flueid Agentic Access
  operation_count: 132
  slug: flueid-agentic-access
  summary_line: 132 operations · 79 acting · 1 human-in-the-loop
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
  description: The Public API from Flueid — 1 operation(s) for public.
  name: Flueid Public API
  slug: flueid-public-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Settings API from Flueid — 1 operation(s) for settings.
  name: Flueid Settings API
  slug: flueid-settings-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Order Events API from Flueid — 2 operation(s) for order events.
  name: Flueid Order Events API
  slug: flueid-order-events-api
- baseURL: https://api.pro.flueid.com
  baseurl_source: declared
  description: The Property Data API from Flueid — 22 operation(s) for property data.
  name: Flueid Property Data API
  slug: flueid-property-data-api
artifact_total: 26
common:
- group: other
  href: https://artifacts.apis.io/flueid/capabilities/flueid-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/flueid-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/flueid/overlays/flueid-pro-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/flueid-pro-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/flueid/agentic-access/flueid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flueid-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/flueid/security/flueid-domain-security.yml
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
  href: https://artifacts.apis.io/flueid/security/flueid-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flueid-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/flueid/authentication/flueid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flueid-authentication.yml
- group: design
  href: https://artifacts.apis.io/flueid/conventions/flueid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flueid-conventions.yml
- group: design
  href: https://artifacts.apis.io/flueid/data-model/flueid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flueid-data-model.yml
- group: design
  href: https://artifacts.apis.io/flueid/lifecycle/flueid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flueid-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/flueid/conformance/flueid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flueid-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flueid/llms/flueid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flueid-llms.txt
- group: agent
  href: https://artifacts.apis.io/flueid/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/flueid/plans/flueid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flueid-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/flueid/rate-limits/flueid-rate-limits.yml
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
overview: 'Flueid publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account Partner API, Client Companies API, and 13 more. Tagged areas include Company, Real Estate, Title Insurance, Mortgage, and Property Data.


  The Flueid catalog on APIs.io includes 1 Spectral governance ruleset.


  Flueid''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Flueid Plans Pricing
  plan_count: 0
  slug: flueid-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Flueid Rate Limits
  slug: flueid-rate-limits
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Flueid API Rules
  rule_count: 37
  severity_counts:
    error: 29
    hint: 0
    info: 4
    warn: 4
  slug: flueid-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 7.9
    contract_governance: 31.8
    contract_quality: 37.6
    developer_ergonomics: 30.4
    discoverability: 73.2
    operational_transparency: 15.8
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
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
    score: 14.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/flueid/flueid-2026-09-02T145527.png
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
skill_count: 3
skills:
- name: Build and report on a Flueid Pro farm
  slug: flueid-build-and-report-on-a-farm
- name: Open and track a Flueid Pro title order
  slug: flueid-open-and-track-title-order
- name: Research a property with Flueid Pro
  slug: flueid-property-research
slug: flueid
tags:
- Company
- Real Estate
- Title Insurance
- Mortgage
- Property Data
- Verification of Title
- Financial Services
- Lending
- PropTech
- Settlement Services
website: https://www.flueid.com/
---
