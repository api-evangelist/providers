---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Transifex Agentic Access
  operation_count: 113
  slug: transifex-agentic-access
  summary_line: 113 operations · 57 acting
api_count: 18
apis:
- description: The Activity Reports API from Transifex — 9 operation(s) for activity reports.
  name: Transifex Activity Reports API
  slug: transifex-activity-reports-api
- description: The Context Screenshots API from Transifex — 5 operation(s) for context screenshots.
  name: Transifex Context Screenshots API
  slug: transifex-context-screenshots-api
- description: Glossaries
  name: Transifex Glossaries API
  slug: transifex-glossaries-api
- description: Internationalization formats supported by Transifex.
  name: Transifex I18n Formats API
  slug: transifex-i18n-formats-api
- description: Languages objects represent each available language in Transifex.
  name: Transifex Languages API
  slug: transifex-languages-api
- description: Represents Transifex's organizations. Every user can be a member of one or multiple organizations. Only the organizations the authenticated user belongs to will appear here.
  name: Transifex Organizations API
  slug: transifex-organizations-api
- description: Project Webhooks lets you specify actions which will trigger some notification event. When that event occurs, Transfex application will make a HTTP request to the URL configured for the webhook (callb
  name: Transifex Project Webhooks API
  slug: transifex-project-webhooks-api
- description: Represents projects, as used within Transifex. Each project belongs to an organization.
  name: Transifex Projects API
  slug: transifex-projects-api
- description: Represents comments on resource strings. These are the same comments exposed in the Transifex Editor under the "Comments" tab. A comment can also be flagged as an **issue**. In this case, some extra f
  name: Transifex Resource String Comments API
  slug: transifex-resource-string-comments-api
- description: Resource Strings
  name: Transifex Resource Strings API
  slug: transifex-resource-strings-api
- description: The Resource Translations API from Transifex — 7 operation(s) for resource translations.
  name: Transifex Resource Translations API
  slug: transifex-resource-translations-api
- description: Represents a resource that holds source strings. Resources belong to a specific project in Transifex.
  name: Transifex Resources API
  slug: transifex-resources-api
- description: The Statistics API from Transifex — 2 operation(s) for statistics.
  name: Transifex Statistics API
  slug: transifex-statistics-api
- description: Tasks are work items that can be assigned to users within a project. They help organize and track translation work.
  name: Transifex Tasks API
  slug: transifex-tasks-api
- description: The Team Memberships API from Transifex — 2 operation(s) for team memberships.
  name: Transifex Team Memberships API
  slug: transifex-team-memberships-api
- description: The Teams API from Transifex — 4 operation(s) for teams.
  name: Transifex Teams API
  slug: transifex-teams-api
- description: The Translation Memory API from Transifex — 4 operation(s) for translation memory.
  name: Transifex Translation Memory API
  slug: transifex-translation-memory-api
- description: Represents Transifex's users.
  name: Transifex Users API
  slug: transifex-users-api
artifact_total: 35
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/transifex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transifex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transifex-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.transifex.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.transifex.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/transifex
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transifex
- group: company
  title: ''
  type: Blog
  url: https://www.transifex.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.transifex.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.transifex.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/transifex
- group: commercial
  title: ''
  type: Plans
  url: plans/transifex-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/transifex-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/transifex-finops.yml
created: '2026-06-13'
description: Transifex is a cloud-based localization management platform that enables development and content teams to translate software, websites, mobile apps, and digital content at scale. The Transifex REST API v3 provides programmatic access to manage translation projects, resources, language teams, and translation memory. Developers can automate localization workflows, push and pull source strings, trigger translation jobs, and integrate continuous localization into CI/CD pipelines. The platform supports OAuth 2.0 and bearer token authentication, with SDKs available for Python, JavaScript, Swift, Java, and a Go-based CLI tool.
examples:
- key_count: 1
  name: Create Project
  slug: create-project
- key_count: 1
  name: Download Translations
  slug: download-translations
- key_count: 1
  name: Project Response
  slug: project-response
- key_count: 1
  name: Project Webhook
  slug: project-webhook
- key_count: 1
  name: Resource String
  slug: resource-string
- key_count: 1
  name: Resource Translation
  slug: resource-translation
- key_count: 1
  name: Upload Source Strings
  slug: upload-source-strings
finops:
- name: Transifex Finops
  service_category: ''
  slug: transifex-finops
graphqls:
- description: Transifex is a localization platform for software and content. The API covers project management, resource management, translations, translation memory, glossary, team management, and over-the-air del
  name: Transifex GraphQL API
  slug: transifex-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transifex.png
json_schemas:
- name: Transifex API
  property_count: 0
  slug: transifex
jsonld:
- class_count: 9
  name: Transifex Context
  property_count: 14
  slug: transifex-context
layout: provider
modified: '2026-06-13'
name: Transifex
nav: Providers
network: true
overview: 'Transifex publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Activity Reports API, Context Screenshots API, Glossaries API, and 15 more. Tagged areas include Localization, Translation, i18n, l10n, and Language.


  The Transifex catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Transifex''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Transifex Plans Pricing
  plan_count: 3
  slug: transifex-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Transifex Rate Limits
  slug: transifex-rate-limits
rules:
- name: Transifex API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: transifex-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.1
  delta: -3.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transifex/refs/heads/main/screenshots/transifex-2026-06-20T195541.png
security:
- kind: authentication
  name: Transifex Authentication
  slug: transifex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Transifex Domain Security
  slug: transifex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transifex
tags:
- Localization
- Translation
- i18n
- l10n
- Language
- Content Management
- Workflow Automation
website: https://www.transifex.com
---
