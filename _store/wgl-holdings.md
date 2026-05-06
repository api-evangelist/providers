---
aid: wgl-holdings
name: WGL Holdings
description: WGL Holdings was an integrated energy holding company headquartered in Washington, D.C., serving over 1 million customers across the District of Columbia, Maryland, and Virginia. Its operations spanned regulated natural gas distribution (Washington Gas), retail energy marketing (WGL Energy Services), commercial energy systems, and midstream energy services (WGL Midstream, Hampshire Gas). WGL Holdings was acquired by AltaGas on July 6, 2018, and continues to operate as a subsidiary.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Natural Gas
  - Utilities
  - Electricity
  - Retail Energy
  - Midstream
url: https://raw.githubusercontent.com/api-evangelist/wgl-holdings/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: wgl-holdings:washington-gas
    name: Washington Gas
    description: Washington Gas is the regulated natural gas distribution utility subsidiary of WGL Holdings, providing safe, reliable, and affordable natural gas to more than 1.2 million customers in the District of Columbia, Maryland, and Virginia. It is one of the oldest gas utilities in the United States, founded in 1848.
    humanURL: https://www.washingtongas.com
    tags:
      - Natural Gas
      - Utilities
      - Regulated
      - Distribution
    properties:
      - type: Website
        url: https://www.washingtongas.com
      - type: Customer Portal
        url: https://www.washingtongas.com/my-account
      - type: Corporate Governance
        url: https://www.washingtongas.com/about/corporate-governance
      - type: Safety
        url: https://www.washingtongas.com/safety
  - aid: wgl-holdings:wgl-energy-services
    name: WGL Energy Services
    description: WGL Energy Services is an unregulated retail energy subsidiary of WGL Holdings that sells natural gas and electricity to commercial, industrial, and residential customers in Maryland, Virginia, Delaware, Pennsylvania, Ohio, D.C., and New Jersey. It also offers renewable energy products and carbon neutrality solutions.
    humanURL: https://www.wglenergy.com
    tags:
      - Retail Energy
      - Natural Gas
      - Electricity
      - Renewable Energy
      - Carbon Neutrality
    properties:
      - type: Website
        url: https://www.wglenergy.com
      - type: Customer Portal
        url: https://my.wges.com
      - type: Login
        url: https://one.wglenergy.com/dms/index.php
  - aid: wgl-holdings:wgl-midstream
    name: WGL Midstream
    description: WGL Midstream, Inc. is a subsidiary of Washington Gas Resources engaged in acquiring and optimizing natural gas storage and transportation assets. It focuses on midstream energy services including gas storage, pipeline capacity, and energy asset management.
    humanURL: https://www.wgl.com
    tags:
      - Midstream
      - Natural Gas Storage
      - Pipeline
      - Energy Assets
    properties:
      - type: Website
        url: https://www.wgl.com
  - aid: wgl-holdings:hampshire-gas
    name: Hampshire Gas
    description: Hampshire Gas Company owns and operates interests in natural gas storage facilities in and around Hampshire County, West Virginia. It provides underground natural gas storage services that support pipeline operations and supply reliability.
    humanURL: https://www.wgl.com
    tags:
      - Natural Gas Storage
      - Underground Storage
      - West Virginia
      - Pipeline
    properties:
      - type: Website
        url: https://www.wgl.com
common:
  - type: Website
    url: https://www.wglholdings.com
  - type: Parent Company
    url: https://www.altagas.ca
  - type: Washington Gas
    url: https://www.washingtongas.com
  - type: WGL Energy
    url: https://www.wglenergy.com
  - type: Sustainability
    url: https://sustainability.wglholdings.com
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/WGL_Holdings
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/wgl-holdings/refs/heads/main/vocabulary/wgl-holdings-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/wgl-holdings/refs/heads/main/json-ld/wgl-holdings-context.jsonld
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/wgl-holdings/refs/heads/main/json-schema/wgl-holdings-customer-account-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
