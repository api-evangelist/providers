---
aid: cohere
url: https://raw.githubusercontent.com/api-evangelist/cohere/refs/heads/main/apis.yml
apis:
  - aid: cohere:chat-api
    name: Cohere Chat API
    tags:
      - Artificial Intelligence
      - Chat
      - Conversational AI
      - Large Language Models
      - Text Generation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cohere.com
    humanURL: https://docs.cohere.com/reference/chat
    properties:
      - url: https://docs.cohere.com/reference/chat
        type: Documentation
      - url: openapi/cohere-chat-api-openapi.yml
        type: OpenAPI
    description: The Cohere Chat API enables developers to integrate large language model text generation capabilities into their applications through a conversational interface. It supports multi-turn conversations, tool use with JSON schema definitions, retrieval-augmented generation, and streaming responses. The API is available via the v2 endpoint and works with Cohere's Command family of models.
  - aid: cohere:embed-api
    name: Cohere Embed API
    tags:
      - Artificial Intelligence
      - Embeddings
      - Natural Language Processing
      - Semantic Search
      - Vector Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cohere.com
    humanURL: https://docs.cohere.com/reference/embed
    properties:
      - url: https://docs.cohere.com/reference/embed
        type: Documentation
      - url: openapi/cohere-embed-api-openapi.yml
        type: OpenAPI
    description: The Cohere Embed API generates vector embeddings from text and images, enabling semantic search, clustering, and classification use cases. It supports multilingual content and can process both text and image inputs using the Embed v3 model family. Developers can use these embeddings to build retrieval systems, recommendation engines, and other applications that require understanding semantic similarity between content.
  - aid: cohere:rerank-api
    name: Cohere Rerank API
    tags:
      - Artificial Intelligence
      - Information Retrieval
      - Relevance
      - Reranking
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cohere.com
    humanURL: https://docs.cohere.com/reference/rerank
    properties:
      - url: https://docs.cohere.com/reference/rerank
        type: Documentation
      - url: openapi/cohere-rerank-api-openapi.yml
        type: OpenAPI
    description: The Cohere Rerank API takes a query and a list of text documents and returns them ordered by relevance with assigned relevance scores. It is commonly used as a second-stage ranker in retrieval-augmented generation pipelines to improve the quality of search results before passing them to a language model. The API supports multilingual reranking and can significantly improve the precision of search and retrieval systems.
  - aid: cohere:classify-api
    name: Cohere Classify API
    tags:
      - Artificial Intelligence
      - Classification
      - Natural Language Processing
      - Text Analysis
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cohere.com
    humanURL: https://docs.cohere.com/reference/classify
    properties:
      - url: https://docs.cohere.com/reference/classify
        type: Documentation
      - url: openapi/cohere-classify-api-openapi.yml
        type: OpenAPI
    description: The Cohere Classify API performs text classification by assigning labels to input text based on provided examples. It can be used for sentiment analysis, content moderation, topic categorization, and other classification tasks. Developers provide a set of labeled examples along with texts to classify, and the API returns predicted labels with confidence scores for each input.
  - aid: cohere:embed-jobs-api
    name: Cohere Embed Jobs API
    tags:
      - Artificial Intelligence
      - Batch Processing
      - Embeddings
      - Vector Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cohere.com
    humanURL: https://docs.cohere.com/reference/list-embed-jobs
    properties:
      - url: https://docs.cohere.com/reference/list-embed-jobs
        type: Documentation
      - url: openapi/cohere-embed-jobs-api-openapi.yml
        type: OpenAPI
    description: The Cohere Embed Jobs API allows developers to create and manage batch embedding jobs for processing large volumes of text data asynchronously. Rather than embedding texts one at a time, developers can submit datasets for bulk embedding and monitor job progress. This is useful for initializing vector databases, processing large document collections, and other scenarios where embedding large amounts of content is needed.
  - aid: cohere:datasets-api
    name: Cohere Datasets API
    tags:
      - Artificial Intelligence
      - Data Management
      - Datasets
      - Fine-Tuning
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cohere.com
    humanURL: https://docs.cohere.com/reference/list-datasets
    properties:
      - url: https://docs.cohere.com/reference/list-datasets
        type: Documentation
      - url: openapi/cohere-datasets-api-openapi.yml
        type: OpenAPI
    description: The Cohere Datasets API provides endpoints for uploading, managing, and retrieving datasets used with other Cohere services such as fine-tuning and embed jobs. Developers can create datasets from files, list existing datasets, retrieve dataset metadata, and delete datasets they no longer need. The API supports various data formats and validates uploaded data against expected schemas.
  - aid: cohere:models-api
    name: Cohere Models API
    tags:
      - Artificial Intelligence
      - Machine Learning
      - Models
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cohere.com
    humanURL: https://docs.cohere.com/reference/list-models
    properties:
      - url: https://docs.cohere.com/reference/list-models
        type: Documentation
      - url: openapi/cohere-models-api-openapi.yml
        type: OpenAPI
    description: The Cohere Models API allows developers to list and retrieve information about available Cohere models, including the Command, Embed, and Rerank model families. It provides details such as model names, versions, supported endpoints, context lengths, and capabilities. This API is useful for programmatically discovering which models are available and selecting the appropriate model for a given task.
  - aid: cohere:tokenize-api
    name: Cohere Tokenize API
    tags:
      - Artificial Intelligence
      - Natural Language Processing
      - Text Processing
      - Tokenization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cohere.com
    humanURL: https://docs.cohere.com/reference/tokenize
    properties:
      - url: https://docs.cohere.com/reference/tokenize
        type: Documentation
      - url: openapi/cohere-tokenize-api-openapi.yml
        type: OpenAPI
    description: The Cohere Tokenize API splits input text into tokens using the tokenizer associated with a specified model. It returns both the token strings and their corresponding token IDs. This is useful for understanding how text will be processed by Cohere models, estimating token counts for billing purposes, and debugging input formatting issues.
  - aid: cohere:detokenize-api
    name: Cohere Detokenize API
    tags:
      - Artificial Intelligence
      - Natural Language Processing
      - Text Processing
      - Tokenization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cohere.com
    humanURL: https://docs.cohere.com/reference/detokenize
    properties:
      - url: https://docs.cohere.com/reference/detokenize
        type: Documentation
      - url: openapi/cohere-detokenize-api-openapi.yml
        type: OpenAPI
    description: The Cohere Detokenize API converts a sequence of token IDs back into their corresponding text string using the tokenizer for a specified model. It is the inverse operation of the Tokenize API and is useful for inspecting model outputs at the token level, debugging tokenization behavior, and reconstructing text from token representations.
