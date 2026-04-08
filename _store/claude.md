---
aid: claude
url: https://raw.githubusercontent.com/api-evangelist/claude/refs/heads/main/apis.yml
apis:
- name: Claude Messages API
  description: Primary API for sending messages to Claude and receiving responses.
  image: https://www.anthropic.com/images/icons/anthropic-icon.png
  humanURL: https://docs.anthropic.com/en/api/messages
  baseURL: https://api.anthropic.com/v1
  tags:
  - AI
  - Conversational AI
  - Large Language Models
  - Natural Language Processing
  properties:
  - type: Documentation
    url: https://docs.anthropic.com/en/api/messages
  - type: OpenAPI
    url: openapi/claude-messages-api.yml
  - type: OpenAPI (Anthropic)
    url: https://docs.anthropic.com/claude/reference/openapi-spec
  - type: JSON Schema (Message)
    url: json-schema/claude-message-schema.json
  - type: JSON Schema (Tool Use)
    url: json-schema/claude-tool-use-schema.json
  - type: JSON-LD Context
    url: json-ld/claude-context.jsonld
  - type: Authentication
    url: https://docs.anthropic.com/claude/reference/authentication
  - type: Pricing
    url: https://www.anthropic.com/pricing
  - type: Rate Limits
    url: https://docs.anthropic.com/en/api/rate-limits
  - type: Getting Started
    url: https://docs.anthropic.com/en/api/getting-started
  - type: Messages Examples
    url: https://docs.anthropic.com/en/api/messages-examples
  - type: Client SDKs
    url: https://docs.anthropic.com/en/api/client-sdks
  - type: Python SDK
    url: https://github.com/anthropics/anthropic-sdk-python
  - type: TypeScript SDK
    url: https://github.com/anthropics/anthropic-sdk-typescript
  - type: API Changelog
    url: https://docs.anthropic.com/en/release-notes/api
  contact:
  - type: Support
    url: https://support.anthropic.com
  - type: Email
    url: mailto:support@anthropic.com
  endpoints:
  - name: Create Message
    method: POST
    path: /messages
    description: Send a message to Claude and receive a response
  - name: Stream Message
    method: POST
    path: /messages
    description: Stream a message response from Claude using server-sent events
  - name: Count Message Tokens
    method: POST
    path: /messages/count_tokens
    description: Count the number of tokens in a message including tools images and documents without creating it
- name: Claude Message Batches API
  description: API for asynchronously processing large volumes of message requests at reduced cost with 50 percent discount.
  image: https://www.anthropic.com/images/icons/anthropic-icon.png
  humanURL: https://docs.anthropic.com/en/api/creating-message-batches
  baseURL: https://api.anthropic.com/v1
  tags:
  - AI
  - Asynchronous
  - Batch Processing
  - Large Language Models
  properties:
  - type: Documentation
    url: https://docs.anthropic.com/en/api/creating-message-batches
  - type: OpenAPI
    url: openapi/claude-messages-api.yml
  - type: JSON Schema (Message)
    url: json-schema/claude-message-schema.json
  - type: JSON-LD Context
    url: json-ld/claude-context.jsonld
  - type: Batch Processing Guide
    url: https://docs.anthropic.com/en/docs/build-with-claude/batch-processing
  contact:
  - type: Support
    url: https://support.anthropic.com
  - type: Email
    url: mailto:support@anthropic.com
  endpoints:
  - name: Create Message Batch
    method: POST
    path: /messages/batches
    description: Create a batch of message requests for asynchronous processing
  - name: List Message Batches
    method: GET
    path: /messages/batches
    description: List all message batches within a workspace
  - name: Retrieve Message Batch
    method: GET
    path: /messages/batches/{message_batch_id}
    description: Retrieve the status and details of a specific message batch
  - name: Retrieve Message Batch Results
    method: GET
    path: /messages/batches/{message_batch_id}/results
    description: Stream the results of a completed message batch as a JSONL file
  - name: Cancel Message Batch
    method: POST
    path: /messages/batches/{message_batch_id}/cancel
    description: Cancel an in-progress message batch
  - name: Delete Message Batch
    method: DELETE
    path: /messages/batches/{message_batch_id}
    description: Delete a completed message batch
- name: Claude Models API
  description: API for listing and retrieving metadata about available Claude models including capabilities and context windows.
  image: https://www.anthropic.com/images/icons/anthropic-icon.png
  humanURL: https://docs.anthropic.com/en/api/models-list
  baseURL: https://api.anthropic.com/v1
  tags:
  - AI
  - Large Language Models
  - Models
  properties:
  - type: Documentation
    url: https://docs.anthropic.com/en/api/models-list
  - type: OpenAPI
    url: openapi/claude-messages-api.yml
  - type: JSON-LD Context
    url: json-ld/claude-context.jsonld
  - type: Models Overview
    url: https://docs.anthropic.com/en/docs/about-claude/models
  contact:
  - type: Support
    url: https://support.anthropic.com
  - type: Email
    url: mailto:support@anthropic.com
  endpoints:
  - name: List Models
    method: GET
    path: /models
    description: List all available Claude models with their metadata
  - name: Get Model
    method: GET
    path: /models/{model_id}
    description: Retrieve metadata for a specific Claude model
