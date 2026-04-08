---
aid: midjourney
url: https://raw.githubusercontent.com/api-evangelist/midjourney/refs/heads/main/apis.yml
apis:
- aid: midjourney:image-generation-api
  name: Midjourney Image Generation API
  tags:
  - AI
  - Creative Tools
  - Generative AI
  - Image Generation
  - Text to Image
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.midjourney.com
  humanURL: https://docs.midjourney.com/
  properties:
  - url: https://docs.midjourney.com/
    type: Documentation
  - url: openapi/midjourney-image-generation-openapi.yml
    type: OpenAPI
  - url: asyncapi/midjourney-image-generation-asyncapi.yml
    type: AsyncAPI
  - url: json-schema/midjourney-image-generation-job-schema.json
    type: JSONSchema
  description: The Midjourney Image Generation API provides programmatic access to Midjourney's AI-powered image generation capabilities. Developers can submit text prompts to generate images, upscale selected outputs to higher resolutions, create variations of generated images, and use describe functionality to generate prompts from existing images.
- aid: midjourney:web-application
  name: Midjourney Web Application
  tags:
  - AI
  - Creative Tools
  - Image Generation
  - User Interface
  - Web Application
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://www.midjourney.com/
  properties:
  - url: https://docs.midjourney.com/
    type: Documentation
  description: The Midjourney Web Application provides a browser-based interface for generating AI images using text prompts. Users can create images, explore a gallery of community creations, manage their generated image library, and access advanced features such as image editing, blending, and variation generation. The web application serves as the primary interface for interacting with Midjourney's generative AI models, complementing the original Discord-based experience with a dedicated creative workspace.
- aid: midjourney:discord-bot
  name: Midjourney Discord Bot
  tags:
  - AI
  - Bot
  - Chat Interface
  - Discord
  - Image Generation
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.midjourney.com/hc/en-us
  properties:
  - url: https://docs.midjourney.com/hc/en-us
    type: Documentation
  description: The Midjourney Discord Bot is the original interface for accessing Midjourney's AI image generation service. Users interact with the bot through Discord slash commands such as /imagine, /blend, /describe, and /shorten to generate and manipulate AI-created images. The bot supports features including text-to-image generation, image upscaling, variation creation, and image blending, all within the Discord messaging platform.
name: Midjourney
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Midjourney is an independent research lab that produces an artificial intelligence program creating images from textual descriptions, accessible primarily through a Discord bot interface.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

