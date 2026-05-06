---
name: IBM MQ
description: APIs for IBM MQ messaging middleware for enterprise integration.
image: https://www.ibm.com/brand/experience-guides/developer/8f4e3cc842d31b9a55e57cb2b0e49605/02_8-bar-positive.svg
tags:
  - Async
  - Enterprise
  - Integration
  - Messaging
  - Middleware
  - Queue
created: '2024-01-20'
modified: '2026-04-28'
url: https://www.ibm.com/products/mq
specificationVersion: '0.18'
apis:
  - name: IBM MQ REST API
    description: REST API for managing and monitoring IBM MQ queue managers, queues, topics, and channels.
    image: https://www.ibm.com/brand/experience-guides/developer/8f4e3cc842d31b9a55e57cb2b0e49605/02_8-bar-positive.svg
    humanURL: https://www.ibm.com/docs/en/ibm-mq/latest?topic=api-rest-overview
    baseURL: https://{host}:{port}/ibmmq/rest/v2
    tags:
      - Admin
      - Messaging
      - Rest
    properties:
      - type: documentation
        url: https://www.ibm.com/docs/en/ibm-mq/latest?topic=api-rest
      - type: openapi
        url: https://www.ibm.com/docs/en/SSFKSJ_9.3.0/com.ibm.mq.dev.doc/rest_api_swagger.json
      - type: OpenAPI
        url: openapi/ibm-mq-admin-rest-openapi.yml
    contact:
      - FN: IBM Support
        email: support@ibm.com
        url: https://www.ibm.com/mysupport
  - name: IBM MQ Messaging REST API
    description: REST API for sending and receiving messages via HTTP.
    image: https://www.ibm.com/brand/experience-guides/developer/8f4e3cc842d31b9a55e57cb2b0e49605/02_8-bar-positive.svg
    humanURL: https://www.ibm.com/docs/en/ibm-mq/latest?topic=api-messaging-rest
    baseURL: https://{host}:{port}/ibmmq/rest/v2/messaging
    tags:
      - Consumer
      - Messaging
      - Producer
      - Rest
    properties:
      - type: documentation
        url: https://www.ibm.com/docs/en/ibm-mq/latest?topic=api-messaging-rest
      - type: openapi
        url: https://www.ibm.com/docs/en/SSFKSJ_9.3.0/com.ibm.mq.dev.doc/messaging_rest_api_swagger.json
      - type: OpenAPI
        url: openapi/ibm-mq-messaging-rest-openapi.yml
    contact:
      - FN: IBM Support
        email: support@ibm.com
        url: https://www.ibm.com/mysupport
  - name: IBM MQ JMS API
    description: Java Message Service API for IBM MQ.
    image: https://www.ibm.com/brand/experience-guides/developer/8f4e3cc842d31b9a55e57cb2b0e49605/02_8-bar-positive.svg
    humanURL: https://www.ibm.com/docs/en/ibm-mq/latest?topic=api-jms
    tags:
      - Java
      - Jms
      - Messaging
    properties:
      - type: documentation
        url: https://www.ibm.com/docs/en/ibm-mq/latest?topic=mq-developing-jms-applications
      - type: sdk
        url: https://mvnrepository.com/artifact/com.ibm.mq/com.ibm.mq.allclient
      - type: AsyncAPI
        url: asyncapi/ibm-mq-messaging-asyncapi.yml
    contact:
      - FN: IBM Support
        email: support@ibm.com
        url: https://www.ibm.com/mysupport
  - name: IBM MQ Native API
    description: Native procedural API for IBM MQ (MQI).
    image: https://www.ibm.com/brand/experience-guides/developer/8f4e3cc842d31b9a55e57cb2b0e49605/02_8-bar-positive.svg
    humanURL: https://www.ibm.com/docs/en/ibm-mq/latest?topic=reference-mqi
    tags:
      - Mqi
      - Native
      - Procedural
    properties:
      - type: documentation
        url: https://www.ibm.com/docs/en/ibm-mq/latest?topic=programming-mqi
    contact:
      - FN: IBM Support
        email: support@ibm.com
        url: https://www.ibm.com/mysupport
common:
  - type: getting-started
    url: https://www.ibm.com/docs/en/ibm-mq/latest?topic=mq-getting-started
  - type: tutorials
    url: https://developer.ibm.com/tutorials/?s=mq
  - type: downloads
    url: https://www.ibm.com/support/pages/downloading-ibm-mq
  - type: pricing
    url: https://www.ibm.com/products/mq/pricing
  - type: support
    url: https://www.ibm.com/mysupport
  - type: blog
    url: https://community.ibm.com/community/user/integration/communities/community-home?CommunityKey=183ec850-4947-49c8-9a2e-8e7c7fc46c64
  - type: JSON-LD
    url: json-ld/ibm-mq-context.jsonld
  - type: JSONSchema
    url: json-schema/ibm-mq-queue-manager-schema.json
  - type: JSONSchema
    url: json-schema/ibm-mq-queue-schema.json
  - type: Rules
    url: rules/ibm-mq-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
