---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
  score: 23.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Northflank Agentic Access
  operation_count: 13
  slug: northflank-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 4
apis:
- baseURL: https://api.northflank.com/v1
  baseurl_source: declared
  description: The Addons API from Northflank — 2 operation(s) for addons.
  name: Northflank Addons API
  slug: northflank-addons-api
- baseURL: https://api.northflank.com/v1
  baseurl_source: declared
  description: The Jobs API from Northflank — 2 operation(s) for jobs.
  name: Northflank Jobs API
  slug: northflank-jobs-api
- baseURL: https://api.northflank.com/v1
  baseurl_source: declared
  description: The Projects API from Northflank — 1 operation(s) for projects.
  name: Northflank Projects API
  slug: northflank-projects-api
- baseURL: https://api.northflank.com/v1
  baseurl_source: declared
  description: The Services API from Northflank — 2 operation(s) for services.
  name: Northflank Services API
  slug: northflank-services-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Northflank Addons API
  slug: open-northflank-addons-api
- collection_type: open
  name: Northflank Addons Jobs API
  slug: open-northflank-jobs-api
- collection_type: open
  name: Northflank Addons Projects API
  slug: open-northflank-projects-api
- collection_type: open
  name: Northflank Addons Services API
  slug: open-northflank-services-api
- collection_type: open
  name: Northflank API
  slug: open-northflank
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/northflank-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/northflank-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/northflank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/northflank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/northflank-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://northflank.com/blog/rss/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northflank
- group: company
  title: ''
  type: Website
  url: https://northflank.com
- group: docs
  title: ''
  type: Documentation
  url: https://northflank.com/docs
- group: docs
  title: ''
  type: API Documentation
  url: https://northflank.com/docs/v1/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/northflank
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/northflank/skills
created: '2026-03-27'
description: Northflank is an internal developer platform providing self-service deployment, scaling, and management of applications, databases, and jobs across cloud providers.
finops:
- name: Northflank Finops
  service_category: API
  slug: northflank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/northflank.png
layout: provider
modified: '2026-05-19'
name: Northflank
nav: Providers
network: true
overview: 'Northflank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Addons API, Jobs API, Projects API, and 1 more. Tagged areas include Cloud Deployment, Developer Experience, Internal Developer Platform, and Platform Engineering.


  Northflank''s developer surface includes authentication, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Northflank Plans Pricing
  plan_count: 3
  slug: northflank-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Northflank Rate Limits
  slug: northflank-rate-limits
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 38.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/northflank/refs/heads/main/screenshots/northflank-2026-06-20T190419.png
security:
- kind: authentication
  name: Northflank Authentication
  slug: northflank-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Northflank Domain Security
  slug: northflank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Northflank Vulnerability Disclosure
  slug: northflank-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Northflank Trust Center
  slug: northflank-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
skill_count: 1
skills:
- name: northflank
  slug: northflank
slug: northflank
tags:
- Cloud Deployment
- Developer Experience
- Internal Developer Platform
- Platform Engineering
website: https://northflank.com
---
