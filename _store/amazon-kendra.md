---
name: Amazon Kendra
segments:
  - Search
  - Machine Learning
description: Amazon Kendra is an intelligent enterprise search service powered by machine learning that enables organizations to index and search across multiple data sources, delivering highly accurate and relevant answers to natural language queries.
url: https://aws.amazon.com/kendra/
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AI
  - AWS
  - Enterprise Search
  - Knowledge Management
  - Machine Learning
  - Natural Language
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Kendra API
    description: The Amazon Kendra API provides programmatic access to create and manage intelligent search indexes, configure data source connectors, submit queries, and manage relevance tuning for ML-powered enterprise search.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/kendra/
    baseURL: https://kendra.amazonaws.com
    tags:
      - Enterprise Search
      - ML Search
      - Natural Language Processing
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/kendra/2019-02-03/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/kendra/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kendra/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/kendra/faqs/
      - type: Features
        url: https://aws.amazon.com/kendra/features/
      - type: Documentation
        url: https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html
      - type: APIReference
        url: https://docs.aws.amazon.com/kendra/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-kendra-openapi.yml
      - type: JSONLD
        url: json-ld/amazon-kendra-context.jsonld
      - type: JSONSchema
        url: json-schema/amazon-kendra-index-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kendra-data-source-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kendra-query-result-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kendra-faq-schema.json
common:
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-kendra/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Console
    url: https://console.aws.amazon.com/kendra/home
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/kendra/
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: Portal
    url: https://aws.amazon.com/kendra/
  - type: Documentation
    url: https://docs.aws.amazon.com/kendra/
  - type: Pricing
    url: https://aws.amazon.com/kendra/pricing/
  - type: GettingStarted
    url: https://aws.amazon.com/kendra/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/kendra/faqs/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Features
    data:
      - name: Intelligent Search
        description: ML-powered semantic search that understands natural language queries and context to return highly accurate answers from enterprise content.
      - name: GenAI RAG Support
        description: Kendra Retriever API enables retrieval-augmented generation workflows with optimized passage chunking and ACL-based filtering for LLM integration.
      - name: Data Source Connectors
        description: Native connectors for Amazon S3, SharePoint, Salesforce, ServiceNow, Google Drive, Confluence, and many more data repositories.
      - name: Relevance Tuning
        description: Fine-tune search results based on document freshness, authoritative sources, and custom synonyms without ML expertise.
      - name: Experience Builder
        description: No-code visual interface to build, customize, and launch search applications with drag-and-drop components.
      - name: Search Analytics Dashboard
        description: Visibility into quality and usability metrics and user interaction patterns to identify content gaps.
      - name: Custom Document Enrichment
        description: Preprocessing capabilities for metadata enrichment, document classification, entity extraction, and AWS AI service integration.
      - name: Incremental Learning
        description: Learns from user interactions and feedback to promote preferred documents to the top of search results over time.
  - type: UseCases
    data:
      - name: Employee Productivity
        description: Help employees find accurate answers and data-driven insights across internal knowledge bases and document repositories.
      - name: Customer Service
        description: Power self-service chatbots and agent-assist solutions for contact centers with intelligent search.
      - name: SaaS Application Integration
        description: Integrate intelligent search and conversational AI into customer-facing applications via the Kendra API.
      - name: Generative AI Applications
        description: Use Kendra GenAI indices in Amazon Q Business and Amazon Bedrock knowledge bases to build RAG applications.
      - name: Enterprise Knowledge Management
        description: Index and search across multiple heterogeneous data sources to create a unified knowledge search experience.
  - type: Integrations
    data:
      - name: Amazon Bedrock
        description: Use Kendra GenAI indices as knowledge bases in Amazon Bedrock for building generative AI applications.
      - name: Amazon Q Business
        description: Integrate Kendra indices with Amazon Q Business for AI-powered enterprise assistant experiences.
      - name: Amazon Lex
        description: Power Lex chatbots with Kendra search for FAQ-based conversational experiences.
      - name: Amazon S3
        description: Native data source connector for indexing documents stored in Amazon S3 buckets.
      - name: Microsoft SharePoint
        description: Native connector to index and search SharePoint Online and SharePoint Server content.
      - name: Salesforce
        description: Index Salesforce objects and knowledge articles for enterprise search.
      - name: ServiceNow
        description: Connect to ServiceNow to index knowledge base articles and service catalog items.
      - name: Amazon Comprehend
        description: Use Comprehend for entity extraction and metadata enrichment during custom document enrichment.
  - type: SpectralRules
    url: rules/amazon-kendra-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-kendra-enterprise-search.yaml
  - type: Vocabulary
    url: vocabulary/amazon-kendra-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include: []
---
