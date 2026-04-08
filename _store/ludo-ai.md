---
aid: ludo-ai
url: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/apis.yml
apis:
- aid: ludo-ai:rest-api
  name: Ludo.ai REST API
  tags:
  - 3D Models
  - Animation
  - Asset Generation
  - Audio
  - Game Development
  - Images
  - Sprites
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.ludo.ai/api/
  humanURL: https://ludo.ai/api-mcp-integration
  properties:
  - url: https://ludo.ai/api-mcp-integration
    type: Documentation
  - url: openapi/ludo-ai-rest-api-openapi.yml
    type: OpenAPI
  description: The Ludo.ai REST API provides programmatic access to the full suite of AI-powered game asset generation capabilities. Developers can generate sprites, icons, UI assets, textures, and backgrounds through image generation endpoints, convert 2D images to 3D GLB models with PBR textures, create animated spritesheets from static images, and produce sound effects, music tracks, and character voices.
- aid: ludo-ai:mcp-server
  name: Ludo.ai MCP Server
  tags:
  - AI Assistants
  - Asset Generation
  - Game Development
  - Model Context Protocol
  - Vibe Coding
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://mcp.ludo.ai/mcp
  humanURL: https://ludo.ai/docs/api-mcp
  properties:
  - url: https://ludo.ai/docs/api-mcp
    type: Documentation
  - url: https://github.com/Ludo-AI/ludo-mcp
    type: GitHubRepository
  description: The Ludo.ai MCP Server exposes the platform's asset generation tools via the Model Context Protocol, allowing AI assistants like Claude and Cursor to generate game assets through natural language conversations. The server provides over 20 tools including createImage, editImage, animateSprite, create3DModel, createSoundEffect, createMusic, createVoice, and createVideo.
- aid: ludo-ai:unity-plugin
  name: Ludo.ai Unity Plugin
  tags:
  - Asset Generation
  - Game Development
  - Plugin
  - Unity
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://github.com/Ludo-AI/ludo-unity-plugin
  properties:
  - url: https://github.com/Ludo-AI/ludo-unity-plugin
    type: Documentation
  description: The Ludo.ai Unity Plugin integrates AI-powered asset generation directly into the Unity game engine. It provides a native interface for Unity developers to access Ludo.ai's image generation, 3D model creation, audio production, and animation tools without leaving the editor. The plugin connects to the Ludo.ai API to deliver generated assets directly into Unity projects, streamlining the game development workflow.
name: Ludo.ai
tags:
- Artificial Intelligence
- Asset Generation
- Game Design
- Game Development
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Ludo.ai is a game design hub that uses artificial intelligence to help developers generate production-ready game assets including images, 3D models, audio, and animations. The platform entered beta for its Model Context Protocol (MCP) integration, exposing its asset generation suite as a headless API that enables vibe coding where developers can trigger asset creation directly from AI assistants like Claude or Cursor.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

