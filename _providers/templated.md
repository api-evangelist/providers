---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Templated Agentic Access
  operation_count: 6
  slug: templated-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.templated.io/v1
  baseurl_source: declared
  description: The Renders API from Templated — 3 operation(s) for renders.
  name: Templated Renders API
  slug: templated-renders-api
- baseURL: https://api.templated.io/v1
  baseurl_source: declared
  description: The Templates API from Templated — 2 operation(s) for templates.
  name: Templated Templates API
  slug: templated-templates-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Templated Renders API
  slug: open-templated-renders-api
- collection_type: open
  name: Templated Renders Templates API
  slug: open-templated-templates-api
- collection_type: open
  name: Templated API
  slug: open-templated
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/templated-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/templated-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/templated-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/templated-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/templated-io
- group: company
  title: ''
  type: Website
  url: https://templated.io/
- group: docs
  title: ''
  type: Documentation
  url: https://templated.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/templated-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/templated-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/templated-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://templated.io/rss.xml
created: '2026-06-25'
description: Templated is an API for automated image, video, and PDF generation from reusable templates. Designers build templates in a drag-and-drop editor, then the REST API renders them at scale by overriding layer content, with synchronous and asynchronous rendering, batch and multi-page output, and webhook callbacks.
finops:
- name: Templated Finops
  service_category: Media and Content Generation
  slug: templated-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/templated.png
layout: provider
modified: '2026-06-25'
name: Templated
nav: Providers
network: true
overview: 'Templated publishes 2 APIs on the [APIs.io](https://apis.io/) network: Renders API and Templates API. Tagged areas include Image-Generation, PDF Generation, Templates, Rendering, and Automation.


  Templated''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Templated Plans Pricing
  plan_count: 4
  slug: templated-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Templated Rate Limits
  slug: templated-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Templated Authentication
  slug: templated-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Templated Domain Security
  slug: templated-domain-security
  summary_line: TLSv1.3 · DMARC
slug: templated
tags:
- Image-Generation
- PDF Generation
- Templates
- Rendering
- Automation
website: https://templated.io/
---
