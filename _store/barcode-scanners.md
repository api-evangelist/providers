---
aid: barcode-scanners
name: Barcode Scanners
description: Barcode scanning technology and APIs for scanning, generating, and looking up barcode data including UPC, EAN, ISBN, QR codes, Code 128, Code 39, and other barcode formats used in retail, logistics, inventory management, and supply chain operations. This index covers barcode lookup APIs, barcode generation APIs, and scanning SDKs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Barcodes
  - Inventory
  - Product Lookup
  - QR Codes
  - Retail
  - Scanning
  - Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/barcode-scanners/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: barcode-scanners:barcode-lookup-api
    name: Barcode Lookup API
    description: Retrieve product information by scanning or entering barcode numbers including UPC, EAN, and ISBN codes. Returns product name, description, category, images, and retail price data.
    humanURL: https://www.barcodelookup.com/api
    baseURL: https://api.barcodelookup.com/v3
    tags:
      - Barcodes
      - EAN
      - Product Lookup
      - UPC
    properties:
      - type: Documentation
        url: https://www.barcodelookup.com/api
  - aid: barcode-scanners:upcitemdb-api
    name: UPCitemdb API
    description: Free and commercial API for looking up product information using UPC, EAN, and other barcodes. Includes product names, descriptions, images, and pricing data.
    humanURL: https://www.upcitemdb.com/
    baseURL: https://api.upcitemdb.com/prod/trial
    tags:
      - Barcodes
      - EAN
      - Product Data
      - UPC
    properties:
      - type: Documentation
        url: https://www.upcitemdb.com/api/docs
  - aid: barcode-scanners:ean-search-api
    name: EAN-Search API
    description: Search and validate EAN-13, UPC-A, and ISBN codes with product information lookup and barcode validation services.
    humanURL: https://www.ean-search.org/
    tags:
      - Barcodes
      - EAN
      - ISBN
      - Product Search
      - UPC
    properties:
      - type: Documentation
        url: https://www.ean-search.org/ean-database-api.html
common:
  - type: Website
    url: https://www.barcodelookup.com/
    name: Barcode Lookup
  - type: Website
    url: https://www.upcitemdb.com/
    name: UPCitemdb
  - type: Website
    url: https://www.ean-search.org/
    name: EAN-Search
  - type: Vocabulary
    url: vocabulary/barcode-scanners-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/barcode-scanners-context.jsonld
  - name: Key Formats
    type: Features
    data:
      - name: UPC-A / UPC-E
        description: Universal Product Code for retail products in North America.
      - name: EAN-13 / EAN-8
        description: International Article Number for global retail products.
      - name: QR Code
        description: 2D matrix barcode for URLs, text, and structured data.
      - name: Code 128
        description: High-density linear barcode for logistics and shipping labels.
      - name: Code 39
        description: Alphanumeric barcode common in industrial and healthcare settings.
      - name: ISBN
        description: International Standard Book Number for books and publications.
      - name: Data Matrix
        description: 2D code for small items and pharmaceutical packaging.
      - name: PDF417
        description: Stacked linear barcode for driver's licenses and boarding passes.
  - name: Use Cases
    type: UseCases
    data:
      - name: Retail Product Lookup
        description: Scan UPC/EAN barcodes to retrieve product details for e-commerce and inventory.
      - name: Inventory Management
        description: Track stock levels and product movements using barcode scanning.
      - name: Supply Chain Tracking
        description: Monitor shipments and warehouse inventory via Code 128 and GS1 barcodes.
      - name: QR Code Marketing
        description: Generate QR codes for product packaging, ads, and digital campaigns.
      - name: Healthcare Asset Tracking
        description: Track medical equipment and medications with Code 39 and Data Matrix.
      - name: Document Management
        description: Index and retrieve documents using barcode labels.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
