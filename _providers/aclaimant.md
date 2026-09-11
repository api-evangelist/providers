---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-10'
api_count: 1
apis:
- baseURL: https://api.aclaimant.com/api
  baseurl_source: declared
  description: The Aclaimant Platform API (x-id "platform-api") is the end-user integration surface for a company or collective on the Aclaimant platform. Swagger 2.0, base path /api, JSON in and JSON / transit+json
  name: Aclaimant Platform API
  slug: aclaimant-platform-api
- description: Callback API for TPAs, carriers, brokers and other Aclaimant partners working claims on behalf of an Aclaimant customer. Base URL https://api.aclaimant.com/partner, bearer-token authorization issued b
  name: Aclaimant Partner / Third-party API
  slug: aclaimant-partner-third-party-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aclaimant-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.aclaimant.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aclaimant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.aclaimant.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.aclaimant.com/api/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.aclaimant.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.aclaimant.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aclaimant.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aclaimant.com/plans-and-pricing
- group: start
  title: ''
  type: Login
  url: https://dashboard.aclaimant.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aclaimant.com/service-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aclaimant.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aclaimant
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aclaimant.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aclaimant.com/
- group: auth
  title: ''
  type: Security
  url: https://www.aclaimant.com/responsible-disclosure
- group: auth
  title: ''
  type: Compliance
  url: conformance/aclaimant-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aclaimant-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aclaimant-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aclaimant-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aclaimant-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aclaimant-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aclaimant-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aclaimant-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.aclaimant.com/hc/en-us/sections/4406733144859-Product-Updates-Releases
- group: design
  title: ''
  type: DataModel
  url: data-model/aclaimant-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/aclaimant-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aclaimant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aclaimant-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aclaimant-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aclaimant-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/aclaimant-platform-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aclaimant-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aclaimant-vulnerability-disclosure.yml
created: '2026-09-06'
description: Aclaimant is a Chicago-based risk management information system (RMIS) used by policyholders, insurance brokers, carriers and third-party administrators to run incident reporting and first notice of loss (FNOL), claims management and analytics, safety and loss control, OSHA logs, policy management, and assets and exposures from one workflow platform. Its machine-readable surface is the Aclaimant Platform API — a Swagger 2.0 contract published at api.aclaimant.com/api with a live Swagger UI console — which lets integrators create and upsert answer bundles, incidents, claims, claim reports, events, files, companies, policies, policy programs, exposures and exposure summations, including bulk jobs with a status endpoint. A separate Partner / Third-party API at api.aclaimant.com/partner lets carriers, TPAs and brokers acknowledge claim receipt and post loss-run claim financial updates back into Aclaimant.
image: https://www.aclaimant.com/hubfs/Aclaimant_February2020/Images/favicon.ico
layout: provider
modified: '2026-09-06'
name: Aclaimant
nav: Providers
network: true
overview: 'Aclaimant publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Risk Management, Insurance, Claims Management, Incident Management, and Safety.


  Aclaimant''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, changelog, and 28 more developer resources.'
plans:
- name: Aclaimant Plans Pricing
  plan_count: 3
  slug: aclaimant-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Aclaimant Rate Limits
  slug: aclaimant-rate-limits
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 54.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Aclaimant Authentication
  slug: aclaimant-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Aclaimant Domain Security
  slug: aclaimant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aclaimant Vulnerability Disclosure
  slug: aclaimant-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Aclaimant Trust Center
  slug: aclaimant-trust-center
  summary_line: SOC 2, GDPR, Penetration test report
slug: aclaimant
tags:
- Risk Management
- Insurance
- Claims Management
- Incident Management
- Safety
- RMIS
- Workers Compensation
- OSHA
- Enterprise Risk Management
- Insurtech
website: https://www.aclaimant.com/
---
