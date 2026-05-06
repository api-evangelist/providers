---
aid: junit
name: JUnit
description: 'JUnit is a programmer-friendly testing framework for Java and the JVM. JUnit 5 is the next generation of JUnit, composed of three modules: JUnit Platform, JUnit Jupiter, and JUnit Vintage.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Java
  - TDD
  - Test Automation
  - Testing
  - Unit Testing
url: https://raw.githubusercontent.com/api-evangelist/junit/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: junit:junit5
    name: JUnit 5 Jupiter
    description: The next generation of JUnit for Java 8 and beyond, providing an expressive API for writing tests and extensions.
    humanURL: https://junit.org/junit5/
    tags:
      - Java
      - Testing
    properties:
      - type: Documentation
        url: https://junit.org/junit5/docs/current/user-guide/
      - type: Reference
        url: https://junit.org/junit5/docs/current/api/
      - type: Getting Started
        url: https://junit.org/junit5/docs/current/user-guide/#overview-getting-started
      - type: Change Log
        url: https://junit.org/junit5/docs/current/release-notes/
      - type: GitHub
        url: https://github.com/junit-team/junit5
      - type: JSONSchema
        url: json-schema/junit-report-schema.json
  - aid: junit:junit4
    name: JUnit 4 Vintage
    description: The legacy version of JUnit still widely used in Java projects.
    humanURL: https://junit.org/junit4/
    tags:
      - Java
      - Testing
    properties:
      - type: Documentation
        url: https://junit.org/junit4/
      - type: Reference
        url: https://junit.org/junit4/javadoc/latest/
      - type: GitHub
        url: https://github.com/junit-team/junit4
common:
  - type: Website
    url: https://junit.org/junit5/
  - type: Documentation
    url: https://junit.org/junit5/docs/current/user-guide/
  - type: GitHub Organization
    url: https://github.com/junit-team
  - type: License
    url: https://github.com/junit-team/junit5/blob/main/LICENSE.md
  - type: JSON-LD
    url: json-ld/junit-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
