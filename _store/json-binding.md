---
aid: json-binding
name: JSON Binding
description: Jakarta JSON Binding (JSON-B) defines a standard binding layer for converting Java objects to and from JSON documents. It specifies a default mapping algorithm for serializing and deserializing existing Java classes to and from JSON, while enabling developers to customize the mapping process through a Java API. JSON-B 3.0 is the stable release shipped with Jakarta EE 10, with version 3.1 under development for Jakarta EE 12.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Java
  - JSON
  - JSON Binding
  - Jakarta EE
  - Serialization
url: https://raw.githubusercontent.com/api-evangelist/json-binding/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: json-binding:json-b
    name: Jakarta JSON Binding
    description: The Jakarta JSON Binding specification for marshaling Java objects to JSON and unmarshaling JSON back into Java objects. Provides a default mapping algorithm and customization through annotations and a runtime configuration API for consistent JSON binding across the Jakarta EE ecosystem.
    humanURL: https://jakarta.ee/specifications/jsonb/
    tags:
      - Java
      - JSON Binding
      - Serialization
    properties:
      - type: Documentation
        url: https://jakarta.ee/specifications/jsonb/
      - type: Specification
        url: https://jakarta.ee/specifications/jsonb/3.0/
common:
  - type: Website
    url: https://jakarta.ee/specifications/jsonb/
  - type: Documentation
    url: https://jakarta.ee/specifications/jsonb/
  - type: GitHub Organization
    url: https://github.com/jakartaee/jsonb-api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
