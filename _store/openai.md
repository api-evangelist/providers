---
aid: openai
url: https://raw.githubusercontent.com/api-search/ai/main/_apis/openai/apis.md
apis:
  - aid: openai:openai-assistants-api
    name: OpenAI Assistants API
    tags:
      - Assistants
    score: 1329
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/assistants/overview
    overlays:
      - url: >-

          overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/assistants-openapi-search.yml
        type: APIs.io Search
      - url: overlays/assistants-openapi-search.yml
        type: APIs.io Search
      - url: overlays/assistants-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://platform.openai.com/docs/assistants/overview
        type: Documentation
      - url: openapi/assistants-openapi-original.yml
        type: OpenAPI
    description: |-
      The Assistants API allows you to build AI assistants within your own
      applications. An Assistant has instructions and can leverage models,
      tools, and knowledge to respond to user queries. The Assistants API
      currently supports three types of tools - Code Interpreter, Retrieval, and
      Function calling. In the future, we plan to release more OpenAI-built
      tools, and allow you to provide your own tools on our platform.
  - aid: openai:openai-audio-api
    name: OpenAI Audio API
    tags:
      - Audio
    score: 128
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/guides/text-to-speech
    overlays:
      - url: >-

          overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/audio-openapi-search.yml
        type: APIs.io Search
      - url: overlays/audio-openapi-search.yml
        type: APIs.io Search
      - url: overlays/audio-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://platform.openai.com/docs/guides/text-to-speech
        type: Documentation
      - url: openapi/audio-openapi-original.yml
        type: OpenAPI
    description: |-

      The Audio API provides two speech to text endpoints, transcriptions and
      translations, based on our state-of-the-art open source large-v2 Whisper
      model.
  - aid: openai:openai-chat-api
    name: OpenAI Chat API
    tags:
      - Chat
    score: 149
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/chat
    overlays:
      - url: >-

          overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/chat-openapi-search.yml
        type: APIs.io Search
      - url: overlays/chat-openapi-search.yml
        type: APIs.io Search
      - url: overlays/chat-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://platform.openai.com/docs/api-reference/chat
        type: Documentation
      - url: openapi/chat-openapi-original.yml
        type: OpenAPI
    description: |-

      Given a list of messages comprising a conversation, the model will return
      a response., providing an AI chat interface you can use to engage with
      users.
  - aid: openai:openai-chat-completions-api
    name: OpenAI Chat Completions API
    tags:
      - Chat
      - Completions
    score: 281
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/chat
    overlays:
      - url: >-
          overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/completions-openapi-search.yml
        type: APIs.io Search
      - url: overlays/completions-openapi-search.yml
        type: APIs.io Search
      - url: overlays/completions-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://platform.openai.com/docs/api-reference/chat
        type: Documentation
      - url: openapi/completions-openapi-original.yml
        type: OpenAPI
    description: |-

      Chat models take a list of messages as input and return a model-generated
      message as output. Although the chat format is designed to make multi-turn
      conversations easy, it's just as useful for single-turn tasks without any
      conversation.
  - aid: openai:openai-embeddings-api
    name: OpenAI Embeddings API
    tags:
      - Embedding
      - Embeddings
      - Inputs
      - Representing
      - Text
      - Vectors
    score: 112
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/guides/embeddings
    overlays:
      - url: >-

          overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/embeddings-openapi-search.yml
        type: APIs.io Search
      - url: overlays/embeddings-openapi-search.yml
        type: APIs.io Search
      - url: overlays/embeddings-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://platform.openai.com/docs/guides/embeddings
        type: Documentation
      - url: openapi/embeddings-openapi-original.yml
        type: OpenAPI
    description: |-

      Learn how to turn text into numbers, unlocking use cases like search.
      OpenAI's text embeddings measure the relatedness of text strings.
  - aid: openai:openai-files-api
    name: OpenAI Files API
    tags:
      - Files
      - Artificial Intelligence
      - AI
    score: 894
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/files
    overlays:
      - url: overlays/files-openapi-search.yml
        type: APIs.io Search
      - url: overlays/files-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://platform.openai.com/docs/api-reference/files
        type: Documentation
      - url: openapi/files-openapi-original.yml
        type: OpenAPI
    description: |-

      Files are used to upload documents that can be used with features like
      Assistants and Fine-tuning. Upload a file that can be used across various
      endpoints. The size of all the files uploaded by one organization can be
      up to 100 GB.
  - aid: openai:openai-fine-tuning-api
    name: OpenAI Fine Tuning API
    tags:
      - About
      - Begins
      - Cancel
      - Creates
      - Creating
      - Dataset Response
      - Details
      - Enqueued
      - Events
      - Fine
      - Fine Tune
      - Fine Tuned
      - Fine Tuning
      - Given
      - Immediately
      - Includes
      - Including
      - Info
      - Jobs
      - Models
      - More
      - Names
      - Organization's
      - Process
      - Status
      - The
      - Tuning
      - Your
    score: 492
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/guides/fine-tuning
    overlays:
      - url: overlays/fint-tuning-openapi-search.yml
        type: APIs.io Search
      - url: overlays/fine-tuning-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
      - url: overlays/fine-tuning-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://platform.openai.com/docs/guides/fine-tuning
        type: Documentation
      - url: openapi/fine-tuning-openapi-original.yml
        type: OpenAPI
    description: |-

      Manage fine-tuning jobs to tailor a model to your specific training data.
      Creates a fine-tuning job which begins the process of creating a new model
      from a given dataset.Response includes details of the enqueued job
      including job status and the name of the fine-tuned models once complete.
  - aid: openai:openai-images-api
    name: OpenAI Images API
    tags:
      - Creates
      - Edited
      - Edits
      - Extended
      - Generations
      - Given
      - Images
      - Original
      - Prompts
      - Variations
    score: 120
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/guides/images
    overlays:
      - url: overlays/images-openapi-search.yml
        type: APIs.io Search
      - url: overlays/images-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://platform.openai.com/docs/guides/images
        type: Documentation
      - url: openapi/images-openapi-original.yml
        type: OpenAPI
    description: |-

      Learn how to generate or manipulate images with DALL_E in the API. The
      Images API provides three methods for interacting with images - creating
      images from scratch based on a text prompt, creating edited versions of
      images by having the model replace some areas of a pre-existing image,
      based on a new text prompt, Creating variations of an existing image.
  - aid: openai:openai-models-api
    name: OpenAI Models API
    tags:
      - About
      - Availability
      - Available
      - Basic
      - Currently
      - Fine Tuned
      - Information
      - Instances
      - Models
      - Organizations
      - Owners
      - Permissioning
      - Provides
      - Providing
      - Roles
    score: 201
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/models
    overlays:
      - url: overlays/models-openapi-search.yml
        type: APIs.io Search
      - url: overlays/models-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://platform.openai.com/docs/models
        type: Documentation
      - url: openapi/models-openapi-original.yml
        type: OpenAPI
    description: |-

      List and describe the various models available in the API. You can refer
      to the Models documentation to understand what models are available and
      the differences between them.
  - aid: openai:openai-threads-api
    name: OpenAI Threads API
    tags:
      - Belonging
      - Calls
      - Cancel
      - Cancels
      - Completed
      - Endpoints
      - File
      - Files
      - Given
      - Is
      - Messages
      - Modifies
      - One
      - Outputs
      - Returns
      - Runs
      - Single
      - Steps
      - Submit
      - Submitted
      - The
      - They're
      - Threads
      - Tool
    score: 1861
    baseURL: https://api.openai.com
    humanURL: >-

      https://platform.openai.com/docs/assistants/how-it-works/managing-threads-and-messages
    overlays:
      - url: overlays/threads-openapi-search.yml
        type: APIs.io Search
      - url: overlays/threads-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://platform.openai.com/docs/assistants/how-it-works/managing-threads-and-messages
        type: Documentation
      - url: openapi/threads-openapi-original.yml
        type: OpenAPI
    description: Create threads that assistants can interact with.
