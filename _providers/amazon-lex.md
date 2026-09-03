---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Amazon Lex Agentic Access
  operation_count: 7
  slug: amazon-lex-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 2
apis:
- baseURL: https://models-v2-lex.amazonaws.com
  baseurl_source: declared
  description: Lex bot management
  name: Amazon Lex Bots API
  slug: amazon-lex-bots-api
artifact_total: 37
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
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-lex-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-lex-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-lex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-lex-domain-security.yml
- group: auth
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
  type: github
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/lex/
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
  title: ''
  type: SpectralRules
  url: rules/amazon-lex-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-lex-vocabulary.yaml
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
modified: '2026-05-19'
name: Amazon Lex
nav: Providers
network: true
overview: 'Amazon Lex publishes 1 API on the [APIs.io](https://apis.io/) network: Bots API.


  The Amazon Lex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Lex''s developer surface includes authentication, developer portal, documentation, support, engineering blog, GitHub presence, developer console, and 19 more developer resources.'
plans:
- name: Amazon Lex Plans Pricing
  plan_count: 3
  slug: amazon-lex-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
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
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 57.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 28.8
    contract_quality: 72.8
    developer_ergonomics: 58.3
    discoverability: 44.4
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: false
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-lex/refs/heads/main/screenshots/amazon-lex-2026-06-20T171723.png
security:
- kind: authentication
  name: Amazon Lex Authentication
  slug: amazon-lex-authentication
  summary_line: apiKey · 1 scheme
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
