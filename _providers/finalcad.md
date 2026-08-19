---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: Project-level operations for Finalcad One construction projects — project details and settings, project libraries, members and roles, locations (folders, plans, IFC/RVT upload), discussion groups, com
  name: Finalcad One Project API
  slug: finalcad-one-project-api
- description: Organization-level administration of a Finalcad One Enterprise tenant — workspaces, members and roles, the observation status, trade, common-observation, priority and form-template libraries, form and
  name: Finalcad One Organization Management API
  slug: finalcad-one-organization-api
- description: Media upload and retrieval for the Finalcad One platform — single-shot upload for files up to 5 MB, a four-step chunked upload (init, append, terminate, abort) above that, media resource lookup and do
  name: Finalcad One Medias API
  slug: finalcad-one-medias-api
- description: 'Webhook subscription management for the Finalcad One platform — list subscribable event codes, then create, read, update and delete hooks that POST to a client URL when meetings, observations, forms, '
  name: Finalcad One Webhooks API
  slug: finalcad-one-webhooks-api
- description: Read-only Finalcad reference libraries — module colors, module icons, module suggestions, application languages and time zones — that must be resolved before creating content in an organization or pro
  name: Finalcad One Libraries API
  slug: finalcad-one-libraries-api
- description: Authentication surface of the Finalcad One API — the legacy user-token exchange and the connected-user lookup. Current integrations authenticate with an organization API key in X-API-Key plus an Autho
  name: Finalcad One Authentication API
  slug: finalcad-one-authentication-api
artifact_total: 11
asyncapis:
- description: ''
  name: Finalcad Webhooks
  slug: finalcad-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.finalcad.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.finalcad.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.finalcad.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.finalcad.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.finalcad.com/en/articles/43-introductory-guide-to-apis
- group: build
  title: ''
  type: Postman
  url: https://developer.finalcad.com/
- group: build
  title: ''
  type: PostmanCollection
  url: collections/finalcad.postman_collection.json
- group: operate
  title: ''
  type: Support
  url: https://help.finalcad.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.finalcad.com/en/collections/20-public-api
- group: start
  title: ''
  type: Login
  url: https://finalcadone-web.eu.finalcad.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FinalCAD
- group: operate
  title: ''
  type: StatusPage
  url: https://status.finalcad.cloud/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orisha.com/en/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orisha.com/fr/legal/mentions-legales/
- group: company
  title: ''
  type: Blog
  url: https://www.orisha.com/fr/construction/blog/
- group: auth
  title: ''
  type: Authentication
  url: authentication/finalcad-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finalcad-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finalcad-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finalcad-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/finalcad-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finalcad-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/finalcad-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/finalcad-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/finalcad-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/finalcad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/finalcad-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/finalcad-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finalcad-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finalcad-domain-security.yml
created: '2026-08-17'
description: Finalcad is a French construction-technology company, founded in Paris in 2011, whose Finalcad One platform digitizes work on building sites — punch lists and defects ("observations"), quality and safety inspection forms, site meetings, plans and BIM models, documents, phases and subcontractor companies — across iOS and Android field apps, a web app (EU and APAC instances), an AutoCAD plugin and the Finalcad One API. The API is a REST surface of 201 published operations spanning organization and workspace administration, project setup and libraries, observations, forms and form answers, locations (folders, plans, IFC/RVT upload), documents, media upload, webhooks, XLSX/PDF exports and a daily Parquet dataset feed for Power BI. Access is restricted to organizations on the Enterprise licence, authenticated with an organization API key plus a per-caller authorization token. Finalcad merged with Wizzcad to form Advae, and Orisha acquired Advae in March 2025; Finalcad is now a solution
  of Orisha Construction, though the developer portal, the API host and the help centre remain live on the Finalcad domains.
image: https://res.cloudinary.com/postman/image/upload/t_team_logo_pubdoc/v1/team/7ab6f429a9b1c16b8650531c70d19d77d2e28100973615e0de9f1663a5faf6b7
layout: provider
modified: '2026-08-17'
name: Finalcad
nav: Providers
network: true
overview: 'Finalcad publishes 6 APIs on the [APIs.io](https://apis.io/) network, including One Project API, One Organization Management API, One Medias API, and 3 more. Tagged areas include Company, Construction, Construction Technology, Field Management, and Project Management.


  The Finalcad catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finalcad''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 23 more developer resources.'
plans:
- name: Finalcad Plans Pricing
  plan_count: 0
  slug: finalcad-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 0
  name: Finalcad Rate Limits
  slug: finalcad-rate-limits
score:
  band: developing
  composite: 53.2
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 71.7
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Finalcad Authentication
  slug: finalcad-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Finalcad Domain Security
  slug: finalcad-domain-security
  summary_line: TLSv1.3 · DMARC
slug: finalcad
tags:
- Company
- Construction
- Construction Technology
- Field Management
- Project Management
- Quality Control
- Safety
- BIM
- Documents
- Collaboration
- SaaS
website: https://www.finalcad.com/
---
