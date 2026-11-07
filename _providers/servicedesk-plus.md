---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-11-06'
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
artifact_total: 14
collections:
- collection_type: open
  name: ManageEngine ServiceDesk Plus Cloud Requests API
  slug: open-servicedesk-plus-requests-api
- collection_type: open
  name: ManageEngine ServiceDesk Plus Cloud API
  slug: open-servicedesk-plus
common:
- group: commercial
  href: https://artifacts.apis.io/servicedesk-plus/finops/servicedesk-plus-finops.yml
  title: ''
  type: FinOps
  url: finops/servicedesk-plus-finops.yml
- group: commercial
  href: https://artifacts.apis.io/servicedesk-plus/plans/servicedesk-plus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/servicedesk-plus-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/servicedesk-plus/rules/servicedesk-plus-rules.yml
  title: ''
  type: Spectral
  url: rules/servicedesk-plus-rules.yml
- group: design
  href: https://artifacts.apis.io/servicedesk-plus/vocabulary/servicedesk-plus-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/servicedesk-plus-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/servicedesk-plus/skills/_index.yml
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
  href: https://artifacts.apis.io/servicedesk-plus/conformance/servicedesk-plus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/servicedesk-plus-conformance.yml
- group: other
  href: https://artifacts.apis.io/servicedesk-plus/overlays/servicedesk-plus-requests-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/servicedesk-plus-requests-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/servicedesk-plus/llms/servicedesk-plus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/servicedesk-plus-llms.txt
- group: auth
  href: https://artifacts.apis.io/servicedesk-plus/well-known/servicedesk-plus-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/servicedesk-plus-security.txt
- group: agent
  href: https://artifacts.apis.io/servicedesk-plus/well-known/servicedesk-plus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/servicedesk-plus-well-known.yml
- group: other
  href: https://artifacts.apis.io/servicedesk-plus/hosts/servicedesk-plus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/servicedesk-plus-hosts.yml
- group: build
  href: https://artifacts.apis.io/servicedesk-plus/integrations/servicedesk-plus-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/servicedesk-plus-integration-edges.yml
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
- group: other
  href: https://artifacts.apis.io/servicedesk-plus/capabilities/servicedesk-plus-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/servicedesk-plus-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/servicedesk-plus/agentic-access/servicedesk-plus-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/servicedesk-plus-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/servicedesk-plus/security/servicedesk-plus-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/servicedesk-plus-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/servicedesk-plus/security/servicedesk-plus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/servicedesk-plus-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/servicedesk-plus/security/servicedesk-plus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/servicedesk-plus-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/servicedesk-plus/authentication/servicedesk-plus-authentication.yml
  title: ''
  type: Authentication
  url: authentication/servicedesk-plus-authentication.yml
- group: auth
  href: https://artifacts.apis.io/servicedesk-plus/scopes/servicedesk-plus-scopes.yml
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
created: '2026-05-11'
description: ManageEngine ServiceDesk Plus is a comprehensive IT service management (ITSM) suite with incident, problem, change, release, and asset management modules, plus a CMDB and project management. ServiceDesk Plus is available as cloud (SaaS) or on-premises, and exposes a REST API for integrating external systems with requests, problems, changes, assets, and the CMDB.
finops:
- has_sources: true
  method: derived
  name: Servicedesk Plus Finops
  primary_unit: seat
  service_category: ''
  slug: servicedesk-plus-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/servicedesk-plus.png
layout: provider
modified: '2026-05-11'
name: ManageEngine ServiceDesk Plus
nav: Providers
network: true
overview: 'ManageEngine ServiceDesk Plus publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Requests API, and 1 more. Tagged areas include ITSM, Help Desk, Incident Management, Asset Management, and CMDB.


  The ManageEngine ServiceDesk Plus catalog on APIs.io includes 1 Spectral governance ruleset.


  ManageEngine ServiceDesk Plus'' developer surface includes signup flow, authentication, documentation, pricing, engineering blog, and 25 more developer resources.'
plans:
- name: Servicedesk Plus Plans Pricing
  plan_count: 3
  slug: servicedesk-plus-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: ManageEngine ServiceDesk Plus API Rules
  rule_count: 35
  severity_counts:
    error: 33
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
  composite: 48.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.3
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 42.9
    developer_ergonomics: 25.6
    discoverability: 75.0
    operational_transparency: 28.9
  previous_composite: 42.8
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
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/servicedesk-plus/servicedesk-plus-2026-06-20T193729.png
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
skill_count: 1
skills:
- name: servicedesk-plus-create-and-retrieve-request
  slug: servicedesk-plus-create-and-retrieve-request
slug: servicedesk-plus
tags:
- ITSM
- Help Desk
- Incident Management
- Asset Management
- CMDB
website: https://www.manageengine.com/products/service-desk/
---