common:
  - type: JSON-LD
    url: json-ld/cohere-context.jsonld
  - type: JSONSchema
    url: json-schema/cohere-chat-message-schema.json
  - type: JSONSchema
    url: json-schema/cohere-embedding-schema.json
  - type: JSONSchema
    url: json-schema/cohere-model-schema.json
  - type: JSONSchema
    url: json-schema/cohere-dataset-schema.json
  - type: Features
    data:
      - Command at $1/$2 per MTok input/output
      - Command-light at $0.30/$0.60
      - Command R at $0.50/$1.50
      - Command R+ 08-2024 at $2.50/$10
      - Command R+ 04-2024 at $3/$15
      - Aya Expanse multilingual at $0.50/$1.50
      - Embed v3 with English/multilingual
      - Rerank for relevance scoring
      - 'Production keys: 10K req/min Chat, 2K Embed, 10K Rerank'
      - 'Trial keys: 20/min Chat, 100/min Embed'
      - Connectors for RAG over data sources
      - Tool use and function calling
      - Compass for unstructured data search
      - Available on AWS Bedrock, Azure, Oracle Cloud
      - Fine-tuning for Command and Aya
      - OpenAI-compatible Chat Completions endpoint
    sources:
      - https://cohere.com/pricing
    updated: '2026-05-04'
modified: '2026-05-04'
description: Generates a text response to a user message and streams it down, token by token.
---
