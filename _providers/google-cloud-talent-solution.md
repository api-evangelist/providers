---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Google Cloud Talent Solution Agentic Access
  operation_count: 12
  slug: google-cloud-talent-solution-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- baseURL: https://jobs.googleapis.com
  baseurl_source: declared
  description: The Companies API from Google Cloud Talent Solution — 1 operation(s) for companies.
  name: Google Cloud Talent Solution Companies API
  slug: google-cloud-talent-solution-companies-api
- baseURL: https://jobs.googleapis.com
  baseurl_source: declared
  description: The Jobs API from Google Cloud Talent Solution — 3 operation(s) for jobs.
  name: Google Cloud Talent Solution Jobs API
  slug: google-cloud-talent-solution-jobs-api
- baseURL: https://jobs.googleapis.com
  baseurl_source: declared
  description: The Tenants API from Google Cloud Talent Solution — 2 operation(s) for tenants.
  name: Google Cloud Talent Solution Tenants API
  slug: google-cloud-talent-solution-tenants-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Talent Solution Companies API
  slug: open-google-cloud-talent-solution-companies-api
- collection_type: open
  name: Google Cloud Talent Solution Companies Jobs API
  slug: open-google-cloud-talent-solution-jobs-api
- collection_type: open
  name: Google Cloud Talent Solution Companies Tenants API
  slug: open-google-cloud-talent-solution-tenants-api
- collection_type: open
  name: Google Cloud Talent Solution API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-talent-solution-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-talent-solution-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-talent-solution-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-talent-solution-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-talent-solution-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/solutions/talent-solution/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/solutions/talent-solution/pricing
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/cloud-talent-solution-release-notes.xml
created: '2026-03-13'
description: Google Cloud Talent Solution provides a job search and talent acquisition platform that leverages machine learning to match job seekers with relevant opportunities. It offers job posting management, candidate profile search, and intelligent job recommendations for enterprises and job boards.
finops:
- name: Google Cloud Talent Solution Finops
  service_category: API
  slug: google-cloud-talent-solution-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-talent-solution.png
json_schemas:
- name: Job
  property_count: 14
  slug: job
jsonld:
- class_count: 3
  name: context Context
  property_count: 1
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Talent Solution
nav: Providers
network: true
overview: 'Google Cloud Talent Solution publishes 3 APIs on the [APIs.io](https://apis.io/) network: Companies API, Jobs API, and Tenants API. Tagged areas include Google Cloud, Job, Machine-Learning, Recruitment, and Search.


  The Google Cloud Talent Solution catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Talent Solution''s developer surface includes authentication, getting-started guide, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Google Cloud Talent Solution Plans Pricing
  plan_count: 3
  slug: google-cloud-talent-solution-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Google Cloud Talent Solution Rate Limits
  slug: google-cloud-talent-solution-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Talent Solution API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-talent-solution-jsonschema-spectral-rules
scopes:
- name: Google Cloud Talent Solution Scopes
  scope_count: 2
  slug: google-cloud-talent-solution-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 59.9
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-talent-solution/refs/heads/main/screenshots/google-cloud-talent-solution-2026-08-17T083409.png
security:
- kind: authentication
  name: Google Cloud Talent Solution Authentication
  slug: google-cloud-talent-solution-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Talent Solution Domain Security
  slug: google-cloud-talent-solution-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Talent Solution Vulnerability Disclosure
  slug: google-cloud-talent-solution-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-talent-solution
tags:
- Google Cloud
- Job
- Machine-Learning
- Recruitment
- Search
- Talent
---
