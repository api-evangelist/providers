---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Apache Tika Agentic Access
  operation_count: 33
  slug: apache-tika-agentic-access
  summary_line: 33 operations · 23 acting
api_count: 13
apis:
- description: The Tika Java API provides the AutoDetectParser for automatic format detection and parsing, Metadata class for reading extracted metadata fields, ContentHandler for streaming SAX-based text extraction
  name: Apache Tika Java API
  slug: apache-tika-java-api
- description: The Apache Tika Server REST API API from Apache Tika — 1 operation(s) for apache tika server rest api.
  name: Apache Tika Apache Tika Server REST API API
  slug: apache-tika-apache-tika-server-rest-api-api
- description: The Detect API from Apache Tika — 1 operation(s) for detect.
  name: Apache Tika Detect API
  slug: apache-tika-detect-api
- description: The Detectors API from Apache Tika — 1 operation(s) for detectors.
  name: Apache Tika Detectors API
  slug: apache-tika-detectors-api
- description: The Language API from Apache Tika — 2 operation(s) for language.
  name: Apache Tika Language API
  slug: apache-tika-language-api
- description: The Meta API from Apache Tika — 3 operation(s) for meta.
  name: Apache Tika Meta API
  slug: apache-tika-meta-api
- description: The Mime Types API from Apache Tika — 1 operation(s) for mime types.
  name: Apache Tika Mime Types API
  slug: apache-tika-mime-types-api
- description: The Parsers API from Apache Tika — 2 operation(s) for parsers.
  name: Apache Tika Parsers API
  slug: apache-tika-parsers-api
- description: The Rmeta API from Apache Tika — 5 operation(s) for rmeta.
  name: Apache Tika Rmeta API
  slug: apache-tika-rmeta-api
- description: The Status API from Apache Tika — 1 operation(s) for status.
  name: Apache Tika Status API
  slug: apache-tika-status-api
- description: The Tika API from Apache Tika — 4 operation(s) for tika.
  name: Apache Tika Tika API
  slug: apache-tika-tika-api
- description: The Translate API from Apache Tika — 2 operation(s) for translate.
  name: Apache Tika Translate API
  slug: apache-tika-translate-api
- description: The Unpack API from Apache Tika — 2 operation(s) for unpack.
  name: Apache Tika Unpack API
  slug: apache-tika-unpack-api
artifact_total: 36
collections:
- collection_type: open
  name: Apache Tika Server REST API
  slug: open-apache-tika
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-tika-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-tika-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-tika-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/tika
- group: docs
  title: ''
  type: Documentation
  url: https://tika.apache.org/
- group: start
  title: ''
  type: Portal
  url: https://tika.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://tika.apache.org/gettingstarted.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/tika/releases
- group: operate
  title: ''
  type: Support
  url: https://cwiki.apache.org/confluence/display/TIKA/MailingLists
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: build
  title: Python Tika Package
  type: SDKs
  url: https://pypi.org/project/tika/
created: '2026-03-16'
description: Apache Tika is a toolkit for detecting and extracting metadata and structured text content from over 1,000 file formats including PDF, Microsoft Office (Word, Excel, PowerPoint), OpenDocument, HTML, XML, images, audio, video, and archive formats. Tika provides a REST API server, Java library, and command-line tool. It is used by Apache Solr, Apache Nutch, and many other systems for content extraction and indexing. It is maintained by the Apache Software Foundation.
features:
- description: Detect and extract content from over 1,000 file formats using parser plugins.
  name: 1000+ Format Support
- description: Extract document metadata including author, creation date, title, and format-specific properties.
  name: Metadata Extraction
- description: Automatic language detection from extracted text content.
  name: Language Detection
- description: Accurate MIME type detection based on file content (magic bytes) not just file extension.
  name: MIME Type Detection
- description: Standalone HTTP server for document processing without Java library dependency.
  name: REST Server
- description: Optional Tesseract OCR integration for text extraction from images and scanned PDFs.
  name: OCR Integration
- description: Recursive parsing of archive formats (ZIP, TAR, JAR) and embedded documents.
  name: Recursive Parsing
finops:
- name: Apache Tika Finops
  service_category: API
  slug: apache-tika-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-tika.png
integrations:
- description: Solr Cell uses Tika for extracting text from uploaded documents for indexing.
  name: Apache Solr
- description: Nutch web crawler uses Tika for parsing fetched web page content.
  name: Apache Nutch
- description: Ingest attachment processor uses Tika for document content extraction.
  name: Elasticsearch
- description: Optional Tesseract integration for OCR on images and scanned documents.
  name: Tesseract OCR
- description: NiFi processor integration for automated document parsing workflows.
  name: Apache NiFi
layout: provider
modified: '2026-05-19'
name: Apache Tika
nav: Providers
network: true
overview: 'Apache Tika publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Apache Tika Server REST API API, Detect API, Detectors API, and 9 more. Tagged areas include Content Extraction, Document Processing, Metadata, Text Extraction, and Open Source.


  Apache Tika''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, and 6 more developer resources.'
plans:
- name: Apache Tika Plans Pricing
  plan_count: 3
  slug: apache-tika-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Apache Tika Rate Limits
  slug: apache-tika-rate-limits
score:
  band: thin
  composite: 38.9
  delta: -2.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 33.9
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-tika/refs/heads/main/screenshots/apache-tika-2026-06-20T172153.png
security:
- kind: domain-security
  name: Apache Tika Domain Security
  slug: apache-tika-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Tika Vulnerability Disclosure
  slug: apache-tika-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-tika
tags:
- Content Extraction
- Document Processing
- Metadata
- Text Extraction
- Open Source
use_cases:
- description: Extract text from documents for indexing in Apache Solr or Elasticsearch.
  name: Search Indexing
- description: Automated metadata extraction and classification for document management systems.
  name: Document Intelligence
- description: Batch content extraction during digital archive migration and transformation.
  name: Content Migration
- description: Legal e-discovery content extraction from diverse document collections.
  name: E-Discovery
website: https://tika.apache.org/
---
