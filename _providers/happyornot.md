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
api_count: 21
apis:
- description: Endpoints and data definitions related to alert comments which have been written for alerts
  name: HappyOrNot alert-comments API
  slug: happyornot-alert-comments-api
- description: Endpoints and data definitions related to alert specifications based on which alerts are triggered
  name: HappyOrNot alert-specifications API
  slug: happyornot-alert-specifications-api
- description: Endpoints and data definitions related to alerts which have been triggered by incoming feedback, based on alert specfications
  name: HappyOrNot alerts API
  slug: happyornot-alerts-api
- description: Button feedback related endpoints and data definitions
  name: HappyOrNot button-feedbacks API
  slug: happyornot-button-feedbacks-api
- description: Contact details data endpoints and data definitions
  name: HappyOrNot contact-details API
  slug: happyornot-contact-details-api
- description: Endpoints and data definitions related to custom data fields
  name: HappyOrNot custom-data-fields API
  slug: happyornot-custom-data-fields-api
- description: Demographics data endpoints and data definitions
  name: HappyOrNot demographics API
  slug: happyornot-demographics-api
- description: Experience points and groups related endpoints and data definitions
  name: HappyOrNot experience-points API
  slug: happyornot-experience-points-api
- description: Follow-up feedback related endpoints and data definitions
  name: HappyOrNot follow-up-feedbacks API
  slug: happyornot-follow-up-feedbacks-api
- description: Endpoints and data definitions related to localizations for selectable options for follow ups in surveys
  name: HappyOrNot follow-up-option-localizations API
  slug: happyornot-follow-up-option-localizations-api
- description: Endpoints and data definitions related to selectable options for follow ups in surveys
  name: HappyOrNot follow-up-options API
  slug: happyornot-follow-up-options-api
- description: Endpoints and data definitions related to localizations for questions used for follow ups in surveys
  name: HappyOrNot follow-up-question-localizations API
  slug: happyornot-follow-up-question-localizations-api
- description: Endpoints and data definitions related to questions used for follow ups in surveys
  name: HappyOrNot follow-up-questions API
  slug: happyornot-follow-up-questions-api
- description: Metadata related endpoints and daa definitions
  name: HappyOrNot metadata API
  slug: happyornot-metadata-api
- description: Endpoints and data definitions related to localizations for question used in surveys
  name: HappyOrNot question-localizations API
  slug: happyornot-question-localizations-api
- description: Endpoints and data definitions related to questions used in surveys
  name: HappyOrNot questions API
  slug: happyornot-questions-api
- description: Endpoints and data definitions related to smileys
  name: HappyOrNot smileys API
  slug: happyornot-smileys-api
- description: Surveys related endpoints and data definitions
  name: HappyOrNot surveys API
  slug: happyornot-surveys-api
- description: Text feedback related endpoints and data definitions
  name: HappyOrNot text-feedbacks API
  slug: happyornot-text-feedbacks-api
- description: Token introspection including token scopes
  name: HappyOrNot token-introspection API
  slug: happyornot-token-introspection-api
- description: Endpoints and data definitions related to users
  name: HappyOrNot users API
  slug: happyornot-users-api
arazzos:
- description: Walk the experience-point tree, resolve surveys, then pull button feedback for a period.
  name: Resolve an experience point and fetch its button feedback
  slug: happyornot-fetch-feedback
