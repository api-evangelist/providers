---
aid: autocontent-api
name: AutoContent API
description: AutoContent API is an AI-powered content generation platform that enables developers and content teams to programmatically produce podcasts, explainer videos, video shorts, deep research reports, infographics, and quizzes from diverse input sources including URLs, PDFs, YouTube videos, plain text, and social data feeds. Built on NotebookLM-style AI technology, it provides REST API endpoints with a credit-based pricing model and integrations with Make.com, Zapier, and WordPress.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Audio
  - Content Generation
  - Podcasts
  - Video
  - Generative AI
  - Text to Speech
  - Automation
url: https://raw.githubusercontent.com/api-evangelist/autocontent-api/refs/heads/main/apis.yml
created: '2025-05-02'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: autocontent-api:podcast-generation
    name: Podcast Generation API
    description: Generate AI-powered podcast episodes from URLs, PDFs, YouTube videos, plain text, or social media feeds. Produces MP3 audio with metadata using NotebookLM-style AI with support for standard voices and custom voice cloning. Consumes 10 credits per episode.
    humanURL: https://autocontentapi.com
    baseURL: https://api.autocontentapi.com
    tags:
      - AI
      - Podcast
      - Audio
      - Content Generation
    properties:
      - type: Documentation
        url: https://autocontentapi.com/docs
      - type: Authentication
        url: https://autocontentapi.com/docs
  - aid: autocontent-api:video-generation
    name: Video Generation API
    description: Programmatically produce explainer videos and short-form vertical video content (9:16 format) from text, URLs, and other source content. Explainer videos consume 50 credits; video shorts consume 400 credits. Output is delivered as MP4 video files.
    humanURL: https://autocontentapi.com
    baseURL: https://api.autocontentapi.com
    tags:
      - AI
      - Video
      - Content Generation
    properties:
      - type: Documentation
        url: https://autocontentapi.com/docs
  - aid: autocontent-api:deep-research
    name: Deep Research API
    description: Performs multi-step AI reasoning that browses the live web, reads reputable sources, and synthesizes comprehensive research reports. Supports output as structured JSON, HTML blog posts, and study guides. Consumes 100-200 credits per research session.
    humanURL: https://autocontentapi.com
    baseURL: https://api.autocontentapi.com
    tags:
      - AI
      - Research
      - Content Generation
    properties:
      - type: Documentation
        url: https://autocontentapi.com/docs
  - aid: autocontent-api:infographics-quizzes
    name: Infographics and Quizzes API
    description: Transform source content into visual infographics and interactive quiz formats. Consumes 10-30 credits per asset. Supports diverse input types and produces structured HTML and visual media output.
    humanURL: https://autocontentapi.com
    baseURL: https://api.autocontentapi.com
    tags:
      - AI
      - Infographics
      - Quizzes
      - Content Generation
    properties:
      - type: Documentation
        url: https://autocontentapi.com/docs
common:
  - type: Website
    url: https://autocontentapi.com
  - type: Documentation
    url: https://autocontentapi.com/docs
  - type: SignUp
    url: https://autocontentapi.com
  - type: Pricing
    url: https://autocontentapi.com/pricing
  - type: RateLimits
    data:
      - name: Amateur Plan
        description: 15 assets/day, 1 concurrent request, 1,000 credits/month at €24/month
      - name: Professional Plan
        description: 30 assets/day, 5 concurrent requests, 5,000 credits/month at €58/month
      - name: Business Plan
        description: 60 assets/day, 10 concurrent requests, 10,000 credits/month at €108/month
      - name: High Volume Plan
        description: 90 assets/day, 10 concurrent requests, 20,000 credits/month at €166/month
  - type: Features
    data:
      - name: AI Podcast Generation
        description: Generate audio podcast episodes from URLs, PDFs, YouTube videos, plain text, and social feeds using NotebookLM-style AI with natural-sounding voices.
      - name: Video Content Production
        description: Programmatically produce explainer videos and short-form vertical video content suitable for social media platforms.
      - name: Deep Research Synthesis
        description: Multi-step AI reasoning that browses the live web and synthesizes comprehensive research reports from reputable sources.
      - name: Infographic Generation
        description: Transform text and data sources into visual infographic formats for presentations, reports, and marketing materials.
      - name: Quiz Creation
        description: Automatically generate interactive quizzes from educational content, PDFs, and URLs for e-learning and assessment purposes.
      - name: Voice Cloning
        description: Create custom voice replicas for personalized podcast and audio content generation that matches a specific speaker's voice profile.
      - name: Multi-Source Input
        description: Accept diverse input formats including URLs, PDF files, YouTube videos, plain text, X/Twitter streams, and Reddit data feeds.
      - name: Credit-Based Pricing
        description: Flexible credit-based consumption model where different content types consume different credit amounts based on complexity and output quality.
  - type: UseCases
    data:
      - name: Content Creator Automation
        description: Content creators and media teams automating production of podcast episodes, videos, and written content from research materials at scale.
      - name: Educational Content Production
        description: Educators and e-learning platforms generating AI-powered audio lessons, explainer videos, and interactive quizzes from course materials.
      - name: Marketing Content at Scale
        description: Marketing teams programmatically producing diverse content formats from campaign briefs, product data, and market research for multi-channel distribution.
      - name: News and Research Automation
        description: Media organizations and research firms automating synthesis of news coverage, competitive intelligence, and industry reports.
      - name: Developer Integration
        description: Developers embedding AI content generation capabilities into applications, CMS platforms, and automated publishing workflows via REST API.
  - type: Integrations
    data:
      - name: Make.com
        description: Native Make.com (formerly Integromat) integration for no-code workflow automation connecting AutoContent API with hundreds of other services.
      - name: Zapier
        description: Zapier integration enabling automated content generation workflows triggered by events in thousands of connected applications.
      - name: WordPress
        description: WordPress plugin or REST API integration for automatically publishing AI-generated content directly to WordPress sites.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
