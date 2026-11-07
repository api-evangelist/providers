---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - finops
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Iress Sourcing APIs bring the UK mortgage and protection sourcing data behind The Exchange, Xplan Mortgage and Trigold directly into a CRM, platform or website. Access is arranged with Iress; no publi
  name: Iress Sourcing APIs
  slug: iress-sourcing-apis
- description: Xplan Integrations connect Iress Xplan financial advice software to third-party applications, either through standard integrations that use an app key with the client's permission or through customise
  name: Xplan Integrations
  slug: xplan-integrations
- description: Iress Web Services V4 is a SOAP XML document/literal web service used to access IRESS market data and Web Admin, IOS+ (Iress Order Management System), IPS (Iress Portfolio System) and FIX+ Administrat
  name: Iress Web Services V4
  slug: iress-web-services-v4
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/iress/components/iress-components.yml
  title: ''
  type: Components
  url: components/iress-components.yml
- group: design
  href: https://artifacts.apis.io/iress/conventions/iress-conventions.yml
  title: ''
  type: Conventions
  url: conventions/iress-conventions.yml
- group: auth
  href: https://artifacts.apis.io/iress/authentication/iress-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iress-authentication.yml
- group: design
  href: https://artifacts.apis.io/iress/lifecycle/iress-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/iress-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/iress/errors/iress-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/iress-problem-types.yml
- group: design
  href: https://artifacts.apis.io/iress/conformance/iress-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iress-conformance.yml
- group: agent
  href: https://artifacts.apis.io/iress/llms/iress-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iress-llms.txt
- group: other
  href: https://artifacts.apis.io/iress/hosts/iress-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iress-hosts.yml
- group: build
  href: https://artifacts.apis.io/iress/integrations/iress-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/iress-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/iress/vendors/iress-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iress-vendors.yml
- group: build
  href: https://artifacts.apis.io/iress/packages/iress-packages.yml
  title: ''
  type: SDKs
  url: packages/iress-packages.yml
- group: build
  href: https://artifacts.apis.io/iress/packages/iress-packages.yml
  title: ''
  type: Packages
  url: packages/iress-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.iress.com/media/documents/Complaints_Policy_v1.1_June_2026.pdf
- group: docs
  title: ''
  type: Documentation
  url: https://help.iress.com/
- group: commercial
  href: https://artifacts.apis.io/iress/plans/iress-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iress-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/iress/finops/iress-finops.yml
  title: ''
  type: FinOps
  url: finops/iress-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.iress.com/blog/
- group: auth
  href: https://artifacts.apis.io/iress/security/iress-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iress-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iress
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iress
- group: company
  title: ''
  type: Website
  url: https://www.iress.com/
- group: start
  title: ''
  type: Login
  url: https://www.iress.com/sign-in/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iress.com/resources/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iress.com/trust/website-terms/
- group: operate
  title: ''
  type: Support
  url: https://www.iress.com/support/software-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.iress.com/Default.htm
- group: operate
  title: ''
  type: Forum
  url: https://community.iress.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.iress.com/trust/
- group: commercial
  title: ''
  type: Legal
  url: https://www.iress.com/resources/legal/
- group: operate
  title: ''
  type: Contact
  url: https://www.iress.com/contact/
created: '2025-02-12'
description: Iress is a technology company providing software to the financial services industry, used by more than 10,000 businesses and 500,000 users. Its products span financial advice (Xplan and Xplan Integrations), trading and market data (Iress Pro, Viewpoint, FIX, order and institutional trading systems, real-time market data from 100+ markets), investment management, and UK mortgage and protection sourcing (The Exchange, Xplan Mortgage, Trigold), whose Sourcing APIs let platforms integrate Iress sourcing data. Iress sold its QuantHouse business (QuantFeed market data API) to BAHA Tech Holding AG, and the former QuantFeed page on iress.com now returns 404.
finops:
- has_sources: false
  method: generated
  name: Iress Finops
  primary_unit: request
  service_category: API
  slug: iress-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iress.png
layout: provider
modified: '2026-10-21'
name: Iress
nav: Providers
network: true
overview: 'Iress is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Data, Market Data, Trading, Wealth Management, and Financial Advice.


  Iress'' developer surface includes authentication, documentation, engineering blog, support, legal docs, and 25 more developer resources.'
plans:
- name: Iress Plans Pricing
  plan_count: 0
  slug: iress-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Iress Rate Limits
  slug: iress-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 28.6
    discoverability: 70.5
    operational_transparency: 2.6
  previous_composite: 30.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/iress/iress-2026-06-20T183604.png
security:
- kind: authentication
  name: Iress Authentication
  slug: iress-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Iress Domain Security
  slug: iress-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iress
tags:
- Financial Data
- Market Data
- Trading
- Wealth Management
- Financial Advice
- Mortgage
- Insurance
- Fintech
website: https://www.iress.com/
---
