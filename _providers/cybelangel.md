---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-10-31'
api_count: 7
apis:
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Manipulate ADM inventory assets and threats.
  name: CybelAngel ADM Inventory API
  slug: cybelangel-adm-inventory-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Alerts
  name: CybelAngel Alerts API
  slug: cybelangel-alerts-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Accessing the application assets
  name: CybelAngel Asset API
  slug: cybelangel-asset-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Audit Logs Public API
  name: CybelAngel audit logs API
  slug: cybelangel-audit-logs-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Credentials incident reports and credentials
  name: CybelAngel Credential watchlist API
  slug: cybelangel-credential-watchlist-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Domain Protection
  name: CybelAngel Domain watchlist API
  slug: cybelangel-domain-watchlist-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Manipulate incident reports.
  name: CybelAngel Incident reports API
  slug: cybelangel-incident-reports-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Manipulate keywords.
  name: CybelAngel Keywords API
  slug: cybelangel-keywords-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: The Reports API from CybelAngel — 1 operation(s) for reports.
  name: CybelAngel Reports API
  slug: cybelangel-reports-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Statistics on the reports, keywords, etc.
  name: CybelAngel Stats API
  slug: cybelangel-stats-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Alerts - Stix
  name: CybelAngel Stix API
  slug: cybelangel-stix-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: Fetch threat intelligence data from the CybelAngel platform.
  name: CybelAngel Threat Intelligence API
  slug: cybelangel-threat-intelligence-api
- baseURL: https://platform.cybelangel.com/api
  baseurl_source: declared
  description: List workspaces.
  name: CybelAngel Workspaces API
  slug: cybelangel-workspaces-api
artifact_total: 27
common:
- group: other
  href: https://artifacts.apis.io/cybelangel/capabilities/cybelangel-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cybelangel-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/cybelangel/overlays/cybelangel-platform-reports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cybelangel-platform-reports-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cybelangel/overlays/cybelangel-alerts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cybelangel-alerts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cybelangel/overlays/cybelangel-adm-inventory-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cybelangel-adm-inventory-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cybelangel/overlays/cybelangel-keywords-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cybelangel-keywords-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cybelangel/overlays/cybelangel-threat-intelligence-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cybelangel-threat-intelligence-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cybelangel/overlays/cybelangel-audit-logs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cybelangel-audit-logs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cybelangel/overlays/cybelangel-partner-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cybelangel-partner-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.cybelangel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cybelangel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cybelangel.com/docs/cybelangel-platform-api/39d4926befc14-what-can-i-do-with-this-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cybelangel.com/docs/cybelangel-platform-api/68a341c676710-references
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cybelangel.com/docs/cybelangel-platform-api/05d245301ecc5-get-your-api-credentials
- group: operate
  title: ''
  type: Support
  url: https://cybelangel.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://cybelangel.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://cybelangel.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CybelAngel
- group: operate
  title: ''
  type: ChangeLog
  url: https://cybelangel.com/changelog/
- group: operate
  title: ''
  type: Roadmap
  url: https://cybelangel.com/changelog/
- group: start
  title: ''
  type: SignUp
  url: https://cybelangel.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://platform.cybelangel.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cybelangel.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cybelangel.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://cybelangel.com/solutions/compliance-cybelangel/
- group: auth
  title: ''
  type: Security
  url: https://cybelangel.com/security.txt
- group: auth
  href: https://artifacts.apis.io/cybelangel/well-known/cybelangel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cybelangel-security.txt
- group: agent
  href: https://artifacts.apis.io/cybelangel/well-known/cybelangel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cybelangel-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.cybelangel.com/.well-known/openid-configuration
- group: auth
  href: https://artifacts.apis.io/cybelangel/authentication/cybelangel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cybelangel-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cybelangel/scopes/cybelangel-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cybelangel-scopes.yml
- group: design
  href: https://artifacts.apis.io/cybelangel/conventions/cybelangel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cybelangel-conventions.yml
- group: operate
  href: https://artifacts.apis.io/cybelangel/rate-limits/cybelangel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cybelangel-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cybelangel/plans/cybelangel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cybelangel-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cybelangel/lifecycle/cybelangel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cybelangel-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cybelangel/changelog/cybelangel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cybelangel-changelog.yml
