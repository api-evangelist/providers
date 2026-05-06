---
aid: bed-bath-and-beyond
name: Bed Bath And Beyond
url: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
description: Bed Bath & Beyond was a chain of domestic merchandise retail stores selling home furnishings, bedding, kitchenware, and other home goods. The company filed for Chapter 11 bankruptcy in April 2023. The brand was subsequently acquired by Beyond Inc. (formerly Overstock.com), which relaunched Bed Bath & Beyond as an online retail destination. Beyond Inc. also owns Overstock, buybuy BABY, and related brands.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bedding
  - Beyond
  - E-Commerce
  - Home Goods
  - Kitchenware
  - Marketplace
  - Retail
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://www.bedbathandbeyond.com
  - type: Website
    url: https://www.beyond.com
    title: Beyond Inc. (Parent Company)
  - type: Marketplace
    url: https://help.bedbathandbeyond.com/help/s/article/Overstock-Marketplace
    title: Marketplace Seller Program
  - type: Features
    data:
      - name: Online Retail
        description: Bed Bath & Beyond operates as an online-only retail destination following the 2023 bankruptcy and brand acquisition by Beyond Inc.
      - name: Marketplace
        description: Third-party sellers can list products through the Bed Bath & Beyond marketplace, integrated via Rithum (formerly CommerceHub).
      - name: EDI Integration
        description: Supplier integrations use X12 EDI documents transmitted through value-added networks, including EDI 850 purchase orders, EDI 856 advance ship notices, and EDI 846 inventory feeds.
  - type: Integrations
    data:
      - name: Rithum (CommerceHub)
        description: Primary integration platform for marketplace sellers to connect inventory, orders, and shipment tracking with Bed Bath & Beyond.
      - name: Sellercloud
        description: Multi-channel ecommerce platform supporting Bed Bath & Beyond marketplace order management via API and EDI.
      - name: Dscopify (Supplier Oasis)
        description: Shopify and Supplier Oasis integration for connecting vendor catalogs with the Bed Bath & Beyond and Overstock marketplace channels.
  - type: UseCases
    data:
      - name: Marketplace Selling
        description: Third-party vendors can list and sell products on the Bed Bath & Beyond marketplace by integrating through approved channel management platforms.
      - name: Supplier Integration
        description: Suppliers submit catalog data, receive purchase orders, and send shipment notifications via EDI through the vendor portal.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
