---
aid: jpa
name: JPA
description: Jakarta Persistence (formerly Java Persistence API / JPA) defines a Java specification and binding layer for the management of persistence and object-relational mapping in Java environments. It provides a standardized ORM framework that enables developers to map Java objects to database tables and interact with relational data using Java rather than SQL. Jakarta Persistence 3.2 is the current stable release with Jakarta EE 11, while version 4.0 is under development for Jakarta EE 12.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Database
  - Java
  - JPA
  - Jakarta EE
  - ORM
  - Persistence
url: https://raw.githubusercontent.com/api-evangelist/jpa/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jpa:jpa
    name: Jakarta Persistence API
    description: The Jakarta Persistence specification for object-relational mapping in Java applications, defining annotations, entity managers, queries via JPQL and the Criteria API, and lifecycle callbacks for managing persistent state across compatible implementations.
    humanURL: https://jakarta.ee/specifications/persistence/
    tags:
      - Database
      - Java
      - ORM
    properties:
      - type: Documentation
        url: https://jakarta.ee/specifications/persistence/
      - type: Specification
        url: https://jakarta.ee/specifications/persistence/3.2/
common:
  - type: Website
    url: https://jakarta.ee/specifications/persistence/
  - type: Documentation
    url: https://jakarta.ee/specifications/persistence/
  - type: GitHub Organization
    url: https://github.com/jakartaee/persistence
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
