---
access_model:
  confidence: high
  label: Free public API — self-service api.data.gov key, DEMO_KEY works with no signup
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://www.ftc.gov/developer
  - https://api.data.gov/signup/
  trial: true
  try_now: true
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
    well_known_catalog: true
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-10'
api_count: 6
apis:
- description: The FTC Developer Portal is the central hub for developer documentation, data dictionaries, and access program details for FTC-managed datasets and services. It names the API base URL (https://api.ftc
  name: FTC Developer Portal
  slug: developer-portal
- description: Read-only REST endpoint returning consumer reports of unwanted and illegal telemarketing calls, filterable by complaint date, violation date, consumer state and city, originating area code and robocal
  name: Do Not Call (DNC) Reported Calls Data API
  slug: dnc-complaints
- description: Read-only REST endpoint returning Hart-Scott-Rodino premerger notifications for which early termination of the waiting period was granted, filterable by title keyword, transaction number and transacti
  name: HSR Early Termination Notices API
  slug: hsr-early-termination-notices
- description: The National Do Not Call Registry program lets telemarketers and sellers download phone-number data they must scrub against before placing calls. Access is provisioned through telemarketing.donotcall.
  name: National Do Not Call Registry
  slug: do-not-call-registry
- description: Consumer Sentinel is the FTC's secure online database of consumer reports of fraud, identity theft, and other complaints, made available to participating federal, state, local, and international law e
  name: Consumer Sentinel Network
  slug: consumer-sentinel
- description: The Hart-Scott-Rodino (HSR) Premerger Notification Program coordinates premerger filings reviewed by the FTC and DOJ. Filings are submitted electronically through the dedicated HSR e-filing system.
  name: HSR Premerger Notification
  slug: hsr-premerger
artifact_total: 12
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ftc.gov/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.ftc.gov/developer
- group: docs
  title: ''
  type: APIReference
  url: https://www.ftc.gov/developer/api/v0/endpoints/do-not-call-dnc-reported-calls-data-api
- group: start
  title: ''
  type: SignUp
  url: https://api.data.gov/signup/
- group: operate
  title: ''
  type: Support
  url: https://www.ftc.gov/about-ftc/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ftc.gov/policy-notices/website-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ftc.gov/policy-notices/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.ftc.gov/policy-notices/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/federal-trade-commission-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-trade-commission-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/federal-trade-commission-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/federal-trade-commission-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/federal-trade-commission-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/federal-trade-commission-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/federal-trade-commission-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/federal-trade-commission-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/federal-trade-commission-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/federal-trade-commission-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/federal-trade-commission-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/federal-trade-commission-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federal-trade-commission-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-trade-commission-mcp.yml
- group: other
  title: ''
  type: DataCatalog
  url: https://www.ftc.gov/data.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FederalTradeCommission
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-trade-commission
- group: company
  title: ''
  type: Website
  url: https://www.ftc.gov/
- group: company
  title: ''
  type: News
  url: https://www.ftc.gov/news-events
- group: other
  title: ''
  type: Open Data
  url: https://www.ftc.gov/site-information/open-government/data-sets
- group: other
  title: ''
  type: Consumer Resources
  url: https://consumer.ftc.gov
- group: company
  title: ''
  type: Blog
  url: https://www.ftc.gov/feeds/press-release.xml
created: '2024-12-03'
description: 'The Federal Trade Commission (FTC) is a U.S. federal agency that enforces antitrust and consumer protection laws affecting virtually every area of commerce. The FTC operates a small public, read-only REST API at https://api.ftc.gov/v0 — fronted by the api.data.gov gateway and covering Do Not Call consumer complaint reports and Hart-Scott-Rodino premerger early termination notices — alongside a Project Open Data (DCAT-US 1.1) inventory of 95 datasets at https://www.ftc.gov/data.json. Two further developer-facing programmes are gated rather than public: the National Do Not Call Registry telemarketer download at telemarketing.donotcall.gov, and the Consumer Sentinel Network of consumer complaint data shared with vetted law enforcement.'
finops:
- name: Federal Trade Commission Finops
  service_category: API
  slug: federal-trade-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-trade-commission.png
layout: provider
modified: '2026-09-09'
name: Federal Trade Commission
nav: Providers
network: true
overview: 'Federal Trade Commission publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Antitrust, Consumer Protection, Do Not Call, Federal-Government, and Law Enforcement.


  Federal Trade Commission''s developer surface includes documentation, API reference, signup flow, support, authentication, sandbox, product news, and 23 more developer resources.'
plans:
- name: Federal Trade Commission Plans Pricing
  plan_count: 0
  slug: federal-trade-commission-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Federal Trade Commission Rate Limits
  slug: federal-trade-commission-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.0
    catalog_earned_first_party: 12.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.5
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 11.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-trade-commission/refs/heads/main/screenshots/federal-trade-commission-2026-06-20T181129.png
security:
- kind: authentication
  name: Federal Trade Commission Authentication
  slug: federal-trade-commission-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Federal Trade Commission Domain Security
  slug: federal-trade-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Federal Trade Commission Vulnerability Disclosure
  slug: federal-trade-commission-vulnerability-disclosure
  summary_line: Bugcrowd
slug: federal-trade-commission
tags:
- Antitrust
- Consumer Protection
- Do Not Call
- Federal-Government
- Law Enforcement
- Open Data
website: https://www.ftc.gov/
---