name: OpenAI
tags:
  - Artificial Intelligence
  - AI
  - Large Language Models
type: Contract
score: 308
access: 3rd-Party
common:
  - url: https://platform.openai.com/docs/overview
    name: Overview - OpenAI API
    type: Portal
    description: 'null'
  - url: https://platform.openai.com/docs/quickstart
    name: Developer quickstart - OpenAI API
    type: GettingStarted
    description: 'null'
  - url: https://platform.openai.com/docs/libraries
    name: Libraries - OpenAI API
    type: SDKs
    description: 'null'
  - url: https://community.openai.com/categories
    name: Categories - OpenAI Developer Community
    type: Forums
    description: 'null'
  - url: https://platform.openai.com/docs/guides/rate-limits
    name: Rate limits - OpenAI API
    type: RateLimits
    description: 'null'
  - url: https://platform.openai.com/docs/deprecations
    name: Deprecations - OpenAI API
    type: Deprecations
    description: 'null'
  - url: https://openai.com/policies/
    name: Terms & policies | OpenAI
    type: TermsOfService
    description: 'null'
  - url: https://openai.com/policies/terms-of-use/
    name: Terms of use | OpenAI
    type: TermsOfService
    description: 'null'
  - url: https://openai.com/policies/privacy-policy/
    name: Privacy policy | OpenAI
    type: PrivacyPolicy
    description: 'null'
  - url: https://platform.openai.com/docs/overview
    name: Overview - OpenAI API
    type: Documentation
    description: 'null'
  - url: https://help.openai.com/en
    name: OpenAI Help Center
    type: Support
    description: 'null'
  - url: https://status.openai.com/
    name: OpenAI Status
    type: Status
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/authentication
    name: API Reference - OpenAI API
    type: Authentication
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/webhook_events/response
    name: API Reference - OpenAI API
    type: Webhooks
    description: 'null'
  - url: properties/openai-openapi
    name: OpenAPI
    type: OpenAPI
  - url: https://github.com/openai
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://openai.com/api/pricing/
    data:
      - id: free
        name: Free
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: 0
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: Access to GPT5
          - name: Real-time data from the web with search
          - name: >-
              Limited access to file uploads, data analysis, image generation,
              and voice mode
          - name: Code edits with the ChatGPT desktop app for macOS
          - name: Use custom GPTs
        description: Explore how AI can help with everyday tasks
      - id: plus
        name: Plus
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: $20.00
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: Extended access to GPT5, our flagship model
          - name: >-
              Extended limits on messaging, file uploads, data analysis, and
              image generation
          - name: Standard and advanced voice mode with video and screensharing
          - name: Access to ChatGPT agent
          - name: Create and use projects, tasks, and custom GPTs
          - name: Limited access to Sora video generation
          - name: Opportunities to test new features
        description: Level up productivity and creativity with expanded access
      - id: pro
        name: Pro
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: $200.00
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: Unlimited access to GPT5
          - name: >-
              Access to GPT5 pro, which uses more compute for the best answers
              to the hardest questions
          - name: >-
              Unlimited access to advanced voice, with higher limits for video
              and screensharing
          - name: >-
              Access to OpenAI o3pro, which uses more compute for the best
              answers to the hardest questions
          - name: Extended access to ChatGPT agent
          - name: Extended access to Sora video generation
          - name: Access to research preview of Codex agent
        description: Get the best of OpenAI with the highest level of access
      - id: team
        name: Team
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: $25.00
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: >-
              Unlimited GPT5 messages, with generous access to GPT5 thinking,
              and access to GPT5 proplus the flexibility to add credits as
              needed
          - name: >-
              A secure, dedicated workspace with essential admin controls, SAML
              SSO, and MFA
          - name: >-
              Team data is excluded from training by default, with encryption at
              rest and in transit. Learn more`
          - name: >-
              Support for compliance with GDPR, CCPA, and other privacy laws.
              Aligned with CSA STAR` and SOC 2 Type 2 Trust Services Criteria.
          - name: >-
              Connectors to apps for more personalized answersGoogle Drive,
              SharePoint, GitHub, Notion, and more
          - name: >-
              Business features like data analysis, record mode, canvas,
              projects, tasks, custom workspace GPTs, and deep research
          - name: >-
              Includes access to Codex and ChatGPT agent for reasoning and
              taking action across your documents, tools, and codebases
        description: A secure, collaborative workspace for startups and growing teams
      - id: enterprise
        name: Enterprise
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Contact
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: >-
              Expanded context window that supports longer inputs and larger
              files
          - name: >-
              Enterprise-level security and controls, including SCIM, user
              analytics, domain verification, and role-based access controls
          - name: >-
              Advanced data privacy with custom data retention policies,
              encryption at rest and in transit, and no training on your
              business data by default. Learn more`
          - name: Support for data residency in seven regions
          - name: >-
              24/7 priority support, SLAs, custom legal terms, and access to AI
              advisors for eligible customers
          - name: >-
              Built for scale with volume discounts, invoicing and ACH billing,
              and support for unlimited users
        description: Enterprise-grade AI, security, and support at scale
    name: Plans
    type: Plans
    description: This is the description of the plans for general OpenAI usage.
  - url: https://openai.com/api/pricing/
    data:
      - id: gpt-5
        name: GPT-5
        type: Flagship
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 1.25
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.125
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 10
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
        description: The best model for coding and agentic tasks across industries.
      - id: gpt-5-mini
        name: GPT-5 mini
        type: Flagship
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 0.25
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.025
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 2
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
        description: A faster, cheaper version of GPT-5 for well-defined tasks.
      - id: gpt-5-nano
        name: GPT-5 nano
        type: Flagship
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 0.05
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.005
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 0.4
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
        description: >-
          The fastest, cheapest version of GPT-5great for summarization and
          classification tasks.
      - id: gpt-4-1
        name: GPT-4.1
        type: Fine-Tuning
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 3
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.75
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 12
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Training
            price: 25
            metric: token
            timeFrame: usage
            description: Training token usage-based pricing.
        description: No description.
      - id: gpt-4-1-mini
        name: GPT-4.1 mini
        type: Fine-Tuning
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 0.8
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.2
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 3.2
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Training
            price: 5
            metric: token
            timeFrame: usage
            description: Training token usage-based pricing.
        description: No description.
      - id: gpt-4-1-nano
        name: GPT-4.1 nano
        type: Fine-Tuning
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 0.2
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.05
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 0.8
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Training
            price: 1.5
            metric: token
            timeFrame: usage
            description: Training token usage-based pricing.
        description: No description.
      - id: o4-mini
        name: o4-mini
        type: Fine-Tuning
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 4
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 1
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 16
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Training
            price: 100
            metric: token
            timeFrame: usage
            description: Training token usage-based pricing.
        description: No description.
    name: Pricing
    type: Pricing
    description: this is the pricing for API usage across different models.
created: '2024-04-14'
modified: '2025-08-14'
position: Consuming
description: >-
  OpenAI is a research organization that focuses on artificial intelligence (AI)
  and machine learning. Their mission is to ensure that AI benefits all of
  humanity, and they work on developing AI technology in a way that is safe and
  beneficial for society. OpenAI conducts cutting-edge research in fields such
  as natural language processing, reinforcement learning, and robotics. They
  also develop and release tools and models that help advance the field of AI
  and are open-source and accessible to the public. Additionally, OpenAI engages
  in outreach and advocacy efforts to promote the responsible development and
  deployment of AI technologies.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.19'
---