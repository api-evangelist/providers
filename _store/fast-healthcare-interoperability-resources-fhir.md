---
aid: fast-healthcare-interoperability-resources-fhir
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/template.yml
apis:
  - aid: >-
      fast-healthcare-interoperability-resources-fhir:fast-healthcare-interoperability-resources-api
    name: US Core Server CapabilityStatement
    tags:
      - Healthcare
      - Standards
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.hl7.org/fhir/
    properties:
      - url: https://www.hl7.org/fhir/
        type: Documentation
      - url: properties/fhir-openapi-original.yml
        type: OpenAPI
      - url: >-
          https://www.postman.com/api-evangelist/fast-healthcare-interoperability-resources-fhir/collection/35240-f4ba6100-8f52-4e08-8071-afb9f06e2668
        type: PostmanCollection
    description: >-
      This Section describes the expected capabilities of the US Core Server
      actor which is responsible for providing responses to the queries
      submitted by the US Core Requestors. The complete list of FHIR profiles,
      RESTful operations, and search parameters supported by US Core Servers are
      defined. Systems implementing this capability statement should meet the
      ONC 2015 Common Clinical Data Set (CCDS) access requirement for Patient
      Selection 170.315(g)(7) and Application Access - Data Category Request
      170.315(g)(8) and the ONC [U.S. Core Data for Interoperability (USCDI)
      Version 4 July
      2023](https://www.healthit.gov/sites/isa/files/2023-07/Final-USCDI-Version-4-July-2023-Final.pdf).
name: Fast Healthcare Interoperability Resources (FHIR)
tags:
  - Healthcare
  - Standards
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: >-
      https://www.postman.com/api-evangelist/fast-healthcare-interoperability-resources-fhir/overview
    type: PostmanWorkspace
created: '2024-07-11'
modified: '2024-12-03'
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
position: Consumer
description: >-
  FHIR is a platform specification that defines a set of capabilities for use
  across the healthcare process, in all jurisdictions, and in lots of different
  contexts. While the basics of the FHIR specification are relatively
  straight-forward (see the Overviews: General, Developers, Clinical, and
  Architects), it can still be difficult to know where to start when
  implementing a solution based on FHIR.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---