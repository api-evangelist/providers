---
access_model:
  confidence: high
  label: Free API access with a reseller account; documented OTE test environment
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - docs
  trial: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: The OnlineNIC Reseller API (build 4.0.9) gives partners programmatic control of the OnlineNIC product catalogue. Twenty-six domain commands cover availability checking, registration, renewal, informat
  name: OnlineNIC Reseller API
  slug: onlinenic
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.onlinenic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.onlinenic.com/cp_english/template_api/api_help.php
- group: start
  title: ''
  type: SignUp
  url: https://www.onlinenic.com/en/Home/register.html
- group: start
  title: ''
  type: Login
  url: https://www.onlinenic.com/en/Home/login.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.onlinenic.com/en/Domains/index/19.html
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.onlinenic.com/portal/en/home
- group: company
  title: ''
  type: Blog
  url: https://www.onlinenic.com/en/News/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onlinenic.com/en/Content/content/118.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onlinenic.com/OnlineNIC_PRIVACY_Statement.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onlinenic-inc-
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/packages/onlinenic-packages.yml
  title: ''
  type: Packages
  url: packages/onlinenic-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/packages/onlinenic-packages.yml
  title: ''
  type: SDKs
  url: packages/onlinenic-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/authentication/onlinenic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onlinenic-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/conventions/onlinenic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/onlinenic-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/errors/onlinenic-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/onlinenic-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/lifecycle/onlinenic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/onlinenic-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/changelog/onlinenic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/onlinenic-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/conformance/onlinenic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onlinenic-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/data-model/onlinenic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/onlinenic-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/sandbox/onlinenic-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/onlinenic-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/plans/onlinenic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onlinenic-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/rate-limits/onlinenic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/onlinenic-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/llms/onlinenic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onlinenic-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/security/onlinenic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onlinenic-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/mcp/onlinenic-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/onlinenic-mcp.yml
created: '2025-02-09'
description: OnlineNIC, Inc. is an ICANN-accredited domain registrar (IANA ID 82) and wholesale reseller platform, operating since 1999, that sells domain names across roughly 400 TLDs, SSL/TLS certificates from DigiCert, GeoTrust, RapidSSL, Sectigo and Symantec, business email, reseller and cloud hosting, escrow and domain-privacy services. It publishes a partner-facing Reseller API — currently build 4.0.9 — that lets resellers register, renew, transfer and manage domains, manage contacts, nameservers and EPP auth codes, apply ID Shield registrant privacy, run Whois verification, and order, reissue, cancel and revoke SSL certificates. The API is an RPC surface over HTTPS with a JSON envelope; the contract is published only as a PDF reference guide, with no OpenAPI or other machine-readable description.
finops:
- name: Onlinenic Finops
  service_category: API
  slug: onlinenic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onlinenic.png
layout: provider
modified: '2026-09-17'
name: OnlineNIC
nav: Providers
network: true
overview: 'OnlineNIC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Domains, Domain Registration, Registrar, DNS, and SSL Certificates.


  OnlineNIC''s developer surface includes signup flow, pricing, support, engineering blog, authentication, changelog, sandbox, and 18 more developer resources.'
plans:
- name: Onlinenic Plans Pricing
  plan_count: 4
  slug: onlinenic-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Onlinenic Rate Limits
  slug: onlinenic-rate-limits
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.7
  facets:
    access_clarity: 84.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 68.5
    operational_transparency: 15.8
  previous_composite: 35.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/screenshots/onlinenic-2026-06-20T190720.png
security:
- kind: authentication
  name: Onlinenic Authentication
  slug: onlinenic-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Onlinenic Domain Security
  slug: onlinenic-domain-security
  summary_line: TLSv1.2 · DMARC
slug: onlinenic
tags:
- Domains
- Domain Registration
- Registrar
- DNS
- SSL Certificates
- Certificates
- Reseller
- Hosting
- Security
website: https://www.onlinenic.com/
---
