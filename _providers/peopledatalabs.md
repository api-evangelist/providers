---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Peopledatalabs Agentic Access
  operation_count: 21
  slug: peopledatalabs-agentic-access
  summary_line: 21 operations · 8 acting
api_count: 10
apis:
- description: The Autocomplete API from People Data Labs — 1 operation(s) for autocomplete.
  name: People Data Labs Autocomplete API
  slug: peopledatalabs-autocomplete-api
- description: The Cleaner Endpoints API from People Data Labs — 3 operation(s) for cleaner endpoints.
  name: People Data Labs Cleaner Endpoints API
  slug: peopledatalabs-cleaner-endpoints-api
- description: The Company Endpoints API from People Data Labs — 2 operation(s) for company endpoints.
  name: People Data Labs Company Endpoints API
  slug: peopledatalabs-company-endpoints-api
- description: The IP Enrichment API from People Data Labs — 1 operation(s) for ip enrichment.
  name: People Data Labs IP Enrichment API
  slug: peopledatalabs-ip-enrichment-api
- description: The Job Title Enrichment API from People Data Labs — 1 operation(s) for job title enrichment.
  name: People Data Labs Job Title Enrichment API
  slug: peopledatalabs-job-title-enrichment-api
- description: The Person Endpoints API from People Data Labs — 5 operation(s) for person endpoints.
  name: People Data Labs Person Endpoints API
  slug: peopledatalabs-person-endpoints-api
- description: The Skill Enrichment API from People Data Labs — 1 operation(s) for skill enrichment.
  name: People Data Labs Skill Enrichment API
  slug: peopledatalabs-skill-enrichment-api
- description: 'The Subscription API from People Data Labs — 5 operations for managing webhook subscriptions: create, list, retrieve, update and delete the HTTPS target URL that People Data Labs pushes batched person'
  name: People Data Labs Subscription API
  slug: peopledatalabs-subscription-api
- description: 'The Preview Enrichment API from People Data Labs — 1 operation returning a preview of a person match: a small set of identity fields plus booleans indicating which further fields exist on the record, '
  name: People Data Labs Preview Enrichment API
  slug: peopledatalabs-preview-enrichment-api
- description: The Subject Request API from People Data Labs — 1 operation returning a CSV of PDL Person IDs belonging to data subjects who have opted out of People Data Labs data, so downstream systems can delete t
  name: People Data Labs Subject Request API
  slug: peopledatalabs-subject-request-api
artifact_total: 35
asyncapis:
- description: ''
  name: Peopledatalabs Webhooks
  slug: peopledatalabs-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: People Data Labs API
  slug: open-people-data-labs
- collection_type: open
  name: api.peopledatalabs.com Autocomplete API
  slug: open-peopledatalabs-autocomplete-api
- collection_type: open
  name: api.peopledatalabs.com Autocomplete Cleaner Endpoints API
  slug: open-peopledatalabs-cleaner-endpoints-api
- collection_type: open
  name: People Data Labs Autocomplete Company API
  slug: open-peopledatalabs-company-api
- collection_type: open
  name: api.peopledatalabs.com Autocomplete Company Endpoints API
  slug: open-peopledatalabs-company-endpoints-api
- collection_type: open
  name: People Data Labs Autocomplete IP API
  slug: open-peopledatalabs-ip-api
- collection_type: open
  name: api.peopledatalabs.com Autocomplete IP Enrichment API
  slug: open-peopledatalabs-ip-enrichment-api
- collection_type: open
  name: api.peopledatalabs.com Autocomplete Job Title Enrichment API
  slug: open-peopledatalabs-job-title-enrichment-api
- collection_type: open
  name: People Data Labs Autocomplete Jobs API
  slug: open-peopledatalabs-jobs-api
- collection_type: open
  name: People Data Labs Autocomplete Person API
  slug: open-peopledatalabs-person-api
- collection_type: open
  name: api.peopledatalabs.com Autocomplete Person Endpoints API
  slug: open-peopledatalabs-person-endpoints-api
- collection_type: open
  name: api.peopledatalabs.com Autocomplete Skill Enrichment API
  slug: open-peopledatalabs-skill-enrichment-api
