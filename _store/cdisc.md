---
aid: cdisc
url: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/apis.yml
apis:
- aid: cdisc:cdisc-library-api
  name: CDISC Library API
  tags:
  - ADaM
  - Clinical Trials
  - Metadata
  - ODM
  - Pharma
  - SDTM
  - Standards
  image: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/image.png
  humanURL: https://www.cdisc.org/cdisc-library
  baseURL: https://library.cdisc.org/api
  properties:
  - url: https://www.cdisc.org/cdisc-library/api-documentation
    type: Documentation
  - url: https://api.developer.library.cdisc.org/api-details
    type: Reference
  - url: https://www.cdisc.org/cdisc-library/getting-started
    type: GettingStarted
  - url: https://api.developer.library.cdisc.org/
    type: Portal
  - url: https://wiki.cdisc.org/display/LIBSUPRT/How-to+articles
    type: KnowledgeBase
  - url: https://wiki.cdisc.org/display/LIBSUPRT/Release+Notes
    type: ChangeLog
  - url: https://jira.cdisc.org/servicedesk/customer/portal/2
    type: Support
  - url: https://library.cdisc.org/browser
    type: Explorer
  - url: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/openapi/cdisc-library-openapi.yml
    type: OpenAPI
  description: The CDISC Library API is a REST API that delivers CDISC standards metadata to software applications that automate standards-based processes. It uses linked data to provide access to SDTM, ADaM, and other clinical data standards. Responses are available in JSON, XML, ODM, CSV, and Excel formats. Access requires a CDISC Library account and an API key obtained from the CDISC Library API Management (APIM) Developer Portal.
- aid: cdisc:cdisc-core-api
  name: CDISC CORE (Checks and Rules Engine) API
  tags:
  - Clinical Trials
  - Conformance
  - Pharma
  - Rules
  - Validation
  image: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/image.png
  humanURL: https://www.cdisc.org/core
  baseURL: https://library.cdisc.org/api
  properties:
  - url: https://www.cdisc.org/core
    type: Documentation
  description: CDISC CORE (Checks and Rules Engine) is an open-source rules engine for validating clinical data against CDISC conformance rules. It enables automated validation of SDTM, ADaM, and other study data artifacts against published CDISC standards.
name: Cdisc
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: CDISC Library uses linked data and a REST API to deliver CDISC standards metadata to software applications that automate standards-based processes. CDISC Library provides access to new relationships between standards as well as a substantially increased number of versioned CDISC standards and controlled terminology packages.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

