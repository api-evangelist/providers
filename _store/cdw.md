---
aid: cdw
url: https://raw.githubusercontent.com/api-evangelist/cdw/refs/heads/main/apis.yml
name: CDW
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - B2B
  - Catalog
  - eProcurement
  - IT Distribution
  - PunchOut
  - Technology
created: '2024-01-15'
modified: '2026-04-23'
specificationVersion: '0.19'
description: CDW is a leading multi-brand provider of information technology solutions to business, government, education, and healthcare customers. CDW offers eProcurement integration capabilities including a Catalog API, PunchOut (cXML/OCI), electronic purchase ordering, and electronic invoicing to enable procurement system integration with partners such as SAP Ariba, Coupa, Oracle, and Jaggaer.
apis:
  - aid: cdw:cdw-catalog-api
    name: CDW Catalog API
    tags:
      - Catalog
      - Inventory
      - Pricing
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cdw.com/content/cdw/en/services/eprocurement-and-custom-catalogs.html
    properties:
      - url: https://www.cdw.com/content/cdw/en/services/eprocurement-and-custom-catalogs.html
        type: Documentation
      - url: https://www.cdw.com/integrations/custompage/v2/6FB6697BBE2441968349584A24C5C459
        type: Overview
    description: The CDW Catalog API uses JSON to deliver customers real-time pricing and inventory status alongside any special pricing or catalog restrictions. It supports integration with eProcurement platforms for current product availability.
  - aid: cdw:cdw-eprocurement-api
    name: CDW eProcurement Integration
    tags:
      - EDI
      - eProcurement
      - PunchOut
      - cXML
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cdw.com/content/cdw/en/services/eprocurement-and-custom-catalogs.html
    properties:
      - url: https://www.cdw.com/content/cdw/en/services/eprocurement-and-custom-catalogs.html
        type: Documentation
    description: CDW eProcurement integration supports PunchOut and Roundtrip catalogs via cXML or OCI, electronic purchase order submission via cXML, EDI, or flat file, and electronic invoicing via XML or EDI. Orders can be submitted via HTTP, SFTP, API, and EDI connections.
common:
  - type: Website
    url: https://www.cdw.com
  - type: Documentation
    url: https://www.cdw.com/content/cdw/en/services/eprocurement-and-custom-catalogs.html
  - type: Overview
    url: https://www.cdw.com/integrations/custompage/v2/6FB6697BBE2441968349584A24C5C459
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
