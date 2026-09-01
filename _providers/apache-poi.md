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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Apache Poi Agentic Access
  operation_count: 11
  slug: apache-poi-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 1
apis:
- description: The Conversion API from Apache POI — 1 operation(s) for conversion.
  name: Apache POI Conversion API
  slug: apache-poi-conversion-api
- description: The Excel API from Apache POI — 4 operation(s) for excel.
  name: Apache POI Excel API
  slug: apache-poi-excel-api
- description: The PowerPoint API from Apache POI — 2 operation(s) for powerpoint.
  name: Apache POI PowerPoint API
  slug: apache-poi-powerpoint-api
- description: The Word API from Apache POI — 2 operation(s) for word.
  name: Apache POI Word API
  slug: apache-poi-word-api
artifact_total: 81
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache POI Conversion API
  slug: open-apache-poi-conversion-api
- collection_type: open
  name: Apache POI Conversion Excel API
  slug: open-apache-poi-excel-api
- collection_type: open
  name: Apache POI Conversion PowerPoint API
  slug: open-apache-poi-powerpoint-api
- collection_type: open
  name: Apache POI Conversion Word API
  slug: open-apache-poi-word-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-poi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-poi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-poi-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/poi
- group: docs
  title: ''
  type: Documentation
  url: https://poi.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-poi-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-poi-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-poi-context.jsonld
created: '2026-03-16'
description: Apache POI is a Java API for manipulating various file formats based upon the Office Open XML standards (OOXML) and Microsoft's OLE2 Compound Document format (OLE2). It supports reading and writing Excel, Word, PowerPoint, Visio, and Outlook files.
examples:
- key_count: 2
  name: Apache Poi Cell Data Example
  slug: apache-poi-cell-data-example
- key_count: 4
  name: Apache Poi Cell Example
  slug: apache-poi-cell-example
- key_count: 3
  name: Apache Poi Conversion Request Example
  slug: apache-poi-conversion-request-example
- key_count: 4
  name: Apache Poi Conversion Result Example
  slug: apache-poi-conversion-result-example
- key_count: 5
  name: Apache Poi Document Example
  slug: apache-poi-document-example
- key_count: 3
  name: Apache Poi Document Request Example
  slug: apache-poi-document-request-example
- key_count: 3
  name: Apache Poi Paragraph Example
  slug: apache-poi-paragraph-example
- key_count: 4
  name: Apache Poi Presentation Example
  slug: apache-poi-presentation-example
- key_count: 3
  name: Apache Poi Presentation Request Example
  slug: apache-poi-presentation-request-example
- key_count: 4
  name: Apache Poi Shape Example
  slug: apache-poi-shape-example
- key_count: 4
  name: Apache Poi Sheet Example
  slug: apache-poi-sheet-example
- key_count: 1
  name: Apache Poi Sheet List Example
  slug: apache-poi-sheet-list-example
- key_count: 3
  name: Apache Poi Slide Example
  slug: apache-poi-slide-example
- key_count: 5
  name: Apache Poi Workbook Example
  slug: apache-poi-workbook-example
- key_count: 2
  name: Apache Poi Workbook List Example
  slug: apache-poi-workbook-list-example
- key_count: 3
  name: Apache Poi Workbook Request Example
  slug: apache-poi-workbook-request-example
features:
- description: Read and write Excel files in legacy XLS (HSSF) and modern XLSX (XSSF) formats
  name: Excel HSSF/XSSF
- description: Read and write Word documents in legacy DOC (HWPF) and modern DOCX (XWPF) formats
  name: Word HWPF/XWPF
- description: Create and manipulate PowerPoint presentations in PPT and PPTX formats
  name: PowerPoint HSLF/XSLF
- description: Evaluate Excel formulas and compute cell values programmatically
  name: Formula Evaluation
- description: Low-memory streaming API (SXSSF) for writing large Excel files
  name: Streaming API
- description: Create and modify charts in Excel workbooks and PowerPoint slides
  name: Chart Support
- description: Sign Office documents with digital signatures using OOXML standards
  name: Digital Signatures
finops:
- name: Apache Poi Finops
  service_category: API
  slug: apache-poi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-poi.png
integrations:
- description: POI is used by Tika for Office document text extraction
  name: Apache Tika
- description: Integrate POI with Spring Boot for web-based document generation
  name: Spring Framework
- description: Available as org.apache.poi artifacts on Maven Central
  name: Maven Central
