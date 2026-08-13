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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Inflectionio Agentic Access
  operation_count: 18
  slug: inflectionio-agentic-access
  summary_line: 18 operations · 9 acting
api_count: 4
apis:
- description: The Contact Activity API from Inflection.io — 4 operation(s) for contact activity.
  name: Inflection.io Contact Activity API
  slug: inflectionio-contact-activity-api
- description: The Contacts API from Inflection.io — 5 operation(s) for contacts.
  name: Inflection.io Contacts API
  slug: inflectionio-contacts-api
- description: The Email Templates API from Inflection.io — 1 operation(s) for email templates.
  name: Inflection.io Email Templates API
  slug: inflectionio-email-templates-api
- description: The Lists and Members API from Inflection.io — 4 operation(s) for lists and members.
  name: Inflection.io Lists and Members API
  slug: inflectionio-lists-and-members-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.inflection.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/inflectionio/mintlify-docs/tree/develop/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/inflectionio/mintlify-docs/tree/develop/api-reference
- group: docs
  title: ''
  type: APIReference
  url: https://api.inflection.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/inflectionio/mintlify-docs/blob/develop/api-reference/quickstart.mdx
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.inflection.io
- group: operate
  title: ''
  type: Support
  url: https://docs.inflection.io
- group: company
  title: ''
  type: Blog
  url: https://www.inflection.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.inflection.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.inflection.io/login/start
- group: start
  title: ''
  type: Login
  url: https://app.inflection.io/login/start
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inflection.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inflection.io/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inflectionio
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/inflectionio-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/inflectionio-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inflectionio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inflectionio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inflectionio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inflectionio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inflectionio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inflectionio-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inflectionio-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/inflectionio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inflectionio-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inflectionio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inflectionio-domain-security.yml
created: '2026-07-17'
description: 'Inflection.io is a B2B marketing automation platform positioned as a modern, AI-native replacement for legacy tools like Marketo. It unifies target accounts, product users, customers, and leads with product-usage, sales, and behavioral signals so marketing teams can build audiences, draft campaigns, map customer journeys, score accounts, and report to the CMO — executing in minutes rather than weeks. The Inflection Developer API is a JSON-over-HTTPS REST API (OpenAPI 3.1, base https://api.inflection.io/v1) for reading and writing the people in a workspace: their profiles, product and marketing activity, static lists, and email templates, authenticated with scoped Personal Access Tokens. Surfaced as a version-one-ventures portfolio company and enriched from the provider''s public developer API surface.'
image: https://www.inflection.io/img/asset/YXNzZXRzL29nLWltYWdlLmpwZw/og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: inflectionio-mcp.yml
  slug: inflectionio-mcpyml
modified: '2026-07-19'
name: Inflection.io
nav: Providers
network: true
overview: 'Inflection.io publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Contact Activity API, Contacts API, Email Templates API, and 1 more. Tagged areas include Company, Saas, Marketing, Marketing Automation, and Email Marketing.


  Inflection.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 83
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 57.8
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inflectionio/refs/heads/main/screenshots/inflectionio-2026-07-25T222410.png
security:
- kind: authentication
  name: Inflectionio Authentication
  slug: inflectionio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inflectionio Domain Security
  slug: inflectionio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: inflectionio
tags:
- Company
- Saas
- Marketing
- Marketing Automation
- Email Marketing
- Customer Data
- B2B
- Contacts
- API
website: https://www.inflection.io
---
