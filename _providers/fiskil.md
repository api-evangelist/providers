---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Consumer-permissioned banking, lending and energy data for Australia and New Zealand, through one API.
  name: Fiskil API
  slug: fiskil-api
- baseURL: https://api.fiskil.com
  baseurl_source: declared
  description: Consent authorisation sessions.
  name: FISKIL Auth API
  slug: fiskil-auth-api
- baseURL: https://api.fiskil.com
  baseurl_source: declared
  description: Accounts, balances, transactions, income, payees, scheduled payments, direct debits and products.
  name: FISKIL Banking API
  slug: fiskil-banking-api
- baseURL: https://api.fiskil.com
  baseurl_source: declared
  description: Identity and data-freshness endpoints shared across sectors.
  name: FISKIL Common API
  slug: fiskil-common-api
- baseURL: https://api.fiskil.com
  baseurl_source: declared
  description: Consent arrangements and permissions.
  name: FISKIL Consent API
  slug: fiskil-consent-api
- baseURL: https://api.fiskil.com
  baseurl_source: declared
  description: The people whose data is shared.
  name: FISKIL End users API
  slug: fiskil-end-users-api
- baseURL: https://api.fiskil.com
  baseurl_source: declared
  description: Energy accounts, smart-meter usage, billing, invoices, plans, service points, concessions and DER.
  name: FISKIL Energy API
  slug: fiskil-energy-api
- baseURL: https://api.fiskil.com
  baseurl_source: declared
  description: Banks, lenders and energy providers available to connect to.
  name: FISKIL Institutions API
  slug: fiskil-institutions-api
- baseURL: https://api.fiskil.com
  baseurl_source: declared
  description: The Transactions API from FISKIL — 2 operation(s) for transactions.
  name: FISKIL Transactions API
  slug: fiskil-transactions-api
artifact_total: 19
asyncapis:
- description: ''
  name: Fiskil Webhooks
  slug: fiskil-webhooks
common:
- group: other
  href: https://artifacts.apis.io/fiskil/capabilities/fiskil-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fiskil-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/fiskil/rules/fiskil-rules.yml
  title: ''
  type: Spectral
  url: rules/fiskil-rules.yml
- group: design
  href: https://artifacts.apis.io/fiskil/json-ld/fiskil-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fiskil-context.jsonld
- group: design
  href: https://artifacts.apis.io/fiskil/vocabulary/fiskil-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fiskil-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fiskil/conformance/fiskil-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fiskil-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fiskil/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fiskil/asyncapi/fiskil-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fiskil-webhooks.yml
- group: design
  href: https://artifacts.apis.io/fiskil/data-model/fiskil-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fiskil-data-model.yml
- group: operate
  href: https://artifacts.apis.io/fiskil/changelog/fiskil-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fiskil-changelog.yml
- group: design
  href: https://artifacts.apis.io/fiskil/conventions/fiskil-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fiskil-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.fiskil.com/security
- group: auth
  href: https://artifacts.apis.io/fiskil/authentication/fiskil-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fiskil-authentication.yml
- group: design
  href: https://artifacts.apis.io/fiskil/errors/fiskil-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fiskil-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/fiskil/llms/fiskil-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fiskil-llms.txt
- group: other
  href: https://artifacts.apis.io/fiskil/hosts/fiskil-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fiskil-hosts.yml
- group: other
  href: https://artifacts.apis.io/fiskil/vendors/fiskil-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fiskil-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fiskil.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.fiskil.com/press
- group: start
  title: ''
  type: Login
  url: https://console.fiskil.com/auth/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fiskil.com/data-api/guides/getting-started/authentication
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fiskil.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fiskil.com/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/fiskil/security/fiskil-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fiskil-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fiskil/security/fiskil-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fiskil-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fiskil/security/fiskil-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fiskil-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fiskil.com/
- group: operate
  title: ''
  type: Support
  url: https://www.fiskil.com/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.fiskil.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fiskil.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fiskil.com/legal/privacy-policy
created: '2026-10-08'
description: Fiskil provides an Open Banking and Open Data platform enabling banks and financial institutions to securely share consumer‑permissioned data via standardized APIs. Their solutions support data portability, partner onboarding, credential‑free access, and regulatory readiness, helping organizations reduce compliance risk, eliminate screen‑scraping, and transform data access into a competitive advantage. Targeted at the North American market, Fiskil’s platform offers scalable, auditable data sharing that meets industry standards and modern consumer expectations.
image: https://www.fiskil.com/images/open-graph-main.png
jsonld:
- class_count: 120
  name: Fiskil Context
  property_count: 372
  slug: fiskil-context
layout: provider
modified: '2026-10-08'
name: FISKIL
nav: Providers
network: true
overview: 'FISKIL publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Banking API, Common API, and 6 more. Tagged areas include Open Banking, Data Sharing, Financial Services, API Platform, and North America.


  The FISKIL catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  FISKIL''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, support, engineering blog, and 23 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: FISKIL API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: fiskil-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 70.9
    developer_ergonomics: 31.5
    discoverability: 74.1
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 52.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 23.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fiskil/fiskil-2026-11-03T132107.png
security:
- kind: authentication
  name: Fiskil Authentication
  slug: fiskil-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fiskil Domain Security
  slug: fiskil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fiskil Vulnerability Disclosure
  slug: fiskil-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Fiskil Trust Center
  slug: fiskil-trust-center
  summary_line: SOC 2
skill_count: 3
skills:
- name: fiskil-get-account-overview
  slug: fiskil-get-account-overview
- name: fiskil-manage-end-users
  slug: fiskil-manage-end-users
- name: fiskil-refresh-banking-transactions
  slug: fiskil-refresh-banking-transactions
slug: fiskil
tags:
- Open Banking
- Data Sharing
- Financial Services
- API Platform
- North America
website: https://www.fiskil.com/
---
