---
aid: proompty
name: Proompty
description: Proompty is a web-based platform that offers customizable prompts and exercises to inspire creativity and productivity. Users can access a wide range of prompts, from writing exercises to drawing challenges, designed to spark new ideas and break through mental blocks.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Prompts
url: https://raw.githubusercontent.com/api-evangelist/proompty/refs/heads/main/apis.yml
created: '2024-06-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: proompty:proompty
    name: Proompty
    tags:
      - Chat
      - Documents
      - Prompts
      - Topics
      - Uploads
    baseURL: https://app.proompty.com/api/
    humanURL: https://app.proompty.com/docs/api
    properties:
      - url: https://app.proompty.com/docs/api
        type: Documentation
      - url: openapi/proompty-openapi-original.yml
        type: OpenAPI
    description: Proompty is an advanced Retrieval Augmented Generation (RAG) API designed to empower users in seamlessly integrating their data and harnessing the power of customized Large Language Model (LLM) prompts for interactive communication. At its core, Proompty operates through a series of interconnected functionalities that enable users to navigate and manipulate their data effectively.
common:
  - url: https://app.proompty.com/docs/api
    type: GettingStarted
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
