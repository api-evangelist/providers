---
aid: cloudmersive
url: https://raw.githubusercontent.com/api-evangelist/cloudmersive/refs/heads/main/apis.yml
name: Cloudmersive
tags:
  - Barcodes
  - Conversions
  - Documents
  - Image Recognition
  - Natural Language
  - OCR
  - Processing
  - Validation
  - Virus Scanning
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-13'
modified: '2026-04-26'
position: Consumer
x-type: company
x-company: Cloudmersive
description: Cloudmersive provides a portfolio of utility APIs covering virus and malware scanning, document conversion, OCR, image recognition, NLP, validation, security threat detection (spam, phishing, fraud, DLP, CDR), speech, video, barcode, currency, and data integration. Each API is documented with a Swagger 2.0 / OpenAPI specification, has SDKs in multiple languages, and is consumable on api.cloudmersive.com behind an API key (`Apikey` header).
apis:
  - aid: cloudmersive:cloudmersive-virus-scan-api
    name: Cloudmersive Virus Scan API
    tags:
      - Antivirus
      - Malware
      - Security
      - Virus Scanning
    humanURL: https://cloudmersive.com/virus-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Virus%20Scan%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/virus
        type: OpenAPI
      - url: openapi/cloudmersive-virus-scan-openapi.json
        type: OpenAPI
    description: Scan files and content for viruses, malware, executables, scripts, macros, password-protected files, and other content threats. Includes both basic and advanced (multi-engine) scan modes and a website scan.
  - aid: cloudmersive:cloudmersive-security-threat-detection-api
    name: Cloudmersive Security Threat Detection API
    tags:
      - Security
      - SQL Injection
      - Threat Detection
      - XSS
    humanURL: https://cloudmersive.com/security-threat-detection-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Security%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/security
        type: OpenAPI
    description: Detect SQL injection, XSS, XXE, SSRF, command injection, and other content-borne attacks against text and HTML inputs.
  - aid: cloudmersive:cloudmersive-spam-api
    name: Cloudmersive Spam Detection API
    tags:
      - Email
      - Spam
    humanURL: https://cloudmersive.com/spam-detection-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Spam%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/spam
        type: OpenAPI
    description: AI-powered spam detection for email and message content.
  - aid: cloudmersive:cloudmersive-phishing-api
    name: Cloudmersive Phishing Detection API
    tags:
      - Email Security
      - Phishing
    humanURL: https://cloudmersive.com/phishing-detection-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Phishing%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/phishing
        type: OpenAPI
    description: Detect phishing attempts in email content and URLs using AI scanning.
  - aid: cloudmersive:cloudmersive-cdr-api
    name: Cloudmersive Content Disarm and Reconstruction (CDR) API
    tags:
      - CDR
      - Document Sanitization
      - Security
    humanURL: https://cloudmersive.com/content-disarm-and-reconstruction-cdr-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=CDR%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/cdr
        type: OpenAPI
    description: Sanitize user documents by stripping macros, scripts, and other embedded threats while preserving usable content (Content Disarm and Reconstruction).
  - aid: cloudmersive:cloudmersive-fraud-api
    name: Cloudmersive Fraud Detection API
    tags:
      - Fraud Detection
      - Risk
    humanURL: https://cloudmersive.com/fraud-detection-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Fraud%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/fraud
        type: OpenAPI
    description: Document fraud and content security threat scanning.
  - aid: cloudmersive:cloudmersive-dlp-api
    name: Cloudmersive Data Loss Prevention (DLP) API
    tags:
      - Compliance
      - DLP
      - PII
    humanURL: https://cloudmersive.com/data-loss-prevention-dlp-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=DLP%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/dlp
        type: OpenAPI
    description: Detect and redact personally identifiable information (PII) and other sensitive data in text and documents.
  - aid: cloudmersive:cloudmersive-convert-api
    name: Cloudmersive Document Convert API
    tags:
      - Conversion
      - Documents
      - File Formats
    humanURL: https://cloudmersive.com/convert-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Convert%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/convert
        type: OpenAPI
    description: Convert files between many formats (DOCX/PDF/HTML/XLSX/PPTX/CSV/JSON/XML), take URL screenshots, edit documents, and process tabular data.
  - aid: cloudmersive:cloudmersive-barcode-api
    name: Cloudmersive Barcode API
    tags:
      - Barcode
      - QR Code
    humanURL: https://cloudmersive.com/barcode-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Barcode%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/barcode
        type: OpenAPI
    description: Generate and recognize barcodes including QR codes, EAN, UPC, Code 128, and more.
  - aid: cloudmersive:cloudmersive-image-api
    name: Cloudmersive Image Recognition and Processing API
    tags:
      - Computer Vision
      - Image Processing
      - Image Recognition
    humanURL: https://cloudmersive.com/image-recognition-and-processing-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Image%20Recognition%20and%20Processing%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/image
        type: OpenAPI
    description: 'Recognize and process images: classify, detect objects, NSFW detection, face detection, image editing, filters, and resizing.'
  - aid: cloudmersive:cloudmersive-nlp-api
    name: Cloudmersive Natural Language Processing API
    tags:
      - NLP
      - Sentiment Analysis
      - Translation
    humanURL: https://cloudmersive.com/natural-language-processing-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Natural%20Language%20Processing%20(NLP)%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/nlp
        type: OpenAPI
      - url: https://api-console.cloudmersive.com/swagger/api/nlpv2
        type: OpenAPI
    description: Tokenization, POS tagging, sentence splitting, language detection, translation, sentiment analysis, and rephrasing.
  - aid: cloudmersive:cloudmersive-ocr-api
    name: Cloudmersive OCR API
    tags:
      - Documents
      - OCR
    humanURL: https://cloudmersive.com/ocr-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Optical%20Character%20Recognition%20(OCR)%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/ocr
        type: OpenAPI
    description: Deep-learning-based OCR for images and PDFs, with form, receipt, and business-card extraction.
  - aid: cloudmersive:cloudmersive-speech-api
    name: Cloudmersive Speech API
    tags:
      - Speech
      - Speech Recognition
      - Text to Speech
    humanURL: https://cloudmersive.com/speech-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Speech%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/speech
        type: OpenAPI
    description: Speech-to-text and text-to-speech in multiple languages.
  - aid: cloudmersive:cloudmersive-validate-api
    name: Cloudmersive Validate API
    tags:
      - Email
      - Validation
    humanURL: https://cloudmersive.com/validate-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Validate%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/validate
        type: OpenAPI
    description: Validate emails, phone numbers, domains, IP addresses, addresses, and other inputs.
  - aid: cloudmersive:cloudmersive-video-api
    name: Cloudmersive Video API
    tags:
      - Conversion
      - Video
    humanURL: https://cloudmersive.com/video-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Video%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/video
        type: OpenAPI
    description: Convert, edit, and process video and audio files.
  - aid: cloudmersive:cloudmersive-currency-api
    name: Cloudmersive Currency API
    tags:
      - Currency
      - Exchange Rate
    humanURL: https://cloudmersive.com/currency-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Currency%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/currency
        type: OpenAPI
    description: Real-time currency exchange rates and conversions across major fiat and crypto currencies.
  - aid: cloudmersive:cloudmersive-config-api
    name: Cloudmersive Configuration API
    tags:
      - Configuration
      - Feature Flags
    humanURL: https://cloudmersive.com/config-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Config%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/config
        type: OpenAPI
    description: Hosted configuration management and feature flag service.
  - aid: cloudmersive:cloudmersive-data-integration-api
    name: Cloudmersive Data Integration API
    tags:
      - Data Integration
      - ETL
    humanURL: https://cloudmersive.com/data-integration-api
    properties:
      - url: https://api-console.cloudmersive.com/swagger/index.html?urls.primaryName=Data%20Integration%20API
        type: Documentation
      - url: https://api-console.cloudmersive.com/swagger/api/dataintegration
        type: OpenAPI
    description: Connect, transform, and integrate data across systems and file formats.
common:
  - type: Website
    url: https://cloudmersive.com/
  - type: Portal
    url: https://cloudmersive.com/developer
  - type: API Console
    url: https://api-console.cloudmersive.com/swagger/index.html
  - type: OpenAPI Index
    url: https://api.cloudmersive.com/openapi.asp
  - type: Privacy Policy
    url: https://cloudmersive.com/privacy-policy
  - type: JSON-LD
    url: json-ld/cloudmersive-context.jsonld
  - type: Spectral
    url: rules/cloudmersive-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cloudmersive-virus-scan-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
