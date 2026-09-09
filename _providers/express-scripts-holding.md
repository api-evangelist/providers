---
access_model:
  confidence: medium
  label: Partner approval required — no self-serve registration and no published pricing
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - https://developer.express-scripts.com/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-08'
api_count: 1
apis:
- description: The partner-facing API estate Express Scripts exposes through its own gateway. The production host api.express-scripts.io and the sandbox host api-sandbox.express-scripts.io both answer HTTP 401 to ev
  name: Express Scripts Partner APIs
  slug: express-scripts-holding-partner-apis
artifact_total: 8
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/express-scripts-holding-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/express-scripts-holding-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/express-scripts-holding-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/express-scripts-holding-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/express-scripts-holding-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/express-scripts-holding-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/express-scripts-holding-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/express-scripts-holding-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/express-scripts-holding-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/express-scripts-holding-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/express-scripts-holding-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/express-scripts-holding-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/express-scripts-holding-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/express-scripts-holding-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/express-scripts-holding-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ExpressScripts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/express-scripts
- group: company
  title: ''
  type: Website
  url: https://www.express-scripts.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.express-scripts.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.express-scripts.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evernorth.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.express-scripts.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.express-scripts.com/frequently-asked-questions
- group: other
  title: ''
  type: ParentCompany
  url: https://www.evernorth.com/
coverage:
  checked: '2026-09-07'
  detail: 'Express Scripts runs a real API estate, but its developer portal ships the flag "public-specs": false in its own deployed configuration and its content backend at p-developer-portal.digitaledge.cigna.com answers {"message":"Missing Authentication Token"} with HTTP 403 on every path, so no specification is reachable without an approved partner account.'
  evidence:
  - status: 403
    url: https://p-developer-portal.digitaledge.cigna.com/specs
  - status: 200
    url: https://developer.express-scripts.com/service-apis
  - status: 401
    url: https://api.express-scripts.io/
  - status: 200
    url: https://p.login.developer.express-scripts.com/oauth2/default/.well-known/openid-configuration
  reason: partner-login
  state: gated
created: '2026-03-24'
description: 'Express Scripts is a pharmacy benefit management (PBM) company, now part of Cigna''s Evernorth Health Services, that processes prescription claims and provides home delivery and specialty pharmacy services for clients including health plans, employers and government programs. Express Scripts runs a real partner API estate — a production gateway at api.express-scripts.io, a separate sandbox gateway at api-sandbox.express-scripts.io, and its own OAuth 2.0 / OpenID Connect authorization server on an Express Scripts Okta tenant that serves live discovery documents anonymously. No API contract is published publicly: the developer portal renders client-side, its content backend refuses anonymous requests, and the portal''s own configuration sets public-specs to false, so specifications are visible only to approved partners after sign-in.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/express-scripts-holding.png
layout: provider
modified: '2026-09-07'
name: Express Scripts Holding
nav: Providers
network: true
overview: 'Express Scripts Holding publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Healthcare, Pharmacy, Pharmacy Benefit Management, and Prescriptions.


  Express Scripts Holding''s developer surface includes authentication, sandbox, support, and 21 more developer resources.'
plans:
- name: Express Scripts Holding Plans Pricing
  plan_count: 0
  slug: express-scripts-holding-plans-pricing
press:
- date: '2026-05-25'
  title: Express Scripts and Medco Health Solutions Sign ...
  url: https://www.prnewswire.com/news-releases/express-scripts-and-medco-health-solutions-sign-definitive-merger-agreement-medco-shareholders-to-receive-291-billion-125940848.html
- date: '2026-05-25'
  title: Express Scripts Complaint
  url: https://www.michigan.gov/ag/-/media/Project/Websites/AG/releases/2025/April/Express-Scripts-Complaint.pdf
- date: '2026-05-25'
  title: 'Wake Up Call: Cigna''s $54B Express Scripts Bid Faces ...'
  url: https://news.bloomberglaw.com/business-and-practice/wake-up-call-cignas-54b-express-scripts-bid-faces-long-review
- date: '2026-05-25'
  title: Cigna Uses AI to Check if Patients Are Taking Their ...
  url: https://www.wsj.com/articles/cigna-uses-ai-to-check-if-patients-are-taking-their-medications-11576174743
- date: '2026-05-25'
  title: Cigna acquires Express Scripts for $67 billion
  url: https://www.benefitscanada.com/news/bencan/cigna-acquires-express-scripts-for-67-billion/
random_paper: 12
rate_limits:
- limit_count: 0
  name: Express Scripts Holding Rate Limits
  slug: express-scripts-holding-rate-limits
scopes:
- name: Express Scripts Holding Scopes
  scope_count: 0
  slug: express-scripts-holding-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 31.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 73.8
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/express-scripts-holding/refs/heads/main/screenshots/express-scripts-holding-2026-06-20T180943.png
security:
- kind: authentication
  name: Express Scripts Holding Authentication
  slug: express-scripts-holding-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Express Scripts Holding Domain Security
  slug: express-scripts-holding-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Express Scripts Holding Vulnerability Disclosure
  slug: express-scripts-holding-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Express Scripts Holding Trust Center
  slug: express-scripts-holding-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: express-scripts-holding
tags:
- Health
- Healthcare
- Pharmacy
- Pharmacy Benefit Management
- Prescriptions
- Claims
- Fortune 100
website: https://www.express-scripts.com
---
