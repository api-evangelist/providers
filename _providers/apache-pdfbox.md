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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Apache Pdfbox Agentic Access
  operation_count: 8
  slug: apache-pdfbox-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 5
apis:
- baseURL_template: https://{host}/pdfbox
  baseurl_source: spec_template
  description: The Documents API from Apache PDFBox — 3 operation(s) for documents.
  name: Apache PDFBox Documents API
  slug: apache-pdfbox-documents-api
- baseURL_template: https://{host}/pdfbox
  baseurl_source: spec_template
  description: The Forms API from Apache PDFBox — 1 operation(s) for forms.
  name: Apache PDFBox Forms API
  slug: apache-pdfbox-forms-api
- baseURL_template: https://{host}/pdfbox
  baseurl_source: spec_template
  description: The Operations API from Apache PDFBox — 2 operation(s) for operations.
  name: Apache PDFBox Operations API
  slug: apache-pdfbox-operations-api
- baseURL_template: https://{host}/pdfbox
  baseurl_source: spec_template
  description: The Pages API from Apache PDFBox — 1 operation(s) for pages.
  name: Apache PDFBox Pages API
  slug: apache-pdfbox-pages-api
- baseURL_template: https://{host}/pdfbox
  baseurl_source: spec_template
  description: The Signatures API from Apache PDFBox — 1 operation(s) for signatures.
  name: Apache PDFBox Signatures API
  slug: apache-pdfbox-signatures-api
artifact_total: 69
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache PDFBox Documents API
  slug: open-apache-pdfbox-documents-api
- collection_type: open
  name: Apache PDFBox Documents Forms API
  slug: open-apache-pdfbox-forms-api
- collection_type: open
  name: Apache PDFBox Documents Operations API
  slug: open-apache-pdfbox-operations-api
- collection_type: open
  name: Apache PDFBox Documents Pages API
  slug: open-apache-pdfbox-pages-api
- collection_type: open
  name: Apache PDFBox Documents Signatures API
  slug: open-apache-pdfbox-signatures-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-pdfbox-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-pdfbox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-pdfbox-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/pdfbox
- group: docs
  title: ''
  type: Documentation
  url: https://pdfbox.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-pdfbox-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-pdfbox-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-pdfbox-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://pdfbox.apache.org/blog/
created: '2026-03-16'
description: Apache PDFBox is an open-source Java library for working with PDF documents. It allows creation of new PDF documents, manipulation of existing documents, and the ability to extract content from documents with support for digital signatures.
examples:
- key_count: 3
  name: Apache Pdfbox Create Document Request Example
  slug: apache-pdfbox-create-document-request-example
- key_count: 5
  name: Apache Pdfbox Document Info Example
  slug: apache-pdfbox-document-info-example
- key_count: 7
  name: Apache Pdfbox Document Metadata Example
  slug: apache-pdfbox-document-metadata-example
- key_count: 4
  name: Apache Pdfbox Form Field Example
  slug: apache-pdfbox-form-field-example
- key_count: 2
  name: Apache Pdfbox Form Fields Example
  slug: apache-pdfbox-form-fields-example
- key_count: 2
  name: Apache Pdfbox Merge Request Example
  slug: apache-pdfbox-merge-request-example
- key_count: 4
  name: Apache Pdfbox Page Info Example
  slug: apache-pdfbox-page-info-example
- key_count: 3
  name: Apache Pdfbox Page List Example
  slug: apache-pdfbox-page-list-example
- key_count: 4
  name: Apache Pdfbox Sign Request Example
  slug: apache-pdfbox-sign-request-example
- key_count: 1
  name: Apache Pdfbox Split Request Example
  slug: apache-pdfbox-split-request-example
- key_count: 4
  name: Apache Pdfbox Text Extraction Result Example
  slug: apache-pdfbox-text-extraction-result-example
features:
- description: Extract plain text and structured content from PDF documents
  name: PDF Text Extraction
- description: Create new PDF documents programmatically with Java API
  name: PDF Creation
- description: Merge, split, rotate, and resize pages in existing PDFs
  name: PDF Manipulation
- description: Apply and verify digital signatures for document authenticity
  name: Digital Signatures
- description: Read and fill interactive PDF forms (AcroForms)
  name: Form Filling
- description: Validate and create PDF/A documents for archiving
  name: PDF/A Validation
- description: Embed and extract fonts, handle Type 1, TrueType, and OpenType
  name: Font Handling
