---
aid: codeproject
url: https://raw.githubusercontent.com/api-evangelist/codeproject/refs/heads/main/apis.yml
name: CodeProject
tags:
  - AI
  - Articles
  - Community
  - Computer Vision
  - Developer Community
  - Face Recognition
  - Forum
  - Knowledge Base
  - License Plate Recognition
  - Object Detection
  - Q&A
  - Software Development
  - Tutorials
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2025-01-01'
modified: '2026-04-26'
position: Consumer
description: CodeProject is a long-running online community for software developers founded in 1999, hosting hundreds of thousands of developer-contributed articles, tutorials, code samples, tips, and a Q&A forum across a broad range of programming topics. It exposes a public REST API at api.codeproject.com (V1 Beta) for read access to articles, forum messages, questions, and authenticated user data, secured by OAuth 2.0 Bearer Tokens. CodeProject also operates CodeProject.AI Server, a free, open-source, self-hosted AI service that exposes object detection, face recognition, license-plate reading (ALPR), scene classification, image processing, audio classification, text analytics, and YOLOv5 training through a local HTTP REST API. CodeProject.AI is widely integrated with home-automation and surveillance platforms (Blue Iris, Home Assistant, Agent DVR).
apis:
  - aid: codeproject:codeproject-api
    name: CodeProject REST API
    tags:
      - Articles
      - Community
      - Forum
      - OAuth2
      - Q&A
      - Read-Only
    type: REST
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.codeproject.com
    humanURL: https://api.codeproject.com/Help
    description: OAuth 2.0 protected REST API providing read access to CodeProject articles, forum messages, questions, and authenticated user data (answers, articles, blog posts, bookmarks, notifications, profile, reputation, tips). Supports Client Credentials, Authorization Code, and Implicit Grant flows. Tokens are issued by the CodeProject identity server and presented as Bearer tokens in the Authorization header.
    properties:
      - url: https://api.codeproject.com/Help
        name: API Documentation
        type: Documentation
      - url: https://api.codeproject.com/
        name: API Base URL
        type: BaseURL
      - url: https://api.codeproject.com/Samples
        name: API Samples
        type: Samples
      - url: https://www.codeproject.com/Articles/986918/The-CodeProject-API-Part
        name: The CodeProject API - Part 1
        type: Article
      - url: https://www.codeproject.com/articles/989081/the-code-project-api-part-getting-some-rest
        name: The CodeProject API - Part 2 Getting Some REST
        type: Article
      - url: openapi/codeproject-rest-api-openapi.yml
        type: OpenAPI
    x-features:
      - OAuth 2.0 Bearer Token authentication
      - Client Credentials, Authorization Code, and Implicit Grant flows
      - Read-only access to articles, forums, and Q&A
      - My endpoints for authenticated user data
      - Article rating filter (>= 3.0) on the public list
    x-use-cases:
      - Aggregating CodeProject articles into developer reading lists
      - Surfacing CodeProject Q&A in IDE assistants
      - Building user dashboards showing reputation and notifications
      - Periodic content sync into knowledge bases
  - aid: codeproject:codeproject-ai-server
    name: CodeProject.AI Server API
    tags:
      - AI
      - Audio
      - Computer Vision
      - Face Recognition
      - Image Processing
      - License Plate Recognition
      - Object Detection
      - On-Premise
      - Self-Hosted
      - Text
      - Training
    type: REST
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: http://localhost:32168
    humanURL: https://www.codeproject.com/AI/
    description: Self-hosted AI service that exposes computer vision (object detection, scene, face, ALPR), image processing (background removal, cartoonise, portrait filter, super-resolution), audio classification, NLP (sentiment, summarization), and YOLOv5 training endpoints through a local HTTP REST API. All endpoints are POST and accept multipart uploads. The server runs on Windows, macOS, Linux, Raspberry Pi, Jetson, and OrangePi, plus Docker images, and integrates with Blue Iris, Home Assistant, and Agent DVR for surveillance use cases.
    properties:
      - url: https://www.codeproject.com/AI/
        name: CodeProject.AI Server Home
        type: Portal
      - url: https://codeproject.github.io/codeproject.ai/
        name: Documentation
        type: Documentation
      - url: https://codeproject.github.io/codeproject.ai/api/api_reference.html
        name: API Reference
        type: APIReference
      - url: https://github.com/codeproject/CodeProject.AI-Server
        name: GitHub Repository
        type: SourceCode
      - url: openapi/codeproject-ai-server-openapi.yml
        type: OpenAPI
    x-features:
      - Local-only HTTP REST API (no internet dependency)
      - YOLO-based object detection (80+ classes)
      - Custom YOLOv5 model loading and training
      - Face detection, registration, recognition, and matching
      - Automatic License Plate Recognition (ALPR)
      - Image background removal, cartoonise, portrait, super-resolution
      - Sound classification and NLP (sentiment, summarization)
      - Modular installer-based feature set
      - Cross-platform (Windows, macOS, Linux, Pi, Jetson, OrangePi, Docker)
    x-use-cases:
      - On-premise CCTV/NVR object and person detection
      - License plate capture for parking and security
      - Privacy-preserving face recognition for home automation
      - Edge AI on Raspberry Pi and Jetson devices
      - Local image moderation and content classification
common:
  - url: https://www.codeproject.com/
    name: CodeProject Website
    type: Website
  - url: https://api.codeproject.com/Help
    name: API Documentation
    type: Documentation
  - url: https://api.codeproject.com/Samples
    name: API Samples
    type: Samples
  - url: https://www.codeproject.com/Terms
    name: Terms of Service
    type: TermsOfService
  - url: https://www.codeproject.com/privacy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://www.codeproject.com/Lounge.aspx
    name: Community Forum
    type: Forum
  - url: https://www.codeproject.com/KB/
    name: Articles and Tutorials
    type: Tutorials
  - url: https://www.codeproject.com/Questions/
    name: Q&A
    type: Support
  - url: https://www.codeproject.com/newsletters
    name: Newsletter
    type: Newsletter
  - url: https://codeproject.ai/
    name: CodeProject.AI
    type: Portal
  - url: https://github.com/codeproject
    name: GitHub Organization
    type: GitHub
  - url: json-ld/codeproject-context.jsonld
    type: JSON-LD
  - url: rules/codeproject-rules.yml
    type: Spectral
  - url: capabilities/codeproject-capabilities.yml
    type: NaftikoCapabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
