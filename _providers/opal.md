---
access_model:
  confidence: medium
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://workwithopal.com/pricing/
  - https://help.workwithopal.com/article/17imdltzi1-opal-api
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The stable REST surface of the Opal marketing planning platform — 66 paths and 97 operations across stories, moments, content, placements, assets, asset references, labels, label sets, stamps, brands,
  name: Opal API v2
  slug: opal-api-v2
- description: The next-generation Opal REST surface, published as work in progress — 97 paths and 154 operations across boards, board objects and collections, board collaborators, blocks and block connectors, categ
  name: Opal API v3
  slug: opal-api-v3
- description: A backend-for-frontend service published in the same public documentation set — 11 paths covering workspace-scoped blocks, smart blocks, smart categories, plans, in-market calendar and experimental pl
  name: Opal Asgard BFF API
  slug: opal-asgard-bff-api
artifact_total: 12
collections:
- collection_type: open
  name: Asgard BFF API
  slug: open-opal-asgard-bff
- collection_type: open
  name: Opal API
  slug: open-opal-v2
- collection_type: open
  name: Opal API (⚠️  WIP)
  slug: open-opal-v3
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/opal-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.workwithopal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://login.ouropal.com/api/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://login.ouropal.com/api/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://login.ouropal.com/api/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://help.workwithopal.com/article/17imdltzi1-opal-api
- group: operate
  title: ''
  type: Support
  url: https://help.workwithopal.com/
- group: company
  title: ''
  type: Blog
  url: https://workwithopal.com/about/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://workwithopal.com/feed/
- group: start
  title: ''
  type: Login
  url: https://login.ouropal.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.workwithopal.com/article/42ysdzfa2y-change-log
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opal-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opal-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/opal-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opal-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/opal-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opal-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opal-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opal-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/opal-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://workwithopal.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://workwithopal.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://workwithopal.com/privacy-policy/
- group: commercial
  title: ''
  type: License
  url: https://workwithopal.com/api-license/
- group: auth
  title: ''
  type: TrustCenter
  url: security/opal-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://workwithopal.com/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opal-domain-security.yml
created: '2026-07-17'
description: 'Opal is a marketing planning and content calendar platform that gives marketing teams a single visual workspace to plan campaigns, build editorial and content calendars, manage creative workflows and approvals, and connect strategy to execution across channels and markets. It is used by enterprise brands such as Target, Starbucks, GM, and SAP, and pairs a unified planning calendar with a "Gem" AI co-pilot plus prebuilt integrations to Slack, Jira, Asana, Wrike, Workfront, Sprinklr, Khoros, Frame.io, Sprout Social, Formstack and Zapier. Opal does ship a real REST API: three OpenAPI 3.0 definitions — v2, v3 and an internal-facing Asgard BFF service — are served publicly from login.ouropal.com and cover stories, moments, content, boards, board objects, assets, asset references, labels, stamps, workflows, custom fields, presentations, rich-text documents and Gem chats. The v2 and v3 surfaces are JSON:API-compliant and authenticate with OAuth 2.0 authorization code (plus a client-credentials
  onboarding flow and a deprecated Session-Token header). The documentation is public, but API credentials are gated: Opal states access requires an active account or an NDA plus approval from Opal leadership, and OAuth client registration is a manual process handled by its integrations team.'
image: https://workwithopal.com/wp-content/uploads/2022/09/opal_logo.png
layout: provider
modified: '2026-08-13'
name: Opal
nav: Providers
network: true
overview: 'Opal publishes 3 APIs on the [APIs.io](https://apis.io/) network: API v2, API v3, and Asgard BFF API. Tagged areas include Company, Consumer, Marketing, Content Planning, and Marketing Calendar.


  Opal''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 23 more developer resources.'
plans:
- name: Opal Plans Pricing
  plan_count: 0
  slug: opal-plans-pricing
random_paper: 130
rate_limits:
- limit_count: 0
  name: Opal Rate Limits
  slug: opal-rate-limits
scopes:
- name: Opal Scopes
  scope_count: 2
  slug: opal-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 50.9
  delta: -0.8
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 55.8
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 51.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opal/refs/heads/main/screenshots/opal-2026-08-07T190443.png
security:
- kind: authentication
  name: Opal Authentication
  slug: opal-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Opal Domain Security
  slug: opal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Opal Trust Center
  slug: opal-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: opal
tags:
- Company
- Consumer
- Marketing
- Content Planning
- Marketing Calendar
- Campaign Management
- Collaboration
- SaaS
- Content Marketing
- Editorial Calendar
- Workflow
- Approvals
- Digital Asset Management
- JSON:API
- OAuth 2.0
- OpenAPI
website: https://www.workwithopal.com
---
