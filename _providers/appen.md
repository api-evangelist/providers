---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Appen Agentic Access
  operation_count: 32
  slug: appen-agentic-access
  summary_line: 32 operations · 28 acting
api_count: 1
apis:
- description: Appen AI Data Annotation Platform (ADAP) API
  name: Appen AI Data Annotation Platform API
  slug: appen-ai-data-annotation-platform-api
- baseURL: https://api.appen.com
  baseurl_source: declared
  description: 'Generate and download reports for either a single job or an entire project, and download datasets from projects. - **Choose scope with exactly one of:** - jobId: download a Job-level report - projectI'
  name: Appen Download API
  slug: appen-download-api
- baseURL: https://api.appen.com
  baseurl_source: declared
  description: The Internal Contributors API from Appen — 12 operation(s) for internal contributors.
  name: Appen Internal Contributors API
  slug: appen-internal-contributors-api
- baseURL: https://api.appen.com
  baseurl_source: declared
  description: 'Job management operations for creating, configuring, and controlling data annotation workflows. - **Job Lifecycle Management:** - **Create Jobs**: Initialize new annotation tasks with project associat'
  name: Appen Jobs API
  slug: appen-jobs-api
- baseURL: https://api.appen.com
  baseurl_source: declared
  description: Project management operations for organizing and structuring your data annotation workflows. - **Project Structure:** - Projects serve as containers for organizing related jobs and data - Each project
  name: Appen Projects API
  slug: appen-projects-api
- baseURL: https://api.appen.com
  baseurl_source: declared
  description: 'Unit management operations for handling individual data rows and their distribution across jobs. - **Unit Operations:** - **List Units**: Retrieve and filter units within a project with pagination cap'
  name: Appen Route Units API
  slug: appen-route-units-api
- baseURL: https://api.appen.com
  baseurl_source: declared
  description: 'Test question management operations for evaluating contributor performance and ensuring quality assurance in data annotation workflows. - **Key Operations:** - **Add Test Questions**: Create new test '
  name: Appen Test Questions API
  slug: appen-test-questions-api
- baseURL: https://api.appen.com
  baseurl_source: declared
  description: 'File upload operations for importing datasets and data into your projects and jobs. - **Dataset Upload Process:** - **Upload Files**: Send CSV files containing your data to existing projects - **Statu'
  name: Appen Upload API
  slug: appen-upload-api
artifact_total: 16
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/agentic-access/appen-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/appen-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/rules/appen-rules.yml
  title: ''
  type: Spectral
  url: rules/appen-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/json-ld/appen-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appen-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/vocabulary/appen-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appen-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/data-model/appen-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appen-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/errors/appen-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appen-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/conformance/appen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appen-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/llms/appen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appen-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/well-known/appen-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/appen-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/well-known/appen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appen-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/hosts/appen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appen-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/vendors/appen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appen-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appen.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/authentication/appen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appen-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appen/refs/heads/main/security/appen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appen.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.appen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.appen.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.appen.com/open-api.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.appen.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Appen
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appen.com/legal-policies/privacy-statement
created: '2026-09-22'
description: Appen provides high-quality training data and data annotation services for AI models, leveraging a global crowd of over 500,000 contributors. With 30 years of experience, they offer data products across speech, vision, language, and structured data, supporting enterprises in building reliable AI systems. Their platform includes tools for data collection, labeling, validation, and evaluation, ensuring compliance and security with SOC 2 and ISO 27001 certifications.
image: https://cdn.prod.website-files.com/656a605609413dfd3feb9d34/6aa317a84eab4c7f1644a689_Appen-social-share.png
json_schemas:
- name: JobDTO
  property_count: 67
  slug: appen-job-dto
- name: Response
  property_count: 5
  slug: appen-response
- name: UpdateTestQuestionRequest
  property_count: 0
  slug: appen-update-test-question-request
jsonld:
- class_count: 7
  name: Appen Context
  property_count: 78
  slug: appen-context
layout: provider
modified: '2026-09-22'
name: Appen
nav: Providers
network: true
overview: 'Appen publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Download API, Internal Contributors API, Jobs API, and 5 more. Tagged areas include Artificial Intelligence, Data, Annotation, Training Data, and Enterprise.


  The Appen catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Appen''s developer surface includes authentication, documentation, API reference, engineering blog, and 19 more developer resources.'
random_paper: 4
rules:
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Appen API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 2
  slug: appen-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 63.8
    developer_ergonomics: 42.3
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Appen Authentication
  slug: appen-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Appen Domain Security
  slug: appen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appen
tags:
- Artificial Intelligence
- Data
- Annotation
- Training Data
- Enterprise
website: https://appen.com/
---
