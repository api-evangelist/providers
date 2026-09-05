---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Superblocks Agentic Access
  operation_count: 6
  slug: superblocks-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.superblocks.com/v1
  baseurl_source: declared
  description: The Applications API from Superblocks — 2 operation(s) for applications.
  name: Superblocks Applications API
  slug: superblocks-applications-api
- baseURL: https://api.superblocks.com/v1
  baseurl_source: declared
  description: The Workflows API from Superblocks — 1 operation(s) for workflows.
  name: Superblocks Workflows API
  slug: superblocks-workflows-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Superblocks Applications API
  slug: open-superblocks-applications-api
- collection_type: open
  name: Superblocks Applications Workflows API
  slug: open-superblocks-workflows-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/superblocks-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/superblocks-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superblocks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superblocks-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.superblocks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superblocks.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superblocksteam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/superblockshq
- group: other
  title: ''
  type: X
  url: https://x.com/superblocks
- group: company
  title: ''
  type: Blog
  url: https://www.superblocks.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.superblocks.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.superblocks.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/superblocks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/superblocks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/superblocks-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/superblocks-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/superblocks-context.jsonld
created: 2026-06-12
description: Superblocks is a programmable internal tools platform that enables engineering and IT teams to build, govern, and deploy enterprise-grade internal applications, workflows, and scheduled jobs on top of databases, REST APIs, GraphQL APIs, and 50+ SaaS integrations. The platform exposes a REST management API at api.superblocks.com/v1 that supports full CRUD operations for applications and workflows, authenticated via API key or Bearer JWT. Superblocks supports three deployment models—fully managed cloud, hybrid (control plane managed, data in user infrastructure), and Cloud-Prem (full platform in a private VPC on AWS, GCP, or Azure)—and is SOC 2 Type II certified and HIPAA compliant. Teams can integrate Superblocks into their CI/CD pipelines using official GitHub Actions for export, import, and deployment of Superblocks resources, plus Terraform modules for AWS and Google Cloud.
examples:
- key_count: 3
  name: Superblocks Create Application Request
  slug: superblocks-create-application-request
- key_count: 2
  name: Superblocks List Applications Response
  slug: superblocks-list-applications-response
- key_count: 1
  name: Superblocks List Workflows Response
  slug: superblocks-list-workflows-response
finops:
- name: Superblocks Finops
  service_category: ''
  slug: superblocks-finops
graphqls:
- description: Superblocks provides a GraphQL integration plugin that enables users to call any external or internal GraphQL API from within Superblocks Applications, Workflows, and Scheduled Jobs. The integration a
  name: Superblocks GraphQL API
  slug: superblocks-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superblocks.png
json_schemas:
- name: Application
  property_count: 7
  slug: superblocks-application
- name: Error
  property_count: 3
  slug: superblocks-error
- name: Pagination
  property_count: 3
  slug: superblocks-pagination
- name: Workflow
  property_count: 5
  slug: superblocks-workflow
jsonld:
- class_count: 6
  name: Superblocks Context
  property_count: 14
  slug: superblocks-context
layout: provider
modified: 2026-06-12
name: Superblocks
nav: Providers
network: true
overview: 'Superblocks publishes 2 APIs on the [APIs.io](https://apis.io/) network: Applications API and Workflows API. Tagged areas include Internal Tools, Low-Code, No-Code, Application, and Workflows.


  The Superblocks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Superblocks'' developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Superblocks Plans Pricing
  plan_count: 3
  slug: superblocks-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 6
  name: Superblocks Rate Limits
  slug: superblocks-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Superblocks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: superblocks-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 83.3
    catalog_earned_first_party: 0.0
    catalog_gap: 31.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 64.7
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 34.2
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superblocks/refs/heads/main/screenshots/superblocks-2026-06-20T194714.png
security:
- kind: authentication
  name: Superblocks Authentication
  slug: superblocks-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Superblocks Domain Security
  slug: superblocks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Superblocks Trust Center
  slug: superblocks-trust-center
  summary_line: SOC 2, HIPAA
slug: superblocks
tags:
- Internal Tools
- Low-Code
- No-Code
- Application
- Workflows
- Scheduled Jobs
- Integration
- Enterprise
- Artificial Intelligence
- Databases
- REST API
- Developer Tools
website: https://www.superblocks.com/
---
