---
aid: anthropic
url: >-
  https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/apis.yml
apis:
  - aid: anthropic:anthropic-message-api
    name: Anthropic Messages API
    tags:
      - AI
      - Artificial Intelligence
      - Messages
    humanURL: https://docs.anthropic.com/en/api/messages
    properties:
      - url: https://docs.anthropic.com/en/api/messages
        type: Documentation
    description: >-
      List available models. The Models API response can be used to determine
      which models are available for use in the API. More recently released
      models are listed first.
  - aid: anthropic:anthropic-models-api
    name: Anthropic Models API
    tags:
      - AI
      - Artificial Intelligence
      - Models
    humanURL: https://docs.anthropic.com/en/api/models-list
    properties:
      - url: https://docs.anthropic.com/en/api/models-list
        type: Documentation
    description: >-
      Send a structured list of input messages with text and/or image content,
      and the model will generate the next message in the conversation.    
  - aid: anthropic:anthropic-message-batches-api
    name: Anthropic Message Batches API
    tags:
      - AI
      - Artificial Intelligence
      - Messages
      - Batches
    humanURL: https://docs.anthropic.com/en/api/creating-message-batches
    properties:
      - url: https://docs.anthropic.com/en/api/creating-message-batches
        type: Documentation
    description: >-
      Send a batch of Message creation requests. The Message Batches API can be
      used to process multiple Messages API requests at once. Once a Message
      Batch is created, it begins processing immediately. Batches can take up to
      24 hours to complete.       
  - aid: anthropic:anthropic-files-api
    name: Anthropic Files API
    tags:
      - AI
      - Artificial Intelligence
      - Files
    humanURL: https://docs.anthropic.com/en/api/files-create
    properties:
      - url: https://docs.anthropic.com/en/api/files-create
        type: Documentation
    description: >-
      The Files API allows you to upload and manage files to use with the
      Anthropic API without having to re-upload content with each request. For
      more information about the Files API, see the developer guide for
      files.      
  - aid: anthropic:anthropic-admin-api
    name: Anthropic Admin API
    tags:
      - AI
      - Artificial Intelligence
      - Administrative
    humanURL: https://docs.anthropic.com/en/api/admin-api/users/get-user
    properties:
      - url: https://docs.anthropic.com/en/api/admin-api/users/get-user
        type: Documentation
    description: 'Manage administrative functions.            '
  - aid: anthropic:anthropic-workspace-api
    name: Anthropic Workspace API
    tags:
      - AI
      - Artificial Intelligence
      - Workspace
    humanURL: https://docs.anthropic.com/en/api/admin-api/workspaces/get-workspace
    properties:
      - url: https://docs.anthropic.com/en/api/admin-api/workspaces/get-workspace
        type: Documentation
    description: 'Manage workspaces.    '
  - aid: anthropic:anthropic-workspace-members-api
    name: Anthropic Workspace Member API
    tags:
      - AI
      - Artificial Intelligence
      - Workspace
      - Members
    humanURL: >-
      https://docs.anthropic.com/en/api/admin-api/workspace_members/get-workspace-member
    properties:
      - url: >-
          https://docs.anthropic.com/en/api/admin-api/workspace_members/get-workspace-member
        type: Documentation
    description: 'Manage workspaces.          '
  - aid: anthropic:anthropic-prompts-api
    name: Anthropic Prompts API
    tags:
      - AI
      - Artificial Intelligence
      - Prompts
    humanURL: https://docs.anthropic.com/en/api/prompt-tools-generate
    properties:
      - url: https://docs.anthropic.com/en/api/prompt-tools-generate
        type: Documentation
    description: 'Manage workspaces.             '
name: Anthropic
tags:
  - AI
  - Artificial Intelligence
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/anthropics/anthropic-quickstarts
    name: Quickstarts
    type: Quickstarts
  - url: https://docs.anthropic.com/en/home
    name: Home - Anthropic
    type: Portal
    description: 'null'
  - url: https://docs.anthropic.com/en/api/messages
    name: Messages - Anthropic
    type: Documentation
    description: 'null'
  - url: https://status.anthropic.com/
    name: Anthropic Status
    type: Status
    description: 'null'
  - url: https://docs.anthropic.com/en/release-notes/api
    name: API - Anthropic
    type: ChangeLog
    description: 'null'
  - url: https://console.anthropic.com/login
    name: Anthropic Console
    type: Login
    description: 'null'
  - url: https://docs.anthropic.com/en/api/rate-limits
    name: Rate limits - Anthropic
    type: RateLimits
    description: 'null'
  - url: https://docs.anthropic.com/en/api/service-tiers
    name: Service tiers - Anthropic
    type: Tiers
    description: 'null'
  - url: https://docs.anthropic.com/en/api/errors
    name: Errors - Anthropic
    type: Errors
    description: 'null'
  - url: https://docs.anthropic.com/en/api/client-sdks
    name: Client SDKs - Anthropic
    type: SDKs
    description: 'null'
  - url: https://docs.anthropic.com/en/api/versioning
    name: Versions - Anthropic
    type: Versioning
    description: 'null'
  - url: https://docs.anthropic.com/en/api/supported-regions
    name: Supported regions - Anthropic
    type: Regions
    description: 'null'
  - url: https://docs.anthropic.com/en/api/getting-help
    name: Getting help - Anthropic
    type: Support
    description: 'null'
created: '2025-08-14'
modified: '2025-08-14'
position: Consuming
description: >-
  Claude is an AI assistant created by Anthropic that helps people with a wide
  variety of tasks through natural conversation. I can assist with writing and
  editing, answer questions on many topics, help with analysis and research,
  provide coding support, engage in creative projects, and offer explanations of
  complex concepts.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---