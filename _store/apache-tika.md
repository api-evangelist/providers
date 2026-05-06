---
aid: apache-tika
name: Apache Tika
description: Apache Tika is a toolkit for detecting and extracting metadata and structured text content from over 1,000 file formats including PDF, Microsoft Office (Word, Excel, PowerPoint), OpenDocument, HTML, XML, images, audio, video, and archive formats. Tika provides a REST API server, Java library, and command-line tool. It is used by Apache Solr, Apache Nutch, and many other systems for content extraction and indexing. It is maintained by the Apache Software Foundation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Content Extraction
  - Document Processing
  - Metadata
  - Text Extraction
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-tika/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-tika:apache-tika-rest-api
    name: Apache Tika REST API
    description: 'The Tika Server REST API provides HTTP endpoints for content type detection, text extraction, metadata extraction, and language detection from uploaded documents. Key endpoints include: PUT /tika for full text extraction, PUT /meta for metadata-only extraction, PUT /detect/stream for MIME type detection, PUT /language/stream for language detection, and GET /parsers for listing available parsers. The server supports streaming large files and returns JSON or plain text responses.'
    humanURL: https://cwiki.apache.org/confluence/display/TIKA/TikaServer
    tags:
      - REST
      - Content Extraction
      - Metadata
      - Document Processing
      - Text Extraction
    properties:
      - type: Documentation
        url: https://cwiki.apache.org/confluence/display/TIKA/TikaServer
      - type: Documentation
        url: https://tika.apache.org/
  - aid: apache-tika:apache-tika-java-api
    name: Apache Tika Java API
    description: The Tika Java API provides the AutoDetectParser for automatic format detection and parsing, Metadata class for reading extracted metadata fields, ContentHandler for streaming SAX-based text extraction, and Detector for MIME type identification. The facade Tika class provides a simple one-line API for text extraction from any supported format.
    humanURL: https://tika.apache.org/
    tags:
      - Java
      - Content Extraction
      - Parser
      - Metadata
    properties:
      - type: Documentation
        url: https://tika.apache.org/
      - type: APIReference
        url: https://tika.apache.org/1.28/api/
      - type: SDK
        url: https://search.maven.org/search?q=org.apache.tika
        title: Maven Java SDK
common:
  - type: GitHubRepository
    url: https://github.com/apache/tika
  - type: Documentation
    url: https://tika.apache.org/
  - type: Portal
    url: https://tika.apache.org/
  - type: GettingStarted
    url: https://tika.apache.org/gettingstarted.html
  - type: ReleaseNotes
    url: https://github.com/apache/tika/releases
  - type: Support
    url: https://cwiki.apache.org/confluence/display/TIKA/MailingLists
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: SDK
    url: https://pypi.org/project/tika/
    title: Python Tika Package
  - type: Features
    data:
      - name: 1000+ Format Support
        description: Detect and extract content from over 1,000 file formats using parser plugins.
      - name: Metadata Extraction
        description: Extract document metadata including author, creation date, title, and format-specific properties.
      - name: Language Detection
        description: Automatic language detection from extracted text content.
      - name: MIME Type Detection
        description: Accurate MIME type detection based on file content (magic bytes) not just file extension.
      - name: REST Server
        description: Standalone HTTP server for document processing without Java library dependency.
      - name: OCR Integration
        description: Optional Tesseract OCR integration for text extraction from images and scanned PDFs.
      - name: Recursive Parsing
        description: Recursive parsing of archive formats (ZIP, TAR, JAR) and embedded documents.
  - type: UseCases
    data:
      - name: Search Indexing
        description: Extract text from documents for indexing in Apache Solr or Elasticsearch.
      - name: Document Intelligence
        description: Automated metadata extraction and classification for document management systems.
      - name: Content Migration
        description: Batch content extraction during digital archive migration and transformation.
      - name: E-Discovery
        description: Legal e-discovery content extraction from diverse document collections.
  - type: Integrations
    data:
      - name: Apache Solr
        description: Solr Cell uses Tika for extracting text from uploaded documents for indexing.
      - name: Apache Nutch
        description: Nutch web crawler uses Tika for parsing fetched web page content.
      - name: Elasticsearch
        description: Ingest attachment processor uses Tika for document content extraction.
      - name: Tesseract OCR
        description: Optional Tesseract integration for OCR on images and scanned documents.
      - name: Apache NiFi
        description: NiFi processor integration for automated document parsing workflows.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
