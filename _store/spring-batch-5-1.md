---
name: Spring Batch 5.1
description: Spring Batch 5.1 is the latest major release of the enterprise batch processing framework for the Spring ecosystem, providing reusable functions for processing large volumes of data including logging, transaction management, job processing statistics, job restart, skip, and resource management. Version 5.1 introduces Micrometer-based metrics, virtual thread support, and enhanced chunk-oriented processing with improved fault tolerance.
image: https://spring.io/img/projects/spring-batch.svg
url: https://spring.io/projects/spring-batch
type: opensource
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Batch Processing
  - Data Processing
  - Enterprise
  - ETL
  - Java
  - Job Scheduling
  - Spring Framework
apis:
  - name: Spring Batch 5.1 Core API
    description: Core framework API for Spring Batch 5.1 including job configuration, chunk-oriented processing, step execution, job repository, and fault tolerance features including retry and skip policies.
    image: https://spring.io/img/projects/spring-batch.svg
    humanURL: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/
    baseURL: https://github.com/spring-projects/spring-batch
    tags:
      - Batch Jobs
      - Chunk Processing
      - Job Repository
      - Step Execution
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/
      - type: API Documentation
        url: https://docs.spring.io/spring-batch/docs/5.1.x/api/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-batch
      - type: Getting Started Guide
        url: https://spring.io/guides/gs/batch-processing/
      - type: Reference Guide
        url: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/index-single.html
      - type: Samples
        url: https://github.com/spring-projects/spring-batch/tree/main/spring-batch-samples
      - type: Release Notes
        url: https://github.com/spring-projects/spring-batch/releases/tag/5.1.0
      - type: Maven Central
        url: https://mvnrepository.com/artifact/org.springframework.batch/spring-batch-core/5.1.0
      - type: Migration Guide
        url: https://github.com/spring-projects/spring-batch/wiki/Spring-Batch-5.0-Migration-Guide
      - type: Changelog
        url: https://github.com/spring-projects/spring-batch/blob/main/CHANGELOG.md
      - type: OpenAPI
        url: openapi/spring-batch-51-openapi.yml
      - type: Spectral Rules
        url: rules/spring-batch-51-rules.yml
  - name: Spring Batch 5.1 Infrastructure API
    description: Infrastructure components for Spring Batch including ItemReader, ItemWriter, ItemProcessor implementations for flat files, XML, JSON, JPA, JDBC, MongoDB, and remote chunking/partitioning support.
    humanURL: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/readersAndWriters.html
    baseURL: https://github.com/spring-projects/spring-batch
    tags:
      - Item Readers
      - Item Writers
      - JDBC
      - JPA
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/readersAndWriters.html
      - type: API Documentation
        url: https://docs.spring.io/spring-batch/docs/5.1.x/api/org/springframework/batch/item/package-summary.html
  - name: Spring Batch 5.1 Integration API
    description: Spring Batch integration with Spring Integration for remote partitioning, remote chunking, and message-driven batch processing.
    humanURL: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/spring-batch-integration.html
    baseURL: https://github.com/spring-projects/spring-batch
    tags:
      - Integration
      - Messaging
      - Remote Chunking
      - Remote Partitioning
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/spring-batch-integration.html
maintainers:
  - name: Spring Team
    email: spring-batch@broadcom.com
    url: https://spring.io/team
  - FN: Mahmoud Ben Hassine
    X-github: mminella
common:
  - type: Blog
    url: https://spring.io/blog/category/spring-batch
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-batch
  - type: GitHub Issues
    url: https://github.com/spring-projects/spring-batch/issues
  - type: GitHub Discussions
    url: https://github.com/spring-projects/spring-batch/discussions
  - type: License
    url: https://github.com/spring-projects/spring-batch/blob/main/LICENSE
  - type: Contributing Guidelines
    url: https://github.com/spring-projects/spring-batch/blob/main/CONTRIBUTING.md
  - type: Security Policy
    url: https://github.com/spring-projects/spring-batch/security/policy
  - type: Maven Central
    url: https://search.maven.org/search?q=g:org.springframework.batch
include:
  - name: Spring Framework
    url: https://spring.io/projects/spring-framework
  - name: Spring Boot
    url: https://spring.io/projects/spring-boot
  - name: Spring Integration
    url: https://spring.io/projects/spring-integration
---
