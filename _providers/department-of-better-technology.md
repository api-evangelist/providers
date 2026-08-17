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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-17'
api_count: 8
apis:
- description: Upload files referenced by response fields.
  name: Department of Better Technology Files API
  slug: department-of-better-technology-files-api
- description: Manage the form fields collected for a project.
  name: Department of Better Technology Forms API
  slug: department-of-better-technology-forms-api
- description: Manage labels used to tag responses within a project.
  name: Department of Better Technology Labels API
  slug: department-of-better-technology-labels-api
- description: Manage projects (forms and their workflow) within a site.
  name: Department of Better Technology Projects API
  slug: department-of-better-technology-projects-api
- description: Assign users or teams to an individual response.
  name: Department of Better Technology Response Assignments API
  slug: department-of-better-technology-response-assignments-api
- description: Attach or detach labels on an individual response.
  name: Department of Better Technology Response Labels API
  slug: department-of-better-technology-response-labels-api
- description: Create, read, update, trash, and recover form submissions.
  name: Department of Better Technology Responses API
  slug: department-of-better-technology-responses-api
- description: Manage the status workflow stages for a project's responses.
  name: Department of Better Technology Statuses API
  slug: department-of-better-technology-statuses-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Screendoor Files API
  slug: open-department-of-better-technology-files-api
- collection_type: open
  name: Screendoor Files Forms API
  slug: open-department-of-better-technology-forms-api
- collection_type: open
  name: Screendoor Files Labels API
  slug: open-department-of-better-technology-labels-api
- collection_type: open
  name: Screendoor Files Projects API
  slug: open-department-of-better-technology-projects-api
- collection_type: open
  name: Screendoor Files Response Assignments API
  slug: open-department-of-better-technology-response-assignments-api
- collection_type: open
  name: Screendoor Files Response Labels API
  slug: open-department-of-better-technology-response-labels-api
- collection_type: open
  name: Screendoor Files Responses API
  slug: open-department-of-better-technology-responses-api
- collection_type: open
  name: Screendoor Files Statuses API
  slug: open-department-of-better-technology-statuses-api
common:
- group: company
  title: ''
  type: Website
  url: https://dobt.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.dobt.co/
- group: docs
  title: ''
  type: Documentation
  url: https://help.dobt.co/
- group: docs
  title: ''
  type: APIReference
  url: https://dobtco.github.io/screendoor-api-docs/
- group: operate
  title: ''
  type: Support
  url: https://help.dobt.co/
- group: company
  title: ''
  type: Blog
  url: https://www.dobt.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dobtco
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dobt.co/
- group: start
  title: ''
  type: SignUp
  url: https://screendoor.dobt.co/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dashboard.dobt.co/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/department-of-better-technology-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/department-of-better-technology-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/department-of-better-technology-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/department-of-better-technology-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/department-of-better-technology-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/department-of-better-technology-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/department-of-better-technology-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/department-of-better-technology-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/department-of-better-technology-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/department-of-better-technology-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/department-of-better-technology-screendoor-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-better-technology-domain-security.yml
created: '2026-07-17'
description: The Department of Better Technology (DOBT), founded in 2013 by former Presidential Innovation Fellows and later acquired by CityBase, builds Screendoor — a form-building and submission- management platform used by government agencies and organizations such as ProPublica, the Los Angeles Times, the Consumer Financial Protection Bureau, and the Ford Foundation to run paperless intake, evaluation, and approval workflows. The Screendoor REST API programmatically manages sites, projects, forms and form fields, workflow statuses, labels, responses (submissions), response labels, and reviewer assignments, using API-key authentication, offset pagination with RFC 5988 Link headers, and an explicit API version.
image: https://raw.githubusercontent.com/dobtco/screendoor-api-docs/master/source/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: department-of-better-technology-mcp.yml
  slug: department-of-better-technology-mcpyml
modified: '2026-07-18'
name: Department of Better Technology
nav: Providers
network: true
overview: 'Department of Better Technology publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Files API, Forms API, Labels API, and 5 more. Tagged areas include Company, Forms, Government, GovTech, and Civic Technology.


  Department of Better Technology''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 25
score:
  band: thin
  composite: 32.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 14.5
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 32.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-better-technology/refs/heads/main/screenshots/department-of-better-technology-2026-07-25T211725.png
security:
- kind: authentication
  name: Department Of Better Technology Authentication
  slug: department-of-better-technology-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Department Of Better Technology Domain Security
  slug: department-of-better-technology-domain-security
  summary_line: TLSv1.3
slug: department-of-better-technology
tags:
- Company
- Forms
- Government
- GovTech
- Civic Technology
- Workflow
- Data Collection
- Screendoor
- Public Sector
- Forms API
website: https://dobt.co
---
