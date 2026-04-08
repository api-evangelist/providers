---
aid: llamaindex
url: https://raw.githubusercontent.com/api-evangelist/llamaindex/refs/heads/main/apis.yml
apis:
- aid: llamaindex:llamacloud-api
  name: LlamaIndex LlamaCloud API
  tags:
  - Agents
  - Artificial Intelligence
  - Cloud
  - Documents
  - LLM
  - RAG
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.cloud.llamaindex.ai
  humanURL: https://developers.api.llamaindex.ai/
  properties:
  - url: https://developers.api.llamaindex.ai/
    type: Documentation
  - url: openapi/llamaindex-llamacloud-api-openapi.yml
    type: OpenAPI
  description: The LlamaCloud API is the central REST API for LlamaIndex's cloud platform, providing programmatic access to managed document processing, indexing, and retrieval services. It enables developers to build production-grade LLM applications by leveraging cloud-hosted infrastructure for document ingestion, knowledge management, and agent orchestration. The API supports authentication via API keys and is available in both US and EU regions.
- aid: llamaindex:llamaparse-api
  name: LlamaIndex LlamaParse API
  tags:
  - Artificial Intelligence
  - Document Parsing
  - LLM
  - OCR
  - PDF
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.cloud.llamaindex.ai
  humanURL: https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/
  properties:
  - url: https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/
    type: Documentation
  - url: openapi/llamaindex-llamaparse-api-openapi.yml
    type: OpenAPI
  description: 'LlamaParse is a GenAI-native document parsing API that can parse complex document data for any downstream LLM use case including agents, RAG pipelines, and data processing workflows. The v2 API provides two main endpoints for parsing: one for JSON requests accepting file IDs or URLs, and another for multipart file uploads. It supports multiple parsing tiers including fast, cost-effective, agentic, and agentic-plus modes, and returns results asynchronously via job polling.'
- aid: llamaindex:llamaextract-api
  name: LlamaIndex LlamaExtract API
  tags:
  - Artificial Intelligence
  - Data Extraction
  - Documents
  - JSON
  - Structured Data
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.cloud.llamaindex.ai
  humanURL: https://developers.llamaindex.ai/python/cloud/llamaextract/getting_started/api/
  properties:
  - url: https://developers.llamaindex.ai/python/cloud/llamaextract/getting_started/api/
    type: Documentation
  - url: openapi/llamaindex-llamaextract-api-openapi.yml
    type: OpenAPI
  description: LlamaExtract is a prebuilt agentic data extraction API that transforms unstructured document data into structured JSON representations. The REST API allows developers to create extraction agents, upload documents, and run extraction jobs programmatically. Jobs are processed asynchronously, and developers can poll for job status and retrieve structured results. It is designed for use cases where documents need to be converted into well-defined schemas for downstream processing.
- aid: llamaindex:llamacloud-index-api
  name: LlamaIndex LlamaCloud Index API
  tags:
  - Document Ingestion
  - Indexing
  - RAG
  - Retrieval
  - Vector Store
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.cloud.llamaindex.ai
  humanURL: https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/
  properties:
  - url: https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/
    type: Documentation
  - url: openapi/llamaindex-llamacloud-index-api-openapi.yml
    type: OpenAPI
  description: The LlamaCloud Index API provides a fully automated document ingestion pipeline with built-in retrieval capabilities. It allows developers to create and manage indexes, upload documents for automatic parsing and embedding, and perform retrieval queries against indexed content. The API supports customizable pipeline configurations and integrates with various vector stores, making it suitable for building production RAG applications without managing infrastructure.
- aid: llamaindex:python-framework
  name: LlamaIndex Python Framework
  tags:
  - Agents
  - Framework
  - LLM
  - Open Source
  - Python
  - RAG
  - SDK
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developers.llamaindex.ai/python/framework/
  properties:
  - url: https://developers.llamaindex.ai/python/framework/
    type: Documentation
  description: LlamaIndex is an open-source Python framework for building LLM-powered applications including agents, RAG pipelines, and custom workflows. It provides data connectors for ingesting data from various sources such as APIs, PDFs, databases, and more. The framework offers high-level abstractions like query engines, chat engines, and agent classes (FunctionAgent, ReActAgent, CodeActAgent), as well as lower-level APIs for advanced customization.
- aid: llamaindex:typescript-framework
  name: LlamaIndex TypeScript Framework
  tags:
  - Agents
  - Framework
  - JavaScript
  - LLM
  - Open Source
  - RAG
  - SDK
  - TypeScript
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developers.llamaindex.ai/typescript/framework/
  properties:
  - url: https://developers.llamaindex.ai/typescript/framework/
    type: Documentation
  description: LlamaIndex TypeScript is the JavaScript and TypeScript implementation of the LlamaIndex framework for building LLM-powered applications. It provides server-side TypeScript support for building agents, RAG pipelines, and agentic workflows with the same core abstractions as the Python framework. The library supports integration with LlamaCloud services and offers convenient access to cloud APIs for document parsing, extraction, and indexing from Node.js environments.
name: Llamaindex
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: LlamaCloud is a hosted service for document processing and search, powered by LlamaIndex.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

