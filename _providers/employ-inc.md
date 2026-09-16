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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-09-15'
api_count: 4
apis:
- baseURL: https://www.employinc.com/wp-json/wp/v2
  baseurl_source: declared
  description: 'The WordPress REST API Employ, Inc. serves at www.employinc.com/wp-json/wp/v2. It exposes the Employ corporate site as JSON: blog posts, marketing and legal pages, media, the resource, case-study, new'
  name: Employ Inc Content API
  slug: employ-inc-content-api
- baseURL: https://www.employinc.com/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The Events Calendar REST API (tribe/events/v1) for Employ, Inc. events and webinars, with a self-describing OpenAPI 3.0.0 contract the host publishes at its own /doc endpoint. Covers events, venues, o
  name: Employ Inc Events Calendar REST API
  slug: employ-inc-events-calendar-rest-api
- baseURL: https://www.employinc.com/wp-json/tec/v1
  baseurl_source: declared
  description: 'The newer tec/v1 generation of The Events Calendar REST API on www.employinc.com, published as a self-describing OpenAPI 3.0.4 contract at its own /docs endpoint. Covers events, organizers and venues '
  name: Employ Inc TEC Events REST API
  slug: employ-inc-tec-events-rest-api
- baseURL: https://status.employinc.com/api/v2
  baseurl_source: declared
  description: 'The public Atlassian Statuspage API on status.employinc.com. Eight anonymous endpoints report the rollup availability indicator, every monitored Employ platform component, the dated incident timeline '
  name: Employ Inc Status API
  slug: employ-inc-status-api
artifact_total: 16
asyncapis:
- description: ''
  name: Employ Inc Status Webhooks
  slug: employ-inc-status-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/security/employ-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/employ-inc-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/authentication/employ-inc-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/llms/employ-inc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/employ-inc-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/conventions/employ-inc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/employ-inc-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/errors/employ-inc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/employ-inc-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/lifecycle/employ-inc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/employ-inc-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/conformance/employ-inc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/employ-inc-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/conformance/employ-inc-conformance.yml
  title: ''
  type: Compliance
  url: conformance/employ-inc-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/security/employ-inc-security-policy.yml
  title: ''
  type: Security
  url: security/employ-inc-security-policy.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/data-model/employ-inc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/employ-inc-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/packages/employ-inc-packages.yml
  title: ''
  type: Packages
  url: packages/employ-inc-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/mcp/employ-inc-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/employ-inc-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/asyncapi/employ-inc-status-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/employ-inc-status-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/plans/employ-inc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/employ-inc-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/employ-inc/refs/heads/main/rate-limits/employ-inc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/employ-inc-rate-limits.yml
created: '2026-09-13'
description: 'Employ, Inc. is the Denver-based parent company of the JazzHR, Lever and Jobvite applicant tracking systems, and of the AI Interview, Screening and Sourcing Companions layered across them. Employ itself runs no developer program: the recruiting APIs its customers integrate against are published under each brand''s own domain and are profiled separately in this network. What Employ publishes on employinc.com is a corporate surface that is nonetheless machine-readable — the WordPress REST API behind its site, two self-describing Events Calendar REST contracts, and an anonymous Atlassian Statuspage API on status.employinc.com — plus the legal, security and responsible-AI documents (Security Exhibit, DPAs, SLAs, NYC Local Law 144 bias audit) that govern every brand underneath it.'
examples:
- key_count: 22
  name: Employ Inc Content Types
  slug: employ-inc-content-types
- key_count: 4
  name: Employ Inc Event Venues
  slug: employ-inc-event-venues
- key_count: 4
  name: Employ Inc Events
  slug: employ-inc-events
- key_count: 2
  name: Employ Inc Status Components
  slug: employ-inc-status-components
- key_count: 2
  name: Employ Inc Status Incidents
  slug: employ-inc-status-incidents
- key_count: 5
  name: Employ Inc Status Summary
  slug: employ-inc-status-summary
- key_count: 9
  name: Employ Inc Taxonomies
  slug: employ-inc-taxonomies
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/employ-inc.png
layout: provider
modified: '2026-09-13'
name: Employ Inc
nav: Providers
network: true
overview: 'Employ Inc publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Content API, Events Calendar REST API, TEC Events REST API, and 1 more. Tagged areas include Human Resources, Recruiting, Talent Acquisition, Applicant Tracking, and ATS.


  The Employ Inc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Employ Inc''s developer surface includes authentication, engineering blog, support, and 21 more developer resources.'
plans:
- name: Employ Inc Plans Pricing
  plan_count: 0
  slug: employ-inc-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Employ Inc Rate Limits
  slug: employ-inc-rate-limits
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 65.4
    developer_ergonomics: 28.0
    discoverability: 81.5
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 42.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Employ Inc Authentication
  slug: employ-inc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Employ Inc Domain Security
  slug: employ-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: employ-inc
tags:
- Human Resources
- Recruiting
- Talent Acquisition
- Applicant Tracking
- ATS
- Hiring
- HR Tech
- Content
- Event
- Status
website: https://www.employinc.com/
---
