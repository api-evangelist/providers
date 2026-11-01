---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Spycloud Agentic Access
  operation_count: 69
  slug: spycloud-agentic-access
  summary_line: 69 operations · 2 acting
api_count: 9
apis:
- baseURL: https://api.spycloud.io/enterprise-v2
  baseurl_source: declared
  description: The Breach API from SpyCloud — 23 operation(s) for breach.
  name: SpyCloud Breach API
  slug: spycloud-breach-api
- baseURL: https://api.spycloud.io/enterprise-v2
  baseurl_source: declared
  description: The Check API from SpyCloud — 2 operation(s) for check.
  name: SpyCloud Check API
  slug: spycloud-check-api
- baseURL: https://api.spycloud.io/enterprise-v2
  baseurl_source: declared
  description: The Compass API from SpyCloud — 5 operation(s) for compass.
  name: SpyCloud Compass API
  slug: spycloud-compass-api
- baseURL: https://api.spycloud.io/enterprise-v2
  baseurl_source: declared
  description: The Data API from SpyCloud — 2 operation(s) for data.
  name: SpyCloud Data API
  slug: spycloud-data-api
- baseURL: https://api.spycloud.io/enterprise-v2
  baseurl_source: declared
  description: The Query API from SpyCloud — 3 operation(s) for query.
  name: SpyCloud Query API
  slug: spycloud-query-api
- baseURL: https://api.spycloud.io/enterprise-v2
  baseurl_source: declared
  description: The Stats API from SpyCloud — 2 operation(s) for stats.
  name: SpyCloud Stats API
  slug: spycloud-stats-api
- baseURL: https://api.spycloud.io/enterprise-v2
  baseurl_source: declared
  description: The Watchlist API from SpyCloud — 5 operation(s) for watchlist.
  name: SpyCloud Watchlist API
  slug: spycloud-watchlist-api
artifact_total: 31
collections:
- collection_type: open
  name: Spycloud Breach API
  slug: open-spycloud-breach-api
- collection_type: open
  name: Spycloud Check API
  slug: open-spycloud-check-api
- collection_type: open
  name: enterprise-ato-prevention-api Compass API
  slug: open-spycloud-compass-api
- collection_type: open
  name: compromised-credit-card-api Data API
  slug: open-spycloud-data-api
- collection_type: open
  name: idlink-api Query API
  slug: open-spycloud-query-api
- collection_type: open
  name: prospecting-api Stats API
  slug: open-spycloud-stats-api
- collection_type: open
  name: enterprise-ato-prevention-api Watchlist API
  slug: open-spycloud-watchlist-api
common:
- group: commercial
  href: https://artifacts.apis.io/spycloud/plans/spycloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spycloud-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/spycloud/capabilities/spycloud-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/spycloud-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/spycloud/mcp/spycloud-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/spycloud-mcp.yml
- group: other
  href: https://artifacts.apis.io/spycloud/overlays/spycloud-compromised-credit-card-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/spycloud-compromised-credit-card-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/spycloud/agentic-access/spycloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/spycloud-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/spycloud/security/spycloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/spycloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/spycloud/security/spycloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spycloud-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/spycloud/authentication/spycloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spycloud-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://spycloud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spycloud.com/public-sc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spycloud.com/public-sc/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spycloud.com/public-sc/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spycloud.com/public-sc/docs/api-guidelines
- group: operate
  title: ''
  type: Support
  url: https://spycloud.com/support/
- group: company
  title: ''
  type: Blog
  url: https://spycloud.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://spycloud.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://spycloud.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://portal.spycloud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spycloud.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spycloud.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spycloud.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.spycloud.com/public-sc/page/release-notes-1
- group: auth
  title: ''
  type: Compliance
  url: https://spycloud.com/legal/governance-risk-and-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/spycloud.com/trust/itvhddyqxnnf6gi6aatcx
- group: auth
  title: ''
  type: Security
  url: https://spycloud.com/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/spycloud/well-known/spycloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spycloud-security.txt
