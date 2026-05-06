---
name: SOA
description: Service-Oriented Architecture (SOA) is an architectural style for building software applications as a collection of loosely coupled, interoperable services. Each service encapsulates a specific business capability and communicates with others through well-defined interfaces, commonly using SOAP, REST, or messaging protocols. SOA enables enterprise integration, reusability, and flexibility across heterogeneous systems.
url: https://raw.githubusercontent.com/api-evangelist/soa/refs/heads/main/apis.yml
tags:
  - SOA
  - Service-Oriented Architecture
  - Enterprise Integration
  - Web Services
  - SOAP
  - ESB
  - Microservices
  - API Design
created: '2025'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: soa:soa-governance
    name: SOA Governance and Registry
    description: Reference resources and tooling for SOA governance, service registries, and enterprise service management. Includes patterns for service discovery, versioning, SLA management, and policy enforcement in SOA environments.
    humanURL: https://en.wikipedia.org/wiki/Service-oriented_architecture
    tags:
      - SOA Governance
      - Service Registry
      - Enterprise Integration
      - Policy Management
    properties:
      - type: Documentation
        url: https://en.wikipedia.org/wiki/Service-oriented_architecture
      - type: Reference
        url: https://www.w3.org/TR/wsdl20/
common:
  - type: Reference Documentation
    url: https://en.wikipedia.org/wiki/Service-oriented_architecture
  - type: W3C SOAP Specification
    url: https://www.w3.org/TR/soap12/
  - type: W3C WSDL Specification
    url: https://www.w3.org/TR/wsdl20/
  - type: OASIS SOA Reference Model
    url: https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=soa-rm
  - type: JSON-LD Context
    url: json-ld/soa-context.jsonld
  - type: JSON Schema
    url: json-schema/soa-service-schema.json
  - type: JSON Structure
    url: json-structure/soa-service-structure.json
  - type: Vocabulary
    url: vocabulary/soa-vocabulary.yml
  - type: Examples
    url: examples/soa-service-registry-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
