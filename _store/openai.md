---
aid: openai
url: https://raw.githubusercontent.com/api-search/ai/main/_apis/openai/apis.md
apis:
  - aid: openai:openai-assistants-api
    name: OpenAI Assistants API
    tags:
      - Assistants
      - Attaching
      - File
      - Files
      - Instructions
      - Models
      - Modifies
      - Returns
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
      - English
      - Generates
      - Inputs
      - Languages
      - Speech
      - Text
      - Transcribes
      - Transcriptions
      - Translations
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
      - Completions
      - Conversations
      - Creates
      - Given
      - Models
      - Responses
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
      - Conversations
      - Creates
      - Given
      - Models
      - Parameters
      - Prompts
      - Provided
      - Responses
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
      - Creates
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
created: 2024/04/14
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
specificationVersion: '0.16'
common:
  - name: Overview - OpenAI API
    description: 'null'
    url: https://platform.openai.com/docs/overview
    type: Portal
  - name: Developer quickstart - OpenAI API
    description: 'null'
    url: https://platform.openai.com/docs/quickstart
    type: GettingStarted
  - name: Pricing - OpenAI API
    description: 'null'
    url: https://platform.openai.com/docs/pricing
    type: Pricing
  - name: Libraries - OpenAI API
    description: 'null'
    url: https://platform.openai.com/docs/libraries
    type: SDKs
  - name: Categories - OpenAI Developer Community
    description: 'null'
    url: https://community.openai.com/categories
    type: Forums
  - name: Rate limits - OpenAI API
    description: 'null'
    url: https://platform.openai.com/docs/guides/rate-limits
    type: RateLimits
  - name: Deprecations - OpenAI API
    description: 'null'
    url: https://platform.openai.com/docs/deprecations
    type: Deprecations
  - name: Terms & policies | OpenAI
    description: 'null'
    url: https://openai.com/policies/
    type: TermsOfService
  - name: Terms of use | OpenAI
    description: 'null'
    url: https://openai.com/policies/terms-of-use/
    type: TermsOfService
  - name: Privacy policy | OpenAI
    description: 'null'
    url: https://openai.com/policies/privacy-policy/
    type: PrivacyPolicy
  - name: Overview - OpenAI API
    description: 'null'
    url: https://platform.openai.com/docs/overview
    type: Documentation
  - name: OpenAI Help Center
    description: 'null'
    url: https://help.openai.com/en
    type: Support
  - name: OpenAI Status
    description: 'null'
    url: https://status.openai.com/
    type: Status
  - name: API Reference - OpenAI API
    description: 'null'
    url: https://platform.openai.com/docs/api-reference/authentication
    type: Authentication
  - name: API Reference - OpenAI API
    description: 'null'
    url: https://platform.openai.com/docs/api-reference/webhook_events/response
    type: Webhooks
---