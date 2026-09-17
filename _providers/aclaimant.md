---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: Callback API for TPAs, carriers, brokers and other Aclaimant partners working claims on behalf of an Aclaimant customer. Base URL https://api.aclaimant.com/partner, bearer-token authorization issued b
  name: Aclaimant Partner / Third-party API
  slug: aclaimant-partner-third-party-api
- baseURL: https://api.aclaimant.com/api
  baseurl_source: declared
  description: The answers API from Aclaimant — 15 operation(s) for answers.
  name: Aclaimant Answers API
  slug: aclaimant-answers-api
- baseURL: https://api.aclaimant.com/api
  baseurl_source: declared
  description: The bulk API from Aclaimant — 8 operation(s) for bulk.
  name: Aclaimant Bulk API
  slug: aclaimant-bulk-api
- baseURL: https://api.aclaimant.com/api
  baseurl_source: declared
  description: The companies API from Aclaimant — 1 operation(s) for companies.
  name: Aclaimant Companies API
  slug: aclaimant-companies-api
- baseURL: https://api.aclaimant.com/api
  baseurl_source: declared
  description: The exposures API from Aclaimant — 2 operation(s) for exposures.
  name: Aclaimant Exposures API
  slug: aclaimant-exposures-api
- baseURL: https://api.aclaimant.com/api
  baseurl_source: declared
  description: The incidents API from Aclaimant — 1 operation(s) for incidents.
  name: Aclaimant Incidents API
  slug: aclaimant-incidents-api
- baseURL: https://api.aclaimant.com/api
  baseurl_source: declared
  description: The policies API from Aclaimant — 2 operation(s) for policies.
  name: Aclaimant Policies API
  slug: aclaimant-policies-api
- baseURL: https://api.aclaimant.com/api
  baseurl_source: declared
  description: The policy-programs API from Aclaimant — 2 operation(s) for policy-programs.
  name: Aclaimant Policy Programs API
  slug: aclaimant-policy-programs-api
artifact_total: 14
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/security/aclaimant-trust-center.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/conformance/aclaimant-conformance.yml
  title: ''
  type: Compliance
  url: conformance/aclaimant-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/authentication/aclaimant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aclaimant-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/conventions/aclaimant-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aclaimant-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/conventions/aclaimant-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aclaimant-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/conformance/aclaimant-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aclaimant-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/errors/aclaimant-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aclaimant-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/lifecycle/aclaimant-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aclaimant-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/changelog/aclaimant-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aclaimant-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.aclaimant.com/hc/en-us/sections/4406733144859-Product-Updates-Releases
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/data-model/aclaimant-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aclaimant-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/packages/aclaimant-packages.yml
  title: ''
  type: Packages
  url: packages/aclaimant-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/plans/aclaimant-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aclaimant-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/rate-limits/aclaimant-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aclaimant-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/sandbox/aclaimant-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aclaimant-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/llms/aclaimant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aclaimant-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/overlays/aclaimant-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aclaimant-platform-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/security/aclaimant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aclaimant-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aclaimant/refs/heads/main/security/aclaimant-vulnerability-disclosure.yml
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
overview: 'Aclaimant publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Answers API, Bulk API, Companies API, and 4 more. Tagged areas include Risk Management, Insurance, Claims Management, Incident Management, and Safety.


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
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.4
  facets:
    access_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 40.6
    developer_ergonomics: 54.2
    discoverability: 75.9
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 54.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
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
