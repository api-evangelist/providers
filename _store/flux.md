---
aid: flux
url: https://raw.githubusercontent.com/api-evangelist/flux/refs/heads/main/apis.yml
apis:
- aid: flux:flux-image-generation-api
  name: Flux Image Generation API
  description: REST API for generating images from text prompts using Black Forest Labs' FLUX models, including FLUX.1 [pro], FLUX.1 [dev], FLUX.1 [schnell], and FLUX.2 variants. The API follows an asynchronous pattern where requests return a polling URL to retrieve the completed image result.
  humanURL: https://docs.bfl.ai/
  baseURL: https://api.bfl.ai/v1
  tags:
  - AI
  - Image Generation
  - Machine Learning
  - Text to Image
  properties:
  - type: Documentation
    url: https://docs.bfl.ai/
  - type: Getting Started
    url: https://docs.bfl.ml/quick_start/generating_images
  - type: Authentication
    url: https://docs.bfl.ai/
  - type: OpenAPI
    url: openapi/flux-image-generation-openapi.yml
  - type: JSONSchema
    url: json-schema/flux-generation-request-schema.json
- aid: flux:flux-image-editing-api
  name: Flux Image Editing API
  description: REST API for editing and transforming existing images using the FLUX.1 Kontext models. Accepts an input image and a text prompt describing desired edits, and returns a modified image. Supports context-aware in-painting, style transfer, and image-to-image transformations.
  humanURL: https://docs.bfl.ml/kontext/kontext_image_editing
  baseURL: https://api.bfl.ai/v1
  tags:
  - AI
  - Image Editing
  - Image to Image
  - Kontext
  properties:
  - type: Documentation
    url: https://docs.bfl.ml/kontext/kontext_image_editing
  - type: OpenAPI
    url: openapi/flux-image-editing-openapi.yml
name: Flux
tags:
- AI
- Image Generation
- Machine Learning
- Open Source
- Text to Image
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: An open-source text-to-image AI model developed by Black Forest Labs that generates high-quality images from text prompts with improved prompt following and visual quality.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

