---
aid: apache-opennlp
name: Apache OpenNLP
description: Apache OpenNLP is a machine learning based toolkit for the processing of natural language text. It supports common NLP tasks such as tokenization, sentence segmentation, part-of-speech tagging, named entity extraction, chunking, parsing, and coreference resolution.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Machine Learning
  - Natural Language Processing
  - NLP
  - Text Processing
  - Apache
  - Open Source
  - Java
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-opennlp/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-opennlp:apache-opennlp
    name: Apache OpenNLP
    description: OpenNLP provides a Java API for NLP tasks including tokenization, sentence detection, POS tagging, named entity recognition, chunking, parsing, and language detection, with support for training custom models.
    humanURL: https://opennlp.apache.org/docs/
    tags:
      - Java
      - NLP
      - Text Processing
      - Apache
      - Open Source
      - Machine Learning
    properties:
      - type: Documentation
        url: https://opennlp.apache.org/docs/
      - type: OpenAPI
        url: openapi/apache-opennlp-tools.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/opennlp
  - type: Documentation
    url: https://opennlp.apache.org/
  - type: GettingStarted
    url: https://opennlp.apache.org/docs/
  - type: SpectralRules
    url: rules/apache-opennlp-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-opennlp-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/nlp-pipeline-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-opennlp-context.jsonld
  - type: Features
    data:
      - name: Language Detection
        description: Detects document language using ISO-639-3 classification
      - name: Sentence Detection
        description: Splits text into individual sentences with character offsets
      - name: Tokenization
        description: Segments text into words and punctuation with position tracking
      - name: Named Entity Recognition
        description: Detects persons, locations, organizations, and other named entities
      - name: POS Tagging
        description: Assigns Penn Treebank POS tags to each token
      - name: Lemmatization
        description: Reduces tokens to their dictionary base forms
      - name: Chunking
        description: Identifies noun phrases, verb phrases, and other syntactic chunks
      - name: Parsing
        description: Builds full syntactic parse trees using constituency parsing
      - name: Document Categorization
        description: Classifies documents into predefined categories
      - name: Custom Model Training
        description: Train custom models with Maxent, Perceptron, or Naive Bayes algorithms
  - type: UseCases
    data:
      - name: Information Extraction
        description: Extract structured data from unstructured text documents
      - name: Text Classification
        description: Automatically categorize documents by topic or sentiment
      - name: Search Enhancement
        description: Improve search relevance with NLP-based query processing
      - name: Content Analysis
        description: Analyze large text corpora for entities, topics, and patterns
      - name: Chatbot Development
        description: Build conversational AI with NLP intent and entity extraction
  - type: Integrations
    data:
      - name: Apache Solr
        description: Integrate OpenNLP with Apache Solr for NLP-enhanced search
      - name: Apache Lucene
        description: Use OpenNLP analyzers in Lucene text processing pipelines
      - name: Apache Flink
        description: Real-time NLP processing with Apache Flink data streams
      - name: UIMA
        description: Apache UIMA framework integration for unstructured information analysis
      - name: Maven/Gradle
        description: Available on Maven Central for Java build system integration
---
