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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Analyze and save documents against a project.
  name: Lang.ai Documents API
  slug: langai-documents-api
- description: Create and inspect classification projects and their tags.
  name: Lang.ai Projects API
  slug: langai-projects-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://lang.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lang.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lang.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lang.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lang.ai/#workflow
- group: operate
  title: ''
  type: Support
  url: https://help.lang.ai/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.lang.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lang-ai
- group: company
  title: ''
  type: Blog
  url: https://capacity.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://capacity.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://capacity.com/lang/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capacity.com/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capacity.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.capacity.com/
- group: auth
  title: ''
  type: Compliance
  url: https://capacity.com/security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/langai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/langai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/langai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/langai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/langai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/langai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/langai-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/langai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/langai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/langai-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/langai-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/langai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/langai-trust-center.yml
created: '2026-07-17'
description: 'Lang.ai is a conversation-intelligence platform that turns unstructured customer interactions — support tickets, chatbot messages, emails and calls — into structured intents, features and tags. Its unsupervised algorithm ingests a dataset of customer text, automatically extracts the intents and features it finds, and lets teams group those into tags that form a custom classifier for any language, industry or business case. A small REST API then applies that classifier in real time: create a project from a CSV dataset, list projects and their tags, analyze a document to get back its matched tags and intents, and save documents with arbitrary metadata for dashboard reporting. Lang.ai was founded in Spain, backed by 500 Global, and is now part of Capacity, whose AI support-automation platform absorbed Lang.ai''s conversation intelligence.'
image: https://docs.lang.ai/images/logo-lang.svg
layout: provider
mcp_servers:
- description: ''
  name: langai-mcp.yml
  slug: langai-mcpyml
modified: '2026-07-19'
name: Lang.ai
nav: Providers
network: true
overview: 'Lang.ai publishes 2 APIs on the [APIs.io](https://apis.io/) network: Documents API and Projects API. Tagged areas include Company, Artificial Intelligence, Machine Learning, Natural Language Processing, and Conversation Intelligence.


  Lang.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 53.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.9
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 53.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Langai Authentication
  slug: langai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Langai Domain Security
  slug: langai-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Langai Vulnerability Disclosure
  slug: langai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Langai Trust Center
  slug: langai-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR
slug: langai
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- Conversation Intelligence
- Customer Support
- Text Classification
- Analytics
- Customer Experience
website: https://lang.ai
---
