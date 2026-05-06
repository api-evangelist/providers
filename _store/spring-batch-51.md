---
name: Spring Batch 5.1
description: Spring Batch 5.1 is the latest enterprise batch processing framework release for the Spring ecosystem. Designed to enable development of robust batch applications vital for daily operations of enterprise systems. Version 5.1 delivers Micrometer metrics, virtual thread support (Java 21), and enhanced chunk-oriented processing with retry, skip, and restart capabilities.
image: https://spring.io/img/projects/spring-batch.svg
url: https://spring.io/projects/spring-batch
type: opensource
created: '2024-01-15'
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
    description: Core API for Spring Batch 5.1 providing batch processing capabilities including job and step configuration, chunk-oriented processing, job repository persistence, and fault tolerance.
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
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.batch/spring-batch-core/5.1.0
      - type: Stack Overflow
        url: https://stackoverflow.com/questions/tagged/spring-batch
      - type: License
        url: https://github.com/spring-projects/spring-batch/blob/main/LICENSE.txt
      - type: Issues
        url: https://github.com/spring-projects/spring-batch/issues
      - type: Sample Projects
        url: https://github.com/spring-projects/spring-batch/tree/main/spring-batch-samples
      - type: Release Notes
        url: https://github.com/spring-projects/spring-batch/releases
      - type: OpenAPI
        url: openapi/spring-batch-51-openapi.yml
      - type: Spectral Rules
        url: rules/spring-batch-51-rules.yml
  - name: Spring Batch 5.1 Actuator Monitoring
    description: Spring Boot Actuator-based monitoring endpoints for Spring Batch 5.1 applications providing job health, execution status, and Micrometer metrics visibility.
    humanURL: https://docs.spring.io/spring-boot/docs/3.2.x/actuator-api/htmlsingle/
    baseURL: http://localhost:8080/actuator
    tags:
      - Actuator
      - Health
      - Metrics
      - Monitoring
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/monitoring-and-metrics.html
maintainers:
  - FN: Spring Team
    email: spring-batch@vmware.com
    X-twitter: springcentral
    X-github: spring-projects
include:
  - name: Spring Batch Integration
    url: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/spring-batch-integration.html
  - name: Spring Batch Test
    url: https://docs.spring.io/spring-batch/docs/5.1.x/reference/html/testing.html
common:
  - type: Blog
    url: https://spring.io/blog/category/batch
  - type: Support
    url: https://spring.io/support
  - type: Forum
    url: https://stackoverflow.com/questions/tagged/spring-batch
  - type: GitHub Issues
    url: https://github.com/spring-projects/spring-batch/issues
  - type: Maven Central
    url: https://search.maven.org/search?q=g:org.springframework.batch
---