- group: agent
  href: https://artifacts.apis.io/spycloud/well-known/spycloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spycloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/spycloud/well-known/spycloud-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/spycloud-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/spycloud/llms/spycloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spycloud-llms.txt
- group: design
  href: https://artifacts.apis.io/spycloud/conventions/spycloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/spycloud-conventions.yml
- group: design
  href: https://artifacts.apis.io/spycloud/errors/spycloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spycloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/spycloud/lifecycle/spycloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/spycloud-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/spycloud/changelog/spycloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/spycloud-changelog.yml
- group: design
  href: https://artifacts.apis.io/spycloud/conformance/spycloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spycloud-conformance.yml
- group: operate
  href: https://artifacts.apis.io/spycloud/rate-limits/spycloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/spycloud-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/spycloud/data-model/spycloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spycloud-data-model.yml
- group: auth
  href: https://artifacts.apis.io/spycloud/security/spycloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/spycloud-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/spycloud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: 'SpyCloud is an Austin, Texas based identity threat protection company that operates one of the largest repositories of recaptured darknet data — breach records, infostealer malware logs, phishing captures and combolists — and exposes it programmatically through a family of high-volume REST APIs. Security, fraud, identity and investigations teams query recaptured credentials, session cookies, exposed PII and infected-device telemetry to prevent account takeover, ransomware, session hijacking and online fraud. The public API surface spans nine separately-licensed products: Enterprise (Employee) ATO Prevention, Consumer ATO Prevention, Cybercrime Investigations, Data Partnership, IDLink identity correlation, Compromised Credit Card, Prospecting, NIST Password check, and Session Identity Protection. All are REST/JSON, authenticated with an x-api-key header, IP allow-listed, cursor-paginated at 1,000 records per page, and backed by a 99.9% uptime SLA.'
finops:
- has_sources: true
  method: derived
  name: Spycloud Finops
  primary_unit: ''
  service_category: ''
  slug: spycloud-finops
  template: true
image: https://spycloud.com/wp-content/uploads/2025/04/bg-img-dotted-lines-1920x700-1-1.png
layout: provider
modified: '2026-08-05'
name: SpyCloud
nav: Providers
network: true
overview: 'SpyCloud publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Breach API, Check API, Compass API, and 4 more. Tagged areas include Cybersecurity, Threat Intelligence, Identity, Fraud Prevention, and Account Takeover.


  SpyCloud''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Spycloud Plans Pricing
  plan_count: 3
  slug: spycloud-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Spycloud Rate Limits
  slug: spycloud-rate-limits
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.3
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 47.7
    developer_ergonomics: 58.9
    discoverability: 71.4
    operational_transparency: 42.1
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/spycloud/spycloud-2026-08-17T082052.png
security:
- kind: authentication
  name: Spycloud Authentication
  slug: spycloud-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Spycloud Domain Security
  slug: spycloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spycloud Vulnerability Disclosure
  slug: spycloud-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Spycloud Trust Center
  slug: spycloud-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 9
skills:
- name: Monitor compromised cards by BIN
  slug: spycloud-compromised-card-monitoring
- name: Check a consumer login for credential exposure
  slug: spycloud-consumer-login-risk-check
- name: Size up exposure for a domain or email without pulling records
  slug: spycloud-domain-exposure-assessment
- name: Triage employee credential exposure
  slug: spycloud-employee-ato-triage
- name: Correlate an identity across recaptured data with IDLink
  slug: spycloud-identity-correlation-idlink
- name: Investigate a malware-infected device and its exposed applications
  slug: spycloud-malware-infection-remediation
- name: Screen a password against compromised-credential data
  slug: spycloud-nist-password-screening
- name: Find stolen session cookies for a domain
  slug: spycloud-session-hijacking-exposure
- name: Pivot across recaptured data to profile a threat actor
  slug: spycloud-threat-actor-investigation
slug: spycloud
tags:
- Cybersecurity
- Threat Intelligence
- Identity
- Fraud Prevention
- Account Takeover
- Dark Web
- Breach Data
- Malware
- Authentication
- Security
website: https://spycloud.com/
---
