---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Activtrak Agentic Access
  operation_count: 23
  slug: activtrak-agentic-access
  summary_line: 23 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.activtrak.com
  baseurl_source: declared
  description: Administer the ActivTrak account (clients, consumers). Beta.
  name: ActivTrak Administration API
  slug: activtrak-administration-api
- baseURL: https://api.activtrak.com
  baseurl_source: declared
  description: SCIM 2.0 user and group management. Beta.
  name: ActivTrak Administration - SCIM API
  slug: activtrak-administration-scim-api
- baseURL: https://api.activtrak.com
  baseurl_source: declared
  description: HR Data Connector - submit CSV bulk user data.
  name: ActivTrak Bulk Import API
  slug: activtrak-bulk-import-api
- baseURL: https://api.activtrak.com
  baseurl_source: declared
  description: Live Data API - query activity reports (Working Hours, Activity Log).
  name: ActivTrak Reports API
  slug: activtrak-reports-api
artifact_total: 20
collections:
- collection_type: open
  name: ActivTrak Public APIs Administration API
  slug: open-activtrak-administration-api
- collection_type: open
  name: ActivTrak Public APIs Administration Administration - SCIM API
  slug: open-activtrak-administration-scim-api
- collection_type: open
  name: ActivTrak Public APIs Administration Bulk Import API
  slug: open-activtrak-bulk-import-api
- collection_type: open
  name: ActivTrak Public APIs Administration Reports API
  slug: open-activtrak-reports-api
common:
- group: other
  href: https://artifacts.apis.io/activtrak/capabilities/activtrak-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/activtrak-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/activtrak/plans/activtrak-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/activtrak-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.activtrak.com/blog/feed/
- group: agent
  href: https://artifacts.apis.io/activtrak/skills/activtrak-bulk-import-hr-data.md
  title: ''
  type: AgentSkill
  url: skills/activtrak-bulk-import-hr-data.md
- group: agent
  href: https://artifacts.apis.io/activtrak/mcp/activtrak-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/activtrak-mcp.yml
- group: other
  href: https://artifacts.apis.io/activtrak/overlays/activtrak-openapi-original-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activtrak-openapi-original-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/activtrak/authentication/activtrak-authentication.yml
  title: ''
  type: Authentication
  url: authentication/activtrak-authentication.yml
- group: auth
  href: https://artifacts.apis.io/activtrak/security/activtrak-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/activtrak-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/activtrak/security/activtrak-trust-center.yml
  title: ''
  type: Compliance
  url: security/activtrak-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/activtrak/security/activtrak-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/activtrak-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/activtrak/security/activtrak-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/activtrak-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/activtrak/security/activtrak-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/activtrak-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/activtrak/lifecycle/activtrak-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/activtrak-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.activtrak.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.activtrak.com/changelog/activtrak/activtrak-public-apis
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.activtrak.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.activtrak.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.activtrak.com/
- group: operate
  title: ''
  type: Support
  url: https://support.activtrak.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.activtrak.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.activtrak.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.activtrak.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://app.activtrak.com/
- group: company
  title: ''
  type: Website
  url: https://www.activtrak.com/
created: '2026-07-17'
description: 'ActivTrak is a workforce analytics and productivity-monitoring SaaS platform. Its Public APIs (v2) expose REST endpoints across three surfaces: the Live Data / Reports API (Working Hours and Activity Log), account administration (Clients, Consumers, and full SCIM 2.0 user and group management), and a Bulk Import HR Data Connector for CSV-driven user provisioning. Authentication is via an API key sent in the x-api-key header (a Bearer form is also accepted on some endpoints). Regional hosts are available for the United States, European Union, United Kingdom, Canada, and Australia. ActivTrak is backed by Sapphire Ventures and is profiled in the API Evangelist network.'
finops:
- has_sources: true
  method: derived
  name: Activtrak Finops
  primary_unit: worker
  service_category: ''
  slug: activtrak-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/activtrak.png
layout: provider
modified: '2026-10-06'
name: ActivTrak
nav: Providers
network: true
overview: 'ActivTrak publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Administration API, Administration - SCIM API, Bulk Import API, and 1 more. Tagged areas include Company, Software-as-a-Service, Workforce Analytics, Productivity, and Employee Monitoring.


  ActivTrak''s developer surface includes authentication, changelog, documentation, API reference, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Activtrak Plans Pricing
  plan_count: 6
  slug: activtrak-plans-pricing
- name: Activtrak Price Estimates
  plan_count: 0
  slug: activtrak-price-estimates
random_paper: 9
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 89.5
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 50.0
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/activtrak/activtrak-2026-07-25T181531.png
security:
- kind: authentication
  name: Activtrak Authentication
  slug: activtrak-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Activtrak Domain Security
  slug: activtrak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Activtrak Vulnerability Disclosure
  slug: activtrak-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Activtrak Trust Center
  slug: activtrak-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 4
skills:
- name: Bulk-import HR user data
  slug: activtrak-bulk-import-hr-data
- name: Manage app access (consumers)
  slug: activtrak-manage-app-access-consumers
- name: Provision users and groups via SCIM
  slug: activtrak-provision-scim-users-groups
- name: Pull activity and working-hours reports
  slug: activtrak-pull-activity-reports
slug: activtrak
tags:
- Company
- Software-as-a-Service
- Workforce Analytics
- Productivity
- Employee Monitoring
- Workforce Management
- SCIM
- Reporting
website: https://www.activtrak.com/
---
