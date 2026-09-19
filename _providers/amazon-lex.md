---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.1
  scored_at: '2026-09-18'
agentic_access:
- acting_count: 92
  human_in_the_loop: 2
  name: Amazon Lex Agentic Access
  operation_count: 113
  slug: amazon-lex-agentic-access
  summary_line: 113 operations · 92 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://models-v2-lex.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Lex bot management
  name: Amazon Lex Bots API
  slug: amazon-lex-bots-api
- baseURL: https://runtime-v2-lex.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'Send user input to a built Amazon Lex V2 bot and manage the conversation session. Six operations: RecognizeText (text turn), RecognizeUtterance (audio or text turn), StartConversation (bidirectional H'
  name: Amazon Lex Runtime V2 API
  slug: amazon-lex-runtime-v2-api
artifact_total: 39
collections:
- collection_type: postman
  name: Amazon Lex Bots API
  slug: postman-amazon-lex-bots-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Lex Bots API
  slug: open-amazon-lex-bots-api
- collection_type: open
  name: Amazon Lex API
  slug: open-amazon-lex
- collection_type: open
  name: Amazon Lex API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-lex/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/agentic-access/amazon-lex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-lex-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/security/amazon-lex-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-lex-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/security/amazon-lex-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-lex-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/security/amazon-lex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-lex-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/authentication/amazon-lex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-lex-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/lex/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/lex/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/lexv2/home
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: knowledge-center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-lex
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/rules/amazon-lex-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-lex-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/vocabulary/amazon-lex-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-lex-vocabulary.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/lex/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/lexv2/latest/APIReference/Welcome.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/lexv2/latest/dg/getting-started.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/lex/pricing/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/smithy/amazon-lex-models-v2-2020-08-07.json
  title: ''
  type: Smithy
  url: smithy/amazon-lex-models-v2-2020-08-07.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/packages/amazon-lex-packages.yml
  title: ''
  type: Packages
  url: packages/amazon-lex-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/packages/amazon-lex-packages.yml
  title: ''
  type: SDKs
  url: packages/amazon-lex-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/cli/amazon-lex-cli.yml
  title: ''
  type: CLI
  url: cli/amazon-lex-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/well-known/amazon-lex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-lex-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/well-known/amazon-lex-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-lex-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/mcp/amazon-lex-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amazon-lex-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/mcp/amazon-lex-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/amazon-lex-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/llms/amazon-lex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-lex-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/conformance/amazon-lex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-lex-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/errors/amazon-lex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amazon-lex-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/lifecycle/amazon-lex-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-lex-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.aws.amazon.com/lexv2/latest/dg/migration.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/conventions/amazon-lex-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amazon-lex-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/changelog/amazon-lex-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/amazon-lex-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/sandbox/amazon-lex-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/amazon-lex-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/data-model/amazon-lex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amazon-lex-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/plans/amazon-lex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-lex-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/rate-limits/amazon-lex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-lex-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/examples/amazon-lex-bot-example.json
  title: ''
  type: Examples
  url: examples/amazon-lex-bot-example.json
created: '2024-01-15'
description: Amazon Lex is a fully managed artificial intelligence (AI) service with advanced natural language models to design, build, test, and deploy conversational interfaces in applications. It provides the deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, enabling you to build applications with highly engaging user experiences and lifelike conversational interactions.
examples:
- key_count: 7
  name: Amazon Lex Bot Example
  slug: amazon-lex-bot-example
- key_count: 7
  name: Amazon Lex Intent Example
  slug: amazon-lex-intent-example
features:
- description: Convert speech to text with high accuracy using the same deep learning technology as Amazon Alexa.
  name: Automatic Speech Recognition
- description: Understand the intent behind user input to build conversational interfaces.
  name: Natural Language Understanding
- description: Deploy bots across web, mobile, messaging channels (Slack, Facebook Messenger, Twilio), and contact centers.
  name: Multi-Channel Deployment
- description: Build intelligent contact center bots with native integration with Amazon Connect.
  name: Amazon Connect Integration
- description: Support multi-turn streaming conversations for complex dialog flows.
  name: Streaming Conversations
- description: Recognize user intents and extract slot values from natural language input.
  name: Intent Recognition
finops:
- name: Amazon Lex Finops
  service_category: API
  slug: amazon-lex-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Deploy Lex bots in Amazon Connect contact flows for IVR and agent assist.
  name: Amazon Connect
- description: Combine Lex for dialog management with Kendra for intelligent document search.
  name: Amazon Kendra
- description: Use Lambda for fulfillment logic and business rules in bot conversations.
  name: AWS Lambda
- description: Convert bot text responses to natural speech using Amazon Polly TTS.
  name: Amazon Polly
json_schemas:
- name: Bot
  property_count: 7
  slug: amazon-lex-bot
- name: Intent
  property_count: 7
  slug: amazon-lex-intent
json_structures:
- name: Amazon Lex Bot Structure
  property_count: 7
  slug: amazon-lex-bot-structure
- name: Amazon Lex Intent Structure
  property_count: 7
  slug: amazon-lex-intent-structure
jsonld:
- class_count: 2
  name: Amazon Lex Context
  property_count: 7
  slug: amazon-lex-context
layout: provider
mcp_servers:
- description: ''
  name: Amazon Lex MCP Server
  slug: amazon-lex-mcp-server
modified: '2026-09-17'
name: Amazon Lex
nav: Providers
network: true
overview: 'Amazon Lex publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bots API and Runtime V2 API. Tagged areas include Artificial Intelligence, Conversational AI, Chatbots, Natural Language Processing, and Speech.


  The Amazon Lex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Lex''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 44 more developer resources.'
plans:
- name: Amazon Lex Plans Pricing
  plan_count: 1
  slug: amazon-lex-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 24
  name: Amazon Lex Rate Limits
  slug: amazon-lex-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Amazon Lex API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 2
  slug: amazon-lex-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon Lex API Rules
  rule_count: 24
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 14
  slug: amazon-lex-spectral-rules
score:
  band: exemplar
  composite: 76.6
  coverage:
    artifact_dirs: 33
    catalog_earned: 84.5
    catalog_earned_first_party: 20.0
    catalog_gap: 30.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 82.9
    contract_governance: 47.0
    contract_quality: 78.2
    developer_ergonomics: 78.0
    discoverability: 75.9
    operational_transparency: 86.8
  previous_composite: 76.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/screenshots/amazon-lex-2026-06-20T171723.png
security:
- kind: authentication
  name: Amazon Lex Authentication
  slug: amazon-lex-authentication
  summary_line: sigv4 · 1 scheme
- kind: domain-security
  name: Amazon Lex Domain Security
  slug: amazon-lex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Lex Vulnerability Disclosure
  slug: amazon-lex-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Lex Trust Center
  slug: amazon-lex-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-lex
tags:
- Artificial Intelligence
- Conversational AI
- Chatbots
- Natural Language Processing
- Speech
- Voice
- Contact Center
- Customer Service
use_cases:
- description: Build self-service chatbots for customer support and FAQ handling.
  name: Customer Service Chatbot
- description: Automate contact center interactions with intelligent IVR and agent assist.
  name: Contact Center Automation
- description: Create employee-facing bots for IT help desk and HR self-service.
  name: Internal Help Desk
- description: Build shopping assistants that understand natural language product queries.
  name: E-Commerce Assistant
website: https://aws.amazon.com/lex/
---
