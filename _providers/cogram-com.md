---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Cogram Com Agentic Access
  operation_count: 30
  slug: cogram-com-agentic-access
  summary_line: 30 operations · 15 acting
api_count: 1
apis:
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: Read-only action items from meetings.
  name: Cogram Action Items API
  slug: cogram-com-action-items-api
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: Read-only log of the emails and meetings Cogram deleted or redacted, and why.
  name: Cogram Audit Log API
  slug: cogram-com-audit-log-api
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: Report backup runs so Cogram can alert when they stop.
  name: Cogram Backup Runs API
  slug: cogram-com-backup-runs-api
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: Read-only kanban board items, with change history.
  name: Cogram Board Items API
  slug: cogram-com-board-items-api
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: 'Zip exports of org data: request, poll, download.'
  name: Cogram Data Exports API
  slug: cogram-com-data-exports-api
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: 'Directory reconciliation: propose and apply the company link that contacts created outside a transmittal send are missing.'
  name: Cogram Directory API
  slug: cogram-com-directory-api
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: 'Reusable project setups: a project type plus groups with roles, applied when a project is created with a template_id.'
  name: Cogram Project Templates API
  slug: cogram-com-project-templates-api
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: Project-type taxonomy used to classify projects (e.g. "Design-Build").
  name: Cogram Project Types API
  slug: cogram-com-project-types-api
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: Projects and their membership/roles.
  name: Cogram Projects API
  slug: cogram-com-projects-api
- baseURL: https://api.cogram.com/v1
  baseurl_source: declared
  description: Organization members and their organization roles.
  name: Cogram Users API
  slug: cogram-com-users-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/cogram-com/agentic-access/cogram-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cogram-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cogram-com/plans/cogram-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cogram-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cogram-com/rules/cogram-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cogram-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cogram-com/json-ld/cogram-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cogram-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cogram-com/vocabulary/cogram-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cogram-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cogram-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cogram-com/data-model/cogram-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cogram-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cogram-com/changelog/cogram-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cogram-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cogram.com/security
- group: design
  href: https://artifacts.apis.io/cogram-com/errors/cogram-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cogram-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cogram-com/conformance/cogram-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cogram-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cogram-com/llms/cogram-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cogram-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cogram-com/well-known/cogram-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cogram-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cogram-com/hosts/cogram-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cogram-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cogram-com/vendors/cogram-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cogram-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cogram.com/terms
- group: auth
  title: ''
  type: Security
  url: https://cogram.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cogram.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cogram.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cogram.com/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://cogram.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://cogram.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cogram.com/
- group: auth
  href: https://artifacts.apis.io/cogram-com/authentication/cogram-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cogram-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cogram-com/security/cogram-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cogram-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cogram-com/security/cogram-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cogram-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cogram.com/
created: '2026-11-04'
description: Cogram provides AI-powered tools for architects and engineers, enabling automated documentation, collaboration, and design workflows. Founded in 2021, the platform leverages large language models to generate construction drawings, specifications, and reports, streamlining the engineering process and reducing manual effort. Cogram’s mission is to accelerate the creation of built environment assets through intelligent software that understands technical language and design intent.
image: https://cogram.com/og-image-v3.png
json_schemas:
- name: BoardItemDetailV1
  property_count: 18
  slug: cogram-com-board-item-detail-v1
- name: DataExportCreateRequest
  property_count: 4
  slug: cogram-com-data-export-create-request
- name: DataExportResponse
  property_count: 22
  slug: cogram-com-data-export-response
- name: ProjectCreateV1
  property_count: 11
  slug: cogram-com-project-create-v1
- name: ProjectUpdateV1
  property_count: 9
  slug: cogram-com-project-update-v1
- name: ProjectV1
  property_count: 18
  slug: cogram-com-project-v1
jsonld:
- class_count: 62
  name: Cogram Com Context
  property_count: 137
  slug: cogram-com-context
layout: provider
modified: '2026-11-04'
name: Cogram
nav: Providers
network: true
overview: 'Cogram publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Action Items API, Audit Log API, Backup Runs API, and 7 more. Tagged areas include Artificial Intelligence, Architecture, Engineering, Documentation, and Collaboration.


  The Cogram catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cogram''s developer surface includes changelog, pricing, getting-started guide, engineering blog, documentation, authentication, and 21 more developer resources.'
plans:
- name: Cogram Com Plans Pricing
  plan_count: 1
  slug: cogram-com-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Cogram API Rules
  rule_count: 62
  severity_counts:
    error: 52
    hint: 0
    info: 3
    warn: 7
  slug: cogram-com-rules
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 35.6
    contract_quality: 63.8
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cogram Com Authentication
  slug: cogram-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cogram Com Domain Security
  slug: cogram-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cogram Com Trust Center
  slug: cogram-com-trust-center
  summary_line: SOC 2, GDPR
skill_count: 4
skills:
- name: cogram-com-create-project-template
  slug: cogram-com-create-project-template
- name: cogram-com-create-project-with-member
  slug: cogram-com-create-project-with-member
- name: cogram-com-data-exports-manage
  slug: cogram-com-data-exports-manage
- name: cogram-com-directory-manage-contact-company-links
  slug: cogram-com-directory-manage-contact-company-links
slug: cogram-com
tags:
- Artificial Intelligence
- Architecture
- Engineering
- Documentation
- Collaboration
website: https://cogram.com/
---
