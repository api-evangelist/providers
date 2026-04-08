---
aid: stability-ai
url: https://raw.githubusercontent.com/api-evangelist/stability-ai/refs/heads/main/apis.yml
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
  properties:
  - url: https://platform.stability.ai/docs/api-reference
    type: Documentation
  - url: openapi/stability-ai-stable-image-generate-openapi.yml
    type: OpenAPI
  description: The Stability AI Stable Image Generate API provides text-to-image generation capabilities powered by models including Stable Diffusion 3 and Stable Image Ultra. Developers can generate high-quality images from text prompts with control over style, dimensions, and output format. The API supports multiple model tiers including Stable Image Core for fast and affordable generation and Stable Image Ultra for state-of-the-art quality results.
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
  properties:
  - url: https://platform.stability.ai/docs/api-reference
    type: Documentation
  - url: openapi/stability-ai-stable-image-edit-openapi.yml
    type: OpenAPI
  description: The Stability AI Stable Image Edit API provides image editing capabilities including inpainting, outpainting, object erasing, background removal, and search-and-replace functionality. Developers can use natural language prompts to modify existing images, fill in masked regions, extend image boundaries, or replace specific objects within a scene. These tools enable advanced image manipulation workflows without requiring traditional image editing expertise.
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
  properties:
  - url: https://platform.stability.ai/docs/api-reference
    type: Documentation
  - url: openapi/stability-ai-stable-image-upscale-openapi.yml
    type: OpenAPI
  description: The Stability AI Stable Image Upscale API enables developers to increase the resolution of images using AI-powered upscaling models. The API offers both conservative upscaling, which preserves the original image closely while increasing resolution, and creative upscaling, which enhances and adds detail to images during the upscaling process. These endpoints are useful for improving image quality for print, display, or further processing workflows.
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
  properties:
  - url: https://platform.stability.ai/docs/api-reference
    type: Documentation
  - url: openapi/stability-ai-stable-image-control-openapi.yml
    type: OpenAPI
  description: The Stability AI Stable Image Control API provides image-to-image generation guided by structural inputs such as sketches and reference structures. Using ControlNet-based models, developers can generate new images that follow the composition, edges, or layout of a source image while applying new styles or content based on text prompts. The API supports sketch-to-image and structure-guided generation workflows for precise creative control.
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
  properties:
  - url: https://platform.stability.ai/docs/getting-started/stable-video-diffusion
    type: Documentation
  - url: openapi/stability-ai-stable-video-diffusion-openapi.yml
    type: OpenAPI
  description: The Stability AI Stable Video Diffusion API enables developers to generate short video clips from a single input image. Powered by the Stable Video Diffusion model, the API produces smooth animated sequences that bring static images to life with realistic motion. This is useful for creating product animations, visual effects previews, and dynamic content from existing image assets.
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
  properties:
  - url: https://platform.stability.ai/docs/api-reference
    type: Documentation
  - url: openapi/stability-ai-stable-fast-3d-openapi.yml
    type: OpenAPI
  description: The Stability AI Stable Fast 3D API generates textured 3D mesh assets from single input images. The API rapidly produces 3D models suitable for use in games, augmented reality, virtual reality, and product visualization workflows. Developers can convert 2D images into fully textured 3D objects, enabling rapid prototyping and asset creation without manual 3D modeling.
name: Stability Ai
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Stability AI is an AI company that develops open-source generative AI models for image, audio, video, and language, including the Stable Diffusion family of image generation models.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

