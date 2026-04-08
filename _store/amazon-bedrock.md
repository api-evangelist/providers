---
aid: amazon-bedrock
url: https://raw.githubusercontent.com/api-evangelist/amazon-bedrock/refs/heads/main/apis.yml
apis:
- aid: amazon-bedrock:amazon-bedrock-api
  name: Amazon Bedrock API
  tags:
  - Foundation Models
  - Generative AI
  humanURL: https://docs.aws.amazon.com/bedrock/latest/APIReference/
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/bedrock/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-bedrock-openapi.yml
  - type: JSONSchema
    url: json-schema/amazon-bedrock-model-schema.json
  description: The Amazon Bedrock management API provides operations for managing foundation models, custom models, model customization jobs, provisioned throughput, guardrails, and other Bedrock resources.
- aid: amazon-bedrock:amazon-bedrock-runtime-api
  name: Amazon Bedrock Runtime API
  tags:
  - Foundation Models
  - Generative AI
  humanURL: https://docs.aws.amazon.com/bedrock/latest/APIReference/
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/bedrock/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-bedrock-runtime-openapi.yml
  description: The Amazon Bedrock Runtime API provides operations for invoking foundation models and running inference.
name: Amazon Bedrock
tags:
- AI
- AWS
- Foundation Models
- Generative AI
- LLM
- Machine Learning
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Bedrock is a fully managed service that makes high-performing foundation models (FMs) from leading AI companies available through a unified API. It enables developers to build and scale generative AI applications using foundation models for text generation, summarization, image generation, and conversational AI without managing infrastructure. Bedrock supports model customization, fine-tuning, and retrieval-augmented generation (RAG) to tailor models to specific use cases.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