- description: Uses Commons Collections and Commons Math for data structures
  name: Apache Commons
json_schemas:
- name: CellData
  property_count: 2
  slug: apache-poi-cell-data
- name: Cell
  property_count: 4
  slug: apache-poi-cell
- name: ConversionRequest
  property_count: 3
  slug: apache-poi-conversion-request
- name: ConversionResult
  property_count: 4
  slug: apache-poi-conversion-result
- name: DocumentRequest
  property_count: 3
  slug: apache-poi-document-request
- name: Document
  property_count: 5
  slug: apache-poi-document
- name: Paragraph
  property_count: 3
  slug: apache-poi-paragraph
- name: PresentationRequest
  property_count: 3
  slug: apache-poi-presentation-request
- name: Presentation
  property_count: 4
  slug: apache-poi-presentation
- name: Shape
  property_count: 4
  slug: apache-poi-shape
- name: SheetList
  property_count: 1
  slug: apache-poi-sheet-list
- name: Sheet
  property_count: 4
  slug: apache-poi-sheet
- name: Slide
  property_count: 3
  slug: apache-poi-slide
- name: WorkbookList
  property_count: 2
  slug: apache-poi-workbook-list
- name: WorkbookRequest
  property_count: 3
  slug: apache-poi-workbook-request
- name: Workbook
  property_count: 5
  slug: apache-poi-workbook
json_structures:
- name: Apache Poi Cell Data Structure
  property_count: 2
  slug: apache-poi-cell-data-structure
- name: Apache Poi Cell Structure
  property_count: 4
  slug: apache-poi-cell-structure
- name: Apache Poi Conversion Request Structure
  property_count: 3
  slug: apache-poi-conversion-request-structure
- name: Apache Poi Conversion Result Structure
  property_count: 4
  slug: apache-poi-conversion-result-structure
- name: Apache Poi Document Request Structure
  property_count: 3
  slug: apache-poi-document-request-structure
- name: Apache Poi Document Structure
  property_count: 5
  slug: apache-poi-document-structure
- name: Apache Poi Paragraph Structure
  property_count: 3
  slug: apache-poi-paragraph-structure
- name: Apache Poi Presentation Request Structure
  property_count: 3
  slug: apache-poi-presentation-request-structure
- name: Apache Poi Presentation Structure
  property_count: 4
  slug: apache-poi-presentation-structure
- name: Apache Poi Shape Structure
  property_count: 4
  slug: apache-poi-shape-structure
- name: Apache Poi Sheet List Structure
  property_count: 1
  slug: apache-poi-sheet-list-structure
- name: Apache Poi Sheet Structure
  property_count: 4
  slug: apache-poi-sheet-structure
- name: Apache Poi Slide Structure
  property_count: 3
  slug: apache-poi-slide-structure
- name: Apache Poi Workbook List Structure
  property_count: 2
  slug: apache-poi-workbook-list-structure
- name: Apache Poi Workbook Request Structure
  property_count: 3
  slug: apache-poi-workbook-request-structure
- name: Apache Poi Workbook Structure
  property_count: 5
  slug: apache-poi-workbook-structure
jsonld:
- class_count: 16
  name: Apache Poi Context
  property_count: 31
  slug: apache-poi-context
layout: provider
modified: '2026-05-19'
name: Apache POI
nav: Providers
network: true
overview: 'Apache POI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Conversion API, Excel API, PowerPoint API, and 1 more. Tagged areas include Document Processing, Excel, Java, Microsoft Office, and PowerPoint.


  The Apache POI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache POI''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Apache Poi Plans Pricing
  plan_count: 3
  slug: apache-poi-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Apache Poi Rate Limits
  slug: apache-poi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache POI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-poi-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Apache POI API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: apache-poi-spectral-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 52.9
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-poi/refs/heads/main/screenshots/apache-poi-2026-06-20T172135.png
security:
- kind: domain-security
  name: Apache Poi Domain Security
  slug: apache-poi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Poi Vulnerability Disclosure
  slug: apache-poi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-poi
tags:
- Document Processing
- Excel
- Java
- Microsoft Office
- PowerPoint
- Word
- Apache
- Open-Source
use_cases:
- description: Generate Excel and Word reports programmatically from application data
  name: Report Generation
- description: Import data from Excel spreadsheets and export results back
  name: Data Import/Export
- description: Fill Office document templates with dynamic data
  name: Template Processing
- description: Convert between legacy Office formats and modern OOXML formats
  name: Document Conversion
---
