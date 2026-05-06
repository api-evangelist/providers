---
aid: us-foods
url: https://raw.githubusercontent.com/api-evangelist/us-foods/refs/heads/main/apis.yml
apis:
  - aid: us-foods:moxe-ordering-platform
    name: US Foods MOXe eCommerce Platform
    tags:
      - Food Service
      - Ordering
      - eCommerce
      - Foodservice Distribution
    humanURL: https://www.usfoods.com/our-services/easy-ordering.html
    properties:
      - url: https://www.usfoods.com/our-services/easy-ordering.html
        type: Documentation
    description: US Foods MOXe is a comprehensive foodservice eCommerce platform enabling restaurants, healthcare facilities, and institutional customers to place orders, manage inventory, track deliveries, and pay invoices. The platform uses AI-powered product search, image ordering, and menu profitability analysis (Menu IQ). Integration with third-party systems is available via EDI and partner connectors.
  - aid: us-foods:edi-integration
    name: US Foods EDI Integration
    tags:
      - EDI
      - Supply Chain
      - Integration
      - B2B
    humanURL: https://www.cleo.com/trading-partner-network/us-foods
    properties:
      - url: https://www.cleo.com/trading-partner-network/us-foods
        type: Documentation
      - url: https://www.spscommerce.com/network/find-a-partner/view/us-foods/
        type: Documentation
    description: US Foods supports electronic data interchange (EDI) for B2B integration with suppliers and trading partners. EDI transactions support purchase orders, invoices, advance ship notices, and product catalog synchronization following GS1 standards and US Foods' trading partner compliance requirements.
  - aid: us-foods:supplier-pim-api
    name: US Foods Supplier Product Information Management
    tags:
      - Product Data
      - Supplier Integration
      - Data Sync
      - Food Safety
    humanURL: https://www.usfoods.com/supplier-info.html
    properties:
      - url: https://www.usfoods.com/supplier-info.html
        type: Documentation
    description: US Foods' Product Information Management (PIM) system allows suppliers to provide updated product information including ingredient statements, allergen data, nutritional information, and product images. Suppliers synchronize data using GS1 Global Data Synchronization Network (GDSN) standards to ensure accurate product information across US Foods' ordering and fulfillment systems.
name: US Foods
tags:
  - Food Service
  - Fortune 500
  - Distribution
  - Supply Chain
  - eCommerce
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: US Foods is one of the largest foodservice distributors in the United States, serving restaurants, healthcare facilities, hospitality businesses, government institutions, and educational facilities. As a Fortune 500 company, US Foods operates a national distribution network with over 70 distribution centers and serves approximately 250,000 customers. The company's digital platform includes the MOXe eCommerce application for ordering and business management, EDI integration for B2B transactions, and a supplier PIM system for product data synchronization. US Foods has undergone significant digital transformation building a data mesh architecture on Apache Kafka, MongoDB, and cloud platforms to support its eCommerce and supply chain operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
