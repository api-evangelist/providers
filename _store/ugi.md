---
aid: ugi
url: https://raw.githubusercontent.com/api-evangelist/ugi/refs/heads/main/apis.yml
name: UGI Corporation
description: 'UGI Corporation is a Fortune 500 international energy distribution and services company headquartered in King of Prussia, Pennsylvania. UGI distributes natural gas, liquid propane, and electricity primarily through four business segments: UGI Utilities (natural gas and electric distribution in Pennsylvania), AmeriGas Propane (largest US propane marketer), Midstream and Marketing, and UGI International (European energy distribution). No public developer API has been identified; the company primarily uses EDI and utility industry standards for B2B data exchange.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-03'
modified: '2026-05-03'
position: Consumer
tags:
  - Energy
  - Utilities
  - Natural Gas
  - Propane
  - Electric
  - Fortune 500
  - Pennsylvania
apis:
  - aid: ugi:ugi-utilities
    name: UGI Utilities
    description: UGI Utilities provides natural gas and electric distribution services to approximately 700,000 customers in 45 counties in Pennsylvania and one county in Maryland. Residential and commercial customers can manage accounts online, start or stop service, pay bills, and enroll in energy assistance programs. No public REST API documented.
    humanURL: https://www.ugi.com
    tags:
      - Natural Gas
      - Electric
      - Utilities
      - Pennsylvania
      - Energy Distribution
    properties:
      - type: Website
        url: https://www.ugi.com
      - type: Support
        url: https://www.ugi.com/contact-us/
      - type: Documentation
        url: https://www.ugi.com/for-your-business/
  - aid: ugi:amerigas
    name: AmeriGas Propane
    description: AmeriGas is the largest retail propane marketer in the United States, serving approximately 1.5 million residential, commercial, industrial, and agricultural customers across all 50 states. A wholly-owned subsidiary of UGI Corporation. Limited public API access; propane delivery ordering and account management available via web portal.
    humanURL: https://www.amerigas.com
    tags:
      - Propane
      - Energy
      - Retail
      - Distribution
      - Delivery
    properties:
      - type: Website
        url: https://www.amerigas.com
      - type: Support
        url: https://www.amerigas.com/contact-us
  - aid: ugi:ugi-energy-services
    name: UGI Energy Services
    description: UGI Energy Services (UGIES) is a competitive natural gas and electricity supplier and midstream service provider for commercial and industrial customers in the northeastern United States. Offers energy procurement, supply, and management services.
    humanURL: https://ugies.com
    tags:
      - Natural Gas
      - Electricity
      - Energy Services
      - Commercial
      - Industrial
    properties:
      - type: Website
        url: https://ugies.com
      - type: Support
        url: https://ugies.com/contact/
  - aid: ugi:ugi-international
    name: UGI International
    description: UGI International manages LPG and natural gas distribution operations across Europe, primarily through Flaga, AvantiGas, and other regional brands serving 17 European countries with liquid petroleum gas distribution and energy services.
    humanURL: https://www.ugicorp.com/company/our-businesses/ugi-international/
    tags:
      - LPG
      - Natural Gas
      - Europe
      - International
      - Energy Distribution
    properties:
      - type: Website
        url: https://www.ugicorp.com/company/our-businesses/ugi-international/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
properties:
  - url: vocabulary/ugi-vocabulary.yml
    type: Vocabulary
  - url: json-ld/ugi-context.jsonld
    type: JSONLDContext
  - url: json-schema/ugi-energy-account-schema.json
    type: JSONSchema
---
