---
aid: belk
name: Belk
url: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
description: Belk is a privately-held American department store chain headquartered in Charlotte, North Carolina, serving the southeastern United States. The company sells clothing, handbags, jewelry, beauty products, and home goods. Belk operates an omnichannel retail model with physical stores and an online marketplace. Supplier and marketplace integrations are handled via EDI through value-added networks, with order management integration available through Rithum (formerly CommerceHub) and other channel management platforms.
tags:
  - Apparel
  - Beauty
  - Department Store
  - E-Commerce
  - Fashion
  - Home Goods
  - Jewelry
  - Marketplace
  - Retail
  - Southeastern US
apis: []
common:
  - type: Website
    url: https://www.belk.com
  - type: Portal
    url: https://www.belk.com/vendor-portal
    title: Vendor Portal
  - type: Features
    data:
      - name: Omnichannel Retail
        description: Belk operates physical stores across the southeastern United States alongside an online retail and marketplace presence at belk.com.
      - name: Marketplace Seller Program
        description: Third-party vendors can list and sell products on Belk.com through the marketplace program, integrated via Rithum (formerly CommerceHub) channel management platform.
      - name: EDI Supplier Integration
        description: Belk uses X12 EDI version 4030 for supplier integration, transmitted through value-added networks (VANs). Required documents include EDI 850 purchase orders, EDI 856 advance ship notices, and EDI 846 inventory feeds.
      - name: Vendor Portal
        description: Belk's vendor portal provides document specifications, EDI information, and vendor FAQ resources for suppliers to configure EDI integrations.
  - type: Integrations
    data:
      - name: Rithum (CommerceHub)
        description: Rithum, formerly CommerceHub, is the primary integration platform for Belk marketplace sellers to manage orders, inventory, and fulfillment.
      - name: Sellercloud
        description: Sellercloud supports Belk account integration through Rithum for omnichannel ecommerce order management and inventory synchronization.
      - name: Alloy.ai
        description: Alloy.ai provides a Belk retailer portal integration for demand forecasting and retail analytics based on Belk point-of-sale data.
      - name: Tradeshift
        description: Tradeshift supports Belk supplier invoice and procurement document exchange through its B2B network integration.
      - name: ConnectPointz
        description: ConnectPointz provides EDI compliance and channel management integration for Belk marketplace and supplier connections.
  - type: UseCases
    data:
      - name: Marketplace Selling
        description: Third-party vendors integrate with the Belk marketplace to list products, receive orders, and manage fulfillment through approved channel platforms.
      - name: EDI Supplier Compliance
        description: Manufacturers and distributors connect to Belk's EDI network to exchange purchase orders, advance ship notices, and inventory feeds in X12 format.
      - name: Retail Analytics
        description: Retail suppliers and analytics platforms consume Belk point-of-sale data through retail portal integrations for demand planning and replenishment.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
