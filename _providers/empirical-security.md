---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Empirical Security Agentic Access
  operation_count: 9
  slug: empirical-security-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://app.empiricalsecurity.com/api
  baseurl_source: declared
  description: Saved CVE queries and their execution.
  name: Empirical Security CVE Groups API
  slug: empirical-security-cve-groups-api
- baseURL: https://app.empiricalsecurity.com/api
  baseurl_source: declared
  description: Query CVEs using Empirical search syntax.
  name: Empirical Security Search API
  slug: empirical-security-search-api
- baseURL: https://app.empiricalsecurity.com/api
  baseurl_source: declared
  description: Retrieve CVE detail, scores, malware hashes and history.
  name: Empirical Security CV Es API
  slug: empirical-security-cves-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Empirical Security CVE Groups API
  slug: open-empirical-security-cve-groups-api
- collection_type: open
  name: Empirical Security CVE Groups CVEs API
  slug: open-empirical-security-cves-api
- collection_type: open
  name: Empirical Security CVE Groups Search API
  slug: open-empirical-security-search-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/overlays/empirical-security-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/empirical-security-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.empiricalsecurity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.empiricalsecurity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.empiricalsecurity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.empiricalsecurity.com/api_reference/cves
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.empiricalsecurity.com/authentication
- group: company
  title: ''
  type: Blog
  url: https://research.empiricalsecurity.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.empiricalsecurity.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.empiricalsecurity.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.empiricalsecurity.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.empiricalsecurity.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/authentication/empirical-security-authentication.yml
  title: ''
  type: Authentication
  url: authentication/empirical-security-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/scopes/empirical-security-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/empirical-security-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/errors/empirical-security-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/empirical-security-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/conventions/empirical-security-conventions.yml
  title: ''
  type: Conventions
  url: conventions/empirical-security-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/lifecycle/empirical-security-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/empirical-security-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/conformance/empirical-security-conformance.yml
  title: ''
  type: Conformance
  url: conformance/empirical-security-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/data-model/empirical-security-data-model.yml
  title: ''
  type: DataModel
  url: data-model/empirical-security-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/well-known/empirical-security-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/empirical-security-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/mcp/empirical-security-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/empirical-security-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/agentic-access/empirical-security-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/empirical-security-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/llms/empirical-security-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/empirical-security-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/security/empirical-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/empirical-security-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Empirical Security builds data-driven models that predict which vulnerabilities will actually be exploited, so security teams can prioritize remediation by real-world risk instead of raw CVSS severity. It operates the Foundation (global) model, which combines real-time internet exploitation telemetry with EPSS and monitors 18,000+ exploited CVEs; hourly-updated EPSS models (epss_v3, epss_v4, epss_v5); and Radiant, an organization-specific model that layers your local assets, configurations and internal telemetry on top of the Foundation data. The read-only REST API exposes CVE detail, per-model scores and percentiles, malware hashes, critical indicators, score history, change history, full dataset export, search, and saved CVE groups, secured with OAuth 2.0 client credentials (JWT bearer). Empirical Security is backed by Costanoa Ventures.
image: https://www.empiricalsecurity.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Empirical Security
nav: Providers
network: true
overview: 'Empirical Security publishes 3 APIs on the [APIs.io](https://apis.io/) network: CVE Groups API, Search API, and CV Es API. Tagged areas include Company, Security, Cybersecurity, Vulnerability Management, and Vulnerability Prioritization.


  Empirical Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 13
scopes:
- name: Empirical Security Scopes
  scope_count: 1
  slug: empirical-security-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.6
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 14.5
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 29.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/screenshots/empirical-security-2026-07-25T213247.png
security:
- kind: authentication
  name: Empirical Security Authentication
  slug: empirical-security-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Empirical Security Domain Security
  slug: empirical-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: empirical-security
tags:
- Company
- Security
- Cybersecurity
- Vulnerability Management
- Vulnerability Prioritization
- CVE
- EPSS
- Exploit Prediction
- Threat Intelligence
website: https://www.empiricalsecurity.com
---
