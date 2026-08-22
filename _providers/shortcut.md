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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Shortcut Agentic Access
  operation_count: 28
  slug: shortcut-agentic-access
  summary_line: 28 operations · 15 acting
api_count: 7
apis:
- description: RESTful API providing full CRUD access to stories, epics, iterations, milestones, workflows, projects, teams, members, files, labels, categories, and webhooks. Requests authenticate with a Shortcut-To
  name: Shortcut REST API v3
  slug: rest-api-v3
- description: The Categories API from Shortcut — 2 operation(s) for categories.
  name: Shortcut Categories API
  slug: shortcut-categories-api
- description: The Custom Fields API from Shortcut — 2 operation(s) for custom fields.
  name: Shortcut Custom Fields API
  slug: shortcut-custom-fields-api
- description: The Documents API from Shortcut — 2 operation(s) for documents.
  name: Shortcut Documents API
  slug: shortcut-documents-api
- description: The Entity Templates API from Shortcut — 2 operation(s) for entity templates.
  name: Shortcut Entity Templates API
  slug: shortcut-entity-templates-api
- description: The Epics API from Shortcut — 4 operation(s) for epics.
  name: Shortcut Epics API
  slug: shortcut-epics-api
- description: The Workflows API from Shortcut — 1 operation(s) for workflows.
  name: Shortcut Workflows API
  slug: shortcut-workflows-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shortcut REST API v3 Categories API
  slug: open-shortcut-categories-api
- collection_type: open
  name: Shortcut REST API v3 Categories Custom Fields API
  slug: open-shortcut-custom-fields-api
- collection_type: open
  name: Shortcut REST API v3 Categories Documents API
  slug: open-shortcut-documents-api
- collection_type: open
  name: Shortcut REST API v3 Categories Entity Templates API
  slug: open-shortcut-entity-templates-api
- collection_type: open
  name: Shortcut REST API v3 Categories Epics API
  slug: open-shortcut-epics-api
- collection_type: open
  name: Shortcut REST API v3 Categories Workflows API
  slug: open-shortcut-workflows-api
- collection_type: open
  name: Shortcut REST API v3
  slug: open-shortcut
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shortcut-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/shortcut-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shortcut-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shortcut-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shortcut-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shortcutsoftware
- group: company
  title: ''
  type: Website
  url: https://www.shortcut.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shortcut.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shortcut.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.shortcut.com/signup
- group: operate
  title: ''
  type: Support
  url: https://help.shortcut.com
- group: company
  title: ''
  type: Blog
  url: https://shortcut.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/useshortcut
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shortcut.com
created: '2026-05-11'
description: Shortcut (formerly Clubhouse) is a cloud-based project management platform built for software development teams, providing stories, epics, objectives, Kanban boards, sprints, reporting, and integrations with GitHub, GitLab, and Slack. The Shortcut REST API v3 exposes full CRUD access to stories, epics, iterations, workflows, members, projects, and webhooks. Authentication uses a per-account API token passed via the Shortcut-Token request header.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shortcut.png
layout: provider
modified: '2026-05-11'
name: Shortcut
nav: Providers
network: true
overview: 'Shortcut publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Custom Fields API, Documents API, and 3 more. Tagged areas include Project Management, Agile, Software Development, Issue Tracking, and Kanban.


  Shortcut''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, GitHub presence, and 7 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 32.7
  delta: -2.8
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shortcut/refs/heads/main/screenshots/shortcut-2026-06-20T193838.png
security:
- kind: authentication
  name: Shortcut Authentication
  slug: shortcut-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shortcut Domain Security
  slug: shortcut-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Shortcut Vulnerability Disclosure
  slug: shortcut-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Shortcut Trust Center
  slug: shortcut-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: shortcut
tags:
- Project Management
- Agile
- Software Development
- Issue Tracking
- Kanban
- Sprint Planning
- Collaboration
- Developer Tools
website: https://www.shortcut.com
---
