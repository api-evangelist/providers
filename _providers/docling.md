---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 31.7
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Docling Agentic Access
  operation_count: 9
  slug: docling-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 18
apis:
- description: Model Context Protocol server that exposes Docling document parsing as MCP tools so Claude, Cursor, Gemini, and other MCP-aware agents can convert PDFs, Office files, and images into structured `Docli
  name: Docling MCP Server
  slug: docling-mcp-server
- description: Canonical `DoclingDocument` data model and serialization primitives — text, tables, pictures, layout, hierarchy, bounding boxes, provenance — shared by the Docling library, Docling Serve, the Java por
  name: Docling Core Types
  slug: docling-core
- description: Native C++ PDF parsing engine used by Docling to extract text with precise coordinates from programmatic (non-scanned) PDF files. Distributed as a Python extension.
  name: Docling Parse PDF Extractor
  slug: docling-parse
- description: Open-weight IBM Research models that power Docling's understanding pipeline — DocLayout (layout detection and reading order), TableFormer (table structure), code- and formula-recognition heads, pictur
  name: Docling IBM Models
  slug: docling-ibm-models
- description: End-to-end evaluation framework for document parsing models and services. Provides standard datasets and metrics for layout, tables, OCR, and reading-order quality so teams can benchmark Docling — and
  name: Docling Eval
  slug: docling-eval
- description: Tools for synthesizing labeled document data from real corpora — useful for fine-tuning layout, table, and reading-order models, and for stress-testing downstream RAG pipelines.
  name: Docling Synthetic Data Generation
  slug: docling-sdg
- description: Transform unstructured documents — once normalized to `DoclingDocument` — into validated, rich, queryable knowledge graphs. Intended for GraphRAG and entity-extraction workflows on top of Docling outp
  name: Docling Graph
  slug: docling-graph
- description: Reference agent that reads, writes, and edits documents using Docling as the IO layer. Demonstrates how Docling output composes with tool-using LLMs to produce structured edits.
  name: Docling Agent
  slug: docling-agent
- description: Go-based Kubernetes operator that deploys and manages Docling Serve workloads — model cache PVCs, GPU/CPU pools, RQ workers, replica sets with sticky sessions, OAuth — from a single CR.
  name: Docling Kubernetes Operator
  slug: docling-operator
- description: A Java API for Docling that lets JVM applications call into the Docling pipeline. Complementary to `docling4j`, which targets Java-native document understanding integrations.
  name: Docling Java Bindings
  slug: docling-java
- description: Brings Docling document understanding into Java projects with idiomatic Java APIs over the Docling serialization format.
  name: Docling4j
  slug: docling4j
- description: TypeScript/JavaScript types and helpers for consuming Docling output (DoclingDocument JSON, DocTags) in Node.js and browser applications.
  name: Docling TypeScript
  slug: docling-ts
- description: First-party LangChain document loader and chunker for Docling. Drops Docling output directly into LangChain retrieval pipelines.
  name: Docling LangChain Integration
  slug: docling-langchain
- description: Shared job-runner primitives used by Docling Serve and the Docling Operator to dispatch conversion work across RQ workers and Ray.
  name: Docling Jobkit
  slug: docling-jobkit
- description: Asynchronous conversion submission.
  name: Docling Async API
  slug: docling-async-api
- description: Document conversion operations.
  name: Docling Convert API
  slug: docling-convert-api
- description: Health and metadata.
  name: Docling System API
  slug: docling-system-api
- description: Task status, results, and streaming.
  name: Docling Tasks API
  slug: docling-tasks-api
artifact_total: 49
collections:
- collection_type: open
  name: Docling CLI as REST
  slug: open-docling-cli
- collection_type: open
  name: Docling Serve REST API
  slug: open-docling-serve
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/docling-agentic-access.yml
- group: start
  title: ''
  type: Portal
  url: https://docling-project.github.io/docling/
- group: docs
  title: ''
  type: Documentation
  url: https://docling-project.github.io/docling/
- group: start
  title: ''
  type: GettingStarted
  url: https://docling-project.github.io/docling/getting_started/quickstart/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/docling-project/docling
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docling-project
- group: commercial
  title: ''
  type: License
  url: https://github.com/docling-project/docling/blob/main/LICENSE
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/docling/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/docling-core/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/docling-serve/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/docling-project/docling-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/docling-project/docling4j
- group: build
  title: ''
  type: SDKs
  url: https://github.com/docling-project/docling-ts
- group: build
  title: ''
  type: CLI
  url: https://docling-project.github.io/docling/reference/cli/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/docling-project/docling/releases
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/docling-project/docling/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: Issues
  url: https://github.com/docling-project/docling/issues
- group: operate
  title: ''
  type: Forums
  url: https://github.com/docling-project/docling/discussions
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/docling-project/docling/blob/main/CONTRIBUTING.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/docling-project/docling/blob/main/CODE_OF_CONDUCT.md
- group: other
  title: ''
  type: Governance
  url: https://lfaidata.foundation/projects/docling/
- group: other
  title: ''
  type: Foundation
  url: https://lfaidata.foundation/
- group: other
  title: ''
  type: Models
  url: https://huggingface.co/ds4sd
- group: other
  title: ''
  type: Models
  url: https://huggingface.co/ibm-granite/granite-docling-258M
- group: company
  title: ''
  type: Blog
  url: https://research.ibm.com/blog/docling-generative-AI
- group: other
  title: ''
  type: AcademicPaper
  url: https://arxiv.org/abs/2408.09869
- group: other
  title: ''
  type: ContainerImage
  url: https://quay.io/repository/docling-project/docling-serve
- group: other
  title: ''
  type: ContainerImage
  url: https://github.com/docling-project/docling-serve/pkgs/container/docling-serve
- group: other
  title: ''
  type: KubernetesOperator
  url: https://github.com/docling-project/docling-operator
created: '2026-05-25T00:00:00.000Z'
description: Docling is an open-source toolkit for parsing diverse document formats — PDF, DOCX, PPTX, XLSX, HTML, images, audio, LaTeX, plain text — into a unified, lossless DoclingDocument representation that downstream generative AI and RAG systems can consume directly. It pairs IBM Research's DocLayout and TableFormer models with the GraniteDocling visual language model and pluggable OCR engines, runs entirely locally for air-gapped use, and ships as a Python library and CLI, a FastAPI HTTP service (docling-serve), an MCP server (docling-mcp), and a Kubernetes operator. Originally created by IBM Research Zurich; now hosted by the LF AI and Data Foundation under the MIT license.
examples:
- key_count: 3
  name: Docling Cli Convert Example
  slug: docling-cli-convert-example
- key_count: 3
  name: Docling Serve Convert Source Async Example
  slug: docling-serve-convert-source-async-example
- key_count: 2
  name: Docling Serve Convert Source Example
  slug: docling-serve-convert-source-example
features:
- Parses PDF, DOCX, PPTX, XLSX, HTML, PNG/TIFF/JPEG, WAV/MP3, WebVTT, LaTeX, and plain text
- Unified DoclingDocument representation with lossless JSON, Markdown, HTML, DocTags, and WebVTT exports
- Advanced PDF understanding — page layout, reading order, table structure, code, formulas, image classification
- TableFormer model for accurate table structure recognition
- GraniteDocling-258M visual language model pipeline for image-first document understanding
- OCR engines — EasyOCR, Tesseract, RapidOCR, Mac OCR — with per-language configuration
- Automatic Speech Recognition (ASR) for audio inputs (WAV, MP3) producing WebVTT
- Local, air-gapped execution — no data leaves the host
- MCP server (docling-mcp) exposes parsing as agent tools for Claude, Cursor, Gemini and other clients
- Docling Serve HTTP API with sync and async endpoints, WebSocket task streaming, and zip-bundle output
- Kubernetes-native deployment via the Docling Operator (model-cache PVCs, RQ workers, GPU pools, OAuth, sticky sessions)
- Plug-and-play integrations with LangChain, LlamaIndex, Haystack, Crew AI, txtai, Bee, spaCy
- Application-specific XML schemas (USPTO, JATS, XBRL)
- Knowledge-graph extraction via docling-graph
- Synthetic data generation via docling-sdg for fine-tuning
- End-to-end evaluation framework (docling-eval) with standard datasets and metrics
- Java, Java-native, TypeScript, and Swift (docling-snap) bindings
- Open-source MIT license, governed by the LF AI and Data Foundation
- Originated at IBM Research Zurich (AI for Knowledge team)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docling.png
json_schemas:
- name: DoclingConvertRequest
  property_count: 4
  slug: docling-convert-request
- name: DoclingDocument
  property_count: 12
  slug: docling-document
json_structures:
- name: Docling Document Structure
  property_count: 0
  slug: docling-document-structure
jsonld:
- class_count: 0
  name: Docling Context
  property_count: 12
  slug: docling-context
layout: provider
modified: '2026-05-25'
name: Docling
nav: Providers
network: true
overview: 'Docling publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Async API, Convert API, System API, and 1 more. Tagged areas include Documents, Parsing, PDF, OCR, and Layout.


  The Docling catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Docling''s developer surface includes developer portal, documentation, getting-started guide, CLI, release notes, changelog, engineering blog, and 22 more developer resources.'
random_paper: 22
rules:
- name: Docling API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: docling-jsonschema-spectral-rules
- name: Docling API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: docling-rules
score:
  band: thin
  composite: 44.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 61.1
    developer_ergonomics: 52.2
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 44.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docling/refs/heads/main/screenshots/docling-2026-06-20T180109.png
slug: docling
tags:
- Documents
- Parsing
- PDF
- OCR
- Layout
- Tables
- RAG
- LLM
- Open Source
- IBM Research
- LF AI and Data
- MCP
- Knowledge Graph
- Generative AI
website: https://docling-project.github.io/docling/
---
