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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Servicedesk Plus Agentic Access
  operation_count: 6
  slug: servicedesk-plus-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: REST API for ServiceDesk Plus enabling programmatic management of requests, problems, changes, releases, assets, the CMDB, users, technicians, projects, and configuration items.
  name: ServiceDesk Plus REST API
  slug: rest-api
- baseURL: https://sdpondemand.manageengine.com/api/v3
  baseurl_source: declared
  description: The Requests API from ManageEngine ServiceDesk Plus — 3 operation(s) for requests.
  name: ManageEngine ServiceDesk Plus Requests API
  slug: servicedesk-plus-requests-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ManageEngine ServiceDesk Plus Cloud Requests API
  slug: open-servicedesk-plus-requests-api
- collection_type: open
  name: ManageEngine ServiceDesk Plus Cloud API
  slug: open-servicedesk-plus
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/plans/servicedesk-plus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/servicedesk-plus-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/rules/servicedesk-plus-rules.yml
  title: ''
  type: Spectral
  url: rules/servicedesk-plus-rules.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.manageengine.com/cybersecurity-solutions.html
- group: auth
  title: ''
  type: Security
  url: https://bugbounty.zohocorp.com/bb/info
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/conformance/servicedesk-plus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/servicedesk-plus-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/overlays/servicedesk-plus-requests-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/servicedesk-plus-requests-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/llms/servicedesk-plus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/servicedesk-plus-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/well-known/servicedesk-plus-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/servicedesk-plus-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/well-known/servicedesk-plus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/servicedesk-plus-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/hosts/servicedesk-plus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/servicedesk-plus-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.manageengine.com/
- group: start
  title: ''
  type: SignUp
  url: https://sdpondemand.manageengine.com/Register.do?new-index
- group: company
  title: ''
  type: Newsroom
  url: https://www.manageengine.com/news/in-the-news.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.servicedeskplus.com/requests/first-call-resolution.html
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/agentic-access/servicedesk-plus-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/servicedesk-plus-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/security/servicedesk-plus-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/servicedesk-plus-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/security/servicedesk-plus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/servicedesk-plus-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/security/servicedesk-plus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/servicedesk-plus-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/authentication/servicedesk-plus-authentication.yml
  title: ''
  type: Authentication
  url: authentication/servicedesk-plus-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/scopes/servicedesk-plus-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/servicedesk-plus-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ManageEngine
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manageengine-it-service-management
- group: company
  title: ''
  type: Website
  url: https://www.manageengine.com/products/service-desk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.manageengine.com/products/service-desk/help/adminguide/api/rest-api.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.manageengine.com/products/service-desk/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.manageengine.com/feed
coverage:
  checked: '2026-10-04'
  detail: No OpenAPI or other machine-readable contract found despite probing known API hosts and documentation pages.
  evidence:
  - status: 0
    url: https://api.manageengine.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-11'
description: ManageEngine ServiceDesk Plus is a comprehensive IT service management (ITSM) suite with incident, problem, change, release, and asset management modules, plus a CMDB and project management. ServiceDesk Plus is available as cloud (SaaS) or on-premises, and exposes a REST API for integrating external systems with requests, problems, changes, assets, and the CMDB.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/servicedesk-plus.png
layout: provider
modified: '2026-05-11'
name: ManageEngine ServiceDesk Plus
nav: Providers
network: true
overview: 'ManageEngine ServiceDesk Plus publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Requests API, and 1 more. Tagged areas include ITSM, Help Desk, Incident Management, Asset Management, and CMDB.


  The ManageEngine ServiceDesk Plus catalog on APIs.io includes 1 Spectral governance ruleset.


  ManageEngine ServiceDesk Plus'' developer surface includes signup flow, getting-started guide, authentication, documentation, pricing, engineering blog, and 21 more developer resources.'
plans:
- name: Servicedesk Plus Plans Pricing
  plan_count: 3
  slug: servicedesk-plus-plans-pricing
random_paper: 1
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: ManageEngine ServiceDesk Plus API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: servicedesk-plus-rules
scopes:
- name: Servicedesk Plus Scopes
  scope_count: 5
  slug: servicedesk-plus-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.9
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 37.5
    discoverability: 75.0
    operational_transparency: 28.9
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/screenshots/servicedesk-plus-2026-06-20T193729.png
security:
- kind: authentication
  name: Servicedesk Plus Authentication
  slug: servicedesk-plus-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Servicedesk Plus Domain Security
  slug: servicedesk-plus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Servicedesk Plus Vulnerability Disclosure
  slug: servicedesk-plus-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Servicedesk Plus Trust Center
  slug: servicedesk-plus-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: servicedesk-plus
tags:
- ITSM
- Help Desk
- Incident Management
- Asset Management
- CMDB
website: https://www.manageengine.com/products/service-desk/
---
