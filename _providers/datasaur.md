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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 5
asyncapis:
- description: ''
  name: Datasaur Webhooks
  slug: datasaur-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://datasaur.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.datasaur.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datasaur.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.datasaur.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datasaur.ai/welcome-to-datasaur/readme
- group: company
  title: ''
  type: Blog
  url: https://datasaur.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://datasaur.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.datasaur.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.datasaur.ai/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@datasaur.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datasaur.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datasaur.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datasaur-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datasaur.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/datasaur-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://datasaur.ai/studio/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datasaur-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datasaur-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/datasaur-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/datasaur-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/datasaur-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datasaur-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/datasaur-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/datasaur-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/datasaur-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/datasaur-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/datasaur-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/datasaur-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/datasaur-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Datasaur is an enterprise AI lab that builds private, secure LLM and data solutions deployed on a customer's own infrastructure. Its Data Studio is a collaborative data-labeling platform (span, row, document, bounding-box, conversational and audio tasks) with ML-assisted labeling, while LLM Labs covers sandboxing, deployment, knowledge bases, model integrations and evaluation. Products include an enterprise chatbot, document intelligence, PII/PHI redaction and private agents, serving legal, healthcare, finance, insurance, eCommerce and government. Developers integrate through a GraphQL API (OAuth2 client credentials) at app.datasaur.ai/graphql, the Robosaur CLI, webhooks, and SAML/SCIM for workspace SSO.
image: https://cdn.prod.website-files.com/623952e7f678f73f3096fd25/66c5ad5767cd845864d963b5_webclip.jpg
layout: provider
mcp_servers:
- description: ''
  name: Datasaur MCP (candidate)
  slug: datasaur-mcp-candidate
modified: '2026-07-18'
name: Datasaur
nav: Providers
network: true
overview: 'Datasaur is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, Data Labeling, Artificial Intelligence, and Machine Learning.


  The Datasaur catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Datasaur''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 23 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 51.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 51.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datasaur/refs/heads/main/screenshots/datasaur-2026-07-25T211356.png
security:
- kind: authentication
  name: Datasaur Authentication
  slug: datasaur-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Datasaur Domain Security
  slug: datasaur-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Datasaur Trust Center
  slug: datasaur-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: datasaur
tags:
- Company
- Enterprise Saas
- Data Labeling
- Artificial Intelligence
- Machine Learning
- Large Language Models
- NLP
- Data Annotation
- GraphQL
website: https://datasaur.ai/
---
