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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Definedcrowd Agentic Access
  operation_count: 29
  slug: definedcrowd-agentic-access
  summary_line: 29 operations · 14 acting
api_count: 8
apis:
- description: The result file is created after the project is completed and is referred to as deliverables. The file contains contributor metadata for completed input units.
  name: Defined.ai (DefinedCrowd) Deliverables API
  slug: definedcrowd-deliverables-api
- description: Each input unit is a single component of work done by the contributors. There are several types of units – audio, text, and image. In a given project, all units should have the same structure. The inp
  name: Defined.ai (DefinedCrowd) Input Units API
  slug: definedcrowd-input-units-api
- description: Jobs are how your data (input units) connects the project with our contributors. Each job has data, instructions, and customizable parameters, which then convert inputs to outputs. Parameters are cust
  name: Defined.ai (DefinedCrowd) Jobs API
  slug: definedcrowd-jobs-api
- description: Aggregate ratings on the "intelligibility" and "naturalness" of utterances.
  name: Defined.ai (DefinedCrowd) Mean Opinion Score API
  slug: definedcrowd-mean-opinion-score-api
- description: Informally, projects can be viewed as configurable packages that process sets of Input Units. The project’s template determines how the Input Units are processed. Projects can be retrieved and managed
  name: Defined.ai (DefinedCrowd) Project Management API
  slug: definedcrowd-project-management-api
- description: Confirm audio meets pronunciation standards.
  name: Defined.ai (DefinedCrowd) Pronunciation Validation API
  slug: definedcrowd-pronunciation-validation-api
- description: Subscribe to automatic notifications for specific email addresses. Email notifications are sent for events that happen during the life cycle of the project. <small> By using this service, the user ful
  name: Defined.ai (DefinedCrowd) Subscriptions API
  slug: definedcrowd-subscriptions-api
- description: 'Several of the Workflow Templates offer the ability to set a language / country code. These configurations instruct Defined.ai to use our human intelligence Contributors that speak and / or reside in '
  name: Defined.ai (DefinedCrowd) Supported Languages API
  slug: definedcrowd-supported-languages-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/definedcrowd-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/definedcrowd-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/definedcrowd-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.definedcrowd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.definedcrowd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.definedcrowd.com/
- group: company
  title: ''
  type: Blog
  url: https://defined.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://defined.ai/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://defined.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://defined.ai/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://enterprise.definedcrowd.com
- group: agent
  title: ''
  type: LLMsTxt
  url: https://defined.ai/llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/definedcrowd-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/definedcrowd-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/definedcrowd-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/definedcrowd-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/definedcrowd-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/definedcrowd-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://defined.ai/about-us
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/definedcrowd-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Defined.ai (formerly DefinedCrowd) is an AI training data platform and marketplace founded in 2015 by Daniela Braga, headquartered in Seattle with offices in Lisbon, Porto, and Tokyo. It provides ready-to-use datasets across speech, text, image, video, and multimodal, plus custom data collection, annotation, machine translation, conversational AI, LLM fine-tuning, and data and model evaluation services sourced from a global community of 1.6M+ vetted contributors across 150+ markets and 500+ languages, dialects, and locales. The Defined.ai Public API (v2.0) lets enterprise customers manage projects programmatically — create Mean Opinion Score and Pronunciation Validation projects, upload input units, configure supported languages, track project status and errors, manage jobs, retrieve deliverables, and subscribe to notifications. Data provenance and compliance are backed by ISO 27001, ISO 27701, ISO 42001, GDPR, and HIPAA.
image: https://defined.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: definedcrowd-mcp.yml
  slug: definedcrowd-mcpyml
modified: '2026-07-18'
name: Defined.ai (DefinedCrowd)
nav: Providers
network: true
overview: 'Defined.ai (DefinedCrowd) publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Deliverables API, Input Units API, Jobs API, and 5 more. Tagged areas include Company, AI Training Data, Data Marketplace, Machine Learning, and Data Annotation.


  Defined.ai (DefinedCrowd)''s developer surface includes authentication, documentation, engineering blog, support, signup flow, and 16 more developer resources.'
random_paper: 102
score:
  band: thin
  composite: 40.4
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 54.6
    developer_ergonomics: 38.6
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/definedcrowd/refs/heads/main/screenshots/definedcrowd-2026-07-25T211622.png
security:
- kind: authentication
  name: Definedcrowd Authentication
  slug: definedcrowd-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Definedcrowd Domain Security
  slug: definedcrowd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: definedcrowd
tags:
- Company
- AI Training Data
- Data Marketplace
- Machine Learning
- Data Annotation
- Speech Data
- Natural Language Processing
- Crowdsourcing
- Artificial Intelligence
website: https://www.definedcrowd.com/
---
