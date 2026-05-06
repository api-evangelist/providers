---
aid: gemini
name: Gemini
description: Google's Gemini API provides access to state-of-the-art generative AI models for text generation, multimodal understanding, code generation, and more.
type: Index
image: https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg
url: https://raw.githubusercontent.com/api-evangelist/gemini/refs/heads/main/apis.yml
access: 3rd-Party
specificationVersion: '0.19'
tags:
  - Agents
  - Artificial Intelligence
  - Audio Understanding
  - Batch Processing
  - Deep Research
  - Document Understanding
  - Embeddings
  - Function Calling
  - Generative Ai
  - Image Generation
  - Large Language Models
  - Machine Learning
  - Multimodal
  - Structured Output
  - Text-To-Speech
  - Video Generation
  - Video Understanding
created: '2024'
modified: '2026-04-18'
apis:
  - name: Gemini REST API
    description: REST API for accessing Gemini models for text generation, chat, embeddings, and multimodal tasks.
    image: https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg
    humanURL: https://ai.google.dev/api
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Chat
      - Embeddings
      - Generative Ai
      - Multimodal
      - Rest
      - Streaming
      - Text Generation
    properties:
      - type: Documentation
        url: https://ai.google.dev/api/rest
      - type: OpenAPI
        url: https://generativelanguage.googleapis.com/$discovery/rest?version=v1beta&key=YOUR_API_KEY
      - type: Authentication
        url: https://ai.google.dev/gemini-api/docs/api-key
      - type: API Reference
        url: https://ai.google.dev/api/all-methods
      - type: Function Calling
        url: https://ai.google.dev/gemini-api/docs/function-calling
      - type: Code Execution
        url: https://ai.google.dev/gemini-api/docs/code-execution
      - type: Grounding
        url: https://ai.google.dev/gemini-api/docs/google-search
      - type: Safety
        url: https://ai.google.dev/gemini-api/docs/safety-settings
      - type: Context Caching
        url: https://ai.google.dev/gemini-api/docs/caching
      - type: Tuning
        url: https://ai.google.dev/api/tuning
      - type: Tools
        url: https://ai.google.dev/gemini-api/docs/tools
      - type: Structured Output
        url: https://ai.google.dev/gemini-api/docs/structured-output
      - type: Thinking
        url: https://ai.google.dev/gemini-api/docs/thinking
      - type: System Instructions
        url: https://ai.google.dev/gemini-api/docs/system-instructions
      - type: Prompting Strategies
        url: https://ai.google.dev/gemini-api/docs/prompting-strategies
      - type: OpenAI Compatibility
        url: https://ai.google.dev/gemini-api/docs/openai
    contact:
      - FN: Google AI Support
        url: https://ai.google.dev/support
  - name: Gemini Python SDK
    description: Python client library for the Gemini API.
    humanURL: https://ai.google.dev/api/python
    baseURL: https://pypi.org/project/google-generativeai/
    tags:
      - Client Library
      - Python
      - Sdk
    properties:
      - type: Documentation
        url: https://ai.google.dev/api/python/google/generativeai
      - type: GitHub
        url: https://github.com/google/generative-ai-python
      - type: Installation
        url: https://pypi.org/project/google-generativeai/
      - type: GitHub
        url: https://github.com/googleapis/python-genai
      - type: Installation
        url: https://pypi.org/project/google-genai/
  - name: Gemini Node.js SDK
    description: Node.js client library for the Gemini API.
    humanURL: https://ai.google.dev/api/node
    baseURL: https://www.npmjs.com/package/@google/generative-ai
    tags:
      - Client Library
      - Javascript
      - Nodejs
      - Sdk
      - Typescript
    properties:
      - type: Documentation
        url: https://ai.google.dev/api/node
      - type: GitHub
        url: https://github.com/google/generative-ai-js
      - type: Installation
        url: https://www.npmjs.com/package/@google/generative-ai
      - type: GitHub
        url: https://github.com/googleapis/js-genai
      - type: Installation
        url: https://www.npmjs.com/package/@google/genai
  - name: Gemini Go SDK
    description: Go client library for the Gemini API, providing an interface for developers to integrate Google generative models into Go applications.
    humanURL: https://ai.google.dev/gemini-api/docs/libraries
    baseURL: https://pkg.go.dev/google.golang.org/genai
    tags:
      - Client Library
      - Go
      - Golang
      - Sdk
    properties:
      - type: Documentation
        url: https://pkg.go.dev/google.golang.org/genai
      - type: GitHub
        url: https://github.com/googleapis/go-genai
      - type: Installation
        url: https://pkg.go.dev/google.golang.org/genai
  - name: Gemini Java SDK
    description: Java client library for the Gemini API, providing an interface for developers to integrate Google generative models into Java applications.
    humanURL: https://ai.google.dev/gemini-api/docs/libraries
    baseURL: https://central.sonatype.com/artifact/com.google.genai/google-genai
    tags:
      - Client Library
      - Java
      - Sdk
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/libraries
      - type: GitHub
        url: https://github.com/googleapis/java-genai
      - type: Installation
        url: https://central.sonatype.com/artifact/com.google.genai/google-genai
  - name: Gemini C# SDK
    description: C# client library for the Gemini API, providing an interface for developers to integrate Google generative models into .NET applications.
    humanURL: https://ai.google.dev/gemini-api/docs/libraries
    baseURL: https://www.nuget.org/packages/Google.GenAI
    tags:
      - Client Library
      - Csharp
      - Dotnet
      - Sdk
    properties:
      - type: Documentation
        url: https://googleapis.github.io/dotnet-genai/
      - type: GitHub
        url: https://github.com/googleapis/dotnet-genai
      - type: Installation
        url: https://www.nuget.org/packages/Google.GenAI
  - name: Gemini Live API
    description: Low-latency bidirectional streaming API enabling real-time voice and video interactions with Gemini models over WebSocket connections.
    humanURL: https://ai.google.dev/gemini-api/docs/live
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Live
      - Real-Time
      - Streaming
      - Video
      - Voice
      - Websocket
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/live
      - type: Capabilities Guide
        url: https://ai.google.dev/gemini-api/docs/live-guide
      - type: Tools
        url: https://ai.google.dev/gemini-api/docs/live-tools
  - name: Gemini Interactions API
    description: Unified interface for interacting with Gemini models and agents, simplifying state management, tool orchestration, and long-running tasks as an improved alternative to generateContent.
    humanURL: https://ai.google.dev/gemini-api/docs/interactions
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Agents
      - Interactions
      - State Management
      - Tool Orchestration
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/interactions
  - name: Gemini Image Generation API
    description: Image generation capabilities through the Gemini API, supporting text-to-image generation, image editing, and multi-turn conversational editing.
    humanURL: https://ai.google.dev/gemini-api/docs/image-generation
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Generative Ai
      - Image Editing
      - Image Generation
      - Text-To-Image
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/image-generation
  - name: Gemini Video Generation API
    description: Video generation capabilities through the Gemini API powered by Veo, supporting text-to-video and image-to-video generation in resolutions up to 4K.
    humanURL: https://ai.google.dev/gemini-api/docs/video
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Generative Ai
      - Image-To-Video
      - Text-To-Video
      - Veo
      - Video Generation
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/video
  - name: Gemini Text-to-Speech API
    description: Native audio generation text-to-speech capabilities through the Gemini API, supporting single and multi-speaker speech synthesis with natural language control over style, accent, pace, and tone.
    humanURL: https://ai.google.dev/gemini-api/docs/speech-generation
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Audio Generation
      - Multi-Speaker
      - Speech Synthesis
      - Text-To-Speech
      - Tts
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/speech-generation
  - name: Gemini Files API
    description: API for uploading and managing media files for use with Gemini models, supporting images, audio, video, and documents up to 2 GB per file with 20 GB per project storage.
    humanURL: https://ai.google.dev/gemini-api/docs/files
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Documents
      - Files
      - Media
      - Storage
      - Upload
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/files
      - type: API Reference
        url: https://ai.google.dev/api/files
      - type: File Input Methods
        url: https://ai.google.dev/gemini-api/docs/file-input-methods
  - name: Gemini Embeddings API
    description: Text embedding capabilities through the Gemini API, generating vector representations for semantic search, classification, clustering, and retrieval augmented generation (RAG) applications.
    humanURL: https://ai.google.dev/gemini-api/docs/embeddings
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Embeddings
      - Rag
      - Semantic Search
      - Text Embeddings
      - Vector Search
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/embeddings
      - type: Model Card
        url: https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001
  - name: Gemini Batch API
    description: Asynchronous batch processing API for submitting large volumes of Gemini API requests at 50 percent of the standard cost, with support for content generation, embeddings, and OpenAI compatibility.
    humanURL: https://ai.google.dev/gemini-api/docs/batch-api
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Asynchronous
      - Batch
      - Bulk Processing
      - Cost Optimization
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/batch-api
  - name: Gemini Deep Research API
    description: Agentic research capability powered by the Interactions API that autonomously plans, executes, and synthesizes multi-step research tasks using web search and URL context to produce detailed cited reports.
    humanURL: https://ai.google.dev/gemini-api/docs/deep-research
    baseURL: https://generativelanguage.googleapis.com
    tags:
      - Agents
      - Deep Research
      - Reports
      - Research
      - Web Search
    properties:
      - type: Documentation
        url: https://ai.google.dev/gemini-api/docs/deep-research
