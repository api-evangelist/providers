---
aid: apache-poi
name: Apache POI
description: Apache POI is a Java API for manipulating various file formats based upon the Office Open XML standards (OOXML) and Microsoft's OLE2 Compound Document format (OLE2). It supports reading and writing Excel, Word, PowerPoint, Visio, and Outlook files.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Document Processing
  - Excel
  - Java
  - Microsoft Office
  - PowerPoint
  - Word
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-poi/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-poi:apache-poi
    name: Apache POI
    description: POI provides Java APIs for reading and writing Microsoft Office formats including Excel (HSSF/XSSF), Word (HWPF/XWPF), PowerPoint (HSLF/XSLF), Visio (HDGF/XDGF), and Outlook (HSMF), with support for formulas, charts, and formatting.
    humanURL: https://poi.apache.org/components/index.html
    tags:
      - Document Processing
      - Excel
      - Java
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://poi.apache.org/components/index.html
      - type: Documentation
        url: https://poi.apache.org/components/
      - type: OpenAPI
        url: openapi/apache-poi-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/poi
  - type: Documentation
    url: https://poi.apache.org/
  - type: SpectralRules
    url: rules/apache-poi-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-poi-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/poi-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-poi-context.jsonld
  - type: Features
    data:
      - name: Excel HSSF/XSSF
        description: Read and write Excel files in legacy XLS (HSSF) and modern XLSX (XSSF) formats
      - name: Word HWPF/XWPF
        description: Read and write Word documents in legacy DOC (HWPF) and modern DOCX (XWPF) formats
      - name: PowerPoint HSLF/XSLF
        description: Create and manipulate PowerPoint presentations in PPT and PPTX formats
      - name: Formula Evaluation
        description: Evaluate Excel formulas and compute cell values programmatically
      - name: Streaming API
        description: Low-memory streaming API (SXSSF) for writing large Excel files
      - name: Chart Support
        description: Create and modify charts in Excel workbooks and PowerPoint slides
      - name: Digital Signatures
        description: Sign Office documents with digital signatures using OOXML standards
  - type: UseCases
    data:
      - name: Report Generation
        description: Generate Excel and Word reports programmatically from application data
      - name: Data Import/Export
        description: Import data from Excel spreadsheets and export results back
      - name: Template Processing
        description: Fill Office document templates with dynamic data
      - name: Document Conversion
        description: Convert between legacy Office formats and modern OOXML formats
  - type: Integrations
    data:
      - name: Apache Tika
        description: POI is used by Tika for Office document text extraction
      - name: Spring Framework
        description: Integrate POI with Spring Boot for web-based document generation
      - name: Maven Central
        description: Available as org.apache.poi artifacts on Maven Central
      - name: Apache Commons
        description: Uses Commons Collections and Commons Math for data structures
---
