---
aid: apache-pdfbox
name: Apache PDFBox
description: Apache PDFBox is an open-source Java library for working with PDF documents. It allows creation of new PDF documents, manipulation of existing documents, and the ability to extract content from documents with support for digital signatures.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Document Processing
  - Java
  - PDF
  - Text Extraction
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-pdfbox/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-pdfbox:apache-pdfbox
    name: Apache PDFBox
    description: PDFBox provides a Java API for creating, manipulating, rendering, and extracting text and images from PDF documents, with support for digital signatures, form filling, PDF/A validation, and font handling.
    humanURL: https://pdfbox.apache.org/2.0/getting-started.html
    tags:
      - Document Processing
      - Java
      - PDF
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://pdfbox.apache.org/2.0/getting-started.html
      - type: OpenAPI
        url: openapi/apache-pdfbox-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/pdfbox
  - type: Documentation
    url: https://pdfbox.apache.org/
  - type: SpectralRules
    url: rules/apache-pdfbox-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-pdfbox-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/pdfbox-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-pdfbox-context.jsonld
  - type: Features
    data:
      - name: PDF Text Extraction
        description: Extract plain text and structured content from PDF documents
      - name: PDF Creation
        description: Create new PDF documents programmatically with Java API
      - name: PDF Manipulation
        description: Merge, split, rotate, and resize pages in existing PDFs
      - name: Digital Signatures
        description: Apply and verify digital signatures for document authenticity
      - name: Form Filling
        description: Read and fill interactive PDF forms (AcroForms)
      - name: PDF/A Validation
        description: Validate and create PDF/A documents for archiving
      - name: Font Handling
        description: Embed and extract fonts, handle Type 1, TrueType, and OpenType
  - type: UseCases
    data:
      - name: Invoice Processing
        description: Extract data from PDF invoices for automated processing
      - name: Document Generation
        description: Generate PDF reports, contracts, and certificates programmatically
      - name: Legal Document Management
        description: Digitally sign and verify legal documents
      - name: Form Data Collection
        description: Fill PDF forms and extract submitted data
      - name: Archive Management
        description: Convert documents to PDF/A for long-term archiving
  - type: Integrations
    data:
      - name: Apache Tika
        description: Content detection and text extraction integration
      - name: Spring Boot
        description: Spring Boot starter for PDF processing in web applications
      - name: Maven Central
        description: Available as org.apache.pdfbox on Maven Central
      - name: iText/OpenPDF
        description: Complementary PDF library for advanced PDF generation
---