common:
  - type: GettingStarted
    url: https://ai.google.dev/gemini-api/docs/quickstart
  - type: Authentication
    url: https://aistudio.google.com/app/apikey
  - type: Pricing
    url: https://ai.google.dev/pricing
  - type: Models
    url: https://ai.google.dev/gemini-api/docs/models
  - type: RateLimits
    url: https://ai.google.dev/gemini-api/docs/quota
  - type: TermsOfService
    url: https://ai.google.dev/terms
  - type: PrivacyPolicy
    url: https://policies.google.com/privacy
  - type: Blog
    url: https://developers.googleblog.com/
  - type: Support
    url: https://discuss.ai.google.dev/
  - type: SDK
    url: https://ai.google.dev/gemini-api/docs/libraries
  - type: ChangeLog
    url: https://ai.google.dev/gemini-api/docs/changelog
  - type: StatusPage
    url: https://aistudio.google.com/status
  - type: GitHubRepository
    url: https://github.com/google-gemini/cookbook
  - type: Console
    url: https://aistudio.google.com/
  - type: Features
    data:
      - name: Multimodal Understanding
        description: Process and understand text, images, audio, video, and documents in a single model.
      - name: Function Calling
        description: Define custom functions that Gemini can invoke to interact with external systems and APIs.
      - name: Structured Output
        description: Generate JSON responses conforming to specified schemas for reliable data extraction.
      - name: Context Caching
        description: Cache large context windows to reduce latency and cost for repeated queries.
      - name: Code Execution
        description: Execute Python code in a sandboxed environment for computational tasks.
      - name: Grounding with Google Search
        description: Ground model responses with real-time Google Search results for factual accuracy.
      - name: Live Streaming API
        description: Real-time bidirectional voice and video interactions over WebSocket connections.
      - name: Image and Video Generation
        description: Generate images and videos from text prompts using Gemini and Veo models.
      - name: Text-to-Speech
        description: Native audio generation with multi-speaker support and natural language style control.
      - name: Deep Research
        description: Autonomous multi-step research agent that synthesizes cited reports from web sources.
      - name: Thinking Mode
        description: Extended reasoning capability for complex problem-solving and analysis tasks.
  - type: UseCases
    data:
      - name: AI-Powered Chatbots
        description: Build conversational AI assistants with multimodal understanding and function calling.
      - name: Document Processing
        description: Extract structured data from documents, PDFs, and images using vision capabilities.
      - name: Content Generation
        description: Generate text, images, and video content with AI for marketing and creative workflows.
      - name: Code Generation
        description: Generate, explain, and debug code across multiple programming languages.
      - name: Semantic Search
        description: Build search systems using Gemini embeddings for semantic similarity matching.
      - name: Real-Time Translation
        description: Translate text and audio in real-time using multimodal capabilities.
  - type: Integrations
    data:
      - name: Google Cloud Vertex AI
        description: Access Gemini models through Vertex AI for enterprise-grade deployment and management.
      - name: Google AI Studio
        description: Prototype and test Gemini API calls with the web-based development environment.
      - name: LangChain
        description: Use Gemini as a provider in LangChain for building AI application pipelines.
      - name: Firebase
        description: Integrate Gemini with Firebase for mobile and web app AI features.
      - name: OpenAI Compatibility
        description: Use Gemini through OpenAI-compatible API endpoints for easy migration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
