---
aid: spring-cloud-config
name: Spring Cloud Config
description: Spring Cloud Config provides server-side and client-side support for externalized configuration in a distributed system. It offers a central place to manage external properties for applications across all environments, backed by Git, SVN, or filesystem repositories with support for encryption, decryption, and runtime refresh.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://spring.io/projects/spring-cloud-config
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Configuration Management
  - Distributed Systems
  - Externalized Configuration
  - Git
  - Java
  - Microservices
  - Spring
  - Spring Cloud
apis:
  - aid: spring-cloud-config:spring-cloud-config-server
    name: Spring Cloud Config Server API
    description: HTTP resource-based API for external configuration management. Serves property sources organized by application name, profile, and label (git branch/tag). Supports JSON, YAML, and Java properties formats plus encryption/decryption and webhook-triggered refresh notifications.
    humanURL: https://spring.io/projects/spring-cloud-config
    baseURL: http://localhost:8888
    tags:
      - Configuration
      - Configuration Management
      - Distributed Systems
      - Encryption
      - Externalized Configuration
      - Git
      - Microservices
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository.html
      - type: OpenAPI
        url: openapi/spring-cloud-config-server-api.yml
      - type: JSONSchema
        url: json-schema/spring-cloud-config-environment-schema.json
      - type: JSONSchema
        url: json-schema/spring-cloud-config-server-configuration-schema.json
      - type: JSONStructure
        url: json-structure/spring-cloud-config-environment-structure.json
      - type: JSONLDContext
        url: json-ld/spring-cloud-config-context.jsonld
      - type: SpectralRules
        url: rules/spring-cloud-config-rules.yml
      - type: NaftikoCapability
        url: capabilities/configuration-management.yaml
common:
  - type: Website
    url: https://spring.io/projects/spring-cloud-config
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-config/reference/
  - type: Getting Started
    url: https://spring.io/guides/gs/centralized-configuration/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-config
  - type: GitHub Organization
    url: https://github.com/spring-cloud
  - type: Issues
    url: https://github.com/spring-cloud/spring-cloud-config/issues
  - type: Releases
    url: https://github.com/spring-cloud/spring-cloud-config/releases
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-cloud-config
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-config-server
  - type: Vocabulary
    url: vocabulary/spring-cloud-config-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