- collection_type: open
  name: api.peopledatalabs.com Subject Request API
  slug: open-peopledatalabs-subject-request-api
- collection_type: open
  name: api.peopledatalabs.com Subscription API
  slug: open-peopledatalabs-subscription-api
- collection_type: open
  name: People Data Labs API
  slug: open-peopledatalabs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/peopledatalabs-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/peopledatalabs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peopledatalabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/people-data-labs
- group: company
  title: ''
  type: Website
  url: https://www.peopledatalabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.peopledatalabs.com
- group: commercial
  title: ''
  type: Plans
  url: plans/peopledatalabs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/peopledatalabs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/peopledatalabs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.peopledatalabs.com/blog
- group: auth
  title: ''
  type: TrustCenter
  url: security/peopledatalabs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peopledatalabs-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://dashboard.peopledatalabs.com/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.peopledatalabs.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.peopledatalabs.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.peopledatalabs.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.peopledatalabs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peopledatalabs.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.peopledatalabs.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.peopledatalabs.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.peopledatalabs.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/peopledatalabs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/peopledatalabs-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/peopledatalabs-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/peopledatalabs-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/peopledatalabs-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/peopledatalabs-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/peopledatalabs-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/peopledatalabs-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.peopledatalabs.com/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/peopledatalabs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/peopledatalabs-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/peopledatalabs-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/peopledatalabs-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/peopledatalabs-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/peopledatalabs-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/peopledatalabs-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/peopledatalabs-webhooks.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/pdl-official/workspace/people-data-labs-workspace/collection/32867294-ef278c05-d32d-47a1-b147-b819bc96238a
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.peopledatalabs.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.peopledatalabs.com/docs/endpoints
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.peopledatalabs.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.peopledatalabs.com/links/release-notes
created: '2026-07-11'
description: People Data Labs (PDL) is a B2B data enrichment and web intelligence provider offering a REST API over a dataset of nearly three billion person profiles and tens of millions of company records. The api.peopledatalabs.com/v5 API lets developers enrich, identify, and search person and company data, resolve contacts and firmographics, look up companies from a domain or LinkedIn URL, and clean and standardize job titles, skills, schools, companies, and locations. Authentication is a single X-Api-Key header, all endpoints are HTTPS REST, and PDL publishes an official OpenAPI specification.
finops:
- name: Peopledatalabs Finops
  service_category: Data and Analytics
  slug: peopledatalabs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peopledatalabs.png
layout: provider
mcp_servers:
- description: ''
  name: People Data Labs Documentation
  slug: people-data-labs-documentation
modified: '2026-08-14'
name: People Data Labs
nav: Providers
network: true
overview: 'People Data Labs publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Cleaner Endpoints API, Company Endpoints API, and 7 more. Tagged areas include Data Enrichment, Web Intelligence, Person Data, Company Data, and B2B Data.


  The People Data Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  People Data Labs'' developer surface includes authentication, documentation, engineering blog, developer portal, signup flow, pricing, support, and 37 more developer resources.'
plans:
- name: Peopledatalabs Plans Pricing
  plan_count: 4
  slug: peopledatalabs-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 7
  name: Peopledatalabs Rate Limits
  slug: peopledatalabs-rate-limits
score:
  band: exemplar
  composite: 68.3
  delta: 0.0
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 30.3
    contract_quality: 58.7
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 73.7
  previous_composite: 68.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peopledatalabs/refs/heads/main/screenshots/peopledatalabs-2026-06-20T191552.png
security:
- kind: authentication
  name: Peopledatalabs Authentication
  slug: peopledatalabs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Peopledatalabs Domain Security
  slug: peopledatalabs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Peopledatalabs Trust Center
  slug: peopledatalabs-trust-center
  summary_line: SOC 2, ISO 27001, FIPS 140
slug: peopledatalabs
tags:
- Data Enrichment
- Web Intelligence
- Person Data
- Company Data
- B2B Data
- Contact Discovery
- Reference Data
- Firmographics
- Identity Resolution
website: https://www.peopledatalabs.com
---
