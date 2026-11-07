---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api-qa.phenompro.com
  baseurl_source: declared
  description: Fetch applicant data, hiring status and leads for a job.
  name: Phenom Applicants API
  slug: phenom-applicants-api
- baseURL: https://api-qa.phenompro.com
  baseurl_source: declared
  description: Combined candidate + job data for jobs a candidate has applied to.
  name: Phenom Applications API
  slug: phenom-applications-api
- baseURL: https://api-qa.phenompro.com
  baseurl_source: declared
  description: Add, update, delete and retrieve candidate records.
  name: Phenom Candidates API
  slug: phenom-candidates-api
- baseURL: https://api-qa.phenompro.com
  baseurl_source: declared
  description: Job Sync — view, create, update and delete jobs in the Phenom database.
  name: Phenom Jobs API
  slug: phenom-jobs-api
- baseURL: https://api-qa.phenompro.com
  baseurl_source: declared
  description: Search candidates and retrieve onboarding information and attachments.
  name: Phenom Onboarding API
  slug: phenom-onboarding-api
- baseURL: https://api-qa.phenompro.com
  baseurl_source: declared
  description: Resume and job-description parsing/extraction.
  name: Phenom Parsers API
  slug: phenom-parsers-api
- baseURL: https://api-qa.phenompro.com
  baseurl_source: declared
  description: Predict skills from job titles and provided skill sets.
  name: Phenom Prediction API
  slug: phenom-prediction-api
- baseURL: https://api-qa.phenompro.com
  baseurl_source: declared
  description: Create, update and delete candidate tags.
  name: Phenom Tags API
  slug: phenom-tags-api
- baseURL: https://api-qa.phenompro.com
  baseurl_source: declared
  description: SCIM 2.0 user and group management.
  name: Phenom User Management API
  slug: phenom-user-management-api
artifact_total: 27
collections:
- collection_type: open
  name: Phenom Talent Experience Platform Applicants API
  slug: open-phenom-applicants-api
- collection_type: open
  name: Phenom Talent Experience Platform Applicants Applications API
  slug: open-phenom-applications-api
- collection_type: open
  name: Phenom Talent Experience Platform Applicants Candidates API
  slug: open-phenom-candidates-api
- collection_type: open
  name: Phenom Talent Experience Platform Applicants Jobs API
  slug: open-phenom-jobs-api
- collection_type: open
  name: Phenom Talent Experience Platform Applicants Onboarding API
  slug: open-phenom-onboarding-api
- collection_type: open
  name: Phenom Talent Experience Platform Applicants Parsers API
  slug: open-phenom-parsers-api
- collection_type: open
  name: Phenom Talent Experience Platform Applicants Prediction API
  slug: open-phenom-prediction-api
- collection_type: open
  name: Phenom Talent Experience Platform Applicants Tags API
  slug: open-phenom-tags-api
- collection_type: open
  name: Phenom Talent Experience Platform Applicants User Management API
  slug: open-phenom-user-management-api
common:
- group: commercial
  href: https://artifacts.apis.io/phenom/plans/phenom-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/phenom-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/phenom/capabilities/phenom-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/phenom-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/phenom/overlays/phenom-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/phenom-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.phenom.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.phenom.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.phenom.com/apiDetail
- group: docs
  title: ''
  type: APIReference
  url: https://developer.phenom.com/apiDetail
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.phenom.com/getStarted
- group: company
  title: ''
  type: Blog
  url: https://www.phenom.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phenompeople
- group: operate
  title: ''
  type: Support
  url: https://www.phenom.com/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.phenom.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.phenom.com/terms--conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.phenom.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.phenom.com/
- group: auth
  title: ''
  type: Security
  url: https://www.phenom.com/vdp
- group: docs
  href: https://artifacts.apis.io/phenom/openapi/_original/phenom-platform-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/phenom-platform-openapi.yml
- group: auth
  href: https://artifacts.apis.io/phenom/authentication/phenom-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phenom-authentication.yml
- group: design
  href: https://artifacts.apis.io/phenom/conventions/phenom-conventions.yml
  title: ''
  type: Conventions
  url: conventions/phenom-conventions.yml
- group: design
  href: https://artifacts.apis.io/phenom/errors/phenom-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/phenom-error-codes.yml
- group: design
  href: https://artifacts.apis.io/phenom/lifecycle/phenom-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/phenom-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/phenom/conformance/phenom-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phenom-conformance.yml
- group: agent
  href: https://artifacts.apis.io/phenom/well-known/phenom-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phenom-well-known.yml
- group: auth
  href: https://artifacts.apis.io/phenom/well-known/phenom-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/phenom-security.txt
- group: auth
  href: https://artifacts.apis.io/phenom/security/phenom-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/phenom-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/phenom/security/phenom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phenom-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/phenom/mcp/phenom-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/phenom-mcp.yml
- group: agent
  href: https://artifacts.apis.io/phenom/llms/phenom-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phenom-llms.txt
- group: design
  href: https://artifacts.apis.io/phenom/data-model/phenom-data-model.yml
  title: ''
  type: DataModel
  url: data-model/phenom-data-model.yml
- group: agent
  href: https://artifacts.apis.io/phenom/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Phenom is an HR technology company whose Intelligent Talent Experience platform applies AI to every stage of the talent lifecycle — helping candidates find and apply to the right jobs, recruiters and hiring managers source and engage talent, employees grow, and HR teams operate more efficiently. The Phenom Developer Portal exposes REST APIs for job sync, candidate management, onboarding, applications and applicants, resume and job-description parsing, SCIM 2.0 user and group management, candidate tagging, and AI-driven skills prediction, letting partners and ATS/HRIS systems integrate with the Phenom platform. Phenom is headquartered in Ambler, Pennsylvania and backed by Sierra Ventures among others.
finops:
- has_sources: true
  method: derived
  name: Phenom Finops
  primary_unit: ''
  service_category: ''
  slug: phenom-finops
  template: true
image: https://images.ctfassets.net/0d3i1kfsuaq3/7DvjJdtfMfhzvhrPvEwY2r/792d04789d00e1b6418b33be5c18762b/Phenom-Meta-Image.png
layout: provider
modified: '2026-07-20'
name: Phenom
nav: Providers
network: true
overview: 'Phenom publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applicants API, Applications API, Candidates API, and 6 more. Tagged areas include Company, Human Resources, Talent Experience, Recruiting, and Applicant Tracking.


  The Phenom catalog on APIs.io includes 1 Spectral governance ruleset.


  Phenom''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 23 more developer resources.'
plans:
- name: Phenom Plans Pricing
  plan_count: 0
  slug: phenom-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Phenom API Rules
  rule_count: 63
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 1
  slug: phenom-rules
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 31.8
    contract_quality: 50.2
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 46.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/phenom/phenom-2026-08-17T081205.png
security:
- kind: authentication
  name: Phenom Authentication
  slug: phenom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Phenom Domain Security
  slug: phenom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Phenom Vulnerability Disclosure
  slug: phenom-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Parse a resume and predict skills
  slug: phenom-parse-resume-and-predict-skills
- name: Search jobs and review applications
  slug: phenom-search-jobs-and-applications
- name: Source a candidate and tag them
  slug: phenom-source-candidate-and-tag
slug: phenom
tags:
- Company
- Human Resources
- Talent Experience
- Recruiting
- Applicant Tracking
- Candidate Experience
- Onboarding
- SCIM
- Resume Parsing
- Skills
- Artificial Intelligence
website: https://www.phenom.com/
---
