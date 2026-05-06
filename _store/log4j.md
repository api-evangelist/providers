---
aid: log4j
name: Apache Log4j
description: Apache Log4j is a versatile, industrial-grade Java logging framework composed of an API, its implementation, and components to assist deployment for various use cases. It is part of the Apache Logging Services project. Log4j is a Java library distributed as Maven artifacts and is consumed via its Java API rather than over the network; no public HTTP/REST surface is published.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Debugging
  - Java
  - Library
  - Logging
  - Monitoring
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/log4j/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: log4j:log4j-api
    name: Log4j API
    description: The logging facade providing a feature-rich Java interface for application logging. Applications code against this stable API while delegating to a backing implementation such as Log4j Core.
    humanURL: https://logging.apache.org/log4j/2.x/manual/api.html
    tags:
      - API
      - Facade
      - Java
      - Logging
    properties:
      - type: Documentation
        url: https://logging.apache.org/log4j/2.x/manual/api.html
      - type: Reference
        url: https://logging.apache.org/log4j/2.x/javadoc.html
      - type: SourceCode
        url: https://github.com/apache/logging-log4j2
  - aid: log4j:log4j-core
    name: Log4j Core
    description: The reference implementation of the Log4j API providing appenders, layouts, filters, lookups and configuration that route log events to consoles, files, databases, network endpoints and more.
    humanURL: https://logging.apache.org/log4j/2.x/manual/configuration.html
    tags:
      - Core
      - Implementation
      - Java
      - Logging
    properties:
      - type: Documentation
        url: https://logging.apache.org/log4j/2.x/manual/configuration.html
      - type: Reference
        url: https://logging.apache.org/log4j/2.x/javadoc.html
      - type: SourceCode
        url: https://github.com/apache/logging-log4j2
common:
  - type: Website
    url: https://logging.apache.org/log4j/2.x/
  - type: Documentation
    url: https://logging.apache.org/log4j/2.x/manual/
  - type: GettingStarted
    url: https://logging.apache.org/log4j/2.x/manual/getting-started.html
  - type: Security
    url: https://logging.apache.org/security.html
  - type: ReleaseNotes
    url: https://logging.apache.org/log4j/2.x/release-notes.html
  - type: Performance
    url: https://logging.apache.org/log4j/2.x/performance.html
  - type: SourceCode
    url: https://github.com/apache/logging-log4j2
  - type: License
    url: https://www.apache.org/licenses/LICENSE-2.0
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
