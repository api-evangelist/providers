---
aid: whatsapp
url: https://raw.githubusercontent.com/api-evangelist/whatsapp/refs/heads/main/apis.yml
apis:
- name: WhatsApp Business Platform API
  description: The Cloud API and On-Premises API that enables medium and large businesses to communicate with customers at scale.
  image: https://www.whatsapp.com/img/fb-post.jpg
  humanURL: https://developers.facebook.com/docs/whatsapp
  baseURL: https://graph.facebook.com/v21.0
  tags:
  - Business
  - Chat
  - Communications
  - Messaging
  properties:
  - type: Documentation
    url: https://developers.facebook.com/docs/whatsapp/cloud-api
  - type: OpenAPI
    url: openapi/whatsapp-cloud-api-openapi.yml
  - type: Authentication
    url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
  - type: Webhooks
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks
  - type: AsyncAPI
    url: asyncapi/whatsapp-webhooks-asyncapi.yml
  - type: JSONSchema
    url: json-schema/whatsapp-message-schema.json
  - type: Reference
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages
  - type: Getting Started
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
  - type: Pricing
    url: https://developers.facebook.com/docs/whatsapp/pricing
  - type: Rate Limits
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput
  - type: Status
    url: https://metastatus.com/
  - type: Change Log
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/changelog
  - type: Error Codes
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes
  - type: PostmanCollection
    url: https://www.postman.com/meta/whatsapp-business-platform/collection/wlk6lh4/whatsapp-cloud-api
  - type: Node.js SDK
    url: https://github.com/WhatsApp/WhatsApp-Nodejs-SDK
  - type: Sandbox
    url: https://business.whatsapp.com/developers/developer-hub
  - type: Migration Guide
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/migrate-to-cloud-api
  - type: Media Reference
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media
  - type: Phone Numbers Reference
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/phone-numbers
  - type: Business Profiles Reference
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/business-profiles
  - type: Two-Step Verification
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification
  - type: Versioning
    url: https://developers.facebook.com/docs/graph-api/guides/versioning
  contact:
  - type: Support
    url: https://developers.facebook.com/support/
  - type: Twitter
    url: https://twitter.com/WhatsApp
- name: WhatsApp Business Account Management API
  description: API for managing WhatsApp Business Accounts, phone numbers, and messaging templates.
  image: https://www.whatsapp.com/img/fb-post.jpg
  humanURL: https://developers.facebook.com/docs/whatsapp/business-management-api
  baseURL: https://graph.facebook.com/v21.0
  tags:
  - Accounts
  - Business
  - Management
  - Templates
  properties:
  - type: Documentation
    url: https://developers.facebook.com/docs/whatsapp/business-management-api
  - type: OpenAPI
    url: openapi/whatsapp-business-management-api-openapi.yml
  - type: Authentication
    url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
  - type: JSONSchema
    url: json-schema/whatsapp-message-template-schema.json
  - type: Getting Started
    url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
  - type: PostmanCollection
    url: https://www.postman.com/meta/whatsapp-business-platform/collection/3kru5r6/whatsapp-business-management-api
  - type: Reference
    url: https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates
  - type: Change Log
    url: https://developers.facebook.com/docs/whatsapp/business-management-api/changelog
  - type: Error Codes
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes
  - type: Rate Limits
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput
- name: WhatsApp Flows API
  description: API for creating structured, interactive forms and multi-step flows within WhatsApp conversations, enabling appointment booking, surveys, lead capture, and other guided experiences using a JSON-based screen definition format.
  image: https://www.whatsapp.com/img/fb-post.jpg
  humanURL: https://developers.facebook.com/docs/whatsapp/flows
  baseURL: https://graph.facebook.com/v21.0
  tags:
  - Flows
  - Forms
  - Interactive
  - Messaging
  properties:
  - type: Documentation
    url: https://developers.facebook.com/docs/whatsapp/flows
  - type: OpenAPI
    url: openapi/whatsapp-flows-api-openapi.yml
  - type: Reference
    url: https://developers.facebook.com/docs/whatsapp/flows/reference/components
  - type: JSONSchema
    url: json-schema/whatsapp-flow-json-schema.json
  - type: Change Log
    url: https://developers.facebook.com/docs/whatsapp/flows/changelogs
  - type: Error Codes
    url: https://developers.facebook.com/docs/whatsapp/flows/reference/error-codes
  - type: PostmanCollection
    url: https://www.postman.com/meta/whatsapp-business-platform/collection/y5swede/whatsapp-flows-api
  - type: GitHubRepository
    url: https://github.com/WhatsApp/WhatsApp-Flows-Tools
  - type: Getting Started
    url: https://developers.facebook.com/docs/whatsapp/flows/gettingstarted
  - type: Authentication
    url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
- name: WhatsApp On-Premises API
  description: The self-hosted version of the WhatsApp Business API that allowed businesses to run the API on their own infrastructure. This API was deprecated on October 23, 2025, and all users must migrate to the Cloud API.
  image: https://www.whatsapp.com/img/fb-post.jpg
  humanURL: https://developers.facebook.com/docs/whatsapp/on-premises
  baseURL: https://localhost:443
  tags:
  - Deprecated
  - Messaging
  - On-Premises
  - Self-Hosted
  properties:
  - type: Documentation
    url: https://developers.facebook.com/docs/whatsapp/on-premises
  - type: Getting Started
    url: https://developers.facebook.com/docs/whatsapp/on-premises/get-started/installation
  - type: Deprecation Notice
    url: https://developers.facebook.com/docs/whatsapp/on-premises
  - type: PostmanCollection
    url: https://www.postman.com/meta/whatsapp-business-platform/collection/vdi189b/whatsapp-on-premises-api-deprecated
  - type: Migration Guide
    url: https://developers.facebook.com/docs/whatsapp/cloud-api/migrate-to-cloud-api
name: WhatsApp
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for the WhatsApp messaging platform, enabling businesses to communicate with customers through the world's most popular messaging app.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

