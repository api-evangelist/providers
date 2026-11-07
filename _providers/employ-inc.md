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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://status.employinc.com/api/v2
  baseurl_source: declared
  description: 'The public Atlassian Statuspage API on status.employinc.com. Eight anonymous endpoints report the rollup availability indicator, every monitored Employ platform component, the dated incident timeline '
  name: Employ Inc Status API
  slug: employ-inc-status-api
- description: 'The public WordPress REST API (wp-json) of the Employ Inc website at www.employinc.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate '
  name: Employ Inc Website (WordPress REST)
  slug: employinc-com-website-wordpress-rest
- baseURL: https://status.employinc.com/api/v2
  baseurl_source: declared
  description: Individually monitored Employ platform components.
  name: Employ Components API
  slug: employ-inc-components-api
- baseURL: https://status.employinc.com/api/v2
  baseurl_source: declared
  description: Incidents and their dated update timelines.
  name: Employ Incidents API
  slug: employ-inc-incidents-api
- baseURL: https://status.employinc.com/api/v2
  baseurl_source: declared
  description: Scheduled maintenance windows.
  name: Employ Maintenance API
  slug: employ-inc-maintenance-api
- baseURL: https://status.employinc.com/api/v2
  baseurl_source: declared
  description: The one-call rollup of everything on the page.
  name: Employ Summary API
  slug: employ-inc-summary-api
artifact_total: 20
asyncapis:
- description: ''
  name: Employ Inc Status Webhooks
  slug: employ-inc-status-webhooks
common:
- group: other
  href: https://artifacts.apis.io/employ-inc/capabilities/employ-inc-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/employ-inc-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/employ-inc/overlays/employ-inc-content-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/employ-inc-content-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/employ-inc/overlays/employ-inc-events-calendar-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/employ-inc-events-calendar-rest-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/employ-inc/security/employ-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/employ-inc-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/employ-inc/authentication/employ-inc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/employ-inc-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.employinc.com/
- group: company
  title: ''
  type: Blog
  url: https://www.employinc.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.employinc.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.employinc.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.employinc.com/privacy-notice-general/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Employ-Inc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.employinc.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/82904967
- group: agent
  href: https://artifacts.apis.io/employ-inc/llms/employ-inc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/employ-inc-llms.txt
- group: design
  href: https://artifacts.apis.io/employ-inc/conventions/employ-inc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/employ-inc-conventions.yml
- group: design
  href: https://artifacts.apis.io/employ-inc/errors/employ-inc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/employ-inc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/employ-inc/lifecycle/employ-inc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/employ-inc-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/employ-inc/conformance/employ-inc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/employ-inc-conformance.yml
- group: auth
  href: https://artifacts.apis.io/employ-inc/conformance/employ-inc-conformance.yml
  title: ''
  type: Compliance
  url: conformance/employ-inc-conformance.yml
- group: auth
  href: https://artifacts.apis.io/employ-inc/security/employ-inc-security-policy.yml
  title: ''
  type: Security
  url: security/employ-inc-security-policy.yml
- group: design
  href: https://artifacts.apis.io/employ-inc/data-model/employ-inc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/employ-inc-data-model.yml
- group: build
  href: https://artifacts.apis.io/employ-inc/packages/employ-inc-packages.yml
  title: ''
  type: Packages
  url: packages/employ-inc-packages.yml
- group: agent
  href: https://artifacts.apis.io/employ-inc/mcp/employ-inc-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/employ-inc-mcp.yml
- group: design
  href: https://artifacts.apis.io/employ-inc/asyncapi/employ-inc-status-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/employ-inc-status-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/employ-inc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/employ-inc/plans/employ-inc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/employ-inc-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/employ-inc/rate-limits/employ-inc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/employ-inc-rate-limits.yml
created: '2026-09-13'
description: 'Employ, Inc. is the Denver-based parent company of the JazzHR, Lever and Jobvite applicant tracking systems, and of the AI Interview, Screening and Sourcing Companions layered across them. Employ itself runs no developer program: the recruiting APIs its customers integrate against are published under each brand''s own domain and are profiled separately in this network. What Employ publishes on employinc.com is a corporate surface that is nonetheless machine-readable — the WordPress REST API behind its site, two self-describing Events Calendar REST contracts, and an anonymous Atlassian Statuspage API on status.employinc.com — plus the legal, security and responsible-AI documents (Security Exhibit, DPAs, SLAs, NYC Local Law 144 bias audit) that govern every brand underneath it.'
examples:
- key_count: 2
  name: Employ Inc Status Components
  slug: employ-inc-status-components
- key_count: 2
  name: Employ Inc Status Incidents
  slug: employ-inc-status-incidents
- key_count: 5
  name: Employ Inc Status Summary
  slug: employ-inc-status-summary
finops:
- has_sources: true
  method: derived
  name: Employ Inc Finops
  primary_unit: ''
  service_category: ''
  slug: employ-inc-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/employ-inc.png
layout: provider
modified: '2026-09-13'
name: Employ
nav: Providers
network: true
overview: 'Employ publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Inc Status API, Components API, Incidents API, and 3 more. Tagged areas include Human Resources, Recruiting, Talent Acquisition, Applicant Tracking, and Hiring.


  The Employ catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Employ''s developer surface includes authentication, engineering blog, support, and 24 more developer resources.'
plans:
- name: Employ Inc Plans Pricing
  plan_count: 0
  slug: employ-inc-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Employ Inc Rate Limits
  slug: employ-inc-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Employ API Rules
  rule_count: 68
  severity_counts:
    error: 60
    hint: 0
    info: 2
    warn: 6
  slug: employ-inc-rules
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 28.9
    contract_governance: 31.8
    contract_quality: 61.5
    developer_ergonomics: 25.6
    discoverability: 69.6
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 44.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa-cpra
    jurisdictions_satisfied: 2
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 37.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/employ-inc/employ-inc-2026-10-11T104149.png
security:
- kind: authentication
  name: Employ Inc Authentication
  slug: employ-inc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Employ Inc Domain Security
  slug: employ-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: employ-inc-check-platform-status
  slug: employ-inc-check-platform-status
- name: employ-inc-list-events
  slug: employ-inc-list-events
- name: employ-inc-monitor-incidents
  slug: employ-inc-monitor-incidents
- name: employ-inc-search-content
  slug: employ-inc-search-content
slug: employ-inc
tags:
- Human Resources
- Recruiting
- Talent Acquisition
- Applicant Tracking
- Hiring
- Content
- Event
- Status
website: https://www.employinc.com/
---
