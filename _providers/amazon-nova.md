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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Nova Agentic Access
  operation_count: 6
  slug: amazon-nova-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 3
apis:
- description: The Amazon Nova API provides programmatic access to Amazon Nova foundation models through Amazon Bedrock for text, image, and video generation, understanding, and reasoning tasks. Supports Nova Premie
  name: Amazon Nova API
  slug: amazon-nova-api
- description: Asynchronous invocation for long-running generation jobs.
  name: Amazon Nova Async API
  slug: amazon-nova-async-api
- description: Synchronous and streaming inference operations.
  name: Amazon Nova Inference API
  slug: amazon-nova-inference-api
artifact_total: 36
collections:
- collection_type: open
  name: Amazon Nova on Amazon Bedrock Runtime API
  slug: open-amazon-nova
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-nova-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-nova-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-nova-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-nova-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-nova-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/ai/nova/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/ai/nova/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/nova/
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
  url: https://aws.amazon.com/blogs/machine-learning/tag/amazon-nova/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/bedrock/
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
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
created: '2026-03-16'
description: 'Amazon Nova is a new generation of state-of-the-art foundation models from Amazon that deliver a compelling combination of accuracy, speed, and cost efficiency. Amazon Nova models are accessible through Amazon Bedrock and support text, image, video, speech understanding and generation across a range of model types: Nova Premier (1M context), Nova Pro, Nova Lite, Nova Micro (text-only), Nova Canvas (image generation), Nova Reel (video generation), and Nova Sonic (speech).'
features:
- description: 'Seven specialized models: Nova Premier (1M context), Nova Pro, Nova Lite, Nova Micro (text), Nova Canvas (image), Nova Reel (video), Nova Sonic (speech).'
  name: Multiple Model Types
- description: Supports text, images, video, documents (PDF, CSV, DOCX, XLS, HTML), and speech as input modalities.
  name: Multimodal Input
- description: Up to 1 million token context window in Nova Premier; 300k tokens in Nova Pro and Lite; 128k in Nova Micro.
  name: Long Context Windows
- description: All understanding models support streaming for real-time interactive applications.
  name: Streaming Responses
- description: All understanding models support batch processing for high-volume offline workloads.
  name: Batch Inference
- description: Nova Pro, Lite, and Micro support fine-tuning for domain-specific customization.
  name: Fine-Tuning
- description: Nova Premier can serve as a teacher model for distillation into Pro, Lite, and Micro.
  name: Model Distillation
- description: Natively integrated with Amazon Bedrock Knowledge Bases, Agents, Guardrails, Evaluations, and Prompt Flows.
  name: Bedrock Integration
finops:
- name: Amazon Nova Finops
  service_category: API
  slug: amazon-nova-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-nova.png
integrations:
- description: Primary access method; all Nova models are served through the Bedrock InvokeModel and InvokeModelWithResponseStream APIs.
  name: Amazon Bedrock
- description: Connect Nova models to structured and unstructured data sources for RAG applications.
  name: Bedrock Knowledge Bases
- description: Orchestrate multi-step agentic workflows with tool use and memory using Nova as the reasoning engine.
  name: Bedrock Agents
- description: Apply safety guardrails to Nova Premier, Pro, and Lite model outputs for content filtering.
  name: Bedrock Guardrails
- description: Build visual prompt chaining workflows connecting Nova models with other services.
  name: Bedrock Prompt Flows
- description: Evaluate Nova model performance on custom benchmarks and safety criteria.
  name: Bedrock Evaluations
- description: Store and access training data, batch inference inputs/outputs, and generated media artifacts.
  name: Amazon S3
- description: Control access to Nova model invocations through fine-grained IAM policies and Bedrock model access settings.
  name: AWS IAM
layout: provider
modified: '2026-04-19'
name: Amazon Nova
nav: Providers
network: true
overview: 'Amazon Nova publishes 2 APIs on the [APIs.io](https://apis.io/) network: Async API and Inference API. Tagged areas include Foundation Models, Generative AI, Image Generation, Machine Learning, and Multimodal.


  Amazon Nova''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 11 more developer resources.'
plans:
- name: Amazon Nova Plans Pricing
  plan_count: 3
  slug: amazon-nova-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Amazon Nova Rate Limits
  slug: amazon-nova-rate-limits
score:
  band: developing
  composite: 50.3
  delta: -1.4
  facets:
    commercial_clarity: 81.6
    contract_quality: 53.4
    developer_ergonomics: 41.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-nova/refs/heads/main/screenshots/amazon-nova-2026-06-20T171754.png
security:
- kind: authentication
  name: Amazon Nova Authentication
  slug: amazon-nova-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Nova Domain Security
  slug: amazon-nova-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Nova Vulnerability Disclosure
  slug: amazon-nova-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Nova Trust Center
  slug: amazon-nova-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-nova
tags:
- Foundation Models
- Generative AI
- Image Generation
- Machine Learning
- Multimodal
- Speech
- Video Generation
use_cases:
- description: Build conversational AI applications with long context awareness using Nova Pro, Lite, or Micro.
  name: Interactive Chat Interfaces
- description: Enhance knowledge retrieval accuracy by combining Nova models with Bedrock Knowledge Bases.
  name: Retrieval-Augmented Generation
- description: Build autonomous AI agents that reason and act using Nova models with Bedrock Agents.
  name: Agentic Applications
- description: Analyze video content and complex documents (PDF, DOCX, XLS) with Nova Pro and Premier.
  name: Video and Document Analysis
- description: Generate and edit high-quality images programmatically with Amazon Nova Canvas.
  name: Image Generation and Editing
- description: Create short video clips from text or image prompts using Amazon Nova Reel.
  name: Video Generation
- description: Build voice-enabled customer service and assistant applications with Nova Sonic speech model.
  name: Voice Assistants
- description: Automate UI interactions and screen navigation workflows using Nova vision capabilities.
  name: UI Workflow Automation
website: https://aws.amazon.com/ai/nova/
---
