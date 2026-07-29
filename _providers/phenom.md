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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-07-28'
api_count: 9
apis:
- description: Fetch applicant data, hiring status and leads for a job.
  name: Phenom Applicants API
  slug: phenom-applicants-api
- description: Combined candidate + job data for jobs a candidate has applied to.
  name: Phenom Applications API
  slug: phenom-applications-api
- description: Add, update, delete and retrieve candidate records.
  name: Phenom Candidates API
  slug: phenom-candidates-api
- description: Job Sync — view, create, update and delete jobs in the Phenom database.
  name: Phenom Jobs API
  slug: phenom-jobs-api
- description: Search candidates and retrieve onboarding information and attachments.
  name: Phenom Onboarding API
  slug: phenom-onboarding-api
- description: Resume and job-description parsing/extraction.
  name: Phenom Parsers API
  slug: phenom-parsers-api
- description: Predict skills from job titles and provided skill sets.
  name: Phenom Prediction API
  slug: phenom-prediction-api
- description: Create, update and delete candidate tags.
  name: Phenom Tags API
  slug: phenom-tags-api
- description: SCIM 2.0 user and group management.
  name: Phenom User Management API
  slug: phenom-user-management-api
artifact_total: 13
common:
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
  title: ''
  type: OpenAPI
  url: openapi/phenom-platform-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/phenom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/phenom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/phenom-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/phenom-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/phenom-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/phenom-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/phenom-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/phenom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phenom-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/phenom-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/phenom-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/phenom-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Phenom is an HR technology company whose Intelligent Talent Experience platform applies AI to every stage of the talent lifecycle — helping candidates find and apply to the right jobs, recruiters and hiring managers source and engage talent, employees grow, and HR teams operate more efficiently. The Phenom Developer Portal exposes REST APIs for job sync, candidate management, onboarding, applications and applicants, resume and job-description parsing, SCIM 2.0 user and group management, candidate tagging, and AI-driven skills prediction, letting partners and ATS/HRIS systems integrate with the Phenom platform. Phenom is headquartered in Ambler, Pennsylvania and backed by Sierra Ventures among others.
image: https://images.ctfassets.net/0d3i1kfsuaq3/7DvjJdtfMfhzvhrPvEwY2r/792d04789d00e1b6418b33be5c18762b/Phenom-Meta-Image.png
layout: provider
mcp_servers:
- description: ''
  name: phenom-mcp.yml
  slug: phenom-mcpyml
modified: '2026-07-20'
name: Phenom
nav: Providers
network: true
overview: 'Phenom publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Applicants API, Applications API, Candidates API, and 6 more. Tagged areas include Company, Hr Tech, Talent Experience, Recruiting, and Applicant Tracking.


  Phenom''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 20 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 48.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 15.8
  previous_composite: 48.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
slug: phenom
tags:
- Company
- Hr Tech
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
