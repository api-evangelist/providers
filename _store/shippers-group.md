---
aid: shippers-group
name: The Shippers Group
description: The Shippers Group is a leading national third-party logistics (3PL) company headquartered in Dallas, Texas. Founded in 1901, the company provides warehousing, co-packaging, fulfillment, and transportation management services across 12 locations totaling over 5 million square feet of space. The Shippers Group serves brand leaders and market innovators in industries including food, consumer packaged goods, and retail. The company was acquired by Kenco Group in December 2023. Client integrations are handled via EDI connections and logistics technology partnerships with warehouse management systems and transportation management systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Third-Party Logistics
  - Warehousing
  - Fulfillment
  - Supply Chain
  - Transportation Management
  - Co-Packaging
  - Consumer Packaged Goods
url: https://raw.githubusercontent.com/api-evangelist/shippers-group/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: shippers-group:shippers-group-logistics
    name: The Shippers Group Logistics Operations
    description: The Shippers Group provides third-party logistics services including warehousing, co-packaging, fulfillment, and transportation management. As a national 3PL provider operating across 12 US locations, the company manages supply chain operations for consumer packaged goods, food, and retail brands. Client integrations are handled through established EDI connections and logistics technology partnerships. No public developer API is currently available; all integrations are conducted via EDI (850, 856, 810 transaction sets) and WMS/TMS integration agreements.
    humanURL: https://www.theshippersgroup.com/
    tags:
      - Third-Party Logistics
      - Warehousing
      - Fulfillment
      - Supply Chain
      - Co-Packaging
    properties:
      - type: Documentation
        url: https://www.theshippersgroup.com/services/
      - type: Website
        url: https://www.theshippersgroup.com/
  - aid: shippers-group:kenco-group
    name: Kenco Group (Parent Company)
    description: Kenco Group acquired The Shippers Group in December 2023. Kenco is a leading 3PL provider offering warehousing, distribution, transportation management, and material handling equipment services. Kenco's technology platform includes WMS, TMS, and analytics capabilities that now extend to Shippers Group operations.
    humanURL: https://www.kencogroup.com/
    tags:
      - Third-Party Logistics
      - Warehousing
      - Distribution
      - Supply Chain
    properties:
      - type: Website
        url: https://www.kencogroup.com/
      - type: Documentation
        url: https://www.kencogroup.com/services/
common:
  - type: Website
    url: https://www.theshippersgroup.com/
  - type: Services
    url: https://www.theshippersgroup.com/services/
  - type: WarehousingServices
    url: https://www.theshippersgroup.com/services/warehousing/
  - type: FulfillmentServices
    url: https://www.theshippersgroup.com/services/fulfillment/
  - type: CoPackagingServices
    url: https://www.theshippersgroup.com/services/co-packaging/
  - type: TransportationServices
    url: https://www.theshippersgroup.com/services/transportation/
  - type: ParentCompany
    url: https://www.kencogroup.com/
  - type: LinkedIn
    url: https://www.linkedin.com/company/the-shippers-group/
  - type: JSONSchema
    url: json-schema/shippers-group-warehouse-schema.json
  - type: JSONStructure
    url: json-structure/shippers-group-warehouse-structure.json
  - type: JSONLDContext
    url: json-ld/shippers-group-context.jsonld
  - type: Examples
    url: examples/shippers-group-warehouse-example.json
  - type: Vocabulary
    url: vocabulary/shippers-group-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
