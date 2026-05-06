---
aid: amazon-nova
name: Amazon Nova
description: 'Amazon Nova is a new generation of state-of-the-art foundation models from Amazon that deliver a compelling combination of accuracy, speed, and cost efficiency. Amazon Nova models are accessible through Amazon Bedrock and support text, image, video, speech understanding and generation across a range of model types: Nova Premier (1M context), Nova Pro, Nova Lite, Nova Micro (text-only), Nova Canvas (image generation), Nova Reel (video generation), and Nova Sonic (speech).'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Foundation Models
  - Generative AI
  - Image Generation
  - Machine Learning
  - Multimodal
  - Speech
  - Video Generation
url: https://raw.githubusercontent.com/api-evangelist/amazon-nova/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-nova:amazon-nova-api
    name: Amazon Nova API
    description: The Amazon Nova API provides programmatic access to Amazon Nova foundation models through Amazon Bedrock for text, image, and video generation, understanding, and reasoning tasks. Supports Nova Premier, Pro, Lite, Micro, Canvas, Reel, and Sonic models.
    humanUrl: https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html
    baseUrl: https://bedrock-runtime.{region}.amazonaws.com
    tags:
      - Foundation Models
      - Generative AI
      - Multimodal
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html
      - type: APIReference
        url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/nova/latest/userguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/bedrock/pricing/
common:
  - type: Portal
    url: https://aws.amazon.com/ai/nova/
  - type: Website
    url: https://aws.amazon.com/ai/nova/
  - type: Documentation
    url: https://docs.aws.amazon.com/nova/
  - type: Terms of Service
    url: https://aws.amazon.com/service-terms/
  - type: Privacy Policy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/tag/amazon-nova/
  - type: GitHub Organization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/bedrock/
  - type: Sign Up
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Features
    data:
      - name: Multiple Model Types
        description: 'Seven specialized models: Nova Premier (1M context), Nova Pro, Nova Lite, Nova Micro (text), Nova Canvas (image), Nova Reel (video), Nova Sonic (speech).'
      - name: Multimodal Input
        description: Supports text, images, video, documents (PDF, CSV, DOCX, XLS, HTML), and speech as input modalities.
      - name: Long Context Windows
        description: Up to 1 million token context window in Nova Premier; 300k tokens in Nova Pro and Lite; 128k in Nova Micro.
      - name: Streaming Responses
        description: All understanding models support streaming for real-time interactive applications.
      - name: Batch Inference
        description: All understanding models support batch processing for high-volume offline workloads.
      - name: Fine-Tuning
        description: Nova Pro, Lite, and Micro support fine-tuning for domain-specific customization.
      - name: Model Distillation
        description: Nova Premier can serve as a teacher model for distillation into Pro, Lite, and Micro.
      - name: Bedrock Integration
        description: Natively integrated with Amazon Bedrock Knowledge Bases, Agents, Guardrails, Evaluations, and Prompt Flows.
  - type: UseCases
    data:
      - name: Interactive Chat Interfaces
        description: Build conversational AI applications with long context awareness using Nova Pro, Lite, or Micro.
      - name: Retrieval-Augmented Generation
        description: Enhance knowledge retrieval accuracy by combining Nova models with Bedrock Knowledge Bases.
      - name: Agentic Applications
        description: Build autonomous AI agents that reason and act using Nova models with Bedrock Agents.
      - name: Video and Document Analysis
        description: Analyze video content and complex documents (PDF, DOCX, XLS) with Nova Pro and Premier.
      - name: Image Generation and Editing
        description: Generate and edit high-quality images programmatically with Amazon Nova Canvas.
      - name: Video Generation
        description: Create short video clips from text or image prompts using Amazon Nova Reel.
      - name: Voice Assistants
        description: Build voice-enabled customer service and assistant applications with Nova Sonic speech model.
      - name: UI Workflow Automation
        description: Automate UI interactions and screen navigation workflows using Nova vision capabilities.
  - type: Integrations
    data:
      - name: Amazon Bedrock
        description: Primary access method; all Nova models are served through the Bedrock InvokeModel and InvokeModelWithResponseStream APIs.
      - name: Bedrock Knowledge Bases
        description: Connect Nova models to structured and unstructured data sources for RAG applications.
      - name: Bedrock Agents
        description: Orchestrate multi-step agentic workflows with tool use and memory using Nova as the reasoning engine.
      - name: Bedrock Guardrails
        description: Apply safety guardrails to Nova Premier, Pro, and Lite model outputs for content filtering.
      - name: Bedrock Prompt Flows
        description: Build visual prompt chaining workflows connecting Nova models with other services.
      - name: Bedrock Evaluations
        description: Evaluate Nova model performance on custom benchmarks and safety criteria.
      - name: Amazon S3
        description: Store and access training data, batch inference inputs/outputs, and generated media artifacts.
      - name: AWS IAM
        description: Control access to Nova model invocations through fine-grained IAM policies and Bedrock model access settings.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
