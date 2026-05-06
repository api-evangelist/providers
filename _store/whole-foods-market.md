---
aid: whole-foods-market
name: Whole Foods Market
description: Whole Foods Market is an American multinational supermarket chain owned by Amazon, exclusively selling products free from hydrogenated fats and artificial colors, flavors, and preservatives. Acquired by Amazon in 2017, Whole Foods integrates with Amazon Prime for delivery, pickup, and member discounts. Supplier integrations are handled through EDI (Electronic Data Interchange) and the Whole Foods Supplier Portal.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Grocery
  - Supermarket
  - Organic
  - Natural Foods
  - Retail
  - Amazon
url: https://raw.githubusercontent.com/api-evangelist/whole-foods-market/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://www.wholefoodsmarket.com
  - type: ParentCompany
    url: https://www.amazon.com
  - type: SupplierPortal
    url: https://www.wholefoodsmarket.com/company-info/information-potential-suppliers
  - type: EDIIntegration
    url: https://www.stacksync.com/edi/whole-foods-market
  - type: VendorReportingPortal
    url: https://www.gocrisp.com/catalog/whole-foods-vendor-reporting-portal
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/Whole_Foods_Market
notes: Whole Foods Market does not offer a public developer API. Supplier integrations use EDI (Electronic Data Interchange) with document types including Purchase Orders (850), Invoices (810), Advanced Shipping Notices (856), and PO Acknowledgments (855). Consumer-facing digital services are powered by Amazon's platform.
artifacts:
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/whole-foods-market/main/json-schema/whole-foods-market-product-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/whole-foods-market/main/json-schema/whole-foods-market-edi-850-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/whole-foods-market/main/json-ld/whole-foods-market-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/whole-foods-market/main/vocabulary/whole-foods-market-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
