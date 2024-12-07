---
aid: fast-healthcare-interoperability-resources-fhir
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/template.yml
apis:
  - aid: >-
      fast-healthcare-interoperability-resources-fhir:fast-healthcare-interoperability-resources-api
    name: Fast Healthcare Interoperability Resources API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.hl7.org/fhir/
    properties:
      - url: https://www.hl7.org/fhir/
        type: Documentation
      - url: properties/fhir-openapi-original.yml
        type: OpenAPI
    description: >-
      FHIR is a platform specification that defines a set of capabilities for
      use across the healthcare process, in all jurisdictions, and in lots of
      different contexts. While the basics of the FHIR specification are
      relatively straight-forward (see the Overviews: General, Developers,
      Clinical, and Architects), it can still be difficult to know where to
      start when implementing a solution based on FHIR.
name: Fast Healthcare Interoperability Resources (FHIR)
tags:
  - Healthcare
  - Standards
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://example.com
    type: Property
created: '2024-07-11T00:00:00.000Z'
modified: '2024-11-14'
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