finops:
- name: Apache Pdfbox Finops
  service_category: API
  slug: apache-pdfbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-pdfbox.png
integrations:
- description: Content detection and text extraction integration
  name: Apache Tika
- description: Spring Boot starter for PDF processing in web applications
  name: Spring Boot
- description: Available as org.apache.pdfbox on Maven Central
  name: Maven Central
- description: Complementary PDF library for advanced PDF generation
  name: iText/OpenPDF
json_schemas:
- name: CreateDocumentRequest
  property_count: 3
  slug: apache-pdfbox-create-document-request
- name: DocumentInfo
  property_count: 5
  slug: apache-pdfbox-document-info
- name: DocumentMetadata
  property_count: 7
  slug: apache-pdfbox-document-metadata
- name: FormField
  property_count: 4
  slug: apache-pdfbox-form-field
- name: FormFields
  property_count: 2
  slug: apache-pdfbox-form-fields
- name: MergeRequest
  property_count: 2
  slug: apache-pdfbox-merge-request
- name: PageInfo
  property_count: 4
  slug: apache-pdfbox-page-info
- name: PageList
  property_count: 3
  slug: apache-pdfbox-page-list
- name: SignRequest
  property_count: 4
  slug: apache-pdfbox-sign-request
- name: SplitRequest
  property_count: 1
  slug: apache-pdfbox-split-request
- name: TextExtractionResult
  property_count: 4
  slug: apache-pdfbox-text-extraction-result
json_structures:
- name: Apache Pdfbox Create Document Request Structure
  property_count: 3
  slug: apache-pdfbox-create-document-request-structure
- name: Apache Pdfbox Document Info Structure
  property_count: 5
  slug: apache-pdfbox-document-info-structure
- name: Apache Pdfbox Document Metadata Structure
  property_count: 7
  slug: apache-pdfbox-document-metadata-structure
- name: Apache Pdfbox Form Field Structure
  property_count: 4
  slug: apache-pdfbox-form-field-structure
- name: Apache Pdfbox Form Fields Structure
  property_count: 2
  slug: apache-pdfbox-form-fields-structure
- name: Apache Pdfbox Merge Request Structure
  property_count: 2
  slug: apache-pdfbox-merge-request-structure
- name: Apache Pdfbox Page Info Structure
  property_count: 4
  slug: apache-pdfbox-page-info-structure
- name: Apache Pdfbox Page List Structure
  property_count: 3
  slug: apache-pdfbox-page-list-structure
- name: Apache Pdfbox Sign Request Structure
  property_count: 4
  slug: apache-pdfbox-sign-request-structure
- name: Apache Pdfbox Split Request Structure
  property_count: 1
  slug: apache-pdfbox-split-request-structure
- name: Apache Pdfbox Text Extraction Result Structure
  property_count: 4
  slug: apache-pdfbox-text-extraction-result-structure
jsonld:
- class_count: 11
  name: Apache Pdfbox Context
  property_count: 32
  slug: apache-pdfbox-context
layout: provider
modified: '2026-05-19'
name: Apache PDFBox
nav: Providers
network: true
overview: 'Apache PDFBox publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Forms API, Operations API, and 2 more. Tagged areas include Document Processing, Java, PDF, Text Extraction, and Apache.


  The Apache PDFBox catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache PDFBox''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Pdfbox Plans Pricing
  plan_count: 3
  slug: apache-pdfbox-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Apache Pdfbox Rate Limits
  slug: apache-pdfbox-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache PDFBox API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-pdfbox-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Apache PDFBox API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 3
    warn: 4
  slug: apache-pdfbox-spectral-rules
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 19.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 21.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-pdfbox/refs/heads/main/screenshots/apache-pdfbox-2026-06-20T172133.png
security:
- kind: domain-security
  name: Apache Pdfbox Domain Security
  slug: apache-pdfbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Pdfbox Vulnerability Disclosure
  slug: apache-pdfbox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-pdfbox
tags:
- Document Processing
- Java
- PDF
- Text Extraction
- Apache
- Open-Source
use_cases:
- description: Extract data from PDF invoices for automated processing
  name: Invoice Processing
- description: Generate PDF reports, contracts, and certificates programmatically
  name: Document Generation
- description: Digitally sign and verify legal documents
  name: Legal Document Management
- description: Fill PDF forms and extract submitted data
  name: Form Data Collection
- description: Convert documents to PDF/A for long-term archiving
  name: Archive Management
---
