---
aid: stability-ai
name: Stability AI
description: Stability AI is an AI company that develops open-source generative AI models for image, audio, video, and language, including the Stable Diffusion family of image generation models. The Stability AI developer platform provides REST APIs for text-to-image generation, image editing, image upscaling, image structure control, video generation, and 3D asset creation. All APIs are accessible at api.stability.ai using bearer token authentication.
url: https://raw.githubusercontent.com/api-evangelist/stability-ai/refs/heads/main/apis.yml
tags:
  - 3D Generation
  - AI
  - Generative AI
  - Image Generation
  - Image Editing
  - Machine Learning
  - Stable Diffusion
  - Text to Image
  - Video Generation
created: '2026-03-20'
modified: '2026-05-04'
apis:
  - aid: stability-ai:stable-image-generate
    name: Stability AI Stable Image Generate API
    tags:
      - Generative AI
      - Image Generation
      - Stable Diffusion
      - Text to Image
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.stability.ai
    humanURL: https://platform.stability.ai/docs/getting-started/stable-image
    description: The Stability AI Stable Image Generate API provides text-to-image generation capabilities powered by models including Stable Diffusion 3.5 and Stable Image Ultra. Developers can generate high-quality images from text prompts with control over style, dimensions, and output format. The API supports multiple model tiers including Stable Image Core for fast and affordable generation and Stable Image Ultra for state-of-the-art quality results.
    properties:
      - url: https://platform.stability.ai/docs/api-reference
        type: Documentation
      - url: openapi/stability-ai-stable-image-generate-openapi.yml
        type: OpenAPI
  - aid: stability-ai:stable-image-edit
    name: Stability AI Stable Image Edit API
    tags:
      - Generative AI
      - Image Editing
      - Inpainting
      - Outpainting
      - Search and Replace
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.stability.ai
    humanURL: https://platform.stability.ai/docs/api-reference
    description: The Stability AI Stable Image Edit API provides image editing capabilities including inpainting, outpainting, object erasing, background removal, and search-and-replace functionality. Developers can use natural language prompts to modify existing images, fill in masked regions, extend image boundaries, or replace specific objects within a scene.
    properties:
      - url: https://platform.stability.ai/docs/api-reference
        type: Documentation
      - url: openapi/stability-ai-stable-image-edit-openapi.yml
        type: OpenAPI
  - aid: stability-ai:stable-image-upscale
    name: Stability AI Stable Image Upscale API
    tags:
      - Generative AI
      - Image Enhancement
      - Image Upscaling
      - Super Resolution
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.stability.ai
    humanURL: https://platform.stability.ai/docs/api-reference
    description: The Stability AI Stable Image Upscale API enables developers to increase the resolution of images using AI-powered upscaling models. The API offers both conservative upscaling, which preserves the original image closely while increasing resolution, and creative upscaling, which enhances and adds detail to images during the upscaling process.
    properties:
      - url: https://platform.stability.ai/docs/api-reference
        type: Documentation
      - url: openapi/stability-ai-stable-image-upscale-openapi.yml
        type: OpenAPI
  - aid: stability-ai:stable-image-control
    name: Stability AI Stable Image Control API
    tags:
      - ControlNet
      - Generative AI
      - Image Generation
      - Image to Image
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.stability.ai
    humanURL: https://platform.stability.ai/docs/api-reference
    description: The Stability AI Stable Image Control API provides image-to-image generation guided by structural inputs such as sketches and reference structures. Using ControlNet-based models, developers can generate new images that follow the composition, edges, or layout of a source image while applying new styles or content based on text prompts.
    properties:
      - url: https://platform.stability.ai/docs/api-reference
        type: Documentation
      - url: openapi/stability-ai-stable-image-control-openapi.yml
        type: OpenAPI
  - aid: stability-ai:stable-video-diffusion
    name: Stability AI Stable Video Diffusion API
    tags:
      - Generative AI
      - Image to Video
      - Stable Diffusion
      - Video Generation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.stability.ai
    humanURL: https://platform.stability.ai/docs/getting-started/stable-video
    description: The Stability AI Stable Video Diffusion API enables developers to generate short video clips from a single input image. Powered by the Stable Video Diffusion model, the API produces smooth animated sequences that bring static images to life with realistic motion.
    properties:
      - url: https://platform.stability.ai/docs/getting-started/stable-video-diffusion
        type: Documentation
      - url: openapi/stability-ai-stable-video-diffusion-openapi.yml
        type: OpenAPI
  - aid: stability-ai:stable-fast-3d
    name: Stability AI Stable Fast 3D API
    tags:
      - 3D Generation
      - Generative AI
      - Image to 3D
      - Mesh Generation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.stability.ai
    humanURL: https://platform.stability.ai/docs/api-reference
    description: The Stability AI Stable Fast 3D API generates textured 3D mesh assets from single input images. The API rapidly produces 3D models suitable for use in games, augmented reality, virtual reality, and product visualization workflows.
    properties:
      - url: https://platform.stability.ai/docs/api-reference
        type: Documentation
      - url: openapi/stability-ai-stable-fast-3d-openapi.yml
        type: OpenAPI
common:
  - type: Website
    url: https://stability.ai
  - type: Documentation
    url: https://platform.stability.ai/docs/getting-started
  - type: Portal
    url: https://platform.stability.ai
  - type: Pricing
    url: https://stability.ai/api-pricing-update-25
  - type: Terms of Service
    url: https://stability.ai/terms-of-service
  - type: Privacy Policy
    url: https://stability.ai/privacy-policy
  - type: GitHub Org
    url: https://github.com/stability-ai
  - type: JSON-LD
    url: json-ld/stability-ai-context.jsonld
  - type: JSONSchema
    url: json-schema/stability-ai-image-generation-schema.json
  - type: JSONStructure
    url: json-structure/stability-ai-image-generation-structure.json
  - type: Vocabulary
    url: vocabulary/stability-ai-vocabulary.yml
  - type: SpectralRules
    url: rules/stability-ai-rules.yml
  - type: Features
    data:
      - 'API Membership $20/mo: 6,000 credits ($60 worth) included'
      - 1 credit = $0.01
      - 'SD3 (Stable Diffusion 3): ~$0.035 per image (3.5 credits)'
      - 'Stable Image Ultra: $0.08 per image (8 credits, SD3.5 Large)'
      - 'Stable Image Core: lower-cost mid-quality option'
      - Stable Diffusion XL (SDXL)
      - Stable Video Diffusion
      - Stable 3D for 3D model generation
      - Stable Audio for music generation
      - 'Enterprise: volume discounts, self-hosted/private models'
      - REST API at api.stability.ai
      - Default 150 req/10s per key
      - 'Image generation: 10 concurrent jobs'
      - 'Video generation: 5 concurrent jobs'
      - Bearer token (API key) auth
      - Open-weights models (research / community use)
    sources:
      - https://platform.stability.ai/pricing
    updated: '2026-05-04'
---