- name: Claude Files API
  description: API for uploading and managing files to reference in Claude API requests without re-uploading content each time.
  image: https://www.anthropic.com/images/icons/anthropic-icon.png
  humanURL: https://docs.anthropic.com/en/docs/build-with-claude/files
  baseURL: https://api.anthropic.com/v1
  tags:
  - AI
  - Document Processing
  - File Management
  - Files
  properties:
  - type: Documentation
    url: https://docs.anthropic.com/en/docs/build-with-claude/files
  - type: Upload File Reference
    url: https://docs.anthropic.com/en/api/files-create
  - type: List Files Reference
    url: https://docs.anthropic.com/en/api/files-list
  contact:
  - type: Support
    url: https://support.anthropic.com
  - type: Email
    url: mailto:support@anthropic.com
  endpoints:
  - name: Upload File
    method: POST
    path: /files
    description: Upload a file to be referenced in future API calls
  - name: List Files
    method: GET
    path: /files
    description: List uploaded files
  - name: Get File Metadata
    method: GET
    path: /files/{file_id}
    description: Retrieve metadata for a specific uploaded file
  - name: Download File
    method: GET
    path: /files/{file_id}/content
    description: Download file content created by skills or the code execution tool
  - name: Delete File
    method: DELETE
    path: /files/{file_id}
    description: Delete an uploaded file
- name: Claude Admin API
  description: API for programmatically managing organization resources including members workspaces API keys and invites.
  image: https://www.anthropic.com/images/icons/anthropic-icon.png
  humanURL: https://docs.anthropic.com/en/api/administration-api
  baseURL: https://api.anthropic.com/v1
  tags:
  - Administration
  - AI
  - API Keys
  - Organization Management
  - Workspaces
  properties:
  - type: Documentation
    url: https://docs.anthropic.com/en/api/administration-api
  - type: List API Keys Reference
    url: https://docs.anthropic.com/en/api/admin-api/apikeys/list-api-keys
  - type: List Workspaces Reference
    url: https://docs.anthropic.com/en/api/admin-api/workspaces/list-workspaces
  - type: List Invites Reference
    url: https://docs.anthropic.com/en/api/admin-api/invites/list-invites
  - type: List Organization Members Reference
    url: https://docs.anthropic.com/en/api/admin-api/workspace_members/list-workspace-members
  contact:
  - type: Support
    url: https://support.anthropic.com
  - type: Email
    url: mailto:support@anthropic.com
  endpoints:
  - name: Get Organization
    method: GET
    path: /organizations/me
    description: Retrieve information about your organization
  - name: List Organization Members
    method: GET
    path: /organizations/users
    description: List all members of the organization
  - name: Update Organization Member
    method: POST
    path: /organizations/users/{user_id}
    description: Update an organization member role
  - name: Remove Organization Member
    method: DELETE
    path: /organizations/users/{user_id}
    description: Remove a member from the organization
  - name: List Invites
    method: GET
    path: /organizations/invites
    description: List all pending invitations
  - name: Create Invite
    method: POST
    path: /organizations/invites
    description: Invite a user to the organization
  - name: Delete Invite
    method: DELETE
    path: /organizations/invites/{invite_id}
    description: Delete a pending invitation
  - name: List Workspaces
    method: GET
    path: /organizations/workspaces
    description: List all workspaces in the organization
  - name: Get Workspace
    method: GET
    path: /organizations/workspaces/{workspace_id}
    description: Retrieve details of a specific workspace
  - name: List Workspace Members
    method: GET
    path: /organizations/workspaces/{workspace_id}/members
    description: List all members of a workspace
  - name: Add Workspace Member
    method: POST
    path: /organizations/workspaces/{workspace_id}/members
    description: Add a member to a workspace
  - name: Update Workspace Member
    method: POST
    path: /organizations/workspaces/{workspace_id}/members/{user_id}
    description: Update a workspace member role
  - name: Remove Workspace Member
    method: DELETE
    path: /organizations/workspaces/{workspace_id}/members/{user_id}
    description: Remove a member from a workspace
  - name: List API Keys
    method: GET
    path: /organizations/api_keys
    description: List all API keys in the organization
  - name: Update API Key
    method: POST
    path: /organizations/api_keys/{api_key_id}
    description: Update an API key name or status
- name: Claude Usage and Cost API
  description: API for tracking token consumption and costs across your organization with breakdowns by model workspace and service tier.
  image: https://www.anthropic.com/images/icons/anthropic-icon.png
  humanURL: https://docs.anthropic.com/en/api/usage-cost-api
  baseURL: https://api.anthropic.com/v1
  tags:
  - AI
  - Analytics
  - Cost Tracking
  - Usage
  properties:
  - type: Documentation
    url: https://docs.anthropic.com/en/api/usage-cost-api
  contact:
  - type: Support
    url: https://support.anthropic.com
  - type: Email
    url: mailto:support@anthropic.com
  endpoints:
  - name: Get Usage Report
    method: GET
    path: /organizations/usage_report/messages
    description: Retrieve token usage report with breakdowns by model workspace and service tier
  - name: Get Cost Report
    method: GET
    path: /organizations/cost_report
    description: Retrieve service-level cost breakdowns in USD including token usage web search and code execution costs
- name: Claude Text Completions API
  description: Legacy API for generating text completions - deprecated in favor of the Messages API.
  image: https://www.anthropic.com/images/icons/anthropic-icon.png
  humanURL: https://docs.anthropic.com/en/api/complete
  baseURL: https://api.anthropic.com/v1
  tags:
  - AI
  - Large Language Models
  - Legacy
  - Text Completion
  properties:
  - type: Documentation
    url: https://docs.anthropic.com/en/api/complete
  - type: Migration Guide
    url: https://docs.anthropic.com/en/api/complete
  contact:
  - type: Support
    url: https://support.anthropic.com
  - type: Email
    url: mailto:support@anthropic.com
  endpoints:
  - name: Create Text Completion
    method: POST
    path: /complete
    description: Generate a text completion from Claude (legacy - use Messages API instead)
name: Claude
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
type: Contract
image: https://www.anthropic.com/images/icons/anthropic-icon.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Anthropic's Claude AI assistant API for natural language processing and conversation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