- description: Read alert specifications, poll triggered alerts, then read their comments.
  name: Monitor HappyOrNot alerts
  slug: happyornot-monitor-alerts
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments API
  slug: open-happyornot-alert-comments-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments alert-specifications API
  slug: open-happyornot-alert-specifications-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments alerts API
  slug: open-happyornot-alerts-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments button-feedbacks API
  slug: open-happyornot-button-feedbacks-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments contact-details API
  slug: open-happyornot-contact-details-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments custom-data-fields API
  slug: open-happyornot-custom-data-fields-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments demographics API
  slug: open-happyornot-demographics-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments experience-points API
  slug: open-happyornot-experience-points-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments follow-up-feedbacks API
  slug: open-happyornot-follow-up-feedbacks-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments follow-up-option-localizations API
  slug: open-happyornot-follow-up-option-localizations-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments follow-up-options API
  slug: open-happyornot-follow-up-options-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments follow-up-question-localizations API
  slug: open-happyornot-follow-up-question-localizations-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments follow-up-questions API
  slug: open-happyornot-follow-up-questions-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments metadata API
  slug: open-happyornot-metadata-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments question-localizations API
  slug: open-happyornot-question-localizations-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments questions API
  slug: open-happyornot-questions-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments smileys API
  slug: open-happyornot-smileys-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments surveys API
  slug: open-happyornot-surveys-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments text-feedbacks API
  slug: open-happyornot-text-feedbacks-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments token-introspection API
  slug: open-happyornot-token-introspection-api
- collection_type: open
  name: HappyOrNot Customer API v2 alert-comments users API
  slug: open-happyornot-users-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/happyornot-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/happyornot-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/happyornot-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/happyornot-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/happyornot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/happyornot-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/happyornot-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://happyornot.github.io/docs/api-v1/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/happyornot-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/happyornot-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/happyornot-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/happyornot-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/happyornot-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/happyornot-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/happyornot-fetch-feedback.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/happyornot-monitor-alerts.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/happyornot-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://happyornot.github.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://happyornot.github.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.happy-or-not.com/v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://happyornot.github.io/docs/
- group: operate
  title: ''
  type: Support
  url: https://support.happy-or-not.com/
- group: company
  title: ''
  type: Blog
  url: https://www.happy-or-not.com/en/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/happyornot
- group: commercial
  title: ''
  type: Pricing
  url: https://www.happy-or-not.com/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://reporting.happy-or-not.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.happy-or-not.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.happy-or-not.com/en/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.happy-or-not.com
created: '2026-07-17'
description: HappyOrNot is a Finnish customer-experience feedback company known for its Smiley Terminal, Smiley Touch and Smiley Digital feedback devices used across retail, airports, healthcare, public sector and workplaces. Its read-only Customer API v2 lets applications and BI tools pull raw feedback data — button (smiley/NPS) ratings, follow-up selections, freeform text, AI demographics, contact-request details and metadata — together with the experience points, groups, surveys, questions, smileys, users and alerts that produce it. Authentication is a package-scoped API token (X-HON-API-Token header or auth query parameter); responses are JSON or CSV, paged with offset/limit and an X-More-Available header. The API is documented with an OpenAPI 3.1 specification and integrates with Power BI, Tableau, Salesforce, Medallia, Qualtrics and Zapier.
image: https://www.happy-or-not.com/wp-content/uploads/2021/03/HappyOrNot-logo.png
layout: provider
mcp_servers:
- description: ''
  name: happyornot-mcp.yml
  slug: happyornot-mcpyml
modified: '2026-07-19'
name: HappyOrNot
nav: Providers
network: true
overview: 'HappyOrNot publishes 21 APIs on the [APIs.io](https://apis.io/) network, including alert-comments API, alert-specifications API, alerts API, and 18 more. Tagged areas include Company, Enterprise, Customer Experience, Customer Feedback, and Surveys.


  HappyOrNot''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 23 more developer resources.'
random_paper: 65
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.3
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 48.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/happyornot/refs/heads/main/screenshots/happyornot-2026-07-25T220655.png
security:
- kind: authentication
  name: Happyornot Authentication
  slug: happyornot-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Happyornot Domain Security
  slug: happyornot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: happyornot
tags:
- Company
- Enterprise
- Customer Experience
- Customer Feedback
- Surveys
- Analytics
- Voice of Customer
- Retail
- Feedback
website: https://www.happy-or-not.com
---
