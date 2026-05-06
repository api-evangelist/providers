---
aid: vwr
url: https://raw.githubusercontent.com/api-evangelist/vwr/refs/heads/main/apis.yml
name: VWR International (Avantor)
description: VWR International, now part of Avantor, is a global distributor of laboratory supplies, chemicals, equipment, and services for the life sciences, pharmaceutical, biotechnology, and research industries. With over 180 years of history, VWR serves more than one million customers in over 30 countries. The company operates as Avantor's distribution and procurement platform, providing laboratory consumables, reagents, instruments, and cold chain solutions. VWR/Avantor offers e-procurement integrations and eProcurement APIs to support laboratory supply chain automation for enterprise customers through EDI, OCI/PunchOut, and catalog integration.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Distribution
  - Laboratory
  - Life Sciences
  - Procurement
  - Scientific Supplies
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Contract
access: 3rd-Party
position: Consuming
apis:
  - aid: vwr:vwr-eprocurement-api
    name: VWR eProcurement Integration
    description: VWR's eProcurement integration supports OCI/PunchOut catalog connections and EDI order transmission for enterprise customers using procurement platforms like SAP Ariba, Coupa, Jaggaer, and Oracle Procurement Cloud. Enables automated purchase requisitions, order placement, and invoice processing for laboratory supplies.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://www.vwr.com/store/content/externalContentPage.jsp?path=/content/en_US/ordering-purchasing/eProcurement.jsp
    baseUrl: https://www.vwr.com
    tags:
      - EDI
      - eProcurement
      - Integration
      - Laboratory
      - Procurement
    properties:
      - type: Documentation
        url: https://www.vwr.com/store/content/externalContentPage.jsp?path=/content/en_US/ordering-purchasing/eProcurement.jsp
common:
  - url: https://www.vwr.com
    type: Website
  - url: https://us.vwr.com/store/
    type: Portal
  - url: https://www.avantorsciences.com/
    type: ParentCompany
  - url: https://www.vwr.com/store/content/externalContentPage.jsp?path=/content/en_US/ordering-purchasing/eProcurement.jsp
    type: Integration
  - url: vocabulary/vwr-vocabulary.yml
    type: Vocabulary
  - url: json-ld/vwr-context.jsonld
    type: JSONLDContext
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
