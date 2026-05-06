---
name: SOAP
description: SOAP (Simple Object Access Protocol) is an XML-based messaging protocol for exchanging structured information in web services, standardized by W3C as SOAP 1.2 (2003). It provides a platform-independent, language-neutral framework for web service communication with built-in standards for security (WS-Security), reliable messaging (WS-ReliableMessaging), and transactions (WS-Transaction). SOAP messages consist of an Envelope containing an optional Header and a required Body.
url: https://www.w3.org/TR/soap12/
tags:
  - SOAP
  - Messaging Protocol
  - Web Services
  - XML
  - W3C Standard
  - Enterprise Integration
  - WS-Star
created: '2025'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: soap:soap-protocol
    name: SOAP 1.2 Protocol
    description: SOAP Version 1.2 (W3C Recommendation, 2003/2007 Second Edition) is a lightweight protocol for exchanging structured information in a decentralized, distributed environment. It defines an XML message format with Envelope/Header/Body structure and a Fault mechanism for error handling.
    humanURL: https://www.w3.org/TR/soap12/
    tags:
      - SOAP
      - XML
      - Messaging Protocol
      - W3C Standard
    properties:
      - type: Specification
        url: https://www.w3.org/TR/soap12-part1/
      - type: Specification
        url: https://www.w3.org/TR/soap12-part2/
      - type: Adjuncts
        url: https://www.w3.org/TR/soap12-part2/
      - type: JSON Schema
        url: json-schema/soap-envelope.json
      - type: JSON Schema
        url: json-schema/soap-header.json
      - type: JSON Schema
        url: json-schema/soap-header-block.json
      - type: JSON Schema
        url: json-schema/soap-body.json
      - type: JSON Schema
        url: json-schema/soap-fault.json
      - type: JSON-LD Context
        url: json-ld/soap-context.jsonld
      - type: JSON Structure
        url: json-structure/soap-envelope-structure.json
      - type: Vocabulary
        url: vocabulary/soap-vocabulary.yml
      - type: Examples
        url: examples/soap-envelope-example.json
common:
  - type: W3C SOAP 1.2 Specification
    url: https://www.w3.org/TR/soap12-part1/
  - type: W3C SOAP 1.2 Adjuncts
    url: https://www.w3.org/TR/soap12-part2/
  - type: W3C SOAP Specifications Index
    url: https://www.w3.org/TR/soap/
  - type: SOAP 1.1 Note
    url: https://www.w3.org/TR/2000/NOTE-SOAP-20000508/
  - type: W3C XML Protocol Working Group
    url: https://www.w3.org/2000/xp/Group/
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/SOAP
  - type: JSON Schema
    url: json-schema/soap-envelope.json
  - type: JSON Schema
    url: json-schema/soap-header.json
  - type: JSON Schema
    url: json-schema/soap-body.json
  - type: JSON Schema
    url: json-schema/soap-fault.json
  - type: JSON-LD Context
    url: json-ld/soap-context.jsonld
  - type: Vocabulary
    url: vocabulary/soap-vocabulary.yml
---