- group: design
  href: https://artifacts.apis.io/cybelangel/errors/cybelangel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cybelangel-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cybelangel/data-model/cybelangel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cybelangel-data-model.yml
- group: design
  href: https://artifacts.apis.io/cybelangel/conformance/cybelangel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cybelangel-conformance.yml
- group: build
  href: https://artifacts.apis.io/cybelangel/packages/cybelangel-packages.yml
  title: ''
  type: Packages
  url: packages/cybelangel-packages.yml
- group: start
  href: https://artifacts.apis.io/cybelangel/sandbox/cybelangel-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cybelangel-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/cybelangel/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cybelangel/llms/cybelangel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cybelangel-llms.txt
- group: auth
  href: https://artifacts.apis.io/cybelangel/security/cybelangel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cybelangel-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cybelangel/security/cybelangel-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cybelangel-vulnerability-disclosure.yml
created: '2026-08-17'
description: CybelAngel is a Paris- and Boston-based external risk protection company that scans the public internet, the deep and dark web, connected devices, cloud storage, code-sharing and paste sites for a customer's exposed data and unmanaged assets. Its platform covers external attack surface (ADM) inventory, data-breach prevention, credential intelligence, brand protection and domain/social-media impersonation, cyber threat intelligence, and analyst-led remediation. For developers it publishes seven documented REST APIs on a Stoplight developer portal — Reports (incident reports, credential and domain watchlists, assets, remediation requests), Alerts in Feed (real-time alerts, also served in OASIS STIX format), ADM Inventory, Keywords, Threat Intelligence claimed-attacks, Audit Logs and a Partner API for MSSPs managing client organizations — all authenticated with OAuth 2.0 client-credentials bearer tokens minted by an Auth0 tenant, plus CybelAngel Connect, a no-code automation studio
  for ServiceNow, Jira, Splunk, Slack, Cortex XSOAR, IBM Security SOAR and Azure Sentinel.
finops:
- has_sources: true
  method: derived
  name: Cybelangel Finops
  primary_unit: ''
  service_category: ''
  slug: cybelangel-finops
  template: true
image: https://cybelangel.com/wp-content/uploads/2026/08/langEN-1-90764-1280x460.avif
layout: provider
modified: '2026-08-17'
name: CybelAngel
nav: Providers
network: true
overview: 'CybelAngel publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including ADM Inventory API, Alerts API, Asset API, and 10 more. Tagged areas include Company, Cybersecurity, Threat Intelligence, external-attack-surface-management, and data-breach-prevention.


  CybelAngel''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, signup flow, and 37 more developer resources.'
plans:
- name: Cybelangel Plans Pricing
  plan_count: 0
  slug: cybelangel-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Cybelangel Rate Limits
  slug: cybelangel-rate-limits
scopes:
- name: Cybelangel Scopes
  scope_count: 10
  slug: cybelangel-scopes
  summary_line: 10 scopes · clientCredentials
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 52.3
    developer_ergonomics: 66.1
    discoverability: 71.4
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 57.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cybelangel/cybelangel-2026-09-02T145211.png
security:
- kind: authentication
  name: Cybelangel Authentication
  slug: cybelangel-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Cybelangel Domain Security
  slug: cybelangel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cybelangel Vulnerability Disclosure
  slug: cybelangel-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 7
skills:
- name: Authenticate to the CybelAngel APIs
  slug: cybelangel-authenticate
- name: Export CybelAngel audit logs and threat intelligence
  slug: cybelangel-export-audit-logs
- name: Manage monitored keywords
  slug: cybelangel-manage-keywords
- name: Poll the CybelAngel alert feed into a SIEM
  slug: cybelangel-poll-alert-feed
- name: Triage the external attack surface
  slug: cybelangel-triage-attack-surface
- name: Triage leaked credentials
  slug: cybelangel-triage-leaked-credentials
- name: Work CybelAngel incident reports end to end
  slug: cybelangel-work-incident-reports
slug: cybelangel
tags:
- Company
- Cybersecurity
- Threat Intelligence
- external-attack-surface-management
- data-breach-prevention
- Credential Intelligence
- Brand Protection
- Dark Web Monitoring
- Digital Risk Protection
- STIX
- security-alerts
- Asset Inventory
- Audit Logs
website: https://www.cybelangel.com/
---
