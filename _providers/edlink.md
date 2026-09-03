---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Edlink Agentic Access
  operation_count: 22
  slug: edlink-agentic-access
  summary_line: 22 operations · 1 acting
api_count: 1
apis:
- baseURL: https://ed.link/api/v2
  baseurl_source: declared
  description: Institution-level roster and school data.
  name: Edlink Graph API
  slug: edlink-graph-api
- baseURL: https://ed.link/api/v2
  baseurl_source: declared
  description: Source and integration metadata.
  name: Edlink Integrations API
  slug: edlink-integrations-api
- baseURL: https://ed.link/api/v2
  baseurl_source: declared
  description: OAuth 2.0 and OpenID Connect single sign-on.
  name: Edlink SSO API
  slug: edlink-sso-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Edlink Agents API
  slug: open-edlink-agents-api
- collection_type: open
  name: Edlink Agents Classes API
  slug: open-edlink-classes-api
- collection_type: open
  name: Edlink Agents Courses API
  slug: open-edlink-courses-api
- collection_type: open
  name: Edlink Agents Districts API
  slug: open-edlink-districts-api
- collection_type: open
  name: Edlink Agents Enrollments API
  slug: open-edlink-enrollments-api
- collection_type: open
  name: Edlink Agents Events API
  slug: open-edlink-events-api
- collection_type: open
  name: Edlink Agents Graph API
  slug: open-edlink-graph-api
- collection_type: open
  name: Edlink Agents Integrations API
  slug: open-edlink-integrations-api
- collection_type: open
  name: Edlink Agents People API
  slug: open-edlink-people-api
- collection_type: open
  name: Edlink Agents Schools API
  slug: open-edlink-schools-api
- collection_type: open
  name: Edlink Agents Sections API
  slug: open-edlink-sections-api
- collection_type: open
  name: Edlink Agents SSO API
  slug: open-edlink-sso-api
- collection_type: open
  name: Edlink API
  slug: open-edlink
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/edlink-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/edlink-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edlink-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/edlink-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://ed.link/community/rss/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edlink
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edlink-inc
- group: company
  title: ''
  type: Website
  url: https://ed.link/
- group: docs
  title: ''
  type: Documentation
  url: https://ed.link/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/edlink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edlink-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/edlink-finops.yml
created: '2026-06-21'
description: Edlink is an education-integration platform offering a unified API for rostering and school data across SIS and LMS systems. The Edlink Graph API exposes normalized districts, schools, classes, sections, courses, people, and enrollments from hundreds of source systems behind a single Bearer-authenticated REST interface, plus SSO, source integrations, and change events.
finops:
- name: Edlink Finops
  service_category: Education Integration
  slug: edlink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edlink.png
layout: provider
modified: '2026-06-21'
name: Edlink
nav: Providers
network: true
overview: 'Edlink publishes 3 APIs on the [APIs.io](https://apis.io/) network: Graph API, Integrations API, and SSO API. Tagged areas include Education, EdTech, Rostering, SIS, and LMS.


  Edlink''s developer surface includes authentication, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Edlink Plans Pricing
  plan_count: 3
  slug: edlink-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Edlink Rate Limits
  slug: edlink-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.2
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edlink/refs/heads/main/screenshots/edlink-2026-07-25T212853.png
security:
- kind: authentication
  name: Edlink Authentication
  slug: edlink-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Edlink Domain Security
  slug: edlink-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: edlink
tags:
- Education
- EdTech
- Rostering
- SIS
- LMS
- Integration
- Unified-API
website: https://ed.link/
---
