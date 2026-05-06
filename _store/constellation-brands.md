---
aid: constellation-brands
name: Constellation Brands
url: https://raw.githubusercontent.com/api-evangelist/constellation-brands/refs/heads/main/apis.yml
tags:
  - Alcohol
  - Beer
  - Beverages
  - Digital Assets
  - Fortune 500
  - Spirits
  - Wine
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-21'
modified: '2026-04-29'
position: Consumer
specificationVersion: '0.19'
x-type: company
description: Constellation Brands is a Fortune 500 producer and marketer of beer, wine, and spirits brands such as Corona, Modelo, Robert Mondavi, and Casa Noble. Constellation publishes a partner-oriented API catalog at dev.cbrands.com that exposes product, brand, and digital-asset data (bottle shots, tasting notes, hot sheets, shelf talkers, neck hangers, recipes, and an items product API) to distributors, retailers, and on-premise partners. Most endpoints require an API key issued through the developer registration process.
apis:
  - aid: constellation-brands:product
    name: Product Items API
    tags:
      - Catalog
      - Items
      - Products
    humanURL: https://dev.cbrands.com/docs/
    baseURL: https://api.cbrands.com/v3
    properties:
      - url: https://dev.cbrands.com/docs/
        type: Documentation
    description: Provides item-level product master data including SKU identifiers, descriptions, varietal and category metadata, and pointers to digital assets. Used by partners to keep distributor and retailer catalogs in sync with Constellation's source-of-truth data.
  - aid: constellation-brands:bottle-shots
    name: Bottle Shots API
    tags:
      - Bottle Shots
      - Digital Assets
      - Images
    humanURL: https://dev.cbrands.com/docs/
    baseURL: https://api.cbrands.com/api/1.0
    properties:
      - url: https://dev.cbrands.com/docs/
        type: Documentation
    description: Returns promotional bottle-shot imagery for Constellation Brands products in multiple formats (PNG, JPG) and resolutions for use on partner sites, e-commerce experiences, and printed materials.
  - aid: constellation-brands:tasting-notes
    name: Tasting Notes API
    tags:
      - Documents
      - Tasting Notes
      - Wine
    humanURL: https://dev.cbrands.com/docs/
    baseURL: https://api.cbrands.com/api/1.0
    properties:
      - url: https://dev.cbrands.com/docs/
        type: Documentation
    description: Retrieves tasting-note documents for wine and spirits brands so partners can render or print structured tasting copy alongside bottle shots and pricing.
  - aid: constellation-brands:hot-sheets
    name: Hot Sheets API
    tags:
      - Awards
      - Documents
      - Reviews
    humanURL: https://dev.cbrands.com/docs/
    baseURL: https://api.cbrands.com/api/1.0
    properties:
      - url: https://dev.cbrands.com/docs/
        type: Documentation
    description: Delivers "hot sheets" containing critical-review scores, awards, and promotional copy that distributors use to merchandise Constellation brands at retail.
  - aid: constellation-brands:shelf-talkers
    name: Shelf Talkers API
    tags:
      - Merchandising
      - POS
      - Retail
    humanURL: https://dev.cbrands.com/docs/
    baseURL: https://api.cbrands.com/api/1.0
    properties:
      - url: https://dev.cbrands.com/docs/
        type: Documentation
    description: Provides point-of-sale shelf-talker artwork keyed to specific products and promotional periods.
  - aid: constellation-brands:neck-hangers
    name: Neck Hangers API
    tags:
      - Merchandising
      - POS
      - Retail
    humanURL: https://dev.cbrands.com/docs/
    baseURL: https://api.cbrands.com/api/1.0
    properties:
      - url: https://dev.cbrands.com/docs/
        type: Documentation
    description: Returns neck-hanger artwork that distributors and retailers attach to bottles for in-store merchandising and promotions.
  - aid: constellation-brands:recipes
    name: Recipes API
    tags:
      - Cocktails
      - Recipes
    humanURL: https://dev.cbrands.com/docs/
    baseURL: https://api.cbrands.com/api/1.0
    properties:
      - url: https://dev.cbrands.com/docs/
        type: Documentation
    description: Supplies cocktail and beverage recipes featuring Constellation brands so on-premise partners and digital experiences can surface branded drink ideas.
common:
  - type: Website
    url: https://www.cbrands.com/
  - type: Developer Portal
    url: https://dev.cbrands.com/docs/
  - type: GitHub Organization
    url: https://github.com/ConstellationBrands
  - type: Investor Relations
    url: https://ir.cbrands.com/
  - type: Careers
    url: https://careers.cbrands.com/
  - type: Privacy Policy
    url: https://www.cbrands.com/privacy-notice
  - type: Terms of Service
    url: https://www.cbrands.com/terms-of-use
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
