---
aid: microsoft-azure-queue-storage
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-queue-storage/refs/heads/main/apis.yml
name: Azure Queue Storage
description: Azure Queue Storage is a Microsoft cloud service for storing large numbers of messages, enabling decoupled and asynchronous communication between application components. Messages can be accessed via authenticated HTTP/HTTPS calls and support visibility timeouts, peeking, and metadata for reliable processing.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Asynchronous Processing
  - Cloud Storage
  - Messaging
  - Queue
  - Storage
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: microsoft-azure-queue-storage:rest-api
    name: Azure Queue Storage REST API
    description: Azure Queue Storage REST API provides cloud-based message queuing for decoupling application components. It supports creating queues, adding messages, peeking at messages, dequeuing messages with visibility timeouts, and managing queue metadata for asynchronous processing.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/queue-service-rest-api
    baseURL: https://{account}.queue.core.windows.net/
    tags:
      - Asynchronous Processing
      - Messaging
      - Queue
      - Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/queue-service-rest-api
      - type: Authentication
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-requests-to-azure-storage
      - type: Versioning
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/versioning-for-the-azure-storage-services
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/storage/queues/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/storage/queues/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/storage/queues/storage-quickstart-queues-portal
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction
  - type: Status
    url: https://azure.status.microsoft/en-us/status
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/product/storage/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
